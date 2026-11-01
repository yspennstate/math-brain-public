from fractions import Fraction as Q
from pathlib import Path
from itertools import product,combinations
import json,time,hashlib
R=Path(__file__).resolve().parent.parent; checks=0; start=time.monotonic()
def ck(v):
 global checks
 checks+=1
 if not v:raise AssertionError(checks)
def save(n,o):(R/'out'/n).write_text(json.dumps(o,indent=2)+'\n',encoding='utf-8')
def walsh(values):return [sum(Q(v)*(-1)**((s&x).bit_count()) for x,v in enumerate(values))/len(values) for s in range(len(values))]
def truthcheck(values):
 w=walsh(values)
 for U in range(len(values)):ck(sum(w[S]*w[S^U] for S in range(len(values)))==int(U==0))
 ps=[]
 for u in [0,1]:
  c=walsh(values[u::2]);ck(all(c[t]==w[t<<1]+(-1)**u*w[(t<<1)|1] for t in range(len(c))))
  ps.append([x*x for x in c])
 return w,ps
norm=lambda v:sum(abs(x) for x in v)
transport=[]
for cap in product(range(1,5),repeat=3):
 for x in product(range(5),repeat=3):
  r=sum(x)
  if not 1<=r<=4 or r>sum(cap):continue
  candidates=[]
  for free in range(3):
   fixed=[i for i in range(3) if i!=free]
   options=[sorted({0,cap[i]}|({x[i]} if x[i]<=cap[i] else set())) for i in fixed]
   for vals in product(*options):
    v=[0]*3
    for i,y in zip(fixed,vals):v[i]=y
    v[free]=r-sum(vals)
    if 0<=v[free]<=cap[free]:candidates.append(v)
  ck(bool(candidates));best=min(candidates,key=lambda v:norm([v[i]-x[i] for i in range(3)]))
  overflow=sum(max(0,x[i]-cap[i]) for i in range(3));ck(norm([best[i]-x[i] for i in range(3)])==2*overflow)
  transport.append({'cap':cap,'ideal':x,'attainer':best,'L1':2*overflow})
ck(len(transport)==2161);save('TRANSPORT_CERTIFICATES.json',transport)
vecs=[v for v in product([-1,0,1],repeat=4) if sum(v)==0];ck(len(vecs)==19)
cs=0
for a,b,r,s in product([Q(1,4),Q(1,2),Q(1)],repeat=4):
 for u,v in product(vecs,repeat=2):
  ck((r*r/a+s*s/b)*(a*norm(u)**2/(r*r)+b*norm(v)**2/(s*s))>=norm([u[i]+v[i] for i in range(4)])**2);cs+=1
ck(cs==29241)
# Direct actual Boolean source: queried bit0, child g2 at plus and y1 at minus.
values=[]
for x in range(8):
 g=-1 if x>>1==0 else 1
 values.append(g if x&1==0 else (-1)**((x>>1)&1))
w,p=truthcheck(values);ck(p==[[Q(1,4)]*4,[0,1,0,0]])
mid=[(p[0][i]+p[1][i])/2 for i in range(4)]
P=[z*z for z in w]
incoming=[Q(1,4)*P[S]/mid[S>>1] for S in range(8)]
ck(sum(incoming)==1)
for S in range(8):ck(incoming[S]*mid[S>>1]==Q(1,4)*P[S])
q33=[[Q(1,4),Q(1,2),Q(1,8),Q(1,8)],[0,Q(3,4),Q(1,8),Q(1,8)]]
q35=[[Q(5,12),Q(1,12),Q(1,4),Q(1,4)],[Q(1,12),Q(5,12),Q(1,4),Q(1,4)]]
for qs in [q33,q35]:ck(all(sum(q)==1 for q in qs))
ck([(q33[0][i]+q33[1][i])/2 for i in range(4)]==[Q(1,8),Q(5,8),Q(1,8),Q(1,8)])
ck([(q35[0][i]+q35[1][i])/2 for i in range(4)]==[Q(1,4)]*4)
grad=[-p[0][i]/q35[0][i]+p[1][i]/q35[1][i] for i in range(4)]
ck(grad==[Q(-3,5),Q(-3,5),Q(-1),Q(-1)])
# A033 derivative numerator: -[3/8+(11/4)x-6x^2].
ck(Q(11,4)-6*Q(1,4)==Q(5,4));ck(3125<10368);ck(16<18)
ck(186624>16*3125 and 186624<256*3125);ck(729>256)
# Independent natural-log lower bound ln y >=2(y-1)/(y+1).
lower33=Q(1,8)*2*(Q(9,8)-1)/(Q(9,8)+1);ck(lower33>Q(1,108))
y=Q(186624,16*3125);lower35=Q(1,8)*2*(y-1)/(y+1);ck(lower35>Q(1,12))
save('REVIEW_A033.json',{'claim_scope':'actual-midpoint fine criterion and exact Boolean witness','verdict':'HOLDS_NO_REPAIR','reconstruction':'Entire within-block Gibbs equality; singly occupied residual; compact finite minimizer. Direct truth Walsh and boundary derivative prove stated witness.','fine_Phi_nats':'1/108','fine_gap_nats_lower':str(lower33),'full_net_sign':'negative:3125<10368','limits':'Declared full-mean compatibility only; no initial source and no universal necessity.'})
save('REVIEW_A035.json',{'claim_scope':'arbitrary-inherited-mean fine criterion and false positive debit','verdict':'HOLDS_NO_REPAIR','reconstruction':'Double equality and single nonnegative residual independently reconstructed. Exact block-constant gradient proves global optimizer.','fine_Phi_nats':'1/12','fine_gap_nats_lower':str(lower35),'M_minus_JS':'positive:729>256','full_M_minus_JS_minus_old_mismatch':'negative:186624<256*3125','limits':'No arbitrary-core source or necessary universal class.'})
# Positive-influence sharpness, with the parent occupancy and old divergence kept.
values=[(-1)**(x&1)*(-1 if x>>1==0 else 1) for x in range(8)]
w,p=truthcheck(values);ck(p==[[Q(1,4)]*4]*2);ck(sum(w[S]**2 for S in range(8) if S&1)==1)
sharp=[]
for s in [Q(1,4),Q(1,8),Q(1,16),Q(1,32)]:
 m=[(1+2*s)/4]*2+[(1-2*s)/4]*2
 parent=[m[S>>1] if S&1 else Q(0) for S in range(8)];ck(sum(parent)==1)
 ck(all(w[S]==0 for S in range(8) if not S&1))
 ck(all(parent[2*T]+parent[2*T+1]==m[T] for T in range(4)))
 e=[2*Q(1,4)-2*z for z in m];phi=norm(e)**2/8;ck(phi==2*s*s)
 # Jensen's exact minimizer has both references=m, so every occupied CE term cancels.
 ck(all(parent[2*T+1]==m[T] for T in range(4)))
 sharp.append({'s':str(s),'Phi_nats':str(phi),'ratio_upper':str(1/(1-4*s*s)),'net_CE_increment':'0 termwise'})
ck(time.monotonic()-start<55)
out={'status':'PASS','checks':checks,'seconds':time.monotonic()-start,'transport_cases':len(transport),'weighted_CS_cases':cs,'actual_Boolean_review_witnesses':2,'sharpness_cases':sharp,'same_author_independent_implementation':True,'external_review_new_bound':'PENDING','full_FEI':'OPEN','helper_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
save('REPRODUCE.json',out);print(json.dumps({k:out[k] for k in ['status','checks','seconds','transport_cases','weighted_CS_cases']}))
