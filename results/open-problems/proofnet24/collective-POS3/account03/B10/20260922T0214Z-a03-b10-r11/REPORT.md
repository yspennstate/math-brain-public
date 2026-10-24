# POS3 account03/B10 — explicit uniform-rank variance cap and a source-parameterized exceptional range

**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair whose ordering probability under the uniform law on all linear extensions lies in `[1/3,2/3]`.  
**Parent status after this report:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact assignment and source-bound collective state

The active owner allocation `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z` assigns account03/B10 to:

> Apply bounded-width/high-variance results to the exact width-three target and derive the remaining exceptional-case requirement with constants/hypotheses explicit.

The assigned partner is **account04/B11**. I consumed its latest complete source-bound report

`proofnet24/collective-POS3/account04/B11/B11-20260922T011236Z-pos3-r12/REPORT.md`

(report blob `e37a40f77dbe414014200d2db8a4cd5601f57d24`). It establishes the source-valid qualitative residue `7 <= pi(P) <= K_3` for any hypothetical width-three counterexample and, crucially, constructs arbitrary-size width-three prime interval orders already at `pi=7` with rank variance at most `49/4` and one-element insertion multiplicity at most `8`. Thus bounded range/variance/local insertion complexity does **not** imply a finite kernel.

I also consumed the newer compatible results:

- account04/B10 handoff blob `a7713fd0ecac31104201ec2a381d55b045a3adc7`: in a hypothetical width-three counterexample every element has its **exact strong-majority rank** with probability `>1/81`; one-sided endpoint cases have probability `>4/9`.
- account02/B10 handoff blob `cc0b07e71d1c01c7741fa83f0058962088511124`: at the first and last strong-majority block boundaries, the majority-direction probability is strictly between `2/3` and `7/9`, and both canonical Hasse-blocker channels are active.
- account01/B19 handoff blob `f1f0eacfcb9f4d908947b7b640944ed6d7b69b34`: the first maximal strong-majority chain block `C` is an order ideal; for `Q=P\C` the exact projected law is weighted by the genuine lift multiplicity `W_C`, every `tau in L(Q)` has one prefix lift, and `e(Q)/e(P)>4/9`.

No projected/deleted law is replaced by a uniform surrogate below. Whenever the uniform law on `L(Q)` is used, it is only as the base measure in the exact identity `e(P)=sum_tau W_C(tau)`.

## 2. External source facts used exactly

Two source results turn the collective pinned-rank atom into an explicit variance statement.

### Stanley rank log-concavity

For a uniformly random linear extension and a fixed element `x`, the sequence

`Pr(rank(x)=k)`

is log-concave. This is the Stanley theorem quoted as Theorem 2.2 in Max Aires and Jeff Kahn, *Variance vs. range for linear extensions, and balancing extensions in posets of bounded width*, arXiv:2510.26134v1 (30 Oct 2025).

### Sharp discrete log-concave min-entropy/variance inequality

Heshan Aravinda, *Entropy-variance inequalities for discrete log-concave random variables via degree of freedom*, Discrete Mathematics 347 (2024), 113683, DOI `10.1016/j.disc.2023.113683`, Theorem 1.4, proves that for any integer-valued log-concave random variable `X`, if

`M(X)=max_k Pr(X=k)`,

then

`M(X)^2 (1 + Var(X)) <= 1`.                                      (2.1)

This is a sharp, numerical form of the qualitative `sigma=Theta(1/q)` relation used by Aires--Kahn.

I also use Aires--Kahn Theorem 3.1: for every `mu>0` and `L` there is a finite threshold `K=K_AK(mu,L)` such that if `(A,B)` is a maximal `mu`-near-maximum incomparable pair, `|B| >= max{mu |A|,K}`, then

`sum_{x in A} sigma(x)^2 >= L |A|`.                              (2.2)

The source states existence of `K`; it does not supply a convenient numerical closed form. I therefore keep that threshold source-parametric rather than inventing a number.

## 3. Uniform-law rank variance is explicitly bounded by 6560

Assume, for contradiction-search purposes, that `P` has width at most three and **no** balanced incomparable pair.

The account04/B10 theorem gives, for every `x in P`,

