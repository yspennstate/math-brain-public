import exact as e
from exact import ck,save
from itertools import combinations
f=[1 if x.bit_count()>=2 else -1 for x in range(32)]
def cofactor(i,v):return {x:f[x]for x in range(32)if x>>i&1==v}
relevance=[]
for i in range(5):
    for v in range(2):
        cf=cofactor(i,v);supp=[j for j in range(5)if j!=i and any(cf[x]!=cf[x^(1<<j)]for x in cf)];ck(len(supp)==4);relevance.append({'fixed_coordinate':i,'value':v,'support':supp})
minors=[]
for A in range(1,31):
    if not A&1:continue
    B=31^A;xs=[x for x in range(32)if x&~A==0];ys=[y for y in range(32)if y&~B==0];found=None
    for x0,x1 in combinations(xs,2):
        for y0,y1 in combinations(ys,2):
            det=f[x0|y0]*f[x1|y1]-f[x0|y1]*f[x1|y0]
            if det:found={'A':A,'B':B,'x':[x0,x1],'y':[y0,y1],'determinant':det};break
        if found:break
    ck(found is not None);minors.append(found)
ck(len(minors)==15)
save('NONMEMBER_CERTIFICATE.json',{'status':'PASS','function':'five-bit +1 iff at least2 binary ones','truth_table':f,'cofactor_supports':relevance,'nonproduct_minors':minors,'excluded_roots':'overlap<=2 mux: both cofactors support4; new pure3-bit/common-event mux: its pure child would support<=3, impossible; product:15 minors; activation: constant-child mux; sign:invariant','old_four_bit_witness_now_admitted':True,'assertions':e.checks})
print(e.checks)
