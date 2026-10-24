import sys,json,time,itertools
from pathlib import Path
from fractions import Fraction as F
ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT.parent/'20261011T232716Z-account05-A026-good-coordinate-erasure'/'code'
sys.path.insert(0,str(OLD))
import transitive as b
import transitive_v2 as v
b.logint=v.logint;b.LN2=v.LN2
K={2:F(5),3:F(-3)}
def add(e,f,scale=F(1)):
 for p,c in f.items():
  e[p]=e.get(p,F(0))+scale*c
  if not e[p]:del e[p]
def phi(a,c):
 e={};b.phi(e,a,c);return e
def B(W,i):
 N=len(W);e={}
 for t in range(N):
  if not t&(1<<i):add(e,phi(F(W[t]**2,N*N),F(W[t|(1<<i)]**2,N*N)))
 return e
def positive(e):
 if not e:return True
 lo,hi=b.interval(e)
 assert lo>=0,('uncertified sign',b.serial(e),str(lo),str(hi))
 return True
def truths(n):
 for mask in range(1<<(1<<n)):
  yield mask,[1 if mask&(1<<x) else -1 for x in range(1<<n)]
def inner(n):
 ans=[]
 for mask,h in truths(n):
  W=b.walsh(h);N=len(h);rows=[]
  for i in range(n):
   d=F(sum(h[x]!=h[x^(1<<i)] for x in range(N)),N)
   gamma=F(W[1<<i],N)
   assert abs(gamma)<=d
   rows.append((i,gamma,d,B(W,i)))
  ans.append((mask,h,F(W[0],N),rows))
 return ans
def scalar():
 rows=[]
 for j,l in itertools.product(range(33),repeat=2):
  a,c=F(j,8),F(l,8)
  excess=phi((a+c)**2,1);add(excess,phi(a*a,1),-1);add(excess,phi(c*c,1),-1)
  difference=dict(K);add(difference,excess,-1);positive(difference)
  rows.append({'a':str(a),'b':str(c),'margin_prime_log':b.serial(difference)})
 sharp=phi(F(1,2),1);add(sharp,phi(F(1,8),1),-2)
 assert sharp==K
 (ROOT/'out/scalar_certificate.json').write_text(json.dumps({'status':'PASS','grid_cases':len(rows),'sharp_squared_parameters':['1/8','1/8','1/2'],'sharp_excess_prime_log':b.serial(sharp),'proof':'PROOF.md section 1 is the continuous proof','records':rows},indent=2)+'\n',encoding='utf-8')
 return len(rows)
def run(pilot,skip=0,tag=None):
 start=time.perf_counter();cache={n:inner(n) for n in range(4 if not pilot else 3)}
 cases=coords=signs=seen=0;negative=0;example=None
 stem=tag if tag else ('pilot' if pilot else 'main')
 path=ROOT/'out'/(stem+'_rows.jsonl')
 assert not path.exists(),'use new output version on retry'
 with path.open('w',encoding='utf-8') as out:
  for nf in range(1,3 if pilot else 4):
   encoder_ns=range(3 if pilot or nf==3 else 4)
   for mask,f in truths(nf):
    NR=1<<(nf-1)
    A=[(f[2*r+1]+f[2*r])//2 for r in range(NR)]
    D=[(f[2*r+1]-f[2*r])//2 for r in range(NR)]
    delta=F(sum(d*d for d in D),NR);AW,DW=b.walsh(A),b.walsh(D)
    shadow=B(b.walsh(f),0)
    for nh in encoder_ns:
     for hm,h,mu,innerrows in cache[nh]:
      seen+=1
      if seen<=skip:continue
      NH=len(h);truth=[f[2*(x>>nh)+(h[x&(NH-1)]==1)] for x in range(NR*NH)]
      W=b.walsh(truth);N=len(truth)
      assert sum(w*w for w in W)==N*N
      for i,gamma,d,Bh in innerrows:
       actual=B(W,i);collision={};unshifted={}
       for a,q in zip(AW,DW):
        add(collision,phi((F(a,NR)+mu*F(q,NR))**2,gamma*gamma*F(q*q,NR*NR)))
        add(unshifted,phi(F(a*a,NR*NR),gamma*gamma*F(q*q,NR*NR)))
       prediction=b.mul(Bh,delta);add(prediction,phi(mu*mu,gamma*gamma),-delta);add(prediction,collision)
       assert prediction==actual
       physical=F(sum(truth[x]!=truth[x^(1<<i)] for x in range(N)),N)
       assert physical==delta*d==F(sum(W[t]**2 for t in range(N) if t&(1<<i)),N*N)
       shift=dict(collision);add(shift,phi(mu*mu,gamma*gamma),-delta);add(shift,unshifted,-1)
       if shift and b.interval(shift)[1]<0:
        negative+=1
        if example is None:example={'outer_n':nf,'outer_mask':mask,'inner_n':nh,'inner_mask':hm,'coordinate':i,'signed_shift_prime_log':b.serial(shift),'interval':b.iv(b.interval(shift))}
       margin=b.mul(K,delta*gamma*gamma);add(margin,shift,-1);positive(margin);signs+=1
       rhs=b.mul(Bh,delta);add(rhs,shadow,gamma*gamma);add(rhs,K,delta*gamma*gamma)
       if gamma:b.lograt(rhs,1/(gamma*gamma),delta*gamma*gamma)
       add(rhs,actual,-1);positive(rhs);signs+=1;coords+=1
      cases+=1
      out.write(json.dumps({'outer_n':nf,'outer_mask':mask,'inner_n':nh,'inner_mask':hm,'status':'PASS'})+'\n')
      if time.perf_counter()-start>(60 if pilot else 120):raise RuntimeError('frozen runtime guard')
   out.flush()
 summary={'helper_version':'A026-shadow-transfer-v1','status':'PASS','cases':cases,'coordinate_identity_checks':coords,'rigorous_sign_checks':signs,'negative_signed_shifts':negative,'first_negative_shift':example,'elapsed_seconds':time.perf_counter()-start,'arithmetic':'integer Walsh/physical edges; exact Fraction prime-log identities; outward dyadic 48-term atanh intervals'}
 summary['skipped_previously_completed_cases']=skip
 (ROOT/'out'/(stem+'_summary.json')).write_text(json.dumps(summary,indent=2)+'\n',encoding='utf-8')
 print(json.dumps(summary,indent=2))
def ownership():
 # AND2 has flat four-atom spectrum: each coordinate B=1,H=2.
 f=[-1,-1,-1,1];h=f[:];BW=B(b.walsh(f),0)
 assert BW=={2:F(1)}
 root_gamma2=F(1,4);active_child_gamma2=F(1)
 Q=root_gamma2+F(1,2)*active_child_gamma2
 assert Q==F(3,4)
 r={'status':'PASS','outer':'AND2(z,r)','encoder':'AND2(x1,x2)','actual_composition':'AND3','root_shadow_B':str(BW[2]),'shadow_entropy_at_root_and_active_child':'2','uniform_shadow_entropy_drop_on_encoder_queries':'0','positive_shadow_charge':str(Q),'physical_encoder_plus_probability':'1/4','uniform_shadow_z_plus_probability':'1/2','actual_terminal_entropy':'0','scope':'unchanged-shadow entropy cannot be a decreasing physical reserve; no FEI counterexample'}
 (ROOT/'out/ownership_control.json').write_text(json.dumps(r,indent=2)+'\n',encoding='utf-8')
if __name__=='__main__':
 (ROOT/'out').mkdir(exist_ok=True)
 pilot=sys.argv[1]=='pilot'
 if pilot:scalar();ownership()
 run(pilot)
