from unittest import TestCase

from cli_color_py.color import Color
from cli_color_py.color import Attributes
from cli_color_py import (
    black,
    red,
    green,
    yellow,
    blue,
    magenta,
    cyan,
    white,
    bright_red,
    bright_green,
    bright_yellow,
    bright_blue,
    bright_magenta,
    bright_cyan,
    reset,
    bold,
    underline,
    blink,
    create_formatter,
)


class TestCliColor(TestCase):
    def test_cli_color_colors(self):
        cases = [
            (30, black),
            (31, red),
            (32, green),
            (33, yellow),
            (34, blue),
            (35, magenta),
            (36, cyan),
            (37, white),
            (91, bright_red),
            (92, bright_green),
            (93, bright_yellow),
            (94, bright_blue),
            (95, bright_magenta),
            (96, bright_cyan),
        ]
        for color, fn in cases:
            self.assertEqual(f"\x1b[{color}mtest\x1b[0m", fn("test"))
            self.assertEqual(f"\x1b[{color+10}mtest\x1b[0m", fn("test", bg=True))

    def test_cli_color_attrs(self):
        cases = [
            (1, bold),
            (4, underline),
            (5, blink),
        ]
        for attr, fn in cases:
            self.assertEqual(f"\x1b[{attr}mtest\x1b[0m", fn("test"))
        self.assertEqual("\x1b[0m", reset())

    def test_cli_color_combining(self):
        self.assertEqual("\x1b[5m\x1b[31mtest\x1b[0m", blink(red("test")))

    def test_cli_color_color(self):
        self.assertEqual(36, Color.CYAN)
        self.assertEqual("\x1b[36m", Color.CYAN.default())
        self.assertEqual("\x1b[46m", Color.CYAN.background())

    def test_formatter(self):
        formatter1 = create_formatter(
            "{yellow}TEST{reset}: {bright_red_bg}{0}{reset} [{cyan}{1}{reset}]"
        )
        self.assertEqual(
            "\x1b[33mTEST\x1b[0m: \x1b[101mtest\x1b[0m [\x1b[36mnow\x1b[0m]",
            formatter1("test", "now"),
        )
        formatter2 = create_formatter(
            "{yellow}TEST{reset}: {msg} [{cyan}{datetime}{reset}]"
        )
        self.assertEqual(
            "\x1b[33mTEST\x1b[0m: test [\x1b[36mnow\x1b[0m]",
            formatter2(msg="test", datetime="now"),
        )

    def test_as_format(self):
        c_fmt = Color.as_format()
        self.assertTrue("cyan" in c_fmt)
        self.assertTrue("bright_cyan_bg" in c_fmt)
        self.assertEqual("\x1b[36m", c_fmt["cyan"])
        self.assertEqual("\x1b[106m", c_fmt["bright_cyan_bg"])
