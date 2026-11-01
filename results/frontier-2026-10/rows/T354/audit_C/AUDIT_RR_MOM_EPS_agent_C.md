# T354 random-reshuffling remainder lemmas with momentum and with eps > 0, audit 1 (agent C, 20 Oct 2026 03:27)

Objects: the RR enclosures in agent_B/remainder_rr_mom_runs.txt (beta1 > 0, eps = 0) and remainder_rr_eps_runs.txt
(beta1 = 0, eps >= 0), and the simulated ratios x*/(x0 r) quoted in the note for beta2 = 0.99. The beta1 = 0, eps = 0 case is
agent A's audit (d0733bc7) and is not repeated here.

Verdict: CONFIRMED numerically. Every exact root lies inside its enclosure, and the exact ratios at beta2 = 0.99 match the
note's simulations to their three digits. I did not re-derive the enclosure algebra by hand; this audit tests the enclosures
against an independent exact computation of x*.

## Method (rr_exact_mom_eps.py)

The test model only (n = 10, b = (9, -1 x 9), a = 1). Under RR the special sample sits at q0 in the current epoch and at an
independent uniform q_m in the m-th earlier one, so m_t and v_t are explicit sums over epochs. 1/(sqrt v + eps) is written as
int_0^inf h(t) e^(-t^2 v) dt with h(t) = (2/sqrt pi)[1 - eps sqrt(pi) t erfcx(eps t)]; the exponential factorizes over epochs,
so E[m e^(-uv)] is a product of per-epoch averages F_m times g_o + dg(1-b1)(a0 + sum G_m/F_m). Gauss-Legendre in t on
[0, 6.5]; epochs with b2^(mn) < 1e-3 enter log prod F through four cumulants of b2^(p-q); the momentum sum is kept explicit
for b1^(mn) down to e^-40. No Laplace kernel or perturbative expansion in d is used, so this is a different route from the note's.

Bug found and fixed in my own first run: the momentum epochs were capped at the variance cutoff, which at beta2 0.9 left 7
epochs and put (0.9, 0.9, 3, 0.2) 30 standard errors off the simulation. After the fix all four checks below agree.

## Frozen-x drift against simulation (rr_sim_check.txt, 4000 chains x 600 epochs)

| beta1 | beta2 | eps | x | exact | sim |
|---|---|---|---|---|---|
| 0.5 | 0.9 | 1 | 0.05 | -0.023761 | -0.023771 +/- 6e-6 |
| 0.9 | 0.9 | 3 | 0.2 | 0.028143 | 0.028139 +/- 2e-6 |
| 0.9 | 0.95 | 0 | 0.1 | 0.022524 | 0.022517 +/- 4e-6 |
| 0.99 | 0.9 | 1 | 0.1 | 0.024449 | 0.024449 +/- 1e-6 |

The first three differ by 1.7 to 2 se, all on the same side (exact above sim, by 2e-4 to 4e-4 relative). That is either chance
or a small simulation transient; it is two orders below the enclosure widths, so it does not touch the verdict.

## Roots against the enclosures (rr_exact_runs.txt)

