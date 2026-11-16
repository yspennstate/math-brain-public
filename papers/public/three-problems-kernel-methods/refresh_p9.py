#!/usr/bin/env python3
"""Rebuild every table and every computed number in paper 9 from the campaign records, then audit.

Every table body between a pair of AUTOTABLE markers, and every numerical macro in the
`macros` region of the preamble, is regenerated from records/ by this script.  Nothing that
can drift is typed into the .tex by hand.

  python refresh_p9.py --pull          fetch fresh records from the box first
  python refresh_p9.py                 rebuild from whatever is already in records/
  python refresh_p9.py --no-build      rebuild and audit, do not run pdflatex

Exit status is non-zero if any audit check fails.
"""
import argparse
import glob
import json
import math
import os
import statistics as st
import subprocess
import sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
TEX = os.path.join(HERE, "paper", "kernel_open_problems_numerics.tex")
RECORDS = os.path.join(HERE, "records")
PDFLATEX = os.environ.get("PDFLATEX", "pdflatex")

# The two proved constants of Target 3, both from track P23 of the ProofNet24 archive
# (run reports of 2026-09-16 07:57 and 08:27; the values have been stable since 2026-09-15 22:26).
#   CTEN  : the ten-window certificate c_10 = 3882594969529/12500000000000, the strongest proved
#           lower bound for liminf E[excess risk]/sigma^2 at n = 2^d, every fixed h > 0
#   CONE  : the audited one-window theorem, liminf E[excess risk]/sigma^2 >= 5/36
# The measured leverage functional V/sigma^2 is compared with CTEN; the measured single-block
# certificate is compared with CONE, which is what the single-block argument proves.
CTEN = 3882594969529 / 12500000000000
CONE = 5.0 / 36.0
YMIN = 0.2   # the one-window theorem's block satisfies D_L/n in (1/5, 1]

ap = argparse.ArgumentParser()
ap.add_argument("--no-build", action="store_true")
a = ap.parse_args()


REC = defaultdict(list)
for f in glob.glob(os.path.join(RECORDS, "p9*.json")):
    try:
        d = json.load(open(f, encoding="utf-8"))
    except Exception as e:
        print(f"  unreadable {os.path.basename(f)}: {e}")
        continue
    REC[d.get("kind", "?")].append(d)
print("records: " + ", ".join(f"{k} {len(v)}" for k, v in sorted(REC.items())) or "none")

AUDIT = []
MACROS = {}
BS = chr(92)          # a LaTeX backslash, never written as a string literal


def check(name, ok, detail="", observed=None, threshold=None, kind="below"):
    """Record a check, and where possible how much room it had to fail."""
    margin = None
    if observed is not None and threshold is not None:
        try:
            margin = (threshold / observed) if kind == "below" else (observed / threshold)
        except ZeroDivisionError:
            margin = float("inf")
    AUDIT.append((name, ok, detail, margin))


def macro(name, text):
    """A number the prose quotes; emitted as \\newcommand{\\num<name>} in the preamble's macros region."""
    assert name.isalpha() and name[0].isupper(), name
    MACROS["num" + name] = str(text)


def fmt(x, n=4):
    return f"{x:.{n}f}"


def sd(v):
    return st.stdev(v) if len(v) > 1 else 0.0


def se(v):
    return sd(v) / math.sqrt(len(v)) if len(v) > 1 else 0.0


def quantile(v, q):
    v = sorted(v)
    k = (len(v) - 1) * q
    lo, hi = math.floor(k), math.ceil(k)
    return v[lo] if lo == hi else v[lo] * (hi - k) + v[hi] * (k - lo)


def sci(x, n=1):
    """1.3e-02 -> $1.3\\times10^{-2}$."""
    if x == 0:
        return "$0$"
    e = int(math.floor(math.log10(abs(x))))
    m = x / (10.0 ** e)
    return f"${m:.{n}f}" + BS + f"times10^{{{e}}}$"


def ms(v, n=2):
    """mean +- sd over designs."""
    return f"${st.mean(v):.{n}f}" + BS + f"pm{sd(v):.{n}f}$"


def mse(v, n=3):
    """mean +- standard error."""
    return f"${st.mean(v):.{n}f}" + BS + f"pm{se(v):.{n}f}$"


def _wls(D, Y, W, ncol):
    """Weighted least squares of Y on [1, 1/d, 1/d^2][:ncol] with weights W = 1/se^2.
    Returns (beta, se(beta), chi2, dof); the standard errors are those of a fit with known
    variances, (X^T W X)^{-1}, and chi2 says how well the model fits at those variances."""
    basis = lambda d: [1.0, 1.0 / d, 1.0 / d ** 2][:ncol]
    XtWX = [[0.0] * ncol for _ in range(ncol)]
    XtWY = [0.0] * ncol
    for d, y, w in zip(D, Y, W):
        b = basis(d)
        for i in range(ncol):
            XtWY[i] += w * b[i] * y
            for j in range(ncol):
                XtWX[i][j] += w * b[i] * b[j]
    A = [row[:] + [1.0 if i == j else 0.0 for j in range(ncol)] for i, row in enumerate(XtWX)]
    for i in range(ncol):
        p = A[i][i]
        for j in range(2 * ncol):
            A[i][j] /= p
        for r in range(ncol):
            if r != i:
                f = A[r][i]
                for j in range(2 * ncol):
                    A[r][j] -= f * A[i][j]
    inv = [row[ncol:] for row in A]
    beta = [sum(inv[i][j] * XtWY[j] for j in range(ncol)) for i in range(ncol)]
    chi2 = 0.0
    for d, y, w in zip(D, Y, W):
        pred = sum(beta[i] * basis(d)[i] for i in range(ncol))
        chi2 += w * (y - pred) ** 2
    dof = max(1, len(D) - ncol)
    ses = [math.sqrt(inv[i][i]) if inv[i][i] > 0 else float("nan") for i in range(ncol)]
    return beta, ses, chi2, dof


# ======================================================================= Target 3 (p9_gap2)
def _gap2_by_dh():
    agg = defaultdict(list)
    for d in REC["p9_gap2"]:
        for r in d["records"]:
            agg[(r["d"], r["h"])].append(r)
    return agg


def _theorem_block(blocks, n):
    """the one-window theorem's block: the largest L with D_L <= n."""
    ok = [b for b in blocks if b["D_L"] <= n]
    return max(ok, key=lambda b: b["L"]) if ok else None


def table_blocks(d_want=10, h_want=1.0):
    agg = _gap2_by_dh()
    rs = agg.get((d_want, h_want))
    if not rs:
        return None
    n = rs[0]["n"]
    check("t3 tau_sum", abs(rs[0]["tau_sum"] - 1.0) < 5e-3, f"{rs[0]['tau_sum']:.6f}",
          observed=max(abs(rs[0]["tau_sum"] - 1.0), 1e-15), threshold=5e-3)
    Ls = sorted(set(b["L"] for r in rs for b in r["blocks"]))
    thm = _theorem_block(rs[0]["blocks"], n)["L"]
    out = []
    for L in Ls:
        if L == 0:
            continue
        bs = [b for r in rs for b in r["blocks"] if b["L"] == L]
        dl = st.mean(b["delta_L"] for b in bs)
        tn = st.mean(b["T_L_over_n"] for b in bs)
        ce = st.mean(b["certificate"] for b in bs)
        sr = [b["S_dev_ratio"] for b in bs if b["S_dev_ratio"] is not None]
        srs = fmt(st.mean(sr), 3) if sr else ""
        mark = "yes" if L == thm else ""
        out.append(f"{L} & {bs[0]['D_L']:.0f} & {fmt(dl)} & {fmt(tn)} & {fmt(dl/(1+dl))} & "
                   f"{fmt(ce)} & {fmt(dl/(1+dl)**2)} & {srs} & {mark}" + BS + BS)
        if sr and bs[0]["D_L"] > 50:
            check(f"t3 second-moment identity L={L}", abs(st.mean(sr) - 1.0) < 0.06,
                  f"{st.mean(sr):.3f}", observed=max(abs(st.mean(sr) - 1.0), 1e-15), threshold=0.06)
        if bs[0]["D_L"] <= n:
            check(f"t3 leverage capture above the annealed bound L={L}", tn >= dl / (1 + dl),
                  f"T_L/n={tn:.4f} vs delta/(1+delta)={dl/(1+dl):.4f}",
                  observed=tn, threshold=dl / (1 + dl), kind="above")
    macro("TthreeBlockDesigns", str(len(rs)))
    # spreads across designs: T_L/n and the certificate on one hand, the identity ratio on the other
    sd_tc = max(sd([b[k] for r in rs for b in r["blocks"] if b["L"] == L]) for L in Ls if L > 0 for k in ("T_L_over_n", "certificate"))
    sd_id = {L: sd([b["S_dev_ratio"] for r in rs for b in r["blocks"] if b["L"] == L and b["S_dev_ratio"] is not None]) for L in Ls if L > 0}
    macro("TthreeSdMax", f"{sd_tc:.4f}")
    macro("TthreeIdSdFirst", f"{sd_id[min(sd_id)]:.2f}"); macro("TthreeIdSdLast", f"{sd_id[max(sd_id)]:.3f}")
    macro("TthreeIdLfirst", str(min(sd_id))); macro("TthreeIdLlast", str(max(sd_id)))
    return "\n".join(out)


