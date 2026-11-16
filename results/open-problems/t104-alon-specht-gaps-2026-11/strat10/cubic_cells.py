"""PROVED: moment cells augmented by exact degree-six scalar inequalities."""
from fractions import Fraction as F
import cells
from cells import DIRECTIONS,controls,minimum
from padding import base_coefficients
CUBIC_DIRECTIONS=((1,0),(0,1),(1,1),(2,1),(1,2))
COUNT=30

def cubic_lower(p,alpha,beta):
    A,B,C=p;s=alpha*alpha+beta*beta
    return 3*(alpha**4*A+6*alpha*alpha*beta*beta*C+beta**4*B)/(s*s)-F(3,2)

def lower_value(p,a,r,vector):
    return cells.lower_value(p,a,r,vector[:25])+a*a*sum(eta*cubic_lower(p,alpha,beta)for eta,(alpha,beta)in zip(vector[25:],CUBIC_DIRECTIONS))

def residual_blocks(r,vector):
    df,eh=cells.residual_blocks(r,vector[:25])
    for eta,(alpha,beta)in zip(vector[25:],CUBIC_DIRECTIONS):
        s=alpha*alpha+beta*beta
        x,y=alpha**3,3*alpha*beta*beta
        for j,c in enumerate((x*x,x*y,y*y)):df[j]-=eta*F(c,s**3)
        x,y=3*alpha*alpha*beta,beta**3
        for j,c in enumerate((x*x,x*y,y*y)):eh[j]-=eta*F(c,s**3)
    return df,eh

def vector_from_record(rec):
    etas=list(map(F,rec['cubic_multipliers']));assert len(etas)==5 and min(etas)>=0
    return cells.vector_from_record(rec)+etas

def check(rec,verts):
    vec=vector_from_record(rec);lo,hi,alo,ahi=map(F,(rec['rlo'],rec['rhi'],rec['alo'],rec['ahi']))
    assert 0<=lo<=hi<=1 and 0<=alo<=ahi
    for k in range(2):
        bb=[controls(lambda rr:residual_blocks(rr,vec)[k][j],lo,hi)for j in range(3)]
        for i in range(3):
            x,y,z=[bb[j][i]for j in range(3)];assert min(x,z)>=0 and x*z>=y*y
    margin=min(minimum(lambda rr:controls(lambda aa:lower_value(p,aa,rr,vec),alo,ahi)[j],lo,hi)for p in verts for j in range(3));assert margin>=0
    return margin

def lower_coefficients(p,a,r,vec):
    extra=lower_value(p,a,r,vec)-cells.base_value(p,a,r)
    return tuple(v+c*extra for v,c in zip(base_coefficients(p,a,r),(16,8,1)))

def check_allN(rec,verts):
    check(rec,verts);vec=vector_from_record(rec);lo,hi,alo,ahi=map(F,(rec['rlo'],rec['rhi'],rec['alo'],rec['ahi']))
    ms=[min(minimum(lambda rr:controls(lambda aa:lower_coefficients(p,aa,rr,vec)[k],alo,ahi)[j],lo,hi)for p in verts for j in range(3))for k in range(3)];assert min(ms)>=0
    return ms
