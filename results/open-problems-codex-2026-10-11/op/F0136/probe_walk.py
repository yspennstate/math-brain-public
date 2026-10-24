"""Bounded finite-time experiment; never a certificate of zero/positive speed."""
from pathlib import Path
import random, math, json, time, statistics

root = Path(__file__).resolve().parent
alpha = (0.5, 0.1, 0.2, 0.1)  # (+e1,+e2,-e1,-e2)
checkpoints = (2000, 10000, 20000)
start = time.monotonic()
paths = []
for trial in range(20):
    rng = random.Random(136000 + trial)
    environment = {}
    x = y = 0
    observed = {}
    for n in range(1, checkpoints[-1]+1):
        site = (x,y)
        cdf = environment.get(site)
        if cdf is None:
            w = [rng.gammavariate(a, 1.0) for a in alpha]
            total = sum(w)
            cdf = (w[0]/total, (w[0]+w[1])/total,
                   (w[0]+w[1]+w[2])/total)
            environment[site] = cdf
        u = rng.random()
        if u < cdf[0]: x += 1
        elif u < cdf[1]: y += 1
        elif u < cdf[2]: x -= 1
        else: y -= 1
        if n in checkpoints:
            observed[str(n)] = dict(x=x, y=y, speed=x/n)
    paths.append(dict(seed=136000+trial, observed=observed,
                      visited_sites=len(environment)))

summary = {}
for n in checkpoints:
    values = [p['observed'][str(n)]['x'] for p in paths]
    summary[str(n)] = dict(mean_x=statistics.mean(values),
                          median_x=statistics.median(values),
                          mean_speed=statistics.mean(values)/n,
                          minimum_x=min(values), maximum_x=max(values))
mean_start = summary[str(checkpoints[0])]['mean_x']
mean_end = summary[str(checkpoints[-1])]['mean_x']
exponent = (math.log(mean_end/mean_start)/math.log(checkpoints[-1]/checkpoints[0])
            if mean_start > 0 and mean_end > 0 else None)
result = dict(alpha=alpha, mean_drift_parameters=(0.3,0), kappa=1.1,
              trials=len(paths), steps_per_trial=checkpoints[-1],
              checkpoints=checkpoints, summary=summary,
              effective_mean_displacement_exponent=exponent,
              paths=paths, elapsed_seconds=time.monotonic()-start,
              implementation='Lazy iid quenched Dirichlet rows from independent gamma variates; rows retained on revisits. Each trial has a new environment.',
              limitation='20 finite paths cannot distinguish zero speed from very slow positive speed; no asymptotic claim is made.')
(root/'walk_probe.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='paths'}, indent=2))