def table_traceform():
    """the two evaluations of V at h = 2: eps*cond(K)^2, the trace form, the factor form, Monte Carlo."""
    agg = _gap2_by_dh()
    ds = sorted(dd for (dd, hh) in agg if hh == 2.0)
    if not ds:
        return None
    out = []
    for dd in ds:
        rs = agg[(dd, 2.0)]
        ek = [r.get("eps_cond2") for r in rs if r.get("eps_cond2") is not None]
        tr = [r.get("V_exact_trace_form") for r in rs if r.get("V_exact_trace_form") is not None]
        fa = [r.get("V_exact_factor_form") for r in rs if r.get("V_exact_factor_form") is not None]
        mc = [r["V_over_sigma2"] for r in rs]
        if not ek:
            # older records without the diagnostic fields: reconstruct eps*cond^2 from the eigenvalues
            ek = [2.2e-16 * (r["K_eig_max"] / r["K_eig_min"]) ** 2 for r in rs]
        m = st.mean(ek)
        eks = f"{m:.1f}" if m < 10 else (f"{m:.0f}" if m < 1000 else sci(m, 1))
        trs = f"{st.mean(tr):.4f}" if tr else "--"
        fas = f"{st.mean(fa):.4f}" if fa else "--"
        out.append(f"{dd} & {len(rs)} & {eks} & {trs} & {fas} & {st.mean(mc):.4f}" + BS + BS)
        if fa:
            check(f"t2 factor form agrees with Monte Carlo at h=2 d={dd}", abs(st.mean(fa) - st.mean(mc)) / st.mean(mc) < 0.02,
                  f"factor {st.mean(fa):.4f} vs MC {st.mean(mc):.4f}", observed=abs(st.mean(fa) - st.mean(mc)) / st.mean(mc), threshold=0.02)
    return "\n".join(out)


def table_band():
    agg = _gap2_by_dh()
    if not agg:
        return None
    out = []
    vh = defaultdict(list)
    ratio = defaultdict(list)
    certs = []
    for (dd, hh) in sorted(agg):
        rs = agg[(dd, hh)]
        n = rs[0]["n"]
        v = [r["V_over_sigma2"] for r in rs]
        gap = max(r["V_rel_gap"] for r in rs)
        check(f"t2 two derivations agree d={dd} h={hh}", gap < 0.05, f"max rel gap {gap:.1e}",
              observed=max(gap, 1e-15), threshold=0.05)
        check(f"t2 bound respected d={dd} h={hh}", st.mean(v) > CTEN,
              f"{st.mean(v):.4f} vs {CTEN:.4f}", observed=st.mean(v), threshold=CTEN, kind="above")
        tb = [_theorem_block(r["blocks"], n) for r in rs]
        dl = st.mean(b["delta_L"] for b in tb)
        ce = [b["certificate"] for b in tb]
        check(f"t3 certificate at the theorem block exceeds 5/36 d={dd} h={hh}", st.mean(ce) > CONE,
              f"{st.mean(ce):.4f} vs {CONE:.4f} at delta={dl:.3f}", observed=st.mean(ce), threshold=CONE, kind="above")
        check(f"t3 theorem block inside (1/5,1] d={dd}", YMIN < dl <= 1.0, f"delta_L={dl:.4f}")
        vh[hh].append(st.mean(v))
        ratio[hh].append(st.mean(v) / CTEN)
        certs.append(st.mean(ce))
        hs = f"{hh:g}"
        out.append(f"{dd} & {hs} & ${fmt(st.mean(v))}" + BS + f"pm{fmt(sd(v))}$ & {len(v)} & "
                   f"{st.mean(v)/CTEN:.2f} & {tb[0]['L']} & {fmt(dl, 3)} & {fmt(st.mean(ce), 3)}" + BS + BS)
    for hh, key in ((0.5, "Half"), (1.0, "One"), (2.0, "Two")):
        if hh in vh:
            macro(f"VhMin{key}", f"{min(vh[hh]):.2f}")
            macro(f"VhMax{key}", f"{max(vh[hh]):.2f}")
            macro(f"RatioMin{key}", f"{min(ratio[hh]):.1f}")
            macro(f"RatioMax{key}", f"{max(ratio[hh]):.1f}")
    macro("CertMin", f"{min(certs):.2f}")
    macro("CertMax", f"{max(certs):.2f}")
    # the two derivations of V: how far apart their MEANS are, per (d, h), in percent
    vg = [100 * abs(st.mean(r["V_over_sigma2"] for r in rs) - st.mean(r["V_over_sigma2_exact"] for r in rs))
          / st.mean(r["V_over_sigma2"] for r in rs) for rs in agg.values()]
    macro("VmeanGapMax", f"{max(vg):.2f}")
    # the two derivations of V, over every design
    allgap = [r["V_rel_gap"] for rs in agg.values() for r in rs]
    macro("VgapMax", sci(max(allgap), 1).strip("$"))
    taus = [r["tau_sum"] for (dd, hh), rs in agg.items() if hh == 0.5 for r in rs]
    macro("TauHalfMin", f"{min(taus):.4f}")
    macro("TauHalfMax", f"{max(taus):.4f}")
    return "\n".join(out)


# ======================================================================= Target 4 (p9_hardedge)
def _hardedge_by_d():
    agg = defaultdict(list)
    for d in REC["p9_hardedge"]:
        for r in d["records"]:
            agg[r["d"]].append(r)
    return agg


def table_hardedge():
    agg = _hardedge_by_d()
    if not agg:
        return None
    out = []
    dratio, bdev = [], []
    for dd in sorted(agg):
        rs = agg[dd]
        t4 = [r["d_tr_A4"] for r in rs]
        op = [r["sqrtd_op_A"] for r in rs]
        ov = [x for r in rs if r.get("ones_overlap") for x in r["ones_overlap"][:3]]
        red = [r["reduction_rel_err"] for r in rs]
        sr = [r["smin_ratio"] for r in rs if r.get("smin_ratio")]
        dratio.append(dd * (1 - st.mean(sr)))
        # the exact moments of the scalar column b: mean over designs against the closed forms
        bm = st.mean(r["b_mean"] for r in rs); bv = st.mean(r["b_var"] for r in rs)
        bdev.append(max(abs(bm - rs[0]["b_mean_pred"]) / abs(rs[0]["b_mean_pred"]), abs(bv - rs[0]["b_var_pred"]) / rs[0]["b_var_pred"]))
        check(f"t3 moments of the scalar column b match the closed forms d={dd}", bdev[-1] < 0.02,
              f"E b {bm:.4f} vs {rs[0]['b_mean_pred']:.4f}, Var b {bv:.4f} vs {rs[0]['b_var_pred']:.4f}",
              observed=bdev[-1], threshold=0.02)
        # The reduction is an exact algebraic identity, so what is checked is floating point; the
        # relative error of a near-zero singular value grows with the conditioning, so gate on the
        # median and carry the tail as a diagnostic.
        check(f"t3 reduction exact d={dd} (median)", st.median(red) < 1e-8,
              f"median {st.median(red):.1e} | tail p99 {quantile(red,0.99):.1e}, max {max(red):.1e}",
              observed=max(st.median(red), 1e-300), threshold=1e-8)
        o = f"{ms(ov)} & {quantile(ov,0.9):.2f}" if ov else "n/a & "
        out.append(f"{dd} & {rs[0]['p']} & {ms(t4)} & {ms(op)} & {o} & {ms(sr, 3)} & {len(rs)}" + BS + BS)
    macro("DratioMin", f"{min(dratio):.1f}"); macro("DratioMax", f"{max(dratio):.1f}")
    macro("BmomWorst", f"{100*max(bdev):.1f}")
    ds = sorted(agg)
    macro("SminRatioFirst", f"{st.mean(r['smin_ratio'] for r in agg[ds[0]]):.3f}")
    macro("SminRatioLast", f"{st.mean(r['smin_ratio'] for r in agg[ds[-1]]):.3f}")
    macro("SminSdFirst", f"{sd([r['smin_ratio'] for r in agg[ds[0]]]):.2f}")
    macro("SminSdLast", f"{sd([r['smin_ratio'] for r in agg[ds[-1]]]):.3f}")
    macro("OverlapFirst", f"{st.mean(x for r in agg[ds[0]] for x in r['ones_overlap'][:3]):.2f}")
    macro("OverlapLast", f"{st.mean(x for r in agg[ds[-1]] for x in r['ones_overlap'][:3]):.2f}")
    macro("HardDmin", str(ds[0])); macro("HardDmax", str(ds[-1]))
    # the exact reduction: median relative error of s_min(Z) against s_min(D[b,H]) at the two ends
    macro("RedMedFirst", sci(st.median(r["reduction_rel_err"] for r in agg[ds[0]]), 1).strip("$"))
    macro("RedMedLast", sci(st.median(r["reduction_rel_err"] for r in agg[ds[-1]]), 1).strip("$"))
    return "\n".join(out)


def goe_null(d):
    """d E Tr(U^4) for U uniform on the unit Frobenius sphere of Sym_d, exactly: U = G/|G|_F with G a
    GOE matrix (E g_ij^2 = 1 off the diagonal, 2 on it), |G|_F^2 ~ 2 chi^2_p, and E Tr G^4 = 2d^3+5d^2+5d."""
    p = d * (d + 1) / 2
    return d * (2 * d ** 3 + 5 * d ** 2 + 5 * d) / (4 * p * (p + 2))


