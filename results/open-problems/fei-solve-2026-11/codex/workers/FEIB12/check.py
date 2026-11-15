import json,time
from pathlib import Path
from numerics import *

def check(F,label):
    d=data(F,True);mu,polys,I,pcv=d['mu'],d['F'],d['I'],d['pc'];n=F.shape[-1].bit_length()-1;N=1<<n
    e={};e['functions']=len(F);e['n']=n
    e['endpoint0_max_error']=float(np.max(abs(d['phi'][:,0]+(mu*np.log2(np.maximum(mu,1e-300))).sum(axis=-1))))
    e['endpoint1_max_error']=float(np.max(abs(d['phi'][:,-1]-d['A'])))
    e['monotonicity_max_violation']=float(max(0,np.diff(d['phi'],axis=1).max()))
    e['gibbs_max_violation']=float(max(0,(d['phi'][:,0,None]-d['phi'][:,:-1]-I[:,None]*np.log2(1/(1-US[:-1]))).max()))
    rho=.5;tau=rho**pcv*polys[:,2]
    e['thinning_normalization_max_error']=float(abs(tau.sum(axis=-1)-1).max())
    Z,kl,C=coupling(d)
    e['kraft_max_error']=float(abs((mu*Z).sum(axis=-1)-1).max())
    # Independent conditional entropy from pair probabilities, not B+KL.
    Cdirect=np.zeros(len(F))
    for U in range(N):
        den=Z[:,U]
        for S in range(N):
            if U&S!=S:continue
            w=np.divide(mu[:,S],polys[:,-1,S],out=np.zeros(len(F)),where=polys[:,-1,S]>0)
            joint=w*mu[:,U];cp=np.divide(w,den,out=np.ones(len(F)),where=den>0)
            Cdirect-=joint*np.log2(np.maximum(cp,1e-300))
    e['conditional_entropy_max_error']=float(abs(C-Cdirect).max())
    e['B_le_conditional_max_violation']=float(max(0,(d['B']-C).max()))
    # Noise derivative identity checked by centered finite differences.
    eps=1e-5;pm=noise_polys(mu,.5-eps);pp=noise_polys(mu,.5+eps)
    finite=-(mu*np.log2(np.maximum(pp,1e-300)/np.maximum(pm,1e-300))).sum(axis=-1)/(2*eps)
    slope=np.zeros(len(F));mean=np.zeros(len(F));median_bound=np.zeros(len(F));atom_bound=np.zeros(len(F));quantile_bound=np.zeros(len(F))
    max_bad=0.;bad=None;max_corrected=0.;noisy=np.zeros(len(F));rhbound=np.zeros(len(F));max_rh=0.;rawm=np.zeros(len(F))
    for S in range(N):
        sup=np.array([U for U in range(N) if U&S==S]);lev=pcv[sup]-pcv[S];up=polys[:,-1,S]
        q=np.divide(mu[:,sup],up[:,None],out=np.zeros((len(F),len(sup))),where=up[:,None]>0)
        qm=np.stack([q[:,lev==j].sum(axis=-1) for j in range(n-pcv[S]+1)],axis=-1)
        cdf=np.cumsum(qm,axis=-1);med=np.argmax(cdf>=.5-1e-14,axis=-1)
        Fnorm=np.divide(polys[:,2,S],up,out=np.ones(len(F)),where=up>0)
        active=mu[:,S]>0
        gap=np.where(active,2.**(-med)-Fnorm,0);ix=gap.argmax()
        if gap[ix]>max_bad:max_bad=float(gap[ix]);bad=dict(tt=tt_hex(F[ix]),S=S,median=int(med[ix]),F_over_up=float(Fnorm[ix]),q=qm[ix].tolist())
        max_corrected=max(max_corrected,float(np.where(active,.5*2.**(-med)-Fnorm,0).max()))
        m=(q*lev).sum(axis=-1);mean+=mu[:,S]*m;rawm+=mu[:,S]*med
        median_bound+=mu[:,S]*(1+med)
        w=q[:,lev==0].sum(axis=-1);non=1-w
        cm=np.divide(m,non,out=np.zeros(len(F)),where=non>1e-14)
        low=w+non*2.**(-cm);atom_bound-=mu[:,S]*np.log2(np.maximum(low,1e-300))
        choices=np.where(cdf>0,-np.log2(np.maximum(cdf,1e-300))+np.arange(qm.shape[-1]),np.inf)
        quantile_bound+=mu[:,S]*np.where(active,choices.min(axis=-1),0)
        numerator=(mu[:,sup]*lev*.5**lev).sum(axis=-1)
        slope-=mu[:,S]*np.divide(numerator,polys[:,2,S],out=np.zeros(len(F)),where=polys[:,2,S]>0)/(.5*np.log(2))
        # Direct derivative energy and absolute-value noisy ratio.
        g=derivative(F,S);hg=fwht(g);ha=fwht(abs(g));c=pc(n-int(pcv[S]))
        direct=(hg**2*.5**c).sum(axis=-1)
        e['direct_up_max_error']=max(e.get('direct_up_max_error',0),float(abs((g*g).mean(axis=-1)-polys[:,-1,S]).max()))
        e['direct_mu_max_error']=max(e.get('direct_mu_max_error',0),float(abs(g.mean(axis=-1)**2-mu[:,S]).max()))
        fab=(ha**2*.5**c).sum(axis=-1)
        e['derivative_noise_max_error']=max(e.get('derivative_noise_max_error',0),float(abs(direct-polys[:,2,S]).max()))
        ratio=np.divide(fab,direct,out=np.ones(len(F)),where=direct>0)
        noisy+=mu[:,S]*np.log2(np.maximum(ratio,1e-300))
        # Reverse HC at u=1/2: ||g||_(1/2)^2=(E sqrt |g|)^4.
        rhlow=np.sqrt(abs(g)).mean(axis=-1)**4
        max_rh=max(max_rh,float((rhlow-fab).max()))
        rhbound+=mu[:,S]*np.log2(np.maximum(up,1e-300)/np.maximum(rhlow,1e-300))
    e['slope_finite_difference_max_error']=float(abs(slope-finite).max())
    cost=d['phi'][:,2]-d['A'];e['median_claim_max_failure']=max_bad;e['median_counterexample']=bad
    e['corrected_median_max_violation']=max_corrected
    e['atom_mean_max_violation']=float(max(0,(cost-atom_bound).max()))
    e['quantile_max_violation']=float(max(0,(cost-quantile_bound).max()))
    e['Jensen_max_violation']=float(max(0,(cost-mean).max()))
    e['atom_no_worse_Jensen_max_violation']=float(max(0,(atom_bound-mean).max()))
    e['reverse_HC_max_violation']=max_rh
    ok=I>1e-12
    for name,val in [('noisy_cancellation',noisy),('conditional_entropy',C),('mean_Jensen',mean),('atom_bound',atom_bound),('quantile_bound',quantile_bound)]:
        z=np.where(ok,val/np.maximum(I,1e-300),-np.inf);ix=z.argmax();e[name+'_sup_over_I']={'value':float(z[ix]),'tt':tt_hex(F[ix])}
    checks=[e[k] for k in e if ('max_error' in k or 'max_violation' in k) and k!='slope_finite_difference_max_error']
    assert all(np.isfinite(x) for x in checks), (label,e)
    assert max(checks)<1e-9,(label,e)
    assert e['slope_finite_difference_max_error']<1e-7
    Path('check_'+label+'.json').write_text(json.dumps(e,indent=2));print(label,json.dumps(e),flush=True)
    return e
if __name__=='__main__':
    t=time.time();check(from_tt(np.arange(65536),4),'all4');check(sample(6,12000,20261110),'sample6')
    print('elapsed_seconds',time.time()-t)
