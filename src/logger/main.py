"""
Author: Louis Goodnews
Date: 2025-07-08
"""

from core.core import Level, Logger


def main() -> None:
    """
    Main function to demonstrate the usage of the Logger class.
    This function initializes the logger and logs messages at different levels.
    It serves as an entry point for the script.
    """

    # Initialize the logger
    logger: Logger = Logger.get_logger(
        level=Level.INFO,
        name=__name__,
    )

    # Log messages at different levels
    logger.info(message="This is an info message.")
    logger.warning(message="This is a warning message.")
    logger.error(message="This is an error message.")
    logger.critical(message="This is a critical message.")
    logger.debug(message="This is a debug message.")

    logger.log(
        level=Level.DEBUG,
        message="This message won't be logged.",
    )

    logger.log(
        level=Level.INFO,
        message="This message will be logged at the INFO level.",
    )


if __name__ == "__main__":
    main()
