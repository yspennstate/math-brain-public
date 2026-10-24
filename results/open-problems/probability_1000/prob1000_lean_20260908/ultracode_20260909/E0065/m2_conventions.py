# m=2, two conventions and two criteria.
# Convention 1 (ordered pairs, source eq (4)): f(x)=a x^2 + 2b x(1-x) + c(1-x)^2, a,b,c in [al,1-al].
# Convention 2 (unordered, mixed coefficient itself bounded): f(x)=a x^2 + b x(1-x) + c(1-x)^2, a,b,c in [al,1-al].
# Criterion L (local): fixed point has |f'(p)|>=1.  Criterion G (global): a 2-cycle exists (f(f(x))=x, x != p).
import numpy as np
def fixed_point(co):
    r=np.roots(co); r=[x.real for x in r if abs(x.imag)<1e-10 and -1e-9<=x.real<=1+1e-9]
    return r
def analyse(a,b,c,conv):
    mb = 2*b if conv==1 else b
    # f(x) = a x^2 + mb x(1-x) + c(1-x)^2 = (a-mb+c) x^2 + (mb-2c) x + c
    A=a-mb+c; B=mb-2*c; C=c
    fps=fixed_point([A,B-1,C])
    p=fps[0]
    fpr=2*A*p+B
    # 2-cycles: f(f(x))-x divided by (f(x)-x)
    f=np.poly1d([A,B,C]); ff=f(f); g=ff-np.poly1d([1,0]); h=f-np.poly1d([1,0])
    q,rem=np.polydiv(g,h)
    roots=np.roots(q); two=[x.real for x in roots if abs(x.imag)<1e-9 and -1e-9<=x.real<=1+1e-9]
    return p,fpr,len(two)>0
def sup_alpha(conv,crit,n=401):
    best=0;arg=None
    g=np.linspace(0,1,n)
    for a in g:
        for c in g:
            lam0=min(a,c,1-a,1-c)
            if lam0<=best: continue
            for b in g:
                lam=min(lam0,b,1-b)
                if lam<=best: continue
                p,fpr,two=analyse(a,b,c,conv)
                hit = abs(fpr)>=1 if crit=='L' else two
                if hit: best=lam;arg=(a,b,c,p,fpr,two)
    return best,arg
for conv in (1,2):
    for crit in ('L','G'):
        print("conv",conv,"crit",crit,sup_alpha(conv,crit))
print("(3-sqrt7)/2 =",(3-7**0.5)/2,"  (3-sqrt7)/4 =",(3-7**0.5)/4)