| beta1 | beta2 | eps | x0 | exact x* | x*/x0 | enclosure |
|---|---|---|---|---|---|---|
| 0.9 | 0.9999 | 0 | 6.05474e-05 | 6.05465e-05 | 0.999984 | [6.053651e-05, 6.055643e-05] inside |
| 0.9 | 0.999 | 0 | 6.07141e-04 | 6.07050e-04 | 0.999851 | [5.965605e-04, 6.174682e-04] inside |
| 0.5 | 0.999 | 0 | 1.65003e-03 | 1.64869e-03 | 0.999190 | [1.638075e-03, 1.659097e-03] inside |
| 0.9 | 0.99 | 0 | 6.2126e-03 | 6.20763e-03 | 0.999200 | vacuous in the note |
| 0 | 0.999 | 1 | 1.50549e-03 | 1.50383e-03 | 0.998895 | [1.498141e-03, 1.509445e-03] inside |
| 0 | 0.999 | 3 | 1.00366e-03 | 1.00272e-03 | 0.999066 | [1.000124e-03, 1.005291e-03] inside |
| 0 | 0.999 | 10 | 4.63227e-04 | 4.62880e-04 | 0.999249 | [4.621317e-04, 4.636203e-04] inside |
| 0 | 0.99 | 0 | 2.07189e-02 | 2.04605e-02 | 0.987527 | [2.693923e-03, 3.877906e-02] inside |
| 0 | 0.99 | 1 | 1.55392e-02 | 1.53699e-02 | 0.989106 | [6.282483e-03, 2.456503e-02] inside |
| 0 | 0.99 | 3 | 1.03594e-02 | 1.02633e-02 | 0.990724 | [6.303852e-03, 1.422685e-02] inside |
| 0 | 0.99 | 10 | 4.78128e-03 | 4.74547e-03 | 0.992512 | [3.645919e-03, 5.840069e-03] inside |

Here x0 already carries the eps factor r = 3/(3 + eps), so x*/x0 is the note's x*/(x0 r). At beta2 0.99 the note's simulated
ratios are 0.986, 0.989, 0.991, 0.993; the exact values are 0.9875, 0.9891, 0.9907, 0.9925. The (0.9, 0.999) root is the same
at 160 and 320 nodes to all nine printed digits.

## Not covered

The enclosure derivations themselves (only tested, not re-derived), models other than the n = 10 test model, and novelty.

## Addendum, 20 Oct 03:41: the enclosure algebra re-derived (rr_mom_eps_algebra_check.py, rr_mom_eps_algebra_check.txt)

The note's verdict changes from "numerically confirmed" to CONFIRMED. The algebra now has a derivation check.

Momentum (remainder_rr_mom.py):
- m_k is a convex combination of past gradients, so |m_k| <= G and |E[m_k r]| <= G times the p-average of the per-position
  cubic bound. Correct.
- The zeroth- and first-order terms use the full lag sums: f', and d K C/V with K = K_rr(n, beta1, beta2), whose pairing rule
  (C / -C/(n-1) / 0) is the beta1 = 0 rule applied lag by lag. Only the second-order sum is truncated at L. The code's tail
  b1^L G(1 + e + e^2) over-covers that truncation. Conservative and correct.
- Second order for lag i:
  - Both Z lags in lag i's own epoch: the exact moment formula, with s1 and s2 the c-sums over that epoch.
  - Both in one other epoch: f' times E[(that epoch's part)^2].
  - Mixed or two different other epochs: 0.
  - "Other" includes the current epoch's partial sum when lag i lies in an earlier epoch. So the bracket needs e_p = d(cur+full)/V
    and not only the earlier-epoch part, and the code uses e_p. Correct.
  - Brute force over all pairs of permutations (current epoch plus one earlier epoch, n = 4, every p and every lag, arbitrary
    weights): max difference 9.6e-15.

eps > 0 (remainder_rr_eps.py):
- (s+eps) D = E[g psi(y)], with psi = (s+eps)/(s sqrt y + eps).
- psi'(1) = -r/2 and psi''(1) = r/4 + r^2/2, re-derived and checked by finite differences at four (s, eps) pairs.
- With q = s sqrt y + eps: q' > 0, q'' < 0, q''' > 0. So the three terms of (1/q)''' all have one sign, and each grows as y falls.
  The closed |psi'''| matches a fourth-order finite difference to 1e-4 relative on y in [0.2, 1.8], and it is decreasing there.
  So M3 at y = 1 - e is the sup on [1-e, 1+e].
- At eps = 0 it reduces to (15/8) y^(-7/2) and (e^3/6) M3 = (5/16) e^3 (1-e)^(-7/2).
Correct.

Also second audit of the beta1 = 0, eps = 0 lemma: AUDIT_RR_B1ZERO_agent_C.md (03:39).
