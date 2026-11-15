"""PROVED: exact integer-frame witnesses for enlargement of the face cover.

Floating supplied frames are used only to choose integers during --export.
Default replay reads only those integers, rational data and saved boxes.
"""
import json,itertools,sys
from math import gcd,isqrt
from functools import reduce
from fractions import Fraction as F
from rational_rays import frame_data,cell_bound
from face_intervals import Interval as I
from directional_bounds import vector_from_record,lower_value
from moment_bounds import value


def simplify(v):
    d=reduce(gcd,map(abs,v));return [x//d for x in v]


def candidates(U,W,r,data):
    uu=sum(x*x for x in U);ww=sum(x*x for x in W)
    a=data['a'];b=a*r;la=data['lam']
    rad=a*b/(la*la*uu*ww);scale=2**256
    low=isqrt(rad.numerator*scale*scale//rad.denominator)
    root=I(F(low,scale),F(low+1,scale))
    assert root.lo**2<=rad<=root.hi**2
    pairs=list(itertools.combinations(range(5),2))
    for (i,j),omega in zip(pairs,data['weights']):
        if omega:continue
        for k,l in [(i,j),(j,i)]:
            first=[5*(a*F(U[k]*U[n],uu)+b*F(W[k]*W[n],ww))/la for n in range(5)]
            second=[5*(U[k]*W[n]-W[k]*U[n])for n in range(5)]
            t=first[k]
            assert first[l]==-1 and second[k]==0 and sum(first)==sum(second)==0
            # Verify the exact Gram identity, including the squared radical.
            for q in range(5):
                for n in range(5):
                    gap=a*F(U[q]*U[n],uu)+b*F(W[q]*W[n],ww)
                    assert first[q]*first[n]+second[q]*second[n]*rad==5*t*gap/la
            N=sum(x*x+y*y*rad for x,y in zip(first,second))
            assert 10*t/(20*t-N)==la
            for rest in itertools.permutations([n for n in range(5)if n not in (k,l)]):
                for sign in [-1,1]:
                    coords=[I(t),I(first[rest[0]]),sign*second[rest[0]]*root,
                            I(first[rest[1]]),sign*second[rest[1]]*root,sign*second[l]*root]
                    yield list(rest)+[k,l],sign,coords


def contains(box,coords):
    return all(F(lo)<=x.lo<=x.hi<=F(hi)for(lo,hi),x in zip(box,coords))


def disjoint(box,coords):
    return any(x.hi<F(lo)or x.lo>F(hi)for(lo,hi),x in zip(box,coords))


def trace_value(U,W,r,data):
    uu=sum(x*x for x in U);ww=sum(x*x for x in W)
    a=data['a'];la=data['lam']
    G=[[a*F(U[i]*U[j],uu)+a*r*F(W[i]*W[j],ww)for j in range(5)]for i in range(5)]
    Pi=[[F(int(i==j))-F(1,5)-F(U[i]*U[j],uu)-F(W[i]*W[j],ww)for j in range(5)]for i in range(5)]
    tr=sum(G[i][i]for i in range(5))
    X1=2*(la*tr-sum(G[i][j]**2 for i in range(5)for j in range(5)))
    X2=F(10,3)*sum(Pi[i][j]*G[i][j]**2 for i in range(5)for j in range(5))
    X3=(1-la)/3*(2*tr-F(10,3)*sum(Pi[i][i]*G[i][i]for i in range(5)))
    Y=2*sum((la/5+G[i][j])*(Pi[i][i]+Pi[j][j]-2*Pi[i][j])*(G[i][i]+G[j][j]-2*G[i][j])for i in range(5)for j in range(i+1,5))
    return X1+X2+X3-Y


def main():
    exporting='--export'in sys.argv
    if exporting:
        sources=[]
        for row in json.load(open('far_end_frames.json'))['rows']:
            raw=row['u'];S=10**7
            U=[round(x[0]*S)for x in raw]; U=[5*x-sum(U)for x in U];U=simplify(U)
            W=[round(x[1]*S)for x in raw]; W=[5*x-sum(W)for x in W]
            un=sum(x*x for x in U); dot=sum(x*y for x,y in zip(U,W))
            W=simplify([un*y-dot*x for x,y in zip(U,W)])
            sources.append(dict(U=U,W=W,r=str(F(round(1000*row['r']),1000))))
    else:sources=json.load(open('exact_witnesses.json'))['witnesses']
    boxes=json.load(open('face_boxes.json'))['boxes']
    old=json.load(open('prior_face_boxes.json'))
    base=json.load(open('strong_moment_cells.json'))+json.load(open('enhanced_moment_cells.json'))
    direct=[(c,vector_from_record(c))for c in json.load(open('directional_moment_cells.json'))]
    counts={'boxed':0,'miss_moment':0,'miss_prior_boxes':0,'miss_nonlinear':0}
    out=[]
    for ix,source in enumerate(sources):
        U,W,r=source['U'],source['W'],F(source['r'])
        data=frame_data(U,W,r)
        assert F(3,25)<r<=1 and data['a']>F(103,200)
        assert data['lam']>data['a'] and min(data['weights'])==0 and data['T']>0
        assert trace_value(U,W,r,data)==data['T']
        charts=list(candidates(U,W,r,data));found=None
        for j,box in enumerate(boxes):
            for perm,sign,coords in charts:
                if contains(box['box'],coords):
                    found=dict(box=j,permutation=perm,reflection=sign);break
            if found is not None:break
        if found is not None:counts['boxed']+=1
        bounds=[cell_bound(c,data['moments'],data['a'],r)for c in base if F(c['rlo'])<=r<=F(c['rhi'])]
        bounds.extend(lower_value(data['moments'],data['a'],r,v)for c,v in direct if F(c['rlo'])<=r<=F(c['rhi']))
        bm=max(bounds);miss_old=all(disjoint(box['box'],coords)for box in old for perm,sign,coords in charts)
        counts['miss_moment']+=int(bm<0);counts['miss_prior_boxes']+=int(miss_old)
        A,B,C=data['moments'];a=data['a'];la=data['lam'];K=A+B+2*C
        fm=A+r*B+(1+r)*C;SS=a*(1+r-fm)-2*la/5
        zn=a*fm*fm/(1+r)-la*(2-K)/5+SS*SS/2
        zj=a*fm*fm/(1+r)-la*(4-K)/5+SS*SS/2
        nonlinear=value(data['moments'],a,r,0,0,0,0,0)
        nonlinear+=(5*r/3-1)*max(F(0),zn)+(1+r)*max(F(0),zj)
        nonlinear_miss=r<F(3,5)or nonlinear<0
        counts['miss_nonlinear']+=int(nonlinear_miss)
        rec=dict(U=U,W=W,r=str(r),a=str(a),T=str(data['T']),chart_certificate=found,
                 max_moment_lower=str(bm),outside_prior_boxes=miss_old,
                 nonlinear_lower=str(nonlinear)if r>=F(3,5)else None)
        if not exporting:assert rec==source
        out.append(rec)
        print('PROVED: exact witness',ix,'boxed',found is not None,'moment missed',bm<0,'prior boxes missed',miss_old,flush=True)
    result=dict(status='PROVED',witnesses=out,counts=counts)
    if exporting:
        with open('exact_witnesses.json','w')as f:json.dump(result,f,indent=2)
    else:assert counts==json.load(open('exact_witnesses.json'))['counts']
    print('PROVED: exact counts',counts)

if __name__=='__main__':main()
