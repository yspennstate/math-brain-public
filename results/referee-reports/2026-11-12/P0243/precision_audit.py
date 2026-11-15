"""Independent high-precision matrix-exponential, hitting-time, and limit audit."""
import csv, json, signal, time
import mpmath as mp
from gamma_audit import quantile
signal.alarm(240)
mp.mp.dps=85
START=time.monotonic()
TARGET=mp.exp(-1)

def bd(k,eps):
    n=k+1
    q=mp.matrix(n)
    for i in range(n):
        if i: q[i,i-1]=1
        if i<k: q[i,i+1]=eps
        q[i,i]=-sum(q[i,j] for j in range(n) if j!=i)
    pi=[eps**i for i in range(n)]
    pi=[p/sum(pi) for p in pi]
    return q,pi

def row_distance(p):
    n=p.rows
    vals=[(sum(abs(p[i,h]-p[j,h]) for h in range(n))/2,i,j)
          for i in range(n) for j in range(i+1,n)]
    return max(vals)

class Spectrum:
    def __init__(self,k,eps):
        self.k=k; self.n=k+1; self.q,self.pi=bd(k,eps)
        n=self.n
        s=mp.matrix(n)
        for i in range(n):
            s[i,i]=self.q[i,i]
            if i+1<n: s[i,i+1]=s[i+1,i]=mp.sqrt(eps)
        vals,vec=mp.eigsy(s)
        self.vals=list(vals)[:-1]
        self.coef=[mp.matrix(n) for _ in range(n-1)]
        for m in range(n-1):
            for i in range(n):
                for j in range(n):
                    self.coef[m][i,j]=vec[i,m]*vec[j,m]*mp.sqrt(self.pi[j]/self.pi[i])
        self.tau0=sum(-1/v for v in self.vals)
    def p(self,t):
        p=mp.matrix([self.pi for _ in range(self.n)])
        for v,c in zip(self.vals,self.coef):
            e=mp.exp(v*t)
            for i in range(self.n):
                for j in range(self.n): p[i,j]+=c[i,j]*e
        return p
    def dbar(self,t): return row_distance(self.p(t))[0]
    def tau1(self):
        lo=mp.mpf(0); hi=mp.mpf(2*self.k+10)
        for _ in range(195):
            mid=(lo+hi)/2
            if self.dbar(mid)>TARGET: lo=mid
            else: hi=mid
        return (lo+hi)/2
    def hitting_tau0(self):
        h=mp.matrix(self.n)
        for j in range(self.n):
            keep=[i for i in range(self.n) if i!=j]
            a=mp.matrix([[-self.q[i,l] for l in keep] for i in keep])
            sol=mp.lu_solve(a,mp.matrix([1]*len(keep)))
            for pos,i in enumerate(keep): h[i,j]=sol[pos]
        rows=[sum(self.pi[j]*h[i,j] for j in range(self.n)) for i in range(self.n)]
        return rows[0],max(abs(v-self.tau0) for v in rows)

def fmt(x): return mp.nstr(x,55)

def main():
    three=[]
    for eps_text in ['0.01','0.001']:
        eps=mp.mpf(eps_text); s=Spectrum(2,eps); root=s.tau1()
        hit,hiterr=s.hitting_tau0()
        exact=2*(1+eps)/(1+eps+eps**2)
        max_expm_error=mp.mpf(0); min_grid_margin=mp.inf
        min_bound_slack=mp.inf; min_descent_slack=mp.inf
        min_d=mp.inf
        path='grid_eps_'+eps_text.replace('.','p')+'.csv'
        with open(path,'w') as f:
            w=csv.writer(f); w.writerow(['t','dbar','max_pair_i','max_pair_j','p00','p20','lower_event_bound'])
            for step in range(3001):
                t=mp.mpf(step)/1000; p=s.p(t); d,i,j=row_distance(p)
                lower=mp.exp(-eps*t)-1+mp.exp(-(1+eps)*t)*(1+(1+eps)*t)
                w.writerow([fmt(t),fmt(d),i,j,fmt(p[0,0]),fmt(p[2,0]),fmt(lower)])
                if step<=2000:
                    min_d=min(min_d,d); min_grid_margin=min(min_grid_margin,d-TARGET)
                    min_bound_slack=min(min_bound_slack,d-lower)
                    descend=1-mp.exp(-(1+eps)*t)*(1+(1+eps)*t)
                    min_descent_slack=min(min_descent_slack,descend-p[2,0])
                if step%50==0:
                    direct=mp.expm(t*s.q)
                    max_expm_error=max(max_expm_error,max(abs(p[a,b]-direct[a,b]) for a in range(3) for b in range(3)))
        three.append({'eps':eps_text,'tau0':fmt(exact),'tau0_spectral':fmt(s.tau0),'tau0_hitting':fmt(hit),
            'tau0_max_hitting_error':fmt(hiterr),'tau1':fmt(root),'ratio':fmt(root/exact),
            'dbar_2':fmt(s.dbar(mp.mpf(2))),'min_dbar_grid_0_2':fmt(min_d),
            'min_margin_grid_0_2':fmt(min_grid_margin),'max_spectral_expm_error':fmt(max_expm_error),
            'min_dbar_minus_lower':fmt(min_bound_slack),'min_descent_slack':fmt(min_descent_slack),
            'root_residual':fmt(s.dbar(root)-TARGET),'grid_file':path})
    limits=[]
    for k in [2,3,4,6]:
        tk=quantile(k)
        for eps_text in ['0.001','0.00001']:
            s=Spectrum(k,mp.mpf(eps_text)); root=s.tau1(); hit,err=s.hitting_tau0()
            direct=mp.expm(root*s.q)
            derr=abs(row_distance(direct)[0]-TARGET)
            limits.append({'k':k,'eps':eps_text,'tau0':fmt(s.tau0),'tau1':fmt(root),
                'ratio':fmt(root/s.tau0),'t_k':fmt(tk),'tau0_minus_k':fmt(s.tau0-k),
                'tau1_minus_tk':fmt(root-tk),'hitting_max_error':fmt(err),'direct_expm_root_error':fmt(derr)})
    # Independent checks of the absorbed limiting semigroup, including the maximizing pair.
    absorbed=[]
    for k in [2,3,4,6]:
        q,_=bd(k,mp.mpf(0))
        for t in [mp.mpf('0.2'),mp.mpf(k),quantile(k)]:
            d,i,j=row_distance(mp.expm(t*q))
            gamma=mp.exp(-t)*sum(t**h/mp.factorial(h) for h in range(k))
            absorbed.append({'k':k,'t':fmt(t),'error':fmt(d-gamma),'pair':[i,j]})
    extra=Spectrum(2,mp.mpf('.05'))
    results={'three_state':three,'limits':limits,'absorbed':absorbed,
             'eps_0p05_ratio':fmt(extra.tau1()/extra.tau0),'dps':mp.mp.dps,
             'seconds':time.monotonic()-START}
    with open('precision_results.json','w') as f: json.dump(results,f,indent=2)
    print(json.dumps(results,indent=2))

if __name__=='__main__': main()
