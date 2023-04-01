# Abstração
from pathlib import Path
LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        # Este módulo não deve ser executado como __main__
        raise NotImplementedError('Implemente o método log')
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    def _log(self, msg):
        msg_format = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando no log: {msg_format}')
        with open(LOG_FILE, 'a') as file:
            file.write(msg_format)
            file.write('\n')

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')
    
if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('qualquer coisa')
    lp.log_success('Que legal')

    lf = LogFileMixin()
    lf.log_error('qualquer coisa')
    lf.log_success('Que legal')
