import json, time
from pathlib import Path
from fractions import Fraction as Q

ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
s,r=32,16
q,p=Q(1,1<<s),Q(1,1<<r)

def ln_bounds(y):
    z=(y-1)/(y+1); power=z; lo=Q(0)
    for j in range(22):
        lo+=2*power/(2*j+1); power*=z*z
    return lo,lo+2*power/(45*(1-z*z))

ln2=ln_bounds(Q(2))
def logarithm(prob):
    x=1/prob; k=0
    while x>=2: x/=2; k+=1
    lo,hi=ln_bounds(x)
    return Q(k)+lo/ln2[1],Q(k)+hi/ln2[0]

def entropy(hist):
    assert sum(count*mass for count,mass in hist)==1
    lo=hi=Q(0)
    for count,mass in hist:
        if mass:
            a,b=logarithm(mass)
            lo+=count*mass*a; hi+=count*mass*b
    return lo,hi

# The root core is balanced by its character bit. Histograms include every
# nonzero amplitude class; signs do not enter squared entropy.
root=[(1,(1-p)**2),((1<<r)-1,p*p),
      (1<<r,p*p*(1-2*q)**2),
      ((1<<r)*((1<<s)-1),4*p*p*q*q)]
plus=[(1,(1-2*p*q)**2),((1<<(r+s))-1,4*p*p*q*q)]
minus=[(1,(1-2*p*(1-q))**2),((1<<r)-1,4*p*p*(1-q)**2),
       ((1<<r)*((1<<s)-1),4*p*p*q*q)]
hr,hp,hm=map(entropy,(root,plus,minus))
bill=(hr[0]-(hp[1]+hm[1])/2,hr[1]-(hp[0]+hm[0])/2)
ratio=(bill[0]/p,bill[1]/p)
assert ratio[0]>Q(399,100)
grid=1<<64
ratio_export=(Q((ratio[0]*grid).__floor__(),grid),Q((ratio[1]*grid).__ceil__(),grid))
assert ratio_export[0]>Q(399,100)
Icore=1+2*s*q
Iroot=p*(Icore+r)
Iplus=2*(r+s)*p*q
Iminus=p*2*s*q+2*r*p*(1-q)
assert Iroot-(Iplus+Iminus)/2==p
assert time.monotonic()-start<60
result={'status':'PASS','parameters':{'s':s,'r':r,'t':1},'representation':'Exact compressed Fourier probability multiplicities from Boolean formulas; no cube enumeration','root_histogram':[[count,str(mass)] for count,mass in root],'positive_leaf_histogram':[[count,str(mass)] for count,mass in plus],'negative_leaf_histogram':[[count,str(mass)] for count,mass in minus],'queried_influence':str(p),'Pi_H_over_Pi_I_rational_enclosure':[str(x) for x in ratio_export],'export_rounding':'Exact outward floor/ceil to denominator 2^64; original rational interval is enclosed','certified_inequality':'399/100 < Pi_H/Pi_I','exact_sign_relative_to_4':'ABOVE' if ratio_export[0]>4 else ('BELOW' if ratio_export[1]<4 else 'UNRESOLVED'),'elapsed_seconds':time.monotonic()-start,'independent_review':'PENDING'}
(ROOT/'out'/'overhead_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'status':'PASS','certified_inequality':result['certified_inequality'],'exact_sign_relative_to_4':result['exact_sign_relative_to_4'],'ratio_decimal_diagnostic_only':[float(x) for x in ratio_export],'elapsed_seconds':result['elapsed_seconds']},indent=2))
