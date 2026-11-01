"""
Verify KEY LEMMA (light, streaming):  q_{D,1}(t)/p_1(t)^2 should ~ log(1/t) for D=2,
-> 1 for large D, and NEVER approach the crude bound 1/p1. Batched MC to bound memory.
"""
import numpy as np, math, sys

def estimate(field, D, t, M, batch, seed):
    cplx = (field == 'C'); rng = np.random.default_rng(seed)
    def gauss(shape):
        if cplx: return (rng.standard_normal(shape)+1j*rng.standard_normal(shape))/math.sqrt(2)
        return rng.standard_normal(shape)
    nX = nQ = done = 0
    while done < M:
        b = min(batch, M-done); done += b
        g = gauss((b, D)); u = gauss((b, D)); v = gauss((b, D))
        u /= np.linalg.norm(u, axis=1, keepdims=True); v /= np.linalg.norm(v, axis=1, keepdims=True)
        X = np.abs(np.einsum('ij,ij->i', g, np.conj(u)))
        Y = np.abs(np.einsum('ij,ij->i', g, np.conj(v)))
        cx = (X <= t); nX += int(cx.sum()); nQ += int((cx & (Y <= t)).sum())
    p = nX/M; q = nQ/M
    return p, q

if __name__ == "__main__":
    M, batch = 3_000_000, 250_000
    for field in ('R', 'C'):
        print(f"=== field {field} (d_F={2 if field=='C' else 1}) ===", flush=True)
        for t in (0.15, 0.10, 0.06):
            L = 1+math.log(1/t); cells=[]
            for D in (2, 3, 5, 20):
                p, q = estimate(field, D, t, M, batch, seed=hash((field,t,D))%(2**31))
                r = q/(p*p) if p>0 else float('nan')
                cells.append(f"D={D:2d}:{r:5.2f}")
            print(f" t={t:.2f}: p1={p:.4f} (1+log1/t)={L:.2f} 1/p1={1/p:6.1f} | q/p1^2: "
                  + "  ".join(cells), flush=True)
