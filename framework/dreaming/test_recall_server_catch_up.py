"""test_recall_server_catch_up.py - the server extends its held state in memory on a store change, and drops it
whenever extend cannot be trusted. Fakes stand in for fastrecall and fastrecall_delta; no store is opened."""
import sys
import types

import recall_server as RS


class State:
    def __init__(self, key):
        self.key = key


def setup(extend, delta=True, age=21600.0):
    fd = types.ModuleType('fastrecall_delta')
    fd.MAX_CARDS = 5000
    fd.extend = extend
    sys.modules['fastrecall_delta'] = fd
    fr = types.SimpleNamespace(DELTA=delta, DELTA_CALL_MAX=2000, DELTA_MAX_AGE_S=age, _MEMO={})
    held = {'key': 'k1', 'prepared': State('base|k1'), 'opened': 100.0}
    return fd, fr, held


def derive():
    pass


def test_extend_ok():
    calls = []
    fd, fr, held = setup(lambda old, store, short: (calls.append(store) or (3, '')))
    n = RS.catch_up(held, fr, 'store.db', derive, 'k2', now=lambda: 200.0)
    assert n == 3 and calls == ['store.db']
    assert held['key'] == 'k2' and held['prepared'].key == 'base|k2'
    assert fr._MEMO['base|k2'] is held['prepared']
    assert fd.MAX_CARDS == 2000


def test_extend_refuses():
    fd, fr, held = setup(lambda *a: (None, 'not append-only'))
    assert RS.catch_up(held, fr, 's', derive, 'k2', now=lambda: 200.0) is None
    assert held['key'] == 'k1' and fr._MEMO == {}


def test_extend_raises():
    def boom(*a):
        raise RuntimeError('half way')
    fd, fr, held = setup(boom)
    assert RS.catch_up(held, fr, 's', derive, 'k2', now=lambda: 200.0) is None
    assert held['key'] == 'k1'


def test_too_old():
    fd, fr, held = setup(lambda *a: (1, ''), age=50.0)
    assert RS.catch_up(held, fr, 's', derive, 'k2', now=lambda: 200.0) is None


def test_delta_off_or_nothing_held():
    fd, fr, held = setup(lambda *a: (1, ''), delta=False)
    assert RS.catch_up(held, fr, 's', derive, 'k2', now=lambda: 200.0) is None
    fd, fr, held = setup(lambda *a: (1, ''))
    held['prepared'] = None
    assert RS.catch_up(held, fr, 's', derive, 'k2', now=lambda: 200.0) is None


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
