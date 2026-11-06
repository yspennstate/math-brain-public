"""Controls for the math recall client against a fake server on a loopback port (no store, no model).

 C1 a warm answer is printed and its exit code returned
 C2 a call refused with store_moved_during_call is asked once more and the second, warm answer is used
 C3 two refusals in a row are not retried a third time: the call falls back (None)
 C4 any other refusal falls back at once, and the fallback is logged with its reason
 C5 no endpoint file: the call falls back and the log names the error
 C6 the default wait for the server is 180 s

    python test_recall_client_retry.py      (a few seconds; ALL PASS at the end)
"""
import base64
import hashlib
import io
import json
import os
import socket
import sys
import threading

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.environ.pop('MATH_RECALL_SERVER_DISABLE', None)
os.environ.pop('MATH_RECALL_SERVER_TIMEOUT', None)
import recall_protocol as P
import recall_client as C

results = []
ENDPOINT = os.path.join(HERE, 'endpoint.json')
COLD = os.path.join(HERE, 'recall_cold_calls.jsonl')
saved = {p: open(p, 'rb').read() if os.path.exists(p) else None for p in (ENDPOINT, COLD)}


def check(ok, what):
    results.append(ok)
    print(('PASS  ' if ok else 'FAIL  ') + what)


def answer(text, rc=0):
    out = text.encode('utf-8')
    return {'ok': 1, 'rc': rc, 'stdout': base64.b64encode(out).decode('ascii'), 'stderr': '',
            'stdout_sha256': hashlib.sha256(out).hexdigest(), 'stderr_sha256': hashlib.sha256(b'').hexdigest()}


def serve(replies):
    """Answer one connection per reply, in order; return the port and the list of requests seen."""
    srv = socket.socket()
    srv.bind(('127.0.0.1', 0))
    srv.listen(8)
    seen = []

    def run():
        for reply in replies:
            conn, _ = srv.accept()
            with conn:
                seen.append(P.receive_frame(conn))
                P.send_frame(conn, reply)
        srv.close()
    threading.Thread(target=run, daemon=True).start()
    return srv.getsockname()[1], seen


def endpoint(port):
    with open(ENDPOINT, 'w', encoding='utf-8') as fh:
        json.dump({'host': '127.0.0.1', 'port': port, 'token': 't', 'code': 'c', 'store': P.requested_store([]),
                   'stamp': P.code_stamp(()), 'environment': P.env_key()}, fh)


class Out(io.StringIO):
    pass


def call():
    C._COLD['logged'] = False
    old, sys.stdout = sys.stdout, Out()
    try:
        r = C._try_server([])
        text = sys.stdout.getvalue()
    finally:
        sys.stdout = old
    return r, text


try:
    port, seen = serve([answer('warm one\n', 3)])
    endpoint(port)
    r, text = call()
    check(r == 3 and text == 'warm one\n' and len(seen) == 1, 'C1 a warm answer is printed and its code returned')

    port, seen = serve([{'ok': 0, 'why': 'store_moved_during_call'}, answer('warm two\n')])
    endpoint(port)
    r, text = call()
    check(r == 0 and text == 'warm two\n' and len(seen) == 2, 'C2 a store-moved refusal is asked once more, warm')

    port, seen = serve([{'ok': 0, 'why': 'store_moved_during_call'}] * 2 + [answer('never\n')])
    endpoint(port)
    r, text = call()
    check(isinstance(r, tuple) and r[1] is None and len(seen) == 2 and text == '', 'C3 a second refusal is not retried again')

    port, seen = serve([{'ok': 0, 'why': 'busy'}])
    endpoint(port)
    r, text = call()
    check(r == ('refused: busy', None) and len(seen) == 1, 'C4 another refusal falls back at once with its reason')

    os.remove(ENDPOINT)
    r, _ = call()
    check(isinstance(r, tuple) and r[1] is None and r[0] == 'FileNotFoundError', 'C5 no endpoint falls back, error named')

    src = open(os.path.join(HERE, 'recall_client.py'), encoding='utf-8').read()
    check("'MATH_RECALL_SERVER_TIMEOUT','180.0'" in src, 'C6 the default wait for the server is 180 s')
finally:
    for p, b in saved.items():
        if b is None:
            if os.path.exists(p):
                os.remove(p)
        else:
            open(p, 'wb').write(b)

print('ALL PASS' if all(results) else 'FAILED %d of %d' % (results.count(False), len(results)))
sys.exit(0 if all(results) else 1)
