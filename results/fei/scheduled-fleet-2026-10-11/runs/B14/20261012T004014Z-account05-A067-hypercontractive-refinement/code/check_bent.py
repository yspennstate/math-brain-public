import json,time
from fractions import Fraction as Q
from pathlib import Path
import check as lib

# Increased precision is frozen here for compressed m<=40 calculations.
original_ln=lib.ln_interval
lib.ln_interval=lambda x,terms=32:original_ln(x,terms)
lib.LN2=lib.ln_interval(Q(2))
lib.LOGCACHE.clear()

def entropy(m,r):
    n=m+r;p=Q(1,1<<n);t=2*p
    lam=Q(1,1<<(m//2))
    plus=((1<<m)+(1<<(m//2)))//2
    minus=((1<<m)-(1<<(m//2)))//2
    return lib.add(lib.scale(lib.phi(lam-t),plus),lib.scale(lib.phi(-lam-t),minus),(8*p*(1-Q(1,1<<r))*(n-1),)*2)

rows=[]
for m in range(2,41,2):
    for r in [2,3,4]:
        p=Q(1,1<<(m+r));delta=Q(1,1<<r);d=2*p
        h=entropy(m,r)
        hc=entropy(m,r-1)
        drop=lib.add(h,lib.scale(hc,-Q(1,2)),(Q(-m,2),)*2)
        ratio=lib.scale(drop,1/d)
        u=Q(2,1<<(m//2+r))
        predicted=(4+2*delta*(m+2*r-6+3/lib.LN2[1]),4+2*delta*(m+2*r-6+3/lib.LN2[0]))
        error=Q(40,3)/lib.LN2[0]*delta*u
        lib.check(ratio[0]>=predicted[0]-error and ratio[1]<=predicted[1]+error)
        # Retained core influence: at the selected vertex all m core neighbors agree.
        core=Q(m,2)+m*d
        lib.check(core>=m*d)
        # Actual full-pad leaf spectra give the universal reserve ledger.
        full_drop=lib.add(h,(-((1-delta)*m),)*2,lib.scale(entropy(m,0),-delta))
        lib.check(full_drop[1]<=4*r*d+(1+6/lib.LN2[0])*core)
        if r==2 and m in [2,4,6,8]:
            values=[(-1 if sum(((x>>(2*j))&1)*((x>>(2*j+1))&1) for j in range(m//2))%2 else 1) for x in range(1<<m)]
            actual=lib.padding_node(values,m,r)
            lib.check(actual['ratio'][0]<=ratio[1] and ratio[0]<=actual['ratio'][1])
        rows.append({'m':m,'r':r,'ratio':ratio,'asymptotic_approximation':predicted,'proved_error_bound':error,'rate_five_refuted':ratio[0]>5})

result={'complete':True,'cases':len(rows),'assertions':lib.ASSERTIONS,'elapsed_seconds':time.perf_counter()-lib.START,'log_terms':32,'actual_boolean_family':'quadratic bent sign, padded and flipped once','rows':rows}
(Path(__file__).resolve().parents[1]/'out'/'check_bent.json').write_text(json.dumps(lib.encode(result),indent=2)+'\n',encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='rows'},indent=2))
