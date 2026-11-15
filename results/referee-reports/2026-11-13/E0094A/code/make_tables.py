"""Insert tables in REPORT.md and draw standalone TV curves."""
import os
os.environ['MPLCONFIGDIR']=str(__import__('pathlib').Path('data/mplconfig').resolve())
os.environ['XDG_CACHE_HOME']=str(__import__('pathlib').Path('data/cache').resolve())
for k in ['OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS','MKL_NUM_THREADS']:
    os.environ[k]='1'
import csv
import json
from pathlib import Path
import re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def section(text,name,body):
    start=f'<!-- {name}_TABLE -->'
    end=f'<!-- END_{name}_TABLE -->'
    if end in text:
        return re.sub(re.escape(start)+'.*?'+re.escape(end),
                      lambda _:start+'\n\n'+body+'\n\n'+end,text,flags=re.S)
    return text.replace(start,start+'\n\n'+body+'\n\n'+end)


def main():
    text=Path('REPORT.md').read_text()
    curves={}
    fig,axes=plt.subplots(2,4,figsize=(13,6.8))
    table=['| n | base t(0.25) | added t(0.25) | ratio | base t(0.01) | added t(0.01) |',
           '|---:|---:|---:|---:|---:|---:|']
    summary=[]
    for n,ax in zip(range(5,12),axes.flat):
        times={}
        for model,color,label in [('base','#8e443d','cycle + transposition'),
                                  ('double','#245f8d','+ doubling')]:
            rows=list(csv.DictReader(open(f'data/walk_n{n}_{model}.csv')))
            times[model]={e:next((int(r['t']) for r in rows if float(r['tv'])<=e),None)
                          for e in [.25,.01]}
            ax.plot([int(r['t']) for r in rows],[float(r['tv']) for r in rows],color=color,label=label)
        b,d=times['base'],times['double']
        assert all(v is not None for v in [b[.25],b[.01],d[.25],d[.01]])
        table.append(f'| {n} | {b[.25]} | {d[.25]} | {b[.25]/d[.25]:.3f} | {b[.01]} | {d[.01]} |')
        summary.append(dict(n=n,base=b,added=d))
        ax.axhline(.25,color='gray',linewidth=.7,linestyle=':')
        ax.set_title(f'n = {n}'+(' (even extension)' if n%2==0 else ''))
        ax.set_xlabel('steps');ax.set_ylabel('total variation');ax.set_ylim(0,1)
        ax.grid(alpha=.16)
    axes.flat[-1].axis('off')
    handles,labels=axes.flat[0].get_legend_handles_labels()
    axes.flat[-1].legend(handles,labels,loc='center',frameon=False)
    fig.suptitle('Full-state total-variation curves; half-lazy walks on S_n')
    fig.tight_layout()
    fig.savefig('data/tv_curves.pdf');fig.savefig('data/tv_curves.png',dpi=170)
    text=section(text,'WALK','\n'.join(table))
    rows=json.loads(Path('data/cycle_matchings.json').read_text())
    table=['| n | admissible matchings | best matching gap | antipodal matching gap |',
           '|---:|---:|---:|---:|']
    table += [f"| {r['n']} | {r['matchings']} | {r['best_gap']:.9f} | {r['antipodal_gap']:.9f} |" for r in rows]
    text=section(text,'CYCLE','\n'.join(table))
    rows=json.loads(Path('data/regular_counts.json').read_text())
    table=['| n | d : number of connected graphs | total | simple-Fiedler failures |',
           '|---:|---|---:|---:|']
    for n in sorted(set(r['n'] for r in rows)):
        rs=[r for r in rows if r['n']==n]
        table.append(f"| {n} | "+', '.join(f"{r['d']} : {r['graphs']}" for r in rs)+
                     f" | {sum(r['graphs'] for r in rs)} | {sum(r['simple_fiedler_failures'] for r in rs)} |")
    text=section(text,'REGULAR','\n'.join(table))
    Path('REPORT.md').write_text(text)
    Path('data/walk_thresholds.json').write_text(json.dumps(summary,indent=2)+'\n')


if __name__=='__main__':main()
