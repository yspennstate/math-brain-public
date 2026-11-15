"""One-process replay watchdog; no solver and no process pool."""
import os
import resource
import sys
import threading


def peak_bytes():
    value=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return value if sys.platform=='darwin' else value*1024


def install(limit=1_000_000_000):
    def watch():
        while True:
            if peak_bytes()>limit:
                os.write(2,b'Replay memory guard exceeded 1 GB child peak\n')
                os._exit(99)
            threading.Event().wait(.02)
    threading.Thread(target=watch,daemon=True).start()
