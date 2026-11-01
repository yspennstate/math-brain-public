from fractions import Fraction as F
from pathlib import Path
from itertools import product
import json,time
import intervals as a
B=Path(__file__).resolve().parents[1];start=time.monotonic();N=0
def ck(v):
 global N
 N+=1
 if not v:raise AssertionError(N)
def ce(p,q):
 out=a.const(0)
 for x,y in zip(p,q):
  if x:out=a.sub(out,a.scale(a.log2(y),x))
 return out
def kl(vals,q):
 p=a.spec(vals);return a.sub(ce(p,q),a.entropy(p))
def infl(vals):return sum((a.influence(vals,i) for i in range((len(vals)-1).bit_length())),F(0))
def sur(vals):return a.sub(a.const(4*infl(vals)),a.entropy(a.spec(vals)))
def overlaps(u,v):return max(u[0],v[0])<=min(u[1],v[1])
def entropy_upper(p):
 # All <=3-bit squared coefficients have one of these five values.
 return sum(({F(0):F(0),F(1):F(0),F(1,4):F(1,2),F(1,16):F(1,4),F(9,16):F(15,32)}[x] for x in p),F(0))
def ref(vals,theta=F(1,6)):
 p=a.spec(vals);mask=sum(1<<i for i in range((len(vals)-1).bit_length()) if a.influence(vals,i))
 if not mask:return p
 q=[p[0]]+[(1-theta)*x for x in p[1:]];q[mask]+=theta*(1-p[0])
 ck(sum(q)==1 and all(not x or y>0 for x,y in zip(p,q)))
 return q
def act(vals,q,eps):
 vv=tuple(eps if not (j&1) else vals[j>>1] for j in range(2*len(vals)))
 p=a.spec(vv);Q=[F(0)]*len(p);Q[:2]=p[:2]
 for s in range(1,len(q)):Q[2*s]=Q[2*s+1]=q[s]/4
 ck(sum(Q)==1)
 return vv,Q
def fresh_act(factors,eps):
 vals=(1,);q=[F(1)]
 for ff in factors:
  vals=tuple(x*y for y in ff for x in vals);fq=ref(ff);q=[x*y for y in fq for x in q]
 return act(vals,q,eps)
def exact_reset_sign(children,old,new):
 # Common integer multiplier clears every physical source weight.
 L=2*max(len(x) for x in children)**2;ratio=F(1)
 for vals,qq,rr in zip(children,old,new):
  for p,q,r in zip(a.spec(vals),qq,rr):
   if p:
    power=p*L/2;ck(power.denominator==1)
    ratio*=(q/r)**power.numerator
 return ratio,L
certificate=[]
ck(3**12>2**19)
ck(6**15<2**4*5**15) # log2(6/5)<4/15, hence six prices<8/5<7/4.
for n in range(4):
 for values in product((-1,1),repeat=2**n):
  p=a.spec(values);I=infl(values);v=1-p[0];hu=entropy_upper(p)
  slack=4*I-hu-F(7,4)*v
  ck(slack>=0)
  certificate.append({'n':n,'values':list(values),'spectrum':[str(x) for x in p],'I':str(I),'variance':str(v),'H_upper':str(hu),'slack':str(slack)})
(B/'out/FACTOR_CERTIFICATE.json').write_text(json.dumps({'log_certificate':'3^12>2^19','coefficient':'7/4','rows':certificate},indent=2)+'\n',encoding='utf8')

