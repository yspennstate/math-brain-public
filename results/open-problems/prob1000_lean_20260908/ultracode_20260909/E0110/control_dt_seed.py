"""Control for sim_grbm.py: halve dt and change the seed for d=32 in both families; the peak time of Delta_d
and the coupling-mass half-time must move by less than the path-to-path noise, or the numbers are discretisation artefacts."""
import numpy as np, json, sim_grbm as S
out=[]
for fam in ['F','T']:
    for (dtf, seed) in [(1.0, 1), (0.5, 2)]:
        S.rng = np.random.default_rng(seed)
        m = np.cumsum(np.ones(32)) if fam=='F' else 1+0.02*np.arange(32)
        dt0 = min(0.5/m.max(),0.01)*0.5
        r,_ = S.run(fam, 32, dt=dt0*dtf, npaths=300)
        r['dt_factor']=dtf; r['seed']=seed
        print(json.dumps(r)); out.append(r)
json.dump(out, open('control_dt_seed.json','w',encoding='utf-8'), indent=1)
