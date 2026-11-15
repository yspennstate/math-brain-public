"""Independent marked-cycle diagnostic; finite job, no theorem inferred."""
import random, math, json, pathlib, time
from fractions import Fraction as F
from statistics import mean, stdev

root = pathlib.Path(__file__).resolve().parent
rng = random.Random(39120261011)
lam = 4/9
rho = F(4,5)
# B=1 with probability .9, B=9 with probability .1, m=1.8.
# H(B=9)=.5 and conditional residual is Uniform(0,9).
pi = sum((1-rho)*rho**n * sum(F(math.comb(n,k), 2**n)*
     (1-F(5,9)**k/F(math.factorial(k))) for k in range(1,n+1))
     for n in range(1,7))
expected_reward = F(1,2)*pi  # r*p_I = 5*.1

def shares(n, rule):
    a = [0.0]*n
    if rule == 'PS': return [1/n]*n
    if rule == 'middle': a[(n-1)//2] = 1
    elif rule == 'alternating': a[0 if n%2 else n-1] = 1
    elif rule == 'ends':
        a[0] += .5
        a[-1] += .5
    return a

def new_arrival(res, marks, rule):
    b = 9.0 if rng.random() < .1 else 1.0
    s = shares(len(res)+1,rule)
    u, acc, pos = rng.random(), 0.0, len(res)
    for i, v in enumerate(s):
        acc += v
        if u < acc:
            pos = i
            break
    res.insert(pos,b)
    marks.insert(pos,b)
    return b

def cycle(rule):
    res, marks = [], []
    idle = rng.expovariate(lam)
    total = idle
    reward = 0
    # Empty prearrival state fails the predicate.
    new_arrival(res,marks,rule)
    next_arrival = rng.expovariate(lam)
    while res:
        s = shares(len(res),rule)
        depart = min(x/v for x,v in zip(res,s) if v>0)
        dt = min(next_arrival, depart)
        total += dt
        res = [max(0.0,x-v*dt) for x,v in zip(res,s)]
        next_arrival -= dt
        if depart <= dt + 1e-11:
            keep = [(x,b) for x,b in zip(res,marks) if x>1e-10]
            res = [x for x,b in keep]
            marks = [b for x,b in keep]
        else:
            predicate = len(res)<=6 and sum(x for x,b in zip(res,marks) if b==9)>=5
            b = new_arrival(res,marks,rule)
            reward += int(predicate and b==9)
            next_arrival = rng.expovariate(lam)
    return reward,total

t0 = time.monotonic()
out = []
for rule in ['PS','middle','alternating','ends']:
    rows = [cycle(rule) for _ in range(8000)]
    rewards = [x[0] for x in rows]
    se = stdev(rewards)/math.sqrt(len(rows))
    obs = mean(rewards)
    out.append(dict(gamma=rule,cycles=len(rows),mean_reward=obs,
        standard_error=se,z=(obs-float(expected_reward))/se,
        mean_cycle_length=mean(x[1] for x in rows)))
record = dict(date='2026-10-11',seed=39120261011,
    model='B=1(.9),9(.1); lambda=4/9; rho=.8; original-size class {9}',
    predicate='prearrival Q<=6 and original-class residual workload >=5',
    exact_stationary_probability=str(pi),
    exact_expected_marked_reward=str(expected_reward),
    expected_marked_reward=float(expected_reward),
    expected_cycle_length=11.25,
    elapsed_seconds=time.monotonic()-t0,results=out,
    caveat='Numerical diagnostic of marked stationary law and cycle compensation; not a proof.')
(root/'marked_cycle_checks.json').write_text(json.dumps(record,indent=2),encoding='utf-8')
print(json.dumps(record,indent=2))
