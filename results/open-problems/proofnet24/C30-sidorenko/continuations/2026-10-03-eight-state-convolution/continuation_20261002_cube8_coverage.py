"""Exact affine coverage of all 40320 strict cube8 weight orders."""
from pathlib import Path
import itertools,json,hashlib
from collections import Counter


def signs(p):
 answer=[]
 for a in range(1,8):
  pivot=a&-a
  answer.append(__import__('math').prod(1 if p[x]>p[x^a] else -1 for x in range(8) if not x&pivot))
 return tuple(answer)

def xor_span(columns):
 return {__import__('functools').reduce(int.__xor__,(columns[i] for i in range(len(columns)) if m>>i&1),0) for m in range(1<<len(columns))}

def main():
 linear=[]
 for columns in itertools.product(range(1,8),repeat=3):
  if len(xor_span(columns))!=8:continue
  linear.append(tuple(__import__('functools').reduce(int.__xor__,(columns[i] for i in range(3) if x>>i&1),0) for x in range(8)))
 assert len(linear)==168
 affine={tuple(v^b for v in L) for L in linear for b in range(8)}
 assert len(affine)==1344
 representative=(0,1,2,7,3,6,5,4)
 orbit={tuple(representative[A[x]] for x in range(8)) for A in affine}
 counts=Counter();bad=set()
 for p in itertools.permutations(range(8)):
  sign=signs(p);counts[sum(v>0 for v in sign)]+=1
  if all(v<0 for v in sign):bad.add(p)
 assert len(bad)==1344 and orbit==bad
 assert sum(counts.values())==40320
 out={'status':'PASS exact affine coverage of all strict orders','linear_group_size':len(linear),
      'affine_group_size':len(affine),'all_strict_order_count':40320,
      'number_by_positive_smoothing_direction':dict(sorted(counts.items())),
      'exceptional_order_count':len(bad),'exceptional_representative':representative,
      'exceptional_affine_orbit_equals_all_bad_orders':True,
      'exceptional_orders_sha256':hashlib.sha256(repr(sorted(bad)).encode()).hexdigest(),
      'affine_permutations':[list(a) for a in sorted(affine)]}
 Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
 print(json.dumps({k:v for k,v in out.items() if k!='affine_permutations'},indent=2))
if __name__=='__main__':main()
