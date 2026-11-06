"""test_recall_client_retry.py - recall_client asks the server once more after a store_moved_during_call refusal,
and only once.

    python test_recall_client_retry.py

A fake server on 127.0.0.1 answers each connection from a script of replies; the client reads a temporary
endpoint.json. No store, model or real server is touched.
 R1 refused store_moved, then served: the client returns the served rc and makes 2 connections
 R2 refused store_moved twice: the client falls back (None) after exactly 2 connections, no loop
 N1 refused for another reason: the client falls back after 1 connection (no retry)
 N2 served at once: 1 connection
 R3 the retry flag is clear again after a retried call (a later call may retry once more)
"""
import base64
import hashlib
import io
import json
import os
import socket
import sys
import tempfile
import threading
from pathlib import Path

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import recall_client  # noqa: E402
from recall_protocol import code_stamp, env_key, requested_store, send_frame, receive_frame  # noqa: E402

fails, ran = [], []


def check(ok, what):
    print(("PASS  " if ok else "FAIL  ") + what)
    ran.append(what)
    if not ok:
        fails.append(what)


def served(rc=0, out=b"answer\n"):
    return dict(ok=1, rc=rc, stdout=base64.b64encode(out).decode(), stderr=base64.b64encode(b"").decode(),
                stdout_sha256=hashlib.sha256(out).hexdigest(), stderr_sha256=hashlib.sha256(b"").hexdigest())


def refused(why):
    return dict(ok=0, why=why)


def run(replies):
    srv = socket.socket()
    srv.bind(("127.0.0.1", 0))
    srv.listen(8)
    srv.settimeout(5)
    port = srv.getsockname()[1]
    seen = []

    def serve():
        for reply in replies:
            try:
                conn, _ = srv.accept()
            except OSError:
                return
            with conn:
                receive_frame(conn)
                seen.append(1)
                send_frame(conn, reply)

    t = threading.Thread(target=serve, daemon=True)
    t.start()
    tmp = Path(tempfile.mkdtemp(prefix="rc_retry_"))
    argv = ["question"]
    (tmp / "endpoint.json").write_text(json.dumps(dict(
        host="127.0.0.1", port=port, token="t", code="c", store=requested_store(argv),
        stamp=code_stamp(()), environment=env_key(), model_files=[])), encoding="utf-8")
    old_here, old_out = recall_client.HERE, sys.stdout
    recall_client.HERE = tmp
    sys.stdout = io.StringIO()
    try:
        rc = recall_client.try_server(argv)
        printed = sys.stdout.getvalue()
    finally:
        sys.stdout = old_out
        recall_client.HERE = old_here
    srv.close()
    t.join(2)
    return rc, len(seen), printed


def main():
    os.environ.pop("MATH_RECALL_SERVER_DISABLE", None)
    rc, n, out = run([refused("store_moved_during_call"), served(0)])
    check(rc == 0 and n == 2 and "answer" in out, "R1 store_moved then served: rc %r, %d connections" % (rc, n))
    check(recall_client._RETRY["used"] is False, "R3 retry flag clear after a retried call")
    rc, n, _ = run([refused("store_moved_during_call"), refused("store_moved_during_call"), served(0)])
    check(rc is None and n == 2, "R2 store_moved twice: rc %r, %d connections" % (rc, n))
    rc, n, _ = run([refused("busy"), served(0)])
    check(rc is None and n == 1, "N1 other refusal: rc %r, %d connections" % (rc, n))
    rc, n, _ = run([served(3)])
    check(rc == 3 and n == 1, "N2 served at once: rc %r, %d connections" % (rc, n))
    print("FAIL" if fails else "PASS", "- %d controls, %d failed" % (len(ran), len(fails)))
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
