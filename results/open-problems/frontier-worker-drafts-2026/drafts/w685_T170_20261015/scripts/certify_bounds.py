"""Standalone exact verifier: rational inputs, Fraction arithmetic, bounded series.

No float, NumPy, scipy, or exploratory output is used. Run with python -I -X utf8.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import json,hashlib
from datetime import datetime,timezone

ROOT=Path(__file__).resolve().parents[1]

def canonical(axes):
    labels={}
    return tuple(labels.setdefault(a,len(labels)) for a in axes)

def build_states():
    states=[]
    for axes in ((0,0),(0,1)):
        for a in (-1,1):
            for b in (-1,1):
                if axes==(0,0) and a!=b:continue
                for counts in ((0,0),(1,0),(1,1)):
                    if axes==(0,0) and counts[1]==1:continue
                    states.append((axes,(a,b),counts))
    return states

STATES=build_states()
INDEX={a:i for i,a in enumerate(STATES)}

def matrix(d,s,z):
    mat=[[Q(0) for _ in STATES] for _ in STATES]
    for i,(axes,signs,(c1,c2)) in enumerate(STATES):
        r=1+max(axes)
        for a in range(r+1):
            mult=1 if a<r else d-r
            if mult<=0:continue
            for sign in (-1,1):
                if a==axes[1] and sign==-signs[1]:continue
                h=int(a==axes[0] and sign==-signs[0] and axes[0]!=axes[1])
                if h and c2:continue
                new=(canonical((axes[1],a)),(signs[1],sign),(c2+h,h))
                mat[i][INDEX[new]]+=mult*z**sign/(s+1+c1+h)
    return mat

def cosh_bounds(x,terms=40):
    assert x>=0
    term,total=Q(1),Q(1)
    for j in range(1,terms+1):
        term=term*x*x/((2*j-1)*(2*j))
        total+=term
    first=term*x*x/((2*terms+1)*(2*terms+2))
    ratio=x*x/((2*terms+3)*(2*terms+4))
    assert 0<=ratio<1
    return total,total+first/(1-ratio)

def sinh_bounds(x,terms=40):
    assert x>=0
    term,total=x,x
    for j in range(1,terms+1):
        term=term*x*x/((2*j)*(2*j+1))
        total+=term
    first=term*x*x/((2*terms+2)*(2*terms+3))
    ratio=x*x/((2*terms+4)*(2*terms+5))
    assert 0<=ratio<1
    return total,total+first/(1-ratio)

def log_bounds(z,terms=80):
    assert z>1
    u=(z-1)/(z+1)
    term=u;total=Q(0)
    for j in range(terms+1):
        total+=2*term/(2*j+1)
        term*=u*u
    upper=total+2*term/((2*terms+3)*(1-u*u))
    return total,upper

def sqrt_bounds(n,scale=10**16):
    k=isqrt(n*scale*scale)
    lower=Q(k,scale)
    upper=lower if k*k==n*scale*scale else Q(k+1,scale)
    assert lower*lower<=n<=upper*upper
    return lower,upper

def floor_decimal(q,places=12):
    scale=10**places;k=q.numerator*scale//q.denominator
    return str(k//scale)+'.'+str(k%scale).zfill(places)

def exact(q):
    return dict(n=str(q.numerator),d=str(q.denominator))

def main():
    params_file=ROOT/'scripts/certificate_parameters.json'
    params=json.loads(params_file.read_text(encoding='utf-8'))['rows']
    # Positive root of alpha*sinh(alpha)-cosh(alpha)=0, derivative alpha*cosh(alpha)>0.
    al=Q(119967864025,10**11);au=Q(119967864026,10**11)
    cl,ch=cosh_bounds(al);sl,sh=sinh_bounds(al)
    assert al*sh-cl<0
    cl,ch=cosh_bounds(au);sl,sh=sinh_bounds(au)
    assert au*sl-ch>0
    ceg_upper=Q(331371710,10**9)
    assert 4*ceg_upper*ceg_upper>au*au-1
    results=[]
    lines=['d\tCEG_upper_display\tblock2_lower_floor\thairpin_lower_floor\thairpin_gain_percent_floor\tMv_over_v_upper_display']
    for p in params:
        d=p['d'];sqlo,sqhi=sqrt_bounds(d)
        baseline_upper=ceg_upper/sqlo
        b=p['block2'];theta=Q(b['theta_n'],b['theta_d']);s=Q(b['s_n'],b['s_d'])
        _,c2hi=cosh_bounds(2*theta)
        _,c1hi=cosh_bounds(theta)
        straight=1/(1+s)**2
        corner=2*(s+4)/(s+2)**3
        kernel_hi=2*d*straight*c2hi+2*d*(d-1)*corner*c1hi*c1hi
        assert kernel_hi<1,(d,'block2 kernel')
        block_lower=sqlo*theta/s
        h=p['hairpin'];z=Q(h['z_n'],h['z_d']);s=Q(h['s_n'],h['s_d'])
        v=[Q(a,h['v_d']) for a in h['v_n']]
        assert len(v)==16 and all(a>0 for a in v)
        mat=matrix(d,s,z)
        ratios=[sum((a*b for a,b in zip(row,v)),Q(0))/v[i] for i,row in enumerate(mat)]
        rho=max(ratios)
        assert rho<1,(d,'hairpin Mv<v')
        loglo,loghi=log_bounds(z)
        hairpin_lower=sqlo*loglo/s
        gain=hairpin_lower/baseline_upper-1
        assert hairpin_lower>baseline_upper
        result=dict(d=d,block2_kernel_upper=exact(kernel_hi),block2_lower=exact(block_lower),hairpin_rho_upper=exact(rho),hairpin_lower=exact(hairpin_lower),CEG_upper=exact(baseline_upper),hairpin_relative_gain_lower=exact(gain),log_z_lower=exact(loglo),log_z_upper=exact(loghi),status='exact arithmetic certificate; mathematical theorem awaits independent audit')
        results.append(result)
        # Every display is a rational floor. Displays do not replace exact comparisons.
        lines.append('\t'.join([str(d),floor_decimal(baseline_upper),floor_decimal(block_lower),floor_decimal(hairpin_lower),floor_decimal(100*gain,6),floor_decimal(rho)]))
    digest=hashlib.sha256(params_file.read_bytes()).hexdigest()
    (ROOT/'logs/exact_certificates.json').write_text(json.dumps(dict(at=datetime.now(timezone.utc).isoformat(),arithmetic='fractions.Fraction only; all series tails bounded',parameter_sha256=digest,states=STATES,alpha_interval=[exact(al),exact(au)],CEG_coefficient_upper=exact(ceg_upper),rows=results),indent=2)+'\n',encoding='utf-8')
    (ROOT/'logs/certified_bounds.tsv').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print('\n'.join(lines))
    print('PASS: all 17 rational kernel/vector and CEG comparison certificates.',flush=True)

if __name__=='__main__':main()
