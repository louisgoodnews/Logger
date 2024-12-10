#!/usr/bin/env python3
"""
Example usage of the Logger class demonstrating different logging levels and colored output.

This script serves as both documentation and a practical example of how to use
the Logger class effectively in your applications. It shows:
- Logger initialization
- Usage of different logging levels
- Colored output in the console
"""

from logger import Logger
from level import Level

def demonstrate_logging() -> None:
    """
    Demonstrate the various logging levels and features of the Logger class.
    
    Creates a logger instance and shows examples of logging at different severity
    levels with colored output.
    """
    # Create a logger instance with a custom name and INFO level
    logger = Logger.get_logger(name="DemoLogger", level=Level.INFO)
    
    # Demonstrate each logging level
    logger.debug("This is a debug message - useful for detailed debugging information")
    logger.info("This is an info message - general information about program execution")
    logger.warning("This is a warning message - indicating potential issues")
    logger.error("This is an error message - something has gone wrong")
    logger.critical("This is a critical message - severe error that needs immediate attention")

def main() -> None:
    """
    Main entry point of the script.
    
    Runs the logging demonstration and handles any potential exceptions.
    """
    try:
        demonstrate_logging()
    except Exception as e:
        # Create an error logger for handling setup failures
        error_logger = Logger.get_logger(name="ErrorHandler", level=Level.ERROR)
        error_logger.critical(f"Failed to run demonstration: {str(e)}")
        raise

if __name__ == "__main__":
    main()