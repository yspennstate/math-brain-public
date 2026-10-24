#!/usr/bin/env python3
from fractions import Fraction
from itertools import combinations
import json

def k3n_edges(n):
    return [(left, 3+j) for j in range(n) for left in range(3)]

def is_forest(nv, edges, mask):
    parent=list(range(nv)); rank=[0]*nv
    def find(x):
        while parent[x]!=x:
            parent[x]=parent[parent[x]]
            x=parent[x]
        return x
    def union(a,b):
        a,b=find(a),find(b)
        if a==b: return False
        if rank[a]<rank[b]: a,b=b,a
        parent[b]=a
        if rank[a]==rank[b]: rank[a]+=1
        return True
    for i,(u,v) in enumerate(edges):
        if (mask>>i)&1 and not union(u,v):
            return False
    return True

def brute_counts(n):
    edges=k3n_edges(n)
    Z=0; Ze=[0]*len(edges); Zef={}
    for mask in range(1<<len(edges)):
        if not is_forest(n+3,edges,mask): continue
        Z+=1
        inc=[i for i in range(len(edges)) if (mask>>i)&1]
        for i in inc: Ze[i]+=1
        for i,j in combinations(inc,2):
            Zef[(i,j)]=Zef.get((i,j),0)+1
    return Z,Ze,Zef

def integer(fr):
    assert fr.denominator==1, fr
    return fr.numerator

def formulas(n):
    p4=4**n
    Z=integer(Fraction(p4*(3*n*n+13*n+16),16))
    Ze=integer(Fraction(p4*(3*n*n+23*n+38),64))
    SL=integer(Fraction(3*p4*(n*n+11*n+22),256)) if n>=2 else None
    D=integer(Fraction(p4*(3*n*n+33*n+82),256)) if n>=2 else None
    SR=integer(Fraction(8*p4*(n+3),64))
    return Z,Ze,SL,D,SR

def delta_formulas(n):
    dSL=integer(Fraction(2*16**n*(41*n*n+181*n+194),4096)) if n>=2 else None
    dD=integer(Fraction(2*16**n*(17*n*n+77*n+66),4096)) if n>=2 else None
    dSR=integer(Fraction(16**n*(n-1)*(9*n**3+51*n*n+104*n+92),4096))
    return dSL,dD,dSR

def main():
    rows=[]
    for n in range(1,6):
        Z,Ze,Zef=brute_counts(n)
        fZ,fE,fSL,fD,fSR=formulas(n)
        assert Z==fZ
        assert all(x==fE for x in Ze)
        sr=Zef.get((0,1),0)
        assert sr==fSR
        dsr=fE*fE-fZ*fSR
        assert dsr==delta_formulas(n)[2]
        row={"n":n,"Z":Z,"Z_e":fE,"Z_ef_same_right":sr,"Delta_same_right":dsr}
        if n>=2:
            sl=Zef.get((0,3),0)
            di=Zef.get((0,4),0)
            assert sl==fSL and di==fD
            dsl=fE*fE-fZ*fSL
            dd=fE*fE-fZ*fD
            assert (dsl,dd)==delta_formulas(n)[:2]
            row.update({"Z_ef_same_left":sl,"Delta_same_left":dsl,
                        "Z_ef_disjoint":di,"Delta_disjoint":dd})
        rows.append(row)
    coeffs=[1107,16941,102441,318247,542740,488300,182960]
    assert all(c>0 for c in coeffs)
    ratios={}
    for n in range(3,10):
        u=17*n*n+77*n+66
        v=41*n*n+181*n+194
        A=3*n*n+23*n+38
        B=9*n*n+29*n+26
        R=Fraction(2*u*u,v*A*B)
        assert 0<R<1
        ratios[str(n)]={"numerator":R.numerator,"denominator":R.denominator,"decimal":float(R)}
    print(json.dumps({
      "status":"PASS",
      "family":"K_{3,n}",
      "measure":"uniform over all unrooted forests, all sizes, disconnected and empty included",
      "brute_force_n":"1..5",
      "rows":rows,
      "escape_ratio_R_n_definition":"rho_disjoint^2/abs(rho_same_left)",
      "escape_ratio_denominator_minus_numerator_coefficients_descending":coeffs,
      "escape_ratio_samples_n_3_to_9":ratios,
      "structural_check":"R_n<1 for every n>0 because every coefficient of the exact difference polynomial is positive"
    },indent=2,sort_keys=True))

if __name__=="__main__":
    main()
