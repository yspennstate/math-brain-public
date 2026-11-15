"""Summarize exact counts; export a standalone scientific line plot."""
import csv
import json
import os
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / 'data'
os.environ['MPLCONFIGDIR'] = str(DATA / '.mplconfig')
os.environ['XDG_CACHE_HOME'] = str(DATA / '.cache')
os.environ.setdefault('OMP_NUM_THREADS','1')
os.environ.setdefault('OPENBLAS_NUM_THREADS','1')
os.environ.setdefault('VECLIB_MAXIMUM_THREADS','1')

rows = list(csv.DictReader((DATA/'counts.csv').open()))
meta = list(csv.DictReader((DATA/'samples.csv').open()))
summary = []
for p, last in [(.6,28),(.75,24),(.9,21)]:
    for n in sorted({5,10,15,20,last}):
        rs = [r for r in rows if round(float(r['p']),2)==p and int(r['n'])==n]
        vals = [float(r['nth_root']) for r in rs]
        summary.append({'p':p,'n':n,'roots':len(vals),'min':min(vals),
                        'median':statistics.median(vals),'max':max(vals)})
with (DATA/'summary.csv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=summary[0].keys());w.writeheader();w.writerows(summary)
within=[]
for p,last in [(.6,28),(.75,24),(.9,21)]:
    for sample in range(3):
        rs=[r for r in rows if round(float(r['p']),2)==p and int(r['sample'])==sample and int(r['n'])==last]
        vals=[float(r['nth_root']) for r in rs]
        within.append({'p':p,'sample':sample,'n':last,'range':max(vals)-min(vals),
                       'max_count_over_min_count':max(int(r['count']) for r in rs)/min(int(r['count']) for r in rs)})
runtime=sum(float(r['seconds']) for r in meta)
(DATA/'summary.json').write_text(json.dumps({'rates':summary,'within_sample':within,
  'total_dfs_wall_seconds':runtime,'enumeration_peak_rss_bytes':3801088,
  'evidence_only':True},indent=2)+'\n')
for s in summary:
    print(f"p={s['p']} n={s['n']} min/median/max={s['min']:.6f}/{s['median']:.6f}/{s['max']:.6f}")
print(f'Total DFS wall time {runtime:.6f} seconds')

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig,axes=plt.subplots(1,3,figsize=(12,3.6),sharex=False)
colors=['#2166ac','#b2182b','#4d9221']
for ax,(p,last) in zip(axes,[(.6,28),(.75,24),(.9,21)]):
    for sample in range(3):
        for root in range(3):
            rs=[r for r in rows if round(float(r['p']),2)==p and int(r['sample'])==sample and int(r['root'])==root and int(r['n'])>=2]
            ax.plot([int(r['n']) for r in rs],[float(r['nth_root']) for r in rs],
                    color=colors[sample],linestyle=['-','--',':'][root],linewidth=1,alpha=.8)
    ax.set(title=f'p = {p}; 3 samples × 3 roots',xlabel='Walk length n',ylabel=r'$\sigma_n(v)^{1/n}$')
    ax.grid(alpha=.2)
fig.suptitle('Exact finite-length counts; four-face cluster proxy; no convergence claim',fontsize=11)
fig.tight_layout()
fig.savefig(DATA/'growth.svg')
