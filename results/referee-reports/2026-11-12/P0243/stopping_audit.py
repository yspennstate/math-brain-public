"""Independent reversible generators, exact occupation LPs, and discrete analogues."""
import os
for name in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS']:
    os.environ[name]='1'
import csv, json, signal, time, warnings
import numpy as np
import scipy
from scipy.optimize import linprog, OptimizeWarning
signal.alarm(240)
warnings.filterwarnings('ignore',category=OptimizeWarning)
START=time.monotonic()
rng=np.random.default_rng(48112026)

# If x_j is time spent at j before stopping, Dynkin applied to indicators gives
# x Q = pi - e_i. Every solution is x=Z_i + t*pi, where Z=(Pi-Q)^(-1)-Pi.
# Because Z 1=0, sum x=t. Therefore min sum x = max_j(-Z_ij/pi_j).
# Attainability: on each arrival at j stop with probability
# pi_j/(pi_j+q_j*x_j); otherwise make an Exp(q_j) hold and a Q jump.
# Balance equations imply expected visits pi_j+q_j*x_j, stopped mass pi_j,
# occupation x_j. pi>0 makes absorption certain in this finite network.
# Equivalently v_j=q_j*x_j, v(I-R)=e_i-pi and objective sum_j v_j/q_j.
# Discrete time replaces q_j*x_j by x_j and R by P, allowing self visits.

def draw_chain(n,index):
    pi=rng.dirichlet(np.full(n,1.3))
    if index%3==0:
        c=np.zeros((n,n))
        for i in range(n):
            j=(i+1)%n
            c[i,j]=c[j,i]=np.exp(rng.uniform(-2,2))
    else:
        raw=np.exp(rng.uniform(-3,3,size=(n,n)))
        c=np.triu(raw,1); c+=c.T
    q=c/pi[:,None]
    q[np.diag_indices(n)]=-q.sum(axis=1)
    q/=np.max(-np.diag(q))
    return q,pi

def assess(q,pi,lp=False):
    n=len(pi); proj=np.tile(pi,(n,1))
    z=np.linalg.solve(proj-q,np.eye(n))-proj
    vals=np.linalg.eigvalsh(-np.sqrt(pi[:,None]/pi[None,:])*q)
    gap=vals[1]
    tau2=1/gap
    per=np.max(-z/pi[None,:],axis=1)
    opt=np.max(per); tau0=np.trace(z)
    result={'tau2':tau2,'tau_stop':opt,'tau0':tau0,'stop_gap_ratio':opt/tau2,
            'upper_ratio':opt/tau0,'lp_error':0.,'flow_error':0.,'lp_duality_error':0.,
            'eigenfunction_margin':0.,'hitting_error':0.}
    # Verify the stronger pointwise statement with normalized eigenfunction.
    _,vec=np.linalg.eigh(-np.sqrt(pi[:,None]/pi[None,:])*q)
    u=vec[:,1]/np.sqrt(pi); u/=np.max(np.abs(u))
    result['eigenfunction_margin']=float(np.min(per-tau2*np.abs(u)))
    if lp:
        values=[]
        for i in range(n):
            b=pi.copy(); b[i]-=1
            # All n balance equations, one redundant. HiGHS handles this rank defect.
            sol=linprog(np.ones(n),A_eq=q.T,b_eq=b,bounds=(0,None),method='highs',
                        options={'threads':1,'primal_feasibility_tolerance':1e-9,
                                 'dual_feasibility_tolerance':1e-9})
            if not sol.success: raise RuntimeError(sol.message)
            values.append(sol.fun)
            result['lp_error']=max(result['lp_error'],abs(sol.fun-per[i])/max(1.,abs(per[i])))
            result['flow_error']=max(result['flow_error'],float(np.max(np.abs(q.T@sol.x-b))))
            result['lp_duality_error']=max(result['lp_duality_error'],abs(sol.fun-b@sol.eqlin.marginals)/max(1.,sol.fun))
        result['lp_tau_stop']=max(values)
        # Independently solve each hitting system, then average with pi.
        hitting=np.zeros((n,n))
        for j in range(n):
            keep=np.arange(n)!=j
            hitting[keep,j]=np.linalg.solve(-q[np.ix_(keep,keep)],np.ones(n-1))
        result['hitting_error']=float(np.max(np.abs(hitting@pi-tau0))/max(1.,tau0))
        # Verify actual stopping probabilities constructed from the LP optimum.
        i=int(np.argmax(per)); x=z[i]+per[i]*pi
        x=np.maximum(x,0)
        rates=-np.diag(q)
        visit=pi+rates*x
        stop=pi/visit
        r=q/rates[:,None]; np.fill_diagonal(r,0)
        continuation=(1-stop)[:,None]*r
        counts=np.linalg.solve((np.eye(n)-continuation).T,np.eye(n)[i])
        result['constructed_stop_error']=float(np.max(np.abs(counts*stop-pi)))
        result['constructed_time_error']=float(abs(np.sum(counts*(1-stop)/rates)-per[i])/max(1.,per[i]))
    return result

