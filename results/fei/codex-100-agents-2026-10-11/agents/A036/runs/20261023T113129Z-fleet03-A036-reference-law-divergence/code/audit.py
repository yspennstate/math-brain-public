from fractions import Fraction as F
from collections import defaultdict
from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parents[1];start=time.perf_counter();N=0
def ck(b):
 global N
 N+=1;assert b,N
 assert time.perf_counter()-start<55
def walsh(t):return [sum(t[z]*(-1 if (z&s).bit_count()%2 else 1) for z in range(len(t))) for s in range(len(t))]
def law(t):return [F(a*a,len(t)**2) for a in walsh(t)]
def ref(p):
 q=[p[0]]+[F(5,6)*a for a in p[1:]];q[-1]+=F(1,6)*(1-p[0]);ck(sum(q)==1);ck(all((a==0)==(b==0) for a,b in zip(p,q)));return q
def lift(v):
 t=[1 if not z&1 else v[z>>1] for z in range(2*len(v))];p=law(t);qv=ref(law(v));q=[F(0)]*len(t);q[:2]=p[:2]
 for s in range(1,len(v)):q[2*s]=q[2*s+1]=qv[s]/4
 ck(sum(q)==1);return t,p,q
k=5;d=F(1,1<<k);g=[(-1 if z&1 else 1)*(-1 if z in [2,3] else 1) for z in range(1<<k)];v=[g[z>>1]*(-1 if z==1 else 1) for z in range(2<<k)];ck(F(sum(v[z]!=v[z^1] for z in range(len(v))),len(v))==d)
t,p,q=lift(v);ts=[[t[z] for z in range(len(t)) if z>>1&1==y] for y in [0,1]];ps=[law(a) for a in ts];pb=[p[z]+p[z|2] for z in range(len(p)) if not z&2];qb=[q[z]+q[z|2] for z in range(len(q)) if not z&2]
ck(pb==[(a+b)/2 for a,b in zip(*ps)]);joint=[[qb[z]*(ps[y][z]/(2*pb[z]) if pb[z] else F(1,2)) for z in range(len(pb))] for y in [0,1]];outs=[sum(a) for a in joint];old=[[a/outs[y] for a in joint[y]] for y in [0,1]];ck(sum(outs)==1)
D=2*len(ts[0])**2;groups=defaultdict(int);atoms=[]
for y in [0,1]:
 vy=[v[z] for z in range(len(v)) if z&1==y];tt,pp,new=lift(vy);ck(tt==ts[y]);ck(pp==ps[y]);ck(sum(old[y])==1)
 for z,ppp in enumerate(pp):
  if ppp:
   exponent=ppp*D/2;ck(exponent.denominator==1);groups[old[y][z]/new[z]]+=int(exponent)
 atoms.append({'outcome':str(outs[y]),'source':list(map(str,pp)),'inherited':list(map(str,old[y])),'fresh':list(map(str,new))})
ratio=F(1)
for base,power in groups.items():ratio*=base**power
ck(ratio>1);e=d*d;eta=F(1,6)*(F(3,10)-F(4,5)*e-e*(1+2*e)/(2*(1+4*e*e)));ck(outs==[(1+eta)/2,(1-eta)/2])
# Python's default integer-string limit is a display guard; no arithmetic domain changes.
import sys;sys.set_int_max_str_digits(200000)
certificate={'status':'PASS','k':k,'denominator_D':D,'sigma_exact':'log2(rational_product)/D','product_numerator':str(ratio.numerator),'product_denominator':str(ratio.denominator),'positive_by_integer_comparison':ratio.numerator>ratio.denominator,'likelihood_groups':[{'ratio':str(z),'exponent':v} for z,v in groups.items()],'atoms':atoms,'assertions':N,'seconds':time.perf_counter()-start,'imports_producer':False}
pout=R/'out/INDEPENDENT_CERTIFICATE.json';pout.write_text(json.dumps(certificate,indent=2),encoding='utf-8');print(json.dumps({'status':'PASS','assertions':N,'seconds':certificate['seconds'],'D':D,'certificate_sha256':hashlib.sha256(pout.read_bytes()).hexdigest(),'bytes':pout.stat().st_size}))
