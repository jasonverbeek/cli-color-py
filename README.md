# cli-color-py 0.5.0

Library to output colored text to the terminal.

This library is designed to be subjectively more elegant and readable than
alternatives I was able to find.

Compared to some alternatives cli-color-py currently has less colors available;
only supporting 14 of the 256+ supported colors in most (modern) terminals.

## Elegant/Minimalistic access to colors and styles

``` python
from cli_color import red, bright_yellow, green, bold

print(green("hello"))
print(bold(red("world")))

print(bright_yellow("background", bg=True))
```

## Low level access to colors and styles

Low level access however is a bit less elegant as for colors you need to
explicitly choose between the foreground or background.

cli-color-py isn't really made for doing stuff like this, but it is possible

```python
from cli_color.color import Color, Attribute

print(
    Color.RED.default(),
    "Red text",
    Color.CYAN.background(),
    "cyan background",
    Attribute.RESET
)
```

## Colors

Supported colors are currently: `black`, `red`, `green`, `yellow`, `blue`,
`magenta`, `cyan`, `white`, `bright_red`, `bright_green`, `bright_yellow`,
`bright_blue`, `bright_magenta`, `bright_cyan`

Background colors can be used by setting `bg` to `True` i.e. `red("text", bg=True)`

_NOTE: background and bright colors are not officially supported_

## Attributes or 'styles'

Supported attributes are: `reset`, `bold`, `underline`, `blink`

Attributes work similar to Colors but cannot be displayed on the background:

``` python
from cli_color import blink

print(blink("LOTTERY WINNER!!!"))
```

## More colors?

It's possible to add 256 color support but this currently seems unnecessary
to me personally.

The 14 available colors should be more than enough for any cli tool/script and
will work nicer with most color schemes.

## Windows

for Windows a modern terminal (compared to cmd/powershell) is required like
Windows Terminal or any other modern terminal on windows that uses ANSI colors.
