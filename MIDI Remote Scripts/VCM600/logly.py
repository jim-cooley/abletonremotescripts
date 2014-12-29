# cheesy logging:
#
# a strategy to cache the ControlSurface during initialization, allowing us to use the log_message() method
#
from _Framework.ControlSurface import ControlSurface


logly_logger = None


def logly_message(message):
	if logly_logger is not None and isinstance(logly_logger, ControlSurface):
		logly_logger.log_message(message)

def logly_set_logger(facility):
	global logly_logger
	logly_logger = facility
