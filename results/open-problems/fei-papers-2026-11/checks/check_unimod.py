import json
from fractions import Fraction as F
R = r"~/AppData/Local/Temp/claude/727c9a8b9fa813fe/agent-66b6-4575-b3c4-a8807fd17369/scratchpad/zen8/toeplitz-hankel-section-profiles"
mT = {0: F(1), 2: F(1), 4: F(8,3), 6: F(11), 8: F(908,15), 10: F(415), 12: F(23840,7), 14: F(325719,10),
      16: F(112135066,315), 18: F(3065263961,700), 20: F(69174280444,1155), 22: F(5680684105259,6300)}
for n in (10, 12, 14):
    d = json.load(open(f"{R}/data/volumes_T{n}.json"))
    s = sum(F(v["volume"]) * v["size"] for v in d["orbits"].values())
    print(f"m{n} from volume table", s, "table", mT[n], s == mT[n], "| file says", d.get("moment_exact"))
u = [(2 * k + 1) * mT[2 * k] for k in range(12)]
print("u", [str(x) for x in u[:6]])
def det(M):
    M = [row[:] for row in M]; n = len(M); dt = F(1)
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None: return F(0)
        if p != c: M[c], M[p] = M[p], M[c]; dt = -dt
        dt *= M[c][c]
        for r in range(c + 1, n):
            f = M[r][c] / M[c][c]
            for cc in range(c, n): M[r][cc] -= f * M[c][cc]
    return dt
print("minors u_{i+j}  ", [float(det([[u[i + j] for j in range(s)] for i in range(s)])) > 0 for s in range(1, 7)])
print("minors u_{i+j+1}", [float(det([[u[i + j + 1] for j in range(s)] for i in range(s)])) > 0 for s in range(1, 7)])
