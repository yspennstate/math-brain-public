import os
os.environ['MPLCONFIGDIR']=os.path.abspath('.mplconfig')
os.environ['XDG_CACHE_HOME']=os.path.abspath('.cache')
os.environ['OPENBLAS_NUM_THREADS']='1'
os.environ['OMP_NUM_THREADS']='1'
import csv,json,math,resource
print('Plot preflight: data and figure buffers < 128 MB; no N by N arrays')
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from numpy.polynomial import Polynomial
rows=list(csv.DictReader(open('finite_moments.csv')))
a=list(map(float,json.load(open('constants.json'))['moments']))
fig,axs=plt.subplots(1,2,figsize=(10,4),sharey=True)
for s,ax in zip(('S','C'),axs):
    ds={int(r['n']):r for r in rows if r['index']==s}
    ns=np.unique(np.geomspace(1000,8000,160).astype(int))
    t=1/np.log(ns)
    for k in range(2,7):
        vals=np.array([float(ds[int(n)]['m'+str(k)])/a[k] for n in ns])
        line,=ax.plot(t,vals,label=f'k={k}')
        fit=Polynomial.fit(t,vals,3)
        tt=np.linspace(0,t.min(),100)
        ax.plot(tt,fit(tt),'--',color=line.get_color(),alpha=.75,lw=1)
    ax.axhline(1,color='black',lw=.8)
    ax.plot([0],[1],'o',color='black',ms=4)
    ax.set(xlabel='1 / log n',title='Sackin' if s=='S' else 'Colless',xlim=(-.004,.148),ylim=(.12,1.09))
    ax.grid(alpha=.2)
axs[0].set_ylabel('Central moment / limiting moment')
axs[1].legend(frameon=False,ncol=2)
fig.text(.5,.01,'Solid: exact recursions, 1000 ≤ n ≤ 8000. Dashed: unforced cubic extrapolation.',ha='center',fontsize=9)
fig.tight_layout(rect=(0,.035,1,1))
fig.savefig('moment_convergence.png',dpi=180)
fig.savefig('moment_convergence.pdf')

json.dump({'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss},open('figure_audit.json','w'),indent=2)
