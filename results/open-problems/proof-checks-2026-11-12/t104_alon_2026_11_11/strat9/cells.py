"""PROVED: exact rational padded directional moment bounds and cell verifier."""
from fractions import Fraction as F
DIRECTIONS=((1,1),(1,0),(0,1),(1,-1))
COUNT=25

def controls(evaluate,lo,hi):
    left,middle,right=evaluate(lo),evaluate((lo+hi)/2),evaluate(hi)
    return left,2*middle-(left+right)/2,right

def minimum(evaluate,lo,hi):
    c0=evaluate(F(0));plus,minus=evaluate(F(1)),evaluate(F(-1))
    c1,c2=(plus-minus)/2,(plus+minus)/2-c0
    vals=[evaluate(lo),evaluate(hi)]
    if c2>0:
        crit=-c1/(2*c2)
        if lo<=crit<=hi:vals.append(evaluate(crit))
    return min(vals)

def base_value(p,a,r):
    A,B,C=p;fm=A+r*B+(1+r)*C
    return F(9,80)+a*(11*fm-2*(1+r))/8+a*a*(100*(1+r)*fm-1600*(A+r*r*B)-1280*(1+r*r)*C-640*r*C+415*(1+r*r)-66*r)/320

def lower_value(p,a,r,vector):
    A,B,C=p;td=vector[20];z1,z2,z3,z4=vector[21:25]
    lam=(2+a*(1+r))/4
    val=base_value(p,a,r)-a*a*(z1*(A-F(1,5))+z2*(B-F(1,5))+(z3+z4)*C)-a*2*lam*td/5
    for i,(alpha,beta)in enumerate(DIRECTIONS):
        theta,q,c,v,dd=vector[5*i:5*i+5]
        mm=alpha*(A+r*C)+beta*(C+r*B)
        kk=alpha*alpha*A+2*alpha*beta*C+beta*beta*B
        ss=a*(alpha+beta*r-mm)-lam*(alpha+beta)/5
        val+=a*(a*(2*q*mm-(1+r)*c)-theta*lam*(alpha*alpha+beta*beta-kk)/5+v*ss-dd/2)
    return val

def residual_blocks(r,vector):
    td=vector[20];z1,z2,z3,z4=vector[21:25]
    # R6+td*(N_r-J_r)+Bessel penalties.
    df=[3+z1,1+r-td,r*r+4*r+2*r*td+z2+z4]
    eh=[1+4*r+2*td+z1+z3,r*(1+r)-r*td,3*r*r+z2]
    for i,(alpha,beta)in enumerate(DIRECTIONS):
        theta=vector[5*i]
        df[0]-=theta*alpha*alpha
        df[2]-=theta*(beta*beta+2*r*alpha*beta)
        eh[0]-=theta*(2*alpha*beta+r*alpha*alpha)
        eh[2]-=theta*r*beta*beta
    return df,eh

def vector_from_record(rec):
    out=[]
    assert len(rec['directions'])==4
    for dr in rec['directions']:
        theta,t,v=map(F,(dr['theta'],dr['tangent'],dr['shift']))
        assert theta>=0
        out.extend((theta,theta*t,theta*t*t,theta*v,theta*v*v))
    td=F(rec['theta_d']);penalties=list(map(F,rec['penalties']))
    assert td>=0 and len(penalties)==4 and min(penalties)>=0
    return out+[td]+penalties

def check(rec,verts):
    vector=vector_from_record(rec)
    lo,hi,alo,ahi=map(F,(rec['rlo'],rec['rhi'],rec['alo'],rec['ahi']))
    assert 0<=lo<=hi<=1 and 0<=alo<=ahi
    for block in range(2):
        bb=[controls(lambda rr:residual_blocks(rr,vector)[block][j],lo,hi)for j in range(3)]
        for k in range(3):
            x,y,z=[bb[j][k]for j in range(3)]
            assert x>=0 and z>=0 and x*z>=y*y
    # Bernstein in a, exact quadratic minima in r.
    margin=min(minimum(lambda rr:controls(lambda aa:lower_value(p,aa,rr,vector),alo,ahi)[j],lo,hi)
               for p in verts for j in range(3))
    assert margin>=0
    return margin
