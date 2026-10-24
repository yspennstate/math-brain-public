from pathlib import Path
from fractions import Fraction as Q
from functools import lru_cache
from math import comb
import argparse,json,time
R=Path(__file__).resolve().parents[1];BITS=100;DEN=1<<BITS;COUNT=0
def ck(x):
 global COUNT
 COUNT+=1
 assert x
def floorq(q):return Q((q.numerator*DEN)//q.denominator,DEN)
def ceilq(q):return -floorq(-q)
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def scale(a,w):return (a[0]*w,a[1]*w) if w>=0 else (a[1]*w,a[0]*w)
def sub(a,b):return add(a,scale(b,-1))
def con(x):return (Q(x),Q(x))
def show(a):return [str(a[0]),str(a[1])]
def lnunit(q):
 z=(q-1)/(q+1);zl=floorq(z);zh=ceilq(z)
 lo=hi=Q(0);pl=zl;ph=zh
 for j in range(48):
  lo=floorq(lo+2*pl/(2*j+1));hi=ceilq(hi+2*ph/(2*j+1))
  pl=floorq(pl*zl*zl);ph=ceilq(ph*zh*zh)
 tail=ceilq(2*ph/(97*(1-zh*zh)))
 return lo,hi+tail
LN2=lnunit(Q(2))
@lru_cache(None)
def log2(q):
 q=Q(q);assert q>0
 e=q.numerator.bit_length()-q.denominator.bit_length()
 r=q/(Q(2)**e)
 if r<1:e-=1;r*=2
 if r>=2:e+=1;r/=2
 assert 1<=r<2
 lo,hi=lnunit(r)
 return (lo/LN2[1]+e,hi/LN2[0]+e)
def eta(q):return scale(log2(1/q),q) if q else con(0)
def ce(p,q):
 out=con(0)
 for a,b in zip(p,q):
  if a:assert b>0;out=add(out,scale(log2(1/b),a))
 return out
def walsh(v):
 a=list(v);h=1
 while h<len(a):
  for j in range(0,len(a),2*h):
   for t in range(j,j+h):a[t],a[t+h]=a[t]+a[t+h],a[t]-a[t+h]
  h*=2
 return a
def law(v):return [Q(x*x,len(v)**2) for x in walsh(v)]
def influence(v):
 n=len(v).bit_length()-1
 return sum(Q(sum(v[t]!=v[t^(1<<i)] for t in range(len(v))),len(v)) for i in range(n))
def marginal(p,i):
 b=1<<i
 return [p[(t&(b-1))|((t>>i)<<(i+1))]+p[(t&(b-1))|((t>>i)<<(i+1))|b] for t in range(len(p)//2)]
def restrict(v,i,b):
 z=1<<i
 return [v[(t&(z-1))|((t>>i)<<(i+1))|(b<<i)] for t in range(len(v)//2)]
def full(h):
 n=len(h);s=[-1,1,1,1]
 return [1 if not(t&1) else h[(t>>1)%n]*s[(t>>1)//n] for t in range(8*n)]
def fullref(qh):
 n=len(qh)
 return [(qh[T%n]/4+int(T==0))/4 for T in range(4*n) for e in [0,1]]
def spectral(k,m):
 rho=Q(1,1<<k);mu=Q(3,4)**m;beta=(1-mu)/2;p=rho*beta
 H0=sub(con(4),scale(log2(3),Q(9,8)));HG=scale(H0,m)
 LB=add(add(eta(beta*beta),scale(sub(HG,eta(mu*mu)),Q(1,4))),con((1-mu*mu)/2))
 HP=add(sub(eta((1-p)**2),eta(p*p)),add(con(4*k*p),scale(LB,2*rho)))
 K=sub(con(1),scale(log2((1+p*p)/(p*p)),p*p));c=add(HP,K)
 JA=2*k*p+rho*Q(3*m,4)
 Cpar=sub(con(5),scale(log2((9+p)*(1-p)),Q(1,2)))
 Ccon=sub(con(5),add(scale(log2(9+p),Q(5,8)),scale(log2(1+p),Q(3,8))))
 Cend=add(scale(Cpar,1-p),scale(Ccon,p))
 a=p/2;g=(1+a)**2/(2*(1+a*a));hb=add(eta(g),eta(1-g))
 E=scale(sub(con(1),hb),(1+a*a)/2)
 Lq=add(scale(log2((9+p*p)/8),Q(1,2)),scale(log2((9+p*p)/(1+p*p)),p*p/8))
 J=add(Lq,E);Croot=add(scale(c,Q(1,2)),con(3))
 S=sub(con(2-2*p+JA),scale(c,Q(1,2)))
 D=scale(sub(Ccon,con(3)),p/2) if Ccon[0]>3 else con(0)
 rem=sub(sub(S,add(sub(Croot,Cend),E)),D)
 ck(LN2[0]>Q(2,3));ck(H0[0]>Q(17,8));ck(H0[1]<3)
 ck(c[1]<4*(1-p+JA/2));ck(Croot[1]<6+JA);ck(S[0]>0)
 ck(J[1]<Q(5,8));ck(E[0]>=0 and E[1]<p*p)
 ck(Cend[1]<Q(7,2));ck(D[0]>=0 and D[1]<p/16)
 # Exact complete tensor coefficient histogram, never an exponential allocation.
 tot=Q(0);first=Q(0);entropy_const=Q(0);entropy_log3=Q(0)
 for b in range(m+1):
  mult=comb(m,b)*7**b;w=Q(9**(m-b),16**m);mass=mult*w
  tot+=mass;first+=b*mass
  entropy_const+=4*m*mass;entropy_log3+=-2*(m-b)*mass
 ck(tot==1);ck(first==Q(7*m,16));ck(entropy_const==4*m);ck(entropy_log3==Q(-9*m,8))
 if m>=256:
  ck(sub(c,con(JA))[0]>Q(443,128));ck(rem[1]<Q(-123,128))
 return {'k':k,'m':m,'p':str(p),'J_A':str(JA),'c_interval':show(c),'c_minus_J_A':show(sub(c,con(JA))),'root_CE':show(Croot),'original_half_core_bank':show(S),'first_booked_debit':show(J),'conversion_E':show(E),'final_CE':show(Cend),'weighted_positive_terminal_deficit':show(D),'exact_bank_remainder_interval':show(rem),'same_bank_failed':rem[1]<0,'core_rate4':True,'root_rate4':True,'tensor_histogram_exact':True},(p,JA,c,Croot,Cend,S,E)
def truth(k,m):
 N=1<<(k+3*m)
 A=[]
 for y in range(N):
  v=y&((1<<k)-1);z=y>>k;g=1
  for j in range(m):g*=(-1 if ((z>>(3*j))&7)==0 else 1)
  A.append(int(v==0 and g==-1))
 children=[[(-1 if q else 1) if A[y>>1] else (-1 if y&1 else 1) for y in range(2*N)] for q in [0,1]]
 h=[children[t&1][t>>1] for t in range(4*N)];ph=law(h);pc=law(children[0]);qc=[(p+int(i==0))/2 for i,p in enumerate(pc)];qh=[(p+int(i==1))/2 for i,p in enumerate(ph)]
 ck(pc==law(children[1]));ck(sum(qh)==1);p=Q(sum(A),N);JA=influence(A)
 ck(p==Q(1,1<<k)*(1-Q(3,4)**m)/2);ck(JA==2*k*p+Q(1,1<<k)*Q(3*m,4))
 ck(influence(children[0])==1-p+JA/2);ck(influence(h)==1+JA/2)
 f=full(h);pf=law(f);qf=fullref(qh);ck(sum(qf)==1);ck(influence(f)==Q(3,2)+JA/4)
 # Compare direct spectra with complete relabeling and marginal references exactly.
 ck(marginal(ph,0)==pc);ck(marginal(qh,0)==qc)
 for i,z in enumerate(pf):ck(not z or qf[i]>0)
 # Direct literal Walsh reconstruction of the full root for every character (pilot only size512).
 if m==1:
  direct=[]
  for S in range(len(f)):
   w=sum(val*(-1 if (S&t).bit_count()%2 else 1) for t,val in enumerate(f));direct.append(Q(w*w,len(f)**2))
  ck(direct==pf)
 # Retain BOTH actual terminals while checking a proper activation query.
 q1=marginal(qf,1);f0=restrict(f,1,0)
 i=2;q2=marginal(q1,i);p0=law(restrict(f0,i,0));p1=law(restrict(f0,i,1))
 ck([Q(x+y,2) for x,y in zip(p0,p1)]==marginal(law(f0),i));ck(sum(q2)==1)
 cs=ce(pc,qc);root=ce(pf,qf);expected=add(scale(cs,Q(1,2)),con(3))
 # These independently computed interval enclosures must overlap; equality follows
 # from the exact spectrum identities and analytic log scaling, not tolerance.
 ck(root[0]<=expected[1] and expected[0]<=root[1])
 scalar,vals=spectral(k,m);ck(cs[0]<=vals[2][1] and vals[2][0]<=cs[1])
 return {'k':k,'m':m,'n_F':len(f).bit_length()-1,'truth_table_verified':True,'both_query_terminals_retained':True,'root_CE_interval':show(root),'scalar_interval_overlap_only':True}
def main(pilot):
 start=time.perf_counter();out={'status':'IN_PROGRESS','scalar':[],'truth':[]}
 for m in ([1] if pilot else [1,2,4,16,64,128,256]):
  out['scalar'].append(spectral(5,m)[0]);ck(time.perf_counter()-start<60)
  (R/'out').mkdir(exist_ok=True);(R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 for m in ([1] if pilot else [1,2]):out['truth'].append(truth(1,m));ck(time.perf_counter()-start<60)
 # Fixed rational endpoints used by the analytic all-m proof.
 ck(3**3<2**5);ck(Q(9,8)**4<2);ck(Q(3,1024)<Q(1,128));ck(Q(1,4096)<Q(1,128))
 ck(Q(5,16)*256/32+Q(123,128)==Q(443,128));ck(Q(7,2)-Q(443,128)-1==Q(-123,128))
 out.update(status='PASS',assertions=COUNT,runtime_seconds=time.perf_counter()-start)
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({'status':'PASS','assertions':COUNT,'scalar_cases':len(out['scalar']),'truth_cases':len(out['truth']),'runtime_seconds':out['runtime_seconds']}))
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--pilot',action='store_true');main(ap.parse_args().pilot)
