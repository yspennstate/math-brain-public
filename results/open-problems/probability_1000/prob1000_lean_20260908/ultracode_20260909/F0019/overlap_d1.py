# F0019: exact transfer-matrix numerics for the d=1 Gaussian directed polymer.
# (a) whole-path overlap OV_n of mu_n versus the endpoint overlaps EP_n (CSY's I_k) and EP'_n;
# (b) independent check of the identity p_n'(beta) = beta (1 - E OV_n) by finite differences;
# (c) monotonicity of OV_n(beta) in beta, pathwise and in mean.
import numpy as np, sys, json, time
rng = np.random.default_rng(20260909)

def layers(omega, beta):
    """omega: (n+1, 2n+1) array, row k = time k (row 0 unused). Returns per-time
    overlaps under mu_n (OV terms), CSY endpoint overlaps I_k = sum_x mu_{k-1}(X_k=x)^2,
    endpoint overlaps I'_k = sum_x mu_k(X_k=x)^2, and log Z_n."""
    n = omega.shape[0]-1; L = omega.shape[1]
    F = np.zeros(L); F[n] = 1.0            # X_0 = 0 at index n
    Fs = [F.copy()]; logZ = 0.0
    I_csy = np.zeros(n+1); I_end = np.zeros(n+1)
    for k in range(1, n+1):
        pred = np.zeros(L); pred[1:] += F[:-1]; pred[:-1] += F[1:]; pred *= 0.5
        # mu_{k-1}(X_k = x) = pred / sum(F)  (F is normalised to sum 1 below, so pred sums to 1)
        I_csy[k] = np.sum(pred**2)
        F = pred*np.exp(beta*omega[k])
        s = F.sum(); logZ += np.log(s); F /= s
        I_end[k] = np.sum(F**2)
        Fs.append(F.copy())
    # backward
    B = np.ones(L); OV = np.zeros(n+1)
    for k in range(n, 0, -1):
        m = Fs[k]*B; m /= m.sum(); OV[k] = np.sum(m**2)
        # B_{k-1}(y) = sum_{x~y} e^{beta w_{k,x}} B_k(x) /2
        g = np.exp(beta*omega[k])*B
        Bn = np.zeros(L); Bn[1:] += g[:-1]; Bn[:-1] += g[1:]; Bn *= 0.5
        B = Bn/Bn.max()
    return OV[1:], I_csy[1:], I_end[1:], logZ

def run():
    out = {}
    # (a) OV vs EP at beta = 1, growing n
    print("(a) d=1 Gaussian, beta=1: mean per-time overlaps, whole-path (OV) vs endpoint (CSY I_k, and I'_k)")
    res_a = {}
    for n in [25, 50, 100, 200, 400]:
        M = 200 if n <= 200 else 80
        ov = ep = ep2 = 0.0
        for _ in range(M):
            w = rng.standard_normal((n+1, 2*n+1))
            OV, Ic, Ie, lz = layers(w, 1.0)
            ov += OV.mean(); ep += Ic.mean(); ep2 += Ie.mean()
        res_a[n] = (ov/M, ep/M, ep2/M)
        print(f"  n={n:4d} M={M:3d}  E OV_n={ov/M:.4f}  E EP_n(CSY)={ep/M:.4f}  E EP'_n={ep2/M:.4f}  ratio OV/EP={ov/ep:.3f}")
    out['a'] = res_a
    # (b) identity check: p_n'(beta) vs beta(1 - E OV_n), common random numbers, central differences
    print("(b) identity p_n' = beta(1 - E OV_n): finite-difference p_n' vs overlap formula")
    n, M, h = 100, 300, 0.02
    res_b = {}
    for beta in [0.5, 1.0, 2.0]:
        d = 0.0; ov = 0.0
        for _ in range(M):
            w = rng.standard_normal((n+1, 2*n+1))
            _,_,_,lp = layers(w, beta+h); _,_,_,lm = layers(w, beta-h)
            OV,_,_,_ = layers(w, beta)
            d += (lp-lm)/(2*h)/n; ov += OV.mean()
        res_b[beta] = (d/M, beta*(1-ov/M))
        print(f"  beta={beta}: FD p_n'={d/M:.4f}   beta(1-E OV_n)={beta*(1-ov/M):.4f}")
    out['b'] = res_b
    # (c) monotonicity in beta of OV_n(beta), same environments
    print("(c) monotonicity of OV_n(beta) in beta (d=1, n=100, M=300): pathwise violations and mean curve")
    betas = np.array([0.1,0.25,0.5,0.75,1.0,1.25,1.5,2.0,2.5,3.0,4.0])
    n, M = 100, 300
    mean = np.zeros(len(betas)); viol = 0; worst = 0.0
    meanI = np.zeros(len(betas))
    for _ in range(M):
        w = rng.standard_normal((n+1, 2*n+1))
        vals = []; valsI=[]
        for b in betas:
            OV, Ic, _, _ = layers(w, b); vals.append(OV.mean()); valsI.append(Ic.mean())
        vals = np.array(vals); valsI=np.array(valsI)
        mean += vals; meanI += valsI
        dv = np.diff(vals)
        if (dv < -1e-12).any():
            viol += 1; worst = min(worst, dv.min())
    mean /= M; meanI/=M
    for b, m, mi in zip(betas, mean, meanI):
        print(f"  beta={b:4.2f}  E OV_n={m:.4f}   E EP_n(CSY)={mi:.4f}")
    print(f"  environments with a pathwise decrease of OV_n along the beta grid: {viol}/{M}, worst step {worst:.2e}")
    print("  mean-curve increments:", np.round(np.diff(mean),5).tolist())
    out['c'] = {'betas': betas.tolist(), 'mean_OV': mean.tolist(), 'mean_EP': meanI.tolist(), 'pathwise_violations': viol, 'M': M, 'worst': worst}
    json.dump(out, open('overlap_d1_results.json','w',encoding='utf-8'), indent=1, default=str)

t=time.time(); run(); print("elapsed", round(time.time()-t,1), "s")
