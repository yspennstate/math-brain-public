# Referee report on route BT-biased-thresholds (C004 / C025)

Referee: independent Opus referee, workflow of 11-12 Oct 2026. I wrote only this file and `referee_code/`.
My code does not import the route's `code/`; it recomputes everything from the definitions
(`referee_code/bfcore.py`: exact butterfly transform, cross-checked against the direct definition of the
biased Fourier coefficient). Nothing was pushed or uploaded.

## Summary of verdicts

| id | route status | verdict | one line |
|---|---|---|---|
| BT-1 | REFUTED | CONFIRMED, but KNOWN | witness recomputed exactly and certified; identical family and asymptotics already in the campaign source `biased.tex`, Thm `biasfull:weightedcounter`. Prop 3.1's divided display is false for s = 4, 5 (needs s >= 6) |
| BT-2 | REFUTED | CONFIRMED, but KNOWN | same source, eq. `biasfull:weightedTC`; the stated p -> 0 limit should be s h(1/s)/(8 - 4/s), not s h(1/s)/8 |
| BT-3 | PROVED | CONFIRMED | exact termwise identity on every Boolean function n <= 4 |
| BT-4 | PROVED (+KNOWN) | CONFIRMED | proof checked; the KNOWN p-biased case is Kahn-Kalai 2007, eq. (3) (citation was missing) |
| BT-5 | PROVED | CONFIRMED | product-law adaptation of paper Lemmas bias:concentration / bias:rank |
| BT-6 | PROVED | CONFIRMED | |
| BT-7 | PROVED | CONFIRMED | Case B inequality (iii) holds for every Boolean function, no floor needed |
| BT-8 | PARTIAL | status correct; the named candidate for gap (1) is false | see BT-10 and section 3 |
| BT-9 | CONJECTURE | not refuted (independent search consistent) | numerical trap recorded in section 5 |
| BT-10 | CONJECTURE (+ PROVED parts) | PROVED parts CONFIRMED; (LCR) REFUTED | new witness: anti-diagonal tribes thresholds |
| BT-11 | EVIDENCE | numbers CONFIRMED; interpretation does not generalize | on the new family every product reference loses (1/2) ln m per unit influence |
| BT-12 | KNOWN | CONFIRMED | O'Donnell-Tan read from the arXiv PDF |

**New result from refereeing (section 3, complete proof).** The weighted thresholds
`T_m = 1[sum_{i=1}^{2m} i y_i >= 2m+1]` under the product law `q_i = r^{i+2}` (r -> 0, m fixed) satisfy
`H+/Delta -> 2`, yet (a) their (LCR) excess is at least `((1/2) ln m - ln 2 - o(1)) I`, and (b) for every
choice of level-wise product reference weights, with exact normalizers, the level-wise Gibbs bound exceeds
`E` by at least `((1/2) ln m - o(1)) I`. So (LCR) is false for weighted thresholds, and no argument that
bounds `E` through level-wise Gibbs inequalities against product-form references (the architecture of paper
Prop. bias:weak, of NOTES Theorem 5.1 and of NOTES section 7) can prove C025 with an absolute constant.
This does not touch FEI+ itself (the ratio on the family tends to 2).

## 0. Literature and prior-campaign findings

* **O'Donnell-Tan, arXiv:1304.1347 (v1, 4 Apr 2013).** Read from the arXiv PDF, pages 3-4.
  Conjecture 1 (FEI+ for product distributions) is exactly
  `sum_{S nonempty} f~(S)^2 log( prod_{i in S}(1-mu_i^2) / f~(S)^2 ) <= C (Inf^mu[f] - Var_mu[f])`;
  with `mu_i = E x_i` in +-1 notation, `1-mu_i^2 = 4q_i(1-q_i) = sigma_i^2`. Theorem 1: composition with
  factor `max{C1, C2}`. Theorem 2: every `F:{-1,1}^k -> {-1,1}` satisfies mu-biased FEI+ with factor
  `2^{O(k)}` for any product distribution ("a factor depending only on its arity k and not the biases").
* **Kahn-Kalai, "Thresholds and expectation thresholds", arXiv:math/0603218 (CPC 16, 2007), eq. (3):**
  `p I_p(F) >= m(p) log_p m(p)` for monotone F under mu_p (their inductive proof covers any F), with
  equality on subcubes. Since `log_p m = ln(1/m)/ln(1/p)`, this is `alpha ln(1/alpha) <= p ln(1/p) sum_i rho_i`,
  the p-biased case that NOTES Lemma 4.2 labels KNOWN without a citation.
* **The route's section 3 refutations are already in the campaign's own source material.**
  `~/mop_fei100/reports/fei-2026-10-11/source_material/reductions/paper/biased.tex`
  (in commit 034ae6a0f, 2026-10-11 23:18 +0300, before this route started), Lemma `biasfull:mixture` and
  Theorem `biasfull:weightedcounter`: the same weighted threshold `A = {m X_0 + X_1 + ... + X_m >= m}` with
  `P_Q(X_0 = 0) = eta = 1/m`, light bias `q = m^{-2}`, gives `alpha TC(mu(.|A))/I = (ln m + 1)/8 + O(ln m/m)`
  and `[V ln(1/V) - sum_i I_i ln^+(4 rho_i/V)]/I = (1/2) ln m - ln 2 + O(ln m/m)`, with `H+/Delta -> 2`.
  Remark `biasfull:creditremark` states the scope; Proposition `biasfull:tribes` gives the same failure for
  rare disjoint tribes (monotone, not a threshold). The route's family (`x = 1/s`, `p = 1/(50 s)`) differs
  only in the light bias. A041's run (20261011T214208Z) also cites these labels.
