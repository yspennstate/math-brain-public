"""test_recall_server_timing.py - the per-call timing line: usage_now reads this process's CPU (and page faults
where the platform gives them), and timing_line writes the fields the log readers expect, never a query."""
import recall_server as RS


def test_usage_now_reads_cpu():
    faults, cpu = RS.usage_now()
    assert cpu is None or cpu >= 0
    assert faults is None or faults >= 0
    total = 0
    for i in range(200000):
        total += i * i
    faults2, cpu2 = RS.usage_now()
    if cpu is not None and cpu2 is not None:
        assert cpu2 >= cpu


def test_timing_line_fields():
    line = RS.timing_line(42, 7, 3.25, 191.0, 2, 0, ' catch 3 0.4', (100, 1.0), (150, 3.5))
    assert line.endswith('\n')
    body = line.split(' ', 2)[2]
    assert body == 'pid 42 req 7 took 3.2 idle 191.0 reload 2 rc 0 catch 3 0.4 pf 50 cpu 2.5\n', body


def test_timing_line_without_usage():
    line = RS.timing_line(1, 1, 1.0, 0.0, 0, 0, '', (None, None), (None, 2.0))
    assert ' pf ' not in line and ' cpu ' not in line
    assert line.rstrip().endswith('rc 0')


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)
