"""Integer interval arithmetic: certify all gamma roots and the finite maximum.

No floating-point transcendental evaluation enters the certificate. Each integer
interval [L,U] represents [L/D,U/D], with D=10^100. Taylor terms are rounded
outwards after each multiplication. The exp tail is bounded geometrically.
"""
import csv, json, signal, time
from decimal import Decimal, localcontext, ROUND_FLOOR
from fractions import Fraction
signal.alarm(240)
START=time.monotonic(); D=10**100

def ceildiv(a,b): return -(-a//b)

def series_interval(x,terms):
    a,b=x.numerator,x.denominator
    assert a>=0
    lower=upper=D;sl=su=D
    for j in range(1,terms+1):
        lower=lower*a//(b*j)
        upper=ceildiv(upper*a,b*j)
        sl+=lower;su+=upper
    return sl,su,upper

def exp_interval(x):
    terms=400
    lo,hi,last_upper=series_interval(x,terms)
    a,b=x.numerator,x.denominator
    assert b*(terms+2)>a
    next_upper=ceildiv(last_upper*a,b*(terms+1))
    tail_upper=ceildiv(next_upper*b*(terms+2),b*(terms+2)-a)
    return lo,hi+tail_upper

def gamma_root_sign(k,t):
    pl,pu,_=series_interval(t,k-1)
    el,eu=exp_interval(t-1)
    if pl>eu:return 1,pl-eu
    if pu<el:return -1,el-pu
    return 0,0

def dec(x,digits=55):
    with localcontext() as ctx:
        ctx.prec=digits
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
    bounds=[];min_margin=None
    for row in csv.DictReader(open('gamma_results.csv')):
        k=int(row['k'])
        if k==1:
            bounds.append((k,Fraction(1),Fraction(1)));continue
        with localcontext() as ctx:
            ctx.prec=100
            floor=int((Decimal(row['t_k'])*10**40).to_integral_value(rounding=ROUND_FLOOR))
        lo=Fraction(floor,10**40);hi=lo+Fraction(1,10**40)
        sl,ml=gamma_root_sign(k,lo);sh,mh=gamma_root_sign(k,hi)
        assert (sl,sh)==(1,-1),(k,sl,sh)
        min_margin=min(ml,mh) if min_margin is None else min(min_margin,ml,mh)
        bounds.append((k,lo,hi))
    winner=bounds[3]
    gaps=[winner[1]/4-hi/k for k,lo,hi in bounds if k!=4]
    assert min(gaps)>0
    e1=Fraction(exp_interval(Fraction(1))[1],D)
    e2=Fraction(exp_interval(Fraction(2))[1],D)
    assert e1<Fraction(27183,10000)
    assert e2<Fraction(73891,10000)
    margin=3-e1-(4+2*e2)/100-Fraction(4,10000)
    assert margin>Fraction(9,100)
    out={'gamma_root_bracket_width':'1e-40','certified_endpoints':118,
         'maximum_k':4,'minimum_gap_from_winner_ratio':dec(min(gaps)),
         'minimum_survival_comparison_scaled_margin':str(min_margin),
         'f_0p01_certified_lower_bound':dec(margin),
         'roots':[{'k':k,'lower':dec(lo),'upper':dec(hi)} for k,lo,hi in bounds],
         'seconds':time.monotonic()-START}
    with open('rational_certificates.json','w') as f:json.dump(out,f,indent=2)
    print(json.dumps({k:v for k,v in out.items() if k!='roots'},indent=2))

if __name__=='__main__':main()
