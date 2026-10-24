"""Exact determinant and count-jet checks for the X044 theorem.
The analytic sign is proved in agents/X044.md, not by these finite samples.
"""
import itertools, json, math
from pathlib import Path
import sympy as S
import numpy as np

I=S.I

def basis():
    out=[]
    for i in range(4):
        a=S.zeros(4); a[i,i]=1; out.append(a)
    for i,j in itertools.combinations(range(4),2):
        for v in (1,I):
            a=S.zeros(4); a[i,j]=v; a[j,i]=S.conjugate(v); out.append(a)
    return out


def data(c,d):
    h=S.Matrix([[1,1],[1,-1]])/S.sqrt(2)
    w=S.diag(h,h*S.diag(1,-I))
    km=S.eye(4)/2; km[0,2]=km[2,0]=c; km[1,3]=km[3,1]=d
    k=S.simplify(w*km*w.conjugate().T)
    dirs=[S.simplify(w*a*w.conjugate().T) for a in basis()]
    r,s=4*c*c,4*d*d; pp=(1-r)*(1-s); qq=(1+r)*(1+s); rr=1-r*s; ss=1+r*s
    vals=[pp,qq,rr,ss]
    masses=[S.Rational(0)]*9
    fd=S.zeros(9,16); fdd=[S.zeros(16) for _ in range(9)]
    atoms=[]; ad=[]; add=[]
    exact=0
    for mask in range(16):
        bits=[(mask>>i)&1 for i in range(4)]
        m=S.Matrix.hstack(*[(k if bits[j] else S.eye(4)-k)[:,j] for j in range(4)])
        p=S.factor(m.det()); inv=m.inv()
        jets=[inv*S.Matrix.hstack(*[(a if bits[j] else -a)[:,j] for j in range(4)]) for a in dirs]
        traces=[S.trace(j) for j in jets]
        dp=S.Matrix([S.simplify(p*t) for t in traces])
        ddp=S.Matrix(16,16,lambda i,j:S.simplify(p*(traces[i]*traces[j]-S.trace(jets[i]*jets[j]))))
        x,y=sum(bits[:2])-1,sum(bits[2:])-1; cell=3*(x+1)+y+1
        f=1-(r+s)*x*y+r*s*(2*x*x-1)*(2*y*y-1)
        assert p==f/16; exact+=1
        masses[cell]+=p
        for j in range(16): fd[cell,j]+=dp[j]
        fdd[cell]+=ddp
        atoms.append(p); ad.append(list(dp)); add.append(ddp)
    weights=[S.binomial(2,a)*S.binomial(2,b) for a in range(3) for b in range(3)]
    cells=[[0,8],[2,6],[1,3,5,7],[4]]
    coeff=[sum((fdd[j] for j in cells[k]),S.zeros(16)) for k in range(4)]
    bb=basis(); vectors=[S.eye(16)[:,j] for j in range(16)]
    vectors += [S.eye(16)[:,i]+S.eye(16)[:,j] for i,j in itertools.combinations(range(16),2)]
    lv=S.Matrix([-1,-1,0,2]); rv=S.Matrix([-1,1,0,0]); tv=S.Matrix([-2,-2,8,-4])
    qadj=S.diag(d,c)
    for vec in vectors:
        a=sum((vec[j]*bb[j] for j in range(16)),S.zeros(4)); u=a[:2,:2]; v=a[2:,2:]; b=a[:2,2:]
        lc=-u.det()-v.det(); rc=-S.trace(u)*S.trace(v)+S.trace(b*b.conjugate().T)
        dd=d*b[0,0]+c*b[1,1]
        tc=2*S.trace(qadj*v*qadj*u)-2*S.expand_complex(dd*S.conjugate(dd))-4*c*d*S.re(b.det())
        pred=S.simplify(lc*lv+rc*rv+tc*tv)
        got=S.Matrix([(vec.T*co*vec)[0] for co in coeff])
        assert S.simplify(pred-got)==S.zeros(4,1); exact+=4
    for j,a in enumerate(bb):
        ta=a[0,0]+a[1,1]; tb=a[2,2]+a[3,3]
        mu=s*a[0,0]+r*a[1,1]; nu=s*a[2,2]+r*a[3,3]
        b=a[:2,2:]
        for aa,bbb in itertools.product(range(3),repeat=2):
            x,y=aa-1,bbb-1; ux,vy=2*x*x-1,2*y*y-1; cell=3*aa+bbb
            g=2*(ta*x+tb*y-mu*ux*y-nu*x*vy)
            g+=-8*(c*S.re(b[0,0])+d*S.re(b[1,1]))*x*y
            g+=32*c*d*(d*S.re(b[0,0])+c*S.re(b[1,1]))*ux*vy
            assert S.simplify(fd[cell,j]-weights[cell]*g/16)==0; exact+=1
    ff=np.array(masses,float); fdp=np.array(fd,float); fddp=np.array(fdd,float)
    ap=np.array(atoms,float); adp=np.array(ad,float); addp=np.array(add,float)
    neg_phi=(fdp.T/ff)@fdp+np.einsum('a,aij->ij',np.log(ff/np.array(weights,float)),fddp)
    neg_h=(adp.T/ap)@adp+np.einsum('a,aij->ij',np.log(ap),addp)
    loss=(adp.T/ap)@adp-(fdp.T/ff)@fdp
    # The complete count correction has exactly the Fisher difference.
    err=float(np.max(np.abs(neg_h-neg_phi-loss)))
    assert err<1e-8
    return dict(c=str(c),d=str(d),r=str(r),s=str(s),exact_assertions=exact,
                min_atom=float(min(atoms)),phi_min_eigenvalue=float(np.linalg.eigvalsh(neg_phi)[0]),
                h_min_eigenvalue=float(np.linalg.eigvalsh(neg_h)[0]),touching_error=err)


