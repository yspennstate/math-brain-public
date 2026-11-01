"""Fixed exact unequal-mass and stopping-frontier certificates."""
import json,hashlib
from fractions import Fraction as Q
import check as c
u=(1,1,1,-1);v=(1,1,1,1);o=0
C,W=c.selector(u,v,o,0);cc=c.walsh(C);ww=c.walsh(W)
m=Q(1,2);beta=Q(1,2);q=Q(1,4);aa=tuple(w+m*x for w,x in zip(ww,cc))
plus=tuple((a+beta*x)**2 for a,x in zip(aa,cc));minus=tuple((a-beta*x)**2 for a,x in zip(aa,cc))
mp=sum(plus);mm=sum(minus);mass=(mp+mm)/2
rho=mp/(2*mass);mix=tuple((a+b)/(2*mass) for a,b in zip(plus,minus))
def H(prob):return c.add(*(c.phi(x) for x in prob))
js=c.add(H(mix),c.scale(H(tuple(x/mp for x in plus)),-rho),c.scale(H(tuple(x/mm for x in minus)),-(1-rho)))
gap=c.add(c.phi(mass),c.scale(c.add(c.phi(mp),c.phi(mm)),Q(-1,2)))
J=c.add(*(c.add(c.phi(a*a+beta*beta*x*x),c.scale(c.add(c.phi((a+beta*x)**2),c.phi((a-beta*x)**2)),Q(-1,2))) for a,x in zip(aa,cc)))
assert (mp,mm,mass,rho)==(Q(1),Q(3,4),Q(7,8),Q(4,7))
assert J==c.add(c.scale(js,mass),gap)
assert c.log_bounds(gap)[0]>0
# Both cores have negative probability 1/4. Actual data-first constant leaves.
data=()
for a in (-1,1):
    for b in (-1,1):
        pa=Q(1,4) if a==-1 else Q(3,4);pb=Q(1,4) if b==-1 else Q(3,4)
        data=c.add(data,c.scale(c.entropy(c.priority((a,),(b,),0)),pa*pb))
control=c.scale(c.entropy(u),Q(1,4)+Q(1,8))
diff=c.add(data,c.scale(control,-1))
assert c.log_bounds(diff)[0]>0
result={'status':'PASS','assertions':4,'physical_branch_weights':['1/2','1/2'],'projected_empty_sector_masses':[str(mp),str(mm)],'normalized_sector_weights':[str(rho),str(1-rho)],'J_bits':c.serial(J),'normalized_weighted_JS_bits':c.serial(js),'positive_mass_correction_bits':c.serial(gap),'mass_correction_natural_interval':[str(x) for x in c.log_bounds(gap)],'frontier_example':{'u':list(u),'v':list(u),'orientation':0,'data_first_terminal_entropy_bits':c.serial(data),'control_first_terminal_entropy_bits':c.serial(control),'difference_natural_interval':[str(x) for x in c.log_bounds(diff)],'meaning':'actual frontiers differ; substituting their terminal entropy formulas is invalid'},'helper_sha256':hashlib.sha256(c.Path(__file__).read_bytes()).hexdigest()}
(c.ROOT/'out/WITNESSES.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print('PASS: 4 exact witness assertions, positive mass correction, distinct terminal entropies.')
