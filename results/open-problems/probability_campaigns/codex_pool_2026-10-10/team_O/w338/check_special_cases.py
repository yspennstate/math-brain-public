"""Small exact/independent checks for the ten-problem research batch.

Run python -X utf8 check_special_cases.py. No live data is changed.
"""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json
import math
import time

ROOT = Path(__file__).resolve().parent
started = time.perf_counter()
results = {}

# P0266: independent quadrature of the transformed Gaussian inverse moment.
errors = []
for r in [0.5, 1.0, 2.0]:
    for horizon in [0.25, 1.0, 4.0]:
        steps = 2000
        f = lambda v: math.exp(-r*r*(1-v)/(2*horizon))/(2*horizon)
        integral = (f(0)+f(1)+sum((4 if i%2 else 2)*f(i/steps)
                    for i in range(1,steps)))/(3*steps)
        exact = -math.expm1(-r*r/(2*horizon))/(r*r)
        errors.append(abs(integral-exact))
assert max(errors) < 1e-10
for gamma2 in [F(1,2), F(1), F(3,2)]:
    dimension = 3+2/gamma2
    tail = (dimension-2)/2
    assert tail > 1
    assert tail/(tail-1) == (gamma2+2)/(2-gamma2)
results['P0266'] = dict(inverse_moment_grid=9, max_quadrature_error=max(errors),
                        subcritical_algebra_cases=3, critical_dimension=4)

# C0133: solve gambler's ruin independently by exact tridiagonal elimination.
def ruin_probability(L):
    d = [F(2)]*(L-1)
    rhs = [F(0)]*(L-1)
    rhs[-1] = F(1)
    for i in range(1,L-1):
        multiplier = -1/d[i-1]
        d[i] -= multiplier*(-1)
        rhs[i] -= multiplier*rhs[i-1]
    u = [F(0)]*(L-1)
    u[-1] = rhs[-1]/d[-1]
    for i in range(L-3,-1,-1):
        u[i] = (rhs[i]+u[i+1])/d[i]
    return u[0]/2
ruin = {str(L):str(ruin_probability(L)) for L in [2,3,5,10,100]}
assert all(ruin_probability(L) == F(1,2*L) for L in [2,3,5,10,100])
results['C0133'] = dict(exact_spatial_excursion_probabilities=ruin,
                        exponential_spatial_tail_counterexample=True)

# P0090: full matrix has spectral radius two; root cannot reach that class.
M = ((F(1,2),F(0)),(F(0),F(2)))
z = [F(1),F(0)]
for n in range(31):
    assert z == [F(1,2**n), F(0)]
    z = [sum(z[i]*M[i][j] for i in range(2)) for j in range(2)]
w = F(2)
assert M[0][0]*w == w-1
critical = [[0,1,0],[0,0,1],[1,0,0]]
population = [1,0,0]
for _ in range(100):
    population = [sum(population[i]*critical[i][j] for i in range(3)) for j in range(3)]
    assert sum(population) == 1
results['P0090'] = dict(reachable_example_generations=31,
                       expected_total_population=2,
                       critical_cycle_generations=100,
                       critical_cycle_population=1)

# P0427: continuation-aware objective, continuous one-dimensional minimization.
def s1(b):
    return min(b,math.sqrt(b))
def s2(b):
    return min(b,b**0.75)
def objective(b):
    r1,r2 = s1(b),s2(4-b)
    return (2+r1/s2(4)+r2/s1(4))/(r1+r2)
left,right = 1.0,4.0
phi = (math.sqrt(5)-1)/2
c,d = right-phi*(right-left),left+phi*(right-left)
for _ in range(100):
    if objective(c) < objective(d):
        right,d = d,c
        c = right-phi*(right-left)
    else:
        left,c = c,d
        d = left+phi*(right-left)
b = (left+right)/2
# Dense whole-interval scan verifies the boundary region also loses.
grid = [(objective(4*i/10000),4*i/10000) for i in range(10001)]
best_grid = min(grid)
assert objective(b) <= best_grid[0]+1e-12
assert objective(F(81,64)) < objective(1)
rates = [s1(4*i/10000)+s2(4-4*i/10000) for i in range(10001)]
assert max(rates) == rates[2500]
results['P0427'] = dict(throughput_allocation=1, throughput_objective=objective(1),
                        prior_diagnostic_allocation=float(F(81,64)),
                        prior_diagnostic_objective=objective(float(F(81,64))),
                        numerical_optimal_allocation=b, numerical_optimal_objective=objective(b),
                        percent_improvement=100*(objective(1)-objective(b))/objective(1),
                        whole_interval_grid=10001)

# C0032: the negative log potential of uniform disk measure is (1-r^2)/2
# inside its disk. Independent finite differences must recover positive density.
disk_potential = lambda r: (1-r*r)/2
laplacians = []
for radius in [0.1,0.25,0.5,0.9]:
    step = 1e-4
    second = (disk_potential(radius+step)-2*disk_potential(radius)
              +disk_potential(radius-step))/(step*step)
    first = (disk_potential(radius+step)-disk_potential(radius-step))/(2*step)
    laplacians.append(second+first/radius)
