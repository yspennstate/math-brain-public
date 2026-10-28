from pathlib import Path
from fractions import Fraction as F
from collections import defaultdict
from math import comb
import json,time,sys,hashlib
R=Path(__file__).resolve().parents[1]; START=time.perf_counter();N=0
D=1<<90;CACHE={}
def ck(x,msg):
 global N
 assert x,msg
 N+=1
 assert time.perf_counter()-START<60,'frozen runtime exceeded'
def rnd(x,up=False):return F(-((-x*D).__floor__()) if up else (x*D).__floor__(),D)
def mul(a,b):return rnd(a[0]*b[0]),rnd(a[1]*b[1],True)
def lnunit(x):
 z=(x-1)/(x+1);z=(rnd(z),rnd(z,True));z2=mul(z,z);v=z;s=(F(0),F(0))
 for j in range(40):
  s=s[0]+2*v[0]/(2*j+1),s[1]+2*v[1]/(2*j+1)
  v=mul(v,z2)
 tail=2*z[1]**81/(81*(1-z[1]**2))
 return s[0],s[1]+tail
LN2=lnunit(F(2))
def log(x):
 if x in CACHE:return CACHE[x]
 orig=x; e=x.numerator.bit_length()-x.denominator.bit_length()
 x=x/(F(2)**e)
 if x<1:x*=2;e-=1
 if x>=2:x/=2;e+=1
 a,b=lnunit(x)
 CACHE[orig]=rnd(e+a/LN2[1]),rnd(e+b/LN2[0],True)
 return CACHE[orig]
def add(*xs):return sum((x[0] for x in xs),F(0)),sum((x[1] for x in xs),F(0))
def scale(a,w):return (a[0]*w,a[1]*w) if w>=0 else (a[1]*w,a[0]*w)
def sub(a,b):return add(a,scale(b,-1))
def val(x):return F(x),F(x)
def eta(x):return scale(log(x),-x) if x else val(0)
def cehist(rows):
 groups=defaultdict(F)
 ck(sum(n*p for n,p,q in rows)==1,'true normalization')
 ck(sum(n*q for n,p,q in rows)==1,'reference normalization')
 for n,p,q in rows:
  ck(n>=0 and p>=0 and q>=0 and (not p or q>0),'support')
  if p:groups[q]-=n*p
 return add(*(scale(log(q),w) for q,w in groups.items()))
def fullcost(rows):
 # Gate reference uniform. True data marginal exactly (P_core*P_s+point0)/2.
 data=[]
 for n,p,q,is0 in rows:
  for multiplicity,mask0 in [(1,True),(3,False)]:
   data.append((n*multiplicity,(p/4+int(is0 and mask0))/2,(q/4+int(is0 and mask0))/2))
 return add(val(1),cehist(data))
def K(t):return sub(val(1),scale(log((1+t)/t),t)) if t else val(1)
def Lq(p):return add(scale(log((9+p*p)/8),F(1,2)),scale(log((9+p*p)/(1+p*p)),p*p/8))
def conversion(p):
 a=p/2;t=(1+a)**2/(2*(1+a*a))
 return scale(add(scale(log(2*t),t),scale(log(2*(1-t)),1-t)),(1+a*a)/2)
def terminals(p):
 cp=add(val(5),scale(log((9+p)*(1-p)),F(-1,2)))
 cc=add(val(5),scale(log(9+p),F(-5,8)),scale(log(1+p),F(-3,8)))
 end=add(scale(cp,1-p),scale(cc,p))
 deficit=(max(F(0),p*(cc[0]-3)/2),max(F(0),p*(cc[1]-3)/2))
 return end,deficit
