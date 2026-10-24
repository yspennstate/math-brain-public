SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B12, 2026-09-24T04:59:49.382903Z.
attacking: relative-accretive carrier stability — replace the latest partner's norm-only destructive budget by the negative symmetric part of the whitened in-range action, then compile an actual five-direction physical cross block through D5 under an arbitrary dense tail.

# account02/B12 — relative-accretive destructive-action stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T045949Z-account02-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Brain status: `WITHOUT_VERIFIED_BRAIN`

## 1. First unpaid implication

The unrestricted conjecture remains OPEN / NOT PROVED / NOT DISPROVED. The current structural debt can be sharpened as follows.

Once an ORIGINAL-coordinate carrier has been found, the latest account03/B12 r49 theorem charges the operator norm of the part of a new local action that falls back into the current carrier image. That norm can be arbitrarily pessimistic: an in-range perturbation of huge norm can be purely rotational/accretive in the carrier's intrinsic metric and cannot reduce the carrier at all.

The theorem below proves that the genuinely harmful quantity is instead the **negative symmetric part of a whitened relative action**. Hence a carrier can fail only through a near-antipodal, near-cancellation direction in this relative metric, not merely because a signed added-spectrum packet is large. The global unpaid implication is therefore narrower: from bare `s_3(A)>=1`, force a bounded ORIGINAL-coordinate carrier for which this relative negative part is controlled, or route the near-cancellation alternative into an already-paid core/pair/cross-volume/projected-crossing/hub/ridge/Schur/common-plane/Pluecker exit. I do not infer such a carrier merely from `s_3(A)>=1`; the live `QFORM-GSTAR-SCALE-FORCING-FALSE-v1` correction forbids that shortcut.

## 2. Source boundary and partner result actually used

Latest compatible partner result read and used:

- account03/B12 r49, `math-open-problems@62da19f9a7ad73a3a65579884463aa3efe93fc2e`,
  `proofnet24/QFORM-density/fleet-2026-09-22/account03/B12/20260924T044434Z-qform-eigenvalue-r49/REPORT.md`.

Its one-step Pythagorean theorem says: for a full-column carrier `M`, with `Pi` the projection onto `Ran(M)`, and an arbitrary local addition `N`, writing

`D=Pi N`, `T=(I-Pi)N`, `g=s_m(M)`, `delta=||D||`, `tau=s_m(T)`,

one has

`s_m(M+N)^2 >= [g-delta]_+^2 + tau^2`.

The source-pinned completed result used for the density step is

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its proved `D_5` theorem is

`||p_Q||_infinity <= 5 sqrt(2e) e_5(M^T M)^(-1/10)`

for any actual ORIGINAL-coordinate cross block `M=A[I,J]`, with no row-marginal condition. Thus `s_5(M)>=g>0` implies

`||p_Q||_infinity <= 5 sqrt(2e)/g`.

No use is made of the false arbitrary-three-dimensional-density coarea interface recorded in the same pinned source.

## 3. Main theorem: relative-accretive carrier stability

Let `M` be a real `p x m` matrix of full column rank and let `N` be any real `p x m` addition. Put

`G=M^T M`, `g=s_m(M)>0`,

and let `Pi=M G^(-1) M^T` be the orthogonal projection onto `Ran(M)`. Define the transverse action

`T=(I-Pi)N`, `tau=s_m(T)`,

and define the **whitened relative in-range action**

`K = G^(-1/2) M^T N G^(-1/2)`.

Let

`alpha = lambda_min( (K+K^T)/2 )`,
`a = [1+alpha]_+`.

### Theorem 3.1 — `QFORM-RELATIVE-ACCRETIVE-CARRIER-STABILITY-v1`

One has

`boxed:
s_m(M+N)^2 >= g^2 a^2 + tau^2.`                                (3.1)

In particular, if `Sym(K)>=0`, then

`boxed: s_m(M+N) >= g`                                           (3.2)

with **no bound at all** on `||N||`, `||Pi N||`, the rank of `N`, or its singular values.

### Proof

Since `M^T(I-Pi)=0`, the in-range part is

`Pi N = M G^(-1) M^T N`.

Let

`U=M G^(-1/2)`.

Then `U^T U=I_m`, so `U` is an isometric embedding. Also

`M+Pi N
 = M(I+G^(-1)M^T N)
 = U (I+K) G^(1/2)`.                                             (3.3)

The vector `(M+Pi N)x` lies in `Ran(M)`, while `Tx` lies in `Ran(M)^perp`. Therefore, exactly,

