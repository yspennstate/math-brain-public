"""Exact bivariate algebra for the q=3 local radius.

No probability theorem is asserted by this script. It checks the closed-form
coefficient inequality on a continuous rectangle, conditional on the plan.
"""
import argparse,ctypes,hashlib,json,math,pathlib,time
from fractions import Fraction as F
import sympy as sp

ROOT=pathlib.Path(__file__).resolve().parent

def memory_check():
    class Memory(ctypes.Structure):
        _fields_=[('length',ctypes.c_ulong),('load',ctypes.c_ulong),
                  ('total',ctypes.c_ulonglong),('available',ctypes.c_ulonglong),
                  ('page_total',ctypes.c_ulonglong),('page_available',ctypes.c_ulonglong),
                  ('virtual_total',ctypes.c_ulonglong),('virtual_available',ctypes.c_ulonglong),
                  ('extended',ctypes.c_ulonglong)]
    info=Memory();info.length=ctypes.sizeof(info)
    assert ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(info))
    assert info.available>=2*1024**3
    return info.available

def coefficients(d,k,l):
    # Works in either the exact rational field or symbolic rational functions.
    Z=k*(k-1)/2+d*(d-k)
    Cu=5*Z/(d*(d-1));Ct=Cu*(1+l)/3
    Kp=d/(9*(d-1));K=1/(9*(1-l))
    A2=Kp*Cu/d**3
    B2=Kp*(3*Ct**2/d**3+l*Cu*Ct/d**3+Cu**2/(12*d**4))
    S1=k*(k-1)/2-1;S2=k*(k-1)*(k-2)/3
    su=(Cu*S1+F(5,2)*S2)/d**2
    st=l*Ct*S1/d+F(5,6)*S2/d**2
    ve=Cu/d**2;te=l*Ct/d
    A=A2+S2/(72*d**3)+K*(Cu*S1+F(5,4)*S2)/d**3
    B=B2+K*((3*te+ve/2)*st+(te/2+ve/12)*su)
    g=k*(k-1)/(12*d**2)
    return A,B,g,Cu,Ct

