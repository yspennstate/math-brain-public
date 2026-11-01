# Audit 2 of NOTE "eps > 0 in closed form" (agent_B/NOTE.md, c_closed_eps.py)

(Audit 1 is agent C, audit_C/AUDIT_CEPS_agent_C.md, numerical on the three-valued b with its own evaluator and solver.)

agent A, 20 Oct 2026 09:5x. Scope: beta1 = 0, a_i = 1, eps >= 0, the formula
c(s) = r K - (p2/2) r1 avg Q - p2 r2 cb/(r K) - p3 r1 avg[k Q]/(r K), x0 = r d K B3/(2 B2).

Verdict: CONFIRMED (11:1x). The coefficients and the solve check by hand (A, B). Twelve Monte Carlo rows of the stream, six on 9/-1
and six on the three-valued 6/2/-1, agree with the NOTE's exact roots. The one 2.7 se row was noise: a re-run with a fresh seed came in
at -1.2, and the two pooled give +1.0. Extrapolated linearly to d = 0, the Monte Carlo gives the following against the closed form:
- 9/-1: -0.661 +- 0.002 at n d 1 (closed form -0.6646) and -0.042 +- 0.008 at n d 5 (-0.0568);
- 6/2/-1: -0.543 +- 0.003 at n d 1 (-0.5390) and -0.257 +- 0.007 at n d 5 (-0.2645).
All four are within 2 se. The exact rows' own linear values sit on the closed form: -0.664 and -0.055 on 9/-1, and -0.5391 and -0.2643
on 6/2/-1.

## A. The Taylor coefficients

With y = 1 + u and r = sq/(sq + eps), psi(y) = (sq + eps)/(sq sqrt(y) + eps) = 1/(1 + h), h = r (u/2 - u^2/8 + u^3/16 - ...).
Then 1/(1 + h) = 1 - h + h^2 - h^3 gives, by powers of u:
- u: -r/2, so p1 = -r/2;
- u^2: r/8 + r^2/4, so p2 = r/4 + r^2/2 = sq (3 sq + eps)/(4 (sq + eps)^2);
- u^3: -r/16 - r^2/8 - r^3/8, so p3 = -(3/8)(r + 2 r^2 + 2 r^3) = -3 sq (eps^2 + 4 eps sq + 5 sq^2)/(8 (sq + eps)^3).
All three equal c_closed_eps.py's expressions identically and reduce to -1/2, 3/4, -15/8 (so p2/2 = 3/8, p3/6 = -5/16) at eps = 0.
Using sq = sqrt(B2) in place of sqrt(V) changes r by O(x^2) = O(d^2), which moves x* only at O(d^3).

## B. The solve

eps enters only through psi; v, V and eta = v/V - 1 do not depend on it. With E[g] = x and E[g eta] = d K (2 x B2 + B3)/B2 (exact,
audit UNIFORM item D), the root equation to the order needed is
    x [1 + 2 p1 d K + (p2/2) E eta^2 + (p3/6) E eta^3] = -p1 d K B3/B2 - (p2/2) E[b eta^2] - (p3/6) E[b eta^3],
so x0 = -p1 d K B3/B2 = r d K B3/(2 B2) and
    x*/x0 = 1 + r d K - (p2/2) E eta^2 - [(p2/2) E[b eta^2] + (p3/6) E[b eta^3]]/x0 + O(d^2).
At this order the coefficients enter linearly; products such as p1 p2 are O(d^2). The three moment ratios are eps-free and are read
off the verified eps = 0 formula (AUDIT_CCLOSED): E eta^2/d -> r1 avg Q, E[b eta^2]/(d x0|_{r=1}) -> 2 r2 cb/K,
E[b eta^3]/(d x0|_{r=1}) -> 6 r1 avg[k Q]/K. Since x0 carries one factor r, the general coefficients are p2 r2 cb/(r K) and
-p3 r1 avg[k Q]/(r K), which is the NOTE's formula term by term. The limits check by hand: as s -> 0, K -> 1/2, avg Q and avg[k Q] -> 0,
cb -> 1/6, giving r/2 - p2 r2/(3 r); as s -> infinity, K, cb -> 1 and avg Q, avg[k Q] -> 1/2, giving r - p2 r1/4 - p2 r2/r - p3 r1/(2 r).

## C. Monte Carlo of the stream at eps = 1 (rrm_mc_cv_eps.py)

rrm_mc_cv.py with the update g/(sqrt(v) + eps), the matching first-order control variate
g/(sqrt V + eps) - g (v - V)/(2 sqrt V (sqrt V + eps)^2), and b drawn as a uniform permutation of a general multiset. At eps = 0 it
reproduces rrm_mc_cv.py to every printed digit (n 20, beta2 .95, 200 chains, seed 3). It shares no code with rr_exact_m2.py or
rrm3v_eps.py. Seed 7, 4000 chains, epochs as in rrmc_batch.sh (rrmc_eps_batch.sh, rrmc_eps_out/).

| b | n | beta2 | n d | MC | NOTE exact | closed form |
|---|---|---|---|---|---|---|
| 9/-1 | 100 | 0.99 | 1 | -0.7088 +- 0.0011 | -0.708 (-0.707679) | -0.6646 |
| 9/-1 | 200 | 0.995 | 1 | -0.6849 +- 0.0008 | -0.686 | -0.6646 |
| 9/-1 | 500 | 0.99 | 5 | -0.1121 +- 0.0044 | -0.105 | -0.0568 |
| 9/-1 | 1000 | 0.995 | 5 | -0.0769 +- 0.0031 | -0.080 | -0.0568 |
| 9/-1 | 1000 | 0.99 | 10 | +0.0516 +- 0.0060 | +0.0602 | +0.1091 |
| 9/-1 | 2000 | 0.995 | 10 | +0.0820 +- 0.0042 | +0.0854 | +0.1091 |
| 6/2/-1 | 100 | 0.99 | 1 | -0.5656 +- 0.0013 | -0.563923 | -0.5390 |
| 6/2/-1 | 200 | 0.995 | 1 | -0.5492 +- 0.0009 | -0.551533 | -0.5390 |
| 6/2/-1 | 200, seed 11 | 0.995 | 1 | -0.5526 +- 0.0009 | -0.551533 | -0.5390 |
| 6/2/-1 | 400 | 0.9975 | 1 | -0.5469 +- 0.0016 | -0.545295 | -0.5390 |
| 6/2/-1 | 500 | 0.99 | 5 | -0.3029 +- 0.0037 | -0.298632 | -0.2645 |
| 6/2/-1 | 1000 | 0.995 | 5 | -0.2799 +- 0.0027 | -0.281463 | -0.2645 |

MC minus exact, in se: -1.0, +1.4, -1.6, +1.0, -1.4, -0.8 on 9/-1; -1.3, +2.7, -1.0, -1.1, +0.6 on 6/2/-1. The n 200 row was re-run with seed 11 and came in at -1.2. The two seeds pooled give +1.0 se,
so the +2.7 was noise. Two exact solvers, the NOTE's and audit 1's, agree on that root to 13 digits. The closed-form column is the d -> 0 limit, so at fixed d it differs from the rows by
the slope in d the NOTE reports (about -5 d at large s on 9/-1).
