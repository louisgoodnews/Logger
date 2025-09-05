# LevelColor Enum

## Overview
The `LevelColor` enum defines ANSI color codes used for terminal output in the Logger class. Each logging level is associated with a specific color to visually distinguish between different types of log messages.

## Enum Values

| Level | ANSI Code | Color | Preview |
|-------|-----------|--------|---------|
| `SILENT` | `\033[0m` | Reset/No color | ![#000000](https://via.placeholder.com/15/000000/000000?text=+) No color |
| `DEBUG` | `\033[94m` | Blue | ![#0000ff](https://via.placeholder.com/15/0000ff/000000?text=+) Blue |
| `INFO` | `\033[92m` | Green | ![#00ff00](https://via.placeholder.com/15/00ff00/000000?text=+) Green |
| `WARNING` | `\033[93m` | Yellow | ![#ffff00](https://via.placeholder.com/15/ffff00/000000?text=+) Yellow |
| `ERROR` | `\033[91m` | Red | ![#ff0000](https://via.placeholder.com/15/ff0000/000000?text=+) Red |
| `CRITICAL` | `\033[95m` | Magenta | ![#ff00ff](https://via.placeholder.com/15/ff00ff/000000?text=+) Magenta |

## Usage

### Importing
```python
from logger import LevelColor
```

### Getting Color Codes
```python
debug_color = LevelColor.DEBUG.value  # Returns: "\033[94m"
```

### String Representation
```python
print(LevelColor.INFO)  # Output: "\033[92m"
```

### Using with Log Messages
```python
# Example of how colors are used internally in the Logger
color_code = LevelColor.INFO.value
reset_code = LevelColor.SILENT.value
print(f"{color_code}This is an info message{reset_code}")
```

## Customization

To customize colors, you can create a mapping in the Logger's `colorization` property:

```python
logger = Logger("my_app")
logger.colorization = {
    "INFO": "\033[96m"  # Change INFO to cyan
}
```

## Notes
- Colors are only visible in terminals that support ANSI color codes
- The `SILENT` color is used to reset the terminal color
- Color output can be disabled by setting `logger.colorization = {}`
- Custom colors must be valid ANSI escape sequences
