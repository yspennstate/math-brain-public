#!/usr/bin/env python3
"""P10/F0119 correction + outward-rounded KS ball certificate at rho=1/4.

(1) Correct the degree-5/6 homogeneous terms in the full-dimensional Taylor
expansion. An earlier helper accidentally used -27/20 and 27/10 for the z^5,
z^6 coefficients of (1/3+z)log(1+3z), instead of -81/20 and 81/10.
The degree-4 term is unaffected. We rederive H4,H5,H6 symbolically.

(2) Combine corrected H4--H6 with the exact path-scoped H7--H14 invariant
identities and a degree>=15 analytic tail to prove at lambda_*=1/sqrt(2):

 max(|m|,|n|)<=1/4 ==> H_*(p,q)>=1e-3(|m|^4+|n|^4),

where H_*=(Psi(p)+Psi(q))/2-K_*(p,q).

Write r=max(|m|,|n|), s=t r, C=Re(m^3)=r^3 x,
D=Re(n^3)=s^3 y, with 0<=t<=1 and x,y in [-1,1]. Branch endpoints are
dyadic and mpmath.iv supplies outward-rounded interval arithmetic.
"""
import itertools
import sympy as sp
import mpmath as mp

# --- exact H4,H5,H6 correction ---
N=6
a,b,c,d=sp.symbols('a b c d', real=True)
s2=sp.sqrt(2)
xv=[a,b,-a-b]; yv=[c,d,-c-d]

def pmul(P,Q):
    R=[sp.Integer(0)]*(N+1)
    for i,pi in enumerate(P):
        if pi==0: continue
        for j,qj in enumerate(Q):
            if i+j<=N and qj!=0: R[i+j]+=pi*qj
    return [sp.expand(v) for v in R]

def ppow(P,n):
    R=[sp.Integer(1)]+[sp.Integer(0)]*N
    for _ in range(n): R=pmul(R,P)
    return R

def psi_dev(zps):
    out=[sp.Integer(0)]*(N+1)
    for n,coef in [(2,sp.Rational(3,2)),(4,sp.Rational(5,4)),
                   (5,-sp.Rational(81,20)),(6,sp.Rational(81,10))]:
        S=[sp.Integer(0)]*(N+1)
        for zp in zps:
            P=ppow(zp,n); S=[S[k]+P[k] for k in range(N+1)]
        out=[sp.expand(out[k]+coef*S[k]) for k in range(N+1)]
    return out

