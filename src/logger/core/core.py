"""
Author: Louis Goodnews
Date: 2025-07-08
"""

import traceback

from datetime import datetime

from enum import Enum
from typing import Any, Callable, Final, List, Optional


__all__: Final[List[str]] = ["Level", "Logger"]


class Level(Enum):
    """
    Enum representing the logging levels.

    This enum defines the standard logging levels used in the Logger class.
    Each level is associated with a numeric value that indicates its severity.
    The levels are used to filter log messages based on their importance.

    Attributes:
        DEBUG: Detailed information, typically of interest only when diagnosing problems.
        INFO: Confirmation that things are working as expected.
        WARNING: An indication that something unexpected happened, or indicative of some problem in the near future.
        ERROR: Due to a more serious problem, the software has not been able to perform some function.
        CRITICAL: A very serious error, indicating that the program itself may be unable to continue running.
    """

    # Numeric values for each logging level
    SILENT = 0
    DEBUG = 10
    INFO = 20
    WARNING = 30
    ERROR = 40
    CRITICAL = 50

    def __str__(self) -> str:
        """
        Return the name of the logging level.

        :return: The name of the logging level.
        :rtype: str
        """

        # Return the name of the logging level as a string
        return self.name


class LevelColor(Enum):
    """
    Enum representing the colors associated with each logging level.

    This is used for terminal output to visually distinguish log levels.
    Each level is associated with a specific ANSI color code.

    The colors are used to format log messages in the terminal.

    Attributes:
        DEBUG: Blue color for debug messages.
        INFO: Green color for informational messages.
        WARNING: Yellow color for warning messages.
        ERROR: Red color for error messages.
        CRITICAL: Magenta color for critical messages.
    """

    # ANSI color codes for different log levels
    SILENT = "\033[0m"  # No color
    DEBUG = "\033[94m"  # Blue
    INFO = "\033[92m"  # Green
    WARNING = "\033[93m"  # Yellow
    ERROR = "\033[91m"  # Red
    CRITICAL = "\033[95m"  # Magenta

    def __str__(self) -> str:
        """
        Return the ANSI color code associated with the logging level.

        :return: The ANSI color code as a string.
        :rtype: str
        """

        # Return the ANSI color code as a string
        return self.value


