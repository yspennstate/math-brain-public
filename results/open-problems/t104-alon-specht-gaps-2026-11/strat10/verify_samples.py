"""PROVED: replay finite rational sample certificates only."""
import json
from certify_samples import check_actual
from fractions import Fraction as F
records=json.load(open('exact_samples.json'))['records']
for rec in records:assert check_actual(rec['source'],F(rec['scale_fraction']))==rec['verification']
assert records
print('PROVED:',len(records),'exact positive rational points satisfy every inherited (11) filter; OPEN global sign.')
