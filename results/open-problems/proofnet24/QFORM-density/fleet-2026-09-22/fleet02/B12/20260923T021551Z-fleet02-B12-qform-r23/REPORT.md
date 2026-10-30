SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T02:15:51Z.
attacking: localized physical-core stability under an arbitrary dense operator-norm tail plus arbitrary-magnitude spectral additions, paid by local rank reserve or hostile inertia rather than by treating the quadratic random perturbation as small.

# fleet02/B12 r23 — local reserve + hostile-inertia stability under dense tails

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Additional eigenvalue control  
**Status:** `PROVED SUPPORTING STABILITY THEOREMS / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. First unpaid implication

The bare hypothesis `s_3(A)>=1` still does not force a bounded physical core with reserve against arbitrary hostile spectral additions.  What is proved below is the exact stability mechanism once a physical core has either (i) `r` extra singular directions beyond the required three, or (ii) enough same-sign threshold count to pay the *hostile inertia of the added spectrum on that core*.  The remaining full-target task is therefore structural: force such a protected core, or force one of the already-paid diffuse-volume / grouped-bank / hub exits, before taking any reciprocal local curvature cost.

The point of the present result is that a completely dense small tail and an arbitrarily large added eigenvalue can coexist safely.  The small dense tail is used only through deterministic matrix perturbation of the actual physical core; it is never asserted that `X^T T X` is a small random variable.

## 1. Sources actually used

1. Newest Claude package required by the owner:  
   `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,  
   `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.
   I read `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.  The completed physical three-coordinate theorem used below is Theorem A of `COUNTEREXAMPLE_SEARCH.md`: if an actual `3 x 3` quadratic matrix has all three eigenvalues of modulus at least `sigma`, arbitrary linear terms allowed, then the density cap is `6 sqrt(pi)/sigma`.  Conditioning on the other ORIGINAL coordinates therefore gives the same bound for a physical `3 x 3` principal block of an ambient form.

2. Finite-core theorem:  
   `yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`,  
   `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`, Corollary 4.1.  On `m>=3` original independent coordinates, an actual symmetric quadratic matrix with three eigenvalues of modulus at least `sigma` has density at most
   `2 sqrt(6 pi m)/sigma`, uniformly in arbitrary affine terms.  The same report's Theorem 5.1 already proves stability under a small dense tail alone; the new step here is to add an arbitrary-magnitude spectral perturbation on top and pay it by local rank/inertia rather than norm.

