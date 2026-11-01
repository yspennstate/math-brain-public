from dataclasses import dataclass
import sympy as sp

@dataclass
class Seg:
    l: sp.Rational
    u: sp.Rational
    m: sp.Rational
    c: sp.Rational
    def val(self,a):
        return sp.simplify(self.m*a+self.c)

def gittins_segments(xs, ps):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); n=len(xs); segs=[]
    for j in range(n):
        l=sp.Rational(0) if j==0 else xs[j-1]; u=xs[j]; S=sum(ps[j:])
        lines=[]
        for k in range(j,n):
            den=sum(ps[j:k+1])
            C=sum(ps[i]*xs[i] for i in range(j,k+1)) + xs[k]*sum(ps[k+1:])
            lines.append((-S/den, sp.factor(C/den)))
        pts={l,u}
        for i in range(len(lines)):
            for j2 in range(i+1,len(lines)):
                m1,c1=lines[i]; m2,c2=lines[j2]
                if m1 != m2:
                    z=sp.factor((c2-c1)/(m1-m2))
                    if l < z < u: pts.add(z)
        pts=sorted(pts)
        for A,B in zip(pts[:-1],pts[1:]):
            mid=(A+B)/2
            m,c=min(lines,key=lambda mc: mc[0]*mid+mc[1])
            if segs and segs[-1].u==A and segs[-1].m==m and segs[-1].c==c:
                segs[-1].u=B
            else:
                segs.append(Seg(A,B,m,c))
    return segs

def mserpt_segments(xs, ps):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); segs=[]; H=None
    for j in range(len(xs)):
        l=sp.Rational(0) if j==0 else xs[j-1]; u=xs[j]
        S=sum(ps[j:]); mean=sum(ps[i]*xs[i] for i in range(j,len(xs)))/S
        start=sp.factor(mean-l)
        H=start if H is None else max(H,start)
        segs.append(Seg(l,u,sp.Rational(0),H))
    return segs

def new_mean(xs, ps, segs, R):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); cutoff=None
    for s in segs:
        if s.val(s.l) >= R:
            cutoff=s.l; break
    if cutoff is None:
        return sp.factor(sum(p*x for p,x in zip(ps,xs)))
    return sp.factor(sum(p*min(x,cutoff) for p,x in zip(ps,xs)))

def old_stats(xs, ps, segs, R):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); old0=[]; sq=[]
    for x in xs:
        ints=[]
        for s in segs:
            if s.l >= x: break
            A=s.l; B=min(s.u,x)
            if B<=A: continue
            vA=s.val(A); vB=s.val(B)
            if s.m==0:
                if vA <= R: ints.append((A,B))
            else:
                if vA <= R:
                    ints.append((A,B))
                elif vB <= R:
                    root=sp.factor((R-s.c)/s.m)
                    if root < B: ints.append((max(A,root),B))
        merged=[]
        for A,B in ints:
            if merged and A <= merged[-1][1]:
                merged[-1]=(merged[-1][0],max(B,merged[-1][1]))
            else:
                merged.append((A,B))
        old0.append(merged[0][1] if merged and merged[0][0]==0 else sp.Rational(0))
        sq.append(sum((B-A)**2 for A,B in merged))
    return sp.factor(sum(p*v for p,v in zip(ps,old0))), sp.factor(sum(p*v for p,v in zip(ps,sq)))

def worst_at(segs, x, a):
    vals=[]
    for s in segs:
        A=max(a,s.l); B=min(x,s.u)
        if A < B: vals.append(s.val(A))
    return max(vals)

def residence(xs, ps, segs, lam, x):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); lam=sp.Rational(lam); x=sp.Rational(x)
    starts=[s.val(s.l) for s in segs]
    pts={sp.Rational(0),x}
    for s in segs:
        if 0<s.l<x: pts.add(s.l)
        if 0<s.u<x: pts.add(s.u)
        A=max(sp.Rational(0),s.l); B=min(x,s.u)
        if A<B and s.m!=0:
            for q in starts:
                z=sp.factor((q-s.c)/s.m)
                if A<z<B: pts.add(z)
    pts=sorted(pts); total=sp.Rational(0)
    for A,B in zip(pts[:-1],pts[1:]):
        mid=(A+B)/2; R=worst_at(segs,x,mid); En=new_mean(xs,ps,segs,R)
        total += (B-A)/(1-lam*En)
    return sp.factor(total)

