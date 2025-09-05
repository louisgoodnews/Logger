# Level Enum

## Overview
The `Level` enum defines the standard logging levels used in the Logger class. Each level is associated with a numeric value that indicates its severity, allowing for flexible log filtering based on importance.

## Enum Values

| Level | Value | Description |
|-------|-------|-------------|
| `SILENT` | 0 | No logging output (internal use) |
| `DEBUG` | 10 | Detailed information for debugging purposes |
| `INFO` | 20 | Confirmation of normal operation |
| `WARNING` | 30 | Indication of potential issues |
| `ERROR` | 40 | Serious problems that might prevent normal execution |
| `CRITICAL` | 50 | Critical errors that may cause application failure |

## Usage

### Importing
```python
from logger import Level
```

### Checking Log Levels
```python
if current_level >= Level.INFO:
    # This will execute for INFO, WARNING, ERROR, and CRITICAL levels
    pass
```

### String Representation
```python
print(Level.INFO)  # Output: "INFO"
```

## Best Practices
- Use `DEBUG` for detailed diagnostic information
- Use `INFO` for normal operational messages
- Use `WARNING` for non-critical issues
- Use `ERROR` for serious problems that need attention
- Use `CRITICAL` for critical conditions that may cause the application to fail