def hist(k,m):
 rho=F(1,1<<k);mu=F(3,4)**m;beta=(1-mu)/2;p=rho*beta
 H0=add(val(4),scale(log(F(3)),F(-9,8)))
 LB=add(eta(beta*beta),scale(sub(scale(H0,m),eta(mu*mu)),F(1,4)),val((1-mu*mu)/2))
 HP=add(eta((1-p)**2),scale(eta(p*p),-1),val(4*k*p),scale(LB,2*rho))
 c=add(HP,K(p*p));JA=2*k*p+rho*F(3*m,4)
 end,df=terminals(p);E=conversion(p);J=add(Lq(p),E)
 ck(J[1]<F(5,8),'old insertion includes conversion')
 ck(E[0]>=0 and E[1]<p*p,'conversion retained')
 gap=sub(c,val(JA));lower=F(5*m,16)*rho+F(123,128)
 ck(gap[0]>lower,'A020 exact admission no-go')
 S=sub(val(2-2*p+JA),scale(c,F(1,2)))
 remainder=add(end,scale(gap,-1),val(-1-2*p),scale(E,-1),scale(df,-1))
 if m>=256:ck(remainder[1]<F(-123,128),'A020 original half-bank fails')
 ck(S[0]>F(159,128),'positive original half-bank')
 ck(sub(val(6+JA),add(scale(c,F(1,2)),val(3)))[0]>F(291,128),'root eligibility source')
 # Independent exact joint histogram for true child spectra and ONE inherited Q.
 mus=F(3,4)**(m-1);mub=[mus/2,mus];pb=[rho*(1-x)/2 for x in mub]
 rows=[[],[]];rowsbar=[]
 for b in range(m):
  num=comb(m-1,b)*7**b;t=F(9**(m-1-b),16**(m-1))
  for j,nj in [(0,1),(1,3)]:
   emptyG=b==0 and j==0
   gs=[t/4,t if j==0 else F(0)]
   for pad0,npad in [(True,1),(False,(1<<k)-1)]:
    emptyT=emptyG and pad0;ps=[]
    for child in [0,1]:
     ps.append(pb[child]**2 if emptyG else rho*rho*gs[child]/4)
    for u in [0,1]:
     true=[((1-pb[ch])**2 if u and emptyT else ps[ch]) for ch in [0,1]]
     ave=sum(true)/2;is0=not u and emptyT;q=(ave+int(is0))/2;n=num*nj*npad
     for ch in [0,1]:rows[ch].append((n,true[ch],q,is0))
     rowsbar.append((n,ave,q,is0))
 costs=[];res=[]
 for child in [0,1]:
  rr=rows[child];C=fullcost(rr);costs.append(C)
  IG=F(3*(m-1),4)+(1 if child==0 else 0)
  JAc=2*k*pb[child]+rho*IG
  for qsign in [-1,1]:
   If=F(3,2)+(k-1)*pb[child]/2+rho*IG/4+qsign*pb[child]/4
   z=sub(val(4*If),C)
   ck(z[0]>F(15,8),'both physical signs/terminal full reserve')
   ck(sub(z,J)[0]>F(5,4),'SAME old debit paid, no renewal')
   res.append(z)
   ck(JAc>=0 and pb[child]<=F(1,64),'all side conditions')
  # Domination is exact atomwise; no child spectrum reset is performed.
  ck(all(qq>=pp/4 for n,pp,qq,is0 in rr),'inherited Q dominates true by four')
 cb=fullcost(rowsbar);avg=scale(add(*costs),F(1,2))
 ck(not(cb[1]<avg[0] or avg[1]<cb[0]),'independent histogram averaging')
 # Difference in expected physical budget is exactly four times actual pivot.
 beforeI=F(3,2)+(k-1)*p/2+rho*F(3*m,4)/4
 afterI=F(3,2)+(k-1)*p/2+rho*F(3*m-1,4)/4
 ck(beforeI-afterI==rho/16,'actual tensor query pivotal mass')
 # q-erased incoming full cost, explicit same-reference representation.
 beforeC=sub(add(scale(c,F(1,2)),val(3)),Lq(p))
 L=sub(beforeC,avg)
 ck(L[0]>0,'new query complete code charge')
 Wbefore=sub(sub(val(4*beforeI),beforeC),J)
 Wafter=sub(sub(val(4*afterI),avg),J)
 rhs=add(Wbefore,val(-rho/4),L)
 ck(not(Wafter[1]<rhs[0] or rhs[1]<Wafter[0]),'full signed physical telescope')
 # Further ACTUAL padding query. Its reference is another marginal of the SAME Q.
 paddingrows=[[[] for active in [0,1]] for child in [0,1]]
 for b in range(m):
  num=comb(m-1,b)*7**b;t=F(9**(m-1-b),16**(m-1))
  for j,nj in [(0,1),(1,3)]:
   emptyG=b==0 and j==0;gs=[t/4,t if j==0 else F(0)]
   tiny=[pb[ch]**2 if emptyG else rho*rho*gs[ch]/4 for ch in [0,1]]
   tinybar=sum(tiny)/2
   for pad0,npad in [(True,1),(False,(1<<(k-1))-1)]:
    emptyT=emptyG and pad0
    for u in [0,1]:
     is0=not u and emptyT
     erasedparent=(sum((1-x)**2 for x in pb)/2+tinybar) if u and emptyT else 2*tinybar
     q=(erasedparent+int(is0))/2;n=num*nj*npad
     for ch in [0,1]:
      for active in [0,1]:
       true=((1-2*pb[ch])**2 if u and emptyT else 4*tiny[ch]) if active else F(int(u and emptyT))
       paddingrows[ch][active].append((n,true,q,is0))
 padresults=[]
 for ch in [0,1]:
  IG=F(3*(m-1),4)+(1 if ch==0 else 0)
  for active in [0,1]:
   rr=paddingrows[ch][active];CC=fullcost(rr)
   ck(all(q>=pp/8 for n,pp,q,is0 in rr),'second inherited reference dominates by eight')
   for qsign in [-1,1]:
    If=(F(3,2)+(k-2)*pb[ch]+rho*IG/2+qsign*pb[ch]/2) if active else F(3,2)
    z=sub(val(4*If),CC)
    ck(z[0]>F(39,32),'all8 complete padding terminals paid')
    ck(sub(z,J)[0]>F(19,32),'old debit still retained after padding')
    padresults.append(sub(z,J)[0])
 return {'k':k,'m':m,'p':str(p),'c_minus_JA_lower':str(gap[0]),'original_half_bank_remainder_upper':str(remainder[1]),'new_tensor_query_cost_interval':[str(x) for x in L],'minimum_four_terminal_reserve_lower':str(min(z[0] for z in res)),'minimum_four_terminal_reserve_after_old_J_lower':str(min(sub(z,J)[0] for z in res)),'minimum_eight_padding_terminal_reserve_after_old_J_lower':str(min(padresults)),'status':'PASS','private_rows':rows,'costs':costs}
