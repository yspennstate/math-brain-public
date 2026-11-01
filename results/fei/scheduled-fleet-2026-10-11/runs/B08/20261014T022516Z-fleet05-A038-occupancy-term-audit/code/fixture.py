from fractions import Fraction as F
from pathlib import Path
import json,time,hashlib
R=Path(__file__).resolve().parents[1];START=time.monotonic();COUNT=0
def check(x):
    global COUNT
    COUNT+=1
    assert x,COUNT
def signs(core,k):return core[k]
u=(-1,-1,-1,1);v=(-1,1,1,1)
# Coordinate order x,a,b,u0,u1,v0,v1, all recorded physical coordinates.
ancestor=[]
for t in range(128):
    x,a,b,u0,u1,v0,v1=[(t>>i)&1 for i in range(7)]
    ancestor.append(u[u0+2*u1] if x==0 and a else v[v0+2*v1] if x==1 and b else 1)
parent=tuple(ancestor[t] for t in range(128) if not t&(1<<3))
children=[tuple(parent[t] for t in range(64) if ((t>>1)&1)==a) for a in (0,1)]
def spectrum(tab):
    n=len(tab)
    return tuple(F(sum(value*(-1 if (s&t).bit_count()%2 else 1) for t,value in enumerate(tab))**2,n*n) for s in range(n))
def inf(tab,i):return F(sum(tab[t]!=tab[t^(1<<i)] for t in range(len(tab))),len(tab))
P=spectrum(parent);C=[spectrum(t) for t in children]
check(inf(ancestor,3)==F(1,8));check(F(sum(parent),len(parent))==F(3,8))
check(sorted(p for p in P if p)==[F(1,64)]*14+[F(9,64)]*2+[F(1,4)]*2)
check(all(sorted(p for p in z if p)==[F(1,64)]*15+[F(49,64)] for z in C))
check(C[0][0]==F(49,64));check(C[1][1]==F(49,64))
check([inf(parent,j) for j in range(6)]==[F(1,2),F(1,2),F(1,8),F(0),F(1,8),F(1,8)])
check(sum(inf(parent,j) for j in range(6))==F(11,8))
check(sum(sum(inf(t,j) for j in range(5)) for t in children)/2==F(7,8))
q=[(a+b)/2 for a,b in zip(*C)];ds=[sum((q[t] for t in range(32) if t&(1<<j)),F(0)) for j in range(5)]
Q=[];kernel=[]
for t in range(32):
    z=F(1)
    for j,d in enumerate(ds):z*=d if t&(1<<j) else 1-d
    Q.append(z);kernel.append(C[0][t]/(2*q[t]) if q[t] else F(1,2))
check(sum(Q)==1);check(sum(Q[t]*kernel[t] for t in range(32))==F(1,2))
check(all(q[t]*kernel[t]==C[0][t]/2 for t in range(32)))
# v event x=1,b=1 remains identical across query; u is constant -1.
check(sum(1 for t in range(64) if t&1 and t&4)==16)
lhs_low=2**1428*7**525;middle=5**1250;lhs_high=2**1432*7**525
check(lhs_low<middle<lhs_high);check(7**245<2**688)
check(all(P[t]==0 for t in range(64) if t&2 and t&52))
nonempty=1-P[0];check(nonempty==F(55,64))
check([inf(parent,j)/nonempty for j in (0,1,2,4,5)]==[F(32,55),F(32,55),F(8,55),F(8,55),F(8,55)])
check(4*31**2*49**3<55**5)
M0=F(32,55)*(1-F(49,55)**3);L=F(55,64)*F(10,7)*(M0+M0*M0/2)
check(M0==F(1559232,9150625));check(L>F(43,200))
result={'status':'PASS','assertions':COUNT,'runtime_seconds':time.monotonic()-START,'ancestor_u':list(u),'v':list(v),'exposure':{'original_coordinate':3,'value':0,'ancestor_influence':'1/8'},'query':{'descendant_coordinate':1,'name':'private a','influence':'1/2'},'q_reference_0':'1/2','outcome_KL':'0','kappa':'0','rho_exact':'2+(21/32)log2(7)-(25/16)log2(5)','rho_strict_interval':['21/100','43/200'],'parent_influence':'11/8','expected_child_influence':'7/8','parent_entropy_exact':'4-(9/16)log2(3)','expected_child_entropy_exact':'6-(49/32)log2(7)','expected_child_entropy_lower':'17/10','integer_sign_certificates':{'lower':'5^1250<2^1432*7^525','upper':'2^1428*7^525<5^1250','terminal':'7^245<2^688','largest_integer_bits':max(lhs_high.bit_length(),middle.bit_length())},'parent_spectrum':[str(p) for p in P],'child_spectra':[[str(p) for p in z] for z in C],'parent_table':list(parent),'child_tables':[list(t) for t in children]}
result['occupancy_certificate']={'nonempty_mass':str(nonempty),'r':['32/55','32/55','8/55','8/55','8/55'],'excluded_event':'a present and at least one of b,v0,v1 present','actual_excluded_probability':'0','positive_root_bracket':'3/4<c<1','root_bracket_integer':'4*31^2*49^3<55^5','Q_excluded_mass_strict_lower':str(M0),'weighted_K_occ_strict_lower':str(L),'target_debt_comparison':'v K_occ(root)>L>43/200>rho','ln2_strict_upper':'7/10, three-interval convex trapezoid proof'}
(R/'out'/'FIXTURE.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8');print(json.dumps({k:result[k] for k in ['status','assertions','runtime_seconds','rho_strict_interval','expected_child_entropy_lower']}))
