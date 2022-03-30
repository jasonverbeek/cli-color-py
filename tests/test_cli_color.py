from unittest import TestCase

from cli_color.color import Color
from cli_color import (
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
    blink
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
