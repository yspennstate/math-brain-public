"""An explicit local recall diagnostic on four already-returned cards, not a blind test."""
from pathlib import Path
import json
import time
from bridge_card_filter import select_spectral_measure_cards

BASE = Path(__file__).resolve().parent

def main():
    data = json.loads((BASE / 'BRAIN_RETRIEVAL.json').read_text(encoding='utf-8'))
    raw = next(q['rows'] for q in data['queries'] if q['name'] == 'poisson_bridge')
    expected_id = 'claim_930971f2e2958ad4b39127882e7fb8c2f41978d305608de432e06a9933e30a3d'
    start = time.perf_counter()
    after = select_spectral_measure_cards(raw)
    # Independent, manually judged relevance is the spectral-measure/Stieltjes topic,
    # not the assertion that the returned card proves Anderson delocalisation.
    judged_relevant = {expected_id}
    before_correct = sum(r['id'] in judged_relevant for r in raw)
    after_correct = sum(r['id'] in judged_relevant for r in after)
    result = {
        'command': 'python -X utf8 ~/brain_workers/w489/measure_filter.py',
        'sample': 'same four bounded export lookup candidates; nonblind local diagnostic',
        'before_returned': len(raw), 'before_relevant': before_correct,
        'before_precision': before_correct / len(raw),
        'after_returned': len(after), 'after_relevant': after_correct,
        'after_precision': after_correct / len(after) if after else 0,
        'retained_known_relevant': [r['id'] for r in after if r['id'] in judged_relevant],
        'filtered_ids': [r['id'] for r in raw if r['id'] not in {s['id'] for s in after}],
        'seconds': time.perf_counter() - start,
        'limitation': 'Four manually judged candidates only. Precision gain is local; no population, ranking, timing, or mathematical-validity improvement inferred.',
        'deployment': 'local prototype only; no global recall controls changed',
    }
    assert len(raw) == 4 and before_correct == 1
    assert len(after) == 1 and after_correct == 1
    assert after[0]['id'] == expected_id
    result['checks_passed'] = True
    (BASE / 'FILTER_MEASUREMENT.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