def table_lb():
    """(L-b) at d = 20, 30, 40 with the exact generic-direction null and the fits the prose quotes."""
    agg = _hardedge_by_d()
    ds = [d for d in (20, 30, 40) if d in agg]
    if len(ds) < 3:
        return None
    out, Y, SE = [], [], []
    for dd in ds:
        t4 = [r["d_tr_A4"] for r in agg[dd]]
        m, s = st.mean(t4), se(t4)
        Y.append(m); SE.append(s)
        ex = m - goe_null(dd)
        out.append(f"{dd} & {len(t4)} & ${m:.4f}" + BS + f"pm{s:.4f}$ & {goe_null(dd):.4f} & "
                   f"${ex:.3f}" + BS + f"pm{s:.3f}$ & {ex/s:.0f} & {dd*ex:.2f}" + BS + BS)
    # two-point fit through the ends, weighted three-point fit, and the same for d x excess
    a2 = (Y[0] * ds[0] - Y[2] * ds[2]) / (ds[0] - ds[2]) if False else None
    # solve a + b/d through (ds[0], Y[0]) and (ds[2], Y[2])
    b2 = (Y[0] - Y[2]) / (1 / ds[0] - 1 / ds[2])
    a2 = Y[0] - b2 / ds[0]
    pull = (a2 + b2 / ds[1] - Y[1]) / SE[1]
    beta, ses, chi2, dof = _wls(ds, Y, [1 / s ** 2 for s in SE], 2)
    macro("LbTwoA", f"{a2:.3f}"); macro("LbTwoB", f"{b2:.2f}"); macro("LbMidPull", f"{abs(pull):.2f}")
    macro("LbFitA", f"{beta[0]:.3f}"); macro("LbFitAse", f"{ses[0]:.3f}")
    macro("LbFitB", f"{beta[1]:.2f}"); macro("LbFitBse", f"{ses[1]:.2f}"); macro("LbChi", f"{chi2:.2f}")
    macro("LbFitPull", f"{abs(beta[0]-2.0)/ses[0]:.1f}")
    dex = [ds[i] * (Y[i] - goe_null(ds[i])) for i in range(3)]
    b2e = (dex[0] - dex[2]) / (1 / ds[0] - 1 / ds[2]); a2e = dex[0] - b2e / ds[0]
    pulle = (a2e + b2e / ds[1] - dex[1]) / (ds[1] * SE[1])
    macro("LbExcA", f"{a2e:.2f}"); macro("LbExcB", f"{b2e:.1f}"); macro("LbExcPull", f"{abs(pulle):.2f}")
    macro("LbExcC", f"{round(a2e)}")
    ends = abs(Y[0] - Y[2]) / math.hypot(SE[0], SE[2])
    macro("LbEndsSe", f"{ends:.0f}")
    check("t4 (L-b) flat fit rejected: ends many se apart", ends > 5, f"{ends:.1f} combined se")
    check("t4 (L-b) intercept within 3 se of 2", abs(beta[0] - 2.0) < 3 * ses[0],
          f"a={beta[0]:.3f}+-{ses[0]:.3f}", observed=abs(beta[0] - 2.0), threshold=3 * ses[0])
    return "\n".join(out)


def _ks_to_wishart(vals):
    F = lambda t: 1 - math.exp(-math.sqrt(t) - t / 2)
    v = sorted(vals)
    n = len(v)
    m = 0.0
    for i, x in enumerate(v):
        Fx = F(x)
        m = max(m, abs((i + 1) / n - Fx), abs(i / n - Fx))
    return m


def table_ks():
    agg = _hardedge_by_d()
    if not agg:
        return None
    out = []
    for dd in sorted(agg):
        rs = agg[dd]
        N = len(rs)
        kz = _ks_to_wishart([r["stat_Z"] for r in rs])
        kb = _ks_to_wishart([r["stat_BH"] for r in rs])
        kh = _ks_to_wishart([r["stat_H"] for r in rs])
        crit = 1.36 / math.sqrt(N)
        vz = "rejected" if kz > crit else "consistent"
        vb = "rejected" if kb > crit else "consistent"
        out.append(f"{dd} & {N} & {kz:.3f} & {kb:.3f} & {kh:.3f} & {crit:.3f} & {vz} / {vb}" + BS + BS)
        if N >= 200:
            check(f"t4 reduced matrix consistent with the Wishart hard edge d={dd}", kb < crit,
                  f"KS {kb:.3f} vs critical {crit:.3f}", observed=kb, threshold=crit)
    return "\n".join(out)


def table_invmoment():
    agg = _hardedge_by_d()
    if not agg:
        return None
    out = []
    B = 150
    spread_mean, cv_mean, spread_med, cv_med = [], [], [], []
    for dd in sorted(agg):
        rs = agg[dd]
        inv = [1 / math.sqrt(r["stat_Z"]) for r in rs]
        blocks = [inv[i:i + B] for i in range(0, len(inv) - B + 1, B)]
        if len(blocks) < 2:
            continue
        means = [st.mean(b) for b in blocks]
        meds = [st.median(b) for b in blocks]
        out.append(f"{dd} & {len(blocks)} & {min(means):.1f}--{max(means):.1f} & {sd(means)/st.mean(means):.2f} & "
                   f"{min(meds):.2f}--{max(meds):.2f} & {sd(meds)/st.mean(meds):.2f}" + BS + BS)
        spread_mean.append(max(means) / min(means)); cv_mean.append(sd(means) / st.mean(means))
        spread_med.append(100 * (max(meds) - min(meds)) / min(meds)); cv_med.append(sd(meds) / st.mean(meds))
    macro("InvMeanSpreadMin", f"{min(spread_mean):.0f}"); macro("InvMeanSpreadMax", f"{max(spread_mean):.0f}")
    macro("InvMeanCvMin", f"{min(cv_mean):.2f}"); macro("InvMeanCvMax", f"{max(cv_mean):.2f}")
    macro("InvMedSpreadMin", f"{min(spread_med):.0f}"); macro("InvMedSpreadMax", f"{max(spread_med):.0f}")
    macro("InvMedCvMin", f"{min(cv_med):.2f}"); macro("InvMedCvMax", f"{max(cv_med):.2f}")
    return "\n".join(out)


def table_tail():
    agg = _hardedge_by_d()
    if not agg:
        return None
    F = lambda t: 1 - math.exp(-math.sqrt(t) - t / 2)
    out = []
    for dd in sorted(agg):
        rs = agg[dd]
        if len(rs) < 200:
            continue
        bh = [r["stat_BH"] for r in rs]
        cells = " & ".join(f"{F(quantile(bh, q)):.3f}" for q in (0.02, 0.05, 0.10, 0.20))
        out.append(f"{dd} & {len(rs)} & {cells}" + BS + BS)
    return "\n".join(out)


# ======================================================================= Target 1 (p9_cgec)
def table_cgec():
    agg = defaultdict(list)
    for d in REC["p9_cgec"]:
        for r in d["records"]:
            agg[(r["d"], r["delta"], d.get("normalize_F", 1))].append(r)
    if not agg:
        return None
    out = []
    for (dd, de, nf) in sorted(agg, key=lambda k: (k[0], k[1], -k[2])):
        rs = agg[(dd, de, nf)]
        q = [r["d_q11_var"] for r in rs]
        lg = [r["L_rel_gap"] for r in rs]
        rg = [r["risk_end_to_end_gap"] for r in rs]
        sw = [r["risk_same_w_gap"] for r in rs]
        check(f"t4 leverage variance is Theta(1/d) at d={dd} delta={de} nf={nf}", st.mean(q) < 5.0,
              f"d*Var(q11) = {st.mean(q):.3f}", observed=st.mean(q), threshold=5.0)
        cols = "unit" if nf == 1 else "raw"
        out.append(f"{dd} & {de:g} & {cols} & {ms(q)} & {ms(lg)} & {sci(st.mean(rg))} & {sci(st.mean(sw))} & {len(rs)}" + BS + BS)
    # the same-w risk gap, raw columns over unit columns, per (d, Delta)
    ratios = defaultdict(list)
    for (dd, de, nf) in agg:
        if nf == 0 and (dd, de, 1) in agg:
            ratios[dd].append(st.mean(r["risk_same_w_gap"] for r in agg[(dd, de, 0)]) / st.mean(r["risk_same_w_gap"] for r in agg[(dd, de, 1)]))
    if 64 in ratios:
        macro("SwRatioMinSixtyFour", f"{min(ratios[64]):.1f}"); macro("SwRatioMaxSixtyFour", f"{max(ratios[64]):.1f}")
    if 128 in ratios:
        macro("SwRatioOneTwoEight", f"{st.mean(ratios[128]):.1f}")
    h = REC["p9_cgec"][0]["hermite"]
    # the Hermite constants quoted in the prose come from the record of the Delta = 1/2 lanes
    for d in REC["p9_cgec"]:
        if abs(d["delta"] - 0.5) < 1e-9:
            h = d["hermite"]
            break
    macro("HermCone", f"{h['c1']:.5f}"); macro("HermV", f"{h['V']:.5f}"); macro("HermCtwelve", f"{h['C12']:.5f}")
    macro("HermSh", f"{h['c_shared']:.6f}"); macro("HermPr", f"{h['c_private']:.6f}")
    err = max(abs(h["shared_identity_err"]), abs(h["private_identity_err"]))
    macro("HermErr", sci(err, 0).strip("$") if err > 0 else "0")
    return "\n".join(out)


