"""PROVED: exact directional edge-square bounds and rational cell replay."""
from fractions import Fraction as F
from moment_bounds import value,blocks,controls,minimum

DIRECTIONS=((1,1),(1,0),(0,1),(1,-1))


def direction_value(p,a,r,alpha,beta,theta,q,c,v,d):
    A,B,C=p
    moment=alpha*(A+r*C)+beta*(C+r*B)
    diag=alpha*alpha*A+2*alpha*beta*C+beta*beta*B
    lam=(2+a*(1+r))/4
    S=a*(alpha+beta*r-moment-(1+r)*F(alpha+beta,20))-F(alpha+beta,10)
    return (a*(2*q*moment-(1+r)*c)-theta*lam*(alpha*alpha+beta*beta-diag)/5
            +v*S-F(1,2)*d)


def lower_value(p,a,r,vector):
    # For each direction: theta, theta*t, theta*t^2, theta*v, theta*v^2.
    offset=5*len(DIRECTIONS)
    td=vector[offset]
    penalties=vector[offset+1:offset+5]
    A,B,C=p
    base=value(p,a,r,0,0,0,0,0,penalties)
    base-=(2+a*(1+r))*td/10
    for i,(alpha,beta)in enumerate(DIRECTIONS):
        base+=direction_value(p,a,r,alpha,beta,*vector[5*i:5*i+5])
    return base


def residual_blocks(r,vector,d_zero=False):
    offset=5*len(DIRECTIONS)
    td=vector[offset]
    penalties=vector[offset+1:offset+5]
    # Start with R + td*N - td*J and the four Bessel penalties.
    df,eh=blocks(r,0,0,td,penalties)
    df=list(df)
    eh=list(eh)
    for i,(alpha,beta)in enumerate(DIRECTIONS):
        theta=vector[5*i]
        df[0]-=theta*alpha*alpha
        df[2]-=theta*(beta*beta+2*r*alpha*beta)
        eh[0]-=theta*(2*alpha*beta+r*alpha*alpha)
        eh[2]-=theta*r*beta*beta
    if d_zero:
        # Only the f^2 entry matters on d=0; a fixed unit dummy entry
        # expresses this as an equivalent, nondegenerate PSD condition.
        df[0],df[1]=F(1),F(0)
    return df,eh


def vector_from_record(rec):
    vector=[]
    for dr in rec['directions']:
        theta,t,v=map(F,(dr['theta'],dr['tangent'],dr['shift']))
        assert theta>=0
        vector.extend((theta,theta*t,theta*t*t,theta*v,theta*v*v))
    assert len(rec['directions'])==len(DIRECTIONS)
    td=F(rec['theta_d'])
    penalties=list(map(F,rec['penalties']))
    assert td>=0 and len(penalties)==4 and min(penalties)>=0
    return vector+[td]+penalties


def check(rec,verts):
    vector=vector_from_record(rec)
    lo,hi,alo,ahi=map(F,(rec['rlo'],rec['rhi'],rec['alo'],rec['ahi']))
    assert 0<lo<=hi<=1 and 0<alo<=ahi
    d_zero=rec.get('basis_d_zero',False)
    if d_zero:
        assert lo==hi==1
    for block in range(2):
        bb=[controls(lambda r:residual_blocks(r,vector,d_zero)[block][j],lo,hi)for j in range(3)]
        for k in range(3):
            aa,cc,dd=[bb[j][k]for j in range(3)]
            assert aa>=0 and dd>=0 and aa*dd>=cc*cc
    margin=min(minimum(lambda r:lower_value(p,a,r,vector),lo,hi)
               for p in verts for a in(alo,ahi))
    assert isinstance(margin,F)and margin>=0
    return margin
