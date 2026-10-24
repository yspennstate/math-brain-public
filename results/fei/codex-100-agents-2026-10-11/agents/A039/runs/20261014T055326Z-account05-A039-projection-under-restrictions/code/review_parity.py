import mixed as M
from fractions import Fraction as F
import json,time
L=M.L
start=time.perf_counter();out=[]
for n in range(1,5):
 t=[-1 if not (s&1) and s&2 else ((-1 if (s>>3).bit_count()%2 else 1) if s&1 and s&4 else 1) for s in range(1<<(n+3))]
 p,d,h,tc,S=M.info(t);Q,c=M.rootref(p,d);A=M.kl(p,Q)
 M.ck(L.ent(p)=={2:F(3)})
 M.ck(d==[F(1,2),F(1,2)]+[F(1,4)]*(n+1))
 children,refs,E,O,rows=M.step(t,Q,1);facts=[M.info(x) for x in children]
 Hc=L.add((4,L.L(F(2))),(-F(9,8),L.L(F(3))))
 M.ck(all(L.ent(f[0])==Hc for f in facts))
 M.ck([sum(f[1]) for f in facts]==[F(n+2,4),F(n+4,4)])
 tcmean=M.scale(F(1,2),M.sumiv(f[3] for f in facts));D=M.sub(M.plus(O,tcmean),A)
 surplus=M.scale(F(1,2),M.sumiv(f[4] for f in facts))
 M.ck(D[1]<F(n,8));M.ck(M.sub(M.scale(F(1,8),surplus),D)[0]>0)
 # Separately reconstruct the exceptional physical outcome from the scalar root.
 w=M.one
 for _ in range(n+1):w=M.mul(w,M.sub(M.one,M.scale(F(4,15),c)))
 q0=M.sub((F(21,40),F(21,40)),M.scale(F(8,75),M.mul(c,w)))
 scalarO=M.scale(F(-1,2),L.log_iv(M.scale(4,M.mul(q0,M.sub(M.one,q0)))))
 M.ck(O[0]<=scalarO[1] and scalarO[0]<=O[1])
 out.append({'n':n,'c':M.enc(c),'D':M.enc(D),'surplus':M.enc(surplus),'reference_only_rows':rows,'scalar_outcome_KL':M.enc(scalarO)})
# Exact integer certificates for all analytic signs, not logarithmic decimal tests.
ints=[(3**9,2**14),(2**159*11**44,3**108*5**60),(3**54*5**30,2**79*11**22),(2**16*7**14,3**9*5**15),(3*2**19,7**7)]
for a,b in ints:M.ck(a>b)
h=L.h;z=F(15,16)
k=L.add((1,h(F(1,4))),(-z,h(F(4,15))))
M.ck(k=={2:F(5,2),3:F(-27,16),5:F(-15,16),11:F(11,16)})
Hc=L.add((4,L.L(F(2))),(-F(9,8),L.L(F(3))))
# Average child TC = (n+2)h(1/4)-Hc. A=H(M)-H(root), H(root)=3.
base=L.add((1,h(F(1,4))),(-1,Hc),(3,L.L(F(2))))
clow=L.add((1,base),(-1,h(z)),(-2*z,h(F(8,15))))
M.ck(clow=={3:F(-9,16),5:F(-15,16),7:F(7,8)})
Hctrl=L.add((1,L.L(F(15))),(-F(14,15),L.L(F(7))))
obound=L.add((F(1,2),L.L(F(4,3))))
cup=L.add((1,base),(-1,h(z)),(-z,Hctrl),(1,obound))
M.ck(cup=={2:F(-2),3:F(-1,8),7:F(7,8)})
result={'status':'INDEPENDENT_RECONSTRUCTION_HOLDS_NO_REPAIR','claim_id':'A038-CERTIFIED-CHILD-SURPLUS-CONVERSION','version':1,'bases':out,'integer_certificates':[{'left':str(a),'right':str(b),'strict':True} for a,b in ints],'checks':M.checks,'runtime_seconds':time.perf_counter()-start}
(M.R/'out/PARITY_REVIEW.json').write_text(json.dumps(result,indent=2),encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k not in ['bases','integer_certificates']}))
