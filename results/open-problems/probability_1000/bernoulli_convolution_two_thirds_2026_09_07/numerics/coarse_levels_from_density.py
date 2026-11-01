# k-level coarse shares (k = 1, 2, 3) from a saved stationary density, levels n = 0..NMAX.
import numpy as np, sys
c = np.load(sys.argv[1]); NMAX = int(sys.argv[2]) if len(sys.argv) > 2 else 8
def stats(mass):
    half = mass.size//2; m0 = mass[:half]; m1 = mass[half:]; tot = m0+m1
    u = np.where(tot>0, (m0-m1)/np.maximum(tot,1e-300), 0.0)
    return float(np.sum(tot*u**2))/float(np.sum(tot)), u, tot
lv = []; g = c
for n in range(NMAX + 4):
    if g.size % 54: break
    E, u, tot = stats(g); lv.append((n, E, u, tot)); g = g[:g.size//2] + g[g.size//2:]
print("n | Eu2 | k=1: dec, coarse share | k=2: dec, share | k=3: dec, share   (share = coarse lower bound / k-level decrement)")
for i in range(min(NMAX + 1, len(lv) - 3)):
    n, E, u, tot = lv[i]; T = float(tot.sum()); half = u.size; out = [f"n={n}: Eu2={E:.3e}"]
    for k in (1, 2, 3):
        Ek = lv[i+k][1]; ncls = 3**k; per = half//ncls; Lc = 0.0
        for cc in range(ncls):
            s = (-1.0)**sum((cc//3**d) % 3 for d in range(k)); sl = slice(cc*per, (cc+1)*per)
            Pc = float(tot[sl].sum())/T; num = s*float((tot[sl]*u[sl]).sum())/T; Lc += num**2/max(Pc, 1e-300)
        out.append(f"k={k}: dec/Eu2={(E-Ek)/E:.3f} share={Lc/max(E-Ek,1e-300):.3f}")
    print("  ".join(out))
