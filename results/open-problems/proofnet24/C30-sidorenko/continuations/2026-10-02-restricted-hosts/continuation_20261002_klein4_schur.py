"""Exact four-state Cayley host polynomial and a Schur-convexity test."""
import itertools,json,math
from collections import Counter
from pathlib import Path

def derivative(P,var):
    out=Counter()
    for mon,c in P.items():
        if mon[var]:
            mm=list(mon);mm[var]-=1;out[tuple(mm)]+=c*mon[var]
    return out

def main():
    edges=[(i,5+j)for i in range(5)for j in range(5)if(j-i)%5 in[0,1,4]]
    counts=Counter()
    for tail in itertools.product(range(4),repeat=9):
        X=(0,)+tail;mon=[0]*4
        for x,y in edges:mon[X[x]^X[y]]+=1
        counts[tuple(mon)]+=1
    # Multiplying by 4^6 gives the normalized density polynomial.
    P=Counter({mon:4096*c for mon,c in counts.items()})
    for perm in itertools.permutations(range(4)):
        assert all(P[tuple(mon[j]for j in perm)]==c for mon,c in P.items())
    diff=derivative(P,0);diff.subtract(derivative(P,1))
    quotient=Counter()
    for(a,b,c,d),coef in diff.items():
        if a>b:
            for j in range(a-b):quotient[(a-1-j,b+j,c,d)]+=coef
    # Check exact multiplication by x0−x1, independent of the quotient rule.
    check=Counter()
    for(a,b,c,d),coef in quotient.items():
        check[(a+1,b,c,d)]+=coef;check[(a,b+1,c,d)]-=coef
    assert {k:v for k,v in diff.items()if v}=={k:v for k,v in check.items()if v}
    neg={','.join(map(str,k)):v for k,v in quotient.items()if v<0}
    ordered=Counter()
    for(a,b,c,d),coef in quotient.items():
        for i in range(a+1):
            for j in range(c+1):ordered[(a+b-i,c+d-j,i,j)]+=coef*math.comb(a,i)*math.comb(c,j)
    ordered_negative={','.join(map(str,k)):v for k,v in ordered.items()if v<0}
    assert not ordered_negative
    assert ordered[(0,0,13,0)]==61440
    result={'status':'exact ordered Schur-convexity certificate PASS; raw coefficient shortcut fails',
            'fixed_assignments':sum(counts.values()),'density_polynomial':{','.join(map(str,k)):v for k,v in sorted(P.items())},
            'schur_derivative_quotient':{','.join(map(str,k)):v for k,v in sorted(quotient.items())if v},
            'negative_quotient_coefficients':neg,'all_quotient_coefficients_nonnegative':not neg,
            'ordered_substitution':'p0=a+d,p1=a,p2=b+e,p3=b; monomial order a,b,d,e',
            'ordered_quotient_coefficients':{','.join(map(str,k)):v for k,v in sorted(ordered.items())if v},
            'negative_ordered_quotient_coefficients':ordered_negative,'ordered_certificate_pass':not ordered_negative,
            'pure_difference_coefficient':ordered[(0,0,13,0)],
            'quantitative_theorem':'F(p)>=sum(p)^15+1024 sum_{i<j}|p_i-p_j|^15'}
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2))
    print({'nonzero_polynomial_terms':len(P),'raw_negative_quotient_coefficients':len(neg),'ordered_nonzero_terms':sum(bool(v)for v in ordered.values()),'ordered_test_pass':not ordered_negative})

if __name__=='__main__':main()
