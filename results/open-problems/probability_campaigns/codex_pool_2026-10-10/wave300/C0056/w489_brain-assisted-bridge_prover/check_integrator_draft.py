"""Run only the integrator's pure draft parser; do not call ingestion/sealing/main."""
from pathlib import Path
import json
import runpy

BASE = Path(__file__).resolve().parent
PARSER = Path('~/math-brain-build/tools/integrate_drafts.py')

def main():
    namespace = runpy.run_path(str(PARSER), run_name='w489_read_only_draft_validation')
    payload, errors = namespace['parse_draft'](BASE / 'DRAFT_bundle_001.json')
    result = {'command': 'python -X utf8 ~/brain_workers/w489/check_integrator_draft.py',
              'validator': str(PARSER) + ':parse_draft', 'valid': not errors,
              'errors': errors, 'entries': len(payload.get('entries', [])),
              'relations': len(payload.get('relations', [])),
              'ingestion_called': False, 'store_opened': False,
              'gate_key_read': False, 'mathematical_proof_verified': False}
    (BASE / 'INTEGRATOR_VALIDATION.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
    print(json.dumps(result))
    return 0 if not errors else 1

if __name__ == '__main__':
    raise SystemExit(main())
