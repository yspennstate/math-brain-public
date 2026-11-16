import numpy as np, math
rng=np.random.default_rng(7)
for r in (4,16,64,256):
    reps = 2000 if r<=64 else 600
    out=[]
    for shape in ("real sym","complex sym","complex Ginibre"):
        v=[]
        for _ in range(reps):
            if shape=="real sym":
                G=rng.standard_normal((r,r)); G=(G+G.T)/math.sqrt(2)
            elif shape=="complex sym":
                G=(rng.standard_normal((r,r))+1j*rng.standard_normal((r,r)))/math.sqrt(2); G=(G+G.T)/math.sqrt(2)
            else:
                G=(rng.standard_normal((r,r))+1j*rng.standard_normal((r,r)))/math.sqrt(2)
            v.append(np.linalg.norm(G,2)/(2*math.sqrt(r)))
        out.append(f"{shape} {np.mean(v):.3f}+-{np.std(v,ddof=1)/math.sqrt(reps):.3f}")
    print(f"r={r} ({reps} draws): "+"; ".join(out), flush=True)