# Independent verification: direct character sums and undirected edges, not Walsh helper.
for row in certificate:
 vals=row['values'];n=row['n'];size=1<<n
 p=[]
 for s in range(size):
  raw=sum(value*(-1 if (s&x).bit_count()%2 else 1) for x,value in enumerate(vals))
  p.append(F(raw*raw,size*size))
 I=F(sum(vals[x]!=vals[x^(1<<i)] for i in range(n) for x in range(size) if not x&(1<<i)),size//2) if n else F(0)
 ck(p==[F(x) for x in row['spectrum']] and I==F(row['I']))
 ck(4*I-entropy_upper(p)-F(7,4)*(1-p[0])==F(row['slack'])>=0)

small=0
for n in range(3):
 for values in product((-1,1),repeat=2**n):
  q=ref(values)
  for i in range(n):
   if not a.influence(values,i):continue
   ch,old=a.node(tuple(values),q,i);new=[ref(x) for x in ch]
   ratio,L=exact_reset_sign(ch,old,new);ck(ratio<=1);small+=1
ck(small==26)

g=(1,-1,-1,1,-1,1,1,1);p=a.spec(g)
ck(p==[F(1,16)]*7+[F(9,16)])
ck(infl(g)==F(9,4))
witness=[]
for theta in (F(1,12),F(1,6),F(1,3),F(2,3)):
 ch,old=a.node(g,ref(g,theta),0);new=[ref(x,theta) for x in ch]
 ratio,L=exact_reset_sign(ch,old,new)
 R=4*(2+theta)/((2-theta)**3*(1+2*theta))
 ck(R>1 and ratio==R**(L//8))
 ck(old[0]==[F(0),F(0),F(0),F(1)])
 ck(old[1]==[F(1,4),(1-theta)/(2*(2-theta)),(1-theta)/(2*(2-theta)),(2+theta)/(4*(2-theta))])
 ck(old[1]==ref(ch[1],theta/(2-theta)))
 witness.append({'theta':str(theta),'ratio_sigma_times8':str(R)})
theta=F(1,6);K=F(155,156)**13*F(59,60)**5*F(13,12)**10/(F(4,3)**2*(1-F(7,195)**2)**16)
ck(K>1)
activations=[]
for eps in (-1,1):
 vals,Q=act(g,ref(g),eps);ch,old=a.node(vals,Q,1)
 corechildren=[tuple(a.restrict(g,0,b)) for b in (0,1)]
 fresh=[act(v,ref(v),eps)[1] for v in corechildren]
 ratio,L=exact_reset_sign(ch,old,fresh)
 ck(ratio**32==K**L)
 sig=a.const(0)
 for vv,qq,rr in zip(ch,old,fresh):sig=a.add(sig,a.scale(a.sub(kl(vv,rr),kl(vv,qq)),F(1,2)))
 ck(sig[0]>0 and overlaps(sig,a.scale(a.log2(K),F(1,32))))
 activations.append({'eps':eps,'sigma_interval':a.outiv(sig)})

# The actual ORIGINAL F_h lift, not a free incoming calibration.
def root(factors):
 vals=(1,);q=[F(1)]
 for ff in factors:
  vals=tuple(x*y for y in ff for x in vals);fq=ref(ff);q=[x*y for y in fq for x in q]
 fv=a.fixture(vals);pf=a.spec(fv);Q=[F(0)]*len(pf);Q[:8]=pf[:8]
 for s in range(1,len(q)):
  for c in (0,1,4,5):Q[8*s+c]=q[s]/16
 ck(sum(Q)==1);return fv,Q
histories=[]
for copies in (1,2):
 factors=[g]*copies;fv,Q=root(factors);A0=kl(fv,Q);H0=a.entropy(a.spec(fv));I0=infl(fv)
 M0=a.sub(a.const(4*I0),ce(a.spec(fv),Q));ck(M0[0]>1)
 bc,bq=a.node(fv,Q,2);ac,aq=a.node(bc[1],bq[1],1)
 frontier=[]
 for branch in (0,1):
  eps=(-1)**branch;vv,rr=fresh_act(factors,eps)
  ck(vv==ac[branch] and rr==aq[branch])
  labels=[(j,i) for j in range(copies) for i in range(3)]
  frontier.append({'vals':vv,'q':aq[branch],'factors':factors,'labels':labels,'eps':eps,'weight':F(1,4)})
 sigma=a.const(0);query_release=a.sub(A0,a.add(a.scale(kl(bc[0],bq[0]),F(1,2)),a.add(a.scale(kl(ac[0],aq[0]),F(1,4)),a.scale(kl(ac[1],aq[1]),F(1,4)))))
 steps=[]
 for stage in range(min(5,3*copies)):
  nex=[];inc=a.const(0)
  for node in frontier:
   labels=node['labels'];idx=0 if node['eps']==1 else len(labels)-1
   factor,originalbit=labels[idx];ch,qs=a.node(node['vals'],node['q'],idx+1)
   qrelease=a.sub(kl(node['vals'],node['q']),a.scale(a.add(kl(ch[0],qs[0]),kl(ch[1],qs[1])),F(1,2)))
   query_release=a.add(query_release,a.scale(qrelease,node['weight']))
   pos=sum(1 for j in range(idx) if labels[j][0]==factor)
   for outcome in (0,1):
    ff=list(node['factors']);ff[factor]=tuple(a.restrict(ff[factor],pos,outcome))
    vv,rr=fresh_act(ff,node['eps']);ck(vv==ch[outcome])
    w=node['weight']/2;ds=a.sub(kl(vv,rr),kl(vv,qs[outcome]));inc=a.add(inc,a.scale(ds,w))
    nex.append({'vals':vv,'q':rr,'factors':ff,'labels':labels[:idx]+labels[idx+1:],'eps':node['eps'],'weight':w})
  sigma=a.add(sigma,inc);frontier=nex
  S=a.scale(sur(bc[0]),F(1,2));Hf=a.scale(a.entropy(a.spec(bc[0])),F(1,2));If=infl(bc[0])/2
  finalKL=a.scale(kl(bc[0],bq[0]),F(1,2))
  for node in frontier:
   w=node['weight'];S=a.add(S,a.scale(sur(node['vals']),w));Hf=a.add(Hf,a.scale(a.entropy(a.spec(node['vals'])),w));If+=w*infl(node['vals']);finalKL=a.add(finalKL,a.scale(kl(node['vals'],node['q']),w))
  e=a.sub(a.sub(H0,Hf),a.const(4*(I0-If)));net=a.add(a.add(A0,e),sigma)
  remaining=a.sub(S,(max(F(0),net[0]),max(F(0),net[1])))
  ck(remaining[0]-F(1,4)>=F(3,4)-F(1,2**65))
  ck(overlaps(a.add(A0,sigma),a.add(query_release,finalKL)))
  ck(query_release[0]>=-F(1,2**65))
  if copies==1 and stage==0:
   ck(inc[0]>0 and overlaps(inc,a.scale(a.log2(K),F(1,64))))
  steps.append({'generation':stage+1,'frontier_nodes':len(frontier),'actual_signed_reset':a.outiv(inc),'cumulative_reset':a.outiv(sigma),'remaining_after_old_quarter':a.outiv(a.sub(remaining,a.const(F(1,4))))})
 histories.append({'copies':copies,'root_bits':(len(fv)-1).bit_length(),'steps':steps})
out={'status':'PASS','assertions':N,'channel_assertions':a.COUNT,'factor_cases':len(certificate),'small_essential_queries':small,'pure_witness':witness,'activation_witness':activations,'K':str(K),'histories':histories,'runtime_seconds':time.monotonic()-start,'scope':'Exact finite certificates and analytic extension in PROOF; no all-dimensional FEI conclusion'}
(B/'out/CHECK.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf8')
print(json.dumps({k:out[k] for k in ('status','assertions','channel_assertions','factor_cases','small_essential_queries','runtime_seconds')}))