def finite_recurrence_checks():
    rows=[]
    for d_int in (4,9,16,25,49):
        d=F(d_int);l=F(1,math.isqrt(d_int))
        for k_int in sorted({2,3,d_int//2,d_int-1,d_int}):
            if k_int<2:continue
            k=F(k_int);A,B,g,Cu,Ct=coefficients(d,k,l)
            Kp=d/(9*(d-1));K=1/(9*(1-l));ve=Cu/d**2;te=l*Ct/d
            aa=Kp*Cu/d**3
            bb=Kp*(3*Ct**2/d**3+l*Cu*Ct/d**3+Cu**2/(12*d**4))
            for j_int in range(2,k_int):
                j=F(j_int);uj=(j*Cu+F(5,2)*j*(j-1))/d**2
                tj=j*l*Ct/d+F(5,6)*j*(j-1)/d**2
                gj=j*(j-1)/(12*d**2)
                aa+=gj/(6*d)+K*(uj/(2*d)+j*Cu/(2*d**3))
                bb+=K*(3*tj*te+(uj*te+tj*ve)/2+uj*ve/12)
            assert (aa,bb)==(A,B)
            rows.append({'d':d_int,'k':k_int,'A':str(A),'B':str(B),'g':str(g)})
    return rows

def integer_coefficients(poly):
    common=math.lcm(*(int(v.q) for _,v in poly.terms()))
    out={tuple(k):int(v*common) for k,v in poly.terms()}
    content=math.gcd(*out.values());assert common>0 and content>0
    return {k:v//content for k,v in out.items()},common,content

def bernstein_axis(poly,axis,n):
    common=math.lcm(*(math.comb(n,i) for i in range(n+1)));out={}
    for key,value in poly.items():
        for j in range(key[axis],n+1):
            kk=list(key);kk[axis]=j;kk=tuple(kk)
            out[kk]=out.get(kk,0)+value*math.comb(j,key[axis])*(common//math.comb(n,key[axis]))
    out={k:v for k,v in out.items() if v};content=math.gcd(*out.values())
    return {k:v//content for k,v in out.items()},common,content

def save(name,phase,poly,meta):
    data=dict(meta);data['phase']=phase;data['poly']=[[list(k),v] for k,v in sorted(poly.items())]
    target=ROOT/f'uniform_local_{name}_{phase}.json'
    target.write_text(json.dumps(data,separators=(',',':')),encoding='utf-8')
    print(json.dumps({'phase':phase,'terms':len(poly),'negative':sum(v<0 for v in poly.values())}),flush=True)

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--M',required=True)
    parser.add_argument('--lambda-max',required=True);parser.add_argument('--margin',default='1/100')
    parser.add_argument('--name',required=True);args=parser.parse_args()
    start=time.monotonic();free=memory_check();m=F(args.M);upper=F(args.lambda_max);margin=F(args.margin)
    assert 0<m<=6 and 0<upper<1 and 0<margin<1
    recurrence=finite_recurrence_checks()
    l,r,z=sp.symbols('l r z');d=1/l**2;k=2+r*(d-2)
    A,B,g,Cu,Ct=coefficients(d,k,l)
    gap=sp.cancel((1-sp.Rational(margin.numerator,margin.denominator))*g-sp.Rational(m.numerator,m.denominator)*A-sp.Rational(m.numerator**2,m.denominator**2)*B)
    numerator,denominator=sp.fraction(gap)
    # The denominator must be a nonzero constant times factors l,1-l,1+l.
    content,factors=sp.factor_list(denominator,l)
    sign=1 if content>0 else -1;exponents={'l':0,'1-l':0,'1+l':0}
    for factor,power in factors:
        if factor==l:exponents['l']+=power
        elif factor==l-1:exponents['1-l']+=power;sign*=(-1)**power
        elif factor==l+1:exponents['1+l']+=power
        else:raise AssertionError(('unexpected denominator factor',factor,power))
    assert sp.simplify(denominator-sign*abs(content)*l**exponents['l']*(1-l)**exponents['1-l']*(1+l)**exponents['1+l'])==0
    numerator=sp.expand(sign*numerator);denominator=sign*denominator
    poly=sp.Poly(numerator.subs(l,sp.Rational(upper.numerator,upper.denominator)*z),z,r,domain=sp.QQ)
    raw,common,gcd=integer_coefficients(poly);degrees=list(poly.degree_list())
    assert (degrees[0]+1)*(degrees[1]+1)*1000<10*1024**2
    meta={'status':'local radius algebra','M_radius':str(m),'posterior_x_radius':str(m/9),
          'lambda_upper':str(upper),'retained_drift_fraction':str(margin),'degrees':degrees,
          'denominator_positive_content':str(abs(content)),'denominator_factors':exponents,
          'raw_common_multiplier':str(common),'raw_content_divided_out':str(gcd),
          'normalization':'raw/common*content = positive_denominator*((1-margin)*g-M_radius*A-M_radius^2*B)',
          'finite_closed_form_checks':recurrence,'available_memory_before':free}
    save(args.name,'raw',raw,meta);current=raw;transforms=[]
    for axis in (0,1):
        current,den,div=bernstein_axis(current,axis,degrees[axis]);transforms.append({'axis':axis,'positive_multiplier':str(den),'positive_content_divided_out':str(div)})
        meta['transforms']=transforms.copy();save(args.name,f'bern{axis+1}',current,meta)
    negative=sum(v<0 for v in current.values());meta['status']='PASS coefficient inequality on entire rectangle' if negative==0 else 'INCOMPLETE: negative Bernstein coefficients'
    meta.update({'strictly_positive_coefficients':sum(v>0 for v in current.values()),'negative_coefficients':negative,
                 'implicit_zero_coefficients':math.prod(n+1 for n in degrees)-len(current),'wall_seconds':time.monotonic()-start,
                 'builder_sha256':hashlib.sha256(pathlib.Path(__file__).read_bytes()).hexdigest()})
    ROOT.joinpath(f'uniform_local_{args.name}_report.json').write_text(json.dumps(meta,indent=2),encoding='utf-8')
    print(json.dumps({k:v for k,v in meta.items() if k not in ['finite_closed_form_checks','transforms','available_memory_before']}),flush=True)

if __name__=='__main__':main()
