"""Exact failures of two sufficient proof shortcuts, not of Lyons's conjecture."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
from verify_fourier_extension import logsum
from verify_shuffle_obstruction import enclose_decimal


def multiply(a,b):
    return [a[0]*b[0],a[0]*b[1]+a[1]*b[0],a[0]*b[2]+a[1]*b[1]+a[2]*b[0]]


def count(ps):
    ans=[F(1)]
    for p in ps:
        nxt=[F(0)]*(len(ans)+1)
        for i,q in enumerate(ans):nxt[i]+=q*(1-p);nxt[i+1]+=q*p
        ans=nxt
    return ans


def projection_weight(S,T):
    if len(S)!=len(T):return F(0)
    if len(S) in [0,4]:return F(1)
    if len(S) in [1,3]:return F(1,4)
    os=(S[1]-S[0])%2==0;ot=(T[1]-T[0])%2==0
    return F(0) if os and ot else F(1,4) if os or ot else F(1,8)


def fourier_jets(lam,velocity):
    bits=list(product([0,1],repeat=4));source=[]
    for t in bits:
        p=[F(1),F(0),F(0)]
        for i,b in enumerate(t):p=multiply(p,[lam[i] if b else 1-lam[i],velocity[i] if b else -velocity[i],F(0)])
        source.append(p)
    atoms=[]
    for s in bits:
        S=[i for i,b in enumerate(s) if b];row=[F(0)]*3
        for t,p in zip(bits,source):
            T=[i for i,b in enumerate(t) if b];w=projection_weight(S,T)
            row=[a+w*b for a,b in zip(row,p)]
        atoms.append(row)
    assert [sum(p[j] for p in atoms) for j in range(3)]==[1,0,0]
    return bits,atoms


def curvature(atoms):
    return logsum([(2*p[2],p[0]) for p in atoms],sum(p[1]**2/p[0] for p in atoms))


def marginal_jets(a,b,c,d):
    out=[]
    for x,y in product([0,1],repeat=2):
        out.append(multiply([a if x else 1-a,c if x else -c,0],[b if y else 1-b,d if y else -d,0]))
    middle=[(out[1][j]+out[2][j])/2 for j in range(3)]
    return [out[0],middle,middle,out[3]]


def main():
    # Small balanced rational example where the bound (9), after discarding
    # the remaining local Q terms, does not pay the adverse mean interaction.
    lam=[F(1,100),F(99,100),F(99,100),F(1,100)]
    c,d,u,v=map(F,[-5,2,-1,2]);velocity=[c+u,d+v,c-u,d-v]
    bits,atoms=fourier_jets(lam,velocity);bybits=dict(zip(bits,atoms))
    P=bybits[(1,1,0,0)];O=bybits[(1,0,1,0)];p0=bybits[(0,0,0,0)][0];p4=bybits[(1,1,1,1)][0]
    c1=bybits[(1,0,0,0)][0];c3=bybits[(1,1,1,0)][0]
    f=count(lam);g=[F(0)]*4;h=[F(0)]*3
    for i in range(4):
        for k,p in enumerate(count([lam[j] for j in range(4) if j!=i])):g[k]+=velocity[i]*p
        for j in range(4):
            if i==j:continue
            for k,p in enumerate(count([lam[l] for l in range(4) if l not in [i,j]])):h[k]+=velocity[i]*velocity[j]*p
    alpha=[c1*c1/(p0*P[0]),P[0]*O[0]/(c1*c3),c3*c3/(p4*P[0])]
    beta=[16*P[0]/f[2],f[2]**2/(16*P[0]*O[0]),16*P[0]/f[2]]
    excess=8*(O[0]*P[1]-P[0]*O[1])**2/(P[0]*O[0]*f[2])
    boundary=g[0]**2/f[1]+g[3]**2/f[3]
    terms=[(h[k],beta[k]) if h[k]>=0 else (-h[k],alpha[k]) for k in range(3)]+[(4*c*d,O[0]/P[0])]
    lower=logsum(terms,excess+boundary);full=curvature(atoms)
    assert all(q<0 for q in h) and lower[1]<-1 and full[0]>1700
    first=dict(eigenvalues=list(map(str,lam)),pair_coordinate_velocity=list(map(str,[c,d,u,v])),h=list(map(str,h)),discarded_local_bound=enclose_decimal(lower),actual_negative_entropy_curvature=enclose_decimal(full),certified_bound_upper='-1',certified_actual_curvature_lower='1700')

    # Mutual information between the two opposite measured pairs is not
    # jointly convex even with the overall diagonal mean fixed.
    lam=[F(1,100),F(3,5),F(1,100),F(1,100)];c=F(1);d=F(-1);u=v=F(0)
    velocity=[c+u,d+v,c-u,d-v];a=(lam[0]+lam[2])/2;b=(lam[1]+lam[3])/2
    bits,atoms=fourier_jets(lam,velocity);marginal=marginal_jets(a,b,c,d)
    # Independently verify the opposite-pair marginal at the level of jets.
    for i,(s,t) in enumerate(product([0,1],repeat=2)):
        actual=[sum(p[j] for bit,p in zip(bits,atoms) if bit[0]==s and bit[2]==t) for j in range(3)]
        assert actual==marginal[i]
    mutual=logsum([(2*p[2],p[0]) for p in atoms]+[(-4*p[2],p[0]) for p in marginal],sum(p[1]**2/p[0] for p in atoms)-2*sum(p[1]**2/p[0] for p in marginal))
    full=curvature(atoms)
    assert mutual[1]<-F(2,5) and full[0]>68
    second=dict(eigenvalues=list(map(str,lam)),pair_coordinate_velocity=['1','-1','0','0'],a=str(a),b=str(b),mutual_information_second_derivative=enclose_decimal(mutual),actual_negative_entropy_curvature=enclose_decimal(full),certified_mutual_curvature_upper='-2/5',certified_actual_curvature_lower='68')
    # Exact polynomial core of the two-dimensional count convolution.
    import verify_fourier_extension as core
    core.NN=6
    variables=[]
    for i in range(4):
        k=[0]*6;k[i]=1;variables.append(core.Poly({tuple(k):1}))
    aa,bb,xx,yy=variables
    U=[[(1-aa)**2-xx**2,aa*(1-aa)+xx**2],[aa*(1-aa)+xx**2,aa**2-xx**2]]
    V=[[(1-bb)**2-yy**2,bb*(1-bb)+yy**2],[bb*(1-bb)+yy**2,bb**2-yy**2]]
    joint=[[core.Poly() for j in range(3)] for i in range(3)]
    for i,j,k,l in product(range(2),repeat=4):joint[i+k][j+l]+=U[i][j]*V[k][l]
    ff=core.count([aa+xx,bb+yy,aa-xx,bb-yy]);oo=U[0][1]*V[0][1]
    pp=(4*oo+2*U[1][1]*V[0][0]+2*U[0][0]*V[1][1])/8
    expected=[[ff[0],ff[1]/2,oo],[ff[1]/2,4*pp,ff[3]/2],[oo,ff[3]/2,ff[4]]]
    for i,j in product(range(3),repeat=2):core.identity('bivariate count cell '+str((i,j)),joint[i][j],expected[i][j])
    out=dict(status='PASS: two proof shortcuts fail; actual entropy curvature remains positive',local_bound_obstruction=first,mutual_information_obstruction=second,bivariate_count_polynomial_identities=core.checks)
    Path(__file__).with_name('fourier_barriers_certificate.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