# ======================================================================= the moment ladder (Veronese only)
CATALAN = {4: 2, 6: 5, 8: 14, 10: 42}


def _moments_by_law():
    agg = defaultdict(list)
    for d in REC["p9_moments"]:
        law = d.get("rowlaw") or "veronese"
        for r in d["records"]:
            agg[(law, r["d"])].append(r)
    return agg


def table_moments():
    agg = _moments_by_law()
    ver = {dd: rs for (law, dd), rs in agg.items() if law == "veronese"}
    if not ver:
        return None
    out = []
    edges = []
    for dd in sorted(ver):
        rs = ver[dd]
        cells = []
        for k in (4, 6, 8, 10):
            v = [x[f"m{k}"] for x in rs if f"m{k}" in x]
            cells.append(mse(v) if v else "n/a")
            if v and len(v) > 4:
                check(f"t4 moment above Catalan d={dd} k={k}", st.mean(v) > CATALAN[k],
                      f"{st.mean(v):.3f} vs {CATALAN[k]}", observed=st.mean(v), threshold=CATALAN[k], kind="above")
        e = [x["edge"] for x in rs]
        edges.append(st.mean(e))
        cells.append(mse(e))
        out.append(f"{dd} & {len(rs)} & " + " & ".join(cells) + BS + BS)
        res = max(x.get("null_residual", 0.0) for x in rs)
        pp = rs[0]["p"]
        tol = 2.2e-16 * pp ** 1.5
        check(f"t4 null residual tiny d={dd}", res < tol,
              f"max ||Zv|| = {res:.1e}, {res / tol:.2f} of the eps p^1.5 scale, over {len(rs)} designs",
              observed=max(res, 1e-300), threshold=tol)
        od = [x["m3_signed"] for x in rs if "m3_signed" in x]
        if len(od) > 4:
            sem = st.stdev(od) / math.sqrt(len(od))
            check(f"t4 odd moment vanishes d={dd}", abs(st.mean(od)) < 4 * sem,
                  f"sqrt(d) Tr(A^3) = {st.mean(od):+.4f} +- {sem:.4f}",
                  observed=abs(st.mean(od)), threshold=4 * sem)
    macro("EdgeMin", f"{min(edges):.3f}"); macro("EdgeMax", f"{max(edges):.3f}")
    macro("MomDmax", str(max(ver)))
    m4 = [x["m4"] for x in ver[max(ver)]]
    macro("MomLastMfour", f"{st.mean(m4):.3f}"); macro("MomLastPull", f"{(st.mean(m4)-2)/se(m4):.0f}")
    ratio = [st.mean([x["edge"] ** 2 / x["m4"] for x in ver[dd]]) for dd in sorted(ver)]
    macro("OpRatioFirst", f"{ratio[0]:.2f}"); macro("OpRatioLast", f"{ratio[-1]:.2f}")
    return "\n".join(out)


def table_control():
    """the pipeline control: Gaussian and Rademacher rows against Veronese rows at the same d."""
    agg = _moments_by_law()
    ds = sorted(dd for (law, dd) in agg if law == "gauss")
    if not ds:
        return None
    name = {"veronese": "Veronese", "gauss": "Gaussian rows", "rademacher": "Rademacher rows"}
    out = []
    worst = 0.0
    for dd in ds:
        for law in ("veronese", "gauss", "rademacher"):
            rs = agg.get((law, dd))
            if not rs:
                continue
            cells = [mse([x[f"m{k}"] for x in rs]) for k in (4, 6, 8, 10)]
            cells.append(mse([x["edge"] for x in rs]))
            out.append(f"{dd} & {name[law]} & {len(rs)} & " + " & ".join(cells) + BS + BS)
            if law != "veronese" and len(rs) > 20:
                v = [x["m4"] for x in rs]
                worst = max(worst, abs(st.mean(v) - goe_null(dd)) / se(v))
                check(f"t4 control rows give the generic fourth moment d={dd} {law}",
                      abs(st.mean(v) - goe_null(dd)) < 4 * se(v),
                      f"{st.mean(v):.4f}+-{se(v):.4f} vs exact {goe_null(dd):.4f}",
                      observed=abs(st.mean(v) - goe_null(dd)), threshold=4 * se(v))
    macro("ControlWorstSe", f"{worst:.1f}")
    return "\n".join(out)


def table_kssemi():
    """Kolmogorov--Smirnov distance of sqrt(d) A's spectrum to the semicircle, from the records that
    carry it, per row law."""
    agg = _moments_by_law()
    name = {"veronese": "Veronese", "gauss": "Gaussian rows", "rademacher": "Rademacher rows"}
    out = []
    ratio = []
    for (law, dd) in sorted(agg, key=lambda k: (k[1], k[0] != "veronese", k[0])):
        rs = [r for r in agg[(law, dd)] if "ks_semicircle" in r]
        if not rs:
            continue
        v = [r["ks_semicircle"] for r in rs]
        out.append(f"{dd} & {name[law]} & {len(rs)} & {mse(v, 4)}" + BS + BS)
        if law == "gauss":
            vv = [r["ks_semicircle"] for r in agg[("veronese", dd)] if "ks_semicircle" in r]
            if vv:
                ratio.append(st.mean(vv) / st.mean(v))
    if not out:
        return None
    if ratio:
        macro("KsRatioMin", f"{min(ratio):.2f}"); macro("KsRatioMax", f"{max(ratio):.2f}")
    return "\n".join(out)


def table_momentfit():
    """The intercept of the Veronese moment ladder, weighted by the inverse squared standard errors:
    a two-term fit a + b/d and a three-term fit a + b/d + e/d^2 over every dimension measured."""
    agg = _moments_by_law()
    ver = {dd: rs for (law, dd), rs in agg.items() if law == "veronese"}
    if not ver:
        return None
    key = {2: "m4", 3: "m6", 4: "m8", 5: "m10"}
    cat = {2: 2.0, 3: 5.0, 4: 14.0, 5: 42.0}
    ds = sorted(ver)
    out = []
    worst = 0.0
    for k in (2, 3, 4, 5):
        Y = [st.mean([x[key[k]] for x in ver[d]]) for d in ds]
        SE = [se([x[key[k]] for x in ver[d]]) for d in ds]
        W = [1 / s ** 2 for s in SE]
        b2, s2, c2, dof2 = _wls(ds, Y, W, 2)
        b3, s3, c3, dof3 = _wls(ds, Y, W, 3)
        pull2 = (b2[0] - cat[k]) / s2[0]
        pull3 = (b3[0] - cat[k]) / s3[0]
        worst = max(worst, abs(pull3))
        out.append(f"{k} & {cat[k]:.0f} & ${b2[0]:.3f}" + BS + f"pm{s2[0]:.3f}$ & {pull2:+.1f} & {c2:.1f}/{dof2} & "
                   f"${b3[0]:.3f}" + BS + f"pm{s3[0]:.3f}$ & ${b3[1]:.1f}" + BS + f"pm{s3[1]:.1f}$ & {pull3:+.1f} & {c3:.1f}/{dof3}" + BS + BS)
        if k == 2:
            macro("MomFitB", f"{b3[1]:.1f}"); macro("MomFitBse", f"{s3[1]:.1f}")
        if k == 5:
            macro("MomChiTwoLast", f"{c2:.1f}"); macro("MomChiDof", str(dof2))
    macro("MomDmin", str(min(ds))); macro("MomFitWorst", f"{worst:.1f}")
    check("t4 three-term intercept within 2 se of Catalan (all k)", worst < 2.0,
          f"worst intercept is {worst:.1f} s.e. from its Catalan number", observed=worst, threshold=2.0)
    return "\n".join(out)


# ======================================================================= Target 5 (p9_prune)
LAWNAME = {"rademacher": r"Rademacher", "gauss": r"Gaussian", "bern02": r"Bernoulli$(0.2)$",
           "t5": r"Student $t_5$", "exp1": r"exponential"}
COVERED = {"rademacher", "gauss"}          # symmetric and concentrated: inside the theorem


def _prune_blocks():
    agg = defaultdict(list)
    for d in REC["p9_prune"]:
        if d.get("mode") != "block":
            continue
        for r in d["records"]:
            agg[(r["law"], r["n"], r["r"], r.get("aspect", 0.5))].append(r)
    return agg


