from datetime import datetime
import os


def log(path):
    def decor(func):
        CACHE = {}
        def timedate(*args,**kwargs):
            t = str(datetime.now().time())[0:8]
            d = str(datetime.now().date())
            CACHE['time'] = t
            CACHE['date'] = d
            CACHE['function name'] = func.__name__
            CACHE['log'] = os.getcwd()
            CACHE['input'] = args,kwargs
            output = func(*args,**kwargs)
            CACHE['output'] = output
            with open(f'{path}check_list.json', 'w') as f:
                f.write(str(CACHE))
        return timedate
    return decor