3. Designated partner `fleet03/B12`:  
   `yspennstate/math-open-problems@2b9f9ccd93e8df4a7bb6b6f4bd3ec351c286976c`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B12/20260923T014701Z-qform-eigenvalue-r22/REPORT.md`.  Its threshold hostile-inertia theorem says, for symmetric `M,E` and `L>0`,
   `N_+(M+E;L) >= N_+(M;L)-nu_-(E)` and
   `N_-(M+E;L) >= N_-(M;L)-nu_+(E)`.
   I apply this to the **compressed final physical core** after first absorbing the dense small tail by Weyl.

All arguments below stay in original coordinates.  No spectral rotation is used to assert independence.

## 2. A rank-reserve lemma

For a matrix `M`, write singular values `s_1(M)>=...>=s_m(M)>=0`.

### Lemma 2.1 — finite-rank perturbations spend at most their rank

If `R` is `m x m` with `rank(R)<=r`, then for `j+r<=m`,

`boxed:  s_j(M+R) >= s_{j+r}(M).`                                    (2.1)

**Proof.** Let `U` be the span of right singular vectors of `M` corresponding to the first `j+r` singular values.  Then `dim U=j+r` and `||Mx||>=s_{j+r}(M)||x||` for `x in U`.  Since `codim ker R<=r`,

`dim(U cap ker R)>=j`.

Choose any `j`-dimensional subspace `S` of this intersection.  On `S`, `(M+R)x=Mx`, so

`min_{x in S, ||x||=1} ||(M+R)x|| >= s_{j+r}(M)`.

The max-min characterization of `s_j(M+R)` gives (2.1). QED.

Also, if `D` is arbitrary with `||D||op<=delta`, Weyl's singular-value inequality gives

`s_k(M+D) >= s_k(M)-delta`.                                         (2.2)

Combining (2.1)-(2.2),

`boxed: s_j(M+D+R) >= s_{j+r}(M)-delta.`                            (2.3)

This is the deterministic matrix statement needed for dense-tail stability.

## 3. Main localized reserve theorem

Let `H` be a set of `m` ORIGINAL coordinates, `m>=3+r`.  Decompose the full symmetric matrix as

`A=A0+T+E`,                                                         (3.1)

with

`||T||op<=delta`                                                    (3.2)

and no rank/sign/magnitude restriction on `T`.  Put

`B0=A0[H,H]`, `D=T[H,H]`, `R=E[H,H]`.                              (3.3)

Compression is contractive, so `||D||op<=delta`.

### Theorem 3.1 — `QFORM-LOCAL-RANK-RESERVE-DENSE-TAIL-v1`

Assume

`rank(R)<=r`, `s_{3+r}(B0)>=L+delta`, `L>0`.                        (3.4)

Then the actual final physical core `B=A[H,H]` satisfies

`boxed: s_3(B)>=L`,                                                 (3.5)

and for every independent cap-one product input and arbitrary ambient outside blocks/couplings,

`boxed: ||p_(X^T A X)||_infinity <= 2 sqrt(6 pi m)/L.`              (3.6)

For `m=3` and `r=0`, the newest-Claude three-coordinate theorem sharpens (3.6) to

`boxed: ||p_(X^T A X)||_infinity <= 6 sqrt(pi)/L.`                  (3.7)

**Proof.** Equation (2.3) with `j=3` gives

`s_3(B0+D+R) >= s_{3+r}(B0)-delta >= L`,

which is (3.5).  Now condition on every original coordinate outside `H`.  The `X_H` remain mutually independent with their original density caps.  The conditional polynomial has quadratic part exactly `B`; every cross coupling to the conditioned coordinates appears only as an arbitrary deterministic affine term.  Corollary 4.1 of the finite-core theorem gives the conditional cap `2 sqrt(6 pi m)/L`, uniformly in the outside value.  Averaging the conditional interval bounds proves (3.6).  When `m=3`, apply Theorem A of the required `e5f71d...` counterexample-search report instead, giving (3.7). QED.

### Spectral-addition formulation

Suppose

`E=sum_a tau_a v_a v_a^T`.                                        (3.8)

No restriction is placed on `tau_a`: they may be arbitrarily small, arbitrarily large, and of either sign.  Since

`range(E[H,H]) subset span{(v_a)_H}`,                              (3.9)

Theorem 3.1 applies whenever the restrictions `(v_a)_H` span at most `r` dimensions.  Thus even **arbitrarily many** added spectral directions are harmless if their footprint on the protected physical core has bounded rank.  Nothing requires the `v_a` to be coordinate axes, and no rotated input variables are introduced.

## 4. Sign-refined theorem: helpful additions are free

The rank-reserve theorem charges every compressed rank direction.  The designated partner result lets us charge only the sign capable of erasing the chosen one-sided core.

### Theorem 4.1 — `QFORM-LOCAL-HOSTILE-INERTIA-DENSE-TAIL-v1`

With the notation above, suppose either

`N_+(B0;L+delta) - nu_-(R) >= 3`,                                  (4.1+)

or

`N_-(B0;L+delta) - nu_+(R) >= 3`.                                  (4.1-)

Then the final physical core has at least three eigenvalues of modulus at least `L`, and

`boxed: ||p_(X^T A X)||_infinity <= 2 sqrt(6 pi m)/L.`              (4.2)

If `m=3`, (4.1+) with `nu_-(R)=0`, or (4.1-) with `nu_+(R)=0`, gives the sharper newest-Claude bound

`boxed: ||p_(X^T A X)||_infinity <= 6 sqrt(pi)/L.`                  (4.3)

**Proof.** Assume (4.1+).  Weyl for ordered eigenvalues under the compressed dense tail gives

`N_+(B0+D;L) >= N_+(B0;L+delta)`.                                  (4.4)

Apply the partner hostile-inertia theorem at threshold `L` to `M=B0+D` and perturbation `R`:

`N_+(B;L) >= N_+(B0+D;L)-nu_-(R)
           >= N_+(B0;L+delta)-nu_-(R) >=3`.                        (4.5)

The negative case is identical.  Condition outside `H` and use the finite-core theorem exactly as in Theorem 3.1.  For `m=3`, use Theorem A from `e5f71d...`. QED.

### Consequence for signed spectral additions

If `R=sum tau_a w_aw_a^T`, then

`nu_-(R) <= # {a: tau_a<0}`,                                      (4.6)

because the negative part has rank at most the number of negative coefficients; positive semidefinite additions cannot create extra negative inertia beyond that rank budget.  Hence, for a positive protected core, arbitrary positive added eigenvalues are free regardless of magnitude and only negative additions spend threshold directions.  The statement with signs reversed is symmetric.

