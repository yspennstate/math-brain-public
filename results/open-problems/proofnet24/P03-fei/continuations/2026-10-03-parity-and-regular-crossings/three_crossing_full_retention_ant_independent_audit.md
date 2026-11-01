# Independent audit: full retained crossings still obstruct the local split

2 October 2026. Auditor: `/root/antivoter_audit`.

**Analytic verdict: PASS.** I read the complete stable
`three_crossing_full_retention_obstruction.md`, the separate
`three_crossing_full_retention_explicit_bounds.md`, and the predecessor
`three_crossing_largest_weight_obstruction.md`. I independently checked
the score realization, all retained crossings, perturbation probability,
Fourier entropy continuity, influence comparison, and explicit finite-N
bounds. This proves failure of a proposed largest-weight LOCAL entropy
increment criterion. It is not a counterexample to ordinary FEI, the
actual-middle-crossing trace candidate, or the completed slab theorems.

## 1. Actual common-score realization and retained crossings

For odd (N\ge3\), the pivot has weight (w=N+1\), the N original
weights are one, and the (K=2N^6\) new weights are
\(a=3w/K\). Thus (w>1>a>0\) and the pivot is uniquely largest in
the defining score. The three cuts (-w,2,w\) are ordered, span (2w\),
and have adjacent gaps at most (2w\).

If r tiny bits are positive, their contribution is
\(V=3w(r-N^6)/N^6\). The original score (wz+\sum x_j\) is odd,
(N^6\) is odd, and (3w\) is even. Hence every full score has odd
integer numerator over denominator (N^6\), whereas all cuts have even
numerators over that denominator. No tie occurs for any vertex.

With all original x bits negative, the branch z=-1 grid has endpoints
(-4w-N\) and (2w-N=w+1\). The z=+1 grid has endpoints
(1-3w\) and (1+3w\). Both extend strictly beyond both outer cuts.
Their step is (3w/N^6<1\); each interior interval has length at least
(N-1\ge2\). Each grid therefore contains an attained score in every
one of the four intervals. Each branch has exactly three genuine
alternating changes in its attained-score order. This is full retention
in BOTH restrictions, not merely retention in the parent function.

The new independent checker
`three_crossing_routes_ant_independent_check.py` constructs exact
rational witnesses by solving the grid inequalities with integer floor
division. It checks all odd N from 3 through 81. Its report records four
attained scores in each branch, without enumerating a huge tiny-bit cube.

## 2. The reference obstruction is realized exactly

Deleting V but retaining all tiny coordinates as irrelevant leaves the
original predecessor. For z=-1, the score is (-w+T\), so its value is
odd-N majority. For z=+1, the score (w+T\) starts at one, then three;
only the all-negative x configuration has its majority value flipped.
Consequently the pivot influence is exactly \(\varepsilon=2^{-N}\).
Adding irrelevant Fourier coordinates creates zero coefficients and
does not change spectral entropy or the split increment.

I rechecked the predecessor's analytic lower bound. Its odd-level
majority coefficients follow by differentiating majority to the central
layer indicator and using ((1+t)^d(1-t)^d=(1-t^2)^d\). The central
coefficient and Vandermonde/log-concavity estimates give

\[
|\widehat g(S)|\ge\frac{2^{-d}}{(2d+1)(d+1)}\ge2\varepsilon
\quad(N=2d+1\ge15).
\]

The exact coefficient-pair split identity has nonnegative term
(P[1+h_2(q)-h_2(r)]\). Even subsets contribute (2\varepsilon\)
in total. For odd subsets, (|\widehat A|\ge|\widehat g|/2\), and
(Ph_2(q)\ge\varepsilon^2\log_2(P/\varepsilon^2)\). Summing the
(2^{N-1}\) odd subsets gives exactly

\[
\Delta_zH(f_N^0)\ge\varepsilon L_N,\qquad
L_N=\frac{N+3}{2}-\log_2\frac{N(N+1)}2\longrightarrow\infty.
\]

The independent checker verifies the exact rational coefficient
inequalities for odd N through 81. The infinite-family conclusion uses
the analytic estimates, not those checks.

## 3. Tail and continuity estimates

The old odd-integer score is at distance at least one from all even cuts.
On (|V|<1\), every old label remains unchanged in the full function
and each branch. Applying the Rademacher exponential bound to
(Ka^2=9w^2/K\) gives

