"""Small, single-thread deterministic diagnostics. Numerical checks are not proofs."""
import itertools
import json
import math
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
cpu_started = time.process_time()
rows = []

def save():
    receipt = {'rows': rows, 'passed': all(r.get('passed', True) for r in rows),
               'cpu_seconds': time.process_time()-cpu_started,
               'wall_seconds': time.perf_counter()-started,
               'scope': 'Deterministic finite diagnostics only; not an independent or formal proof.'}
    (ROOT/'MEASUREMENTS.json').write_text(json.dumps(receipt, indent=2), encoding='utf-8')

def gate(label):
    path = Path('~/.claude/compute/compute_state.json')
    data = json.loads(path.read_text(encoding='utf-8-sig'))
    age = time.time()-path.stat().st_mtime
    keep = ('ts','status','mode','reasons','cpu_pct','mem_avail_mb','commit_avail_mb','disk_free_gb','hung_windows')
    local = {k:data.get(k) for k in keep}
    admit = (0 <= age <= 90 and data.get('status') != 'distress'
             and float(data.get('mem_avail_mb',0)) >= 8192
             and float(data.get('commit_avail_mb',0)) >= 8192
             and float(data.get('disk_free_gb',0)) >= 5
             and not data.get('hung_windows'))
    gate_row = {'unit':label,'age_s':age,'local':local,'admitted':admit,
                'planned_budget':'One thread; <=2 CPU seconds total; no models, training, GPU or background process.'}
    with (ROOT/'COMPUTE_GATES.jsonl').open('a',encoding='utf-8') as out:
        out.write(json.dumps(gate_row)+'\n')
    if not admit:
        rows.append({'kind':'compute-gate','unit':label,'passed':False,'status':'DEFERRED'})
        save()
        raise SystemExit('DEFERRED: fresh conservative resource gate did not admit numerical diagnostics')
    if time.process_time()-cpu_started > 2:
        save()
        raise SystemExit('Bounded CPU budget reached; completed rows remain saved')

gate('scalar residual and finite contact enumeration')
b2 = 2/math.pi
q = 1-b2
violations = []
for k in range(1001):
    r = k/1000
    residual = b2*(math.asin(r)-r)
    if not -2e-15 <= residual <= q*r**3+2e-15:
        violations.append(r)
rows.append({'kind':'L1 scalar grid','points':1001,'violations':violations,
             'sharp_endpoint':b2*(math.pi/2-1),'sharp_constant':q,'passed':not violations})
save()

for beta in (0.05,0.4,1.0):
    n = 6
    states = list(itertools.product((-1,1),repeat=n))
    weights = [math.exp(beta*sum(s[i]*s[(i+1)%n] for i in range(n))) for s in states]
    z = math.fsum(weights)
    moments = {}
    for mask in range(1<<n):
        sites = [i for i in range(n) if mask & (1<<i)]
        moments[mask] = math.fsum(w*math.prod(s[i] for i in sites) for s,w in zip(states,weights))/z
    def moment(indices):
        mask = 0
        for i in indices:
            mask ^= 1<<i
        return moments[mask]
    G = [[moment((i,j)) for j in range(n)] for i in range(n)]
    chi = math.fsum(G[0])
    B = math.fsum(g*g for g in G[0])
    contacts = []
    for i,j,k in itertools.product(range(n),repeat=3):
        if len({0,i,j,k}) < 4:
            u4 = moment((0,i,j,k))-G[0][i]*G[j][k]-G[0][j]*G[i][k]-G[0][k]*G[i][j]
            contacts.append(-u4)
    observed = math.fsum(contacts)
    predicted = 12*chi**2-16*chi-6*B+12
    error = abs(observed-predicted)
    rows.append({'kind':'L3 exact finite cyclic Ising enumeration','n':n,'beta':beta,
                 'spin_configurations':len(states),'contact_triples':len(contacts),
                 'chi':chi,'B':B,'observed_contact_mass':observed,'predicted_contact_mass':predicted,
                 'absolute_error':error,'passed':error <= 2e-10})
    save()

for n in (2,3,4,8,16):
    observed = 2*sum(len({0,i,j,k})<4 for i,j,k in itertools.product(range(n),repeat=3))
    predicted = 12*n*n-22*n+12
    rows.append({'kind':'L3 perfectly correlated sharpness check','n':n,'observed':observed,
                 'predicted':predicted,'passed':observed == predicted})
    save()

for n in (4,8,16):
    gate('Gaussian-sign block n='+str(n))
    gamma = 1.04  # An illustrative exponent, not an asserted measured Ising exponent.
    linear = []
    remainder = []
    bound = []
    for i,j,k in itertools.product(range(1-n,n),repeat=3):
        count = (n-abs(i))*(n-abs(j))*(n-abs(k))
        r = (1+i*i+j*j+k*k)**(-gamma/2)
        linear.append(count*b2*r)
        remainder.append(count*b2*(math.asin(r)-r))
        bound.append(count*q*r**3)
    norm = n**(-6+gamma)
    v_linear = norm*math.fsum(linear)
    v_remainder = norm*math.fsum(remainder)
    v_bound = norm*math.fsum(bound)
    rows.append({'kind':'L2 exact block covariance sums','n':n,'gamma':gamma,
                 'linear_gaussian_variance':v_linear,'nonlinear_remainder_variance':v_remainder,
                 'proved_residual_bound':v_bound,'relative_remainder':v_remainder/v_linear,
                 'passed':0 <= v_remainder <= v_bound+2e-12})
    save()

save()
print(json.dumps({'rows':len(rows),'passed':all(r['passed'] for r in rows),
                  'max_contact_error':max(r.get('absolute_error',0) for r in rows),
                  'relative_remainders':[r['relative_remainder'] for r in rows if 'relative_remainder' in r],
                  'cpu_seconds':time.process_time()-cpu_started},indent=2))
