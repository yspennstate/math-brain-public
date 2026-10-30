from itertools import product

N = 9
COVERS = [
    (0,1),(0,3),(1,4),(1,5),(2,5),
    (3,5),(4,7),(5,6),(5,8),(6,7),
]

def transitive_closure(n, edges):
    R = [[False]*n for _ in range(n)]
    for a,b in edges:
        R[a][b] = True
    for k in range(n):
        for i in range(n):
            if R[i][k]:
                for j in range(n):
                    if R[k][j]:
                        R[i][j] = True
    return R

R = transitive_closure(N, COVERS)

def comparable(a,b):
    return R[a][b] or R[b][a]

# Enumerate all unordered three-chain covers.
chain_covers = set()
for colors in product(range(3), repeat=N):
    if set(colors) != {0,1,2}:
        continue
    good = True
    for i in range(N):
        for j in range(i+1,N):
            if colors[i] == colors[j] and not comparable(i,j):
                good = False
                break
        if not good:
            break
    if good:
        chains = []
        for c in range(3):
            # Natural labels are topological for this certificate.
            chains.append(tuple(i for i in range(N) if colors[i] == c))
        chain_covers.add(tuple(sorted(chains)))

# Exact linear extensions.
predmask = [0]*N
for v in range(N):
    for u in range(N):
        if R[u][v]:
            predmask[v] |= 1 << u

extensions = []
def rec(order, mask):
    if len(order) == N:
        extensions.append(tuple(order))
        return
    for v in range(N):
        if (mask >> v) & 1:
            continue
        if predmask[v] & ~mask:
            continue
        rec(order + [v], mask | (1 << v))
rec([],0)

def flux_matrix(chains, x):
    a = next(i for i,c in enumerate(chains) if x in c)
    b,c = [i for i in range(3) if i != a]
    W = [[0]*(len(chains[c])+1) for _ in range(len(chains[b])+1)]
    for L in extensions:
        pos = {v:k for k,v in enumerate(L)}
        s = sum(pos[y] < pos[x] for y in chains[b])
        t = sum(pos[y] < pos[x] for y in chains[c])
        W[s][t] += 1
    return a,b,c,W

active = 0
all_squares = 0
min_weighted_slack = None
for chains in sorted(chain_covers):
    for x in range(N):
        a,b,c,W = flux_matrix(chains,x)
        r = chains[a].index(x) + 1
        for s in range(len(chains[b])):
            for t in range(len(chains[c])):
                all_squares += 1
                w00 = W[s][t]
                w10 = W[s+1][t]
                w01 = W[s][t+1]
                w11 = W[s+1][t+1]

                # Ordinary TP2, including support-boundary squares.
                assert w00*w11 >= w10*w01

                if w10*w01:
                    active += 1
                    k = (r-1) + s + t
                    n_minus = k + 2
                    n_plus = N - k - 1
                    assert n_minus >= 2 and n_plus >= 2
                    # Quantitative Fishburn-TP2:
                    # W00 W11 / (W10 W01)
                    # >= n_minus/(n_minus-1) * n_plus/(n_plus-1).
                    lhs = w00*w11*(n_minus-1)*(n_plus-1)
                    rhs = w10*w01*n_minus*n_plus
                    slack = lhs-rhs
                    assert slack >= 0
                    if min_weighted_slack is None or slack < min_weighted_slack:
                        min_weighted_slack = slack

print("linear_extensions", len(extensions))
print("three_chain_covers", len(chain_covers))
print("elementary_squares", all_squares)
print("active_cross_squares", active)
print("min_quantitative_integer_slack", min_weighted_slack)
print("POS3_FLUX_FISHBURN_TP2_CHECK_PASS")
