"""Is the block-path swap an involution between bad and good? phi(bad) swaps on P_red(v,w); psi(good) swaps on P_blue(v,w).
Counts bad colourings with psi(phi(x)) == x, by shift; and whether the involution-closed part is level-preserving."""
import sys, random, itertools
from collections import Counter, defaultdict
sys.path.insert(0, '.')
from e1_swap import comps
exec(open(r'colour_blockpath_swap.py').read().split('V, m, seed')[0].split('from e1_swap import comps')[1])
V, m, seed, cnt = map(int, sys.argv[1:5]); rnd = random.Random(seed); st = Counter()
for t in range(cnt):
    H = [tuple(sorted(rnd.sample(range(V), 2))) for _ in range(m)]
    cfg = {}
    for mask in range(1 << m):
        kr, fr = comps(V, [H[j] for j in range(m) if mask >> j & 1]); kb, fb = comps(V, [H[j] for j in range(m) if not mask >> j & 1])
        cfg[mask] = (kr + kb, [fr(x) for x in range(V)], [fb(x) for x in range(V)])
    def sw(mask, P): return mask ^ sum(1 << j for j in range(m) if H[j][0] in P and H[j][1] in P)
    for u, v, w in itertools.permutations(range(V), 3):
        bad, good = [], set()
        for mask, (k, r, b) in cfg.items():
            if r[u] == r[v] or r[u] == r[w] or b[u] != b[v]: continue
            if r[v] == r[w] and b[v] != b[w]: bad.append(mask)
            if b[v] == b[w] and r[v] != r[w]: good.add(mask)
        inv_img = set(); rest = []
        for mask in bad:
            m2 = sw(mask, onpath(V, [H[j] for j in range(m) if mask >> j & 1], v, w))
            m3 = sw(m2, onpath(V, [H[j] for j in range(m) if not m2 >> j & 1], v, w))
            if m3 == mask: inv_img.add(m2); st['inv shift %d' % (cfg[m2][0] - cfg[mask][0])] += 1
            else: rest.append((mask, m2))
        for mask, m2 in rest:
            st['rest image in inv-image' if m2 in inv_img else 'rest image in leftover good'] += 1
        Gl = Counter(cfg[g][0] for g in good - inv_img); Rl = Counter(cfg[x][0] for x, _ in rest)
        st['levels where leftover good < rest'] += sum(1 for k in Rl if Gl[k] < Rl[k])
        Gk = Counter(cfg[g][0] for g in good); Bk = Counter(cfg[x][0] for x in bad)
        for k in Bk:
            ratio = Gk[k] / Bk[k]
            if ratio < st.get('min ratio', 9e9): st['min ratio'] = ratio; st['min at'] = (H, (u, v, w), k, Gk[k], Bk[k], Rl[k], Gl[k])
            st['tight levels (good==bad)'] += Gk[k] == Bk[k]
            st['tight levels with rest>0'] += Gk[k] == Bk[k] and Rl[k] > 0
            st['min (leftover-rest) at a level'] = min(st.get('min (leftover-rest) at a level', 9e9), Gl[k] - Rl[k])
        st['rest'] += len(rest); st['leftover good'] += len(good - inv_img)
print(V, m, seed, dict(st))
