SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B08, 2026-09-23T03:05:29Z.
attacking: bilateral child-curvature forced by low-cross-rank survivors in the diffuse balanced-cut branch.

# fleet01/B08 auto11 — bilateral curvature in the low-cross-rank diffuse survivors

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Diffuse eigenvector case  
**Status:** `ESSENTIAL_STEP_APPLIED / PROVED_SUPPORTING_STRUCTURAL_THEOREM / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted owner conjecture remains OPEN. The new result is a deterministic, basis-free-in-the-physical-coordinates singular-value consequence of the restricted eigenvector equations. It introduces no moment, support, Gaussian, log-concavity, iid, sign, compactness, connectedness, or post-rotation-independence hypothesis. It keeps the full actual matrix `A`; no small spectral or cross tail is deleted.

A density conclusion is claimed below only in branches already paid by the completed designated partner theorem. Those paid branches have a continuous `C_0` density. The new low-cross-rank branches are structural reductions and do not by themselves prove continuity or bounded density.

## 1. Fresh source state and theorem consumed

Fresh control at the beginning of the run was `yspennstate/math-research-brain` main commit

`a4e0f8faabaaf120b5aad73b2446d9080f78f758`,


The designated completed partner result actually applied is fleet02/B08,

`QFORM-DIFFUSE-HYBRID-VOLUME-TAIL-LADDER-v1`,

canonical source

`yspennstate/math-open-problems@31212dc0982ef58cdae6fc12c9354599a663fad6`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B08/20260923T020620Z-fleet02-B08-QFORM-auto11/REPORT.md`.

Its setup is the following. Choose three genuine orthonormal eigenvectors of the full matrix,

`A R = R Lambda`, `R^T R=I_3`, `min_j |lambda_j|>=L`,

with selected-frame physical row leverage at most `1/48`. The completed diffuse partition gives an ORIGINAL-coordinate cut `I sqcup J` satisfying

`G_I=R_I^T R_I >=(3/8)I_3`, `G_J=R_J^T R_J >=(3/8)I_3`.

Put

`rho=sqrt(3/5)`,
`c0=(L/2)rho`,
`beta=(3L/16)rho`.

For a child, let `k_I` be the number, capped at three, of actual eigenvalues of `A[I,I]` having modulus at least `c0`. The partner's source-valid ladder says:

* `k_I=0`: either `||p_Q||_inf<121.842/L` with a continuous density, or a two-sided physical 3-volume BICOLOP anchor occurs;
* `k_I=1`: either `dist_F(B,rank<=2)<beta/8`, or a continuous density bound `<600.976/L`, or BICOLOP;
* `k_I=2`: either `dist_F(B,rank<=1)<beta/8`, or `dist_F(B,rank<=2)<beta/120`, or a continuous density bound `<36058.550/L`, or BICOLOP;

where `B=A[I,J]`. The same theorem can be applied after interchanging `I,J`, since the cut is balanced on both sides and the cross block is replaced by `B^T`.

The purpose of this run is to determine what the two low-rank tubes FORCE on both physical children simultaneously.

## 2. Main theorem: low cross rank forces bilateral child curvature

For a matrix `M`, write its singular values as

`s_1(M)>=s_2(M)>=...>=0`.

For `r>=0`, write

`d_r(M)=dist_F(M,{rank<=r})=(sum_{j>r}s_j(M)^2)^(1/2)`.

### Theorem 2.1 — `QFORM-BALANCED-CUT-LOWCROSS-BILATERAL-CURVATURE-v1`

Let `A` be real symmetric. Let `R in R^(n x 3)` have orthonormal columns and consist of three genuine full-matrix eigenvectors:

`A R=R Lambda`, `min_j |lambda_j|>=L>0`.

Let `I sqcup J=[n]` be an ORIGINAL-coordinate cut and suppose for some `0<alpha<=1/2`,

`G_I=R_I^T R_I >=alpha I_3`,
`G_J=R_J^T R_J >=alpha I_3`.

Set

`rho=sqrt(alpha/(1-alpha))`, `B=A[I,J]`.

Then for each `r=0,1,2`,

`boxed{
 s_(3-r)(A[I,I]) >= rho L-rho^(-1)s_(r+1)(B),
 s_(3-r)(A[J,J]) >= rho L-rho^(-1)s_(r+1)(B).
}`                                                               (2.1)

Consequently,

`boxed{
 s_(3-r)(A[I,I]), s_(3-r)(A[J,J])
 >=rho L-rho^(-1)d_r(B).
}`                                                               (2.2)

Here the singular values of a symmetric child are precisely the absolute values of its eigenvalues. Thus a cross block close to rank `r` forces **both** children to carry at least `3-r` actual eigenvalues at a fixed scale.

### Proof

Whiten the selected frame on the physical banks:

`U_I=R_I G_I^(-1/2)`, `U_J=R_J G_J^(-1/2)`.

Then `U_I,U_J` have orthonormal columns. Define

`C_I=U_I^T A[I,I] U_I`,
`H=U_I^T B U_J`,
`T=G_J^(1/2)G_I^(-1/2)`.