class Logger:
    """
    A simple logger class for logging messages at different levels.
    This class provides methods to log messages at various levels (DEBUG, INFO, WARNING, ERROR, CRITICAL).

    It allows for filtering messages based on the logging level and provides a way to format log messages with timestamps and colors.

    Attributes:
        name (str): The name of the logger.
        level (Level): The current logging level of the logger.
    """

    def __init__(
        self,
        name: str,
        level: Level = Level.INFO,
    ) -> None:
        """
        Initialize the Logger instance.

        :param name: The name of the logger.
        :type name: str
        :param level: The logging level (default is Level.INFO).
        :type level: Level
        :type name: str

        :return: None
        :rtype: None
        """

        # Initialize the colorization settings
        self._colorization: Final[dict[str, Any]] = {}

        # Set the logging level
        self._level: Final[Level] = level

        # Set the name of the logger
        self._name: Final[str] = name

    @property
    def colorization(self) -> dict[str, Any]:
        """
        Get the colorization settings for the logger.

        This property is currently a placeholder and does not implement any functionality.
        It can be extended in the future to support colorization of log messages.

        :return: The colorization settings as a dictionary.
        :rtype: dict[str, Any]
        """

        # Return the current colorization settings
        return self._colorization

    @colorization.setter
    def colorization(
        self,
        **kwargs: Any,
    ) -> None:
        """
        Set the colorization settings for the logger.
        This setter allows for updating the colorization settings of the logger.

        :param kwargs: Additional keyword arguments for future colorization settings.
        :type kwargs: Any

        :return: None
        :rtype: None
        """

        # Update the colorization settings
        self.colorization.update(kwargs)

    @property
    def level(self) -> Level:
        """
        Get the current logging level.

        :return: The current logging level.
        :rtype: Level
        """

        # Return the current logging level
        return self._level

    @property
    def name(self) -> str:
        """
        Get the name of the logger.

        :return: The name of the logger.
        :rtype: str
        """

        # Return the name of the logger
        return self._name

    @classmethod
    def get_logger(
        cls,
        name: str,
        level: Level = Level.INFO,
    ) -> "Logger":
        """
        Get a logger instance with the specified name and level.

        :param name: The name of the logger.
        :type name: str
        :param level: The logging level (default is Level.INFO).
        :type level: Level

        :return: An instance of Logger.
        :rtype: Logger
        """

        # Return a new Logger instance
        return cls(
            level=level,
            name=name,
        )

    def __contains__(
        self,
        item: Any,
    ) -> bool:
        """
        Check if the Logger instance contains a specific item.

        :param item: The item to check for.
        :type item: Any

        :return: True if the Logger instance contains the item, False otherwise.
        :rtype: bool
        """

        # Check if the item is in the Logger instance
        return item in self.__dict__

    def __eq__(
        self,
        other: "Logger",
    ) -> bool:
        """
        Check if the Logger instance is equal to another object.

        :param other: The object to compare with.
        :type other: object

        :return: True if the Logger instance is equal to the other object, False otherwise.
        :rtype: bool
        """

        # Check if the other object is an instance of Logger
        if not isinstance(other, Logger):
            # If the other object is not an instance of Logger, return False
            return False

        # Return True if the Logger instances are equal
        return self.name == other.name and self.level == other.level

    def __getitem__(
        self,
        key: str,
    ) -> Optional[Any]:
        """
        Get an attribute of the Logger instance by key.

        :param key: The name of the attribute to retrieve.
        :type key: str

        :return: The value of the specified attribute, or None if it does not exist.
        :rtype: Optional[Any]
        """

        # Return the value of the specified attribute or None if it does not exist
        return self.__dict__.get(
            key,
            None,
        )

    def __repr__(self) -> str:
        """
        Return a string representation of the Logger instance.

        :return: A string representation of the Logger.
        :rtype: str
        """

        # Return a formatted string with the logger's name and level
        return f"<Logger(name={self.name}, level={self.level})>"

    def __str__(self) -> str:
        """
        Return a string representation of the Logger instance.

        :return: A string representation of the Logger.
        :rtype: str
        """

        # Return a formatted string with the logger's name and level
        return self.__repr__()

    def log(
        self,
        message: Any,
        override: bool = False,
        level: Level = Level.SILENT,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log a message with the specified logging level.

        :param level: The logging level for the message. Defaults to Level.SILENT.
        :type level: Level
        :param message: The message to log.
        :type message: Any
        :param override: If True, the message will be logged regardless of the logger's level. Defaults to False.
        :type override: bool
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Check if the logging level is appropriate for the message
        if not override and level.value < self.level.value:
            # If the level is lower than the logger's level, do not log the message
            return

        # Print the log message with the appropriate color and formatting
        print(
            f"{self.colorization.get(level.name, LevelColor[level.__str__()].value)}[{datetime.now().strftime("%Y-%m-%d %H:%M:%S")}] [{self.name}] [{level.name}]: {message} {args if args else ""} {kwargs if kwargs else ""}\033[0m"
        )

    def silent(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log a message at the SILENT level.

        :param message: The message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the SILENT level
        self.log(
            level=Level.SILENT,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def debug(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log a debug message.

        :param message: The debug message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the DEBUG level
        self.log(
            level=Level.DEBUG,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def info(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log an informational message.

        :param message: The informational message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the INFO level
        self.log(
            level=Level.INFO,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def warning(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log a warning message.

        :param message: The warning message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the WARNING level
        self.log(
            level=Level.WARNING,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def error(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log an error message.

        :param message: The error message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the ERROR level
        self.log(
            level=Level.ERROR,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def critical(
        self,
        message: Any,
        *args: Any,
        **kwargs: Any,
    ) -> None:
        """
        Log a critical message.

        :param message: The critical message to log.
        :type message: Any
        :param args: Additional positional arguments to format the message.
        :param kwargs: Additional keyword arguments to format the message.

        :return: None
        :rtype: None
        """

        # Log the message at the CRITICAL level
        self.log(
            level=Level.CRITICAL,
            message=message,
            override=True,
            *args,
            **kwargs,
        )

    def execute(
        self,
        function: Callable[[Any], Any],
        *args: Any,
        **kwargs: Any,
    ) -> Optional[Any]:
        """
        Execute a function and log its execution.
        This method wraps the execution of a function, logging its start and end times,
        along with any arguments passed to it. It also logs the result of the function execution.
        If an error occurs during execution, it logs the error message.

        :param function: The function to execute.
        :type function: Callable[[Any], Any]
        :param args: Positional arguments to pass to the function.
        :param kwargs: Keyword arguments to pass to the function.

        :return: The result of the function execution, or None if an error occurs.
        :rtype: Optional[Any]

        :raises Exception: If an error occurs during the function execution, it logs the error and returns None.
        """

        try:
            # Record the start time of the function execution
            start: datetime = datetime.now()

            # Log the start of the function execution
            self.info(message=f"Executing {function.__name__} with args: {args}, kwargs: {kwargs}")

            # Execute the function with the provided arguments
            result: Optional[Any] = function(*args, **kwargs)

            # Record the end time of the function execution
            end: datetime = datetime.now()

            # Calculate the duration of the function execution
            duration: float = (end - start).total_seconds()

            # Log the successful execution
            self.info(message=f"{function.__name__} executed successfully.")
            self.info(message=f"Execution time: {duration:.2f} seconds")
            self.info(message=f"Result: {result}")

            # Return the result of the function execution
            return result
        except Exception as e:
            # Log any errors that occur during execution
            self.error(message=f"Error executing {function.__name__}: {e}")

            # Return None if an error occurs
            return None

    def exception(
        self,
        exception: Exception,
        message: Any,
        log_traceback: bool = True,
    ) -> None:
        """
        Log an exception.

        :param message: The exception message to log.
        :type message: Any
        :param exception: The exception to log.
        :type exception: Exception
        :param log_traceback: Whether to log the traceback. Defaults to True.
        :type log_traceback: bool

        :return: None
        :rtype: None
        """

        # Check if the traceback should be logged
        if log_traceback:
            # Add the traceback to the message
            message += (
                f"\n Traceback for {exception.__class__.__name__}:\n\n{traceback.format_exc()}"
            )

        # Log the exception
        self.log(
            level=Level.ERROR,
            message=message,
            *args,
            **kwargs,
        )
