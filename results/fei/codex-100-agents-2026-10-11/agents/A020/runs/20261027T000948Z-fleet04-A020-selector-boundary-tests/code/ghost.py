from pathlib import Path
from fractions import Fraction as Q
from itertools import product
import importlib.util,json,time,sys
sys.dont_write_bytecode=True
R=Path(__file__).resolve().parents[1]
s=importlib.util.spec_from_file_location('rev',R/'code/review.py');h=importlib.util.module_from_spec(s);s.loader.exec_module(h)
start=time.perf_counter();N=0
def ck(t):
 global N
 N+=1
 assert t,N
E=h.E;P=h.PE;alpha=Q(17,32)
ck(P[0]==Q(25,64));ck(sum(P[1:])==Q(39,64));ck(h.inf(E)==Q(11,8))
ck(alpha*alpha<Q(1,2))
# ONE evaluated block, all physical outcomes, asymmetric stopping:
# a=1: leave four irrelevant bits; a=0: query the remaining four.
leaves=[(Q(1,2),1,1)]
for z in range(16):leaves.append((Q(1,32),E[z<<1],0))
ck(sum(w for w,e,K in leaves)==1);ck(sum(w*K for w,e,K in leaves)==Q(1,2))
ck(h.project(P,[1,2,3,4])[0]==alpha)
rows=[]
for k in [5,8,16]:
 rho=Q(1,1<<k)
 for blocks in [1,2,4]:
  mu=Q(5,8)**(blocks+1);p=rho*(1-mu)/2
  for dead in range(blocks+1):
   for phase in [1,-1]:
    for sigma in [1,-1]:
     g=[phase*x for x in E];pg=h.law(g);nu=Q(sum(g),32);a=(1-nu)/2
     core=[sigma if g[x>>1]==-1 else (-1 if x&1 else 1) for x in range(64)]
     pc=h.law(core);f=h.full(core);pf=h.law(f)
     # Slice with all unqueried ghosts absent. Original reference is NOT normalized on this slice.
     qc=[(1-2*p)*Q(int(x==1),2)+Q(int(x==0),2)+rho*(alpha**dead*P[x>>1]+(1-2*mu)*int((x>>1)==0))/8 for x in range(64)]
     qf=h.fullref(qc)
     selected=[x for x in range(len(pf)) if (x>>4)!=0]
     # Nonempty source => no added vacuum or principal atom at these rows.
     mass=sum(pf[x] for x in selected);ck(mass==Q(39,256))
     for x in selected:
      T=x>>4;ck(qf[x]==rho*alpha**dead*P[T]/128);ck(pf[x]==P[T]/64)
     direct=h.ce([pf[x] for x in selected],[qf[x] for x in selected])
     H=h.ce(P[1:],P[1:]);L=h.log(1/alpha)
     lower=mass*(k+7+dead*L[0])+H[0]/4
     upper=mass*(k+7+dead*L[1])+H[1]/4
     ck(direct[0]<=upper and lower<=direct[1])
     fi=4*h.inf(f);ck(fi==6-2*a+Q(11,8)-sigma*a);ck(fi<=Q(115,16))
     rows.append({'k':k,'blocks_evaluated':blocks,'ghost_blocks':dead,'source_phase':phase,'q_sign':sigma,'selected_mass':str(mass),'fourI':str(fi)})
 # j=2^(k+8)+1 gives an all-outcome expected negative reserve.
 j=(1<<(k+8))+1
 upper=Q(115,16)-rho*Q(39,1024)*(j-1)
 ck(upper==Q(-41,16));ck(Q(5,8)**5<Q(1,8))
result={'status':'PASS','assertions':N,'profiles':len(rows),'per_block_physical_leaves':len(leaves),'selected_mass':'39/256','ghost_floor':'17/32','negative_expected_reserve_upper_bound':'-41/16 (strict)','seconds':time.perf_counter()-start,'h_assertions':h.N}
h.save('GHOST_CHECKS.json',result);h.save('GHOST_PROFILES.json',rows);print(json.dumps(result))
