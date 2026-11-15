"""Summarize by environment; pairs in a common comb are a cluster."""
import csv,json,math,os,pathlib
os.environ.setdefault('MPLCONFIGDIR',str(pathlib.Path('data/.matplotlib').resolve()))
os.environ.setdefault('XDG_CACHE_HOME',str(pathlib.Path('data/.cache').resolve()))
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
rows=list(csv.DictReader(open('data/collisions.csv')))
gammas=sorted({float(r['gamma']) for r in rows})
times=sorted({int(r['time']) for r in rows})
summary=[]
for g in gammas:
 for t in times:
  selected=[r for r in rows if float(r['gamma'])==g and int(r['time'])==t]
  rec={'gamma':g,'time':t}
  for k in ['total','backbone']:
   env={}
   for r in selected:env.setdefault(int(r['environment']),[]).append(int(r[k]))
   a=np.array([np.mean(v) for v in env.values()])
   rec[k+'_mean']=float(a.mean())
   rec[k+'_environment_se']=float(a.std(ddof=1)/math.sqrt(len(a)))
   rec[k+'_pair_median']=float(np.median([int(r[k]) for r in selected]))
  summary.append(rec)
with open('data/summary.csv','w') as f:
 w=csv.DictWriter(f,fieldnames=list(summary[0]));w.writeheader();w.writerows(summary)
fig,axes=plt.subplots(1,2,figsize=(11,4.2))
for gi,g in enumerate(gammas):
 s=[r for r in summary if r['gamma']==g]
 t=np.array([r['time'] for r in s]);c=f'C{gi}'
 for ax,k in zip(axes,['total','backbone']):
  mean=np.array([r[k+'_mean'] for r in s]);se=np.array([r[k+'_environment_se'] for r in s])
  ax.plot(t,mean,'o-',ms=3,color=c,label=f'gamma={g:.5f}')
  ax.fill_between(t,np.maximum(mean-se,1e-4),mean+se,color=c,alpha=.13)
  if k=='total': guide=t.astype(float)**((1+g)/4)
  else:
   q=(5-3*g)/4
   cumulative=np.cumsum(np.arange(1,int(t[-1])+1,dtype=float)**(-q))
   guide=cumulative[t-1]
  # Amplitude aligned at the final point: a shape guide, not a fitted constant.
  ax.plot(t,guide*mean[-1]/guide[-1],'--',color=c,alpha=.65)
  ax.set_xscale('log',base=2);ax.set_yscale('log')
  ax.set_xlabel('steps T');ax.grid(alpha=.2)
axes[0].set_title('All collisions: mean and power-law guide')
axes[1].set_title('Backbone collisions: mean and sum guide')
axes[0].set_ylabel('collisions at times 1 through T')
axes[0].legend(fontsize=8)
fig.text(.5,.01,'32 environments × 8 pairs; shading = 1 environment-cluster SE; dashed guides aligned at final point',ha='center',fontsize=8)
fig.tight_layout(rect=(0,.04,1,1));fig.savefig('data/collision_growth.png',dpi=150)
print(json.dumps([r for r in summary if r['time']==times[-1]],indent=2))
metadata={'seed_scheme':'explicit in code/simulate.cpp','environments_per_gamma':32,'pairs_per_environment':8,'T':131072,'threads':1,'nice':10,'step_pairs':3*32*8*131072,'law':'H=floor(U^(-1/gamma)); P(H>=k)=k^(-gamma), k>=1; C=1','cap':131073,'cap_reason':'Unreachable by time T, so no path transition through time T is changed.','initial_collision_counted':False,'guides':'quenched asymptotic orders; amplitudes aligned at final means, no exact constants claimed','peak_resident_memory':'not measured; simulation uses sparse tooth maps and constant path state; raw CSV under 1 MB'}
pathlib.Path('data/metadata.json').write_text(json.dumps(metadata,indent=2)+'\n')
