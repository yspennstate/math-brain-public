# Exterior-tail completion for the actual-spectral hybrid

**Result:** `QFORM-DIFFUSE-HYBRID-EXTERIOR-TAIL-v1`  
**Classification:** `ESSENTIAL_STEP_APPLIED / PROVED SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`  
**Scope:** continuation of the same account02/B08 invocation and the same actual physical cut used in `REPORT.md`.

This addendum sharpens the run's volume-tail ladder. It uses only the completed five-volume theorem D5 from the owner-requested source snapshot `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`. Hence it does not rely on the pending-review collective-tail theorem and it imposes no volume-marginal or leverage hypothesis.

## 1. Source-valid input

Let `B=A[I,J]` be an **actual physical cross block**. Write its singular values as

`s_1 >= s_2 >= ... >= 0`.

The completed source theorem D5 states

`||p_Q||_inf <= 5 sqrt(2e) [e_5(B^T B)]^(-1/10)`               (1.1)

whenever `e_5(B^T B)>0`. Same-side blocks and affine terms may be arbitrary, and the proof stays in the original independent coordinates.

For the designated-partner actual-spectral gate, with selected three-eigenvector leverage at most `1/48`, put

`beta = (3/16) sqrt(3/5) L = 0.145236875482778... L`.          (1.2)

If one side of the balanced physical cut retains `k in {1,2}` actual child eigenvalues at the gate, then

`s_(3-k)(B) > beta`.                                             (1.3)

Set

`r=3-k`, `m=5-r=2+k`.                                           (1.4)

Thus `r=2,m=3` in the one-child hybrid and `r=1,m=4` in the two-child hybrid.

## 2. Exterior-tail gate

Define the tail exterior mass

`E_m^(r)(B) = e_m(s_(r+1)^2,s_(r+2)^2,...)`.                   (2.1)

### Theorem 2.1

In either hybrid branch,

`e_5(B^T B) >= beta^(2r) E_m^(r)(B)`.                          (2.2)

Consequently

`||p_Q||_inf
 <= 5 sqrt(2e) beta^(-r/5) [E_m^(r)(B)]^(-1/10)`.              (2.3)

In particular, if

`E_m^(r)(B) >= beta^(2m)`,                                      (2.4)

then

`boxed: ||p_Q||_inf <= 5 sqrt(2e)/beta < 80.271/L.`             (2.5)

If (2.4) fails, then necessarily

`boxed: s_5(B) < beta.`                                         (2.6)

So every unpaid `k=1` or `k=2` hybrid has fewer than five cross singular directions at the actual spectral-gate scale.

### Proof

Because the elementary symmetric polynomial has nonnegative monomials,

`e_5(s_1^2,s_2^2,...)
 >= (product_(j=1)^r s_j^2)
    e_(5-r)(s_(r+1)^2,s_(r+2)^2,...)`.

The actual spectral gate gives `s_j>=s_r>beta` for `j<=r`, proving (2.2). Substitution in D5 gives (2.3). Since `r+m=5`, condition (2.4) makes the right side exactly at most `5 sqrt(2e)/beta`, proving (2.5).

For (2.6), if instead `s_5>=beta`, then the first `m=5-r` tail singular values `s_(r+1),...,s_5` are all at least `beta`; their single product is a monomial in `E_m^(r)` and already equals at least `beta^(2m)`, contradicting failure of (2.4). QED.

### Explicit branch forms

For `k=1`, `r=2,m=3`:

`E_3=e_3(s_3^2,s_4^2,...)`.

If `E_3>=beta^6`, then (2.5) holds; otherwise `s_5<beta`.

For `k=2`, `r=1,m=4`:

`E_4=e_4(s_2^2,s_3^2,...)`.

If `E_4>=beta^8`, then (2.5) holds; otherwise again `s_5<beta`.

The point is that D5 pays **aggregate many-small-direction volume** before any local minor, pivot, or leverage is selected.

## 3. A genuine target family paid only in aggregate

This section checks that the gate is non-vacuous on source-valid matrices with exactly three large eigenvalues and arbitrarily diffuse selected eigendirections.

Let `d=2^q>=128` and let `U` be the normalized `d x d` Sylvester-Hadamard matrix. Put

`C=U diag(p_j) U^T`, `B=U diag(q_j) U^T`,

and

`A=[[C,B],[B,C]]`.                                               (3.1)

The eigenvalues of `A` are `p_j+q_j` and `p_j-q_j`. The selected plus eigenvectors `(u_j,u_j)/sqrt(2)`, `j=1,2,3`, have maximum selected-three-frame coordinate leverage exactly

