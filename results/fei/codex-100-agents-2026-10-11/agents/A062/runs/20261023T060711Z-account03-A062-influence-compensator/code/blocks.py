"""Exact all-interleaving profile Bellman certificate and raw physical reproduction."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
from itertools import product
import sys,json,time
sys.dont_write_bytecode=True
import kernel as k
from check import history,plus,scale,serial,LOGE_LO
ROOT=Path(__file__).resolve().parents[1]

def laws(dims,state,maps):
 p={};R={};N=1<<sum(dims)
 for s in range(N):
  pp=rr=F(1);offset=0
  for dim,m,rows in zip(dims,state,maps):
   t=(s>>offset)&((1<<dim)-1);offset+=dim
   if not m:pp*=int(t==0);rr*=int(t==0)
   else:
    k.check(m==dim);row=rows[m];d=row['d']
    pp*=((1-d)**2 if t==0 else d*d)
    rr*=row['r'] if t==0 else row['c']*rows['delta']**t.bit_count()*(1-rows['delta'])**(m-t.bit_count())
  p[s]=pp;R[s]=rr
 return p,R

def raw(state,maps):
 dims=list(state);N=1<<sum(dims);truth=[]
 for x in range(N):
  bit=offset=0
  for m in dims:
   if m:bit^=int(((x>>offset)&((1<<m)-1))==0)
   offset+=m
  truth.append(bit)
 truth=bytes(truth);w=k.walsh(truth);actual={s:F(v*v,N*N) for s,v in enumerate(w)}
 p,R=laws(dims,state,maps);k.check(actual==p and sum(R.values())==1)
 offset=queries=0
 for j,m in enumerate(dims):
  for local in range(m):
   i=offset+local;bit=1<<i;queries+=1
   a,b=k.children(truth,i);k.check(F(sum(x!=y for x,y in zip(a,b)),len(a))==maps[j][m]['d'])
   erase=lambda s:(s&(bit-1))|((s>>(i+1))<<i)
   q={s:F(0) for s in range(N//2)};bar=dict(q)
   for s,v in p.items():q[erase(s)]+=v;bar[erase(s)]+=R[s]
   predictions=[]
   for outcome,child in enumerate((a,b)):
    wc=k.walsh(child);pc={s:F(v*v,len(child)**2) for s,v in enumerate(wc)}
    un={s:bar[s]*(pc[s]/(2*q[s]) if q[s] else F(1,2)) for s in q}
    pi=sum(un.values());k.check(pi>0);predictions.append(pi)
    rc={s:v/pi for s,v in un.items()}
    dd=dims.copy();dd[j]-=1;ss=list(state);ss[j]=m-1 if outcome==0 else 0
    expected,expected_ref=laws(dd,ss,maps)
    k.check(pc==expected and rc==expected_ref)
    if m>=2:k.check(pi==(maps[j][m]['pi'] if outcome==0 else 1-maps[j][m]['pi']))
    else:k.check(pi==F(1,2))
   k.check(sum(predictions)==1)
  offset+=m
 return queries

def run(widths,choices):
 maps=[]
 for n,choice in zip(widths,choices):
  rows={row['m']:row for row in history(n,choice)};rows['delta']=F(1,1<<(n-1));maps.append(rows)
 records={}
 @lru_cache(None)
 def reserve(state):
  rr=[rows[m] for rows,m in zip(maps,state)];I=sum(row['I'] for row in rr)
  TC=plus(*(row['TC'] for row in rr));K=plus(*(row['K'] for row in rr));T=k.sub(TC,K);B=k.pos(T);continuations=[]
  for j,m in enumerate(state):
   if not m:continue
   active=list(state);active[j]=m-1;inactive=list(state);inactive[j]=0
   child=scale(plus(reserve(tuple(active)),reserve(tuple(inactive))),F(1,2))
   candidate=k.sub(child,maps[j][m]['E']);B=(max(B[0],candidate[0]),max(B[1],candidate[1]))
   k.check(I==maps[j][m]['d']+(sum(maps[t][v]['I'] for t,v in enumerate(active))+sum(maps[t][v]['I'] for t,v in enumerate(inactive)))/2)
   continuations.append({'block':j,'active':active,'inactive':inactive,'candidate':candidate})
  k.check(F(B[1],k.SCALE)<=LOGE_LO*I)
  records[str(state)]={'state':state,'I':I,'TC':TC,'K':K,'T':T,'B':B,'continuations':continuations}
  return B
 # Visit all declared product profiles, not only one chosen policy.
 for state in product(*(range(n+1) for n in widths)):reserve(state)
 first={tuple(widths)}
 for j,n in enumerate(widths):
  for new in [0,n-1]:ss=list(widths);ss[j]=new;first.add(tuple(ss))
 queries=sum(raw(state,maps) for state in sorted(first))
 return {'widths':widths,'choices':choices,'states':len(records),'raw_profiles':len(first),'raw_queries':queries,'root_B':reserve(tuple(widths)),'records':records}

def main():
 start=time.monotonic();pilot='--pilot' in sys.argv
 families=[[2,3]] if pilot else [[2,2],[2,3],[2,4],[3,3],[3,4],[4,4],[2,3,4]]
 results=[]
 for widths in families:
  for choices in product(['product','source-empty'],repeat=len(widths)):
   results.append(run(widths,choices))
   (ROOT/'out/BLOCK_PARTIAL.json').write_text(json.dumps(serial(results)),encoding='utf-8')
   k.check(time.monotonic()-start<55)
 # Global common attenuation is genuinely lost at the first active width3 query.
 # Within the resulting width2 block the odds ratio is1/3; in untouched width4 it is1.
 left=F(1,4)/(1-F(1,4))/(F(1,2)/(1-F(1,2)))
 right=F(1,8)/(1-F(1,8))/(F(1,8)/(1-F(1,8)))
 k.check(left==F(1,3) and right==1 and left!=right)
 out={'status':'PASS','roots':len(results),'profiles':sum(v['states'] for v in results),'raw_profiles':sum(v['raw_profiles'] for v in results),'raw_queries':sum(v['raw_queries'] for v in results),'assertions':k.ASSERTIONS,'seconds':time.monotonic()-start,'results':results,'global_single_lambda_failure':{'actual_family':[3,4],'root_reference':'actual marginal product','query':'width3 coordinate, active outcome','extension_odds_in_queried_block':left,'extension_odds_in_other_block':right},'scope':'all profile policies certified in frozen finite domain; all dimensions/interleavings proved analytically; no reference renewal'}
 (ROOT/'out'/('BLOCK_PILOT.json' if pilot else 'BLOCKS.json')).write_text(json.dumps(serial(out),indent=2)+'\n',encoding='utf-8')
 print(json.dumps({key:out[key] for key in ['status','roots','profiles','raw_profiles','raw_queries','assertions','seconds']}))
if __name__=='__main__':main()
