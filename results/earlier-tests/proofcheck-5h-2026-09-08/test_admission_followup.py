import datetime as dt
import unittest
from admission_followup import validate_state

NOW = dt.datetime(2026, 9, 8, 11, 0, 0)
GOOD = {'ts': '2026-09-08 10:59:30', 'status': 'warn', 'mode': 'owner_present_polite',
        'cpu_pct': 60.0, 'mem_avail_mb': 16000, 'commit_avail_mb': 24000, 'hung_windows': 0}


class AdmissionTests(unittest.TestCase):
    def test_present_and_away_are_allowed_with_headroom(self):
        for mode in ['owner_present_polite', 'owner_away_open', 'open']:
            validate_state({**GOOD, 'mode': mode}, NOW)

    def test_nonfinite_and_non_numeric_metrics_are_rejected(self):
        for field in ['cpu_pct', 'mem_avail_mb', 'commit_avail_mb']:
            for value in [float('nan'), float('inf'), float('-inf'), None, False, '60', -1]:
                with self.subTest(field=field, value=value), self.assertRaises(RuntimeError):
                    validate_state({**GOOD, field: value}, NOW)

    def test_missing_metrics_are_rejected(self):
        for field in GOOD:
            state = {k: v for k, v in GOOD.items() if k != field}
            with self.subTest(field=field), self.assertRaises(RuntimeError):
                validate_state(state, NOW)

    def test_unknown_status_or_mode_is_rejected(self):
        for field, value in [('status', 'green'), ('status', 'distress'), ('mode', 'throttle'), ('mode', 'mystery')]:
            with self.subTest(field=field, value=value), self.assertRaises(RuntimeError):
                validate_state({**GOOD, field: value}, NOW)

    def test_stale_future_and_malformed_time_rejected(self):
        for value in ['2026-09-08 10:56:59', '2026-09-08 11:00:01', 'garbage', None]:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                validate_state({**GOOD, 'ts': value}, NOW)

    def test_real_pressure_rejected(self):
        for field, value in [('cpu_pct', 85.01), ('mem_avail_mb', 7999), ('commit_avail_mb', 7999), ('hung_windows', 1)]:
            with self.subTest(field=field), self.assertRaises(RuntimeError):
                validate_state({**GOOD, field: value}, NOW)

    def test_threshold_boundaries_are_allowed(self):
        validate_state({**GOOD, 'cpu_pct': 85, 'mem_avail_mb': 8000, 'commit_avail_mb': 8000,
                        'ts': '2026-09-08 10:57:00'}, NOW)

    def test_hung_count_must_be_nonnegative_integer(self):
        for value in [False, None, -1, 0.0, float('nan')]:
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                validate_state({**GOOD, 'hung_windows': value}, NOW)

    def test_input_must_be_an_object(self):
        for value in [None, [], 'ok']:
            with self.assertRaises(RuntimeError):
                validate_state(value, NOW)


if __name__ == '__main__':
    unittest.main()