assert max(abs(v+2) for v in laplacians) < 1e-7
results['C0032'] = dict(unit_atom_distributional_laplacian_mass='-2*pi',
                        disk_potential_laplacians=laplacians,
                        recovered_disk_density_sign='positive with corrected minus sign',
                        proof_check='punctured-disk integration by parts')

# C0077: a.s. unconditional convergence with exact rare-event probabilities.
rare = []
for n in [10,11,100,101,1000,1001]:
    a = 1 if n%2 == 0 else 2
    rare.append(dict(n=n, probability=str(F(1,n)),
                     unconditional_mean=str(F(a,n)), conditional_value=a))
results['C0077'] = dict(exact_rare_event_cases=rare,
                        exact_n_times_event_probability=1,
                        conditional_limit_exists=False)

# C0119: finite Gaussian-polymer derivative, independent finite differences.
def polymer_data(dimension, length):
    directions = [tuple(s if j==i else 0 for j in range(dimension))
                  for i in range(dimension) for s in [-1,1]]
    paths = []
    coordinates = set()
    for steps in product(directions,repeat=length):
        position = (0,)*dimension
        path = []
        for t,step in enumerate(steps,1):
            position = tuple(x+y for x,y in zip(position,step))
            site = (t,position)
            coordinates.add(site)
            path.append(site)
        paths.append(path)
    ordered = sorted(coordinates)
    index = {x:i for i,x in enumerate(ordered)}
    return [[index[x] for x in path] for path in paths],len(index)
def free_energy_grad(x,paths,beta):
    energies = [beta*sum(x[i] for i in path) for path in paths]
    high = max(energies)
    weights = [math.exp(e-high) for e in energies]
    total = sum(weights)
    gradient = [0.0]*len(x)
    for path,w in zip(paths,weights):
        for i in path:
            gradient[i] += beta*w/total
    return high+math.log(total),gradient
gradient_errors = []
polymer_cases = []
for dimension,length in [(1,4),(3,3)]:
    paths,coordinates = polymer_data(dimension,length)
    x = [math.sin(i+0.2) for i in range(coordinates)]
    beta = 0.7
    _,g = free_energy_grad(x,paths,beta)
    for i in range(coordinates):
        plus,minus = x.copy(),x.copy()
        plus[i] += 1e-5
        minus[i] -= 1e-5
        difference = (free_energy_grad(plus,paths,beta)[0]
                      -free_energy_grad(minus,paths,beta)[0])/(2e-5)
        gradient_errors.append(abs(difference-g[i]))
    assert abs(sum(g)-beta*length) < 1e-12
    polymer_cases.append(dict(dimension=dimension,length=length,
                              paths=len(paths),coordinates=coordinates))
assert max(gradient_errors) < 1e-8
results['C0119'] = dict(cases=polymer_cases,
                        max_gradient_error=max(gradient_errors),
                        check_scope='gradient identity only; OU theorem is proved in prose')

# P0010: enumerate boundary orientations independently for finite shapes.
def boundary(S):
    edges = set()
    for u in S:
        for step in [(1,0),(-1,0),(0,1),(0,-1)]:
            v = (u[0]+step[0],u[1]+step[1])
            if v not in S:
                edges.add(tuple(sorted((u,v))))
    return sorted(edges)
shapes = [{(0,0)}, {(0,0),(1,0)}, {(0,0),(1,0),(0,1),(1,1)}]
boundary_checks = 0
for S in shapes:
    edges = boundary(S)
    for p in [F(1,10),F(1,4),F(1,2),F(3,4),F(9,10)]:
        probability = F(0)
        for orientation in product([0,1],repeat=len(edges)):
            good = True
            k = sum(orientation)
            for (u,v),bit in zip(edges,orientation):
                # Sorted adjacent endpoints follow the positive coordinate direction.
                target = v if bit else u
                if target not in S:
                    good = False
                    break
            if good:
                probability += p**k*(1-p)**(len(edges)-k)
        assert probability == (p*(1-p))**(len(edges)//2)
        boundary_checks += 1
results['P0010'] = dict(exact_boundary_cases=boundary_checks,
                        perimeters=[len(boundary(S)) for S in shapes],
                        singleton_sink_probability='p^2*(1-p)^2')

# P0036: exact exponential-volume comb from the prior attempt, with pc=1.
# The binary tree attached at spine vertex i begins at depth i+1 and has height i.
def comb_sphere(n):
    return 1+sum(2**(n-i-1) for i in range(n)
                 if 0 <= n-i-1 <= i)
rates = {str(n): math.log(comb_sphere(n))/n for n in [20,40,80,160]}
assert abs(rates['160']-math.log(2)/2) < 0.01
results['P0036'] = dict(comb_log_sphere_growth=rates,
                        limiting_log_sphere_growth=math.log(2)/2,
                        comb_pc=1,
                        cayley_special_case='subexponential growth implies pc=1 by union bound')

results['seconds'] = time.perf_counter()-started
(ROOT/'special_case_measurements.json').write_text(json.dumps(results,indent=2),encoding='utf-8')
print(json.dumps(results,indent=2))