`3/(2d) <= 3/256 < 1/48`.                                       (3.2)

Take `L=1`, `delta=1/20`, and `beta=(3/16)sqrt(3/5)`.

### 3.1 One-child hybrid

Set

`(p_1,q_1)=(1-delta,delta)`,
`(p_2,q_2)=(p_3,q_3)=(1/5,4/5)`.

For `j>=4`, let `p_j=0`, `q_j=eps_1`, where with `N=d-3`,

`eps_1 = beta / binom(N,3)^(1/6)`.                              (3.3)

Then the only eigenvalues with modulus at least one are the three plus eigenvalues, all equal to one. The physical child `C` has exactly one eigenvalue above the actual child threshold `(1/2)sqrt(3/5)`, while `B` has two singular values `4/5` and `N` individually tiny tail directions.

Since the tail three-volume contains all triples of those `N` equal directions,

`E_3 >= binom(N,3) eps_1^6 = beta^6`.                           (3.4)

Thus D5 gives the actual target inequality

`||p_Q||_inf
 <= 5 sqrt(2e) [(4/5)^4 beta^6]^(-1/10)
 = 40.5648720041...`.                                           (3.5)

At `d=128`, `eps_1=0.01758177174...`, and `eps_1 -> 0` as `d -> infinity`; no individual tiny tail direction pays the estimate.

### 3.2 Two-child hybrid

Set

`(p_1,q_1)=(p_2,q_2)=(1-delta,delta)`,
`(p_3,q_3)=(1/5,4/5)`,

and for `j>=4`, `p_j=0`,

`q_j=eps_2 = beta / binom(N,4)^(1/8)`.                          (3.6)

Again exactly three eigenvalues have modulus at least one. Now `C` has exactly two eigenvalues above the child threshold. The tail four-volume satisfies

`E_4 >= binom(N,4) eps_2^8 = beta^8`,                           (3.7)

hence

`||p_Q||_inf
 <= 5 sqrt(2e) [(4/5)^2 beta^8]^(-1/10)
 = 57.0627539849...`.                                           (3.8)

At `d=128`, `eps_2=0.01944369153...`, again tending to zero with dimension.

These are genuine QFORM instances for arbitrary product sources with density cap one. No Gaussian approximation, support bound, moment assumption, or independence after applying `U` is used: D5 is applied directly to the physical cross block in the original coordinates.

## 4. Designated-partner result actually retained

The latest completed account03/B08 handoff, `QFORM-Q1-AGGREGATE-DESHEAR-COMPILER-v1` / r26, also records the q=0 exact-rank-three cross closure: under its q=0 packet,

`Delta_3(B)>=L^6/2304`,

and if the **actual physical** cross block has exact rank three, the completed whole-cross-block L2 theorem gives

`||p_Q||_inf <= 6*48^(1/3)/L < 21.806/L`.                       (4.1)

This is an actual bounded-density inequality, not a structural currency. Together with Theorem 2.1 it cleanly separates the exact-rank-three boundary from the many-small-direction D5-paid region.

## 5. Remaining hybrid after the new gate

Combine the actual child/cross spectral gate, the main run's rank-tube/BICOLOP ladder, and Theorem 2.1. Every still-unpaid `k=1` or `k=2` hybrid now satisfies the additional invariant

`s_5(B)<beta`,                                                   (5.1)

and more sharply its relevant exterior tail is small:

- `k=1`: `e_3(s_3^2,s_4^2,...)<beta^6`;
- `k=2`: `e_4(s_2^2,s_3^2,...)<beta^8`.

Thus the remaining obstruction is not merely 'hybrid': it is an **actual physical low-exterior-rank/high-anchor survivor**. The first unpaid implication is correspondingly sharpened to

**`QFORM-DIFFUSE-LOWRANK-OR-BICOLOP-PAYMENT-v2` — OPEN.**

Use the retained one/two actual child eigendirections together with a cross block having `s_5<beta` and either a near-rank-one/two tube or the two-sided BICOLOP aggregate currency, without deleting the small quadratic tail. Equivalently, build a source-valid counterexample. Any receiver must aggregate before reciprocal local selection and must retain arbitrary complementary spectrum and original-coordinate product structure.

## 6. Status

This is a supporting theorem and reduction, not a proof of the full QFORM conjecture. It preserves arbitrary independent input densities bounded by one and the full actual matrix. Continuity follows in the D5-paid branches because the source theorem gives an integrable characteristic function. The low-exterior-rank/high-anchor survivor remains open.