`Pr(rank(x)=rank_*(x)) > 1/81`,                                  (3.1)

where `rank_*(x)` is the rank of `x` in the transitive strong-majority order. Hence the maximum rank atom satisfies

`q(x):=max_k Pr(rank(x)=k) > 1/81`.                              (3.2)

By Stanley, the rank distribution is log-concave, so Aravinda's inequality (2.1) applies directly to the **actual uniform linear-extension law**:

`1 + Var(rank(x)) <= 1/q(x)^2 < 81^2 = 6561`.

Therefore:

### Theorem 3.1 — explicit all-element variance cap

Every element of a hypothetical width-at-most-three POS3 counterexample satisfies

`Var(rank(x)) < 6560`.                                           (3.3)

Equivalently,

`sigma(P) < sqrt(6560) < 81`.                                   (3.4)

No asymptotic or projected-law approximation is involved.

## 4. The two endpoint majority blocks satisfy the much sharper `65/16` cap

The one-sided `>4/9` estimate can be extended from the global endpoint / first-boundary endpoint already recorded in the collective state to **every element in the first and last maximal strong-majority chain blocks**.

Let `B_1` be the first maximal contiguous block of the strong-majority order lying in one chain, and take `x in B_1`. Every element before `x` in the strong-majority order is an earlier element of that same poset chain, hence is a forced predecessor of `x`. Let `U_x` be the elements after `x` in the strong-majority order and let `M=min(U_x)`. Delete from `M` the members already forced above `x`, leaving `M_0`.

`M_0` is an antichain and every member is incomparable with `x`. Since `width(P)<=3`, the set `{x} union M_0` is an antichain, so

`|M_0| <= 2`.                                                     (4.1)

For every `m in M_0`, no-balancedness and the strong-majority orientation give

`Pr(x precedes m) > 2/3`.                                       (4.2)

Shepp's multivariate XYZ inequality, applied in the order-dual direction when necessary, yields

`Pr(x precedes every m in M_0) >= product_m Pr(x precedes m) > (2/3)^2 = 4/9`.  (4.3)

Preceding all minimal members of the filter `U_x`, together with the already-forced predecessor side, is exactly the event that `x` occupies its strong-majority rank. Thus every `x in B_1` has

`q(x) > 4/9`.                                                     (4.4)

The last block is identical by order reversal. Applying (2.1):

### Theorem 4.1 — endpoint-block variance cap

For every `x` in the first or last maximal strong-majority chain block,

`Var(rank(x)) < (9/4)^2 - 1 = 65/16`.                            (4.5)

This is substantially stronger than the global `6560` bound and is a constraint on whole endpoint blocks, not only the two global endpoint elements.

## 5. Source-parameterized explicit exceptional incomparability range

The account04/B11 partner residue used a qualitative constant `K_3`. The variance cap above identifies a precise source threshold that is sufficient.

Let

`K_* := K_AK(1,6560)`                                            (5.1)

be the finite threshold whose existence is asserted by Aires--Kahn Theorem 3.1 with `mu=1` and `L=6560`.

Choose an incomparable pair of sets `(A,B)` maximizing `|A||B|`; among ties choose an inclusion-maximal one, and orient it so that `|B|>=|A|`. It is a maximal `1`-pair in the sense of Aires--Kahn. If `|B|>=K_*`, (2.2) gives

`sum_{x in A} Var(rank(x)) >= 6560 |A|`,                         (5.2)

whereas (3.3) gives the strict opposite inequality

`sum_{x in A} Var(rank(x)) < 6560 |A|`.                          (5.3)

Contradiction. Hence

`|B| < K_*`, and therefore `|A||B| < K_*^2`.                     (5.4)

For any element `z`, the pair `({z}, Pi(z))`, where `Pi(z)` is the set of elements incomparable with `z`, is an incomparable pair of sets. Consequently the maximum product is at least `pi(P)=max_z |Pi(z)|`. Thus:

### Theorem 5.1 — explicit source-threshold residue

Every hypothetical width-three POS3 counterexample satisfies

`pi(P) < K_AK(1,6560)^2`.                                       (5.5)

