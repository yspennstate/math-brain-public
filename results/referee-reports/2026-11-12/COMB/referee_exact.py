"""Independent exact rational checks, using no authors' code or third-party modules."""
from fractions import Fraction as F
from collections import defaultdict
import json


def advance(dist, transitions):
    out = defaultdict(F)
    for v, mass in dist.items():
        for w, prob in transitions[v]:
            out[w] += mass * prob
    return dict(out)


def kernel(transitions, start, steps):
    out = [{start: F(1)}]
    for _ in range(steps):
        out.append(advance(out[-1], transitions))
    return out


def main():
    # A small comb killed on leaving [-3,3] with its full teeth.
    heights = {-3: 1, -2: 3, -1: 0, 0: 2, 1: 1, 2: 2, 3: 0}
    states = [(x,y) for x,h in heights.items() for y in range(h+1)]
    transitions = {}
    degrees = {}
    for x,y in states:
        if y == 0:
            nbrs = [(x-1,0),(x+1,0)] + ([(x,1)] if heights[x] else [])
        else:
            nbrs = [(x,y-1)] + ([(x,y+1)] if y < heights[x] else [])
        degrees[x,y] = len(nbrs)
        transitions[x,y] = [(w,F(1,len(nbrs))) for w in nbrs if w in states]
    T = 6
    target = [(x,0) for x in (-1,0,1)]
    starts = ((0,0),(0,2))  # same colour, distinct starting vertices
    kernels = {s:kernel(transitions,s,T) for s in set(target) | set(starts)}
    window = range(2,T+1)
    first = sum(kernels[starts[0]][n].get(x,F()) * kernels[starts[1]][n].get(x,F())
                for n in window for x in target)
    cross = F()
    free_uniform = F()
    for n in window:
        a = max(kernels[starts[0]][n].get(x,F()) for x in target)
        b = max(kernels[starts[1]][n].get(x,F()) for x in target)
        for nn in window:
            if nn <= n:
                continue
            spatial = F()
            for x in target:
                continuation = sum(kernels[x][nn-n].get(y,F()) ** 2 for y in target)
                cross += kernels[starts[0]][n].get(x,F()) * kernels[starts[1]][n].get(x,F()) * continuation
                spatial += continuation
            free_uniform += a*b*spatial
    # Independent pair-chain propagation with accumulated reward. The two
    # accumulated totals below retain rewards from paths killed later.
    mass = {(starts[0],starts[1]):F(1)}
    weighted = {}
    first_dp = second_dp = F()
    for n in range(1,T+1):
        aa, bb = defaultdict(F), defaultdict(F)
        for (x,y), prob in mass.items():
            for xx, px in transitions[x]:
                for yy, py in transitions[y]:
                    aa[xx,yy] += prob*px*py
                    bb[xx,yy] += weighted.get((x,y),F())*px*py
        if n in window:
            for x in target:
                reward = aa.get((x,x),F())
                first_dp += reward
                second_dp += 2*bb.get((x,x),F()) + reward
                bb[x,x] += reward
        mass, weighted = dict(aa),dict(bb)
    assert first_dp == first
    assert second_dp == first+2*cross
    assert cross <= free_uniform
    # Exact gambler's ruin clocks. Old: next visit to L Z after time 0.
    # New: first visit to {-L,+L}. The old return has probability 1-1/L.
    clock = []
    for L in (3,9,30):
        old_mean = 1 + F(1)*(L-1)
        new_mean = L*L
        return_probability = 1-F(1,L)
        clock.append(dict(spacing=L,old_mean=str(old_mean),new_mean=new_mean,
                          ratio=str(F(new_mean,old_mean)),return_probability=str(return_probability)))
    # On the comb with H_x=1, the path (0,0),(1,0),(2,0),(3,0)
    # hits a different coarse point with no tooth excursion.
    witness = F(1,3)**3
    # For a backbone SRW killed at +/-3L, the number of visits to a
    # selected root a in [L,2L], conditional on exit at +3L, is geometric.
    L,a = 10,15
    geom_p = (F(1,3*L-a)+F(1,3*L+a))/2
    result = {
        "exact_first_moment":str(first),"exact_first_decimal":float(first),
        "exact_second_moment":str(second_dp),"exact_second_decimal":float(second_dp),
        "pair_chain_equals_pair_of_times_expansion":True,
        "uniform_earlier_kernel_upper_bound_verified":True,
        "uniform_bound_second_decimal":float(first+2*free_uniform),
        "coarse_clocks":clock,
        "no_tooth_excursion_crossing_probability":str(witness),
        "geometric_local_time_example":{"L":L,"a":a,"parameter":str(geom_p),"mean":str(1/geom_p)},
        "critical_exponents":{"4/(gamma+1)":str(F(4)/(F(1,3)+1)),
          "(3-gamma)/4":str((3-F(1,3))/4),"(gamma+1)/4":str((F(1,3)+1)/4),
          "first_moment_N_power":3+1-4,"pair_time_prefactor_N_power":3-4},
        "small_time_concentration_delta_half":{"variance_N_power":"5/4", "variance_log_power":"1/2",
          "chebyshev_N_power":"-3/4","chebyshev_log_power":"-3/2"},
    }
    with open("exact_checks.json","w") as f:
        json.dump(result,f,indent=2)
        f.write("\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
