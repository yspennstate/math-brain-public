"""test_recall_server_prewarm.py - the idle rebuild after a store move: it waits for the store to hold still for a
minute, never runs during or right after a call, never overnight, and at most once per five minutes."""
import recall_server as RS


def fresh():
    return dict(seen=None, since=0.0, checked=0.0, last=-1e9)


def test_rebuilds_after_store_holds_still():
    pw = fresh()
    key = lambda: 'k2'
    assert RS.prewarm_due(pw, 1000.0, 'k1', key, 1040.0) is None      # first sight of k2: start the still clock
    assert RS.prewarm_due(pw, 1000.0, 'k1', key, 1070.0) is None      # still for 30 s only
    assert RS.prewarm_due(pw, 1000.0, 'k1', key, 1101.0) == 'k2'      # still for 61 s: rebuild
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k3', 1200.0) is None   # within 5 min of the last rebuild


def test_store_unchanged_or_recent_call():
    pw = fresh()
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k1', 1100.0) is None
    pw = fresh()
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k2', 1010.0) is None   # last call ended 10 s ago
    assert pw['seen'] is None


def test_no_rebuild_overnight_or_before_any_call():
    pw = fresh()
    assert RS.prewarm_due(pw, None, 'k1', lambda: 'k2', 5000.0) is None
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k2', 1000.0 + 1801) is None


def test_store_key_read_at_most_every_five_seconds():
    pw = fresh()
    reads = []
    def key():
        reads.append(1)
        return 'k1'
    RS.prewarm_due(pw, 1000.0, 'k1', key, 1100.0)
    RS.prewarm_due(pw, 1000.0, 'k1', key, 1102.0)
    RS.prewarm_due(pw, 1000.0, 'k1', key, 1106.0)
    assert len(reads) == 2


def test_moving_store_restarts_the_clock():
    pw = fresh()
    RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k2', 1040.0)
    RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k3', 1090.0)              # moved again
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k3', 1120.0) is None
    assert RS.prewarm_due(pw, 1000.0, 'k1', lambda: 'k3', 1151.0) == 'k3'


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
