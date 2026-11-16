"""PROVED: replay every rational identity/control and chart exclusion of family."""
import json
from family_certificate import build
assert build()==json.load(open('pressure_family.json'))
print('PROVED: r=1 connected residual family 0<s<=1/100, exact positive T6 tending to 0; all inherited residual filters replayed.')