def main():
    rows=[]; full=[]
    for trial in range(2500):
        n=3+trial%5
        q,pi=draw_chain(n,trial)
        lp=(trial<250)
        r=assess(q,pi,lp)
        r.update({'trial':trial,'n':n,'kind':'continuous','lp_solved':lp})
        rows.append(r)
        if lp: full.append({'trial':trial,'pi':pi.tolist(),'Q':q.tolist(),'result':r})
        # Uniformization with a random admissible speed; these are stochastic P.
        speed=rng.uniform(.35,.95)
        g=speed*q
        p=np.eye(n)+g
        d=assess(g,pi,lp)
        ev=np.linalg.eigvalsh(np.sqrt(pi[:,None]/pi[None,:])*p)
        absrel=1/(1-max(ev[-2],abs(ev[0])))
        d.update({'trial':trial,'n':n,'kind':'discrete','lp_solved':lp,
                  'absolute_relaxation':absrel,'absolute_violated':bool(absrel>d['tau_stop']*(1+1e-8))})
        rows.append(d)
    keys=list(dict.fromkeys(k for row in rows for k in row))
    with open('stopping_results.csv','w') as f:
        w=csv.DictWriter(f,fieldnames=keys);w.writeheader();w.writerows(rows)
    with open('stopping_lp_instances.json','w') as f: json.dump(full,f)
    summary={'seed':48112026,'numpy':np.__version__,'scipy':scipy.__version__,
             'chains_continuous':2500,'chains_discrete':2500,'lp_chains_each_kind':250,
             'lp_programs':sum(r['n'] for r in rows if r['lp_solved']),
             'seconds':time.monotonic()-START}
    for kind in ['continuous','discrete']:
        group=[r for r in rows if r['kind']==kind]
        summary[kind]={
            'min_stop_over_tau2':min(r['stop_gap_ratio'] for r in group),
            'max_stop_over_tau0':max(r['upper_ratio'] for r in group),
            'max_relative_lp_error':max(r['lp_error'] for r in group),
            'max_flow_residual':max(r['flow_error'] for r in group),
            'max_relative_duality_gap':max(r['lp_duality_error'] for r in group),
            'max_relative_hitting_error':max(r['hitting_error'] for r in group),
            'min_pointwise_eigen_margin':min(r['eigenfunction_margin'] for r in group),
            'inequality_violations':sum(r['stop_gap_ratio']<1-1e-8 or r['upper_ratio']>1+1e-8 for r in group),
            'max_constructed_stop_error':max(r.get('constructed_stop_error',0) for r in group),
            'max_constructed_time_error':max(r.get('constructed_time_error',0) for r in group)}
    summary['absolute_relaxation_counterexamples']=sum(r.get('absolute_violated',False) for r in rows)
    with open('stopping_summary.json','w') as f: json.dump(summary,f,indent=2,default=lambda x:x.item())
    print(json.dumps(summary,indent=2,default=lambda x:x.item()))

if __name__=='__main__':main()
