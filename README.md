# Colored Console Logger

A simple yet powerful Python logging utility that provides colored console output for different logging levels. Built with Pydantic for robust data validation and type checking.

## Features

- Colored console output for different logging levels
- Five standard logging levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Timestamp and logger name in each log message
- Clean and type-safe implementation using Pydantic
- Easy to integrate into existing projects

## Installation

1. Clone the repository:
```bash
git clone https://github.com/louisgoodnews/Logger.git
cd Logger
```

2. Install dependencies:
```bash
pip install pydantic
```

## Usage

Here's a simple example of how to use the logger:

```python
from src.logger import Logger
from src.logger.level import Level

# Create a logger instance
logger = Logger.get_logger(name="MyApp", level=Level.INFO)

# Log messages at different levels
logger.debug("Debug message")  # Gray text
logger.info("Info message")  # Blue text
logger.warning("Warning!")  # Yellow text
logger.error("Error occurred")  # Red text
logger.critical("Critical!")  # Red text
```

### Logging Levels

The logger supports five standard logging levels, in order of increasing severity:

1. `DEBUG` - Detailed information for debugging
2. `INFO` - General information about program execution
3. `WARNING` - Indication of a potential problem
4. `ERROR` - A serious problem
5. `CRITICAL` - A critical error that may prevent the program from running

### Color Scheme

Each logging level has its own color for better visibility:
- DEBUG: Gray
- INFO: Blue
- WARNING: Yellow
- ERROR: Red
- CRITICAL: Red

## Requirements

- Python 3.6+
- pydantic

## Project Structure

```
Logger/
├── level.py      # Logging level enumeration
├── logger.py     # Main logger implementation
├── main.py       # Usage example
└── README.md     # This file
```

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.