Peczarski's 6-thin theorem gives the independent lower bound `pi(P)>=7`. Therefore the bounded-range residue can be written without an unnamed balancing constant as

`7 <= pi(P) < K_AK(1,6560)^2`.                                  (5.6)

The right-hand side is **source-explicit but not numerically evaluated** because Aires--Kahn Theorem 3.1 itself leaves `K(mu,L)` existential. No numerical value for `K_*` is fabricated here.

Together with the inherited exhaustive frontier, any counterexample also has `|P|>=15`; width two is already solved, so a minimal counterexample has width exactly three.

## 6. A new two-sided exact mean window for first-ideal-block deletion

Let `C={c_1<...<c_m}` be the first maximal strong-majority chain block and `Q=P\C`, as in account01/B19. Let

`alpha := e(Q)/e(P)`.

Every `tau in L(Q)` has exactly one prefix lift `C,tau`; hence, under `nu=Unif(L(Q))`,

`E_nu W_C = e(P)/e(Q) = 1/alpha`.                                (6.1)

The event represented by those prefix lifts is exactly the canonical-rank event for `x=c_m`, so the one-sided atom argument gives

`alpha > 4/9`.                                                    (6.2)

Let `y` be the first element of the second strong-majority block. Every prefix lift has `x` before `y`, so

`alpha <= Pr_P(x precedes y)`.                                   (6.3)

The newest account02/B10 exact full-law endpoint product bound gives

`Pr_P(x precedes y) < 7/9`.                                      (6.4)

Thus:

### Corollary 6.1 — exact ideal-block mean window

Under the genuine **uniform** law `nu` on `L(Q)`, used only as the base measure of the exact lift identity,

`4/9 < alpha < 7/9`,                                             (6.5)

and hence

`9/7 < E_nu W_C < 9/4`.                                         (6.6)

Equivalently, the fraction of non-prefix full extensions satisfies

`2/9 < 1-alpha < 5/9`,                                           (6.7)

while

`2/7 < E_nu(W_C-1) < 5/4`.                                      (6.8)

This is a two-sided strengthening of the previous `<9/4` mean bound. It does **not** say that the induced law on `L(Q)` is uniform: the actual projected law remains

`mu(tau)=W_C(tau)/sum_sigma W_C(sigma)`.                          (6.9)

The existing account01/B19/account02/B10 synthesis further gives that, conditional on the non-prefix component, the first boundary is reversed with probability `>2/5`.

## 7. What this does and does not close

The assigned partner's arbitrary-size `pi=7` prime family already has rank variance at most `49/4`, far below `6560`, and one-element insertion multiplicity at most `8`. Therefore Theorems 3.1 and 5.1 **do not** resurrect a finite-census argument. They instead make the exceptional regime numerically honest on the variance side and isolate the exact remaining transfer problem.

The first unpaid actual-uniform-law implication is still the ideal-block / nested-fringe weighted transfer: use the no-balanced touching constraints, the exact weights `W_C`, the first-boundary two active Hasse channels, and the two-boundary nested-profile charge to force either

1. a balanced pair meeting the deleted block, or
2. a weighted orientation ratio in `[1/2,2]` for an incomparable pair in `Q`.

A scalar argument from `E W_C`, bounded variance, or bounded `pi` alone cannot suffice; the partner's `pi=7` family and account01/B19's four-element weighted example rule out those shortcuts.

## 8. Status

- all-element exact-uniform rank variance `<6560`: **PROVED**, from the `>1/81` pinned atom + Stanley + Aravinda.
- first/last majority-block rank variance `<65/16`: **PROVED**.
- source-parameterized residual `7 <= pi(P) < K_AK(1,6560)^2`: **PROVED**.
- first ideal-block exact mean window `9/7 < E W_C < 9/4`: **PROVED**.
- finite-kernel inference from these bounds: **REFUTED / NOT AVAILABLE**, consistent with the assigned partner's arbitrary-size `pi=7` family.
- full POS3 target: **OPEN / NOT PROVED**.

No novelty or priority claim is made. No benchmark material, FEI proof material, credentials, scheduler identifiers, machine paths, unrelated private data, email, Drive, paid model/API/Codex execution, remote workflow, public release, or production-brain mutation was used.
