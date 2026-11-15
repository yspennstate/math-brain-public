"""Produce tabular comparisons and an exportable scientific figure."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','MKL_NUM_THREADS','VECLIB_MAXIMUM_THREADS','NUMEXPR_NUM_THREADS'):os.environ[name]='1'
import pathlib,json,csv,math
from fractions import Fraction
root=pathlib.Path(__file__).resolve().parents[1]
short=[json.loads(x) for x in (root/'data'/'ring_results.jsonl').read_text().splitlines()]
long=[json.loads(x) for x in (root/'data'/'ring_long.jsonl').read_text().splitlines()]
M2=next(x['current'] for x in short if x['p_slow']==0 and x['K']==2 and x['rho']==1)
mu=Fraction(1,1)/Fraction(1,2)-(Fraction(1,10)/Fraction(1,2)+Fraction(9,10))
assert mu==Fraction(9,10)
predictions={K:{'M':M,'J':M/2,'halfwidth':float(mu)*M/2,'interval':[K/2-float(mu)*M/2,K/2+float(mu)*M/2]} for K,M in [(1,.25),(2,M2)]}
assert abs(predictions[2]['halfwidth']-.45*M2)<1e-14
summary={'mu':str(mu),'M2_estimate':M2,'predictions':predictions,'rows_short':len(short),'rows_long':len(long),'max_simulator_rss_bytes':max(x['maxrss_native'] for x in short+long),'all_nice_10':all(x['nice']==10 for x in short+long)}
(root/'data'/'summary.json').write_text(json.dumps(summary,indent=2))
with (root/'data'/'currents.csv').open('w') as f:
 keys=['n','K','rho','p_slow','env_seed','initial','burn','measure','current','block_sd','bond_min','bond_max','longest_slow_run','nice','maxrss_native']
 w=csv.DictWriter(f,keys);w.writeheader();w.writerows({k:x[k] for k in keys} for x in short+long)
lines=[]
lines.append(f"For this law, E[1/alpha]=1.1 and mu=0.9 (also checked with exact fractions). The homogeneous K=2 run estimates M_2={M2:.9f}; it is a finite-size, finite-time estimate. Its eight-block standard deviation is {next(x['block_sd'] for x in short if x['p_slow']==0 and x['K']==2 and x['rho']==1):.6f}, not a confidence interval.")
lines.append('')
lines.append('| K | Infinite-volume level r M_K | Guaranteed half-width mu r M_K | Guaranteed interval |')
lines.append('|---|---:|---:|---|')
for K,p in predictions.items():lines.append(f"| {K} | {p['J']:.9f} | {p['halfwidth']:.9f} | [{p['interval'][0]:.9f}, {p['interval'][1]:.9f}] |")
lines.append('')
lines.append('The K=2 entries use the estimated M_2; only the K=1 level and interval are exact numerical values. Long runs on the same sampled environment give:')
lines.append('')
lines.append('| K | Density | Initial state | Current | Block SD | Across-bond current range |')
lines.append('|---|---:|---|---:|---:|---|')
for x in long:lines.append(f"| {x['K']} | {x['rho']:.4f} | {x['initial']} | {x['current']:.9f} | {x['block_sd']:.6f} | {x['bond_min']:.6f}–{x['bond_max']:.6f} |")
lines.append('')
for K in (1,2):
 random=[x for x in long if x['K']==K and x['initial']=='random'];center=next(x for x in random if x['rho']==K/2)
 lines.append(f"For K={K}, the long random-state currents span {min(x['current'] for x in random):.9f}–{max(x['current'] for x in random):.9f}. The center exceeds the proposed thermodynamic level by {100*(center['current']/predictions[K]['J']-1):.1f}%. The short random-state center was {next(x['current'] for x in short if x['K']==K and x['p_slow'] and x['env_seed']==20261113 and x['initial']=='random' and x['rho']==K/2):.9f}.")
lines.append('')
lines.append('Block standard deviations describe temporal variation, not independent-sample errors or disorder uncertainty. Across-bond agreement and packed/random agreement are equilibration diagnostics, not proofs of stationarity. The sampled longest slow run is six; the second environment has only three and gives substantially higher short-run center currents. Finite-size capacity and time-to-equilibrium therefore matter separately. These experiments exhibit a nearly flat central finite-ring curve but do not verify the infinite-volume plateau height, its exact half-width, or the true endpoints. Being above r M_K at finite n is compatible with (R2), whose rare-strip limit takes place on the infinite lattice. A wider observed flat interval would also be compatible, because the theorem provides a guaranteed subinterval.')
(root/'data'/'numerical_results.md').write_text('\n'.join(lines)+'\n')
os.environ['MPLCONFIGDIR']=str(root/'data'/'.mplconfig')
os.environ['XDG_CACHE_HOME']=str(root/'data'/'.cache')
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,2,figsize=(12,4.5),constrained_layout=True)
for ax,K in zip(axes,(1,2)):
 p=predictions[K]
 ax.axvspan(*p['interval'],color='#79bcaf',alpha=.25,label='guaranteed infinite-volume interval')
 ax.axhline(p['J'],color='#a13435',ls='--',label='r M_K (M_2 estimated)')
 for ps,color,label in [(0,'#666666','homogeneous, short run'),(.1,'#4b7da8','disordered, short run')]:
  a=sorted([x for x in short if x['K']==K and x['p_slow']==ps and x['env_seed']==20261113 and x['initial']=='random'],key=lambda x:x['rho'])
  ax.plot([x['rho'] for x in a],[x['current'] for x in a],'o:',color=color,label=label)
 a=sorted([x for x in long if x['K']==K and x['initial']=='random'],key=lambda x:x['rho'])
 ax.plot([x['rho'] for x in a],[x['current'] for x in a],'o-',color='#183c54',label='disordered, long run')
 packed=[x for x in long if x['K']==K and x['initial']=='packed']
 ax.scatter([x['rho'] for x in packed],[x['current'] for x in packed],marker='x',s=70,color='#d08020',label='long run, packed start',zorder=5)
 ax.set(xlabel='density (particles per site)',ylabel='accepted jumps per bond per unit time',title=f'K = {K}, n = 10,000',xlim=(0,K),ylim=(0,.48 if K==2 else .28))
 ax.grid(alpha=.2)
axes[0].legend(fontsize=7,loc='lower center')
fig.suptitle('Finite-ring currents: 10% rate 0.5, otherwise rate 1; no thermodynamic extrapolation')
fig.savefig(root/'data'/'current_density.svg');plt.close(fig)
import resource
summary['analysis_peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
summary['analysis_nice']=os.getpriority(os.PRIO_PROCESS,0)
(root/'data'/'summary.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary,indent=2))
