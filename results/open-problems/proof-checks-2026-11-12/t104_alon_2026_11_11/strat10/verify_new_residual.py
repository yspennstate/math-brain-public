"""PROVED: exact membership in the final residual; finite positive sign only."""
import json
from new_residual import verify
x=json.load(open('new_residual_witness.json'));assert verify(x['source'])==x['verification']
print('PROVED: final residual has an exact connected endpoint witness; its exact T6 is positive. OPEN: full residual sign.')