def table_prune_block():
    agg = _prune_blocks()
    if not agg:
        return None
    out = []
    ratios = defaultdict(list)
    for key in sorted(agg, key=lambda k: (k[0] not in COVERED, k[0], k[3], k[1], k[2])):
        law, nn, rr, asp = key
        rs = agg[key]
        be = [x["beta"] for x in rs]
        ra = [x["ratio"] for x in rs]
        ratios[law] += ra
        mark = "" if law in COVERED else "$^{" + BS + "dagger}$"
        asps = "" if abs(asp - 0.5) < 1e-9 else f", aspect {asp:g}"
        out.append(f"{LAWNAME.get(law, law)}{mark}{asps} & {nn} & {rr} & {ms(be)} & {ms(ra)} & {len(rs)}" + BS + BS)
    for law, v in sorted(ratios.items()):
        if len(v) >= 40:
            check(f"p19 block ratio bounded, {law}", st.mean(v) < 3.0,
                  f"mean beta/scale = {st.mean(v):.3f} over {len(v)} designs", observed=st.mean(v), threshold=3.0)
    # the split of beta into its three blocks, at aspect 1/2
    shares = defaultdict(list)
    for key, rs in agg.items():
        if abs(key[3] - 0.5) > 1e-9:
            continue
        for nm in ("A", "D", "B"):
            shares[nm].append(st.mean(x["beta_" + nm] / x["beta"] for x in rs))
    for nm in ("A", "D", "B"):
        if shares[nm]:
            macro(f"Share{nm}Min", f"{min(shares[nm]):.2f}"); macro(f"Share{nm}Max", f"{max(shares[nm]):.2f}")
    # the two laws the symmetry question compares, at n = 1000
    def b(law, r):
        rs = agg.get((law, 1000, r, 0.5))
        return rs
    for r, key in ((4, "Four"), (16, "Sixteen"), (256, "TwoFiveSix")):
        rb, rr_ = b("bern02", r), b("rademacher", r)
        if rb and rr_:
            macro(f"BetaBern{key}", f"{st.mean([x['beta'] for x in rb]):.4f}" + BS + f"pm{se([x['beta'] for x in rb]):.4f}")
            macro(f"BetaRad{key}", f"{st.mean([x['beta'] for x in rr_]):.4f}" + BS + f"pm{se([x['beta'] for x in rr_]):.4f}")
            macro(f"NBern{key}", str(len(rb))); macro(f"NRad{key}", str(len(rr_)))
    # exponents of beta in r at fixed n = 1000
    def expo(law, r1, r2):
        x1, x2 = b(law, r1), b(law, r2)
        if not (x1 and x2):
            return None
        return math.log(st.mean([x["beta"] for x in x2]) / st.mean([x["beta"] for x in x1])) / math.log(r2 / r1)
    for law, key in (("rademacher", "Rad"), ("bern02", "Bern")):
        for (r1, r2, nm) in ((4, 16, "A"), (16, 64, "B"), (64, 256, "C"), (16, 256, "D")):
            e = expo(law, r1, r2)
            if e is not None:
                macro(f"Exp{key}{nm}", f"{e:.2f}")
    return "\n".join(out)


def table_ray():
    """Rademacher rows along two rays of fixed r/n, and the two-term law beta -> sqrt(r/n) + c r/n."""
    agg = _prune_blocks()
    rows = [(16, 1000), (32, 2000), (64, 4000), (64, 1000), (128, 2000), (256, 4000)]
    if not all(("rademacher", n, r, 0.5) in agg for r, n in rows):
        return None
    out = []
    cs = []
    for r, n in rows:
        rs = agg[("rademacher", n, r, 0.5)]
        be = [x["beta"] for x in rs]
        m = st.mean(be)
        ex = m - math.sqrt(r / n)
        out.append(f"{r} & {n} & {r/n:.3f} & ${m:.4f}" + BS + f"pm{se(be):.4f}$ & {math.sqrt(r/n):.4f} & "
                   f"{ex:+.4f} & {ex/(r/n):.2f} & {len(rs)}" + BS + BS)
        if n == 4000:
            cs.append(ex / (r / n))
    c = st.mean(cs)
    macro("RayC", f"{c:.2f}")
    # the law fitted on the two n = 4000 points, tested on the points it did not see
    for (r, n, key) in ((32, 2000, "A"), (128, 2000, "B"), (16, 4000, "C")):
        rs = agg.get(("rademacher", n, r, 0.5))
        if rs:
            m = st.mean([x["beta"] for x in rs])
            pred = math.sqrt(r / n) + c * r / n
            macro(f"RayPred{key}", f"{pred:.4f}"); macro(f"RayMeas{key}", f"{m:.4f}")
            macro(f"RayOff{key}", f"{100*abs(pred-m)/m:.1f}")
    check("p19 fixed-ratio excess over sqrt(r/n) is of order r/n", 0.5 < c < 2.0, f"c = {c:.2f}")
    return "\n".join(out)


def table_prune_adapt():
    agg = defaultdict(list)
    for d in REC["p9_prune"]:
        if d.get("mode") != "adapt":
            continue
        for r in d["records"]:
            agg[(r["n"], r["theta"])].append(r)
    if not agg:
        return None
    out = []
    ks_gap, ov_ad = [], []
    for (nn, th) in sorted(agg):
        rs = agg[(nn, th)]
        io = [x["indep_outlier"] for x in rs]
        iu = [x["indep_overlap_u"] for x in rs]
        ao = [x["adapt_outlier"] for x in rs]
        au = [x["adapt_overlap_u"] for x in rs]
        ki = [x["indep_ks_bulk"] for x in rs]
        ka = [x["adapt_ks_bulk"] for x in rs]
        ks_gap += [abs(p - q) for p, q in zip(ki, ka)]
        ov_ad += au
        out.append(f"{nn} & {th:g} & {ms(io)} & {ms(iu, 3)} & {ms(ao)} & {ms(au, 3)} & "
                   f"{nn*st.mean(ki):.2f} & {nn*st.mean(ka):.2f} & {len(rs)}" + BS + BS)
    if len(ov_ad) >= 20:
        check("p19 adaptive spike keeps the whole top vector", min(ov_ad) > 0.98,
              f"min overlap over {len(ov_ad)} designs = {min(ov_ad):.4f}", observed=1.0 - min(ov_ad), threshold=0.02)
        check("p19 the bulk cannot tell the two arms apart", st.mean(ks_gap) < 5e-3,
              f"mean |KS_indep - KS_adapt| = {st.mean(ks_gap):.2e} over {len(ks_gap)} designs",
              observed=st.mean(ks_gap), threshold=5e-3)
    return "\n".join(out)


# ======================================================================= the identity (p9_correction)
def _corr_groups():
    by = defaultdict(list)
    for d in REC["p9_correction"]:
        lab = d.get("corpus", "?")
        if lab == "emit":
            lab += " " + d.get("comp", "")
        elif lab == "oco2":
            lab += " " + d.get("band", "")
        elif lab == "well":
            lab += " " + d.get("well_name", "")[:14]
        by[lab].append(d)
    return by


