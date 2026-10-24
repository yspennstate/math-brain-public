"""H3 candidate test with a response Gram having positive offdiagonal.

Exact full forest coefficients use frontier connectivity DP, independently
validated against direct enumeration on seven smaller H3 test graphs.
"""
from fractions import Fraction as F
from pathlib import Path
import json
from forest_frontier_dp_heat import forest_R_dp
from H3_response_wedge_heat import candidate
from general_H2_mirror_stress_heat import global_formula


def main():
    n=11;e=(0,1);f=(9,10)
    rows={0:[3,30,1],1:[2,28,2],2:[15,14,3],3:[5,2,4]}
    # Process disposable interior vertices first to keep frontier width low.
    raw=[(0,2,4),(1,2,14)]+[(2,4+i,c)for i,c in enumerate(rows[2])]
    raw +=[(0,3,12),(1,3,2)]+[(3,4+i,c)for i,c in enumerate(rows[3])]
    raw +=[(x,4+i,c)for x in [0,1]for i,c in enumerate(rows[x])]
    raw +=[(x,7,3)for x in [9,10]]+[(x,8,5)for x in [9,10]]
    raw +=[(4,5,3),(5,6,2),(7,8,2)]
    raw +=[(4+i,7+j,a*b)for i,a in enumerate([2,3,7])for j,b in enumerate([1,5])]
    edges=[(x,y,F(c))for x,y,c in raw]
    R=forest_R_dp(n,edges,e,f)
    h2,h3,tau=candidate(n,edges,e,f,r=4)
    for k in [2*n-4,2*n-5,2*n-6]:assert R.get(k,F(0))==0
    assert h2==0 and h3==R.get(2*n-7,F(0)) and h3>0
    # Recover the full root row to check the advertised positive entry B_(4,6).
    _,_,structure=global_formula(n,edges,e,f,4)
    Be=[[F(c)for c in row]for row in structure['Be']]
    boundary=[x for x in structure['boundary']if x!=4]
    positive_entry=-sum(Be[boundary.index(6)])
    assert positive_entry==F(268067,31510540800)>0
    for r in structure['boundary']:
        h2r,h3r,_=candidate(n,edges,e,f,r=r)
        assert h2r==0 and h3r==h3
    for ce,cf in [(F(2),F(3)),(F(1,2),F(7,5))]:
        h2r,h3r,_=candidate(n,edges,e,f,r=4,ce=ce,cf=cf)
        assert h2r==0 and h3r==h3
    out={'status':'exact computational audit of unproved general H3 candidate',
         'arithmetic':'Fraction exact; frontier connectivity forest enumeration',
         'n':n,'unmarked_edges':[(x,y,str(c))for x,y,c in edges],
         'marked_edges':[e,f],'H0':'0','H1':'0','H2':'0','H3':str(h3),
         'tau_at_marked_weights_one':str(tau),
         'positive_response_offdiagonal_B_4_6':str(positive_entry),
         'R_coefficients':{str(k):str(v)for k,v in R.items()},
         'all_roots_and_marked_weight_variants_agree':True,'passed':True}
    Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2))
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