Restrict `AR=R Lambda` to rows in `I`:

`A[I,I]R_I+B R_J=R_I Lambda`.

Substituting `R_I=U_I G_I^(1/2)`, `R_J=U_J G_J^(1/2)`, left multiplying by `U_I^T`, and right multiplying by `G_I^(-1/2)` gives the exact identity

`C_I+H T=S_I`,
`S_I=G_I^(1/2) Lambda G_I^(-1/2)`.                               (2.3)

Because `G_J>=alpha I`, we also have `G_I=I-G_J<=(1-alpha)I`; likewise with `I,J` reversed. Hence

`s_3(S_I)
 >=s_min(G_I^(1/2)) s_min(Lambda) s_min(G_I^(-1/2))
 >=sqrt(alpha/(1-alpha)) L
 =rho L`,                                                        (2.4)

and

`||T||_op<=sqrt((1-alpha)/alpha)=rho^(-1)`.                      (2.5)

For `r=0,1,2`, the singular-value Weyl inequality

`s_(i+j-1)(X+Y)<=s_i(X)+s_j(Y)`

with `i=3-r`, `j=r+1`, applied to (2.3), gives

`rho L
 <=s_3(S_I)
 <=s_(3-r)(C_I)+s_(r+1)(H T)`.                                  (2.6)

The ideal property for singular values and the fact that `U_I,U_J` are contractions yield

`s_(r+1)(HT)
 <=||T||_op s_(r+1)(H)
 <=rho^(-1)s_(r+1)(B)`.                                         (2.7)

Also

`s_(3-r)(C_I)
 =s_(3-r)(U_I^T A[I,I]U_I)
 <=s_(3-r)(A[I,I])`.                                            (2.8)

Combining (2.6)--(2.8) proves the first inequality in (2.1).

For the second, restrict the same eigen-equation to rows in `J`:

`B^T R_I+A[J,J]R_J=R_J Lambda`.

Whitening on `J` gives

`C_J+H^T T_J=S_J`,
`T_J=G_I^(1/2)G_J^(-1/2)`,
`S_J=G_J^(1/2)Lambda G_J^(-1/2)`.

The same bounds give `s_3(S_J)>=rho L` and `||T_J||<=rho^(-1)`, so the preceding argument proves the second inequality. Finally `s_(r+1)(B)<=d_r(B)` by Eckart--Young, proving (2.2). QED.

### Exact-rank corollary

If `rank(B)<=r`, then `d_r(B)=0`, so each physical child has at least `3-r` eigenvalues of modulus at least `rho L`. In particular, on the `alpha=3/8` diffuse cut:

* `rank(B)<=1` forces **two** eigenvalues of modulus at least `sqrt(3/5)L` in each child;
* `rank(B)<=2` forces **one** eigenvalue of modulus at least `sqrt(3/5)L` in each child.

No statement about the density is inferred merely from this rank fact.

## 3. Apply the designated partner tubes to actual inequalities

Now specialize to the completed `1/48` diffuse cut. Then

`alpha=3/8`, `rho=sqrt(3/5)=0.774596669241483...`,

`beta=(3/16)rho L=0.145236875482778... L`.

### 3.1 Partner rank-one tube

The partner's `k_I=2` survivor may satisfy

`d_1(B)<beta/8`.

Since

`(beta/8)/rho=(3/128)L`,

Theorem 2.1 with `r=1` gives simultaneously

`boxed{
 s_2(A[I,I]),s_2(A[J,J])
 > (sqrt(3/5)-3/128)L
 =0.751159169241483... L.
}`                                                               (3.1)

Thus the alleged 'two child + one cross' low-rank survivor is in fact **bilaterally two-curved**. In exterior notation,

`D_2(A[I,I]),D_2(A[J,J])
 > (sqrt(3/5)-3/128)^2 L^2
 =0.564240097535555... L^2`,                                    (3.2)

and hence

`D_2(A[I,I])D_2(A[J,J])
 >0.318366887666933... L^4`.                                    (3.3)

This is new usable curvature currency on the opposite child; no perturbative deletion of the nonzero cross tail was made.

### 3.2 Partner coarse rank-two tube

The partner's `k_I=1` survivor may satisfy

`d_2(B)<beta/8`.

Theorem 2.1 with `r=2` gives

`boxed{
 s_1(A[I,I]),s_1(A[J,J])
 > (sqrt(3/5)-3/128)L
 =0.751159169241483... L.
}`                                                               (3.4)

So the one-child/two-cross survivor always carries a fixed-scale actual child direction on **both** banks.

### 3.3 Partner tight rank-two tube

The second `k_I=2` survivor may satisfy

`d_2(B)<beta/120`.

Now

`(beta/120)/rho=L/640`,

so

`boxed{
 s_1(A[I,I]),s_1(A[J,J])
 > (sqrt(3/5)-1/640)L
 =0.773034169241483... L.
}`                                                               (3.5)

This is within `0.001563 L` of the exact-rank-two scale `sqrt(3/5)L`.

