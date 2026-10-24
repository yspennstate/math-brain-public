# Certify F(theta) >= R(p) on p in [0.08, 0.5], theta = beta/2 + d, d in [0, pi/4], sin^2 beta = p,
# except the lemma-B region p >= 0.49, |theta - beta| <= 0.3. mpmath interval arithmetic.
import json, sys, time
from mpmath import iv, mpf, mp
iv.prec = 80; mp.prec = 80
LN2 = iv.log(2)
PI = iv.pi
def h2_iv(x):            # x: mpf point in [0,1]; enclosure of h2(x) in bits
    if x <= 0 or x >= 1: return iv.mpf(0)
    X = iv.mpf(x)
    return (-X*iv.log(X) - (1-X)*iv.log(1-X)) / LN2
def h2_min(xlo, xhi):    # rigorous lower bound of min of h2 over [xlo,xhi] (h2 concave -> endpoint min)
    xlo = max(xlo, mpf(0)); xhi = min(xhi, mpf(1))
    if xlo > xhi: xlo = xhi
    return min(h2_iv(xlo).a, h2_iv(xhi).a)
def R_iv(p):              # enclosure of R(p) at a point p
    P = iv.mpf(p)
    return (P/2*(-iv.log(P)) + (1-P/2)*(-iv.log(1-P))) / LN2
def sin2_range(lo, hi):   # enclosure of {sin^2 t : t in [lo,hi]} for [lo,hi] subset (-pi/2, pi/2)
    assert lo > -1.5 and hi < 1.5
    s_lo = iv.sin(iv.mpf(lo))**2; s_hi = iv.sin(iv.mpf(hi))**2
    if lo >= 0: return s_lo.a, s_hi.b
    if hi <= 0: return s_hi.a, s_lo.b
    return mpf(0), max(s_lo.b, s_hi.b)
QPI = mp.pi/4 + mpf(2)**-70   # a point mpf strictly above pi/4
assert (PI/4).b < QPI
def lower_bound(b1, b2, d1, d2):
    # box in (beta, d); p = sin^2 beta is increasing on [0, pi/2]
    # theta = beta/2 + d ; theta - beta = d - beta/2
    t_lo = (iv.mpf(b1)/2 + d1).a; t_hi = (iv.mpf(b2)/2 + d2).b
    e_lo = (iv.mpf(d1) - iv.mpf(b2)/2).a; e_hi = (iv.mpf(d2) - iv.mpf(b1)/2).b
    x1 = sin2_range(t_lo, t_hi); x2 = sin2_range(e_lo, e_hi)
    p_hi = (iv.sin(iv.mpf(b2))**2).b
    lb = h2_min(*x1) + h2_min(*x2) - R_iv(p_hi).b
    return lb, b1, b2
def in_lemmaB(p1, b1, b2, d1, d2):
    if (iv.sin(iv.mpf(b1))**2).a < mpf('0.49'): return False
    # |theta - beta| = |d - beta/2| <= 0.3 for all p in box, d in box
    return (iv.mpf(d1) - iv.mpf(b2)/2).a >= mpf('-0.3') and (iv.mpf(d2) - iv.mpf(b1)/2).b <= mpf('0.3')
def run(max_boxes=3000000, max_sec=900):
    t0 = time.time()
    P0, P1 = mpf('0.28'), QPI   # beta range; sin^2(0.28) < 0.08 (lemma A covers below)
    stack = []
    # initial grid
    NP, ND = 64, 64
    for i in range(NP):
        for j in range(ND):
            stack.append((P0 + (P1-P0)*i/NP, P0 + (P1-P0)*(i+1)/NP, QPI*j/ND, QPI*(j+1)/ND))
    # make the last d end exactly at QPI (upper end of pi/4), first at 0
    closed = 0; closedB = 0; minlb = None; worst = None; nsplit = 0
    while stack:
        p1, p2, d1, d2 = stack.pop()
        lb, b1, b2 = lower_bound(p1, p2, d1, d2)
        if lb > 0:
            closed += 1
            if minlb is None or lb < minlb: minlb = lb; worst = (float(p1), float(p2), float(d1), float(d2))
            continue
        if in_lemmaB(p1, b1, b2, d1, d2):
            closedB += 1; continue
        if p2 - p1 < mpf(2)**-40 and d2 - d1 < mpf(2)**-40:
            return {"status": "FAIL", "box": [str(p1), str(p2), str(d1), str(d2)], "lb": str(lb)}
        nsplit += 1
        if closed + closedB + len(stack) > max_boxes or time.time() - t0 > max_sec:
            return {"status": "CAP_EXCEEDED", "closed": closed, "closedB": closedB, "stack": len(stack)}
        # split the side with larger estimated variation (p side weighted by ~4)
        if (p2 - p1) * 2 > (d2 - d1):
            pm = (p1 + p2) / 2; stack.append((p1, pm, d1, d2)); stack.append((pm, p2, d1, d2))
        else:
            dm = (d1 + d2) / 2; stack.append((p1, p2, d1, dm)); stack.append((p1, p2, dm, d2))
    return {"status": "PASS", "closed_positive": closed, "closed_by_lemmaB": closedB, "splits": nsplit,
            "min_positive_lower_bound": str(minlb), "box_of_min": worst, "seconds": round(time.time()-t0, 2),
            "d_domain_upper": str(QPI), "beta_domain": ["0.28", str(QPI)],
            "p_at_beta_lo_upper": str((iv.sin(iv.mpf('0.28'))**2).b)}
def lemma_constants():
    out = {}
    e3 = iv.exp(-3)
    out["h2(e^-3) lower"] = str(h2_min(e3.a, e3.b) if False else min(h2_iv(e3.a).a, h2_iv(e3.b).a))
    out["R(0.08) upper"] = str(R_iv(mpf('0.08')).b)
    out["h2(0.64143) lower"] = str(h2_iv(mpf('0.64143')).a)
    out["(1+sqrt(0.08))/2 upper"] = str(((1+iv.sqrt(iv.mpf('0.08')))/2).b)
    out["sqrt(0.08)/2 upper (must be <= e^-1.5)"] = str((iv.sqrt(iv.mpf('0.08'))/2).b)
    out["e^-1.5 lower"] = str(iv.exp(iv.mpf(-1.5)).a)
    out["(sin(0.3)/0.3)^2 lower (must be >= 0.97)"] = str(((iv.sin(iv.mpf('0.3'))/iv.mpf('0.3'))**2).a)
    out["sin^2(0.3) upper (must be <= 1/e)"] = str((iv.sin(iv.mpf('0.3'))**2).b)
    A = iv.mpf('0.97')*(-iv.log(iv.mpf('0.97')*iv.mpf('0.09')))/LN2 - 2/LN2
    out["A(0.3)/0.3^2 lower (must be > 0)"] = str(A.a)
    out["0.245^2*A(0.3)/0.09 lower"] = str((iv.mpf('0.245')**2*A).a)
    out["log2(0.51/0.49) upper"] = str((iv.log(iv.mpf('0.51')/iv.mpf('0.49'))/LN2).b)
    out["lemma A: 1-1/(2ln2) lower"] = str((1 - 1/(2*LN2)).a)
    out["lemma A: (0.25+0.0435)/ln2 upper"] = str((iv.mpf('0.2935')/LN2).b)
    return out
if __name__ == "__main__":
    res = {"lemma_constants": lemma_constants()}
    res["box_certificate"] = run()
    print(json.dumps(res, indent=1))
    json.dump(res, open(sys.argv[1], "w"), indent=1)