`||(M+N)x||^2
 = ||(M+Pi N)x||^2 + ||Tx||^2`.                                 (3.4)

For every vector `y`,

`||(I+K)y|| >= |<y,(I+K)y>|/||y||
              >= [1+alpha]_+ ||y|| = a||y||`,                   (3.5)

because only `Sym(K)` contributes to the real quadratic form. Combining (3.3) with `||G^(1/2)x||>=g||x||` gives

`||(M+Pi N)x|| >= a g ||x||`.                                   (3.6)

Also `||Tx||>=tau||x||`. Substitute (3.6) into (3.4) and take the infimum over unit `x`. This proves (3.1). QED.

## 4. It strictly strengthens the partner norm budget

The partner r49 lower bound is recovered automatically. Indeed

`K = U^T (Pi N) G^(-1/2)`,

hence

`||K|| <= ||Pi N||/g = delta/g`.

Therefore

`alpha >= -delta/g`,

so

`g[1+alpha]_+ >= [g-delta]_+`.

Consequently (3.1) implies the partner inequality

`s_m(M+N)^2 >= [g-delta]_+^2 + tau^2`.                           (4.1)

But the implication can be strict by an arbitrarily large factor, because `||Pi N||` sees skew/accretive in-range action that cannot destroy a singular-value floor.

A particularly useful obstruction follows immediately. If for some `0<eps<1`

`s_m(M+N) < eps g`,

then (3.1) forces

`boxed:
lambda_min(Sym K) < -1+eps.`                                    (4.2)

Thus a severe carrier collapse requires a whitened direction whose numerical-range action is nearly `-I`. Huge norm alone is not an obstruction.

## 5. Dynamic version for arbitrary successive signed additions

Let `M_r=M_(r-1)+N_r`, with every `M_(r-1)` full column rank. At step `r` define

`G_(r-1)=M_(r-1)^T M_(r-1)`,
`K_r=G_(r-1)^(-1/2) M_(r-1)^T N_r G_(r-1)^(-1/2)`,
`alpha_r=lambda_min(Sym K_r)`,
`a_r=[1+alpha_r]_+`,
`tau_r=s_m((I-Pi_(r-1))N_r)`.

Then repeated application of Theorem 3.1 gives

`boxed:
s_m(M_r)^2 >= s_m(M_(r-1))^2 a_r^2 + tau_r^2.`                  (5.1)

Dropping the transverse reserve yields the multiplicative estimate

`boxed:
s_m(M_R) >= s_m(M_0) prod_(r=1)^R a_r.`                       (5.2)

In particular every step satisfying `Sym K_r>=0` is completely non-destructive, however large its norm or rank. More generally, if `alpha_r>=-eps_r` with `0<=eps_r<1`, then

`s_m(M_R) >= s_m(M_0) prod_r (1-eps_r)`.

This is a scale-free alternative to an additive operator-norm budget.

## 6. Exact strict-obstruction family: unbounded signed spectrum, zero relative loss

Take two ORIGINAL-coordinate banks `I,J`, each of size five, and baseline symmetric core

`A_0 = [[0, 2 I_5], [2 I_5, 0]].`

Let

`R=[[0,1],[-1,0]]`,
`J_0=diag(R,R,0)`

(the last display is block diagonal), so `J_0^T=-J_0` and `||J_0||=1`. For an arbitrary real parameter `c`, add the symmetric signed packet

`E_c = [[0, c J_0], [-c J_0, 0]].`                               (6.1)

This matrix is symmetric because `(cJ_0)^T=-cJ_0`. Its nonzero eigenvalues are

`+|c|` (multiplicity four) and `-|c|` (multiplicity four),

so it is a literal arbitrarily-large signed spectral packet.

The physical cross block changes from

`M_0=2I_5`

to

`M_c=2I_5+cJ_0`.                                                (6.2)

For this cross carrier, `Pi=I`, `g=2`, `tau=0`, and

`K=(c/2)J_0`,

hence

`Sym K=0`                                                        (6.3)

for every `c`. The new theorem gives

`boxed: s_5(M_c)>=2`                                            (6.4)

uniformly as `|c|->infinity`. In fact

`M_c^T M_c = 4I_5 + c^2 J_0^T J_0 >= 4I_5`,

and because `J_0` has a one-dimensional kernel, equality holds: `s_5(M_c)=2`.

By contrast, the partner r49 norm-only charge has

`delta=||Pi(cJ_0)||=|c|`,

so it yields only

`[2-|c|]_+`,

