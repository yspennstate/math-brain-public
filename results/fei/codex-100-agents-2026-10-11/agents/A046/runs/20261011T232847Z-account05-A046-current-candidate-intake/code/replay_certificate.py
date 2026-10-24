"""Read-only replay of B10 lead certificate with local output and a 60s cap."""
import runpy
import json
from pathlib import Path

RUN=Path(__file__).resolve().parents[1]
SOURCE=Path(r'~\brain_workers\FEI100_20261011\claude\B10\runs\20261011T230400Z-claude-B10-onebit-half-tax\code\certify_half_tax.py')
module=runpy.run_path(str(SOURCE),run_name='A046_readonly_replay')
result={'lemma_constants':module['lemma_constants'](),
        'box_certificate':module['run'](max_boxes=3000000,max_sec=60),
        'scope':'faithful source-code replay; independent analytic lemma/coverage review separate'}
(RUN/'out'/'CERTIFICATE_REPLAY.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
assert result['box_certificate']['status']=='PASS'
print(json.dumps(result['box_certificate'],indent=2))
