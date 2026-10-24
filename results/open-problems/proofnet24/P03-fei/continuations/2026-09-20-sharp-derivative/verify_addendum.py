#!/usr/bin/env python3
"""Exact checks of the paid-compression obstruction and a curvature composition identity.
The proposed entropy bound by curvature rank is NOT proved by this program.
"""
import argparse,itertools,json,random
from pathlib import Path
from fractions import Fraction as F
def gf2rank(rows):
    """Exact Gaussian elimination over F_2, rows encoded as integers."""
    basis = {}
    for row in rows:
        while row:
            j = row.bit_length() - 1
            if j in basis:
                row ^= basis[j]
            else:
                basis[j] = row
                break
    return len(basis)
from verify_continuation import H,fwht,bounds,add


def local_state(f,x):
    n=len(f).bit_length()-1
    piv=[i for i in range(n) if f[x]!=f[x^(1<<i)]]
    rows=[]
    for i in piv:
        rows.append(sum((f[x]!=f[x^(1<<i)^(1<<j)])<<k for k,j in enumerate(piv) if i!=j))
    r=gf2rank(rows)
    ones=(1<<len(piv))-1
    flag=int(gf2rank(rows+[ones])>r)
    return rows,r,flag

def table(n,code):return tuple(1-2*((code>>x)&1) for x in range(1<<n))

def compose(outer,children):
    dims=[len(f).bit_length()-1 for f in children]
    n=sum(dims);offsets=[];off=0
    for d in dims:offsets.append(off);off+=d
    states=[[local_state(f,x) for x in range(len(f))] for f in children]
    output=[];records=[]
    for x in range(1<<n):
        xs=[(x>>off)&((1<<d)-1) for off,d in zip(offsets,dims)]
        b=sum((f[z]<0)<<j for j,(f,z) in enumerate(zip(children,xs)))
        output.append(outer[b]);records.append((xs,b))
    for x,(xs,b) in enumerate(records):
        J=[j for j in range(len(children)) if outer[b]!=outer[b^(1<<j)]]
        active=[j for j in J if states[j][xs[j]][2]]
        C=[]
        for j in active:
            C.append(sum((outer[b]!=outer[b^(1<<j)^(1<<ell)])<<k for k,ell in enumerate(active) if ell!=j))
        cr=gf2rank(C);one=(1<<len(active))-1
        predicted_r=sum(states[j][xs[j]][1] for j in J)+cr
        predicted_flag=int(gf2rank(C+[one])>cr)
        _,r,flag=local_state(output,x)
        assert (r,flag)==(predicted_r,predicted_flag),(dims,b,x,r,flag,predicted_r,predicted_flag)
    return len(output)

def run():
    f=tuple(-1 if x in (1,6,10,12) else 1 for x in range(16))
    g=tuple(-1 if x in (0,6,10,12) else 1 for x in range(16))
    compressed=[]
    for x in range(0,16,2):compressed.extend(sorted((f[x],f[x+1])))
    assert tuple(compressed)==g
    infl=lambda h:[F(sum(h[x]!=h[x^(1<<i)] for x in range(16)),16) for i in range(4)]
    assert H(f)=={2:F(3)} and H(g)=={2:F(2)}
    assert infl(f)==infl(g)==[F(1,2)]*4
    # A symmetric all-coordinate obstruction to local R or Q drift payment.
    shell=tuple(-1 if x.bit_count()==1 else 1 for x in range(16))
    Rsum=lambda h:sum(local_state(h,x)[1] for x in range(len(h)))
    Qsum=lambda h:sum(sum(local_state(h,x)[1:]) for x in range(len(h)))
    assert Rsum(shell)==8 and Qsum(shell)==19
    assert H(shell)=={2:F(3)}
    local_obstructions=[]
    for i in range(4):
        leaves=[tuple(v for x,v in enumerate(shell) if (x>>i)&1==b) for b in (0,1)]
        assert [Rsum(g) for g in leaves]==[6,2]
        assert [Qsum(g) for g in leaves]==[13,6]
        assert all(H(g)=={2:F(4),3:-F(9,8)} for g in leaves)
        gap=add(H(shell),H(leaves[0]),-1)
        assert bounds(gap)[0]>F(783,1000)
        local_obstructions.append({'coordinate':i,'R_decrease':'0','Q_decrease':'0',
                                   'entropy_decrease':'(9/8) log2(3) - 1 > 783/1000'})
    monotone_functions=monotone_comparisons=0
    for n in range(4):
        N=1<<n
        for code in range(1<<N):
            h=table(n,code);states=[local_state(h,x) for x in range(N)]
            assert all(r+flag<=len(rows) for rows,r,flag in states)
            assert (sum(r for _,r,_ in states)==0)==(H(h)=={})
            for i in range(n):
                for b in (0,1):
                    leaf=tuple(v for x,v in enumerate(h) if (x>>i)&1==b)
                    for y in range(len(leaf)):
                        x=(y&((1<<i)-1)) | (b<<i) | ((y>>i)<<(i+1))
                        _,r,e=states[x];_,lr,le=local_state(leaf,y)
                        assert lr<=r and lr+le<=r+e
                        monotone_comparisons+=1
            monotone_functions+=1
    cases=points=0
    # Every binary outer table and two children on at most two variables each.
    for dims in ((1,1),(1,2),(2,2)):
        for oc in range(16):
            outer=table(2,oc)
            for c1 in range(1<<(1<<dims[0])):
                for c2 in range(1<<(1<<dims[1])):
                    points+=compose(outer,[table(dims[0],c1),table(dims[1],c2)]);cases+=1
    # Every ternary outer and all one-bit children.
    for oc in range(256):
        outer=table(3,oc)
        for cs in itertools.product(range(4),repeat=3):
            points+=compose(outer,[table(1,c) for c in cs]);cases+=1
    rng=random.Random(20260920)
    for _ in range(1000):
        outer=table(3,rng.randrange(256));children=[table(2,rng.randrange(16)) for _ in range(3)]
        points+=compose(outer,children);cases+=1
    return {'status':'PASS','arithmetic':'Integer Walsh coefficients, exact entropy signatures and binary matrix ranks.',
            'compression_obstruction':{'negative_points_before':[1,6,10,12],'negative_points_after':[0,6,10,12],
                 'H_before':'3','H_after':'2','individual_influences_before':['1/2']*4,'individual_influences_after':['1/2']*4,
                 'walsh_numerators_before':list(fwht(f)),'walsh_numerators_after':list(fwht(g)),
                 'conclusion':'No finite C bounds this entropy loss by C times the influence decrease.'},
            'local_rank_potential_obstruction':{'negative_points':[1,2,4,8],'R':'1/2','Q':'19/16','coordinates':local_obstructions},
            'rank_monotonicity':{'Boolean_tables_checked':monotone_functions,'pointwise_restriction_comparisons':monotone_comparisons},
            'curvature_composition':{'function_parameter_cases':cases,'pointwise_rank_and_flag_checks':points,
                 'coverage':'Exhaustive binary outer/one- or two-bit children for dimensions (1,1),(1,2),(2,2); exhaustive ternary outer/one-bit children; 1000 sampled ternary outer/two-bit children.',
                 'scope':'Exact composition identity only. No universal Fourier-entropy bound by curvature rank is proved.'},
            'full_FEI_status':'UNPROVED'}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output',type=Path,default=Path('addendum_verification.json'));a=p.parse_args()
    text=json.dumps(run(),indent=2)+'\n';a.output.write_text(text,encoding='utf-8');print(text)
if __name__=='__main__':main()
