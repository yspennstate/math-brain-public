"""Check source quotations and bounded mathematical sanity examples; stdlib only."""
import math
import os
from pathlib import Path
import re
import resource
import hashlib

resource.setrlimit(resource.RLIMIT_CPU, (30, 30))
root = Path(__file__).resolve().parent
old = Path('~/codex_op_1114/briefs/AV_T132')
print('OMP_NUM_THREADS:', os.environ.get('OMP_NUM_THREADS'))
print('nice priority:', os.getpriority(os.PRIO_PROCESS, 0))
assert os.environ.get('OMP_NUM_THREADS') == '1'
assert os.getpriority(os.PRIO_PROCESS, 0) >= 15

verify = (root / 'VERIFY.md').read_text()
blocks = re.findall(r'```latex\n(.*?)\n```', verify, re.S)
intro_files = ['metric-introduction.tex', 'critical-introduction.tex',
               'clock-introduction.tex']
texts = [(root / 'sources' / p).read_text() for p in intro_files]
theorems = [b for b in blocks if b.startswith(r'\begin{theorem}')]
assert len(theorems) == 4, len(theorems)
for b in theorems:
    assert any(b in s for s in texts), b[:100]
print('Exact main-theorem source blocks:', len(theorems), 'of 4 match')
for name in intro_files:
    fresh = (root / 'sources' / name).read_text()
    previous = (old / 'sources' / name).read_text()
    assert fresh == previous, name
    print('Re-fetched introduction matches prior source:', name)

# Exact parameter substitutions, evaluated by an independent cosine call.
for q, gamma_sq in [(0, 2), (1, 8/3), (2, 3), (4, 4)]:
    value = 2 + 2 * math.cos(math.pi * gamma_sq / 2)
    assert abs(value-q) < 1e-12
print('q/gamma substitutions:', '0, 1, 2, 4 pass')

# Finite sanity check only: a logarithmic exponent does not imply adjacent ratios.
p, amp = 1/3, 0.07
def log2_a(j):
    return p*j + amp*(-1)**j/math.log(2)
r0 = math.exp(2*amp)
for m in [1, 2, 7, 31, 100]:
    for j in range(1, 200):
        delta = log2_a(j+m)-log2_a(j)-m*p
        assert abs(delta) <= math.log2(r0)+1e-12
ratios = [2**(log2_a(j+1)-log2_a(j)) for j in [1000, 1001]]
assert abs(ratios[0]-ratios[1]) > 0.1
print('Alternating-factor example: offset bounds pass; adjacent ratios:',
      ', '.join(f'{x:.9f}' for x in ratios))
for j in [1000, 10000, 100000]:
    assert abs(log2_a(j)/j-p) <= amp/(math.log(2)*j)+1e-15
print('Alternating-factor example: logarithmic exponent error bound passes')

for path in sorted((root / 'sources').iterdir()):
    if path.is_file():
        print('SHA256', hashlib.sha256(path.read_bytes()).hexdigest(), path.name)
print('All audit checks passed. These checks do not verify preprint proofs.')
