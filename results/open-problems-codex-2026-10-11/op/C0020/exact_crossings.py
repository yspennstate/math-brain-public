"""Exact uniform zero-error decision-tree costs on finite triangular rhombi.
No sampled probabilities. Integer Bellman sums over all completions.
"""
import json, time
from functools import lru_cache
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def solve(w, h):
    start = time.perf_counter()
    n = w*h
    full = (1 << n)-1
    adj = []
    for y in range(h):
        for x in range(w):
            adj.append(sum(1 << (yy*w+xx) for dx,dy in
                [(1,0),(-1,0),(0,1),(0,-1),(1,-1),(-1,1)]
                if 0 <= (xx:=x+dx) < w and 0 <= (yy:=y+dy) < h))
    left = sum(1 << (y*w) for y in range(h))
    right = left << (w-1)
    def crossing(mask):
        seen = mask & left
        frontier = seen
        while frontier:
            if frontier & right: return True
            neighbors = 0
            while frontier:
                b = frontier & -frontier
                neighbors |= adj[b.bit_length()-1]
                frontier ^= b
            frontier = neighbors & mask & ~seen
            seen |= frontier
        return False
    truth = [crossing(m) for m in range(1<<n)]
    policy = {}
    @lru_cache(None)
    def total(known, ones):
        unknown = full ^ known
        if truth[ones] or not truth[ones | unknown]: return 0
        u = unknown.bit_count()
        best = n*(1<<u)+1
        scan = unknown
        while scan:
            b = scan & -scan
            val = (1<<u) + total(known|b,ones) + total(known|b,ones|b)
            if val < best: best, choice = val,b
            scan ^= b
        policy[known,ones] = choice
        return best
    root = total(0,0)
    depths=[]
    for m in range(1<<n):
        known=ones=depth=0
        while (known,ones) in policy:
            b=policy[known,ones]
            known |= b
            ones |= m & b
            depth+=1
        assert truth[ones] == truth[ones | (full ^ known)] == truth[m]
        depths.append(depth)
    assert sum(depths)==root
    # Each decisive partial assignment admits a same-colour certificate.
    witness=[]
    for m in range(1<<n):
        available = m if truth[m] else full^m
        s=available
        best=n
        while True:
            cert = truth[s] if truth[m] else not truth[full^s]
            if cert: best=min(best,s.bit_count())
            if not s:break
            s=(s-1)&available
        witness.append(best)
    influence_counts=[sum(truth[m] != truth[m^(1<<i)] for m in range(1<<n)) for i in range(n)]
    p=Fraction(sum(truth),1<<n)
    I=Fraction(sum(influence_counts),1<<n)
    centered_bound=I*I/(4*p*(1-p))
    cost=Fraction(root,1<<n)
    assert cost>=centered_bound
    assert all(c>=v for c,v in zip(depths,witness))
    # Independent truth-table recursion (no monotonicity stopping test) for n<=9.
    checked_states=0
    if n<=9:
        @lru_cache(None)
        def independent(known,ones):
            nonlocal checked_states
            checked_states+=1
            unknown=full^known
            values={truth[m] for m in range(1<<n) if m&known==ones}
            if len(values)==1:return 0
            choices=[1<<i for i in range(n) if unknown&(1<<i)]
            return (1<<unknown.bit_count())+min(independent(known|b,ones)+independent(known|b,ones|b) for b in choices)
        assert independent(0,0)==root
    result={'width':w,'height':h,'sites':n,'crossing_probability':str(p),
      'optimal_expected_queries':str(cost),'sum_optimal_depths':root,
      'expected_minimum_certificate':str(Fraction(sum(witness),1<<n)),
      'total_influence':str(I),'centered_influence_lower_bound':str(centered_bound),
      'optimal_first_sites':[i for i in range(n) if (1<<n)+total(1<<i,0)+total(1<<i,1<<i)==root],
      'bellman_states':total.cache_info().currsize,'independent_truth_table_states':checked_states,
      'all_inputs_replayed':1<<n,'all_sites_relevant':all(influence_counts),
      'elapsed_seconds':time.perf_counter()-start}
    (ROOT/f'exact_{w}x{h}.json').write_text(json.dumps(result,indent=2),encoding='utf8')
    print(json.dumps(result),flush=True)
    return result

if __name__=='__main__':
    rows=[solve(w,h) for w,h in [(1,1),(2,1),(1,3),(2,2),(3,2),(3,3),(4,3)]]
    (ROOT/'exact_results.json').write_text(json.dumps(rows,indent=2),encoding='utf8')
