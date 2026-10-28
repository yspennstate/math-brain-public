SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B17, 2026-09-22T19:04:08Z.
attacking: sharp-constant persistence under full-rank perturbation, and whether singular/rank-three witnesses can be excluded from the full-rank proof search without changing the best constant.

# account03/B17 — invertible-matrix equivalence and full-rank sharp witnesses

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260922T190408Z-account03-B17-QFORM-r15`  
Assignment: sharp constant and witnesses  
Status: `TARGET_LEVEL_REDUCTION + SHARP-WITNESS THEOREM / FULL CONJECTURE OPEN`  
Execution memory: `WITHOUT_VERIFIED_BRAIN`

## 1. Target and correction discipline

The target is the unrestricted essential-density statement: for independent real coordinates with one-dimensional densities bounded by one, and a real symmetric matrix with at least three eigenvalues of magnitude at least one, bound the density of `Q=X^T A X` by one finite universal constant.

This report does **not** use the refuted arbitrary-joint rank-three coarea inequality, the refuted conditional positive-moment interface, pointwise law-uniform quadratic stationary phase, or a diagonalization that preserves false independence. The argument below uses only weak convergence / interval probabilities, exact spectral perturbation, and the completed extreme-product reduction stated in Section 5.

Continuity is kept separate: the new reduction is for the essential `L^infinity` / interval-concentration conclusion and does not transfer continuity through a singular limit.

## 2. Concentration seminorm and weak lower semicontinuity

For a real random variable `Z`, define

`K(Z) = sup_{a<b} P(a<Z<b)/(b-a)`.

If `Z` has a density `p`, then `K(Z)=||p||_infinity` (with the convention `+infinity`), by the elementary interval characterization of bounded densities and Lebesgue differentiation.

### Lemma 2.1 — weak lower semicontinuity

If `Z_k => Z` weakly, then

`K(Z) <= liminf_k K(Z_k)`.

**Proof.** Fix any open bounded interval `I=(a,b)`. Portmanteau gives

`P(Z in I) <= liminf_k P(Z_k in I)`.

Hence

`P(Z in I)/|I| <= liminf_k K(Z_k)`.

Taking the supremum over open intervals proves the claim. No density or moment assumption is used. `□`

This simple observation is the exact direction needed for sharp lower bounds: a singular limiting witness cannot have a larger interval-density constant than all of its approximants.

## 3. Main new reduction: invertible matrices are enough, with the same best constant

Let `A` be any real symmetric `n x n` matrix satisfying the target spectral hypothesis. Let `Pi_0` be the orthogonal projection onto `ker(A)`. For `epsilon>0` define

`A_epsilon = A + epsilon Pi_0`.

Then:

1. `A_epsilon` is invertible;
2. every nonzero eigenvalue of `A` is unchanged;
3. every zero eigenvalue becomes exactly `epsilon`;
4. in particular the original three eigenvalues with magnitude at least one remain unchanged.

For every random vector `X` with finite real coordinates almost surely,

`Q_epsilon - Q = epsilon X^T Pi_0 X -> 0`

almost surely as `epsilon ->0`. No moment assumption is required: for each realized finite vector `X`, the scalar `X^T Pi_0 X` is finite.

Therefore `Q_epsilon => Q`. Lemma 2.1 gives

`K(X^T A X) <= liminf_{epsilon downarrow0} K(X^T A_epsilon X)`.

### Theorem 3.1 — same sharp constant on the invertible subclass

Let

`C_* = sup K(X^T A X)`

over the full target class, and let `C_*^inv` be the same supremum restricted to invertible target matrices `A`. Then

`boxed(C_* = C_*^inv)`.

**Proof.** Trivially `C_*^inv <= C_*`. Conversely, for every admissible possibly singular `A` and product input law, the exact perturbations `A_epsilon` above are invertible and admissible, so

`K(X^T A X) <= liminf_epsilon K(X^T A_epsilon X) <= C_*^inv`.

Taking the supremum over the full class gives `C_*<=C_*^inv`. `□`

### Consequences

- To prove the **essential bounded-density conjecture**, it is enough to prove it for **invertible** `A`; singular matrices then follow with **no loss in the constant**.
- Conversely, if the conjecture is false because a singular target family has unbounded concentration constants, invertible perturbations already carry the same failure: `K(Q)<=liminf K(Q_epsilon)` forces the perturbing constants to diverge as well.
- Thus exact rank three is **not** a separate sharp-constant obstruction. It can be approached from the full-rank class without reducing the concentration constant.

This does not say a proof of the invertible case is easy. It removes only singularity as a logically separate sharp-constant branch.

## 4. Explicit full-rank sequence forcing the `3 sqrt(2)` lower bound

The preceding theorem is abstract. Here is an exact full-rank stress family.

For each integer `m>=2`, put

`u = m^(-1/2) (1,...,1) in R^m`,
`P = u u^T = J_m/m`,
`K = I_m-P`,
`epsilon_m = m^(-2)`.

Define the `3m x 3m` block matrix

`A_m = diag(P+epsilon_m K, P+epsilon_m K, -P+epsilon_m K)`.

Its spectrum is exactly

`{1,1,-1} union {m^(-2) repeated 3m-3 times}`.

So `A_m` is invertible for every finite `m`, and has exactly three eigenvalues of magnitude at least one.

Let the `3m` physical coordinates be iid `Uniform[-1/2,1/2]`, partitioned into three blocks `X^(1),X^(2),X^(3)`. Set

`Y_{j,m}=u^T X^(j)`.

Then

`X^T A_m X = Y_{1,m}^2 + Y_{2,m}^2 - Y_{3,m}^2 + epsilon_m R_m`,

where

`R_m = sum_{j=1}^3 ||K X^(j)||^2 >=0`.

Because every physical coordinate has absolute value at most `1/2`,

`0 <= R_m <= sum_i X_i^2 <= 3m/4`,

hence deterministically

`0 <= epsilon_m R_m <= 3/(4m) ->0`.

By the ordinary one-dimensional CLT applied independently in the three disjoint blocks,

`(Y_{1,m},Y_{2,m},Y_{3,m}) => (G_1,G_2,G_3)`

with independent `G_j~N(0,1/12)`. Slutsky therefore yields

`Q_m := X^T A_m X => Q_infty := G_1^2+G_2^2-G_3^2`.

The density of `Q_infty` at zero is exact. If `sigma^2=1/12`, then

`G_1^2+G_2^2` has density `(2 sigma^2)^(-1) exp(-u/(2sigma^2))`, `u>0`,

and `G_3^2` has density

`[sqrt(2 pi) sigma sqrt(v)]^(-1) exp(-v/(2sigma^2))`, `v>0`.

Therefore

`p_{Q_infty}(0)`
`= integral_0^infty [1/(2sigma^2)]e^{-v/(2sigma^2)} [1/(sqrt(2pi)sigma sqrt(v))]e^{-v/(2sigma^2)} dv`
`= 1/(2 sqrt(2) sigma^2)`
`= 3 sqrt(2)`.

By Lemma 2.1,

`boxed(liminf_{m->infty} K(Q_m) >= 3 sqrt(2))`.

Equivalently, for every `eta>0`, all sufficiently large `m` in this **invertible** family satisfy

`K(Q_m) >= 3 sqrt(2)-eta`.

For these finite-dimensional uniform-cube inputs and invertible `A_m`, the pushforward is absolutely continuous: away from the single critical point `x=0`, the map `x -> x^T A_m x` is a smooth submersion; the critical point has input measure zero. Thus the same statement may be read as an essential-density lower bound.

### Sharp-constant implication

Every universal constant valid even after restricting to invertible matrices must satisfy

`boxed(C >= 3 sqrt(2) = 4.242640687119285... )`.

The established lower bound is therefore **not a rank-deficiency artifact**. A proof of the full-rank case cannot exploit any strict universal gap below `3 sqrt(2)` merely because the extra eigenvalues are nonzero.

## 5. Completed account04 mathematics applied to an actual reduction

The designated `account04/B17` still has no completed QFORM artifact visible in either the shared handoff tree or the canonical QFORM account04/B17 archive at this run. I therefore do not invent one.

I apply the compatible completed `account04/B14` theorem instead:

- repository: `yspennstate/math-open-problems`;
- path: `proofnet24/QFORM-density/fleet-2026-09-22/account04/B14/20260922T114319Z-b14-qform-extreme-reduction-r1/REPORT.md`;
- theorem used: for each interval small-ball problem, the full cap-one product class has the same sharp constant as product indicator densities `1_{E_i}` with `|E_i|=1`, and compact finite unions of intervals suffice by total-variation approximation.

Combining that theorem with Theorem 3.1 gives the concrete equality

`C_*`
`= sup { K(X^T A X) : A invertible, target spectral condition, X_i uniform on compact finite unions E_i, |E_i|=1 }`.

So, **with no loss in the best essential-density constant**, both reductions may be imposed simultaneously:

1. the matrix may be assumed invertible;
2. every input density may be assumed to be an indicator of a compact finite union of intervals of total length one.

There is still no uniform bound on fragment count, diameter, or translation. This joint reduction is a useful exact proof interface for the remaining work: it removes fractional input densities and exact matrix singularity without changing the constant, while preserving the difficult arbitrary fragmentation and rotation.

The explicit witness family in Section 4 already lies inside this reduced class, since every input set is the single interval `[-1/2,1/2]`.

## 6. What this changes in the proof/witness search

This run closes one structural ambiguity in the sharp-constant problem:

> **The full target and the invertible-matrix target have exactly the same optimal essential-density constant.**

Hence observations that some tested full-rank matrices have lower peaks cannot be promoted to a proof strategy based on a universal rank-three-versus-full-rank gap. Arbitrarily small nonzero kernel eigenvalues transfer every singular concentration obstruction into the invertible class.

For B17 witness search, this also means that a future counterexample or stronger lower-bound witness may be designed first in a singular/rank-three geometry when convenient; if it has a high interval concentration constant, the same lower bound is inherited by invertible perturbations.

For proof synthesis, however, the reduction is one-way in regularity: essential `L^infinity` bounds pass to the singular limit, but continuity of the density is **not** weakly closed. The owner's extra continuous-density conclusion remains separately open.

## 7. Remaining implication

The full universal finite upper bound remains open. The present theorem does not control `C_*`; it identifies an equivalent matrix/input subclass and proves that the known `3sqrt(2)` obstruction survives in genuinely full rank.

A nonredundant next B17 step is to attack whether additional eigenvalues bounded away from zero by a *fixed* spectral floor can still approach `3sqrt(2)`, or whether there is a quantitative sharp-constant gap once all noncore eigenvalues satisfy `|lambda|>=delta>0`. That is a different question from mere invertibility and could constrain any proof that splits small and large spectral tails.

## 8. Source state


Full QFORM status: `OPEN / NOT PROVED`.