def table_corr():
    by = _corr_groups()
    if not by:
        return None
    out = []
    worst_all = 0.0
    # the two arms: R1_con is the correction fitted to the residuals against the deployed mean's own
    # training-row predictions (the arm the identity certifies); R1_act the one fitted to the
    # out-of-fold residuals, the labels the pipeline fits to.  Both are scored on the same test block.
    oof_at, oof_best, oof_phys_at, gam_eta = defaultdict(list), defaultdict(list), [], []
    transfer_flag = transfer_recomp = 0
    for lab in sorted(by):
        ds = by[lab]
        gains, pgains, hurts, idents = [], [], 0, []
        for d in ds:
            rows = d.get("rows", [])
            if not rows:
                continue
            best = min(rows, key=lambda r: r["R1_con"])
            R0 = d["R0"]
            gains.append(100 * (R0 - best["R1_con"]) / max(R0, 1e-300))
            pgains.append(100 * (best["phys_mean"] - best["phys_con"]) / max(best["phys_mean"], 1e-300))
            hurts += sum(1 for r in rows if not r["helps"])
            idents.append(max(abs(r["identity_rel_err"]) for r in rows))
            oof_at[lab].append(100 * (R0 - best["R1_act"]) / max(R0, 1e-300))
            oof_best[lab].append(max(100 * (R0 - r["R1_act"]) / max(R0, 1e-300) for r in rows))
            oof_phys_at.append((100 * (best["phys_mean"] - best["phys_act"]) / max(best["phys_mean"], 1e-300), oof_at[lab][-1]))
            transfer_flag += sum(1 for r in rows if r["gamma_gt_eta"])
            transfer_recomp += sum(1 for r in rows if math.sqrt(R0) - math.sqrt(r["R1_con"]) > r["eta"])
            gam_eta.extend((math.sqrt(R0) - math.sqrt(r["R1_con"]), r["eta"]) for r in rows)
        if not gains:
            continue
        check(f"t5 identity exact {lab}", max(idents) < 1e-9, f"{max(idents):.1e}",
              observed=max(max(idents), 1e-300), threshold=1e-9)
        worst_all = max(worst_all, max(idents))
        out.append(f"{lab.replace('_',' ')} & {len(ds)} & ${st.mean(gains):.1f}" + BS + f"pm{sd(gains):.1f}$ & "
                   f"${st.mean(pgains):.1f}" + BS + f"pm{sd(pgains):.1f}$ & {hurts} / {8*len(ds)} & "
                   f"${st.mean(oof_at[lab]):.1f}" + BS + f"pm{sd(oof_at[lab]):.1f}$ & "
                   f"${st.mean(oof_best[lab]):.1f}" + BS + f"pm{sd(oof_best[lab]):.1f}$ & {sci(max(idents), 0)}" + BS + BS)
        key = lab.replace(" ", "").replace("2", "Two").replace("1", "One").replace("3", "Three").replace("4", "Four")
        key = "".join(ch for ch in key if ch.isalpha())
        macro(f"Gain{key}", f"{st.mean(gains):.1f}"); macro(f"PGain{key}", f"{st.mean(pgains):.1f}")
        macro(f"Hurt{key}", f"{hurts}"); macro(f"Lanes{key}", f"{len(ds)}")
    # the operating point the prose quotes: an 8,000-row kernel stage and four folds on every lane
    ops = {(d.get("nfit"), d.get("folds")) for d in REC["p9_correction"] if d.get("rows")}
    check("t5 operating point: nfit 8000 and four folds on every lane", ops == {(8000, 4)}, str(sorted(ops)))
    # the transfer condition gamma > eta of the mismatch bound, counted two ways
    npairs = sum(len(d.get("rows", [])) for d in REC["p9_correction"])
    check("t5 transfer count: recorded flag equals the recomputed gamma > eta", transfer_flag == transfer_recomp,
          f"flag {transfer_flag}, recomputed {transfer_recomp}")
    macro("TransferPairs", str(transfer_flag)); macro("TransferLanes",
          str(sum(1 for d in REC["p9_correction"] if any(r["gamma_gt_eta"] for r in d.get("rows", [])))))
    pos = [(g, e) for g, e in gam_eta if g > 0]
    if pos:
        macro("GammaMax", f"{max(g for g, e in pos):.2f}")
        macro("TransferSlackMin", f"{min(e / g for g, e in pos):.1f}")
        check("t5 transfer condition fails on every pair (eta > gamma wherever gamma > 0)",
              min(e / g for g, e in pos) > 1, f"min eta/gamma {min(e / g for g, e in pos):.2f}",
              observed=min(e / g for g, e in pos), threshold=1, kind="min")
    # the out-of-fold arm across the corpora
    emit123 = [g for lab in ("emit Y1", "emit Y2", "emit Y3") for g in oof_best.get(lab, [])]
    if emit123:
        macro("OofBestEmitMax", f"{max(emit123):.1f}")
    if oof_best.get("emit Y4"):
        macro("OofBestYfourMax", f"{max(oof_best['emit Y4']):.1f}")
    oco_best = [g for lab in oof_best if lab.startswith("oco2") for g in oof_best[lab]]
    if oco_best:
        macro("OofBestOcoMin", f"{min(oco_best):.1f}"); macro("OofBestOcoMax", f"{max(oco_best):.1f}")
    if oof_best.get("emit Y4"):
        macro("OofBestYfourNeg", str(sum(1 for g in oof_best["emit Y4"] if g < 0)))
    emit_at = [g for lab in ("emit Y1", "emit Y2", "emit Y3") for g in oof_at.get(lab, [])]
    if emit_at:
        # the arm loses risk at lambda*: quote the rise in risk as a positive number
        macro("OofAtEmitRiseMin", f"{-max(emit_at):.0f}"); macro("OofAtEmitRiseMax", f"{-min(emit_at):.0f}")
    emit_all_at = [g for lab in oof_at if lab.startswith("emit") for g in oof_at[lab]]
    oco_at = [g for lab in oof_at if lab.startswith("oco2") for g in oof_at[lab]]
    if emit_all_at:
        check("t5 o.o.f. arm at lambda* raises the risk on every EMIT lane", max(emit_all_at) < 0,
              f"largest gain {max(emit_all_at):.2f} pct")
    if oco_at:
        macro("OofAtOcoNeg", str(sum(1 for g in oco_at if g < 0))); macro("OofAtOcoLanes", str(len(oco_at)))
    if oof_phys_at:
        macro("OofPhysNeg", str(sum(1 for p, g in oof_phys_at if p < 0)))
        agree = sum(1 for p, g in oof_phys_at if (p > 0) == (g > 0))
        macro("OofPhysSignAgree", str(agree))
        check("t5 o.o.f. physical change agrees in sign with its squared-risk change on every lane",
              agree == len(oof_phys_at), f"{agree} of {len(oof_phys_at)}")
        macro("OofPhysWorseMax", f"{-min(p for p, g in oof_phys_at):.0f}")
    macro("IdentWorst", sci(worst_all, 0).strip("$"))
    macro("CorrLanes", str(len(REC["p9_correction"])))
    macro("CorrPairs", str(sum(len(d.get("rows", [])) for d in REC["p9_correction"])))
    # physical error transfer, EMIT components with a positive gain
    ag = pg = 0.0; k = 0; agree = tot = 0
    for d in REC["p9_correction"]:
        rows = d.get("rows", [])
        if not rows:
            continue
        best = min(rows, key=lambda r: r["R1_con"])
        g = (d["R0"] - best["R1_con"]) / d["R0"]
        p = (best["phys_mean"] - best["phys_con"]) / best["phys_mean"]
        tot += 1; agree += (g > 0) == (p > 0)
        if d["corpus"] == "emit" and d.get("comp") in ("Y1", "Y2", "Y3"):
            ag += g; pg += p; k += 1
    macro("SignAgree", f"{agree}"); macro("SignTot", f"{tot}")
    if k:
        macro("EmitSqGain", f"{100*ag/k:.1f}"); macro("EmitPhysGain", f"{100*pg/k:.1f}"); macro("EmitGainLanes", str(k))
    # the mismatch bound at the best ridge over every lane
    etas, slack = [], []
    for d in REC["p9_correction"]:
        rows = d.get("rows", [])
        if rows:
            best = min(rows, key=lambda r: r["R1_con"])
            etas.append(best["eta"]); slack.append(best["eta_bound"] / max(best["eta"], 1e-300))
    if etas:
        macro("EtaMin", f"{min(etas):.2f}"); macro("EtaMax", f"{max(etas):.2f}")
        macro("SlackMin", f"{min(slack):.0f}"); macro("SlackMax", f"{max(slack):.0f}")
        check("t5 mismatch bound holds at the best ridge (all lanes)", min(slack) > 1.0, f"min slack {min(slack):.0f}")
    return "\n".join(out)


def table_signs():
    """lanes with a positive margin at each ridge, per component."""
    by = _corr_groups()
    if not by:
        return None
    lams = None
    out = []
    for lab in sorted(by):
        ds = by[lab]
        lams = sorted(set(r["lam"] for d in ds for r in d.get("rows", [])))
        cells = []
        for lam in lams:
            cells.append(str(sum(1 for d in ds for r in d.get("rows", []) if r["lam"] == lam and r["helps"])))
        out.append(f"{lab.replace('_',' ')} & {len(ds)} & " + " & ".join(cells) + BS + BS)
    # the Y3 pattern: lanes negative at each of the three smallest ridges
    y3 = by.get("emit Y3", [])
    for lam, key in ((1e-8, "A"), (1e-7, "B"), (1e-6, "C")):
        macro(f"YthreeNeg{key}", str(sum(1 for d in y3 for r in d["rows"] if abs(r["lam"] - lam) < 1e-15 and not r["helps"])))
    # OCO-2: the margin relative to the mean's own risk from 1e-5 up, in percent
    oco = [d for lab, ds in by.items() if lab.startswith("oco2") for d in ds]
    big = [100 * abs(r["sign_margin"]) / d["R0"] for d in oco for r in d["rows"] if r["lam"] >= 1e-4 - 1e-20]
    small_pos = sum(1 for d in oco for r in d["rows"] if r["lam"] <= 1e-6 + 1e-20 and r["helps"])
    neg5 = sum(1 for d in oco for r in d["rows"] if abs(r["lam"] - 1e-5) < 1e-20 and not r["helps"])
    if big:
        macro("OcoMarginMaxFour", f"{max(big):.1f}")
    macro("OcoLanes", str(len(oco))); macro("OcoNegFive", str(neg5))
    check("t5 OCO-2 margin negative at every ridge up to 1e-6 on every lane", small_pos == 0, f"{small_pos} positive pairs")
    return "\n".join(out)


# ======================================================================= the dimension gap (p9_gap)
def _gap_blocks():
    agg = defaultdict(list)
    for rec in REC["p9_gap"]:
        for r in rec["records"]:
            agg[(r["d"], r["h"], r["k"])].append(r)
    return agg


def table_gap(d_want=8, h_want=0.5, field="risk_noise"):
    agg = _gap_blocks()
    ks = sorted(k for (d, h, k) in agg if d == d_want and h == h_want)
    if not ks:
        return None
    LADDER = [0.02, 0.05, 0.10, 0.20, 0.30]
    out = []
    for k in ks:
        by = defaultdict(list)
        for r in agg[(d_want, h_want, k)]:
            by[round(r["delta"], 2)].append(r[field])
        if len(by) < 3:
            continue
        cells = [fmt(st.mean(by[x]), 3) if x in by else "" for x in LADDER]
        out.append(f"{k} & {agg[(d_want, h_want, k)][0]['N_k']:.0f} & " + " & ".join(cells) + BS + BS)
    return "\n".join(out)


def table_gapiso():
    return table_gap(field="tail_isotropy")


