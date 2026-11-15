"""Render recorded Monte Carlo results, without rerunning any simulation."""
import json
import numpy as np

results=[]
exact=json.load(open('referee_numeric.json'))
for n in (1000,10000,20000):
    rows=json.load(open(f'referee_sim_{n}.json'))
    samples=np.load(f'referee_samples_{n}.npz')
    for row in rows:
        key=f"r{row['r']}" if row['r'] else f"k{row['k']}"
        row['pzero']=float(np.mean(samples[key]==0))
        results.append(row)
print('INTERIOR: sample normalized mean,var; exact finite-n normalized mean,var; KS to limit; Pzero')
for row in results:
    if row['r']: continue
    n,k=row['n'],row['k']; s=(k*(n-k)/n)**.5
    target=exact[f'{n},{k}']
    print(f"|{n}|{k}|{row['norm_mean']:.6f} ({row['norm_se_mean']:.6f})|{row['norm_var']:.6f} ({row['norm_se_var']:.6f})|{target['eh']/s:.6f}|{target['var']/s**2:.6f}|{row['ks']:.5f}|{row['pzero']:.5f}|")
print('FIXED r: sample mean,var; exact finite-n mean,var; KS to mixed-Poisson limit')
for row in results:
    if not row['r']: continue
    n,k=row['n'],row['k']; target=exact[f'{n},{k}']
    print(f"|{n}|{row['r']}|{row['mean']:.6f} ({row['se_mean']:.6f})|{row['var']:.6f} ({row['se_var']:.6f})|{target['eh']:.6f}|{target['var']:.6f}|{row['ks']:.5f}|")
print('max primary simulation |zmean|',max(abs(row['zmean']) for row in results))
print('max primary simulation |zvar|',max(abs(row['zvar']) for row in results))
print('largest primary omission bound',max(row['omission_bound'] for row in results))
print('largest normalized quadrature order difference',max(row['order_difference'] for row in exact.values()))
