# Search rank-4 binary matroids [I4|A] for a pair positively correlated under the uniform basis measure (the S8 phenomenon).
import itertools
def rank(cols):
    piv = {}
    for v in cols:
        while v:
            t = v.bit_length() - 1
            if t not in piv: piv[t] = v; break
            v ^= piv[t]
    return len(piv)
I = [1, 2, 4, 8]; quads = list(itertools.combinations(range(8), 4)); found = []
for code in range(1 << 16):
    A = [(code >> (4 * c)) & 15 for c in range(4)]
    if 0 in A: continue
    cols = I + A
    B = [qq for qq in quads if rank([cols[i] for i in qq]) == 4]
    n = len(B)
    for e, f in itertools.combinations(range(8), 2):
        ne = sum(e in b for b in B); nf = sum(f in b for b in B); nef = sum(e in b and f in b for b in B)
        if n * nef > ne * nf: found.append((code, e, f, n, ne, nf, nef)); break
    if len(found) >= 3: break
print(len(found), found)
