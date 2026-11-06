"""test_recall_keeper_dry.py - the keeper's decisions without starting a server: the resource gate answers, a probe
verdict is ok / slow / neutral, a wire edit is seen only against a recorded wire key, liveness reads this process, an
endpoint whose pid is some other program is refused for adoption, and a keeper with no store exits at once."""
import os, tempfile
from pathlib import Path
import recall_keeper as K
import recall_protocol


def test_gate_answers():
    g = K.gate()
    assert set(g) >= {'commit_fraction', 'c_free_gib', 'allowed'}
    assert g['allowed'] in (0, 1)


def test_verdict():
    assert K.verdict(3.0, None) == 'ok'
    assert K.verdict(K.PROBE_SLOW + 1, None) == 'slow'
    assert K.verdict(None, 'timeout') == 'slow'
    assert K.verdict(None, 'store_moved_during_call') == 'neutral'


def test_wire_changed_needs_a_recorded_key():
    assert K.wire_changed({}) is False
    assert K.wire_changed({'wire': recall_protocol.wire_key()}) is False
    assert K.wire_changed({'wire': 'not-the-current-key'}) is True


def test_alive_reads_this_process():
    assert K.alive(os.getpid()) is True
    assert K.alive(0) is False


def test_endpoint_pid_of_another_program_is_not_adopted():
    try:
        K.Adopted(os.getpid())          # this is a test runner, not recall_server.py
    except OSError as e:
        assert 'not a recall server' in str(e) or 'cannot read pid' in str(e), e
    else:
        raise AssertionError('adopted a process that is not a recall server')


def test_no_store_exits_at_once():
    saved_log, saved_store = K.LOG, os.environ.pop('MATHBRAIN_STORE', None)
    fd, name = tempfile.mkstemp(suffix='.log')
    os.close(fd)
    K.LOG = Path(name)
    try:
        assert K.main() is None
        text = Path(name).read_text(encoding='utf-8')
        assert 'no MATHBRAIN_STORE' in text, text
    finally:
        K.LOG = saved_log
        if saved_store is not None:
            os.environ['MATHBRAIN_STORE'] = saved_store
        os.remove(name)


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