def block(r,s):
    L=math.log((1+r*s)**2/((1-r*r)*(1-s*s)))
    tau=2*L-8*math.log((1+r*s)/(1-r*s))
    B=(2+r+s)/(1-r*s)-math.log((1+r*s)/((1-r)*(1-s)))
    u=(r-s)**2/((1-r)*(1-r*s))+L/2+s*tau/4
    v=(r-s)**2/((1-s)*(1-r*s))+L/2+r*tau/4
    return B,u,v


def hyperbolic_check(r,s):
    assert 0<=s<=r<1
    r0=(r-s)/(1-r*s); m=-math.log1p(-r0*r0)/2
    l=math.log((1+r*s)/math.sqrt((1-r*r)*(1-s*s)))
    Uc=r0*r0/(1-r0); Vc=r0*r0/(1+r0)
    B,u,v=block(r,s); B0,u0,v0=block(r0,0)
    du=s*Uc+(1-s)*(l-m)+s*m
    dv=(r-r0)*Vc+(1-r)*(l-m)+(r-r0)*m
    assert abs((u-u0)-du)<1e-8 and abs((v-v0)-dv)<1e-8
    assert B>=B0-1e-12 and du>=-1e-12 and dv>=-1e-12
    return dict(r=r,s=s,old_B=B,B_increment=B-B0,u_increment=du,v_increment=dv,
                q_min_eigenvalue=float(np.linalg.eigvalsh([[B+u,B],[B,B+v]])[0]))

if __name__=='__main__':
    reports=[data(S.Rational(3,10),S.Rational(1,5)),data(S.Rational(499,1000),S.Rational(1,5))]
    hyper=[hyperbolic_check(r,s) for r,s in [(0.81,0.36),(0.99,0.01),(0.9996,0.36),(0.81,0.81),(0.36,0)]]
    assert min(x['phi_min_eigenvalue'] for x in reports)>0
    assert min(x['h_min_eigenvalue'] for x in reports)>0
    # A symbol-only check of both rational hyperbolic coefficients.
    r,s=S.symbols('r s'); r0=(r-s)/(1-r*s)
    assert S.factor((r-s)**2/((1-r)*(1-r*s))-(1+s)*r0**2/(1-r0))==0
    assert S.factor((r-s)**2/((1-s)*(1-r*s))-(1+r)*r0**2/(1+r0))==0
    out={'status':'PASS','exact_assertions':sum(x['exact_assertions'] for x in reports)+2,'determinant_witnesses':reports,'hyperbolic_checks':hyper}
    Path(__file__).with_name('results.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
