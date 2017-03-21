import handlers, pandas

def route53_backups(n):
    return (n * 2, pandas.__version__)

if __name__ == '__main__':
    handlers.invoking(route53_backups)
