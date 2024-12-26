from typing import *

from datetime import datetime

from level import Level


class Logger:
    """
    A configurable logging class that provides colored console output for different logging levels.

    This class implements standard logging functionality with colored output for different severity levels.

    Attributes:
        level (Level): The minimum logging level for this logger instance
        name (str): The name identifier for this logger instance
    """

    def __init__(
        self,
        level: Level,
        name: str,
    ) -> None:
        """
        Initializes a Logger instance.

        Args:
            level (Level): The minimum logging Level
            name (str): The name identifier for the logger
        """
        self._level: Level = level
        self._name: str = name

    @property
    def level(self) -> Level:
        """
        Returns the current minimum logging Level for the logger.
        """
        return self._level

    @level.setter
    def level(
        self,
        value: Level,
    ) -> None:
        """
        Updates the minimum logging Level for the logger.

        Args:
            value (str): The new minimum logging Level for the logger.

        Returns:
            None
        """
        self._level = value

    @property
    def name(self) -> str:
        """
        Returns the name identifier for the logger.
        """
        return self._name

    @name.setter
    def name(
        self,
        value: str,
    ) -> None:
        """
        Updates the name identifier for the logger.

        Args:
            value (str): The new name identifier for the logger.

        Returns:
            None

        Raises:
            AttributeError: The name identifier for the logger is not intended to be changed.
        """
        self.critical(
            message=f"Cannot set attribute 'name' in '{self.__class__.__name__}'."
        )

        raise AttributeError(
            f"Attribute 'name' of '{self.__class__.__name__}' is immutable."
        )

    @classmethod
    def get_logger(
        cls,
        name: str,
        level: Level = Level.INFO,
    ) -> "Logger":
        """
        Factory method to create a new Logger instance.

        Args:
            name (str): The name identifier for the logger
            level (Level, optional): The minimum logging level. Defaults to Level.INFO

        Returns:
            Logger: A new Logger instance with the specified name and level
        """
        logger: "Logger" = Logger(
            level=level,
            name=name,
        )

        logger.info(message=f"Initialized Logger '{logger.name}'...")

        return logger

    def _colourise_(
        self,
        level: Level,
        message: str,
    ) -> str:
        """
        Internal method to add ANSI color codes to log messages based on their level.

        Args:
            level (Level): The logging level determining the color
            message (str): The message to be colorized

        Returns:
            str: The colorized message with ANSI escape codes
        """
        colourisation: Dict[str, str] = {
            "RESET": "\x1b[0m",
            "DEBUG": "\x1b[90m",  # Gray
            "INFO": "\x1b[94m",  # Blue
            "WARNING": "\x1b[93m",  # Yellow
            "ERROR": "\x1b[91m",  # Red
            "CRITICAL": "\x1b[91m",  # Red
            "SILENT": "\x1b[0m",  # Gray
        }

        return f"{colourisation[level.value]}{message}{colourisation['RESET']}"

    def critical(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log a critical message.

        Args:
            message (str): The critical message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.CRITICAL,
            message=message,
            **kwargs,
        )

    def debug(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log a debug message.

        Args:
            message (str): The debug message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.DEBUG,
            message=message,
            **kwargs,
        )

    def error(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log an error message.

        Args:
            message (str): The error message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.ERROR,
            message=message,
            **kwargs,
        )

    def function(
        self,
        function: Callable[..., Any],
        *args,
        **kwargs,
    ) -> Any:
        """
        Decorator to log the execution of a function.

        Args:
            function (Callable[..., Any]): The function to be decorated
            *args: Positional arguments passed to the function
            **kwargs: Keyword arguments passed to the function

        Returns:
            Any: The result of the decorated function
        """
        self.log(
            level=Level.INFO,
            message=f"Executing: {function.__name__}",
        )

        start: datetime = datetime.now()
        result = function(*args, **kwargs)

        end: datetime = datetime.now()
        self.log(
            level=Level.INFO,
            message=f"Completed: {function.__name__}",
        )

        self.log(
            level=Level.INFO,
            message=f"Duration: {(end - start).total_seconds()}s",
        )
        return result

    def info(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log an informational message.

        Args:
            message (str): The info message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.INFO,
            message=message,
            **kwargs,
        )

    def log(
        self,
        message: str,
        level: Level = Level.INFO,
        **kwargs,
    ) -> None:
        """
        Core logging method that handles message formatting and output.

        Args:
            message (str): The log message to output
            level (Level, optional): The severity level of the message. Defaults to Level.INFO
            **kwargs: Additional keyword arguments for future extensibility
        """
        print(
            f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] [{self.name}] {self._colourise_(level, message)}",
            **kwargs,
        )

    def silent(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log a silent message.

        Args:
            message (str): The silent message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.SILENT,
            message=message,
            **kwargs,
        )

    def warning(
        self,
        message: str,
        **kwargs,
    ) -> None:
        """
        Log a warning message.

        Args:
            message (str): The warning message to log
            **kwargs: Additional keyword arguments passed to log()
        """
        self.log(
            level=Level.WARNING,
            message=message,
            **kwargs,
        )
