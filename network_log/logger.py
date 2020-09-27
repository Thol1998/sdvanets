import logging


class Logging:
    def __init__(self, **kwargs):
        self.str_form = "%(asctime)s  %(name)s %(levelname)s %(message)s"
        filename = ''
        try:
            if 'filename' not in kwargs:
                raise ValueError('filename must be specified')
            if 'path' in kwargs:
                filename = kwargs.pop('path') + kwargs.pop('filename')
            else:
                filename = kwargs.pop('filename')
            if 'log' not in kwargs:
                raise ValueError('log must be specified at the script\'s parameters')
            self.is_log = kwargs.pop('log')
            if not self.is_log:
                print('Disabling logs...')
            logging.basicConfig(filename=filename, format=self.str_form)
            self.logger = None

        except PermissionError:
            raise PermissionError('Permission denied, try with sudo.')

        except IOError:
            raise IOError('No such file or directory: %s' % filename)

    def log(self, msg, lvl, flag=None):
        if flag and self.is_log:
            if lvl == 'debug':
                self.logger.debug(msg)
            elif lvl == 'info':
                self.logger.info(msg)
            elif lvl == 'warn':
                self.logger.warn(msg)
            elif lvl == 'error':
                self.logger.error(msg)
            elif lvl == 'critical':
                self.logger.critical(msg)

    def config_log(self, logger_name):
        self.logger = logging.getLogger(logger_name)
        self.logger.setLevel(level=logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(level=logging.DEBUG)
        formatter = logging.Formatter(self.str_form)
        ch.setFormatter(formatter)

        self.logger.addHandler(ch)

    def set_str_form(self, str_form):
        self.str_form = str_form
