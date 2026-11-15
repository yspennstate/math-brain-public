"""Exact formulas and independent census/resource audits for FEIB25."""
import itertools,json,math,hashlib
from fractions import Fraction
from pathlib import Path
import numpy as np
from levels import ROOT,profile,threshold,plan

def burnside(n):
    N=1<<n;total=0;elements=0
    for perm in itertools.permutations(range(n)):
        for mask in range(N):
            image=[sum(((x>>j)&1)<<perm[j] for j in range(n))^mask for x in range(N)]
            visited=set();cycles=[]
            for x in range(N):
                if x in visited:continue
                y=x;length=0
                while y not in visited:visited.add(y);length+=1;y=image[y]
                cycles.append(length)
            total+=1<<len(cycles)
            if all(v%2==0 for v in cycles):total+=1<<len(cycles)
            elements+=2
    assert total%elements==0
    return dict(group_elements=elements,orbits=total//elements)

def main():
    coverage={str(n):burnside(n) for n in range(1,6)}
    for n in range(1,6):
        here=(ROOT/f'npn{n}.bin').read_bytes()
        prior=(ROOT.parent/'FEIB13'/f'npn{n}.bin').read_bytes()
        assert here==prior
        assert len(here)//4==coverage[str(n)]['orbits']
        coverage[str(n)]['matches_prior_bytes']=True
    (ROOT/'coverage_audit.json').write_text(json.dumps(coverage,indent=2))
    rows=[];discrep=0.
    for m in [3,5,7,9,13,15,31,63,127,255,511,1023,4095,16383,65535]:
        r=(m-1)//2
        # math.comb computes the integer numerator exactly before division.
        b=float(Fraction(math.comb(2*r,r),1<<(2*r)))
        L=m*b*b/4*math.log2(1+1/(b*b))
        row=dict(m=m,b=b,W_previous=.25,W_target=(1+m*b*b)/4,A_target=.25+L,
                 lower_bound=.25+.125*math.log2(r+2),
                 I_d2=1.5+m*b/2,G=.5+2*L,L1_ratio_d2=(.25+L)/(.75+m*b*b/2))
        if m<=13:
            maj=threshold(m,(m+1)//2);h=np.r_[maj,np.ones_like(maj)];f=np.r_[h,-h];p=profile(f)
            error=max(abs(p['A'][2]-row['A_target']),abs(p['W'][1]-.25),
                      abs(p['W'][2]-row['W_target']),abs(p['I']-row['I_d2']),abs(p['G']-row['G']))
            discrep=max(discrep,error)
            assert error<1e-12
        rows.append(row)
    (ROOT/'selector_majority.json').write_text(json.dumps(dict(rows=rows,max_truth_table_formula_discrepancy=discrep),indent=2))
    # A full larger-n profile using the exact majority coefficient recurrence.
    # c_{k+2}/c_k=-k/(m-k-1), hence the recurrence for aggregate W_k below.
    m=1023;r=(m-1)//2;b=float(Fraction(math.comb(2*r,r),1<<(2*r)))
    wm=np.zeros(m+1);wm[1]=m*b*b
    for k in range(1,m-1,2):wm[k+2]=wm[k]*k*k*(m-k)/((k+2)*(k+1)*(m-k-1))
    assert abs(wm.sum()-1)<1e-12
    wh=np.zeros(m+2);wh[:m+1]+=.25*wm;wh[1:]+=.25*wm;wh[0]+=.25;wh[1]+=.25
    ah=np.zeros(m+2);term=m*b*b/4*math.log2(1+1/(b*b));ah[1]=.25+term;ah[2]=term
    ah[1:]+=.25*wm
    for parity in [0,1,2]:
        W=np.r_[np.zeros(parity),wh];A=np.r_[np.zeros(parity),ah];n=m+1+parity
        (ROOT/f'selector_profile_n{n}.json').write_text(json.dumps(dict(n=n,W=W.tolist(),A=A.tolist(),dW=(np.arange(n+1)*W).tolist(),prev_dW=np.r_[0,np.arange(n)*W[:-1]].tolist()),indent=2))
    print(json.dumps(dict(coverage=coverage,selector_formula_error=discrep,last_selector=rows[-1]),indent=2))

if __name__=='__main__':main()
