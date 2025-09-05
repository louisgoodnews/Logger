# Logger Class Documentation

## Overview
The `Logger` class provides a flexible and easy-to-use logging system for Python applications with color-coded output and multiple log levels.

## Table of Contents
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Logging Levels](#logging-levels)
- [Class Reference](#class-reference)
- [Examples](#examples)

## Installation

```bash
pip install logger-package  # Replace with actual package name
```

## Quick Start

```python
from logger import Logger, Level

# Create a logger instance
logger = Logger(name="my_app", level=Level.DEBUG)

# Log messages at different levels
logger.debug("Debugging information")
logger.info("Application started")
logger.warning("This is a warning")
logger.error("An error occurred")
logger.critical("Critical failure!")
```

## Logging Levels

| Level | Value | Description |
|-------|-------|-------------|
| SILENT | 0 | No output (internal use) |
| DEBUG | 10 | Detailed debugging information |
| INFO | 20 | General information |
| WARNING | 30 | Potential issues |
| ERROR | 40 | Serious problems |
| CRITICAL | 50 | Critical errors |

## Class Reference

### Logger Class

```python
Logger(name: str, level: Level = Level.INFO)
```

#### Methods
- `debug(message: Any, *args, **kwargs)` - Log debug message
- `info(message: Any, *args, **kwargs)` - Log info message
- `warning(message: Any, *args, **kwargs)` - Log warning
- `error(message: Any, *args, **kwargs)` - Log error
- `critical(message: Any, *args, **kwargs)` - Log critical error
- `exception(exception: Exception, message: Any, log_traceback=True)` - Log exception
- `execute(function: Callable, *args, **kwargs)` - Execute and log function
- `log(message: Any, level: Level, override=False, *args, **kwargs)` - Generic log method

#### Properties
- `level` - Get current logging level
- `name` - Get logger name
- `colorization` - Get/set color settings

### Level Enum
```python
class Level(Enum):
    SILENT = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50
```

### LevelColor Enum
```python
class LevelColor(Enum):
    SILENT = "\033[0m"    # No color
    DEBUG = "\033[94m"    # Blue
    INFO = "\033[92m"     # Green
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"    # Red
    CRITICAL = "\033[95m" # Magenta
```

## Examples

### Basic Logging
```python
logger = Logger("my_module")
logger.info("Application started")

try:
    result = 10 / 0
except Exception as e:
    logger.exception(e, "Division by zero")
```

### Using execute()
```python
def process_data(data):
    return {"status": "success", "items_processed": len(data)}

data = [1, 2, 3, 4, 5]
result = logger.execute(process_data, data)
```

### Custom Format
```python
class CustomLogger(Logger):
    def log(self, message, override=False, level=Level.SILENT, *args, **kwargs):
        if not override and level.value < self.level.value:
            return
        timestamp = datetime.now().isoformat()
        print(f"[{level.name}] {message} | {timestamp}")
```

### Disable Colors
```python
logger = Logger("my_app")
logger.colorization = {}  # Disable colors
```