def table_gapdeep():
    """the blocks whose ladder reaches delta >= 0.44: the mean noise risk out to delta = 0.6."""
    agg = _gap_blocks()
    if not agg:
        return None
    LADDER = [0.02, 0.05, 0.10, 0.20, 0.30, 0.44, 0.60]
    out = []
    for (dd, hh, k) in sorted(agg):
        by = defaultdict(list)
        for r in agg[(dd, hh, k)]:
            by[round(r["delta"], 2)].append(r["risk_noise"])
        if max(by) < 0.44 or len(by) < 4:
            continue
        cells = [fmt(st.mean(by[x]), 3) if x in by else "--" for x in LADDER]
        out.append(f"{dd} & {k} & {agg[(dd, hh, k)][0]['N_k']:.0f} & " + " & ".join(cells) + BS + BS)
    return "\n".join(out) if out else None


def table_gapsum():
    """within-block monotonicity at every dimension: inverted pairs, and the isotropy's."""
    agg = _gap_blocks()
    if not agg:
        return None
    ds = sorted(set(d for (d, h, k) in agg))
    out = []
    tot_inv = tot_pairs = tot_blocks = 0
    inv_nk, inv_diff, inv_risk = [], [], []          # where the inverted pairs live (cells with 4 designs)
    for dd in ds:
        blocks = inv = pairs = iso_mono = 0
        cells = set()
        where = []
        for k in sorted(k for (d, h, k) in agg if d == dd):
            by = defaultdict(list); iso = defaultdict(list)
            for r in agg[(dd, 0.5, k)]:
                by[round(r["delta"], 2)].append(r["risk_noise"]); iso[round(r["delta"], 2)].append(r["tail_isotropy"])
            if len(by) < 3:
                continue
            xs = sorted(by)
            m = [st.mean(by[x]) for x in xs]; mi = [st.mean(iso[x]) for x in xs]
            cells.update(len(by[x]) for x in xs)
            blocks += 1
            thisinv = sum(1 for i in range(len(m)) for j in range(i + 1, len(m)) if m[i] < m[j])
            if thisinv and min(len(by[x]) for x in xs) >= 3:
                inv_nk.append(agg[(dd, 0.5, k)][0]["N_k"])
                inv_diff += [m[j] - m[i] for i in range(len(m)) for j in range(i + 1, len(m)) if m[i] < m[j]]
                inv_risk += [m[j] for i in range(len(m)) for j in range(i + 1, len(m)) if m[i] < m[j]]
            inv += thisinv
            pairs += len(m) * (len(m) - 1) // 2
            iso_mono += all(mi[i] > mi[i + 1] for i in range(len(mi) - 1))
            if thisinv:
                where.append(f"$k={k}$")
        tot_inv += inv; tot_pairs += pairs; tot_blocks += blocks
        cs = "/".join(str(c) for c in sorted(cells))
        out.append(f"{dd} & {blocks} & {cs} & {inv} / {pairs} & {iso_mono} / {blocks} & {', '.join(where) if where else '--'}" + BS + BS)
    macro("GapBlocks", str(tot_blocks)); macro("GapInv", str(tot_inv)); macro("GapPairs", str(tot_pairs))
    macro("GapDims", str(len(ds)))
    if inv_nk:
        macro("GapInvNmax", f"{max(inv_nk):.0f}"); macro("GapInvDiffMax", f"{max(inv_diff):.3f}")
        macro("GapInvRiskMax", f"{max(inv_risk):.2f}")
    check("gap: risk falls as the gap widens within blocks (inversions rare)", tot_inv <= 0.06 * tot_pairs,
          f"{tot_inv} inverted pairs over {tot_pairs} pairs in {tot_blocks} blocks", observed=tot_inv / max(tot_pairs, 1), threshold=0.06)
    return "\n".join(out)


# ======================================================================= the regularisation block
def _corpus_key(r):
    c = str(r.get("corpus", "?")).replace("_", BS + "_")
    comp = str(r.get("comp") or r.get("band") or r.get("table") or r.get("well") or "").replace("_", BS + "_")
    if c in ("emit", "oco2") and comp:
        return c, comp
    return c, ""


def _msd(v, n=2):
    if len(v) == 1:
        return f"{v[0]:.{n}f}"
    return f"${st.mean(v):.{n}f}" + BS + f"pm{st.stdev(v):.{n}f}$"


def table_regpath():
    agg = defaultdict(list)
    for d in REC["p9_regpath"]:
        for r in d["records"]:
            if abs(r.get("noise", 0.0)) < 1e-12:
                agg[(_corpus_key(r), r["n"])].append(r)
    if not agg:
        return None
    out = []
    for ck in sorted({k[0] for k in agg}):
        nmax = max(n for (c, n) in agg if c == ck)
        rs = agg[(ck, nmax)]
        al = [x["alpha_hat"] for x in rs if x["alpha_hat"] == x["alpha_hat"]]
        rr = [x["r_hat"] for x in rs if x["r_hat"] == x["r_hat"]]
        ex = [x["crossover_exponent"] for x in rs if x["crossover_exponent"] == x["crossover_exponent"]]
        ratio = [x["interp_over_best"] for x in rs]
        lam = st.median([math.log10(float(x["lam_best"])) for x in rs])
        out.append(f"{ck[0]} & {ck[1]} & {nmax} & {_msd(al) if al else '--'} & {_msd(rr) if rr else '--'} & "
                   f"{_msd(ex) if ex else '--'} & $10^{{{lam:.0f}}}$ & {_msd(ratio)} & {len(rs)}" + BS + BS)
        if ck[0] == "burgers" and al and rr:
            a_, r_ = st.mean(al), st.mean(rr)
            macro("BurgAlpha", f"{a_:.2f}"); macro("BurgR", f"{r_:.2f}"); macro("BurgExp", f"{st.mean(ex):.2f}")
            macro("BurgFactor", f"{10**st.mean(ex):.0f}")
            # Cui et al.: the noisy optimal rate takes over at n_2^* ~ sigma^{-max(2, 1/(alpha min(r,1)))}
            macro("BurgTakeoverExp", f"{max(2.0, st.mean(ex)):.0f}")
            macro("BurgTakeover", f"{10**max(2.0, st.mean(ex)):.0f}")
            macro("BurgRate", f"{2*a_*min(r_,1)/(1+2*a_*min(r_,1)):.2f}")
    return "\n".join(out)


def table_gatemlp():
    agg = defaultdict(list)
    for d in REC["p9_gate"]:
        for r in d["records"]:
            agg[(_corpus_key(r), r.get("mean", "?"), float(r.get("wd", 0.0)) if r.get("mean") == "mlp" else None)].append(r)
    if not agg:
        return None
    out = []
    for key in sorted(agg, key=lambda k: (k[0], k[1] != "const", k[1], k[2] or 0.0)):
        rs = agg[key]
        th = [x["theta_hat"] for x in rs]
        cap = [x["gain_captured"] for x in rs if x["gain_captured"] == x["gain_captured"]]
        gw = sum(bool(x["gated_worsens"]) for x in rs)
        fw = sum(bool(x["full_worsens"]) for x in rs)
        w = "--" if key[2] is None else (f"$10^{{{math.log10(key[2]):.0f}}}$" if key[2] > 0 else "0")
        out.append(f"{key[0][0]} {key[0][1]} & {key[1]} & {w} & {_msd(th)} & {_msd(cap) if cap else '--'} & "
                   f"{gw} / {fw} & {len(rs)}" + BS + BS)
        if key[0][0] == "burgers" and key[1] == "mlp":
            x = rs[0]
            macro("GateTrainMse", sci(x["mean_train_mse"], 1).strip("$"))
            macro("GateTheta", f"{x['theta_hat']:.2f}"); macro("GateCaptured", f"{100*x['gain_captured']:.0f}")
            macro("GateRiskMean", sci(x["risk_mean"], 1).strip("$")); macro("GateRiskGated", sci(x["risk_gated"], 1).strip("$"))
            macro("GateRiskBest", sci(x["risk_best"], 1).strip("$"))
        if key[0][0].startswith("caltech") and key[1] == "const":
            x = rs[0]
            macro("AdvRiskMean", f"{x['risk_mean']:.2f}"); macro("AdvRiskGated", f"{x['risk_gated']:.3f}"); macro("AdvRiskBest", f"{x['risk_best']:.3f}")
    return "\n".join(out)


def table_newcorp():
    agg = defaultdict(list)
    for d in REC["p9_delta"]:
        for r in d["records"]:
            if abs(r.get("noise", 0.0)) < 1e-12:
                agg[(_corpus_key(r), r["n"])].append(r)
    if not agg:
        return None
    rows = []
    for ck in sorted({k[0] for k in agg}):
        nmax = max(n for (c, n) in agg if c == ck)
        rs = agg[(ck, nmax)]
        rows.append((st.mean([x["delta_eff"] for x in rs]), ck, nmax, rs))
    rows.sort()
    out = []
    for dmean, ck, nmax, rs in rows:
        d_eff = st.mean([x["d_eff0"] for x in rs]); p_eff = st.mean([x["participation"] for x in rs])
        adv = [x["interp_advantage"] for x in rs]
        out.append(f"{ck[0]} & {ck[1]} & {nmax} & {d_eff:.0f} & {p_eff:.1f} & {_msd([x['delta_eff'] for x in rs], 3)} & "
                   f"{_msd(adv)} & {len(rs)}" + BS + BS)
        if ck[0].startswith("caltech"):
            x = rs[0]
            macro("AdvBestLam", f"10^{{{math.log10(float(x['lam_best'])):.0f}}}")
            macro("AdvRiskRidge", f"{x['risk_ridge']:.4f}"); macro("AdvRiskInterp", f"{x['risk_interp']:.4f}")
            macro("AdvAdvantage", f"{x['interp_advantage']:.2f}"); macro("AdvDeltaEff", f"{x['delta_eff']:.2f}")
    # cross-driver sign check against the regularisation path at noise 0
    rp = defaultdict(list)
    for d in REC["p9_regpath"]:
        for r in d["records"]:
            if abs(r.get("noise", 0.0)) < 1e-12:
                rp[_corpus_key(r)].append(r["interp_over_best"])
    agree = tot = 0
    for dmean, ck, nmax, rs in rows:
        if ck in rp:
            adv = st.mean([x["interp_advantage"] for x in rs]); q = st.median(rp[ck])
            tot += 1
            agree += 1 if (abs(adv) < 0.3 and abs(q - 1) < 0.02) else int((adv < 0) == (q > 1))
    if tot:
        check("reg two drivers agree on the sign of the interpolation advantage", agree == tot, f"{agree} of {tot} corpora")
    return "\n".join(out)


