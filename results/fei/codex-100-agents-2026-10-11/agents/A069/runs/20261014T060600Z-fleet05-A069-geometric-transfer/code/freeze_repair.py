from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
s=json.loads((R/'FROZEN_SPEC.json').read_text())
s['helper_version']='A069-final-reference-v2'
s['repair']='Correct unnormalized Walsh multiplier in equation(4) to2; original normalization failure logged. Domain, case count, symmetry, arithmetic, memory and55s cap unchanged.'
(R/'FROZEN_SPEC_V2.json').write_text(json.dumps(s,indent=2)+'\n')
