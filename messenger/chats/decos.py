def method_require(method):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if method == args[0]:
                return func(*args, **kwargs)
            raise Exception("Wrapper exception")
        return wrapper
    return decorator        

def str_change(type):
    def decorator(func):
        def wrapper(*args,**kwargs):
            if type == 'upper':
                return func(*args,**kwargs).upper()
            elif type == 'lower':
                return func(*args,**kwargs).lower()    
            raise Exception('FUCK YOU')
        return wrapper
    return decorator    

@method_require('GET')
def foo(request_method):
    return True

print(foo('GET'))    