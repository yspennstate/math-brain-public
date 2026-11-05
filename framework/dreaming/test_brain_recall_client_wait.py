"""Controls for brain_recall_client._wait_loading: wait for a server that is still loading, never for a hung one.
Run: python test_brain_recall_client_wait.py (or pytest)."""
import os, socket, sys, tempfile, time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import brain_recall_client as C


def _setup(stamp_age, wait=2.0):
    d = tempfile.mkdtemp()
    stamp = os.path.join(d, "spawn.stamp")
    open(stamp, "w").write("x")
    t = time.time() - stamp_age
    os.utime(stamp, (t, t))
    C.SPAWN_STAMP = stamp
    C.WAIT_LOADING_S = wait
    C.WAITED_S = None




def _replies(*seq):
    it = iter(seq)

    def req(_):
        r = next(it)
        if isinstance(r, BaseException):
            raise r
        return r
    return req


def test_stale_spawn_does_not_wait():
    _setup(stamp_age=C.SPAWN_FRESH_S + 5)
    C._request = _replies({"out": "never"})
    assert C._wait_loading({"op": "recall"}) is None


def test_waits_through_refusals_for_a_loading_server():
    _setup(stamp_age=1)
    C._request = _replies(ConnectionRefusedError(), FileNotFoundError(), {"out": "served"})
    assert C._wait_loading({"op": "recall"}) == {"out": "served"}
    assert C.WAITED_S is not None


def test_read_timeout_is_not_loading():
    _setup(stamp_age=1)
    C._request = _replies(socket.timeout(), {"out": "late"})
    assert C._wait_loading({"op": "recall"}) is None


def test_code_changed_decline_keeps_waiting():
    _setup(stamp_age=1)
    C._request = _replies({"decline": "code changed"}, {"out": "new server"})
    assert C._wait_loading({"op": "recall"}) == {"out": "new server"}


def test_zero_turns_it_off():
    _setup(stamp_age=1, wait=0)
    C._request = _replies({"out": "never"})
    assert C._wait_loading({"op": "recall"}) is None


def test_gives_up_at_the_deadline():
    _setup(stamp_age=1, wait=0.05)
    C._request = lambda _: (_ for _ in ()).throw(ConnectionRefusedError())
    t0 = time.time()
    assert C._wait_loading({"op": "recall"}) is None
    assert time.time() - t0 < 2


if __name__ == "__main__":
    n = 0
    for k, f in sorted(globals().items()):
        if k.startswith("test_") and callable(f):
            f()
            n += 1
            print("ok", k)
    print("%d passed" % n)
