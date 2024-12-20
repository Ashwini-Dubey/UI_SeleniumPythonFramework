import pytest
import logging
import inspect

# Fixture for setting up the browser instance for the tests
@pytest.mark.usefixtures("setup")
class BaseClass:
    """
    Base class for all test classes.
    This class sets up the WebDriver instance for each test class using the 'setup' fixture
    defined in 'conftest.py'.
    """

    def getlogger(self):
        # Create a logger instance
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        # Create a file handler
        fileHandler = logging.FileHandler("../utilities/logfile.log")

        # Create a log formatter and attach it to the file handler
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s : %(message)s")
        fileHandler.setFormatter(formatter)

        # Add the file handler to the logger
        logger.addHandler(fileHandler)  # fileHandler Object

        # Set the log level to DEBUG to capture all log messages
        logger.setLevel(logging.DEBUG)

        return logger