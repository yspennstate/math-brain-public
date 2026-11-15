"""Additional differential-evolution restarts, followed by local polishing."""
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):
    os.environ[key] = '1'
import time
import json
import numpy as np
from scipy.optimize import differential_evolution, minimize
from fractions import Fraction
from search5 import matrix, mix, MAPS, PAIRS, TRI
from exact_core import calculate,lump,save_json,leaf_family


def main():
    start = time.monotonic()
    best = 0
    neval = 0
    records = []
    for restart in range(8):
        rng = np.random.default_rng(47311+restart)
        pop = rng.uniform(-12,12,(120,15))
        for j,t in enumerate((3,10,100,1000)):
            w = np.array(leaf_family(3,t),float)
            z = np.log(np.maximum(w[TRI],np.max(w)*1e-13))
            z -= .5*(z.min()+z.max())
            pop[j] = np.clip(z,-16,16)
        def objective(z):
            nonlocal best,neval
            neval += 1
            if time.monotonic()-start > 110:
                raise TimeoutError
            try:
                w = matrix(z)
                rat = mix(MAPS[9].T@w@MAPS[9])/mix(w)
            except np.linalg.LinAlgError:
                return 0
            if rat > 3.00001 or not np.isfinite(rat):
                return 0
            if rat > best+1e-7:
                ew = [[Fraction(format(x,'.8g')) for x in row] for row in w]
                x = calculate(ew)
                hw,groups = lump(ew,(3,4))
                y = calculate(hw)
                er = y['tmix']/x['tmix']
                if abs(float(er)-rat) < 1e-5:
                    best = float(er)
                    rec = dict(restart=restart,weights=ew,pair=[3,4],
                               ratio=er, original=x['tmix'],quotient=y['tmix'],
                               original_pairs=x['pairs'],quotient_pairs=y['pairs'])
                    records.append(rec)
                    save_json('search5_de_best.json',rec)
                    print(f"restart={restart} evals={neval} exact_ratio={best:.12f}",flush=True)
            return -rat
        try:
            res = differential_evolution(objective,[(-16,16)]*15,init=pop,
                                         maxiter=350,polish=False,seed=rng,
                                         tol=1e-8,workers=1)
            res2 = minimize(objective,res.x,method='Nelder-Mead',
                            bounds=[(-16,16)]*15,
                            options=dict(maxfev=8000,xatol=1e-7,fatol=1e-10))
            print(f"restart {restart} complete, numerical={-res2.fun:.12f}",flush=True)
        except TimeoutError:
            print('Wall budget reached.',flush=True)
            break
    save_json('search5_de_results.json',dict(records=records,evaluations=neval,
                                           wall_seconds=time.monotonic()-start,
                                           best=best))
    print(f"FINAL best={best:.14f} evals={neval} seconds={time.monotonic()-start:.3f}")


if __name__ == '__main__':
    main()
