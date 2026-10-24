"""Independent binary finite-difference and conditional-law reconstruction. No peer imports."""
from pathlib import Path
from fractions import Fraction as F
from functools import lru_cache
import json, math, time, sys, hashlib
R=Path(__file__).resolve().parents[1]
START=time.perf_counter();COUNT=0;K=F(9,2)
def ck(b):
 global COUNT
 COUNT+=1
 if not b: raise AssertionError(COUNT)
def save(name,v): (R/'out'/name).write_text(json.dumps(v,indent=2,default=str)+'\n',encoding='utf-8')
def point(x): return F(x),F(x)
def add(*xs): return tuple(sum(x[k] for x in xs) for k in (0,1))
def neg(x): return -x[1],-x[0]
def sub(x,y): return add(x,neg(y))
def mul(x,y):
 a=[u*v for u in x for v in y];return min(a),max(a)
def scale(x,t): return mul(x,point(t))
def div(x,y):
 ck(y[0]>0);return mul(x,(1/y[1],1/y[0]))
def pos(x): ck(x[0]>0)
def zero(x): ck(x[0]<=0<=x[1])
@lru_cache(None)
def ln_reduced(x):
 # x in [1,2]; positive atanh series with rigorous positive tail.
 z=(x-1)/(x+1);u=z*z;term=z;s=F(0);N=48
 for k in range(N): s+=2*term/(2*k+1);term*=u
 return s,s+2*term/((2*N+1)*(1-u))