def soap_mean(xs, ps, policy, lam):
    xs=list(map(sp.Rational,xs)); ps=list(map(sp.Rational,ps)); lam=sp.Rational(lam)
    segs=gittins_segments(xs,ps) if policy=='G' else mserpt_segments(xs,ps)
    cond=[]
    for x in xs:
        R0=max(s.val(s.l) for s in segs if s.l<x)
        En=new_mean(xs,ps,segs,R0); Eo0,Esq=old_stats(xs,ps,segs,R0)
        wait=sp.factor(lam*Esq/(2*(1-lam*Eo0)*(1-lam*En)))
        cond.append(sp.factor(wait+residence(xs,ps,segs,lam,x)))
    return sp.factor(sum(p*t for p,t in zip(ps,cond))), cond, segs

# Generic stabilized-tail derivative.
lam,mu,r,b,d,M20=sp.symbols('lam mu r b d M20', positive=True)
beta=1-lam*mu; x=b+d; M2=M20+r*x**2; rho=lam*(mu+r*d)
W=lam*M2/(2*(1-rho)*beta)
target=r*lam/(2*beta)*(2*x/(1-rho)+lam*M2/(1-rho)**2)
assert sp.factor(sp.diff(W,d)-target)==0
print('GENERIC_TAIL_WAIT_DERIVATIVE_PASS')

# Sanity check against the published SOAP {2,14} Gittins example at lambda=1/20.
EG,condG,_=soap_mean([2,14],[sp.Rational(1,2),sp.Rational(1,2)],'G',sp.Rational(1,20))
assert condG == [sp.Rational(7,3),sp.Rational(533,27)]
assert EG == sp.Rational(298,27)
print('SOURCE_TWOPOINT_SANITY_PASS')

# Exact four-point contact obstruction.
ps=[sp.Rational(1,3),sp.Rational(1,12),sp.Rational(1,2),sp.Rational(1,12)]
L=sp.Rational(1,10)
base=[sp.Rational(1),sp.Rational(5,2),sp.Rational(7,2)]

def values(dd):
    xs=base+[sp.Rational(7,2)+dd]
    EG,_,gsegs=soap_mean(xs,ps,'G',L)
    EM,_,msegs=soap_mean(xs,ps,'M',L)
    return EG,EM,sp.factor(EM-EG),sp.factor(2*EG-EM),gsegs,msegs

EG5,EM5,D5,F5,G5,M5=values(sp.Rational(5))
EG52,EM52,D52,F52,G52,M52=values(sp.Rational(26,5))
EG6,EM6,D6,F6,G6,M6=values(sp.Rational(6))
assert EG5 == sp.Rational(52145,13706)
assert EM5 == sp.Rational(57497,14952)
assert D5 == sp.Rational(961,23496)
assert F5 == sp.Rational(619013,164472)
assert D52 == sp.Rational(1553,11748)
assert D6 == D52
# The preterminal Gittins geometry is identical across the contact.
assert [(s.l,s.u,s.m,s.c) for s in G5[:-1]] == [(s.l,s.u,s.m,s.c) for s in G52[:-1]]
# M-SERPT record candidates are (d+31)/12, (d+19)/8, (d+7)/7, d;
# the first contact is exactly d=5.
Dsym=sp.symbols('Dsym')
starts=[(Dsym+31)/12,(Dsym+19)/8,(Dsym+7)/7,Dsym]
assert sp.factor(starts[1]-starts[0]-(Dsym-5)/24)==0
# The one-sided post-contact factor-two slack is smaller by 65/712.
Fplus=sp.factor(EG5-D52)
assert Fplus == sp.Rational(301999,82236)
assert sp.factor(F5-Fplus) == sp.Rational(65,712)
print('FOURPOINT_CONTACT_D5', 'EG=',EG5, 'EM=',EM5, 'D=',D5, 'F=',F5)
print('FOURPOINT_POSTCONTACT_D52', 'EG=',EG52, 'EM=',EM52, 'D=',D52, 'F=',F52)
print('STABILIZED_OPEN_CELL_GAP', D52)
print('CONTACT_SLACK_DROP', sp.Rational(65,712))
print('ALL_EXACT_CHECKS_PASS')
