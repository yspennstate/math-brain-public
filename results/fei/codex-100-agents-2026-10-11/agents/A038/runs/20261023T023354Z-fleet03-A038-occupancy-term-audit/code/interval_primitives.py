import json,time,hashlib,sys
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
R=Path(__file__).resolve().parents[1]
START=time.monotonic(); COUNT=0; GRID=10**24
def check(b,label):
 global COUNT
 COUNT+=1
 assert b,label
 if time.monotonic()-START>55: raise RuntimeError('frozen 55-second watchdog')
def floor(x):return F((x*GRID).__floor__(),GRID)
def ceil(x):return F((x*GRID).__ceil__(),GRID)
class V:
 def __init__(self,a,b=None): self.a=F(a);self.b=F(a if b is None else b)
 def __add__(s,t):
  t=val(t);return V(floor(s.a+t.a),ceil(s.b+t.b))
 __radd__=__add__
 def __neg__(s):return V(-s.b,-s.a)
 def __sub__(s,t):return s+-val(t)
 def __rsub__(s,t):return val(t)+-s
 def __mul__(s,t):
  t=val(t);x=[s.a*t.a,s.a*t.b,s.b*t.a,s.b*t.b];return V(floor(min(x)),ceil(max(x)))
 __rmul__=__mul__
 def __truediv__(s,t):
  t=val(t);assert t.a>0;return s*V(floor(1/t.b),ceil(1/t.a))
 def __pow__(s,n):
  assert n>=0
  r=V(1)
  for _ in range(n):r=r*s
  return r
 def out(s):return [str(s.a),str(s.b)]
def val(x):return x if isinstance(x,V) else V(x)
@lru_cache(None)
def ln(q):
 t=(q-1)/(q+1);lo=2*sum((t**(2*j+1)/F(2*j+1) for j in range(24)),F(0));return lo,lo+2*t**49/(49*(1-t*t))
LN2=ln(F(2))
@lru_cache(None)
def lg(q):
 assert q>0
 shift=0
 while q<1:q*=2;shift-=1
 while q>=2:q/=2;shift+=1
 a,b=ln(q);return V(floor(shift+a/LN2[1]),ceil(shift+b/LN2[0]))
def log(v):
 v=val(v);return V(lg(v.a).a,lg(v.b).b)
def entropy(p):return sum((-q*lg(q) for q in p if q),V(0))
def kl(p,q):return sum((w*(lg(w)-log(z)) for w,z in zip(p,q) if w),V(0))
def h(q):return entropy([q,1-q])
def spectrum(t):
 n=len(t);return [F(sum(v*(-1 if (a&s).bit_count()%2 else 1) for a,v in enumerate(t)),n) for s in range(n)]
def remove(s,i):return (s&((1<<i)-1))|((s>>(i+1))<<i)
def restrict(t,i,b):return [v for a,v in enumerate(t) if (a>>i)&1==b]
def node(t):
 a=spectrum(t);p=[x*x for x in a];n=(len(t)).bit_length()-1
 d=[sum((w for s,w in enumerate(p) if s>>i&1),F(0)) for i in range(n)]
 for i in range(n):check(d[i]==F(sum(t[s]!=t[s^(1<<i)] for s in range(len(t))),len(t)),'spectral-edge influence')
 return {'t':t,'a':a,'p':p,'d':d,'I':sum(d),'H':entropy(p),'TC':sum((h(x) for x in d),V(0))-entropy(p)}
def push(N,q,i):
 # q is the incoming JOINT reference, retaining its original prefix mass.
 n=len(q)//2;out=[[V(0) for _ in range(n)] for _ in range(2)]
 for s in range(len(q)):
  if s>>i&1:continue
  j=remove(s,i);u=N['a'][s];v=N['a'][s|(1<<i)];den=2*(u*u+v*v)
  folded=q[s]+q[s|(1<<i)]
  for b in range(2):
   k=(u+(-1 if b else 1)*v)**2/den if den else F(1,2)
   out[b][j]=folded*k
 return out
