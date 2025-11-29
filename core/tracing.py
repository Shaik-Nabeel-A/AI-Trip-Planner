import functools
import time
from core.logging import logger

def trace_tool(func):
    """Decorator to trace tool execution time and args"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        logger.info(f"Starting tool: {func.__name__} with args: {args}, kwargs: {kwargs}")
        try:
            result = func(*args, **kwargs)
            end_time = time.time()
            duration = end_time - start_time
            logger.info(f"Finished tool: {func.__name__} in {duration:.2f}s")
            return result
        except Exception as e:
            logger.error(f"Error in tool {func.__name__}: {str(e)}")
            raise e
    return wrapper
