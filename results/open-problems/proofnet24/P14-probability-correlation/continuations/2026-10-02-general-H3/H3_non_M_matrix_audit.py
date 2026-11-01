"""Independent integer forest-subset check of H3 on a non-M-matrix response.

The e response has positive off-diagonal in its full three-port matrix.
A rank-one interface to the f ports makes H2 zero. The formula calculation
uses exact rational electrical solves, while the certificate uses separately
compiled C++ with bounded 128-bit integer subset weights, followed by
arbitrary precision Python coefficient products.
"""
from fractions import Fraction as F
from pathlib import Path
import subprocess,json
from H3_response_wedge_heat import candidate
from general_H2_mirror_stress_heat import global_formula

def main():
    edges=[(0,2,4),(1,2,14),(0,3,12),(1,3,2)]
    for x,row in enumerate([(3,30,1),(2,28,2),(15,14,3),(5,2,4)]):
        edges += [(x,4+j,c) for j,c in enumerate(row)]
    edges += [(x,9,2) for x in [7,8]]+[(x,10,3) for x in [7,8]]
    edges += [(4,9,2),(4,10,10),(5,9,3),(5,10,15)]
    n=11;e=(0,1);f=(7,8)
    h2,h3,tau=candidate(n,[(x,y,F(c))for x,y,c in edges],e,f,r=4)
    _,_,structure=global_formula(n,[(x,y,F(c))for x,y,c in edges],e,f,4)
    payload=f'{n} {len(edges)} {e[0]} {e[1]} {f[0]} {f[1]}\n'+''.join(f'{x} {y} {c}\n'for x,y,c in edges)
    executable=Path(__file__).with_name('forest_subset_integer_audit')
    assert 2**len(edges)*max(c for x,y,c in edges)**(n-1)<2**127
    forest=json.loads(subprocess.check_output([str(executable.resolve())],input=payload.encode()))
    polys=[[int(c) for c in p]for p in forest['polynomials']]
    R={}
    for degree in range(2*n-1):
        val=sum(polys[1][k]*polys[2][degree-k]-polys[0][k]*polys[3][degree-k]
                for k in range(n)if 0<=degree-k<n)
        if val:R[str(degree)]=str(val)
    forest['R_coefficients']=R
    actual=F(forest['R_coefficients'].get(str(2*n-7),'0'))
    result={'status':'exact independent check of provisional H3 formula','n':n,'unmarked_edges':edges,'marked_edges':[e,f],
            'H2_candidate':str(h2),'H3_candidate':str(h3),'H3_actual':str(actual),'tau':str(tau),'match':h2==0 and h3==actual,
            'structure':structure,'full_forest_subset_certificate':forest}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print(json.dumps({k:result[k]for k in ['H2_candidate','H3_candidate','H3_actual','tau','match']},indent=2))
    assert result['match']

if __name__=='__main__':main()
