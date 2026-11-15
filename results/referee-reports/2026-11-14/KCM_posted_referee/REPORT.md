ACCEPT (two wording fixes, neither touches a proof)

# Referee report: "Stationary measures of planar kinetically constrained models with bounded conditional odds" (posted version)

Repository: yspennstate/kcm-planar-stationary-bounded-odds, commit 63e47fe (13 Nov 2026). Read 14 Nov 2026 by
an agent, independently of the pre-posting reports D0028A (claim) and D0028AR (referee, MINOR) of 13 Nov, which
were read only afterwards to compare.

## What the paper claims

1. Theorem 1.1: on Z^2, for constraints of uniform finite range that do not depend on the constrained spin, every
   stationary measure with bounded conditional odds (single-site conditional probabilities in [eps, 1-eps] given any
   finite set of other sites) satisfies detailed balance.
2. Theorem 1.2: if moreover the constraints come from an update family and pi_a(G_{V_n}) -> 1 for every a in (0,1),
   such a measure is pi. Applies to FA-1f and FA-2f at every q. Corollary 1.3 handles the delta_1 atom of FA-1f.
3. Proposition 1.4: on strips Z x H every stationary measure of FA-1f (and of monotone site-dependent constraints that
   allow every FA-1f move and vanish at 1) is (1-lambda) pi + lambda delta_1, with no hypothesis on mu. The paper says
   this also follows from MST25 Theorem 2.5 and Lemma 2.8 after relabelling the strip as Z.

The paper does not claim the MST conjecture on Z^2 and says so (end of Section 1.3).

## Proofs, re-derived line by line

- Lemma 2.1 (zero mass forces zero flux): correct; applying it to zeta^x shows no pair (a, a^x) has exactly one zero
  for any x, so A_V(x) is finite.
- Lemma 2.2: phi(u,v) = (u-v) log(u/v) is convex and 1-homogeneous, hence subadditive, which gives (a); (b) is the
  triangle inequality over extensions; (c) uses (u-v) log(u/v) = (u-v)^2 / logmean >= 2(u-v)^2/(u+v) and
  Cauchy-Schwarz with sum (a + a^x) <= 2. All correct.
- Lemma 2.3: the symmetrised identity for mu(L F(eta_V)) = 0 is right; for interior x the ratio
  r_x(zeta)/r_x(zeta^x) = pi_V(zeta^x)/pi_V(zeta) (checked for both values of zeta_x), so a/a^x = rho(zeta)/rho(zeta^x)
  and the interior terms are -A/2. Tail bound: on {l > lambda}, -(a - a^x) l <= a^x l <= mu_V(zeta^x) l
  <= M mu_V(zeta) l e^{-l} <= M mu_V(zeta) lambda e^{-lambda} for lambda >= 1; the {l < -lambda} group is its mirror
  image under zeta <-> zeta^x. The 2M/e bound is the same with threshold 0. Correct.
- Lemma 2.4: monotonicity of S_n uses that V_{n-1} is interior to V_n and B_n interior to V_{n+1}; (2.7) follows from
  Lemma 2.2(b),(c) and Cauchy-Schwarz. Correct.
- Lemma 2.5: A_{V_n}(x) = 0 forces a = a^x termwise; summing over extensions gives (1.4). Correct.
- Theorem 1.1: |B_n| = 8r^2 n - 4r^2 + 4r <= 8r^2 n for r >= 1 (checked). The bound |l| <= K uses that
  mu_V(zeta)/mu_V(zeta^x) is a conditional odds ratio with conditioning set V minus x. Then S_n^2 <= Cn(S_{n+1}-S_n)
  and S_n <= Dn. If some S_m = s > 0, the product of (1 + s/(Cn)) diverges so S_n -> infinity; once S_n >= 3C,
  1 + 3/n >= (1 + 1/n)^2 for n >= 1 gives quadratic growth, contradicting S_n <= Dn. Correct, and this is exactly where
  the log factor of MST25 Remark 2.16 disappears: bounded odds bound |l| by a constant, so no truncation at log n is
  needed.
- Remark 3.1 (d >= 3): with S_n^2 <= C n^{d-1} dS and S_n <= D n^{d-1} a bounded positive S is consistent, since the
  required increments s^2/(C n^{d-1}) are summable. Correct.
- Proposition 3.2 (strips): |B_n| = 2r|H| is constant, S_n is bounded and nondecreasing, the shell currents go to 0, and
  the tail bound with lambda -> infinity after n -> infinity gives S_n = 0. Correct; no hypothesis on mu is used.
