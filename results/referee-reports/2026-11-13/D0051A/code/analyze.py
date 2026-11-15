"""Summarize independent replicates, draw original figures, audit artifacts."""
import os
for name in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[name]='1'
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
os.environ['MPLCONFIGDIR']=str(ROOT/'data'/'.mplconfig')
os.environ['XDG_CACHE_HOME']=str(ROOT/'data'/'.cache')
import csv
import json
from collections import defaultdict
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

DATA=ROOT/'data'

def write_csv(path,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=list(rows[0]))
        writer.writeheader(); writer.writerows(rows)

def main():
    with (DATA/'path_statistics.csv').open() as f: rows=list(csv.DictReader(f))
    groups=defaultdict(list)
    keys=['N','xi','radius_pixels','sample','measure','estimator']
    for row in rows:
        assert all(np.isfinite(float(row[k])) for k in ['mean','sd','q05','q50','q95'])
        assert float(row['q05'])<=float(row['q50'])<=float(row['q95'])
        groups[tuple(row[k] for k in keys)].append(row)
    summary=[]
    for key,rs in groups.items():
        means=np.array([float(r['mean']) for r in rs])
        summary.append({**dict(zip(keys,key)), 'replicates':len(rs),
                        'mean':float(means.mean()),'replicate_SE':float(means.std(ddof=1)/np.sqrt(len(rs))),
                        'mean_q05':np.mean([float(r['q05']) for r in rs]),
                        'mean_q50':np.mean([float(r['q50']) for r in rs]),
                        'mean_q95':np.mean([float(r['q95']) for r in rs])})
    write_csv(DATA/'summary.csv',summary)
    paired=[]
    for key,rs in groups.items():
        if key[3]!='geodesic': continue
        control_key=key[:3]+('straight',)+key[4:]
        control={r['replicate']:r for r in groups[control_key]}
        diffs=np.array([float(r['mean'])-float(control[r['replicate']]['mean']) for r in rs])
        paired.append({**dict(zip(keys,key)), 'replicates':len(diffs),
                       'paired_mean_difference':float(diffs.mean()),
                       'paired_SE':float(diffs.std(ddof=1)/np.sqrt(len(diffs)))})
    write_csv(DATA/'paired_geodesic_minus_straight.csv',paired)
    # Re-derive the optimizer by a dense numerical search, separately from algebra.
    xi,Q=1/np.sqrt(6),5/np.sqrt(6)
    alpha=np.linspace(-2,2,200001)
    A=2-alpha**2/2; b=xi*(Q-alpha)
    U=np.minimum(A,b); W=np.minimum(1,A/b)
    root=xi-np.sqrt(xi**2+4-2*xi*Q)
    B=xi*(Q-xi+np.sqrt(xi**2-2*xi*Q+4))
    assert abs(alpha[np.argmax(U)]-root)<3e-5
    assert np.isclose(B,(4+np.sqrt(15))/6,atol=1e-14)
    assert np.isclose(2-root**2/2,xi*(Q-root),atol=1e-14)
    assert np.all(W>=-1e-12) and np.all(W<=1+1e-12)
    fig,axes=plt.subplots(1,2,figsize=(10,3.8))
    axes[0].plot(alpha,U,label='Euclidean upper bound')
    axes[0].plot(alpha,W,label='LQG upper bound')
    axes[0].axvline(root,color='grey',lw=.8,ls='--')
    axes[0].set(xlabel='alpha',ylabel='dimension upper bound',title='Bounds at gamma = sqrt(8/3)')
    axes[0].legend(frameon=False)
    xis=sorted({float(r['xi']) for r in summary})
    for x in xis:
        rs=sorted([r for r in summary if r['N']=='512' and float(r['xi'])==x
                   and r['sample']=='geodesic' and r['measure']=='vertices' and r['estimator']=='raw'],
                  key=lambda r:float(r['radius_pixels']))
        scales=[np.log(513/float(r['radius_pixels'])) for r in rs]
        axes[1].errorbar(scales,[r['mean'] for r in rs],yerr=[r['replicate_SE'] for r in rs],
                         marker='o',capsize=2,label=f'xi={x:.3f}')
    axes[1].axhline(0,color='grey',lw=.8)
    axes[1].set(xlabel='log(1/r), N=512',ylabel='mean h_r / log(1/r)',title='Finite-grid evidence: vertex sampling')
    axes[1].legend(frameon=False)
    fig.tight_layout(); fig.savefig(DATA/'bounds_and_evidence.svg'); fig.savefig(DATA/'bounds_and_evidence.png',dpi=140); plt.close(fig)

    # Histograms of the actual circle-average thickness estimator, not just means.
    with (DATA/'histograms.csv').open() as f: hist=list(csv.DictReader(f))
    hist_groups=defaultdict(list)
    mass_groups=defaultdict(float)
    for row in hist:
        key=tuple(row[k] for k in ['N','replicate','xi','radius_pixels','sample','measure','estimator'])
        mass_groups[key]+=float(row['mass'])
        if row['left']=='overflow':continue
        if row['N']=='512' and float(row['xi'])==xi and row['sample']=='geodesic' and row['estimator']=='raw':
            hist_groups[(row['measure'],float(row['radius_pixels']),float(row['left']))].append(float(row['mass']))
    mass_error=max(abs(v-1) for v in mass_groups.values())
    assert mass_error<1e-12
    fig,axes=plt.subplots(1,2,figsize=(10,3.6),sharey=True)
    for ax,measure in zip(axes,['vertices','lfpp_length']):
        for radius in [32,16,8,4,2]:
            bin_left=sorted({k[2] for k in hist_groups if k[:2]==(measure,radius)})
            values=[np.mean(hist_groups[(measure,radius,left)])/.1 for left in bin_left]
            ax.plot(np.array(bin_left)+.05,values,label=f'r={radius}/513')
        ax.set(xlabel='h_r / log(1/r)',title=measure.replace('_',' '))
        ax.legend(frameon=False,fontsize=8)
    axes[0].set_ylabel('density (mean over 12 fields)')
    fig.suptitle('LFPP thickness histograms, N=512, xi=1/sqrt(6)')
    fig.tight_layout();fig.savefig(DATA/'thickness_histograms.svg');fig.savefig(DATA/'thickness_histograms.png',dpi=140);plt.close(fig)
    # An original simulation image, not an image of a paper.
    sample=np.load(DATA/'field_N512_rep00.npz')
    fig,ax=plt.subplots(figsize=(5,5))
    ax.imshow(sample['h'],origin='lower',cmap='coolwarm',vmin=-6,vmax=6)
    for x in xis[1:]:
        p=sample[f'path_xi_{x:.8f}']
        ax.plot(p[:,1],p[:,0],lw=1,label=f'xi={x:.3f}')
    ax.set_title('One DGFF sample and its LFPP geodesics')
    ax.legend();fig.tight_layout();fig.savefig(DATA/'sample_geodesics.png',dpi=140);plt.close(fig)
    # npz hashes and finiteness verification for every saved field/path.
    import hashlib
    field_audit=[]
    for path in sorted(DATA.glob('field_*.npz')):
        saved=np.load(path)
        assert np.all(np.isfinite(saved['h']))
        for k in saved.files:
            if k.startswith('path_'):
                p=saved[k]
                assert np.all(np.abs(np.diff(p,axis=0)).sum(axis=1)==1)
        field_audit.append({'file':path.name,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    # Sources must remain plain text. PDF bytes / page scans never persisted.
    for path in (ROOT/'sources').iterdir():
        assert path.suffix in ('.txt','.md')
        assert not path.read_bytes().startswith(b'%PDF')
        path.read_text()
    import resource
    peak_rss=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    assert peak_rss<4_000_000_000
    audit=dict(analysis_peak_rss_bytes=peak_rss,B=B,alpha_bound=root,alpha_plus=xi+np.sqrt(xi**2+4-2*xi*Q),
               grid_argmax=float(alpha[np.argmax(U)]),histogram_mass_max_error=mass_error,
               all_statistics_finite=True,source_formats_plain_text=True,fields=field_audit,
               statistics_rows=len(rows),histogram_rows=len(hist))
    (DATA/'audit.json').write_text(json.dumps(audit,indent=2)+'\n')
    print(json.dumps({k:v for k,v in audit.items() if k!='fields'},indent=2))
    print('N=512, radius=4 pixels, raw:')
    for r in summary:
        if r['N']=='512' and r['radius_pixels']=='4.0' and r['sample']=='geodesic' and r['estimator']=='raw':
            print(r)

if __name__=='__main__':main()
