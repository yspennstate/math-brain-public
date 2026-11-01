"""Independent integer Walsh/physical restriction audit; no producer code imported."""
from pathlib import Path
from fractions import Fraction as F
import itertools, json, time, sys, hashlib
import arithmetic as ar

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'out'
COUNT=0
def ck(v):
 global COUNT
 COUNT+=1
 assert v,COUNT
def dump(name,obj):
 (OUT/name).write_text(json.dumps(obj,indent=2)+'\n',encoding='utf-8')
def fw(v):
 w=list(v); step=1
 while step<len(w):
  for i in range(0,len(w),2*step):
   for j in range(i,i+step):
    a,b=w[j],w[j+step];w[j],w[j+step]=a+b,a-b
  step*=2
 return [F(x,len(v)) for x in w]
def delete(x,j):return (x&((1<<j)-1))|((x>>(j+1))<<j)
def restrict(v,j,t):
 return [v[(x&((1<<j)-1))|((x>>j)<<(j+1))|(t<<j)] for x in range(len(v)//2)]
def marginal(v,j):
 w=[F(0)]*(len(v)//2)
 for x,p in enumerate(v):w[delete(x,j)]+=p
 return w

ORIGINAL=(1,0,0,0,-1,1,1,1,1,0,0,0,1,-1,-1,-1)
def controller(pattern):
 live=[j for j,t in enumerate(pattern) if t==2]
 vals=[]
 for x in range(1<<len(live)):
  full=sum((pattern[j] if pattern[j]!=2 else ((x>>live.index(j))&1))<<j for j in range(4))
  vals.append(ORIGINAL[full])
 return vals

def run(pilot=False):
 started=time.perf_counter();limit=55 if pilot else 180
 patterns=[(2,2,2,2)] if pilot else list(itertools.product(range(3),repeat=4))
 ks=[3] if pilot else [3,4,5,6]
 families=nodes=positive=zero=0;witness=None;gram=None
 for pattern in patterns:
  a=controller(pattern);r=len(a).bit_length()-1;b=[1-t*t for t in a]
  A,B=fw(a),fw(b);beta=sum(t*t for t in B)
  ck(beta==F(sum(b),len(b)))
  C=sum(x*x*y*y for x,y in zip(A,B));D=sum(x*y**3 for x,y in zip(A,B));E=sum(y**4 for y in B)
  gamma=C-D*D/E if E else F(0);ck(gamma>=0)
  if pattern==(2,2,2,2):
   ck((C,D,E,gamma,beta)==(F(3,512),F(3,256),F(21,512),F(9,3584),F(3,8)))
   gram={'C':str(C),'D':str(D),'E':str(E),'Gamma':str(gamma),'beta':str(beta)}
  for k in ks:
   for sigma in [-1,1]:
    families+=1
    v=[a[x&((1<<r)-1)]+sigma*b[x&((1<<r)-1)]*(-1 if (x>>r).bit_count()%2 else 1) for x in range(1<<(r+k))]
    ck(set(v)<=set([-1,1]));coeff=fw(v);p=[x*x for x in coeff]
    expected=[F(0)]*len(v)
    for U in range(1<<r):expected[U]=A[U]**2;expected[U|(((1<<k)-1)<<r)]=B[U]**2
    ck(p==expected);ck(sum(p)==1)
    icont=sum(U.bit_count()*(A[U]**2+B[U]**2) for U in range(1<<r))
    ck(ar.ib(p)==icont+k*beta)
    # Physical edge counting is independent of the Fourier identity.
    influences=ar.edges(v)
    ck(sum(influences)==ar.ib(p));ck(all(t==beta for t in influences[r:]))
    if k==3 and pattern==(2,2,2,2):ck(coeff==ar.spectrum(v))
    H=ar.ent(p)
    ck(H[1]<r+1+F(1,10**20))
    for jj in range(k):
     nodes+=1;j=r+jj
     ck(sum(F(v[x])*(-1 if (x>>j)&1 else 1) for x in range(len(v)))==0)
     qold=marginal(expected,j)
     ck(all(not(p[x] and p[x^(1<<j)]) for x in range(len(p)))) # B_j=0, no occupied-pair ambiguity
     # Q=P gives actual conditional occupancy KL identically zero on every fiber.
     for x in range(len(qold)):
      if qold[x]:
       lo=(x&((1<<j)-1))|((x>>j)<<(j+1));hi=lo|(1<<j)
       actual_mass=p[lo]+p[hi]
       ck([p[lo]/actual_mass,p[hi]/actual_mass]==[expected[lo]/qold[x],expected[hi]/qold[x]])
     increments=[]
     for outcome in [0,1]:
      vv=restrict(v,j,outcome);pp=[x*x for x in fw(vv)]
      ck(pp==qold) # both FULL inherited laws already actual; all calibration KL=0
      qnew=list(qold);tail=((1<<(k-1))-1)<<r;ghost=1<<r
      for U in range(1<<r):
       qnew[U|tail]-=B[U]**2/F(64)
       qnew[U|ghost]+=B[U]**2/F(64)
      ck(sum(qnew)==1);ck(all(x>=0 for x in qnew))
      ck(all(not pp[x] or qnew[x]>0 for x in range(len(pp))))
      ck(all(qnew[U]==pp[U] for U in range(1<<r)))
      for U in range(1<<r):
       ck(qnew[U|tail]==F(63,64)*pp[U|tail]);ck(qnew[U|ghost]==B[U]**2/64)
      diff=ar.sub(ar.ce(pp,qnew),ar.ce(pp,qold));exact=ar.mul(beta,ar.lg(F(64,63)))
      ck(diff[0]<=exact[1] and exact[0]<=diff[1])
      if beta:
       ck(diff[0]>0);positive+=1
      else:
       ck(qnew==qold);zero+=1
      increments.append(ar.pretty(diff))
     if pattern==(2,2,2,2) and k==3 and sigma==1 and jj==0:
      witness={'definition':'F(x,y)=a(x)+(1-a(x)^2)*parity3(y)','controller':list(ORIGINAL),'seed_influence':'1','wrapper_seed_influence':str(beta),'root_H_bits':ar.pretty(H),'root_I':str(ar.ib(p)),'controller_I':str(icont),'B_j':'0','occupancy_KL':'0','both_block_refunds':['0','0'],'each_child_delta':increments,'exact_child_and_average_increment':'(3/8)*log2(64/63)','lower_bound':'3/512','lower_bound_proof':'ln(1+1/63)>1/64 and ln(2)<1','same_old_siblings':'unchanged; full child CE charged','full_fei_counterexample':False}
      ck(ar.mul(beta,ar.lg(F(64,63)))[0]>F(3,512))
      dump('WITNESS.json',witness)
     if time.perf_counter()-started>limit:raise RuntimeError('frozen deadline exceeded')
    # No growth of actual spectrum entropy with parity degree.
    expected_H=ar.ent([x*x for x in A]+[y*y for y in B])
    ck(H==expected_H)
 result={'status':'PASS','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'pilot':pilot,'families':families,'query_nodes':nodes,'positive_full_child_resets':positive,'zero_tail_full_child_resets':zero,'exact_assertions':COUNT,'seconds':time.perf_counter()-started,'gram':gram,'claim_scope':'A096 zero-phase obstruction only; phase-funded theorem NOT independently accepted here'}
 dump('PILOT.json' if pilot else 'VALIDATION.json',result)
 print(json.dumps(result))
if __name__=='__main__':run('--pilot' in sys.argv)