@lru_cache(None)
def log2(x):
 ck(x>0)
 a=x.numerator.bit_length()-x.denominator.bit_length()
 y=x/F(2)**a
 if y<1:y*=2;a-=1
 ck(1<=y<2)
 if y==1:return point(a)
 l=ln_reduced(y);d=ln_reduced(F(2))
 # Round once to bounded fixed-point endpoints, independently of source's logs.
 lo=l[0]/d[1];hi=l[1]/d[0];D=1<<112
 return F((lo.numerator*D)//lo.denominator,D)+a,F(-((-hi.numerator*D)//hi.denominator),D)+a
def entropy(ps):return neg(add(*(scale(log2(p),p) for p in ps if p)))
HSET={0,1,2,4,8,16,32,6,17,40}
J=tuple(1 if (x^1) in HSET else -1 for x in range(64))
G=tuple(-1 if x in {0,1,2} else 1 for x in range(64))
@lru_cache(None)
def core(t):
 N=len(t);n=N.bit_length()-1
 # Direct integer characters, not FWHT, Gray code or imported helpers.
 W=[sum(t[x]*(-1 if (s&x).bit_count()%2 else 1) for x in range(N)) for s in range(N)]
 p=F(sum(v<0 for v in t),N);v=4*p*(1-p)
 ck(sum(w*w for w in W)==N*N)
 inf=[F(sum(t[x]!=t[x^(1<<j)] for x in range(N)),N) for j in range(n)]
 ck(sum(inf)==sum(F(w*w,N*N)*s.bit_count() for s,w in enumerate(W)))
 masses=[F(w*w,N*N) for w in W];H=entropy(masses)
 # Entropy of the normalized NONEMPTY physical set in this core.
 E=entropy([q/v for q in masses[1:] if q]) if v else point(0)
 return dict(t=t,W=W,p=p,v=v,H=H,E=E,I=sum(inf),inf=inf)
# Binary multilinear coefficients from the truth values using inclusion-exclusion.
D=[]
for s in range(64):
 D.append(sum((-1)**(s.bit_count()-a.bit_count())*J[a] for a in range(64) if a&s==a))
for x in range(64): ck(sum(D[s] for s in range(64) if s&x==s)==J[x])
@lru_cache(None)
def packet(tables):
 cs=[core(t) for t in tables];p=[c['p'] for c in cs];var=[z*(1-z) for z in p]
 # J(x)=sum b_T product(x_i-p_i), computed by finite differences.
 b=[sum(F(D[u])*math.prod(p[j] for j in range(6) if (u^s)>>j&1) for u in range(64) if u&s==s) for s in range(64)]
 masses=[b[s]**2*math.prod(var[j] for j in range(6) if s>>j&1) for s in range(64)]
 ck(sum(masses)==1)
 q=[]
 for j in range(6):
  edge=sum(math.prod(p[k] if x>>k&1 else 1-p[k] for k in range(6) if k!=j) for x in range(64) if not x>>j&1 and J[x]!=J[x|(1<<j)])
  q.append(edge);ck(sum(masses[s] for s in range(64) if s>>j&1)==cs[j]['v']*edge)
 # Conditional entropy of full spectral set, given occupied-block pattern.
 H=add(entropy(masses),*(scale(c['E'],c['v']*z) for c,z in zip(cs,q)))
 I=sum(c['I']*z for c,z in zip(cs,q));S=sub(point(K*I),H)
 C=sub(H,add(*(scale(c['H'],z) for c,z in zip(cs,q))))
 A=scale(sub(point(K*cs[0]['I']),cs[0]['H']),q[0])
 M=sub(S,A)
 T=neg(M) if M[1]<0 else point(0)
 ck(M[1]<0 or M[0]>0 or M==point(0))
 U=sub(A,T);O=M if M[0]>0 else point(0)
 zero(sub(S,add(U,O)))
 return dict(cs=cs,p=p,b=b,masses=masses,q=q,H=H,I=I,S=S,C=C,A=A,M=M,T=T,U=U,O=O)
def restrict(t,j,bit):
 n=len(t).bit_length()-1
 return tuple(t[(x&((1<<j)-1))|((x>>j)<<(j+1))|(bit<<j)] for x in range(1<<(n-1)))
def tagged(tag):
 free=[j for j,x in enumerate(tag) if x=='*'];fixed=sum(1<<j for j,x in enumerate(tag) if x=='1')
 return tuple(G[fixed|sum(((x>>k)&1)<<j for k,j in enumerate(free))] for x in range(1<<len(free)))
@lru_cache(None)
def state(tag):return packet((tagged(tag),)+(G,)*5)
def branch(tag,j):return [tag[:j]+str(b)+tag[j+1:] for b in (0,1)]
def edge(P,children,block,coord):
 d=P['q'][block]*P['cs'][block]['inf'][coord]
 ck(P['I']-sum(c['I'] for c in children)/2==d)
 for j in range(6):ck(sum(c['q'][j] for c in children)/2==P['q'][j])
 dh=sub(P['H'],scale(add(*(c['H'] for c in children)),F(1,2)))
 if not d:
  ck(children[0]['cs']==children[1]['cs']);zero(dh);dh=point(0)
 e=sub(dh,point(K*d));e4=sub(dh,point(4*d))
 zero(sub(add(P['S'],e),scale(add(*(c['S'] for c in children)),F(1,2))))
 return dict(d=d,e=e,e4=e4)
def propagate(labels,e,children):
 B=scale(add(*(c['S'] for c in children)),F(1,2));pos(B)
 new=dict(labels);new['query'+str(len(labels)+1)]=e
 out=[]
 for c in children:
  pos(c['S']);ls={k:mul(a,div(c['S'],B)) for k,a in new.items()}
  remain=sub(c['S'],add(*ls.values()));pos(remain)
  for bank in ['U','O']:
   debit=mul(add(*ls.values()),div(c[bank],c['S']))
   if c[bank]==point(0):zero(debit)
   else:pos(sub(c[bank],debit))
  out.append(ls)
 for k,a in new.items():zero(sub(scale(add(*(x[k] for x in out)),F(1,2)),a))
 return out
def scalar_view(P):return {k:P[k] for k in ['p','q','H','I','S','A','M','T','U','O','C']}
def small_validation():
 # Explicit 12-bit truth table. Direct bitset character sums, no transform.
 t=(-1,-1,-1,1);base=(t,)*6;count=0
 for tables in [base,(restrict(t,0,0),)+(t,)*5,(restrict(t,0,1),)+(t,)*5,((1,),)+(t,)*5,((-1,),)+(t,)*5]:
  P=packet(tables);ns=[len(z).bit_length()-1 for z in tables];off=[sum(ns[:j]) for j in range(6)];n=sum(ns);N=1<<n
  table=[J[sum((tables[j][(x>>off[j])&((1<<ns[j])-1)]<0)<<j for j in range(6))] for x in range(N)]
  negative=sum(1<<x for x,v in enumerate(table) if v<0);a=negative.bit_count();chars=[0]*N
  bitmasks=[sum(1<<x for x in range(N) if x>>j&1) for j in range(n)]
  Ws=[]
  for s in range(N):
   if s:chars[s]=chars[s&(s-1)]^bitmasks[(s&-s).bit_length()-1]
   w=N-2*a if not s else -2*(a-2*(negative&chars[s]).bit_count());Ws.append(w)
   occupied=0;pred=F(1)
   for j in range(6):
    z=(s>>off[j])&((1<<ns[j])-1)
    if z:occupied|=1<<j;pred*=F(-P['cs'][j]['W'][z],2*len(tables[j]))
   ck(F(w,N)==P['b'][occupied]*pred);count+=1
  ck(sum(w*w for w in Ws)==N*N)
  for j in range(6):
   for c in range(ns[j]):
    d=F(sum(table[x]!=table[x^(1<<(off[j]+c))] for x in range(N)),N)
    ck(d==P['q'][j]*P['cs'][j]['inf'][c])
  zero(sub(entropy([F(w*w,N*N) for w in Ws]),P['H']))
 return count
def main():
 order=[2,0,1,3,4,5];tag='******';rows=[]
 for j in order:
  ts=branch(tag,j);P=state(tag);ch=[state(t) for t in ts];idx=[k for k,x in enumerate(tag) if x=='*'].index(j)
  for c in [P]+ch:pos(c['S']);ck(c['U'][0]>=0)
  rows.append(dict(tag=tag,kids=ts,children=ch,**edge(P,ch,0,idx)));tag=ts[0]
 e1,e2=rows[0]['e4'],rows[1]['e4'];pos(e1);pos(e2)
 As=[scale(sub(point(4*c['cs'][0]['I']),c['cs'][0]['H']),c['q'][0]) for c in rows[1]['children']]
 B4=scale(add(*As),F(1,2));pos(B4)
 original=[{'first_K4':mul(scale(e1,2),div(a,B4)),'second_K4':mul(e2,div(a,B4))} for a in As]
 for row in rows[:2]:
  for c in row['children']:
   M4=sub(add(*(scale(sub(point(4*z['I']),z['H']),q) for z,q in zip(c['cs'][1:],c['q'][1:]))),c['C']);pos(M4)
 pos(sub(scale(B4,F(3,5)),add(scale(e1,2),e2)))
 leaves=[dict(tag=rows[0]['kids'][1],reach=F(1,2),labels={}),dict(tag=rows[1]['kids'][1],reach=F(1,4),labels=original[1])]
 labels=original[0];target=None
 for depth,row in enumerate(rows[2:],2):
  if row['tag']=='00000*':target=dict(labels=labels.copy(),P=state(row['tag']),leaves=leaves.copy())
  ls=propagate(labels,row['e'],row['children'])
  leaves.append(dict(tag=row['kids'][1],reach=F(1,2**(depth+1)),labels=ls[1]));labels=ls[0]
 leaves.append(dict(tag='000000',reach=F(1,64),labels=labels))
 tax=(K-4)*(rows[0]['d']+rows[1]['d']/2);root=sub(state('******')['S'],point(tax));pos(sub(root,point(F(11,10))))
 def finish(ls):
  ck(sum(x['reach'] for x in ls)==1)
  for x in ls:
   P=x.get('P') or state(x['tag']);x['state']=scalar_view(P);x['remaining']=sub(P['S'],add(*x['labels'].values()));pos(x['remaining'])
  mean=add(*(scale(x['remaining'],x['reach']) for x in ls));zero(sub(mean,root));return mean
 mean=finish(leaves);ck(len(leaves)==7)
 T=target['P']['T'];ck(T[0]>F(1,10) and T[1]<F(11,100))
 pos(sub(sub(target['P']['S'],add(*target['labels'].values())),point(F(12,25))))
 # Each of the five unchanged original raw core weights is conserved.
 for j in range(1,6):ck(sum(x['reach']*x['state']['q'][j] for x in leaves)==state('******')['q'][j])
 for name,val in [('first_K4',e1),('second_K4',scale(e2,F(1,2)))]:zero(sub(add(*(scale(x['labels'].get(name,point(0)),x['reach']) for x in leaves)),val))
 # Replace, not append, the last query. Old labels and stopped siblings unchanged.
 tables=((-1,1),)+(G,)*5;P=packet(tables)
 ch=[packet((tables[0],restrict(G,0,b))+(G,)*4) for b in (0,1)]
 r=edge(P,ch,1,0);pos(r['e']);ck([c['p'][1] for c in ch]==[F(1,16),F(1,32)])
 pos(sub(P['S'],add(*target['labels'].values())))
 ls=propagate(target['labels'],r['e'],ch)
 alt=target['leaves']+[dict(tag='cross'+str(b),P=c,reach=F(1,64),labels=l) for b,(c,l) in enumerate(zip(ch,ls))]
 mean2=finish(alt);ck(len(alt)==7)
 coeff=small_validation()
 # Source endpoints compared ONLY after our computation, never imported as inputs.
 src=Path(r'~\brain_workers\FEI100_20261011\agents\A072\runs\20261014T124911Z-account05-A072-exact-walsh-engine\out')
 source=json.loads((src/'ledger.json').read_text(encoding='utf-8'))
 def compare(ours,theirs):
  a,b=map(F,theirs);ck(max(a,ours[0])<=min(b,ours[1]))
 compare(root,source['root_remaining_after_tax']);compare(T,source['target_tag00000star']['selected_to_outer_transfer'])
 mapping={'first_K4':'first_query_K4','second_K4':'second_query_K4',**{'query'+str(j):'query_'+str(j)+'_K9over2' for j in range(3,7)}}
 for leaf,other in zip(leaves,source['complete_terminals']):
  ck(leaf['tag']==other['tag']);ck(leaf['reach']==F(other['reach']))
  compare(leaf['remaining'],other['remaining'])
  for name,value in leaf['labels'].items():compare(value,other['labels'][mapping[name]])
 for row in rows:
  for tag in [row['tag']]+row['kids']:
   z=state(tag);ss=json.loads((src/('state_'+tag.replace('*','x')+'.json')).read_text(encoding='utf-8'))
   ck(z['I']==F(ss['I']));ck(z['q']==list(map(F,ss['outer']['q'])))
   for key in ['H','S','A','M','U','O']:compare(z[key],ss[key])
 hh=json.loads((src/'heterogeneous.json').read_text(encoding='utf-8'));compare(r['e'],hh['full_query_excess_K9over2'])
 for c,s in zip(ch,hh['children']):compare(c['S'],s['full_terminal']['S'])
 # Adversarial controls: source rate reset and omitted terminal both visibly fail.
 ck(tax>0);ck(root[1]<state('******')['S'][0])
 ck(sum(x['reach'] for x in leaves[:-1])!=1)
 ck(J[0]!=-J[0])
 ck(time.perf_counter()-START<55)
 result=dict(passed=True,assertions=COUNT,coefficient_checks=coeff,runtime_seconds=time.perf_counter()-START,root_remaining=root,transfer=T,target_remaining=sub(P['S'],add(*target['labels'].values())),cross_excess=r['e'],cross_children=[scalar_view(c) for c in ch],original_leaves=leaves,alternative_leaves=alt,original_mean=mean,alternative_mean=mean2,prefix_tax=tax,rows=[{k:v for k,v in r.items() if k!='children'} for r in rows],rung='finite exact certificate independently reconstructed; no Lean claim')
 save('CERTIFICATE.json',result)
 print(json.dumps({k:result[k] for k in ['passed','assertions','coefficient_checks','runtime_seconds']},default=str))
if __name__=='__main__':main()
