from pathlib import Path
import json,sys,time
HERE=Path(__file__).resolve().parents[1]
OLD=HERE.parent/'20261023T014805Z-fleet03-A047-boundary-search/code/check.py'
exec(compile(OLD.read_text(encoding='utf-8').split('cases=')[0],str(OLD),'exec'))
ROOT=HERE
ALPHA=F(1,6)

def reference(t):
 p,_=spec(t)
 if len(p)==1:return p.copy()
 essential=0
 for s in p:essential|=s
 v=1-p.get(0,F(0));q={s:(1-ALPHA)*w for s,w in p.items()}
 q[0]=p.get(0,F(0))
 q[essential]=q.get(essential,F(0))+ALPHA*v
 return {s:w for s,w in q.items() if w}

def activation(t,eps,char):
 n=len(t).bit_length()-1
 return tuple(eps if not z&1 else t[(z>>1)&((1<<n)-1)]*(-1 if char and z>>(n+1)&1 else 1) for z in range(len(t)*2*(2 if char else 1)))

def lift(t,qcore,eps,char):
 pg,_=spec(t);mu=F(sum(t),len(t))*(0 if char else 1)
 qg={s|(b<<(len(t).bit_length()-1)):w for s,w in qcore.items() for b in ([1] if char else [0])}
 q={0:(eps+mu)**2/4,1:(eps-mu)**2/4}
 for s,w in qg.items():
  if s:
   q[s<<1]=w/4;q[(s<<1)|1]=w/4
 return {s:w for s,w in q.items() if w}

rows=[];positive=[];pilot='--pilot' in sys.argv
(ROOT/'out').mkdir(exist_ok=True)
logfile=ROOT/'out'/('PILOT_CASES.jsonl' if pilot else 'SEARCH_CASES.jsonl')
logfile.write_bytes(b'')
def examine(t,n,code,j,kind,eps=1,char=False):
 coreq=reference(t);children=[restrict(t,j,b) for b in [0,1]]
 if kind=='core':
  actual=t;q=coreq;coord=j;fresh=[reference(z) for z in children]
 else:
  actual=activation(t,eps,char);q=lift(t,coreq,eps,char);coord=j+1
  fresh=[lift(z,reference(z),eps,char) for z in children]
 p,_=spec(actual)
 ts,cc,qs,E,O=step(actual,tuple(range(len(actual).bit_length()-1)),q,coord)
 sig=scale(add(*(add(kl(spec(z)[0],fq),scale(kl(spec(z)[0],oq),-1)) for z,fq,oq in zip(ts,fresh,qs))),F(1,2))
 lo,hi=bounds(sig)
 sign='ZERO' if not sig else 'NEGATIVE' if hi<0 else 'POSITIVE' if lo>0 else 'UNRESOLVED'
 ck(sign!='UNRESOLVED')
 extra=bool(set(q)-set(p)) or any(set(fq)-set(spec(z)[0]) for z,fq in zip(ts,fresh))
 row={'n':n,'code':code,'coordinate':j,'kind':kind,'epsilon':eps if kind!='core' else None,'character_spectator':char,'sign':sign,'interval':[str(lo),str(hi)],'reference_only_support':extra}
 rows.append(row)
 with logfile.open('a',encoding='utf-8',newline='') as f:f.write(json.dumps(row)+'\n')
 if sign=='POSITIVE':
  positive.append(row)
  if len(positive)<=12:
   out=dict(row,truth_table=list(t),query_truth_table=list(actual),old_reference={str(k):str(v) for k,v in q.items()},inherited=[{str(k):str(v) for k,v in z.items()} for z in qs],fresh=[{str(k):str(v) for k,v in z.items()} for z in fresh],exact_log_form={str(k):str(v) for k,v in sig.items()})
   save(('PILOT_' if pilot else '')+f'POSITIVE_{len(positive)}.json',out)

for n in ([3] if pilot else [2,3]):
 for code in range(8 if pilot else 1<<((1<<n)-1)):
  t=(1,)+tuple(1-2*((code>>(z-1))&1) for z in range(1,1<<n))
  for j in range(n):
   if restrict(t,j,0)==restrict(t,j,1):continue
   examine(t,n,code,j,'core')
   for eps in [-1,1]:
    for char in [False,True]:examine(t,n,code,j,'activation',eps,char)

result={'status':'PASS','cases':len(rows),'positive_count':len(positive),'same_support_positive_count':sum(not x['reference_only_support'] for x in positive),'counts':{s:sum(x['sign']==s for x in rows) for s in ['NEGATIVE','ZERO','POSITIVE','UNRESOLVED']},'assertions':COUNT,'runtime_seconds':time.perf_counter()-START,'pilot':pilot,'positive_examples':positive[:12],'rung':'exact finite signs; no all-dimensional inference'}
save('PILOT.json' if pilot else 'SEARCH.json',result)
print(json.dumps(result))