def invden(D):
    R=[sp.Integer(0)]*(N+1); alpha=sp.Rational(3,2)*D
    for k in range(N//2+1): R[2*k]=(-alpha)**k
    return R

zpx=[[0,xi]+[0]*(N-1) for xi in xv]; zpy=[[0,yi]+[0]*(N-1) for yi in yv]
Px=psi_dev(zpx); Py=psi_dev(zpy); K=[sp.Integer(0)]*(N+1)
for perm in itertools.permutations(range(3)):
    yp=[yv[i] for i in perm]; DD=sum(xv[i]*yp[i] for i in range(3)); inv=invden(DD)
    zps=[]
    for i in range(3):
        num=[sp.Rational(1,3),(xv[i]+yp[i])/s2,sp.Rational(3,2)*xv[i]*yp[i]]+[0]*(N-2)
        pi=pmul(num,inv); pi[0]-=sp.Rational(1,3); zps.append(pi)
    P=psi_dev(zps); weight=[1,0,sp.Rational(3,2)*DD]+[0]*(N-2); WP=pmul(weight,P)
    K=[sp.expand(K[k]+WP[k]/6) for k in range(N+1)]
H=[sp.factor(sp.expand((Px[k]+Py[k])/2-K[k])) for k in range(N+1)]
Az=sum(v**2 for v in xv); Bz=sum(v**2 for v in yv); Cxz=sum(v**3 for v in xv); Cyz=sum(v**3 for v in yv)
H4z=sp.Rational(1,32)*(5*Az**2-2*Az*Bz+5*Bz**2)
alpha_z=-sp.Rational(27,16)+27*s2/64; beta_z=39*s2/16
H5z=alpha_z*(Az*Cxz+Bz*Cyz)+beta_z*(Az*Cyz+Bz*Cxz)
H6z=(sp.Rational(243,320)*(Az**3+Bz**3)+sp.Rational(81,80)*(Cxz**2+Cyz**2)
     +sp.Rational(3,32)*(Az**2*Bz+Az*Bz**2)-sp.Rational(45,16)*Cxz*Cyz)
assert sp.expand(H[4]-H4z)==0 and sp.expand(H[5]-H5z)==0 and sp.expand(H[6]-H6z)==0
print('CORRECTED_H4_EXACT_PASS'); print('CORRECTED_H5_EXACT_PASS'); print('CORRECTED_H6_EXACT_PASS')
print('H5_z_alpha =',alpha_z); print('H5_z_beta =',beta_z)
print('H6_z_coeffs =',sp.Rational(243,320),sp.Rational(81,80),sp.Rational(3,32),-sp.Rational(45,16))
print('H5_m_alpha =',-sp.Rational(1,4)+s2/16); print('H5_m_beta =',13*s2/36)
print('H6_m_coeffs =',sp.Rational(9,40),sp.Rational(1,20),sp.Rational(1,36),-sp.Rational(5,36))

# --- outward-rounded radius 1/4 proof ---
mp.mp.dps=50; iv=mp.iv; SQ2=iv.sqrt(2); TARGET=mp.mpf('0.001')
am=-iv.mpf(1)/4+SQ2/16; bm=13*SQ2/36
a7=-iv.mpf(1)/2+SQ2/16; b7=-7*SQ2/24; g7=-19*SQ2/48
c1=-iv.mpf(9)/8+9*SQ2/128; c2=-iv.mpf(1)/18+SQ2/288; c4=SQ2/6; c5=SQ2/12; c6=83*SQ2/96
alpha11=-iv.mpf(2)/5+SQ2/80; beta11=-iv.mpf(27)/10+27*SQ2/320; delta11=-125*SQ2/288; eps11=-51*SQ2/64; zeta11=-55*SQ2/96
v1=-2+SQ2/32; v2=27*(-64+SQ2)/256; v3=83*SQ2/192; v4=35*SQ2/96; v5=5*SQ2/16; v6=517*SQ2/384

def Pk(k,t,x,y):
    if k==4: return (5-2*t*t+5*t**4)/72
    if k==5: return am*(x+t**5*y)+bm*(t**3*y+t**2*x)
    if k==6: return iv.mpf(9)/40*(1+t**6)+iv.mpf(1)/20*(x*x+t**6*y*y)+iv.mpf(1)/36*(t**2+t**4)-iv.mpf(5)/36*t**3*x*y
    if k==7: return a7*(x+t**7*y)+b7*(t**2*x+t**5*y)+g7*(t**4*x+t**3*y)
    if k==8: return iv.mpf(27)/64*(1+t**8)+iv.mpf(1)/4*(x*x+t**8*y*y)+iv.mpf(1)/6*(t**6+t**2)+iv.mpf(1)/16*t**3*x*y*(1+t**2)-iv.mpf(59)/288*t**4
    if k==9: return c1*(x+t**9*y)+c2*(x**3+t**9*y**3)+c4*(t**6*x+t**3*y)+c5*(t**6*x*y**2+t**3*x**2*y)+c6*(t**5*y+t**4*x)
    if k==10: return iv.mpf(27)/32*(1+t**10)+iv.mpf(15)/16*(x*x+t**10*y*y)-iv.mpf(5)/36*t**3*x*y*(1+t**4)-iv.mpf(5)/24*t**4*(1+t**2)+iv.mpf(1)/6*(t**6*y*y+t**4*x*x)+iv.mpf(67)/576*t**5*x*y
    if k==11: return alpha11*(x**3+t**11*y**3)+beta11*(x+t**11*y)+delta11*(t**5*x*x*y+t**6*x*y*y)+eps11*(t**6*x+t**5*y)+zeta11*(t**4*x+t**7*y)
    if k==12: return iv.mpf(31)/528*(x**4+t**12*y**4)+iv.mpf(279)/88*(x*x+t**12*y*y)+iv.mpf(2511)/1408*(1+t**12)+iv.mpf(101)/240*t**6*x*x*y*y-iv.mpf(643)/1440*(t**6*x*x+t**6*y*y)+iv.mpf(95)/576*(t**5+t**7)*x*y+iv.mpf(5)/16*(t**8+t**4)+iv.mpf(833)/2880*t**6
    if k==13: return v1*(x**3+t**13*y**3)+v2*(x+t**13*y)+v3*(t**7*x*x*y+t**6*x*y*y)+v4*(t**8*x*y*y+t**5*x*x*y)+v5*(t**8*x+t**5*y)+v6*(t**6*x+t**7*y)
    if k==14: return iv.mpf(63)/104*(t**14*y**4+x**4)+iv.mpf(8505)/832*(t**14*y*y+x*x)+iv.mpf(6561)/1664*(1+t**14)-iv.mpf(19)/48*(t**8+t**6)*x*x*y*y+iv.mpf(29)/96*(t**8*x*x+t**6*y*y)-iv.mpf(35)/96*(t**9+t**5)*x*y+iv.mpf(59)/96*(t**6*x*x+t**8*y*y)+iv.mpf(257)/1152*t**7*x*y-iv.mpf(139)/192*(t**8+t**6)
    raise ValueError(k)

def endpoint15_coeff(r):
    return iv.mpf(1)/2*iv.mpf(2)**15/(15*14)/(1-2*r)+iv.mpf(2)**15/(15*14)*iv.mpf(2)**(-iv.mpf(15)/2)/(1-SQ2*r)

def tail15_coeff(r,t):
    den=1+t**4; z=r**2*t
    Ce=(endpoint15_coeff(r)+t**15*endpoint15_coeff(t*r))/den
    Cjd=r*t**8/(56*(1-z)*den)
    ell=(1+t)/SQ2; q=t/2
    C26=(7-6*z)/(1-z)**2; C25=(6-5*z)/(1-z)**2
    Ccub=iv.mpf(1)/3/den*(ell**3*t**6*C26+3*r*ell**2*q*t**6*C26+3*ell*q**2*t**5*C25+r*q**3*t**5*C25)
    C36=(28-48*z+21*z**2)/(1-z)**3; C35=(21-35*z+15*z**2)/(1-z)**3; C34=(15-24*z+10*z**2)/(1-z)**3
    Cquart=iv.mpf(2)/9/den*(r*ell**4*t**6*C36+4*ell**3*q*t**5*C35+6*r*ell**2*q**2*t**5*C35+4*ell*q**3*t**4*C34+r*q**4*t**4*C34)
    return Ce+Cjd+Ccub+Cquart

def lower_box(box):
    r=iv.mpf([box[0][0],box[0][1]]); t=iv.mpf([box[1][0],box[1][1]]); x=iv.mpf([box[2][0],box[2][1]]); y=iv.mpf([box[3][0],box[3][1]])
    den=1+t**4; val=iv.mpf(0)
    for k in range(4,15): val += Pk(k,t,x,y)/den*r**(k-4)
    return val-tail15_coeff(r,t)*r**11

stack=[(((0.0,0.25),(0.0,1.0),(-1.0,1.0),(-1.0,1.0)),0)]
evaluated=leaves=max_depth=0; min_leaf=mp.inf
while stack:
    box,depth=stack.pop(); lo=mp.mpf(lower_box(box).a); evaluated+=1
    if lo>TARGET:
        leaves+=1; min_leaf=min(min_leaf,lo); max_depth=max(max_depth,depth); continue
    widths=[(box[0][1]-box[0][0])/0.25,box[1][1]-box[1][0],(box[2][1]-box[2][0])/2,(box[3][1]-box[3][0])/2]
    dim=max(range(4),key=lambda j:widths[j]); mid=(box[dim][0]+box[dim][1])/2
    b1=list(box); b2=list(box); b1[dim]=(box[dim][0],mid); b2[dim]=(mid,box[dim][1])
    stack.append((tuple(b1),depth+1)); stack.append((tuple(b2),depth+1))
print('RMAX = 0.25'); print('TARGET_NORMALIZED_GAP =',TARGET); print('evaluated_boxes =',evaluated); print('certified_leaf_boxes =',leaves); print('max_depth =',max_depth); print('minimum_certified_leaf_lower =',min_leaf)
assert min_leaf>TARGET
print('RADIUS_025_PASS'); print('OVERALL_PASS')
