from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,time,sys,itertools,math
import kernel as k
ROOT=Path(__file__).resolve().parents[1];PILOT='--pilot' in sys.argv;FORMULA='--formula' in sys.argv
k.CAP=50 if PILOT else 180;start=time.perf_counter();checks=0
def core(m,point):
 b=[k.bent(y,m) for y in range(1<<m)]
 cm=[b[y] if ((y.bit_count()%2)^(y==point)) else 0 for y in range(1<<m)]
 ba=k.fwht(b);ca=k.fwht(cm)
 return [Q(c,a) for c,a in zip(ca,ba)],Q(sum(bool(c) for c in cm),1<<m)
def formula(m,point,F,J):
 lrows,pi=core(m,point);mult=defaultdict(int)
 for l in lrows:mult[l]+=1
 d=pi/16;out={};missing=1-Q(15,16)**F
 for eps,count in ((1,10),(-1,6)):
  if missing:out[('O',eps)]=(missing*Q(count,16),pi*missing*Q(count,16)*(Q(1)-Q(eps,4))**2+pi*missing*Q(count,256))
 for l,c in mult.items():
  for eps,count in ((1,10),(-1,6)):
   for a in range(F+1):
    for b in range(J+1):
     weight=Q(c,1<<m)*Q(count,16)*math.comb(F,a)*Q(10,16)**a*Q(6,16)**(F-a)*math.comb(J,b)*Q(10,16)**b*Q(6,16)**(J-b)
     w=Q(3,4)**a*Q(5,4)**(F-a)*Q(1,2)**b*Q(3,2)**(J-b)
     U=(1-l)+l*w*(1-Q(eps,4));V=l*w*Q(eps,4)
     out[('C',str(l),eps,a,b)]=(weight*V*V/d,weight*(U*U+V*V))
 assert sum(u for u,r in out.values())==sum(r for u,r in out.values())==1
 return out,d
def coarse(states):
 out=defaultdict(lambda:[Q(0),Q(0)])
 for label,(u,r) in states.items():
  lab=label if label[0]=='O' else label[:3]
  out[lab][0]+=u;out[lab][1]+=r
 return dict(out)
def KL(states):
 result=(Q(0),Q(0))
 for u,r in states.values():
  if u:result=k.add(result,k.mul(k.ratlog(u/r),u))
 return result
def build(m,L,point,fixed):
 labels=[]
 for j in range(L):labels.extend([(j,'x',i) for i in range(4)]+([] if j in fixed else [(j,'z',0)]))
 vals=[]
 for v in range(1<<(m+len(labels))):
  y=v&((1<<m)-1);p=(y.bit_count()%2)^(y==point);sign=k.bent(y,m);offset=m
  for j in range(L):
   x=(v>>offset)&15;offset+=4;z=fixed[j] if j in fixed else (v>>offset)&1
   if j not in fixed:offset+=1
   sign*=k.bent(x,4)*(-1 if p and x==0 and z else 1)
  vals.append(sign)
 return vals,labels
def rowlabel(s,m,L,j,point,fixed,labels,lrows):
 y=s&((1<<m)-1);offset=m;xs={};zs={}
 for h in range(L):
  xs[h]=(s>>offset)&15;offset+=4
  if h not in fixed:zs[h]=(s>>offset)&1;offset+=1
 eps=k.bent(xs[j],4)
 if any(value for h,value in zs.items() if h!=j):return ('O',eps)
 a=sum(k.bent(xs[h],4)==1 for h in range(L) if h!=j and h not in fixed)
 b=sum(k.bent(xs[h],4)==1 for h in fixed if fixed[h]==1)
 return ('C',str(lrows[y]),eps,a,b)
records=[]
if FORMULA:
 for L,J,point in itertools.product((1,2,4,8,16,32,64),(0,1,3),(0,1)):
  k.clock();states,d=formula(2,point,L-1,J);checks+=2
  assert len(states)<=2+8*L*(J+1);checks+=1
  # An arbitrary terminal spectator tensors both laws with the same mass.
  spec=(Q(1,4),Q(3,4));assert sum(u*t for u,r in states.values() for t in spec)==1;checks+=1
  records.append(dict(remaining_modules=L,fixed_one_modules=J,point=point,state_count=len(states),d=str(d),mu_mass='1',reference_mass='1',terminal_spectator_preserved=True))
else:
 cases=[(2,2,1)] if PILOT else list(itertools.product((2,4),(1,2),(0,1)))
 for m,L,point in cases:
  t,_=build(m,L,point,{});H=k.entropy_table(t);I=k.influence(t);contexts=[]
  for j in range(L):
   for history in range(1<<j):
    k.clock();fixed={h:(history>>h)&1 for h in range(j)};t,labels=build(m,L,point,fixed);N=len(t);slot=m+labels.index((j,'z',0));ft=k.fwht(t)
    lrows,pi=core(m,point);d=pi/16;states=defaultdict(lambda:[Q(0),Q(0)]);ratios={}
    for s in range(N):
     if s&(1<<slot):continue
     a,b=ft[s],ft[s^(1<<slot)];assert b;checks+=1
     mu=Q(b*b,N*N)/d;r=Q(a*a+b*b,N*N)
     lab=rowlabel(s,m,L,j,point,fixed,labels,lrows);ratio=mu/r
     if lab in ratios:assert ratios[lab]==ratio
     ratios[lab]=ratio;states[lab][0]+=mu;states[lab][1]+=r;checks+=1
    expected,de=formula(m,point,L-j-1,sum(fixed.values()))
    assert d==de and {a:tuple(v) for a,v in states.items()}==expected;checks+=3
    fullKL=KL(states);small=coarse(states);coarseKL=KL(small);loss=k.sub(fullKL,coarseKL)
    oriented=k.mul(k.sub(k.ratlog(1/d),fullKL),d)
    if L==2 and j==0:assert loss[0]>0;checks+=1
    contexts.append(dict(j=j,history=history,F=L-j-1,J=sum(fixed.values()),d=str(d),trace_states=len(states),coarse_states=len(small),full_KL=k.emit(fullKL),coarse_KL=k.emit(coarseKL),lost_conditional_KL=k.emit(loss),oriented_cost=k.emit(oriented),states={str(lab):dict(mu=str(mu),r=str(r),likelihood=str(ratios[lab])) for lab,(mu,r) in states.items()}))
  records.append(dict(m=m,L=L,point=point,n=m+5*L,root_H=k.emit(H),root_I=str(I),contexts=contexts))
  with (ROOT/'out'/('pilot_cases.jsonl' if PILOT else 'cases.jsonl')).open('a',encoding='utf8') as fp:fp.write(json.dumps(records[-1])+'\n')
out=dict(helper_version='A035-signed-count-trace-v1',runtime_seconds=time.perf_counter()-start,checks=checks,case_count=len(records),contexts=sum(len(r.get('contexts',[])) for r in records),records=records)
name='formula.json' if FORMULA else 'pilot.json' if PILOT else 'validation.json'
(ROOT/'out'/name).write_text(json.dumps(out,indent=2),encoding='utf8')
print(json.dumps({a:b for a,b in out.items() if a!='records'}))
if not FORMULA:
 for r in records:print(r['m'],r['L'],r['point'],[(c['j'],c['history'],c['trace_states'],c['lost_conditional_KL']) for c in r['contexts']])