def positive(x):return V(max(F(0),x.a),max(F(0),x.b))
def main():
 # Coordinates x,a,b,y0,y1. The original u0=0 exposure has reached u=-1.
 mixed='--mixed' in sys.argv
 nonflat='--nonflat4' in sys.argv
 bfirst='--b-first' in sys.argv
 major='--majority' in sys.argv or mixed or nonflat
 dim=7 if nonflat else (6 if major else 5)
 t=[]
 for z in range(1<<dim):
  x,a,b=[(z>>j)&1 for j in range(3)]
  core=(-1 if (z>>3).bit_count()>=2 else 1) if major else (-1 if z>>3==0 else 1)
  if mixed:core=(-1 if z>>5&1 else 1)*(-1 if (z>>3)&3==0 else 1)
  if nonflat:core=(-1 if z>>6&1 else 1)*(-1 if (z>>3)&7==0 else 1)
  t.append((-1 if a else 1) if x==0 else (core if b else 1))
 N=node(t);p=N['p'];z=1-p[0];r=[x/z for x in N['d']]
 expected=([F(8,15)]*2+[F(4,15)]+[F(2,15)]*3) if major else ([F(32,55)]*2+[F(8,55)]*3)
 if mixed:expected=[F(8,15)]*2+[F(4,15),F(2,15),F(2,15),F(4,15)]
 if nonflat:expected=[F(8,15)]*2+[F(4,15)]+[F(1,15)]*3+[F(4,15)]
 check(z==(F(15,16) if major else F(55,64)) and r==expected,'exact source marginals')
 def poly(c):
  x=F(1)
  for v in r:x*=1-c*v
  return 1-c-x
 lo,hi=F(3,4),F(1)
 check(poly(lo)>0 and poly(hi)<0,'positive root bracket')
 derivative_sum=F(0)
 for j,v in enumerate(r):
  term=v
  for k,w in enumerate(r):
   if j!=k:term*=1-F(3,4)*w
  derivative_sum+=term
 check(derivative_sum<1,'strictly negative polynomial derivative on root bracket')
 for _ in range(42):
  mid=(lo+hi)/2
  if poly(mid)>0:lo=mid
  else:hi=mid
 c=V(lo,hi);q=[]
 for s in range(1<<dim):
  if s==0:q.append(V(1-z));continue
  w=V(z)/c
  for j,v in enumerate(r):w=w*(c*v if s>>j&1 else 1-c*v)
  q.append(w)
 def encloses(v,x):return v.a<=x<=v.b
 check(encloses(sum(q,V(0)),1),'reference normalization')
 for j in range(dim):check(encloses(sum((w for s,w in enumerate(q) if s>>j&1),V(0)),N['d'][j]),'reference marginal')
 first_i=2 if bfirst else 1
 A=kl(p,q);qa=push(N,q,first_i);first=[node(restrict(t,first_i,b)) for b in range(2)]
 qa_mass=[sum(row,V(0)) for row in qa]
 Oa=kl([F(1,2)]*2,qa_mass)
 source_first=push(N,[V(w) for w in p],first_i)
 for b in range(2):
  for w,expected in zip(source_first[b],first[b]['p']):check(w.a==w.b==expected/2,'exact first source kernel')
 D1=Oa+sum((v['TC']*F(1,2) for v in first),V(0))-A
 S0=sum(((4*v['I']-v['H'])*F(1,2) for v in first),V(0))
 increments=[];final=[];qs=[];rows=[];refonly=0
 for b in range(2):
  # a is removed, so original y0 is coordinate 2.
  child=first[b];qb=push(child,qa[b],2)
  final_b=[node(restrict(child['t'],2,e)) for e in range(2)]
  source_second=push(child,[V(w) for w in child['p']],2)
  for e in range(2):
   for w,expected in zip(source_second[e],final_b[e]['p']):check(w.a==w.b==expected/2,'exact second source kernel')
  final.extend(final_b);qs.extend([sum(row,V(0)) for row in qb])
  cond=[sum(row,V(0))/qa_mass[b] for row in qb]
  O=kl([F(1,2)]*2,cond)
  inc=O+sum((v['TC']*F(1,2) for v in final_b),V(0))-child['TC']
  increments.append(inc)
  coherent=sum(child['a'][s]*child['a'][s|4]!=0 for s in range(len(child['p'])) if not s&4)
  reference_only_mass=sum((qa[b][s]+qa[b][s|4] for s in range(len(child['p'])) if not s&4 and child['p'][s]+child['p'][s|4]==0),V(0))
  if major:
   if not bfirst or b==1:check(coherent>0,'active next query has strictly positive true erasure')
   check(reference_only_mass.a>0,'source-zero rows have positive inherited reference mass')
  refonly+=sum(child['p'][s]+child['p'][s|4]==0 for s in range(len(child['p'])) if not s&4)
  rows.append({'first_outcome':b,'coherent_source_rows':coherent,'reference_only_incoming_mass':reference_only_mass.out(),'conditional_outcome_KL':O.out(),'incremental_conversion':inc.out(),'incoming_prefix_mass':qa_mass[b].out(),'child_H':child['H'].out(),'child_I':str(child['I']),'terminal_H':[v['H'].out() for v in final_b],'terminal_I':[str(v['I']) for v in final_b]})
 Ototal=kl([F(1,4)]*4,qs)
 Dtotal=Ototal+sum((v['TC']*F(1,4) for v in final),V(0))-A
 telescope=D1+sum((v*F(1,2) for v in increments),V(0))
 check(Dtotal.a<=telescope.b and telescope.a<=Dtotal.b,'inherited-reference telescope')
 Sfinal=sum(((4*v['I']-v['H'])*F(1,4) for v in final),V(0))
 book=positive(D1)+sum((positive(v)*F(1,2) for v in increments),V(0))
 nonflat_bill=None
 if nonflat:
  core=node([(-1 if z>>3&1 else 1)*(-1 if z&7==0 else 1) for z in range(16)])
  check(len(set(w for w in core['p'] if w))>1,'core is genuinely non-flat')
  tcore=F(sum(w==-1 for w in core['t']),16)
  G=h(tcore/2)+sum((h(d/4) for d in core['d']),V(0))
  Hfinal=sum((v['H']*F(1,4) for v in final),V(0))
  Ifinal=sum((v['I']*F(1,4) for v in final),F(0))
  deficit=N['H']-Hfinal-4*(N['I']-Ifinal)
  L=A+positive(deficit)
  check(G.a>2,'marginal-gap sufficient condition fails')
  check(L.b<Sfinal.a,'exact canonical whole liability paid by original retained terminal bank')
  check(L.b<S0.a,'same original intermediate child bank also suffices')
  if bfirst:
   check(deficit.a>0,'actual query deficit is strictly positive')
   check(book.b<=F(11,32),'old conservative booking within uniform allowance')
   check((L+book).b<min(S0.a,Sfinal.a),'full source plus old booking paid without renewed bank')
  nonflat_bill={'core_spectrum':list(map(str,core['p'])),'core_influences':list(map(str,core['d'])),'G':G.out(),'full_liability_L':L.out(),'positive_query_deficit':positive(deficit).out(),'signed_query_deficit':deficit.out(),'remaining_final_owner_after_full_L':(Sfinal-L).out(),'remaining_original_owner_after_full_L':(S0-L).out(),'full_L_plus_old_booking':(L+book).out(),'remaining_final_owner_after_L_and_booking':(Sfinal-L-book).out()}
 # Frozen target is payment, without choosing a post hoc fraction.
 payment=book.b<min(S0.a,Sfinal.a)
 out={'status':'PASS' if payment else 'PAYMENT_UNRESOLVED','assertions':COUNT,'runtime_seconds':time.monotonic()-START,'c_bracket':c.out(),'A':A.out(),'first_conversion_D1':D1.out(),'original_mean_child_surplus':S0.out(),'final_mean_surplus':Sfinal.out(),'positive_bookings':book.out(),'remaining_original_bank':(S0-book).out(),'remaining_final_surplus':(Sfinal-book).out(),'full_tree_conversion':Dtotal.out(),'reference_only_rows_second_query':refonly,'rows':rows,'root_truth_table':t,'root_H':N['H'].out(),'root_I':str(N['I']),'source_kernel_convention':'common erased signed Hadamard kernel; fair on EVERY zero-source row; incoming reference is never reset or replaced'}
 if major:
  check(refonly>0,'reference-only second-query rows exercised')
  check(all(len(set(v['t']))==2 for v in final),'all four terminal functions nonconstant')
 out['assertions']=COUNT
 if nonflat:out['exact_canonical_admission']=nonflat_bill
 out['family']='character times two-bit point defect' if mixed else ('Maj3' if major else 'two-bit point defect')
 if nonflat:out['family']='character times THREE-bit point defect: genuinely non-flat core'
 out['first_query']='b' if bfirst else 'a'
 (R/'out'/('NONFLAT4_B_CHECK.json' if nonflat and bfirst else ('NONFLAT4_CHECK.json' if nonflat else ('MIXED_CHECK.json' if mixed else ('MAJORITY_CHECK.json' if major else 'CHECK.json'))))).write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
 print(json.dumps({k:out[k] for k in ['status','assertions','runtime_seconds','first_conversion_D1','positive_bookings','original_mean_child_surplus','final_mean_surplus','reference_only_rows_second_query']}))
if __name__=='__main__':main()
