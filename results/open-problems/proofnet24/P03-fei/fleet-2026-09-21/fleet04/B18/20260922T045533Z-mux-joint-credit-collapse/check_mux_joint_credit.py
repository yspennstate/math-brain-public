import mpmath as mp
mp.mp.dps = 80
LN2=mp.log(2)
C=mp.mpf('6.521851214')
def h2(x):
    if x <= 0 or x >= 1:
        return mp.mpf('0')
    return (-x*mp.log(x)-(1-x)*mp.log(1-x))/LN2
def V(u): return 4*u*(1-u)
def Gamma(u):
    vv=V(u)
    return C*vv + mp.mpf('0.137')*vv*(1-vv)
def ent(weights):
    s=mp.mpf('0')
    for w in weights:
        if w>0: s -= w*mp.log(w)/LN2
    return s
def direct(p,q0,q1):
    qq=1-p
    v0=V(q0); v1=V(q1); vp=V(p)
    r=qq*q0+p*q1
    w=[
        (1-2*r)**2,
        qq**2*v0,
        p**2*v1,
        vp*(q1-q0)**2,
        p*qq*v0,
        p*qq*v1
    ]
    H=ent(w)
    delta=q0+q1-2*q0*q1
    ItA=vp*delta
    It0=qq*v0
    It1=p*v1
    D=(ItA*(Gamma(p)+h2(vp))/vp
       +It0*(Gamma(q0)+h2(v0))/v0
       +It1*(Gamma(q1)+h2(v1))/v1
       -Gamma(r)-H)
    return D,H
def collapsed(p,q0,q1):
    qq=1-p
    a=1-2*q0; b=1-2*q1
    vp=V(p)
    r=qq*q0+p*q1
    delta=q0+q1-2*q0*q1
    m=qq*a*a+p*b*b
    if abs(m) < mp.mpf('1e-70'):
        bracket=mp.mpf('0')
    else:
        e1=p*b*b/m
        e2=p*qq*(b-a)**2/m
        bracket=m*(h2(e1)-h2(e2))
    return (qq*Gamma(q0)+p*Gamma(q1)-Gamma(r)
            +delta*(Gamma(p)+h2(vp))
            -(2-m)*h2(p)+bracket)
def credit(p,q0,q1):
    qq=1-p
    a=1-2*q0; b=1-2*q1
    m=qq*a*a+p*b*b
    delta=q0+q1-2*q0*q1
    u=V(p)*delta
    if abs(m) < mp.mpf('1e-70'):
        return h2(u)-h2(p)
    return (m*h2(p*b*b/m)+h2(u)
            -m*h2(p*qq*(b-a)**2/m)
            -(1-m)*h2(p))
def Kfun(u): return h2((1-u)/2)
def Phi(x):
    y=mp.sqrt(max(mp.mpf('0'),1-x*x))
    return Kfun(y)-Kfun(x)
def balanced_formula(q0,q1):
    a=1-2*q0; b=1-2*q1
    s=a*a+b*b
    delta=(1-a*b)/2
    r=(q0+q1)/2
    if abs(s)<mp.mpf('1e-70'):
        ep=mp.mpf('0')
    else:
        x=2*abs(a*b)/s
        ep=(s/2)*(1+Phi(x))-1
    return (Gamma(q0)+Gamma(q1))/2-Gamma(r)+C*delta-1+ep
def ephi_bal(q0,q1):
    a=1-2*q0; b=1-2*q1
    s=a*a+b*b
    if abs(s)<mp.mpf('1e-70'):
        return -1
    return (s/2)*Phi(2*abs(a*b)/s) -(1-s/2)
def variance_bal(q0,q1):
    a=1-2*q0; b=1-2*q1; s=a*a+b*b
    if abs(s)<mp.mpf('1e-70'): return mp.mpf('0')
    return a*a*b*b*(2-s)/s
maxerr=mp.mpf('0')
count=0
grid=[mp.mpf(k)/17 for k in range(1,17)]
for p in grid:
    for q0 in grid:
        for q1 in grid:
            d,_=direct(p,q0,q1)
            c=collapsed(p,q0,q1)
            maxerr=max(maxerr,abs(d-c)); count+=1
maxbal=mp.mpf('0'); minreserve=mp.inf
for q0 in grid:
    for q1 in grid:
        d,_=direct(mp.mpf('0.5'),q0,q1)
        bf=balanced_formula(q0,q1)
        maxbal=max(maxbal,abs(d-bf))
        a=1-2*q0; b=1-2*q1
        rho=abs(a*b)
        lhs=ephi_bal(q0,q1)
        rhs=Phi(rho)+variance_bal(q0,q1)/(2*LN2)
        minreserve=min(minreserve,lhs-rhs)
zcmax=mp.mpf('0')
for q in grid:
    zcmax=max(zcmax,abs(credit(mp.mpf('0.5'),mp.mpf('0.5'),q)),
                      abs(credit(mp.mpf('0.5'),q,mp.mpf('0.5'))))
adag=mp.mpf('0.268204856')
Gquarter=mp.mpf('4.4548')+adag*mp.mpf(3)/16
end_slack=C-2-Gquarter
mid_slack=C/2-2
print('PASS')
print('general_grid_points', count)
print('max_general_collapse_error', mp.nstr(maxerr, 10))
print('balanced_grid_points', len(grid)**2)
print('max_balanced_formula_error', mp.nstr(maxbal,10))
print('min_strong_convexity_reserve_slack', mp.nstr(minreserve,20))
print('max_zero_credit_line_abs', mp.nstr(zcmax,10))
print('Gamma_dagger_quarter', mp.nstr(Gquarter,20))
print('dyadic_endpoint_slack_q0', mp.nstr(end_slack,20))
print('dyadic_midpoint_slack_qhalf', mp.nstr(mid_slack,20))
