"""All monotone Boolean functions of n <= 6 variables (7,828,354 at n = 6).

For each: Hinf, I, the empty and singleton parts of the min-entropy
    A0 = log2(1/fhat(empty)^2),  A1 = 2 log2(1/max_i Inf_i)   (monotone: |fhat({i})| = Inf_i),
and the ratios Hinf/I, min(A0, A1)/I.  Reports maxima and maximizers.
"""
import sys, json, time
import numpy as np
import psutil
_p = psutil.Process(); _p.nice(psutil.BELOW_NORMAL_PRIORITY_CLASS); _p.cpu_affinity([2, 3, 10, 11, 12, 13, 14, 15])
sys.path.insert(0, __file__.rsplit("/", 1)[0].rsplit("\\", 1)[0])
from fmei_lib import coeffs, popcounts, bits_to_pm


def monotone_masks(n):
    """Monotone (increasing) truth tables on n variables as uint64 masks; bit x = f(x)."""
    M = np.array([0, 1], dtype=np.uint64)  # n = 0: constant false, constant true (one point)
    for k in range(n):
        half = 1 << k
        full = np.uint64((1 << half) - 1) if half < 64 else np.uint64(0xFFFFFFFFFFFFFFFF)
        out = []
        for f0 in M:
            ok = (f0 & (~M & full)) == 0          # f0 <= f1 pointwise
            f1 = M[ok]
            out.append(f0 | (f1 << np.uint64(half)))
        M = np.concatenate(out)
    return M


def main():
    t0 = time.time()
    res = {}
    for n in range(1, 7):
        M = monotone_masks(n)
        N = 1 << n
        pc = popcounts(n).astype(np.float64)
        single = np.array([1 << i for i in range(n)])
        best = dict(ratio=-1.0, ratio01=-1.0)
        worst_kkl = -np.inf
        cnt = len(M)
        CH = 100000
        c2ln2 = 2 / np.log(2)
        viol_2ln2 = 0
        viol_4 = 0
        for a in range(0, cnt, CH):
            chunk = M[a:a + CH]
            tt = bits_to_pm(chunk, n)
            c = coeffs(tt)
            p = c * c
            I = p @ pc
            nc = I > 1e-15
            with np.errstate(divide="ignore"):
                Hinf = -np.log2(p.max(axis=1))
                A0 = -np.log2(p[:, 0])
                A1 = -np.log2(p[:, single].max(axis=1))
            A01 = np.minimum(A0, A1)
            r = np.where(nc, Hinf / np.where(nc, I, 1), -1.0)
            r01 = np.where(nc, A01 / np.where(nc, I, 1), -1.0)
            viol_2ln2 += int(np.sum(nc & (Hinf > c2ln2 * I + 1e-12)))
            viol_4 += int(np.sum(nc & (Hinf > 4 * I + 1e-12)))
            k = int(np.argmax(r))
            if r[k] > best["ratio"]:
                best.update(ratio=float(r[k]), mask=int(chunk[k]), Hinf=float(Hinf[k]), I=float(I[k]), mean=float(c[k, 0]))
            k = int(np.argmax(r01))
            if r01[k] > best["ratio01"]:
                best.update(ratio01=float(r01[k]), mask01=int(chunk[k]), A01=float(A01[k]), I01=float(I[k]))
        res[n] = dict(count=cnt, **best, violations_Hinf_gt_2overln2_I=viol_2ln2, violations_Hinf_gt_4I=viol_4)
        print(n, json.dumps(res[n]), f"{time.time() - t0:.1f}s", flush=True)


if __name__ == "__main__":
    main()
