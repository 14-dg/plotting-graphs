import threading, time

args = {'i' : 0}

def foo(args):
    print (args['i'])
    time.sleep(5)

threading.start_new_thread(foo,(args,))

while True:
    args['i'] = args['i'] + 1