"""Candidate follow-up: fail closed on untrusted compute telemetry.

This module launches no process and changes no governor or production file.
"""
import datetime as dt
import math


def validate_state(state, now=None):
    if not isinstance(state, dict):
        raise RuntimeError('Compute telemetry is not an object')
    if state.get('status') not in {'ok', 'warn'}:
        raise RuntimeError('Compute status is distressed or unknown')
    if state.get('mode') not in {'owner_present_polite', 'owner_away_open', 'open'}:
        raise RuntimeError('Compute mode is throttled or unknown')
    try:
        stamp = dt.datetime.strptime(state['ts'], '%Y-%m-%d %H:%M:%S')
        age = ((now or dt.datetime.now()) - stamp).total_seconds()
    except (ValueError, TypeError, KeyError) as exc:
        raise RuntimeError('Compute timestamp is missing or malformed') from exc
    if not 0 <= age <= 180:
        raise RuntimeError('Compute telemetry is stale or future-dated')
    for field in ('cpu_pct', 'mem_avail_mb', 'commit_avail_mb'):
        value = state.get(field)
        if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value) or value < 0:
            raise RuntimeError('Compute metric is missing, nonfinite or invalid: ' + field)
    hung = state.get('hung_windows')
    if isinstance(hung, bool) or not isinstance(hung, int) or hung < 0:
        raise RuntimeError('Hung-window count is missing or invalid')
    if (hung != 0 or state['cpu_pct'] > 85 or state['mem_avail_mb'] < 8000
            or state['commit_avail_mb'] < 8000):
        raise RuntimeError('Compute admission held; no new compiler process')