def walsh(x):
 a=list(x);h=1
 while h<len(a):
  for z in range(0,len(a),2*h):
   for j in range(z,z+h):a[j],a[j+h]=a[j]+a[j+h],a[j]-a[j+h]
  h*=2
 return a
def law(x):return [F(y*y,len(x)**2) for y in walsh(x)]
def energy(p):return sum((s.bit_count()*x for s,x in enumerate(p)),F(0))
def marginal(a,i):
 out=[F(0)]*(len(a)//2)
 for s,x in enumerate(a):out[(s&((1<<i)-1))|((s>>(i+1))<<i)]+=x
 return out
def restrict(a,i,b):return [a[(s&((1<<i)-1))|((s>>i)<<(i+1))|(b<<i)] for s in range(len(a)//2)]
def table(k,m):
 # Physical core order: q,u,v_1..v_k, then m three-bit blocks. Gate is last.
 nc=2+k+3*m;M=1<<nc;h=[]
 for z in range(M):
  g=1
  for j in range(m):g*=(-1 if ((z>>(2+k+3*j))&7)==0 else 1)
  active=((z>>2)&((1<<k)-1))==0 and g==-1
  h.append((-1)**(z&1) if active else (-1)**((z>>1)&1))
 ph=law(h);qh=[(x+int(s==1))/2 for s,x in enumerate(ph)]
 f=[1 if not(z>>(nc+2)) else h[z&(M-1)]*([-1,1,1,1][(z>>nc)&3]) for z in range(1<<(nc+3))]
 qr=[qh[z&(M-1)]/16+(F(1,4) if (z&((1<<(nc+2))-1))==0 else 0) for z in range(len(f))]
 ck(sum(qr)==1,'literal root reference')
 ref=marginal(qr,0);ref=marginal(ref,1+k)
 vals=[];Is=[];means=[]
 for qb in [0,1]:
  f0=restrict(f,0,qb)
  for tb in [0,1]:
   fc=restrict(f0,1+k,tb);pc=law(fc)
   C=cehist([(1,p,q) for p,q in zip(pc,ref)]);vals.append(C);Is.append(energy(pc))
   ck(energy(pc)==F(sum(fc[z]!=fc[z^(1<<i)] for z in range(len(fc)) for i in range(len(fc).bit_length()-1)),len(fc)),'direct all physical edges')
 # core erased law is independently the actual average of the two tensor children.
 for qb in [0,1]:
  hp=restrict(h,0,qb);xp=law(hp);new=marginal(xp,1+k)
  x0=law(restrict(hp,1+k,0));x1=law(restrict(hp,1+k,1))
  ck(new==[(a+b)/2 for a,b in zip(x0,x1)],'actual unequal-child erased law')
 ck(vals[0]==vals[2] and vals[1]==vals[3],'cost symmetry retains both physical signs')
 ck(vals[0]!=vals[1],'proper children have unequal spectra/cost')
 # No fresh terminal reference after the padding query, including the offbranch.
 qnext=marginal(ref,1);padding=[]
 for qb in [0,1]:
  for tb in [0,1]:
   f1=restrict(restrict(f,0,qb),1+k,tb)
   for vb in [0,1]:
    ff=restrict(f1,1,vb);pp=law(ff);CC=cehist([(1,p,q) for p,q in zip(pp,qnext)])
    padding.append(CC)
    ck(sum(pp)==1,'literal8 terminal normalization')
 return {'k':k,'m':m,'full_dimension':nc+3,'four_terminal_influences':[str(x) for x in Is],'status':'PASS'}
def main():
 pilot='--pilot' in sys.argv;rs=[];ts=[]
 ck(LN2[0]>F(2,3),'natural log constant')
 ck(31**31>2**152,'h2(1/32)<1/4 exact')
 ck(3**3<2**5,'H0>17/8')
 ck(log(F(3))[0]>1,'H0<3')
 ck(15**15>2**56,'h2(1/16)<1/2 exact')
 for k,m in ([[5,4]] if pilot else [[5,m] for m in [4,8,16,64,256]]):
  rr=hist(k,m);rr.pop('private_rows');rr.pop('costs');rs.append(rr)
  (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps({'status':'RUNNING','rows':rs,'assertions':N}),encoding='utf-8')
 for k,m in ([[1,1]] if pilot else [[1,1],[1,2]]):ts.append(table(k,m))
 out={'status':'PASS','histogram_cases':len(rs),'truth_table_cases':len(ts),'assertions':N,'runtime_seconds':time.perf_counter()-START,'rows':rs,'table_rows':ts,'arithmetic':'Fraction and outward90-bit rational log intervals; no float tolerance'}
 (R/'out'/('PILOT.json' if pilot else 'CHECK.json')).write_text(json.dumps(out,indent=2),encoding='utf-8')
 print(json.dumps({k:v for k,v in out.items() if k not in ['rows','table_rows']}))
if __name__=='__main__':main()
