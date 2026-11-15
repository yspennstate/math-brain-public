"""Exploratory follow-up; first fits and all original data remain unchanged."""
from analyze import *
import resource
results={}
t,values=load(ROOT/'data'/'renewal_q025.csv')
results['renewal_q025_early']=fit(t,values['density'],.25,.25,273101,interval=(.25,1.5))
results['renewal_q025_early']['selection']='Exploratory early window after the original t>=8 window had no resolved signal.'
t,values=load(ROOT/'data'/'hmm_q025_long.csv')
assert values['density'].shape==(500,38)
results['hmm_q025_long']=fit(t,values['density'],.25,.25,273102,interval=(75,600))
results['hmm_q025_long']['selection']='Exploratory later window after observing nonmonotonic early relaxation.'
summary=[]
for observable,eq in [('density',.25),('pair',.0625),('origin',.25),('origin_pair',.0625)]:
    mean=values[observable].mean(0);se=values[observable].std(0,ddof=1)/np.sqrt(len(values[observable]))
    summary.extend([dict(time=float(tt),observable=observable,mean=float(m),equilibrium=eq,
                         difference=float(m-eq),se=float(s)) for tt,m,s in zip(t,mean,se)])
with (ROOT/'data'/'long_summary.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
fig,axes=plt.subplots(1,2,figsize=(10,4))
m=values['density'].mean(0);se=values['density'].std(0,ddof=1)/np.sqrt(500)
axes[0].errorbar(t,m-.25,yerr=1.96*se,fmt='o-',ms=3);axes[0].axhline(0,c='black',lw=.7)
axes[0].set(xlabel='Time',ylabel='Mean infection indicator minus 0.25',title='Hidden Markov law: initial movement away')
mask=(t>=75)&(abs(m-.25)>4*se)
axes[1].errorbar(t[mask],abs(m[mask]-.25),yerr=1.96*se[mask],fmt='o',ms=3)
f=results['hmm_q025_long'];tt=np.array(f.get('times_used',[]))
if f['status']=='fit':axes[1].plot(tt,f['exp_amplitude']*np.exp(-f['exp_rate']*tt),'--',label='Exponential fit')
axes[1].set(xlabel='Time',ylabel='Absolute deviation',title='Exploratory fit, 75 to 600');axes[1].set_yscale('log');axes[1].legend()
fig.tight_layout();fig.savefig(ROOT/'data'/'long_decay.png',dpi=160);plt.close(fig)
# Independent boundary-cone bound for the long interval.
d=3968;u=600
lp=d*math.log(2*u)-math.lgamma(d+1)-math.log1p(-(2*u)/(d+1))
results['long_boundary_union_bound_log10']=math.log10(256)+lp/math.log(10)
results['analysis_peak_rss_bytes_macos']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
(ROOT/'data'/'extra_fits.json').write_text(json.dumps(results,indent=2))
print(json.dumps(results,indent=2))