* The section-3 family below (anti-diagonal thresholds with geometric biases) and the level-wise
  product-reference obstruction do not appear in CAMPAIGN, CLAIMS, COUNTEREXAMPLES, `biased.tex`, the baseline
  paper's bias section, or the fleet's runs (searched for "anti-diagonal", "perfect matching", "product
  reference", "LCR"). I did not search the external literature for it.

## 1. Checks run (all code in `referee_code/`, my own)

| script | what it checks | result |
|---|---|---|
| t0_sanity.py | butterfly spectrum == direct definition `fhat(S)^2 = (E[f prod(y_i-q_i)])^2 / prod q_i(1-q_i)` (exact), Parseval, MAJ3, OR2 limit | 210/210 exact matches; MAJ3 ratio 4; OR2 -> 7.77049 at q = 1e-4 |
| t1_lemma41.py, t1b_negcontrol.py | Lemma 4.1 termwise `G_f[B u {i}] == G_{e_i}[B]` and the Delta identity, exact | every Boolean function n<=3 (all orders, 6 biases each, 1,656 cases) and all 65,536 functions n=4: 0 failures; two deliberately faulted arms fail 400/400, the true arm 0/400 |
| t2_lemma42.py | DTC identity computed from the joint law of mu_A; c_i definition; inequality | 2,654 increasing T (n<=4) + 120 weighted thresholds n=6..10, biases to 1e-8: identity error <= 2e-69 at 70 digits; DTC >= 0; equality on subcubes; omitting DTC would err by up to 0.92 nats |
| t3_antichain_rank.py | Lemma 4.3 exhaustive; Lemma 4.4 exact (all 168 antichains of {0,1}^4, 30 laws each, plus layers m<=30); Lemma 4.5 functional and its noise step | 0 violations; rank functional max 0.85 (bound 4.386); noise step max slack -0.24 |
| t4_weak_and_floor.py | Thm 5.1, Cor 5.2, Thm 6.1, Case B (iii), (v), (i) | Thm 5.1 max (E - V ln 1/V)/I = 1.43 (bound 9.21); Cor 5.2 nearly tight on AND_k at q = delta (6.80 vs 6.91 at delta = 1e-3), never exceeded; E/J <= 2.7 vs K_delta >= 105.5; Case B inequality on every Boolean function n<=4 (66,352 cases): max lhs/rhs = 0.234; identity (v) exact; (i) exact on 9,660 checks |
| t5_witness.py | BT-1/BT-2 witness: generic exact transform for s<=12, rigorous intervals, independent closed forms to s=65536, and biased.tex's parametrization | reproduces every number the route reports (section 2) |
| t6_lcr.py | exact (LCR) excess; controls on T_s; first runs on the new family | T_s: -0.7656, -0.7259 (route: -0.77, -0.73); new family grows with m |
| t7_antidiag.py | section 3: exact full spectra m<=7; structured interval certificates m<=64; optimal product reference by convex minimization | section 3.4 |
| t8_gibbs.py | BT-11 reproduction; the same Gibbs bounds on the new family | section 2, BT-11 |
| t9_bt9_search.py | independent search against BT-9 | best 7.770780163550 < 2+4/ln 2 = 7.770780163556 |
| t10_jensen.py | the convexity step behind "symmetric thresholds satisfy (LCR)" | global credit <= level-wise credits on 1,500 random functions |

## 2. Claim-by-claim verdicts

### BT-1 (REFUTED: no absolute C in `V ln(1/V) <= sum_i I_i ln^+(4 rho_i/V) + C I` for weighted thresholds) -- CONFIRMED; status should be KNOWN

* Each step of Proposition 3.1 checks out. Exact facts: `p_h = alpha(1-x)` follows from
  `alpha = p_h + (1-p_h) a` and `(1-p_h) a = x alpha`; `I_0 = 4p_h(1-p_h)(1-a) <= 4alpha(1-x)`,
  `I_j = 4(1-p)x alpha`, `4rho_0/V = (1-a)/(alpha(1-alpha))`, `4rho_j/V = x/(p(1-alpha)) >= 1`. Steps (i)-(iv)
  are correct under the stated hypotheses `p <= x <= 1/2`, `alpha <= 1/2` (step (iv) drops `alpha ln 4 >= 0`
  and `s p x ln(x/p) >= 0`, and replaces `1-x+sx` by `1+sx`, all in the safe direction).
* **Defect (harmless for the refutation).** The second display, "With x = 1/s ... excess/I >=
  ((s-1)/(2s)) ln s - ln 2 - delta_s", divides a lower bound for the excess by the upper bound `I <= 8 alpha`.
  That is valid only when the bracket `((s-1)/s) ln s - ln 4 - alpha ln(1/alpha) - 4 alpha` is nonnegative,
  i.e. `s >= 6` here. At s = 4 the certified value is `excess/I = -0.1874002782 < -0.173287 =
  ((s-1)/(2s)) ln s - ln 2` (t5, interval arithmetic), so the display is false as stated for s = 4 (and the
  bracket is also negative at s = 5). For s >= 6 it holds (certified at s = 6, 8, 10, 12).
* Exact recomputation (t5): my generic transform on the full `2^{s+1}` table (s <= 12) and independently
  derived closed forms agree exactly on V, I, Delta (rationals) and to 1e-30 on the logarithmic quantities,
  and reproduce every reported number: s = 4: excess/I -0.1874002782, H+/Delta 2.102602087; s = 8: 0.2365805316,
  2.049534992; s = 10: 0.3655723228, 2.039936678; s = 16, 32, 64, 128: 0.6289981, 1.0027728, 1.3652940,
  1.7210778. Continued with rigorous intervals: 2.0728935 (256), 2.7706223 (1024), 3.4651616 (4096),
  4.8519840 (65536), tracking `(ln s)/2 - ln 2`.
* The statement refuted is exactly the one claimed (a universal C over weighted thresholds and product laws),
  and T_s is a weighted threshold under a genuine product law. **But the refutation is already
  `biased.tex` Theorem `biasfull:weightedcounter`, equation `biasfull:weightedcredit`**, with the same
  threshold and the same `x = eta = 1/m`; running that parametrization (q = m^{-2}) through my closed forms
  gives 2.7705617 at m = 1024 against the route's 2.7706223 at s = 1024. It must be relabeled KNOWN with that
  citation and not presented as a finding of this route.

### BT-2 (REFUTED: no absolute C in `alpha TC(mu_A) <= C I` for minority events of weighted thresholds) -- CONFIRMED; KNOWN

* The TC formula `TC(mu_A) = s[h(x+(1-x)p) - (1-x)h(p)]` was checked against TC computed directly from the
  explicit conditional law (sum of marginal entropies minus joint entropy) for s <= 12: exact agreement.
* alpha TC/I: 0.3110649 (s = 4), 0.4709079 (16), 0.5530611 (32), 0.6368022 (64), 0.7216616 (128), matching
  the route; 1.4990003 at s = 65536 (interval-certified), tracking `(ln s + 1)/8`.
* **Minor slip.** In Proposition 3.2 the displayed lower bound has denominator `4(1 - x + s x) = 4(2 - 1/s)`
  at `x = 1/s`, so its `p -> 0` limit is `s h(1/s)/(8 - 4/s)`, not `s h(1/s)/8`. Unboundedness is unaffected.
* KNOWN: `biased.tex` equation `biasfull:weightedTC`, same family.

### BT-3 (PROVED: least-element decomposition) -- CONFIRMED

The argument: (R3) gives `fhat(B u {i}) = sigma_i dhat_i(B)` for i not in B, for any Boolean T (d_i in
{-1,0,1}). For B inside U_i, `phi_B` depends only on `y_{U_i}`, so `dhat_i(B) = E[d_i phi_B] = E[e_i phi_B] =
ehat_i(B)`. Each nonempty S has a unique last element in the order. Hence `P(S) = sigma_i^2 ehat_i(B)^2`,
`ln(sigma_S^2/P(S)) = ln(sigma_B^2/ehat_i(B)^2)` and `|S| - 1 = |B|`, termwise. Exact check (t1): the termwise
identity in G-coordinates for every nonempty S of every Boolean function with n <= 3 (all orders) and of all
65,536 functions with n = 4, biases down to 1e-6: zero failures; the Delta identity exactly. The checker is not
vacuous: two deliberately faulted versions fail on 400/400 cases. Notational nit: CLAIMS.json writes `rho_i`;
for non-monotone T it must be read as `rhohat_i = E d_i` (signed), as NOTES does.

### BT-4 (PROVED: DTC identity; KNOWN p-biased inequality) -- CONFIRMED; citation supplied

The argument: `H(mu_A) = -ln(1/alpha) + sum_i [b_i ln(1/q_i) + (1-b_i) ln(1/(1-q_i))]`; given `Y_{-i} = z`, the
conditional law of `Y_i` is Bern(q_i) when both extensions lie in A, a point mass at 1 when only (z,1) does
(i pivotal), and (z,0) in A with (z,1) not in A is impossible for increasing A; `mu_A(i pivotal) = q_i rho_i/alpha
= c_i`; `b_i = c_i + (1-c_i)q_i`; the bracket reduces to `c_i ln(1/q_i)`; `DTC >= 0` by the chain rule. My check
(t2) computes `H(Y_i | Y_{-i})` from the joint law, not from the route's formula: identity error <= 2e-69 at 70
digits over 2,774 cases, equality on subcubes. The p-biased inequality is Kahn-Kalai 2007, eq. (3) (above). The
version with unequal q_i via the DTC identity appears to be the route's own elementary proof.

### BT-5 (PROVED: antichain bound; biased rank lemma) -- CONFIRMED

Lemma 4.4: the fair-bit decomposition has the right law (`P(Y_j = majority value) = 1 - 2m_j + m_j`); a fiber of
an antichain is an antichain; Sperner density `c_q <= (q+1)^{-1/2}` (paper lem:antichain-density);
`E[1/(F+1)] <= 1/E F` by the generating function and Cauchy-Schwarz; the single-coordinate bound by
conditioning. Lemma 4.5: the noise identity under a product law; `E[d(Y)d(Y')] <= rho sup_y P(d(Y')=1 | Y=y)`
because d is 0/1; fair activation probability `2 t m_j`; Lemma 4.3 on the fiber, then restriction to F;
`m_j >= q_j(1-q_j) = sigma_j^2/4`; on `{kappa < K-1}`, `(1-t)^kappa >= (1-t)^{K-1}`; `(1-1/(2K))^{-(K-1)} <= e^{1/2}`;
the integral equals `2 ln(2 sqrt e) + 2 = 3 + ln 4`. Tests (t3): Lemma 4.3 on all 179 regular monotone functions
n <= 4, Lemma 4.4 exactly on all antichains n <= 4 and on layers m <= 30: 0 violations; the rank functional
never exceeded 0.85 on 220 thresholds n <= 11 and its noise inequality never failed (max slack -0.24).
Remark: this is a direct product-law adaptation of paper Lemmas bias:concentration and bias:rank, with
lem:pivotal-antichain replacing the slice structure. PROVED is right; the novelty is modest.

### BT-6 (PROVED: E <= V ln(1/V) + A_0 I for regular monotone T) -- CONFIRMED

Every step holds: Gibbs on k-sets; `ln(sigma_i^2/theta_k(i)) = a ln^+(Lambda_i/k)`; normalizer: on
`[Lambda_i, Lambda_{i+1}]` one has `x - 1 <= Lambda_i` (since `sigma_i^2 <= 1`), so
`sigma_i^2 h(Lambda_i) <= int h(x-1) dx` and `sum_i theta_k(i) <= 1 + 6k <= 7k`, `Z_k <= (7k)^k/k! <= (7e)^k`;
rank term via `|S| >= |B cap U_i| + 1` and Lemma 4.5; level entropy `<= V ln(1/V) + V(1 + ln m) <= V ln(1/V) + I`.
`A_0 = 9.2094633`. Regularity is used only through Lemma 4.5; weights of either sign, zero weights (placed last)
and the reduction R1 are handled. Test (t4): all 171 nonconstant regular monotone functions n <= 4 with 40
random biases each (to 1e-6): max `(E - V ln(1/V))/I = 1.43`.

### BT-7 (PROVED: corrected FEI+ under a bias floor) -- CONFIRMED

Corollary 5.2: for `alpha >= 1/20`, `V >= 0.19` and `ln(1/0.19) = 1.6607 <= 1.661`; otherwise the dual
`T*(y) = 1 - T(1-y)` (increasing, biases `1-q_i`, same rho, I, V; the floor is symmetric), `V <= 4 alpha < 1/e`
so `V ln(1/V) <= 4 alpha ln(1/alpha)`, Lemma 4.2, `4 q_i rho_i = I_i/(1-q_i)`, and `ln(1/q)/(1-q)` is decreasing
(`ln x <= x-1`). The bound is nearly attained by AND_k at `q = delta` (6.799 against 6.915 at delta = 1e-3),
never exceeded (t4).
Theorem 6.1: Case A, `J_i >= eta I_i`. Case B: `T = u + y_0(1-u-v)` holds for any T (uv = 0 for monotone T);
(i) if `d_0 = 1` at both `y^{j<-0}` and `y^{j<-1}` then T equals `y_0` there, so j is not pivotal, and
`P(d_0(Y^{j<-b}) = 0) <= eps/P(Y_j = b)`; with `eps < delta(1-delta)/2` this gives `rho_j < 1/2`; (ii) the
coefficient formulas; `|uhat(B)| <= sigma_B/2`; (iii) eq. bias:eq-5-9 (its proof covers `a +- b`), the
identity for `phi_s(lambda^2 x)` and `lambda^2 ln(1/lambda^2) <= 2lambda/e`; the constant
`4 + 4 ln 2 + 4/e = 8.2441 <= 8.25`; (iv) Corollary 5.2 on the restrictions; (v) exact. Tests (t4): the
deterministic inequality (iii) holds for **every** Boolean function n <= 4 with coordinate 0 as the pivot (66,352
cases, biases to 1e-6, max lhs/rhs = 0.234); it uses neither monotonicity nor the floor. Identity (v) held
exactly in every case; (i) held exactly on 9,660 monotone checks; `E/J <= 2.7` against `K_delta >= 105.5`.
The statement proved is exactly the one claimed, including the constant `(2K_delta/ln 2)`.

### BT-8 (PARTIAL: C025 uniformly) -- status correct; gap (1) is mis-specified

Proved only with a bias floor: correct. But the claim names (LCR) as "the precise candidate" for gap (1);
section 3 refutes (LCR) and shows more: no level-wise product reference can close gap (1) on weighted
thresholds. Gap (1) should read "a normalization mechanism that is not a product reference on whole spectral
levels". Gap (2) (near-dictator without a floor) stands as stated.

### BT-9 (CONJECTURE: sup H+/Delta = 2 + 4/ln 2 over weighted thresholds and product laws) -- not refuted

Independent search (t9): all 116 distinct threshold functions with every coordinate relevant for n = 2..5
(integer weights <= 7 for n <= 4, <= 5 for n = 5), 6,159 random log-odds starts in [-16, 16] with greedy
hill-climbing to |logit| <= 27, exact spectra, 40-digit logarithms: best 7.770780163550, below
`2 + 4/ln 2 = 7.770780163556`, always at an AND/OR degeneration. The section-3 family has ratio -> 2.
A first float64 run reported 7.770826 > 2 + 4/ln 2 on OR2; that was a rounding artifact (section 5).

### BT-10 (CONJECTURE (LCR), with PROVED sub-claims) -- PROVED parts CONFIRMED; (LCR) REFUTED

* The implication holds. With `theta_k(i) = max(sigma_i^2 min(1,(k/Lambda_i)^a), 4 pi_i^(k))`:
  `sum_i theta_k(i) <= 7k + 4k`, so `Z_k <= (11e)^k`; `ln(sigma_i^2/theta_k(i)) = min(a ln^+(Lambda_i/k),
  ln(sigma_i^2/(4 pi_i^(k))))`, which is at most `a ln^+(Lambda_i/k) - ln^+(4 pi_i^(k)/sigma_i^2)` (check the two
  signs of `ln(4pi/sigma^2)`); the level-k mass containing i is `W_k pi_i^(k)`, so the subtracted credit is exactly
  the right side of (LCR); with Lemma 4.5 the constant is `C + 1 + ln 11 + (6/5)(3 + ln 4)`.
* The symmetric case holds: `x -> x ln^+(cx)` is convex and `pi_i = sum_k (W_k/V) pi_i^(k)`, so level-wise
  credits dominate the global credit for **every** function (t10: 1,500 random functions, max violation 0);
  with paper Lemma bias:credit and `sum_k W_k ln(1/W_k) <= V ln(1/V) + I`, (LCR) holds for symmetric thresholds
  with `C = 15 + ln 2`.
* (LCR) itself is **false** for weighted thresholds: Theorem R3 (section 3) gives
  `LCR-excess/I >= (1/2) ln m - ln 2 - o(1)`; exact values 0.0889, 0.1853, 0.2660 for m = 5, 6, 7 and certified
  lower bounds 0.6920, 1.0394, 1.3862 for m = 16, 32, 64, against the route's empirical maximum 0.744.

### BT-11 (EVIDENCE: on T_s the loss sits in the normalizer estimate) -- numbers CONFIRMED; the conclusion does not generalize

Reproduced (t8): T_s, s = 4, 8, 12: E/I = 0.6222, 0.6620, 0.6735; paper-type reference with exact Z_k:
1.3508, 1.2865, 1.2384; level-dependent: 0.6307, 0.6712, 0.6830. All match. But NOTES section 3 concludes
"the obstruction is to the bookkeeping ..., not to the reference measure itself". That is true for T_s only. On
the anti-diagonal family both bounds, with exact normalizers, grow (m = 2..6: 1.180, 1.454, 1.635, 1.769, 1.875)
like `E/I + (1/2) ln(2m - 1)` while `E/I = 0.6932`; Theorem R3(c) proves that every product reference does this.

### BT-12 (KNOWN: O'Donnell-Tan) -- CONFIRMED

Conjecture 1, Theorem 1 and Theorem 2 say what the route says (section 0). The open part is indeed uniformity in
the arity for thresholds with arbitrary weights.

## 3. New: anti-diagonal tribes thresholds (referee results with complete proofs)

Notation as NOTES section 0, natural logarithms. `M_{i,k} = sum_{|S|=k, S contains i} P(S)`, so
`pi_i^(k) = M_{i,k}/W_k`; `h` is binary entropy in nats; `nu_k(S) = P(S)/W_k` on k-sets.

**Lemma R1 (a level-2 lower bound for the (LCR) excess).** Let T be increasing, mu any product law with
`0 < q_i < 1`, and assume `4 pi_i^(2) >= sigma_i^2` for every i with `M_{i,2} > 0`. Then

    LCR-excess := sum_{k>=1} W_k ln(1/W_k) - sum_k sum_i W_k pi_i^(k) ln^+(4 pi_i^(k)/sigma_i^2)
               >= W_2 [ 2 H(u) - H_2 - 4 ln 2 ] - R,

where `u_i = M_{i,2}/(2W_2)` (a probability vector), `H_2 = H(nu_2)`, and
`R = sum_{|S| not in {0,2}} P(S) sum_{i in S} ln(1/(q_i(1-q_i)))`.

*Proof.* (a) Every `W_k <= 1`, so the left sum is at least `W_2 ln(1/W_2)`. (b) For k != 2, `pi <= 1` gives
`ln^+(4pi/sigma_i^2) <= ln(4/sigma_i^2) = ln(1/(q_i(1-q_i)))`, so the credits of all levels k != 2 total at most R.
(c) By hypothesis every level-2 credit argument is >= 1, so the level-2 credit equals
`sum_i M_{i,2}[ln(4/sigma_i^2) + ln(M_{i,2}/W_2)] = sum_{|S|=2} P(S) ln(16/sigma_S^2) + 2W_2(ln 2 - H(u))`.
(d) `W_2 ln(1/W_2) + sum_{|S|=2} P ln sigma_S^2 = sum_{|S|=2} P ln(sigma_S^2/P) - W_2 H_2 = E_2 - W_2 H_2`, with
`E_2` the level-2 part of E. (e) For increasing T and |S| = 2, `d_S T = T(11)-T(10)-T(01)+T(00)` lies in
{-1,0,1}, so `|G_S| <= 1/2` and `E_2 = sum_{|S|=2} P ln(1/G_S^2) >= W_2 ln 4`. Combining,
`W_2 ln(1/W_2) - (level-2 credit) = E_2 - W_2 H_2 - 6W_2 ln 2 + 2W_2 H(u) >= W_2[2H(u) - H_2 - 4 ln 2]`. QED.

**Lemma R2 (a product reference cannot fit a matching).** Let nu be a law on 2-subsets of [n], let M be a set of
pairwise disjoint 2-sets with `nu(M) > 0`, `nu_M = nu(. | M)`, `theta in (0,inf)^n`, and
`Q_theta({a,b}) = theta_a theta_b / e_2(theta)`. Then

    KL(nu || Q_theta) >= nu(M) H(nu_M) - h(nu(M)).

If nu is uniform on a perfect matching of [2m], then `inf_theta KL(nu || Q_theta) = ln(2m - 1)`.

*Proof.* Splitting the KL sum over M and its complement O, and applying the log-sum inequality on O with
`Q_theta(O) <= 1`: `KL >= nu(M) ln nu(M) + nu(M) K_M + nu(O) ln nu(O) = nu(M) K_M - h(nu(M))`, where
`K_M = sum_{S in M} nu_M(S) ln(nu_M(S) e_2(theta)/theta_S) = -H(nu_M) + ln e_2(theta) - sum_{S in M} nu_M(S) ln theta_S`.
Because the pairs of M are disjoint, `e_2(theta)` contains the monomials `theta_S` (S in M) and, for distinct
S = {a,b}, S' = {c,d} in M, the four cross monomials summing to `(theta_a+theta_b)(theta_c+theta_d) >=
4 sqrt(theta_S theta_S')`; hence `e_2(theta) >= (sum_{S in M} sqrt(theta_S))^2`. By concavity of ln,
`ln sum_S sqrt(theta_S) >= sum_S nu_M(S) ln(sqrt(theta_S)/nu_M(S))`, so
`ln e_2(theta) >= sum_S nu_M(S) ln theta_S + 2H(nu_M)` and `K_M >= H(nu_M)`. For the uniform law on a perfect
matching, Maclaurin's inequality `e_2(theta)/C(2m,2) >= (prod_i theta_i)^{1/m}` gives
`KL >= ln C(2m,2) - ln m = ln(2m-1)`, with equality at constant theta. QED.

**Theorem R3.** Fix m >= 2, n = 2m, `T_m = 1[sum_{i=1}^{n} i y_i >= n+1]` (a weighted threshold), `f = 2T_m - 1`,
and the product law `q_i = r^{i+2}`, `0 < r <= 1/2`. Let `M = {{i, n+1-i} : 1 <= i <= m}` (the anti-diagonal
pairs; `q_i q_{n+1-i} = r^{n+5}` for all i). As `r -> 0` with m fixed:

(a) `P(S) = 4r^{n+5}(1 + O(r^3))` for S in M, and `P(S) <= 4^{2n} r^{n+6}` for every other nonempty S. Hence
`W_2 = 4m r^{n+5}(1 + O(r))`, `I = 2W_2(1 + O(r))`, `Delta/I -> 1/2`, `E/I -> ln 2` and `H+/Delta -> 2`.

(b) `LCR-excess/I >= (1/2) ln m - ln 2 - o(1)`.

(c) For every level k and every `theta_k in (0,inf)^n`, the level-wise Gibbs bound
`B = sum_k [W_k ln(e_k(theta_k)/W_k) + sum_{|S|=k} P(S) sum_{i in S} ln(sigma_i^2/theta_k(i))]` satisfies
`B - E >= W_2 [nu_2(M) H(nu_2(.|M)) - h(nu_2(M))] = ((1/2) ln m - o(1)) I`.

Consequently there is no absolute C for which (LCR) holds for all weighted thresholds and product laws; and no
argument that bounds E by level-wise Gibbs inequalities against product-form references, with any weights and
exact normalizers (paper Prop. bias:weak, NOTES Theorem 5.1, NOTES section 7, code/gibbs_ld.py), can give
`E <= C I` uniformly on weighted thresholds. FEI+ itself holds on the family with ratio tending to 2.

*Proof of (a).* Write `w(S) = sum_{i in S} i` and `N_X = sum_{j in X} j y_j`. For `Y` inside [n],
`prod_{j in Y} q_j = r^{w(Y) + 2|Y|}`, so for every X and every integer `u >= 1`,
`P(N_X >= u) <= sum_{nonempty Y in X, w(Y) >= u} prod_{j in Y} q_j <= 2^n r^{u+2}`. Also
`sigma_S^2 <= 4^{|S|} r^{w(S) + 2|S|}` and `sigma_S^2 <= 1`. By (R3), `G_S = 2^{-|S|} E[d_S f]` with
`|d_S f| <= 2^{|S|}`, and `d_S f(y) != 0` forces `T(1_S, y) = 1`, i.e. `N_{S^c} >= n + 1 - w(S)`; so
`|G_S| <= min(1, P(N_{S^c} >= n+1-w(S)))`.
If `w(S) <= n`: `P(S) <= 4^{|S|} r^{w(S)+2|S|} (2^n r^{n+3-w(S)})^2 = 4^{|S|+n} r^{2n+6+2|S|-w(S)} <= 4^{2n} r^{n+8}`.
If `w(S) >= n+1` and S not in M: |S| = 1 is impossible (`w <= n`); |S| = 2 forces `w(S) >= n+2` and
`P(S) <= 16 r^{n+6}`; `|S| >= 3` gives `P(S) <= 4^n r^{n+7}`.
If `S = {i, i*}` in M (`i* = n+1-i`): `G_S = (1/2)[1 - P(N' >= i*) - P(N' >= i) + P(N' >= n+1)]` with
`N' = N_{S^c}`, each probability at most `2^n r^3`, so `G_S = 1/2 + O(r^3)`; and
`sigma_S^2 = 16 r^{n+5}(1-q_i)(1-q_{i*}) = 16 r^{n+5}(1 + O(r^3))`. So `P(S) = 4r^{n+5}(1 + O(r^3))`.
There are at most `2^n` sets, which gives W_2, I and `Delta = W_2 + O(r^{n+6})`. For E: on M,
`P ln(sigma_S^2/P) = P ln(1/G_S^2) = P(ln 4 + O(r^3))`; every other set has
`P ln(sigma_S^2/P) <= P ln(1/P) <= 4^{2n} r^{n+6} ln(4^{-2n} r^{-n-6}) = O(r^{n+6} ln(1/r))` (x ln(1/x) is
increasing on [0, 1/e]). So `E = W_2 ln 4 (1 + o(1))`, `E/I -> ln 2`, and `H+/Delta = E/(Delta ln 2) -> 2`.

*Proof of (b).* From (a): `nu_2(M) = 1 - O(r)`; on M the masses are equal up to factors `1 + O(r^3)`, so
`H(nu_2(.|M)) = ln m - O(r^3)`. Then `H_2 = h(nu_2(M)) + nu_2(M) H(nu_2(.|M)) + nu_2(O) H(nu_2(.|O)) <=
ln m + O(r ln(1/r))` (O = the other 2-sets, at most `n^2` of them). `M_{i,2} = P({i,i*}) + O(n 4^{2n} r^{n+6})`,
so `u_i = (1 + O(r))/(2m)` and `H(u) >= ln(2m) - O(r)`. `R <= 2^n n 4^{2n} r^{n+6} ((n+2) ln(1/r) + ln 2) =
o(W_2)`. The hypothesis of Lemma R1 holds for small r: `4 pi_i^(2)/sigma_i^2 >= (1+O(r))/(m r^{i+2}) -> inf`.
Lemma R1 gives `LCR-excess >= W_2[2 ln(2m) - ln m - 4 ln 2 - o(1)] - o(W_2) = W_2[ln m - 2 ln 2 - o(1)]`;
divide by `I = 2W_2(1 + O(r))`. QED.

*Proof of (c).* At each level the Gibbs bound is an identity plus a divergence:
`B_k - E_k = W_k [ln e_k(theta_k) - E_{nu_k} ln theta_k(S) - H(nu_k)] = W_k KL(nu_k || Q_{theta_k}) >= 0`, where
`E_k` is the level-k part of E and `Q_theta(S) = prod_{i in S} theta(i)/e_k(theta)`. Keep k = 2 and apply
Lemma R2 with the matching M; by (b) the bracket tends to ln m and `W_2/I -> 1/2`. QED.

**3.4 Numerical confirmation (t6, t7, t8).**

Exact full spectra, `r = 1/(4m^2)` (t7 Part 1):

| m | exact LCR excess/I | Lemma R1 bound | inf_theta KL(nu_2 \|\| Q_theta) | ln(2m-1) | E/I | H+/Delta |
|---|---|---|---|---|---|---|
| 2 | -0.4093737 | -0.411801 | 0.97026 | 1.09861 | 0.694316 | 2.00351 |
| 3 | -0.1877894 | -0.1936834 | 1.52155 | 1.60944 | 0.693315 | 2.00024 |
| 4 | -0.03082034 | -0.03647232 | 1.88433 | 1.94591 | 0.693222 | 2.00004 |
| 5 | 0.08886905 | 0.08497079 | 2.15187 | 2.19722 | 0.693185 | 2.00001 |
| 6 | 0.1853047 | 0.1822751 | 2.36308 | 2.39790 | 0.69317 | 2.0000 |
| 7 | 0.2659859 | 0.2635152 | 2.53734 | 2.56495 | 0.693163 | 2.0000 |

(The infimum over theta was computed by convex minimization in `log theta`; heuristic `(1/2) ln m - ln 2` =
-0.347, -0.144, 0, 0.112, 0.203, 0.280.)

Structured certificates (t7 Part 2): the level-1 and level-2 masses, `I_i = sigma_i^2 rho_i` and R computed from the
exact generating function of `N_{-i}` and `N_{-ij}` truncated at degree n, in mpmath interval arithmetic (60
digits); the method agrees exactly with the full-spectrum computation at m = 2 (r = 2^-4) and m = 4 (r = 2^-6).
Certified (Lemma R1 hypothesis checked in each case):

| m | r | certified LCR excess/I >= | (1/2) ln m - ln 2 | nu_2(M) | R/W_2 |
|---|---|---|---|---|---|
| 16 | 2^-12 | 0.692035 | 0.693147 | 0.9997711 | 9.1e-5 |
| 32 | 2^-14 | 1.039391 | 1.039721 | 0.9999409 | 2.6e-5 |
| 64 | 2^-16 | 1.386200 | 1.386294 | 0.999985 | 7.2e-6 |

Gibbs bounds of the route's two references with exact normalizers on the family (t8), m = 2..6: paper-type
1.1796, 1.4542, 1.6354, 1.7691, 1.8747; level-dependent 1.1795, 1.4538, 1.6353, 1.7691, 1.8747; true E/I = 0.6932.

**3.5 Scope and consequences.** The mechanism is the rare-tribes mechanism of `biased.tex` Prop.
`biasfull:tribes`: the level-2 spectral sample chooses one of m disjoint blocks, an entropy of ln m, while any
per-coordinate or product charge pays about ln(2m) for each of the two members. For a weighted threshold the 2-sets
contained in A always form a shifted family (if `w_a + w_b >= theta` and `w_c >= w_a` then `w_c + w_b >= theta`),
so they are never a matching of two or more pairs; but the geometric law `q_i = r^{i+2}` puts all but `O(r)` of
the level-2 spectral mass on the anti-diagonal matching. This is not a
counterexample to FEI+ (ratio -> 2). For C025 it means: a proof must use a normalization or reference that is not a
product over coordinates on whole spectral levels (for example mixtures over blocks, the joint witness/queue
references of C008, or exact composition-type decompositions). The route's proposed next step, "prove (LCR) for
weighted thresholds", is closed. The family should join T_s and the three-class family as a mandatory test for any
proposed credit or reference in this stream.

## 4. Key raw outputs

* t5: `s= 4 excess/I=[-0.1874002782, -0.1874002782] ... claimed lower display ... = -0.173287; certified: excess/I < displayed lower bound? True`;
  `s= 6 ... [0.06550743529] ... 0.0534193 ... False`; closed forms agree with the generic transform: True (s = 4..12);
  `s=65536 excess/I=[4.851984006, 4.851984006] alphaTC/I=[1.49900033, 1.49900033]`;
  biased.tex parametrization `m=1024 excess/I=[2.770561654] alphaTC/I=[0.9908897957]`.
* t1: `n<=3 all functions: 1656 cases, fails 0`; `n=4 all 65536 functions: 65536 cases, total fails 0`;
  negative arms `{'A': 400, 'B': 400, 'C': 0}`.
* t2: `max |identity error| 5.7956e-70` (n<=4), `1.8854e-69` (thresholds n=6..10).
* t4: `D. Case-B inequality, all Boolean T n<=4, pivot coordinate 0: 66352 cases; max (lhs-rhs) = 0.0 ; max lhs/rhs = 0.2343 ; identity (v) failures: 0`.
* t9: `random starts: 6159  best H+/Delta found: 7.770780163550083  exceeds 2+4/ln2? False`.

## 5. Numerical traps met during refereeing

* float64 logarithms of arguments within 1e-11 of 1 lose about five digits. The first t9 run reported
  `H+/Delta = 7.770826 > 2 + 4/ln 2` for OR2 at `q = (3e-12, 1.1e-8)`; at 50 digits the value is 7.7707801473,
  below the proven bound of paper Lemma comp:elementary-gates. Any ratio near an AND/OR degeneration must be
  evaluated with high-precision (or log1p) logarithms.
* In mpmath interval arithmetic, `x.a` and `x.b` are degenerate intervals, not mpf numbers; convert before
  comparing.

## 6. Not checked

* BT-9 beyond thresholds with n <= 5 (and the route's larger searches were not replayed).
* The citation in Lemma 4.3 (paper lem:pivotal-antichain) was checked against the paper's statement and
  exhaustively for n <= 4, not against any external source.

(This was the 11 Oct 23:3x-23:4x workflow ask: work with the Opus agents to help solve FEI; my part was to referee
route BT-biased-thresholds, C004/C025, claim by claim.)