This local theorem is strictly different from the partner's cofinite-global theorem: only the chosen physical core needs the one-sided reserve.  The ambient matrix may have arbitrarily many eigenvalues of both signs and arbitrary outside couplings.

## 5. Concrete target-class inequalities

### 5.1 Arbitrary rank-one addition of either sign + arbitrary dense small tail

Let `H` contain four original coordinates and suppose

`B0=(1+delta) diag(1,1,-1,-1)`,                                    (5.1)

with `0<=delta<infinity`.  Let `T` be **any** symmetric ambient matrix with `||T||op<=delta`, and let

`E=tau vv^T`                                                       (5.2)

for arbitrary `tau in R` and arbitrary ambient `v`.  Then `rank(E[H,H])<=1` and `s_4(B0)=1+delta`, so Theorem 3.1 with `r=1`, `L=1` gives

`boxed: s_3(A[H,H])>=1`,                                          (5.3)

and therefore

`boxed: ||p_(X^T A X)||_infinity <= 4 sqrt(6 pi)
       = 17.366430109398... .}`                                   (5.4)

The bound is independent of `tau`, including `tau -> +infinity`, `tau -> -infinity`, or `tau ->0`.  It is also independent of the rank and sign pattern of the dense tail `T`.  Since singular values of a principal submatrix do not exceed the corresponding singular values of the full matrix, (5.3) itself certifies that the final full matrix lies in the target class.

### 5.2 Helpful-sign addition needs no fourth reserve direction

Let `|H|=3`, `B0=(1+delta) I_3`, `||T||op<=delta`, and let `E[H,H]` be any positive semidefinite matrix of arbitrary norm.  Then `nu_-(E[H,H])=0`, so Theorem 4.1 gives

`N_+(A[H,H];1)>=3`.

Applying the required newest-Claude Theorem A to this **actual final three-coordinate core** gives the real ambient inequality

`boxed: ||p_(X^T A X)||_infinity <= 6 sqrt(pi)
       = 10.634723105433... .}`                                   (5.5)

This is the requested application of a completed `e5f71d...` result: arbitrary dense small tails and arbitrarily large helpful-sign added eigenvalues coexist with a uniform output-density bound, while all outside quadratic dependence is retained exactly.

## 6. Sharp obstruction for a fixed three-core

The extra reserve in Theorem 3.1 is not an artifact of the proof.  A fixed physical three-core cannot survive an arbitrary rank-one hostile addition without additional structure:

`B0=L I_3`, `R=-L e_1e_1^T`                                      (6.1)

gives

`B0+R=diag(0,L,L)`,                                                (6.2)

which has only two singular values at least `L`.  Thus a theorem based only on `s_3(B0)>=L` cannot keep the same fixed core under arbitrary rank-one additions of either sign.  One must supply a fourth reserve direction, exploit the sign as in Theorem 4.1, or switch to another physical/aggregate certificate.  This is an obstruction to a proof interface, not a counterexample to QFORM.

## 7. Why small matrix norm is not used as small random error

For any `delta>0`, let `T=delta e_1e_1^T` and take an admissible cap-one law `X_1~Uniform[R,R+1]`.  Then

`X^T T X = delta X_1^2 >= delta R^2` almost surely.                (7.1)

Hence `||T||op<=delta` gives no law-uniform pointwise or probabilistic smallness of the quadratic perturbation on unbounded product inputs.  The proofs above use `delta` only to certify eigenvalues/singular values of the **actual final physical matrix**, after which original-coordinate conditioning supplies the density estimate.

## 8. Checks and scope

A deterministic random-matrix sanity check tested (2.1) across dimensions `4..10` and all admissible reserve ranks, and tested the threshold/inertia composition (4.5) under random dense tails.  No violation was found.  These computations are not proof premises; Sections 2-4 are analytic.

**What is proved:** a dimension-free localized-core stability theorem under a full-rank dense operator-norm tail plus arbitrary-magnitude low-rank / low-footprint-rank spectral additions; and a sign-refined version charging only hostile compressed inertia.

**What is not proved:** the bare three-large-eigenvalue hypothesis does not yet force a core satisfying (3.4) or (4.1).  Diffuse exact-rank-three matrices can have no uniformly conditioned bounded physical core.  The full QFORM conjecture therefore remains `OPEN / NOT PROVED / NOT DISPROVED`.

**Continuity:** not claimed by the present argument; the target here is the universal essential density bound.
