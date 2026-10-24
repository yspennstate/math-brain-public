import argparse,itertools,json,time
from fractions import Fraction as F
from functools import lru_cache
from pathlib import Path
BASE=Path(__file__).resolve().parents[1];ASSERT=0
def ck(b):
    global ASSERT
    ASSERT+=1
    if not b:raise AssertionError(ASSERT)
@lru_cache(None)
def tab(m):return tuple(1 if m>>x&1 else -1 for x in range(4))
@lru_cache(None)
def influence_product(m,n):
    t=tuple(a*b for a,b in zip(tab(m),tab(n)))
    return F(sum(t[x]!=t[x^(1<<i)] for i in range(2) for x in range(4)),4)
def reserves(I,a,b):
    pi=(1-a,a*(1-b),a*b)
    root=2*(pi[0]*pi[1]*I[0]+pi[0]*pi[2]*I[1]+pi[1]*pi[2]*I[2])
    split=2*a*(1-a)*((1-b)*I[0]+b*I[1])+2*a*b*(1-b)*I[2]
    return root,split
def main(pilot):
    start=time.monotonic();cases=patterns=sharp=0
    widths=(1,2) if pilot else (1,2,3)
    for r,s in itertools.product(widths,repeat=2):
        a,b=F(1,2**r),F(1,2**s);k=(2-a-b)/(1-a*b)
        ck(F(4,3)<=k<2)
        for z in itertools.product((0,1),repeat=3):
            I=(int(z[0]!=z[1]),int(z[0]!=z[2]),int(z[1]!=z[2]))
            root,split=reserves(I,a,b);ck(split<=k*root);patterns+=1
            if z[2]!=z[0] and z[0]==z[1]:ck(split==k*root)
    masks=(0,1,6,15) if pilot else range(16)
    for x,y,z in itertools.product(masks,repeat=3):
        I=(influence_product(x,y),influence_product(x,z),influence_product(y,z))
        for r,s in itertools.product(widths,repeat=2):
            a,b=F(1,2**r),F(1,2**s);k=(2-a-b)/(1-a*b)
            root,split=reserves(I,a,b);ck(split<=k*root)
            ck(split-root==2*a*(1-a)*b*(1-b)*I[2]);cases+=1
    # Three distinct nonconstant actual signs: g0=x,g1=-x,g2=xy.
    witness=(10,5,9);ck(len(set(witness))==3)
    I=(influence_product(10,5),influence_product(10,9),influence_product(5,9));ck(I==(0,1,1))
    rows=[]
    for r,s in itertools.product(range(1,13),repeat=2):
        a,b=F(1,2**r),F(1,2**s);k=(2-a-b)/(1-a*b);root,split=reserves(I,a,b)
        ck(root>0 and split==k*root);sharp+=1
        rows.append({'r':r,'s':s,'kappa':str(k),'root_R_star':str(root),'split_R_data':str(split)})
    (BASE/'out/sharp_witness.json').write_text(json.dumps({'core_masks':witness,'pair_product_influences':[str(v) for v in I],'rows':rows},indent=2))
    result={'status':'PASS','pilot':pilot,'core_width_cases':cases,'pivot_cases':patterns,'sharp_width_pairs':sharp,'assertions':ASSERT,'seconds':time.monotonic()-start,'arithmetic':'Exact Fraction cut ratios and direct Boolean boundaries'}
    (BASE/'out'/('compression_pilot.json' if pilot else 'compression.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result))
if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--pilot',action='store_true');main(p.parse_args().pilot)