- Lemma 4.1: the emptying path to 0_V is legal for every exterior by monotonicity, the reversed steps are legal because
  c_x ignores eta_x, and detailed balance summed over extensions gives rho_V(zeta) = rho_V(zeta^x). The bound
  |nu(F) - nu(F|G)| <= 2(1 - nu(G)) checks. Correct.
- Lemma 4.2 (domination by pi_eps): the sequential coupling is right.
- Theorem 1.2, Corollary 1.3, Proposition 1.4: correct. nu = (mu - lambda delta_1)/(1 - lambda) is a probability
  because mu({1}) = lambda, and stationary because delta_1 is.
- Lemma 5.1 (FA-2f): the growth fact, the good-block construction (seed m x m, then alternately a column of length k
  and a row of length k+1 up to L x L), the bound prod(1-t^k)(1-t^{k+1}) >= 1 - 2t^m/(1-t), the count of blocks
  (log J = 2 log N - O(log log N) against m^2 = O((log N)^{2/3})), and 2N^2 t^L <= 2N^{2 - C|log t|} with
  C > 3/|log t| all check, as does the final sweep (columns of height L, then full rows, each containing an
  L-segment). Correct.
- Remark 5.2 (finite boxes): a legal flip at x leaves BP unchanged because x is emptiable at the first BP step in both
  configurations; the code confirms the fibre count equals the kernel dimension in all 40 cases.

## Fixes

1. Proof of Proposition 1.4, line 424 of main.tex: "These events decrease to {1}^c along the increasing V_n" should
   read "increase to". The events {eta_{V_n} != 1_{V_n}} grow with V_n and their union is {eta != 1}; the conclusion
   nu(G_{V_n}) -> 1 is continuity from below and is unaffected.
2. Proof of Lemma 4.2, lines 399-400: "Each conditional probability is an average of conditional probabilities given
   eta_{{x_1..x_k} minus x_k}" - it is that conditional probability (take V = {x_1, ..., x_k} in (1.5)); "is an
   average of" can be dropped.

Cosmetic, no change needed: V_n means [-nr, nr]^2 in Section 3 and [-n, n]^2 in Theorem 1.2; both are fine in context.
In Lemma 4.1 rho_V is undefined on G_V when mu_V vanishes there, which only happens when mu(G_V) = 0, the trivial case
the proof already covers.

## Sources

- All 12 DOIs resolve on Crossref with the authors, titles, journals, volumes, issues and pages printed in the
  bibliography (crossref.out). The ICM 2026 proceedings are SIAM (10.1137/25M180425X, vol. 5, pp. 497-515), as cited.
- MST25 (arXiv:2510.20461v1, re-downloaded and read): Theorem 2.4 is the translation-invariant statement credited to
  Holley [11]; Theorem 2.5 is the one-dimensional statement without translation invariance; Lemma 2.8 the internal
  spanning identification; Corollary 2.9 covers FA-1f, BABP and delta-West in d = 1; Theorems 2.12 and 2.13 are the 1D
  and d-dimensional East classifications; Conjecture 3 is the mixture conjecture; Remark 2.16 is the log(k) obstruction
  in d = 2. Every citation in the paper points to the right item.
- Martinelli ICM survey Conjecture 1.6 on p. 499: checked by D0028AR on 13 Nov; not re-read here.
- Prior work: a web search (14 Nov) found nothing proving detailed balance for non-translation-invariant stationary
  measures of a KCM in d = 2; D0028AR's longer search (Holley-Stroock, Moulin Ollagnier-Pinchon, Jahnel-Koppl,
  Georgii, Mountford) found the same, and the paper now cites the first three and explains why rates bounded below do
  not apply.

## Code

`python -I code/finite_checks.py` from the repository root ran in about two minutes and printed "40 cases, all
checks passed". Its output equals data/finite_checks.json after line endings are normalised (sha256 cc3361a3... both
ways). On Windows the script writes CRLF, so a rerun there makes `sha256sum -c SHA256SUMS` report the JSON as changed;
`open(..., "w", newline="\n")` at line 151 would make reruns byte-identical everywhere. The committed blob matches
SHA256SUMS.

## Comparison with the 13 Nov reports

D0028AR's two requests (call the strip result a corollary of MST25; add Holley-Stroock, Moulin Ollagnier-Pinchon and
Jahnel-Koppl) are both done in the posted version (lines 103-109 and 150-153). Neither earlier report caught the
"decrease" in the proof of Proposition 1.4.