which becomes zero once `|c|>=2`. This is a concrete obstruction to treating the norm of the in-range action as the right destructive invariant.

## 7. Arbitrary small dense tail and the pinned D5 inequality

Append an arbitrary-dimensional symmetric spectator block `Theta`, with completely unrestricted signs, multiplicities, eigenvalue magnitudes and internal mixing. Then add an arbitrary globally dense symmetric tail `T_dense` satisfying

`||T_dense||_op <= 1/64`.                                       (7.1)

Let `M_final=A[I,J]` be the **actual final ORIGINAL-coordinate cross block**. A physical compression cannot increase operator norm, so

`||T_dense[I,J]||_op <= 1/64`.

Singular-value Weyl applied only to coefficient matrices gives

`boxed:
s_5(M_final) >= 2-1/64 = 127/64.`                              (7.2)

No assertion is made that `X^T T_dense X` is a small random variable.

Now apply the completed pinned `D_5` theorem to this actual final cross block. From (7.2),

`e_5(M_final^T M_final) >= (127/64)^10`.

Therefore

`boxed:
||p_(X^T A X)||_infinity
 <= 5 sqrt(2e)/(127/64)
 = 5.875008457567557... .`                                      (7.3)

The D5 proof permits arbitrary same-bank quadratic blocks, arbitrary exterior couplings and affine terms, and it has no row-marginal gate. Its Fourier inversion also supplies a continuous `C_0` density on this branch.

## 8. The stress family stays in the exact owner target

Before the dense tail, the ten-coordinate core

`[[0,M_c],[M_c^T,0]]`

has eigenvalues `+s_j(M_c)` and `-s_j(M_c)`, `j=1,...,5`. By (6.4), every one has modulus at least two. Adding the arbitrary spectator `Theta` cannot remove those ten singular values. After the dense tail, singular-value Weyl gives

`s_10(A_final) >= 2-1/64 = 127/64 > 1`.                         (8.1)

Because `A_final` is symmetric, its singular values are the absolute values of its eigenvalues. Thus every member of this family has at least three eigenvalues of modulus at least one, uniformly in `c`, in the entire spectator spectrum, and in every allowed dense tail.

This is a source-valid exact-target family with an unbounded signed added-spectrum packet for which the norm-only destructive budget fails completely while the relative-accretive invariant is exact.

## 9. Dense-tail and provenance cautions

The dense tail enters only through deterministic inequalities such as

`||T_dense[I,J]|| <= ||T_dense||`

and singular-value Weyl. It is never treated as a uniformly small quadratic random perturbation; for unbounded cap-one inputs that would be false.

All density receivers act on literal ORIGINAL-coordinate banks. No orthogonal change of variables is used to declare transformed inputs independent. The matrices `G^(-1/2)` and `K` are deterministic analysis devices for coefficient singular values only; they do not rotate the random input law.

## 10. Remaining gap

The full QFORM conjecture remains OPEN / NOT PROVED / NOT DISPROVED.

This run removes one source of artificial loss in the additional-eigenvalue programme: large in-range action is harmless whenever its whitened symmetric part is nonnegative, and any serious collapse forces a relative near-cancellation direction with `lambda_min(Sym K)` close to `-1`.

The still-unpaid structural step is to start only from `s_3(A)>=1` and prove that either a bounded ORIGINAL-coordinate carrier can be chosen so that this relative negative part stays universally away from `-1` (possibly with transverse reserve), or the near-cancellation geometry itself forces one of the already-paid projected-crossing/grouped-bank/hub/ridge/physical-core/physical-pair/Schur/common-plane/Pluecker exits. This report does not claim that extraction and therefore does not claim the universal theorem.

## 11. Sanity check

A deterministic numerical check on 20,000 random full-column matrices `M` and arbitrary rectangular additions `N` tested (3.1) directly. There were zero violations; the minimum numerical margin `s_m(M+N)^2 - (g^2 a^2+tau^2)` in that sample was approximately `0.00475`. This is only a consistency check; the proof is the exact orthogonal identity (3.4).

## 12. Control / source integrity

Fresh control source was resolved from `math-research-brain` main at `2c60050fa1698076d252302c745923da86ebb298` before this run's start write; OWNER CONTROL was revision `2026-09-22.15`, QFORM-only, fleet enabled, no paused account or slot. The live correction state was read before the work and the theorem avoids all known refuted interfaces.

Authenticated native Brain receiver use was not available, so this run remains `WITHOUT_VERIFIED_BRAIN`; repository transport is not being reported as native Brain recall.
