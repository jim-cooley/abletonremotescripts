# cheesy logging:
#
# a strategy to cache the ControlSurface during initialization, allowing us to use the log_message() method
#
from _Framework.ControlSurface import ControlSurface


_logger = None


def logly_message(message):
	if _logger is not None and isinstance(_logger, ControlSurface):
		_logger.log_message(message)

def logly_set_logger(facility):
	global _logger
	logly_logger = facility
