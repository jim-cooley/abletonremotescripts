# cheesy logging:
#
# a strategy to cache the ControlSurface during initialization, allowing us to use the log_message() method
#
from _Framework.ControlSurface import ControlSurface

_logger = None


def log_message(message):
	if _logger is not None and isinstance(_logger, ControlSurface):
		_logger.log_message(message)

def show_message(message):
	if _logger is not None and isinstance(_logger, ControlSurface):
		_logger.show_message(message)

def log_set_logger(facility):
	global _logger
	_logger = facility
