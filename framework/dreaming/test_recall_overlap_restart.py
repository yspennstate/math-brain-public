"""test_recall_overlap_restart.py - a wire-only edit leaves the code key alone and changes the wire key; two wire
generations of one store hold two server locks; the keeper sees the change by content, not by mtime."""
if "-h" in __import__("sys").argv[1:] or "--help" in __import__("sys").argv[1:]:
    print((__doc__ or "").strip() or "usage: python %s" % __import__("os").path.basename(__file__))
    raise SystemExit(0)
import os
import shutil
import tempfile
import time
from pathlib import Path

import recall_protocol as P
import recall_server as RS
import recall_keeper as K


def with_copy(fn):
    """Run fn on a throwaway copy of the wire files, so the real ones are never touched."""
    tmp = Path(tempfile.mkdtemp())
    old_here = P.HERE
    try:
        for name in P.WIRE_FILES:
            src = old_here / name
            (tmp / name).write_bytes(src.read_bytes() if src.exists() else b'')
        P.HERE = tmp
        return fn(tmp)
    finally:
        P.HERE = old_here
        shutil.rmtree(tmp, ignore_errors=True)


def test_wire_edit_keeps_code_key():
    names = {p.name for p in P.code_files()}
    assert not names & set(P.WIRE_FILES), names & set(P.WIRE_FILES)
    def run(tmp):
        code0, wire0 = P.code_key(), P.wire_key()
        with open(tmp / 'recall_client.py', 'a', encoding='utf-8') as fh:
            fh.write('\n# a comment\n')
        assert P.code_key() == code0
        assert P.wire_key() != wire0
    with_copy(run)


def test_touch_is_not_a_wire_change():
    def run(tmp):
        wire0 = P.wire_key()
        path = tmp / 'recall_server.py'
        st = path.stat()
        os.utime(path, ns=(st.st_atime_ns, st.st_mtime_ns + 5 * 10**9))
        assert P.wire_key() == wire0
    with_copy(run)


def test_protocol_is_in_the_key():
    code0 = P.code_key()
    P.PROTOCOL += 1
    try:
        assert P.code_key() != code0
    finally:
        P.PROTOCOL -= 1


def test_two_generations_two_locks():
    store = os.path.join(tempfile.gettempdir(), 'overlap_test_%d.sqlite3' % os.getpid())
    a = RS.mutex(store, 'a' * 64)
    try:
        b = RS.mutex(store, 'b' * 64)
        try:
            try:
                RS.mutex(store, 'a' * 64)
            except RuntimeError as e:
                assert 'second instance' in str(e)
            else:
                raise AssertionError('same generation took a second lock')
        finally:
            RS.release(b)
    finally:
        RS.release(a)


def test_keeper_wire_changed():
    assert K.wire_changed({}) is False                      # an old server with no wire: the stamp check decides
    assert K.wire_changed({'wire': P.wire_key()}) is False
    assert K.wire_changed({'wire': '0' * 64}) is True


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
