# Logger

Logger is a lightweight and flexible Python logging utility designed to simplify and standardize logging across your projects. It provides an easy-to-use interface for capturing, formatting, and managing log messages, making debugging and monitoring more efficient.

## Features

- Simple API for logging messages at various levels (info, warning, error, debug)
- Customizable log formats and output destinations (console, file, etc.)
- Supports log rotation and retention policies
- Thread-safe and suitable for multi-process applications
- Easily extendable for advanced use cases

## Use Cases

- **Application Debugging:** Track application flow and errors during development.
- **Production Monitoring:** Collect logs for monitoring and troubleshooting in production environments.
- **Audit Trails:** Maintain records of important events and user actions.
- **Performance Analysis:** Log timing and performance metrics for optimization.

## Installation

Install the package directly from GitHub (recommended during development):

```bash
pip install git+https://github.com/louisgoodnews/Logger.git@main
```

## Basic Usage

```python
from logger import Logger

log = Logger('my_app.log')
log.info('Application started')
log.error('An error occurred')
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please open issues or submit pull requests on GitHub.

Before contributing, please read the CONTRIBUTING.md guidelines.

## Project Status

This project is currently in active development. Feedback and contributions are highly appreciated.

## Python Compatibility

Tested with Python 3.8 and above.
