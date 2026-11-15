"""Regenerate/check the rational log enclosure table without transcendental calls."""
from fractions import Fraction as F
from pathlib import Path
import argparse,re
p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
lo=[(m**1024).bit_length()-1-8192 for m in range(256,512)]
hi=[((m+1)**1024).bit_length()-8192 for m in range(256,512)]
assert 2*sum(F(1,3)**(2*j+1)/(2*j+1) for j in range(4))>F(1000,1443)
if a.check:
 s=Path('quantlog.h').read_text()
 for key,vals in [('qlo',lo),('qhi',hi)]:
  found=[int(x) for x in re.search(key+r'\[256\]=\{([^}]+)\}',s)[1].split(',')]
  assert vals==found
 print('All 512 integer-only log enclosure entries checked.')
else:
 Path('quantlog.h').write_text('// Integer-only enclosures in units 1/1024, from exact bit lengths of m^1024.\nstatic const int qlo[256]={'+','.join(map(str,lo))+'};\nstatic const int qhi[256]={'+','.join(map(str,hi))+'};\nstatic int qlog(uint64_t x,int upper){int e=63-__builtin_clzll(x);unsigned m=e>=8?x>>(e-8):x<<(8-e);return 1024*e+(upper?qhi[m-256]:qlo[m-256]);}\n')
 print('Wrote quantlog.h.')
