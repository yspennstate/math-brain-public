"""Exact integer core for symmetric Boolean functionals. Logs are base 2."""
from math import comb
import mpmath as mp

def integer_data(f):
    n = len(f)-1
    d = list(map(int, f))
    rows=[]
    for k in range(n+1):
        cs=[1]
        for t in range(n-k): cs.append(cs[-1]*(n-k-t)//(t+1))
        rows.append((sum(c*x for c,x in zip(cs,d)),
                     sum(c*abs(x) for c,x in zip(cs,d)),
                     sum(c*x*x for c,x in zip(cs,d)),
                     sum(c for c,x in zip(cs,d) if x)))
        d=[d[t]-d[t+1] for t in range(n-k)]
    return rows

def evaluate(f, dps=70):
    with mp.workdps(dps):
        n=len(f)-1; rows=integer_data(f)
        vals={k:mp.mpf(0) for k in ['A','B','Gamma','P','H','I']}
        den=mp.mpf(2)**(2*n)
        for k,(F,L,Q,N) in enumerate(rows):
            if not F: continue
            w=mp.mpf(comb(n,k))*F*F/den
            mu=mp.mpf(F)*F/den
            def log_dyadic(num,bits):
                power=1<<bits
                if 2*num>power:
                    return mp.log1p(mp.mpf(num-power)/power)/mp.log(2)
                return mp.log(mp.mpf(num),2)-bits
            log_up=log_dyadic(Q,n+k)
            log_mu=log_dyadic(F*F,2*n)
            vals['A']-=w*log_up
            R=Q*(1<<(n-k))
            vals['B']+=w*mp.log1p(mp.mpf(R-F*F)/(F*F))/mp.log(2)
            vals['Gamma']+=w*mp.log1p(mp.mpf(L-abs(F))/abs(F))/mp.log(2)
            vals['P']-=w*log_dyadic(N,n-k)
            vals['H']-=w*log_mu
            vals['I']+=k*w
        vals['balanced']=(rows[0][0]==0)
        vals['value_vector']=''.join('+' if x>0 else '-' for x in f)
        vals['n']=n
        for name in ['A','B','Gamma','P','H']:
            vals[name+'/I']=vals[name]/vals['I'] if vals['I'] else None
            vals[name+'/(I-1)']=vals[name]/(vals['I']-1) if vals['balanced'] and vals['I']>1 else None
        return vals

def mask_vector(n,mask):
    return [1]+[-1 if mask>>(t-1)&1 else 1 for t in range(1,n+1)]

if __name__=='__main__':
    import sys,json
    f=[1 if x=='+' else -1 for x in sys.argv[1]]
    print(json.dumps(evaluate(f),default=str,indent=2))
