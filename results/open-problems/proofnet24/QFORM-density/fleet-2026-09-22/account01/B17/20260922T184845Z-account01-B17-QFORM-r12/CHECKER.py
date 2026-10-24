import math

SQRT2 = math.sqrt(2.0)
PI = math.pi


def L(ell, a):
    D = 1.0 + 2.0*a*(1.0-ell)
    if ell == 0.0:
        return D**-0.5
    z = math.sqrt(3.0*ell*a/D)
    return D**-0.5 * math.sqrt(math.pi) * math.erf(z) / (2.0*z)


def f_y(y, e1, e2):
    if y <= 0.0:
        t = 0.0
    elif y >= 1.0:
        return 0.0
    else:
        t = y/(1.0-y)
    a = t*t + 0.5
    return (2.0/(PI*SQRT2))*L(e1,a)*L(e2,a)/(1.0-y)**2


def simpson(f,a,b):
    c=(a+b)/2.0
    return (b-a)*(f(a)+4.0*f(c)+f(b))/6.0


def adapt(f,a,b,eps,whole,depth):
    c=(a+b)/2.0
    left=simpson(f,a,c)
    right=simpson(f,c,b)
    if depth<=0 or abs(left+right-whole) <= 15.0*eps:
        return left+right+(left+right-whole)/15.0
    return adapt(f,a,c,eps/2.0,left,depth-1)+adapt(f,c,b,eps/2.0,right,depth-1)


def physical_peak(e1,e2):
    f=lambda y:f_y(y,e1,e2)
    # t=y/(1-y); the omitted y-tail is below the displayed precision target.
    b=1.0-1e-8
    whole=simpson(f,0.0,b)
    val=adapt(f,0.0,b,2e-10,whole,30)
    return 12.0*val


pairs=[(0,0),(0.25,0),(0.5,0),(1,0),(0.25,0.25),(0.5,0.5),(0.75,0.75),(1,1)]
print("3sqrt2", repr(3.0*SQRT2))
for p in pairs:
    print(p, repr(physical_peak(*p)))
