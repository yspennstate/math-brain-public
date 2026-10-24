"""Same trap exponent and drift in d=3, where nonzero speed is known."""
from pathlib import Path
import random, math, json, time, statistics

root = Path(__file__).resolve().parent
alpha = (0.5, 0.05, 0.05, 0.2, 0.05, 0.05)
checkpoints = (2000, 10000, 20000)
start = time.monotonic()
paths = []
for trial in range(20):
    rng = random.Random(136100+trial)
    environment = {}
    position = [0,0,0]
    observed = {}
    for n in range(1, checkpoints[-1]+1):
        site = tuple(position)
        cdf = environment.get(site)
        if cdf is None:
            weights = [rng.gammavariate(a, 1.0) for a in alpha]
            total = sum(weights)
            running = 0.0
            cdf = []
            for w in weights[:-1]:
                running += w
                cdf.append(running/total)
            environment[site] = cdf
        u = rng.random()
        direction = 0
        while direction < 5 and u >= cdf[direction]:
            direction += 1
        axis = direction if direction < 3 else direction-3
        position[axis] += 1 if direction < 3 else -1
        if n in checkpoints:
            assert sum(abs(z) for z in position) <= n
            assert sum(position) % 2 == n % 2
            observed[str(n)] = dict(position=position[:], x=position[0],
                                    speed=position[0]/n)
    paths.append(dict(seed=136100+trial, observed=observed,
                      visited_sites=len(environment)))

summary = {}
for n in checkpoints:
    xs = [p['observed'][str(n)]['x'] for p in paths]
    summary[str(n)] = dict(mean_x=statistics.mean(xs),
                          median_x=statistics.median(xs),
                          mean_speed=statistics.mean(xs)/n,
                          minimum_x=min(xs), maximum_x=max(xs))
a = summary[str(checkpoints[0])]['mean_x']
b = summary[str(checkpoints[-1])]['mean_x']
exponent = math.log(b/a)/math.log(checkpoints[-1]/checkpoints[0]) if a>0 and b>0 else None
result = dict(alpha=alpha, dimension=3, drift_parameters=(0.3,0,0), kappa=1.1,
              rigorous_control='Sabot-Tournier overview Theorem 5(i): d>=3, nonzero drift and kappa>1 imply nonzero limiting velocity.',
              trials=len(paths), steps_per_trial=checkpoints[-1],
              summary=summary, effective_mean_displacement_exponent=exponent,
              elapsed_seconds=time.monotonic()-start, paths=paths,
              implementation='Lazy iid Dirichlet rows retained on revisits; directions +e1,+e2,+e3,-e1,-e2,-e3.',
              limitation='Finite-time observations of a rigorously ballistic model; not a theorem or comparison principle for dimension two.')
(root/'ballistic_control_probe.json').write_text(json.dumps(result, indent=2), encoding='utf-8')
print(json.dumps({k:v for k,v in result.items() if k!='paths'}, indent=2))
