import handlers, pandas

def my_function(n):
    return (n * 2, pandas.__version__)

if __name__ == '__main__':
    handlers.invoking(my_function)
