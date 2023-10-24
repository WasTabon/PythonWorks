import datetime

class CallLogger:
    def __init__(self):
        self.calls_info = []

    def log_call(self, func):
        def wrapper(*args, **kwargs):
            call_time = datetime.datetime.now()
            try:
                result = func(*args, **kwargs)
                status = 'Success'
            except Exception as err:
                result = str(err)
                status = 'Error'

            log_entry = (call_time, func.__name__, args, kwargs, status, result)
            self.calls_info.append(log_entry)
            self.sync_to_file(log_entry)
            return log_entry
        return wrapper

    def sync_to_file(self, log_entry):
        with open('log.txt', 'a') as file:
            file.write(str(log_entry) + '\n')
            print(log_entry)

    def clear_log_file(self):
        with open('log.txt', 'w') as file:
            file.write('')

    def get_logs(self):
        for call in self.calls_info:
            yield call

logger_instance = CallLogger()

@logger_instance.log_call
def func(arg1, arg2):
    return f'{arg1} is not {arg2}'

# Очистить лог перед запуском
logger_instance.clear_log_file()

# Вызов функций для записи логов
func('gre', 'erg')
func('gdf', 'ger')
func('rge', 'ger', 111)