def table_crossover():
    agg = defaultdict(list)
    for d in REC["p9_regpath"]:
        for r in d["records"]:
            agg[(_corpus_key(r), round(float(r.get("noise", 0.0)), 4), r["n"])].append(r["interp_over_best"])
    if not agg:
        return None
    levels = [0.0, 0.03, 0.1, 0.3]
    out = []
    for ck in sorted({k[0] for k in agg}):
        ns_by_level = {lv: {n for (c, lv2, n) in agg if c == ck and lv2 == lv} for lv in levels}
        common = set.intersection(*[v for v in ns_by_level.values() if v]) if any(ns_by_level.values()) else set()
        if not common:
            common = ns_by_level[0.0]
        if not common:
            continue
        nmax = max(common)
        cells = []
        for lv in levels:
            v = agg.get((ck, lv, nmax))
            cells.append(f"{st.median(v):.2f}" if v and st.median(v) < 100 else (sci(st.median(v)) if v else "--"))
        out.append(f"{ck[0]} & {ck[1]} & {nmax} & " + " & ".join(cells) + BS + BS)
    return "\n".join(out)


BUILDERS = {"tab:t3": table_blocks, "tab:t3band": table_band, "tab:traceform": table_traceform,
            "tab:gap": table_gap, "tab:gapiso": table_gapiso, "tab:gapsum": table_gapsum, "tab:gapdeep": table_gapdeep,
            "tab:t4": table_hardedge, "tab:lb": table_lb, "tab:ks": table_ks,
            "tab:invmoment": table_invmoment, "tab:tail": table_tail,
            "tab:moments": table_moments, "tab:control": table_control, "tab:momentfit": table_momentfit,
            "tab:kssemi": table_kssemi,
            "tab:t1": table_cgec,
            "tab:corr": table_corr, "tab:signs": table_signs,
            "tab:prunerate": table_prune_block, "tab:ray": table_ray, "tab:pruneadapt": table_prune_adapt,
            "tab:regpath": table_regpath, "tab:crossover": table_crossover,
            "tab:gatemlp": table_gatemlp, "tab:newcorp": table_newcorp}

src = open(TEX, encoding="utf-8").read()
updated = 0
for key, fn in BUILDERS.items():
    # the markers are matched with their line break, so that tab:ks cannot match inside tab:kssemi
    b, e = "% BEGIN AUTOTABLE " + key + chr(10), "% END AUTOTABLE " + key + chr(10)
    if b not in src or e not in src:
        print(f"  {key}: no AUTOTABLE region in the source")
        continue
    body = fn()
    if body is None:
        print(f"  {key}: no records, left as is")
        continue
    i, j = src.index(b) + len(b), src.index(e)
    src = src[:i] + body + chr(10) + src[j:]
    updated += 1
    print(f"  {key}: rebuilt from records")

# the two constants and every computed number the prose quotes
macro("Cten", f"{CTEN:.4f}")
macro("CtenLong", f"{CTEN:.14f}")
macro("Cone", f"{CONE:.4f}")
macro("Records", str(sum(len(v) for v in REC.values())))

# the laptop-scale files kept beside the records, when present
_lap = os.path.join(HERE, "records_additions", "offbox_scratchpad")
_k24 = os.path.join(_lap, "kurtosis_law2_d24.json")
if os.path.exists(_k24):
    _arms = json.load(open(_k24, encoding="utf-8"))
    _ns = [int(x["n"]) for x in _arms]
    macro("KurtDtwentyfourNmin", f"{min(_ns):,}".replace(",", "{,}"))
    macro("KurtDtwentyfourNmax", f"{max(_ns):,}".replace(",", "{,}"))
_vh = os.path.join(_lap, "vh2.log")
if os.path.exists(_vh):
    _rows = []
    for ln in open(_vh, encoding="utf-8"):
        parts = ln.split()
        if len(parts) >= 7 and parts[0].isdigit():
            d_, p_ = int(parts[0]), int(parts[1])
            sig = math.sqrt((p_ - 1) * (d_ * d_ + 13 * d_ + 14) / 2)      # the exact variance parameter
            _rows.append((d_, float(parts[5]) / sig, float(parts[6]) / sig))
    if _rows:
        macro("VhDmin", str(_rows[0][0])); macro("VhDmax", str(_rows[-1][0]))
        macro("VhRmaxMin", f"{min(r[1] for r in _rows):.1f}"); macro("VhRmaxMax", f"{max(r[1] for r in _rows):.0f}")
        macro("VhRqFirst", f"{_rows[0][2]:.1f}"); macro("VhRqLast", f"{_rows[-1][2]:.1f}")
b, e = "% BEGIN AUTOTABLE macros" + chr(10), "% END AUTOTABLE macros" + chr(10)
if b in src and e in src:
    lines = [BS + "newcommand{" + BS + k + "}{" + v + "}" for k, v in sorted(MACROS.items())]
    i, j = src.index(b) + len(b), src.index(e)
    src = src[:i] + chr(10).join(lines) + chr(10) + src[j:]
    print(f"  macros: {len(lines)} computed numbers written to the preamble")
    # every \num... macro the prose uses must exist, and every macro emitted should be used
    import re
    used = set(re.findall(r"\\(num[A-Z][A-Za-z]*)", src))
    missing = sorted(k for k in used if k not in MACROS)
    check("every computed number the prose quotes is defined by the build", not missing, ", ".join(missing))
    unused = sorted(k for k in MACROS if k not in used)
    if unused:
        print(f"  {len(unused)} computed macro(s) not used in the prose: " + ", ".join(unused))
open(TEX, "w", encoding="utf-8", newline="\n").write(src)
print(f"{updated} tables rebuilt")

# The source must carry no control characters, and no reference broken across a line.
_ctrl = [(i, hex(ord(c)), ln[max(0, j - 30):j + 20])
         for i, ln in enumerate(open(TEX, encoding="utf-8").read().split("\n"), 1)
         for j, c in enumerate(ln) if ord(c) < 32]
check("source carries no control characters", not _ctrl,
      (f"{len(_ctrl)} found, first at line {_ctrl[0][0]} ({_ctrl[0][1]})") if _ctrl else "none")
for _i, _h, _ctx in _ctrl[:5]:
    print(f"  CONTROL CHARACTER line {_i} {_h}: {_ctx!r}")
_lines = open(TEX, encoding="utf-8").read().split("\n")
_broken = [i for i, ln in enumerate(_lines, 1) if ln.rstrip().endswith("~") or ln.startswith("ef{")]
check("no reference broken across a line break", not _broken, f"lines {_broken[:5]}" if _broken else "none")

print("\naudit")
fails = 0
for name, ok, detail, _m in AUDIT:
    if not ok:
        fails += 1
        print(f"  FAIL {name}: {detail}")
print(f"  {len(AUDIT)-fails} of {len(AUDIT)} checks pass")
scored = [(m, n, d) for n, ok, d, m in AUDIT if ok and m is not None]
if scored:
    scored.sort()
    print("  closest calls (margin = threshold / observed):")
    for m, n, d in scored[:3]:
        print(f"    {m:8.1f}x  {n}  [{d}]")
    vacuous = [(m, n) for m, n, _ in scored if m > 1000]
    if vacuous:
        print(f"  {len(vacuous)} check(s) passed with over 1000x margin - sanity checks, not evidence:")
        for m, n in vacuous[:4]:
            print(f"    {m:10.0f}x  {n}")
unscored = sum(1 for n, ok, d, m in AUDIT if m is None)
if unscored:
    print(f"  {unscored} check(s) report no margin (boolean or count based)")

if not a.no_build:
    for _ in range(2):
        subprocess.run([PDFLATEX, "-interaction=nonstopmode", "-halt-on-error",
                        os.path.basename(TEX)], cwd=os.path.dirname(TEX),
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    log = open(os.path.join(os.path.dirname(TEX), "kernel_open_problems_numerics.log"),
               encoding="utf-8", errors="replace").read()
    err = log.count("\n! ")
    over = log.count("Overfull")
    undef = log.count("undefined")
    print(f"build: {err} errors, {over} overfull, {undef} undefined-reference warnings")
    fails += err + undef

sys.exit(1 if fails else 0)
