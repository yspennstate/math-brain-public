TASK: B18 ACCOUNT: account02 RUN: 2026-09-21T13:37:21.763323+00:00 — Han-credit block descent and FEI extremal recursion

MODEL: GPT-5.6 Sol; source=self_report
THINKING LEVEL: UNKNOWN; source=not_exposed; requested=maximum actually supported
THINKING USAGE: NOT_EXPOSED; provider thinking time=NOT_EXPOSED; coverage=unavailable
BRAIN STATUS: WITHOUT_VERIFIED_BRAIN

# Status

**Full uniform-cube Fourier entropy-influence conjecture: OPEN / NOT PROVED.**

This run attacks the active account02/B18 assignment: the existential restriction/recursion bridge. It uses the newest compatible block selector and block recombination results at their exact scopes and derives a new fixed-cardinality descent theorem with the Han/dual-Shearer deficit retained as a negative credit. No lattice, surjectivity, plateaued, read-once, affine-symmetric, or polynomial-core hypothesis is removed.

Fresh scientific master immediately before the derivation was `e067fbba2c77a956b240a924c833143bc3175ee9`. Exact dependencies:

1. account03/B18 block-selector compiler, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T100020Z-block-selector-compiler/REPORT.md`, blob `4d0a67f151c9fd9674bd985460c33113c3363418`: for a restriction-descendant maximizing `r=H/I`, every nonempty physical block A is critical, `Delta_A H >= r I_A`, and physical-block influence costs telescope.
2. account01/B14 prediction-error block theorem, `proofnet24/P03-fei/fleet-2026-09-21/account01/B14/20260921T101355Z-block-lsi-overlap/REPORT.md`, blob `f3c518e5facba0fa7412fd0929ccc074549b17c8`: `Delta_A H=B_A+R_A` with `B_A=H(X_A|X_{A^c})` and `0<=R_A<=c_* M_A`, `c_*=2/ln 2`.
3. account01/B18 random-erasure EXIT dual, `proofnet24/P03-fei/fleet-2026-09-21/account01/B18/20260921T111435Z-erasure-exit-dual/REPORT.md`, blob `eb51df70d0e43e8255ebee6dc904da4f2e5d8389`: the Bernoulli-erasure curve obeys the corresponding continuous Bayes-error tube on maximal-ratio cores.
4. account04/B18 restriction-tree debit/reserve ledger, `proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/account04/B18/20260921T131816Z-b18-fei-r12/REPORT.md`, blob `a2eb9b018bb339d038384dad9ee5a894778b0a95`: exact global debit/reserve accounting and a finite-degree reserve seed, with the dimension-independent accumulated debit payment still open.

The new result below is not another erasure-tube statement: it converts the exact fixed-cardinality block excess into a **guaranteed high-ratio restriction child**, and then into an extremal-constant recursion, while preserving the Han deficit rather than dropping it.

# 1. Notation

Let `f:{-1,1}^n->{-1,1}` have exactly n relevant coordinates. Let `X` be its spectral sample,

`Pr[X=S]=fhat(S)^2`.

Write

`H=H(X)`, `I=sum_i p_i`, `p_i=Pr[i in X]`.

For a nonempty block `A subseteq [n]` let

`I_A=sum_{i in A}p_i`,

`B_A=H(X_A | X_{A^c})`,

and

`Delta_A H = H(f) - 2^{-|A|} sum_a H(f_a)`.

The inherited block theorem gives

`Delta_A H = B_A + R_A`,  `0<=R_A<=c_* M_A`,  `c_*=2/ln 2`,          (1.1)

where

`M_A = sum_{i in A} E min{Pr(X_i=1 | X_{A^c}), Pr(X_i=0 | X_{A^c})}`.   (1.2)

Fix `k in {1,...,n-1}` and put `q=n-k`. Let

`N_k=binom(n,k)`, `u_k=binom(n-1,k-1)=(k/n)N_k`,
`v_k=binom(n-1,k)=(q/n)N_k`.

Let

`h_q = (1/binom(n,q)) sum_{|B|=q} H(X_B)`                           (1.3)

be the average q-coordinate marginal entropy. Define the Han deficit

`A_q := h_q - (q/n)H`.                                                (1.4)

Entropy submodularity / Han's inequality gives `A_q>=0`.

Finally define the average one-bit Bayes error after seeing q coordinates,

`eps_q := [binom(n,q)(n-q)]^{-1}
          sum_{|B|=q} sum_{i notin B}
          E min{Pr(X_i=1|X_B),Pr(X_i=0|X_B)}`.                       (1.5)

Because `A^c=B` bijects k-blocks with q-blocks,

`(1/N_k) sum_{|A|=k} M_A = k eps_q`.                                 (1.6)

# 2. PROVED: exact fixed-cardinality excess identity

Assume now that `g` is a nonconstant physical restriction descendant maximizing

`r=H(g)/I(g)`

among all nonconstant restriction descendants. Delete any irrelevant coordinates, so g has n relevant coordinates. The inherited all-block criticality gives

`e_A := Delta_A H - r I_A >=0`                                      (2.1)

for every nonempty proper block A.

## Theorem 2.1 — Han credit equals part of the aggregate local excess

For every `1<=k<=n-1`,

`sum_{|A|=k} e_A = sum_{|A|=k} R_A - N_k A_q`,  q=n-k.               (2.2)

Consequently,

`0 <= N_k A_q <= sum_{|A|=k}R_A <= c_* N_k k eps_q`,                (2.3)

or equivalently

`0 <= h_q-(q/n)H <= c_*(n-q) eps_q`.                                (2.4)

### Proof

First,

`sum_{|A|=k} I_A = u_k I`.                                           (2.5)

Also `B_A=H-H(X_{A^c})`, so complementing k-blocks gives

`sum_{|A|=k}B_A = N_k(H-h_q)`.                                      (2.6)

Since `u_k=(k/n)N_k` and `H=rI`,

`u_k H - sum B_A
 = N_k[(k/n)H-H+h_q]
 = N_k[h_q-(q/n)H]
 = N_k A_q`.                                                         (2.7)

Now sum `e_A=B_A+R_A-rI_A` and use (2.5)-(2.7):

`sum e_A
 = sum R_A + sum B_A - u_k H
 = sum R_A - N_k A_q`.

This proves (2.2). Since every `e_A>=0`, the left side is nonnegative. The prediction-error theorem gives `R_A<=c_*M_A`; summing and using (1.6) gives (2.3)-(2.4). QED.

### Entropy-profile form

Let `d_q=h_{q+1}-h_q`. Averaging the chain rule over pairs `(B,i)` with `|B|=q`, `i notin B`, gives

`d_q = E_{B,i} H(X_i|X_B)`.                                         (2.8)

The elementary binary inequality `h_2(t)>=2 min(t,1-t)` implies

`eps_q <= d_q/2`.                                                     (2.9)

Therefore every maximal-ratio critical core obeys the all-scale necessary condition

`0 <= h_q-(q/n)H
   <= (1/ln 2)(n-q)(h_{q+1}-h_q)`,  1<=q<=n-1.                       (2.10)

At `q=1`, `nA_1=sum_i h_2(p_i)-H` is total correlation. At `q=n-1`, `nA_{n-1}=H-sum_i H(X_i|X_{-i})` is dual total correlation. Thus (2.10) is a discrete fixed-cardinality interpolation between the two dependence endpoints in the account01 EXIT curve.

# 3. PROVED: high-ratio block descent with the negative Han credit retained

For a proper k-block A, let

`r_A^+ := max_a H(f_a)/I(f_a)`

over nonconstant restriction children, taking constant children to contribute no candidate. Because A is proper and all remaining coordinates are relevant at the parent, `I-I_A>0`.

From the exact restriction telescopes,

`H = Delta_A H + 2^{-k}sum_a H(f_a)`,
`I = I_A       + 2^{-k}sum_a I(f_a)`.

Hence

`e_A = Delta_A H-rI_A
     = 2^{-k}sum_a I(f_a)[r-r(f_a)]`.                               (3.1)

In particular some nonconstant child satisfies

`r(f_a) >= r - e_A/(I-I_A)`.                                        (3.2)

Summing the denominators over all k-blocks gives

`sum_{|A|=k}(I-I_A)=v_k I`.                                         (3.3)

Since all `e_A>=0`, some k-block A obeys

`e_A/(I-I_A)
 <= [sum e_A]/[v_k I]
 = [sum R_A-N_kA_q]/[v_k I]`.                                       (3.4)

This proves the main theorem.

## Theorem 3.1 — Han-credit block descent

For every maximal-ratio restriction core g with n relevant coordinates and every `q in {1,...,n-1}`, there exists a restriction child h obtained by fixing exactly `n-q` physical coordinates such that

`r(h) >= r(g) - Gamma_q(g)`,                                        (3.5)

where the exact toll is

`Gamma_q(g)
 := [sum_{|A|=n-q} R_A - N_{n-q} A_q]
    / [binom(n-1,n-q) I(g)] >=0`.                                   (3.6)

Using `R_A<=c_*M_A` gives the source-admissible upper certificate

`Gamma_q(g)
 <= [n/(q I(g))]
    { c_*(n-q) eps_q - [h_q-(q/n)H(g)] }`.                           (3.7)

The bracket in (3.7) is nonnegative on such a critical core by Theorem 2.1.

This is the exact recursion bridge missing from the preceding proper-block compiler: the cost of descending from n relevant coordinates to at most q is **not** the raw Bayes payment `c_*(n-q)eps_q`; the Han deficit `h_q-(q/n)H` is a mandatory negative credit.

# 4. PROVED: extremal FEI constants satisfy the same recursion

Let

`C_n := max{H(f)/I(f): f Boolean, nonconstant, with at most n relevant coordinates}`.

The maximum exists because there are finitely many Boolean functions after deleting irrelevant coordinates. Let f attain `C_n`, and fix `q<n`. Every restriction fixing `n-q` coordinates has at most q relevant coordinates and therefore ratio at most `C_q`.

For every such block A,

`H <= Delta_AH + C_q(I-I_A)`.                                       (4.1)

Sum (4.1) over all k=n-q blocks and use (2.6):

`v_k H
 <= sum_{|A|=k}R_A - N_k A_q + C_q v_k I`.                      (4.2)

Thus

`C_n-C_q
 <= [sum R_A-N_kA_q]/[v_k I]`                                       (4.3)

for the extremizer f, and hence

`C_n-C_q
 <= [n/(qI)]
    {c_*(n-q)eps_q-[h_q-(q/n)H]}`.                                  (4.4)

Dropping the Han credit and using `M_A<=I_A`, equivalently
`(1/N_k)sum M_A<= (k/n)I`, yields the crude but unconditional recursion

`C_n <= C_q + c_*(n-q)/q`.                                          (4.5)

For q=n-1,

`C_n <= C_{n-1} + c_*/(n-1)`.                                      (4.6)

Therefore

`C_n <= c_* H_{n-1}`                                                (4.7)

with `H_m` the harmonic number. This logarithmic consequence is not claimed as new literature; the point is the strictly sharper source-exact formula (4.4), which exposes exactly where Boolean dependence can improve the recursion.

# 5. Minimal-counterexample form

Fix a candidate coefficient C and suppose f is a counterexample with the minimum number n of relevant coordinates. Put

`delta := H(f)-C I(f)>0`.

Every proper physical restriction child satisfies FEI(C). Hence for every proper block A,

`Delta_AH-CI_A
 = delta - 2^{-|A|}sum_a [H(f_a)-CI(f_a)]
 >= delta`.                                                         (5.1)

Summing over all k=n-q blocks and repeating the calculation gives

`v_k delta <= sum_{|A|=k}R_A-N_kA_q`.                               (5.2)

Thus, for every `1<=q<n`,

`delta
 <= [n/q]{c_*(n-q)eps_q-[h_q-(q/n)H]}`.                         (5.3)

For q=n-1 this gives

`delta <= c_* I/(n-1)`,                                             (5.4)

because `eps_{n-1}=n^{-1}sum_i M_i<=I/n` and `A_{n-1}>=0`.

Equation (5.3) is stronger than saying “every coordinate of a minimal counterexample is locally bad”: **every fixed-cardinality scale carries enough Bayes prediction error, after paying its Han dependence credit, to fund the same global defect delta.**

# 6. Decisive sanity calculation: the three-bit one-point defect

Take the genuine Boolean function on three bits that equals -1 at one cube point and +1 elsewhere. Its spectral masses are

`p_empty=9/16`, and `p_S=1/16` for all seven nonempty S.

Direct Walsh arithmetic gives

`H=2.216917186688699`,
`I=3/4`,
`r=2.955889582251599`.

It is restriction-maximal: a restriction toward the exceptional point is the two-bit one-point defect with ratio exactly 2, while the opposite restriction is constant.

At the singleton-descent scale q=2, direct evaluation gives

`h_2=1.548794940695399`,
`eps_2=1/4`,
`A_2=h_2-(2/3)H=0.070850149569599`.

The exact recombination sum over the three singleton blocks is

`sum_i R_{i}=1.646384822086195`.

Therefore the exact toll in (3.6) is

`Gamma_2
 =[sum_i R_i-3A_2]/[(2)(3/4)]
 =0.955889582251599
 =r-2`.

So Theorem 3.1 lands exactly on the best nonconstant one-bit restriction child in this example. Replacing the exact recombination by the generic `c_*M` bound gives the looser but valid toll `1.300994741749765`. This calculation is only a theorem sanity check, not evidence for global FEI.

# 7. Exact remaining universal obstruction

The current block route no longer has an accounting/lifetime ambiguity. The unpaid object can be stated at each fixed cardinality q as

`T_q(f)
 := c_*(n-q)eps_q - [h_q-(q/n)H] >=0`                              (7.1)

on a maximal-ratio counterexample core.

Theorem 3.1 says a q-dimensional restriction can be reached while losing at most

`[n/(qI)] T_q(f)`                                                   (7.2)

in the H/I ratio.

A dimension-independent FEI proof would follow if Boolean spectral realizability forced an adaptive sequence of scales for which these losses have a universal bounded sum. Generic probability cannot provide this: a rare independent product law has zero Han deficit and positive Bayes error, producing the logarithmic/harmonic obstruction in (4.5). Exact product spectral laws with rare marginals are forbidden by the already-proved Boolean product-spectrum rigidity, but the quantitative statement needed here is stronger:

> **OPEN universal implication (Bayes-Han stability):** quantify how far a Boolean spectral law with rare marginals must move away from the independent entropy profile so that the accumulated `T_q` toll is universally summable.

This is the same KL-scale stability obstruction seen from a different exact coordinate system. The earlier product-phase theorem pays Hellinger-scale distance and is therefore insufficient by itself. The account01 EXIT theorem supplies the continuous erasure tube; (3.5)-(4.4) now show exactly how much failure of that tube must be converted into ratio-preserving restriction descent.

A useful next nonoverlapping ownership split is:
- B14: prove/refute a quantitative Boolean lower bound on the Han deficit or on the Bayes-Han gap at one scale.
- B15: compare packet/free-energy negative credits to `A_q` without dropping KL terms.
- B16: connect signed first-hit/plaquette covariance to a lower bound on `A_q` or a reduction in `eps_q`.
- B17: seek explicit Boolean families maximizing `T_q/I` at several scales.
- B18/account02: integrate any such bound into the exact descent recurrence (3.5)/(4.4), and test whether the resulting scale sequence has a bounded total toll.

# 8. Claim ledger

## PROVED in this run
- Exact aggregate block excess identity (2.2): `sum e_A=sum R_A-N_kA_q`.
- Every restriction-maximal ratio core satisfies the fixed-cardinality Bayes-Han inequality (2.4), and hence the entropy-profile inequality (2.10).
- Han-credit block descent theorem (3.5)-(3.7): for every target cardinality q there is an actual physical restriction child whose H/I ratio loses at most the exact aggregate excess toll.
- Extremal finite-dimensional constants satisfy the exact negative-credit recursion (4.3)-(4.4), with crude corollary `C_n<=C_q+c_*(n-q)/q`.
- Minimal counterexamples satisfy the all-scale defect lower-payment (5.3), with singleton corollary `delta<=c_*I/(n-1)`.
- The three-bit one-point-defect sanity calculation matches the exact singleton descent toll to the observed ratio loss `r-2`.

## CONDITIONAL / inherited
- `Delta_A=B_A+R_A` and `R_A<=c_*M_A` are inherited from account01/B14.
- All-block criticality at a maximal-ratio descendant is inherited from account03/B18.
- Product-spectrum endpoint rigidity, phase/Hellinger stability, packet/free-energy credits, and the new restriction-tree reserve ledger retain their original assumptions and scopes.

## OPEN
- A universal summable bound on the adaptive Bayes-Han tolls `T_q/I`.
- A KL-scale Boolean stability theorem strong enough to turn exact-product rigidity into such a bound.
- Full FEI with a dimension-independent constant.

## REFUTED / NOT CLAIMED
- Dropping the Han credit is not expected to close FEI; it yields only the harmonic/logarithmic recursion.
- The entropy-profile inequality (2.10) is a necessary critical-core condition, not by itself a contradiction.
- The finite n=3 check is not a finite verification of FEI.
- No publication priority or new sharp FEI constant is claimed.

# 9. Current literature check

A fresh 21 September 2026 search still finds unrestricted FEI open. Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for plateaued functions (sharp class constant 4) and partially bent functions (sharp class constant 2), not universally. González--MacManus--Pereyra, arXiv:2606.00246 (29 May 2026), use restriction entropy decrements and stopping binary trees, with the full conjecture conditional on the missing local restriction payment. Han's Combinatorica 2025 bound retains an influence-profile entropy term rather than a dimension-independent FEI constant. The current public optimization-constant record lists the certified monotone lower bound `>6.521845710923046575` and no finite universal upper bound. These checks support the claim discipline above; no novelty-priority inference is drawn from search absence.
