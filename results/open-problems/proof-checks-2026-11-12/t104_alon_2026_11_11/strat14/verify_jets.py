"""Exact degree-two expansions of the target and constraints at nine limits."""
import json
from pathlib import Path
from chart_jets import expansions

def replay():
    actual=expansions()
    assert actual==json.loads((Path(__file__).resolve().parent/'chart_expansions.json').read_text())
    assert len(actual)==9
    print('PROVED (verify_jets.py): all nine quadratic-field target and active-constraint Taylor expansions match exactly.',flush=True)

if __name__=='__main__':replay()
