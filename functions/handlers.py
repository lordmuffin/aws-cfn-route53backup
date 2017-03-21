import os, sys, subprocess, json

LIBS = os.path.join(os.getcwd(), 'local', 'lib')

def handler(filename):
    def handle(event, context):
        env = os.environ.copy()
        env.update(LD_LIBRARY_PATH=LIBS)
        proc = subprocess.Popen(
            ('python', filename),
            env=env,
            stdin=subprocess.PIPE,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT)
        (stdout, _) = proc.communicate(input=json.dumps(event))
        try:
            return json.loads(stdout)
        except ValueError:
            raise ValueError(stdout)
    return handle

def invoking(f):
    output = f(json.load(sys.stdin))
    json.dump(output, sys.stdout)

my_function = handler('my_function.py')
other_function = handler('other_function.py')
