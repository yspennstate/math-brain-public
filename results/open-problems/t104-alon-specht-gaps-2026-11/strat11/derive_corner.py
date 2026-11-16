"""Generate the local certificates using rational arithmetic only."""
import json
from pathlib import Path
from corner_algebra import tangent_data, remainder_data, matrix_ball_data, verify_invariant_formula

if __name__=='__main__':
    assert verify_invariant_formula()
    for name,data in [('tangent_certificate.json',tangent_data()),('remainder_certificate.json',remainder_data()),('matrix_ball_certificate.json',matrix_ball_data())]:
        Path(name).write_text(json.dumps(dict(label='PROVED by verify_corner.py',**data),indent=2)+'\n')
        print('PROVED:',name,flush=True)
