import sys
from functools import lru_cache
from fractions import Fraction as F
import check as c
OLD_INTERVAL=c.b.interval
PILOT=sys.argv[1]=='pilot'
Q=c.b.Q
@lru_cache(None)
def integer_interval(items):
 if not items:return F(0),F(0)
 D=max(v.denominator for _,v in items)
 assert D&(D-1)==0
 low=high=0
 for p,weight in items:
  assert D%weight.denominator==0
  l,h=c.b.logint(p)
  ln=l.numerator*(Q//l.denominator);hn=h.numerator*(Q//h.denominator)
  wn=weight.numerator*(D//weight.denominator)
  low+=wn*(ln if wn>0 else hn);high+=wn*(hn if wn>0 else ln)
 return F(low,D*Q),F(high,D*Q)
def interval(e):
 result=integer_interval(tuple(sorted(e.items())))
 if PILOT:assert result==OLD_INTERVAL(e)
 return result
c.b.interval=interval
if PILOT:c.run(True,tag='pilot_v2')
else:
 rows=(c.ROOT/'out/main_rows.jsonl').read_text(encoding='utf-8').splitlines()
 assert len(rows)==7841
 c.run(False,skip=len(rows),tag='continuation')
