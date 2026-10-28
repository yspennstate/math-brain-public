from pathlib import Path
import hashlib,json,time
p=Path(__file__).with_name('check_repair.py')
exec(compile(p.read_text(encoding='utf-8').split('cases=0;coordinates=0')[0],str(p),'exec'))
start=time.monotonic();checks=0
def build(parts):
 vals=[-1]
 for s in parts:
  v=truth(*s)
  vals=compose(tuple(vals),v)
 return tuple(vals)
constp=(0,(),None);constm=(0,(0,),None)
a=(2,(3,),None);b=(3,(3,4),0);c=(3,(1,2),0);d=(1,(1,),None);z=(2,(3,),0)
fixtures=[(a,b,c),(b,b,b),(c,c,c),(d,a,z),(constp,b,c),(constm,b,c),(constm,constm,d)]
@lru_cache(None)
def repair(parts):
 f=build(parts);_,I,H=stats(f)
 if len(set(f))==1:return Q(0),{},Q(0)
 j=next(j for j,s in enumerate(parts) if len(set(truth(*s)))>1)
 s=parts[j];i=pivot(s[0],s[1]);idx=sum(t[0] for t in parts[:j])+i
 f0,f1,di,qi,B=local(f,idx);le(sign(add(B,const(-14*di))),0)
 children=[]
 for bit in (0,1):
  cp=list(parts);cp[j]=child(*s,i,bit);cp=tuple(cp)
  eq(build(cp),(f0,f1)[bit]);children.append(repair(cp))
 tI=di+sum(t[0] for t in children)/2
 tH=add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)),sc(add(children[0][1],children[1][1]),Q(1,2)))
 eq(tI,I);eq(tH,H);le(sign(add(H,const(-17*I))),0)
 if time.monotonic()-start>120:raise TimeoutError('frozen cap')
 return tI,tH,Q(0)
prefixes=0
for parts in fixtures:
 repair(parts)
 f=build(parts);_,I,H=stats(f)
 for j,s in enumerate(parts):
  for i in range(s[0]):
   idx=sum(t[0] for t in parts[:j])+i
   f0,f1,di,qi,B=local(f,idx);zs=[]
   for bit in (0,1):
    cp=list(parts);cp[j]=child(*s,i,bit);cp=tuple(cp)
    eq(build(cp),(f0,f1)[bit]);zs.append(repair(cp))
   eq(I,di+sum(t[0] for t in zs)/2)
   eq(H,add(H,sc(add(stats(f0)[2],stats(f1)[2]),-Q(1,2)),sc(add(zs[0][1],zs[1][1]),Q(1,2))))
   eq(sum(t[2] for t in zs),Q(0));prefixes+=1
out={'status':'PASS','fixture_triples':len(fixtures),'one_query_prefixes':prefixes,'continuation_states':repair.cache_info().currsize,'exact_assertions':checks,'runtime_seconds':time.monotonic()-start,'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'repair_helper_sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
(run/'out'/'MULTI.json').write_text(json.dumps(out,indent=2),encoding='utf-8');print(json.dumps(out))