\[
d_N:=\Pr(|V|\ge1)\le2e^{-K/(18w^2)}\le2e^{-N^4/36}.
\]

The factor two is the two-sided tail, and both exponents are correct.
The full and individual branch disagreement probabilities are bounded
by this same d_N, since V is independent of the original coordinates.
For the paired pivot restrictions, a changed pivotal indicator requires
at least one changed branch, so

\[
|I_z(f_N)-\varepsilon|\le2d_N.
\]

For Boolean u,v disagreeing on probability d, Parseval gives
\(\|\widehat u-\widehat v\|_2=2\sqrt d\). Both Fourier vectors have
norm one. Thus the variation distance between their squared coefficient
laws is at most (2\sqrt d\), with exactly the stated normalization.
The maximal coupling argument proves
\( |H(P)-H(Q)|\le h_2(t)+t\log_2(D-1)\).
It includes the empty Fourier atom and applies to the full entropy used
throughout this campaign.

For total dimension (M=N+2N^6+1\), using (D\le2^M\) and
\(t_N=2\sqrt2e^{-N^4/72}<1/2\) gives per-function error
\(\omega_N=t_NM+h_2(t_N)\). The error in the full-minus-average-branch
split increment is at most (2\omega_N\), not three such errors:
the branch errors each have weight one-half. Since M is polynomial in N,
both \(\omega_N/\varepsilon\) and \(d_N/\varepsilon\) vanish.
The resulting ratio lower bound therefore diverges.

## 4. Explicit positivity and finite-N lower bound

The separate addendum is also correct. Put
\(B=\lfloor N^4/72\rfloor\),
\(D=\lfloor N^4/36\rfloor\). For N>=15,
\(B\ge3N^2\), \(D\ge6N^2\), and (D\ge2B\).
Using (e>2\) gives (d_N\le2^{1-D}\) and
\(2\sqrt{d_N}\le\bar t=2^{2-B}<1/2\).
The binary-entropy bound with \(\log_2e<2\) gives
\(h_2(\bar t)\le\bar tB\).

The exact elementary inequalities
\(M+B\le3N^6\le2^{2+6N}\),
\(3N^2\ge8N+5\), and \(6N^2\ge2N+2\) imply

\[
2\bar\omega\le\varepsilon^2,\qquad2d_N\le\varepsilon^2.
\]

Thus, for every odd N>=15,

\[
I_z(f_N)\ge\varepsilon(1-\varepsilon)>0,
\quad
\frac{\Delta_zH(f_N)}{I_z(f_N)}
\ge\frac{L_N-\varepsilon}{1+\varepsilon}.
\]

The numerator is positive: (L_{15}=9-\log_2 120>2\), and the
odd-N sequence L_N increases because its successive product ratio is
less than two. I also independently checked the addendum's exponent
and integer inequalities through odd N=81. This removes any possible
ambiguity about dividing by zero or dividing a negative lower bound by
an upper influence bound.

## 5. Checker status and honest conclusion

I read the author's `verify_three_crossing_direct_entropy_heat.py`.
Its retained-grid and dyadic sections use exact integers/Fractions and
do not claim a huge truth-table enumeration. Its majority formula is
checked by actual integer Walsh transforms. Other decision-tree entropy
and point-hole evaluations are explicitly labeled numerical supplements.
I found and reported an execution-only `len(vals)` reporting typo; the
author corrected the affected occurrences to `len(values)` and finished
the script successfully. I then checked the stable source and complete
saved report. It records 102 branch grids (odd N=3..103), 45 dyadic
certificates (odd N=15..103), and 43,688 direct integer majority Walsh
coefficients. The old typo is absent. No proof inference relies on a
numerical entropy supplement. I did not alter author files.

My independently completed report is
`three_crossing_routes_ant_independent_checks.json`. It certifies the
new exact grid and quantitative calculations separately from the trace
route checks. The analytic full-retention theorem and explicit bounds
pass regardless of that reporting typo.

The closed conclusion is precise: a dimension-independent estimate
\(\Delta_zH(f)\le C I_z(f)\) cannot follow from the pivot being the
largest defining weight, three nearby crossings, and all crossings
remaining genuine in both restrictions. Extremely rare score tails
preserve those combinatorial conditions while leaving entropy and pivot
influence close to an already adverse example. This does not establish
an FEI violation or disprove the actual-middle-crossing trace inequality.
