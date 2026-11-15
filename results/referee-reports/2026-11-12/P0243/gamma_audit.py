"""Independent gamma quantiles; no author code. Runtime bounded by tiny scalar problems."""
import csv, json, time
import mpmath as mp
mp.mp.dps=75

def survival(k,t):
    term=mp.mpf(1)
    total=term
    for j in range(1,k):
        term*=t/j
        total+=term
    return mp.exp(-t)*total

def quantile(k):
    lo=mp.mpf(0); hi=mp.mpf(2*k+10)
    target=mp.exp(-1)
    for _ in range(240):
        mid=(lo+hi)/2
        if survival(k,mid)>target: lo=mid
        else: hi=mid
    return (lo+hi)/2

if __name__=='__main__':
    start=time.monotonic()
    rows=[]
    for k in range(1,61):
        t=quantile(k)
        rows.append({'k':k,'t_k':mp.nstr(t,65),'ratio':mp.nstr(t/k,65),
                     'residual':mp.nstr(survival(k,t)-mp.exp(-1),5),
                     'derivative':mp.nstr(-mp.exp(-t)*t**(k-1)/mp.factorial(k-1),12)})
    with open('gamma_results.csv','w') as f:
        w=csv.DictWriter(f,fieldnames=rows[0]); w.writeheader(); w.writerows(rows)
    best=max(rows,key=lambda r:mp.mpf(r['ratio']))
    print(json.dumps({'first_five':rows[:5],'maximum':best,'last':rows[-1],
                      'seconds':time.monotonic()-start},indent=2))
