import asyncio
import functools as ft

'''
async_cmd
Wraps a function into an asynchronous runner

Params:
    func: callable 
        function to be wrapped
        
Returns:
    callable
    wrapper function
'''
def async_cmd(func: callable) -> callable:
    @ft.wraps(func)
    def wrapper(*args, **kwargs):
        return asyncio.run(func(*args, **kwargs))
    
    return wrapper
