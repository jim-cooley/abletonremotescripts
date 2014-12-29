# cheesy logging:
#
# a strategy to cache the ControlSurface during initialization, allowing us to use the log_message() method
#
from _Framework.ControlSurface import ControlSurface

_logger = None


# sets the logger (called from your global init)
class Logger:
	@classmethod
	def log_message(cls, message):
		if _logger is not None:
			_logger.log_message(message)

	@classmethod
	def set_logger(cls, facility):
		_logger = facility