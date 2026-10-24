from fractions import Fraction
from math import gcd

TRUTH_MASK = 2624023184
N_BITS = 5
COORD = 2

def lcm(a,b): return a//gcd(a,b)*b

def fwht_int(vals):
    a=list(vals); h=1
    while h<len(a):
        for j in range(0,len(a),2*h):
            for k in range(j,j+h):
                x,y=a[k],a[k+h]; a[k],a[k+h]=x+y,x-y
        h*=2
    return a

def add(dst, src, scale=Fraction(1)):
    for m,c in src.items():
        dst[m]=dst.get(m,Fraction(0))+scale*c
        if dst[m]==0: del dst[m]

def log_ratio_terms(num_coeffs):
    # list of (weight, numerator, denominator), representing weight*log2(num/den)
    out={}
    for w,a,b in num_coeffs:
        if a!=1: out[a]=out.get(a,Fraction(0))+w
        if b!=1: out[b]=out.get(b,Fraction(0))-w
    return out

def data(vals):
    n=(len(vals)).bit_length()-1; D=1<<(2*n)
    W=fwht_int(vals); P=[w*w for w in W]
    PI=[sum(P[t] for t in range(len(P)) if (t&s)==s) for s in range(len(P))]
    U=log_ratio_terms([(Fraction(P[s],D),PI[s],P[s]) for s in range(len(P)) if P[s]])
    return n,D,P,PI,U

def restrict(vals,i,bit):
    return [vals[s|(bit<<i)] for s in range(len(vals)) if not ((s>>i)&1)]

def certificate(vals,i):
    n,D,P,PI,U=data(vals)
    children=[]
    for bit in (0,1): children.append(data(restrict(vals,i,bit))[4])
    Delta=dict(U); add(Delta,children[0],Fraction(-1,2)); add(Delta,children[1],Fraction(-1,2))

    Bi={}; bit=1<<i
    for s in range(len(P)):
        if s&bit: continue
        a,b=P[s],P[s|bit]; t=a+b
        if a: add(Bi,log_ratio_terms([(Fraction(a,D),t,a)]))
        if b: add(Bi,log_ratio_terms([(Fraction(b,D),t,b)]))

    Ui={}
    for s in range(1,len(P)):
        if s&bit and P[s]:
            add(Ui,log_ratio_terms([(Fraction(P[s],D*s.bit_count()),PI[s],P[s])]))

    inf=Fraction(sum(P[s] for s in range(len(P)) if s&bit),D)
    influence=Fraction(sum(s.bit_count()*P[s] for s in range(len(P))),D)
    U0=log_ratio_terms([(Fraction(P[0],D),D,P[0])]) if P[0] else {}
    if influence:
        add(Ui,U0,inf/influence)
    R=dict(Delta); add(R,Bi,-1); add(R,Ui,Fraction(5,4))
    R[2]=R.get(2,Fraction(0))-2*inf  # rational c equals c*log2(2)
    if R[2]==0: del R[2]
    den=1
    for c in R.values(): den=lcm(den,c.denominator)
    exps={m:int(c*den) for m,c in R.items()}
    pos=1; neg=1
    for m,e in exps.items():
        if e>0: pos*=pow(m,e)
        elif e<0: neg*=pow(m,-e)
    return inf,den,exps,pos,neg

if __name__=='__main__':
    vals=[1 if (TRUTH_MASK>>j)&1 else -1 for j in range(1<<N_BITS)]
    inf,den,exps,pos,neg=certificate(vals,COORD)
    print('truth_mask',TRUTH_MASK,'coordinate',COORD,'influence',inf)
    print('scale',den,'nonzero_log_atoms',len(exps))
    print('positive_bits',pos.bit_length(),'negative_bits',neg.bit_length())
    print('integer_comparison',pos>neg)
    print('difference_bits',(pos-neg).bit_length())
    assert pos>neg
    print('PASS: Delta_i U - B_i + (5/4) U_i^star - 2 Inf_i > 0 exactly')