## 4. Bilateral paid-or-structured ledger

Applying the designated partner theorem from **both orientations** of the same balanced physical cut yields a sharper exhaustive description of the `k<3` diffuse branch.

Let `k_I,k_J` count actual child eigenvalues of modulus at least

`c0=(1/2)sqrt(3/5)L=0.387298334620742...L`.

If either orientation enters a paid branch, then the full ambient quadratic form has a continuous density and, using the worst partner constant,

`boxed{ ||p_Q||_inf <36059/L. }`                                 (4.1)

If either orientation gives BICOLOP, retain that product-preserving two-sided 3-volume anchor.

Assume neither of those conclusions occurs and `k_I,k_J<3`. Then `k_I,k_J` cannot equal zero, because the partner `k=0` alternative has only the paid or BICOLOP outcomes. Hence `k_I,k_J in {1,2}`. Moreover exactly one of the following source-valid survivor types occurs (overlaps are harmless):

**(S11)** `k_I=k_J=1`,

`d_2(B)<beta/8`,

and by (3.4) both children have an actual eigenvalue of modulus greater than

`c_1 L`, `c_1=sqrt(3/5)-3/128=0.751159169241483...`.

**(S22-R1)**

`d_1(B)<beta/8`.

Then (3.1) forces **both** children to have at least two eigenvalues of modulus greater than `c_1 L`; in particular `k_I=k_J=2` automatically.

**(S12/22-R2tight)** at least one side has `k=2`,

`d_2(B)<beta/120`,

and by (3.5) both children have an actual eigenvalue of modulus greater than

`c_2 L`, `c_2=sqrt(3/5)-1/640=0.773034169241483...`.

The only other diffuse state is the already-known **three-child** branch: at least one physical child has three actual eigenvalues of modulus at least `c0`. That branch is not declared solved; naive repeated descent loses fixed spectral scale and still needs a multiscale payment.

This yields the supporting reduction:

### Corollary 4.1 — `QFORM-DIFFUSE-PAID-OR-BILATERAL-CURVATURE-v1`

Under selected-three row leverage at most `1/48`, the completed balanced cut routes the full problem to at least one of:

1. a **paid continuous-density branch** with `||p_Q||_inf<36059/L`;
2. the partner's **two-sided BICOLOP 3-volume anchor**;
3. a **three-curvature physical child** at scale `c0 L`;
4. the **S11** bilateral one-curvature/rank-two-tube state;
5. the **S22-R1** bilateral two-curvature/rank-one-tube state;
6. the **S12/22-R2tight** bilateral one-curvature/tight-rank-two state.

Every object is an actual physical block of the full matrix. No uncancelled selected-eigenvector component is substituted for it.

For the owner target `L>=1`, item 1 gives the universal numerical bound `<36059` on that paid part of the diffuse regime.

## 5. Why this is useful and what it does not prove

The partner's low-rank tubes initially looked like a loss of cross curvature. Theorem 2.1 shows that this curvature cannot disappear: because the selected eigenvectors solve the **actual** eigen-equation, loss of `(r+1)`-st cross singular value is paid by a `(3-r)`-th singular value in **each** principal child. Thus the difficult near-rank-one tube contains two strong child directions on both sides, while the near-rank-two tubes contain one strong child direction on both sides.

This directly complements localized-coordinate conditioning. The next analytic receiver should spend these **two independent physical banks simultaneously**, rather than perturbatively deleting the small nonzero cross tail or recursively following only one child.

What is NOT proved:

* no full density estimate is claimed in S11, S22-R1, S12/22-R2tight, BICOLOP, or the three-child branch;
* no law-uniform characteristic-function perturbation from `B` to a low-rank truncation is used (that mechanism is refuted under the owner quantifiers);
* no arbitrary-joint rank-three coarea bound, conditional projection-density moment, fiber supremum, post-rotation independence, or one-good-minor reciprocal selection is used;
* repeated eigenvalues cause no algebraic problem because the theorem begins with any three genuine full-matrix eigenvectors and uses only their invariant eigen-equation; it does not claim that diffuseness of an arbitrary chosen basis is itself basis-invariant.

## 6. First unpaid implication after this run

`QFORM-BILATERAL-CHILD-CURVATURE-RECEIVER-v1` — OPEN.

Prove a product-preserving analytic estimate for one of the two genuinely new balanced states:

* **two-plus-two / near-rank-one:** each independent physical bank has two actual child eigenvalues `>=c_1 L` while the true cross block is within `beta/8` in Frobenius norm of rank one;
* **one-plus-one / near-rank-two:** each independent physical bank has one actual child eigenvalue `>=c_1 L` (or `c_2 L` in the tight branch) while the true cross block is close to rank two.

The receiver must keep the nonzero cross tail inside the oscillatory/product argument, because small coefficient norm alone is not a law-uniform perturbation under density-cap-one inputs. A promising route is a two-bank fractional-trace or anisotropic Brascamp--Lieb estimate that spends curvature on both banks before absolute values.

Full QFORM and the full continuity conclusion remain OPEN.
