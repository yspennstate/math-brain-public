SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B08, 2026-09-23T22:42:10Z.
attacking: the near-alignment zero-tail endpoint by replacing smallest-singular-value stability with an exact angle-free three-volume identity for a literal original-coordinate crossing.

# account01/B08 r37 — angle-free volume closes the exact rank-two-child endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner continuation consumed:** `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`  
**Owner control:** revision `2026-09-22.15` on the startup refresh  
**Role:** diffuse eigenvector case  
**Classification:** `PROVED SUPPORTING ENDPOINT THEOREM / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**.  The unrestricted continuity conclusion remains **OPEN**.  The endpoint theorem proved below has a continuous `C_0` density.  No moment, compact-support, log-concavity, iid, post-rotation independence, or small-random-perturbation assumption is used.

## 1. First unpaid implication attacked

B08 r36 proved the exact transverse-star amplification theorem after deleting one original coordinate.  In its notation,

`A=[[a,b^T],[b,C]]`,

and if a selected three-eigenvector row has leverage `p<=1/48`, then a small third child singular value forces a large **absolute** star component transverse to the top-two child eigenspace.  The literal-cross `s_3` receiver paid the branch when the star angle was not too small, but its lower bound deteriorated as the star became aligned with the child two-plane.

The first question in this run was therefore:

> Is the alignment itself a genuine obstruction at the exact zero-tail endpoint `s_3(C)=0`, or is it only an artefact of paying the smallest crossing singular value?

It is only an artefact.  The product of the three nonzero crossing singular values has an exact formula in which the aligned star component cancels completely.  Combining that formula with the designated partner's balanced physical half-cut and the checked exact-rank crossing Fourier theorem yields a uniform continuous density `<10.098/L` for the entire diffuse `s_3(C)=0` endpoint, **with no star-angle hypothesis at all**.

This is not a solution of the full conjecture: for `0<s_3(C)<<L`, the child tail creates an additional genuine bilinear crossing which cannot be silently discarded.  The remaining issue is leakage-uniform stability/aggregation, not exact alignment.

## 2. Source-pinned inputs actually used

### 2.1 Previous B08 deletion theorem

The immediately preceding source is

`yspennstate/math-open-problems@e7518cad31bf0381bdf682478ca472a0c08f77b9`,

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260923T213743Z-account01-B08-qform-r36/REPORT.md`.

It proves the following two exact consequences.  Let `R in R^{n x 3}` have orthonormal columns,

`A R=R Lambda`, `min_j |lambda_j|>=L`,

and delete an ORIGINAL coordinate `i`, writing

`A=[[a,b^T],[b,C]]`.

Let `p=||R_{i,*}||^2`.  Let `U` span the top-two absolute-eigenvalue eigenspace of `C`, let `P=UU^T`, and put

`x=s_3(C)/L`, `r=(I-P)b`, `tau=||r||`.

For `x<1`,

`tau >= (1-x)L sqrt((1-p)/p)`.                                  (2.1)

Independently,

`s_2(C)>=sqrt(1-p)L`.                                            (2.2)

Both statements retain the complete ambient matrix and follow from the selected eigenvector equation and the exact identity `(A^2)_{-i,-i}=C^2+bb^T`.

### 2.2 Completed designated partner: account02/B08 balanced half-cut

The completed partner result used at the decisive equation is

`yspennstate/math-open-problems@66582bd87d50634f3525a57c87acffdbde97aea1`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/20260923T153836Z-account02-B08-qform-r28/REPORT.md`, Lemma 3.1.

If `W` is an `m x 3` matrix with orthonormal columns and

`max_j ||W_{j,*}||^2 <=1/48`,                                    (2.3)

then there exists an ORIGINAL-coordinate partition `S disjoint_union T` such that

`I_3/4 <= W_S^T W_S <=3I_3/4`,
`I_3/4 <= W_T^T W_T <=3I_3/4`.                                  (2.4)

This partner result is applied below to the actual frame `[w,U]`; it is not cited only as background.

### 2.3 Exact-rank crossing receiver

The checked source is

`yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`,

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`, Section 1.

For an exact-rank-`r>2` ORIGINAL-coordinate crossing block `B` in

`Q=F(X)+2X^TBY+G(Y)`,

where the scalar coordinates of `X` and `Y` are mutually independent and have densities bounded by one, it gives

`||p_Q||_infinity <= [2r/(r-2)] (s_1(B)...s_r(B))^(-1/r)`.        (2.5)

For `r=3`,

`||p_Q||_infinity <=6 [s_1(B)s_2(B)s_3(B)]^(-1/3)`.              (2.6)

Its characteristic-function majorant is integrable, hence the produced density is continuous and vanishes at infinity.  Arbitrary measurable internal terms `F,G` are permitted, so arbitrary within-bank quadratic terms are retained.

### 2.4 Newest partner update also checked

The chronologically newest account02/B08 handoff checked before this proof is


which source-pins `math-open-problems@34c64bff0ddefd088c372ef60e7a1e1266a18a43`.

It proves `QFORM-THREEEIG-PHYSICAL-PAIR-619-GATE-v1`: if any invertible ORIGINAL-coordinate `2 x 2` principal block has least singular value at least `L/64`, then the full ambient form has essential density `<619/L` (continuity is not claimed in that branch).  Thus, in the endpoint below, any state with such a pair is already paid by the newest partner result; the new three-volume theorem also pays the complementary all-pairs-near-singular state under its stated diffuse endpoint hypotheses.

## 3. Exact angle-free three-volume theorem

Assume the setup of Section 2.1 and now impose

`p<=1/48`,                                                       (3.1)

`s_3(C)=0`.                                                      (3.2)

By (2.2), `s_2(C)>0`, so `C` has **exact rank two**.  Write

`C=U D U^T`,                                                     (3.3)

where `U^T U=I_2` and `D=diag(theta_1,theta_2)` with arbitrary signs.  Equation (2.2) gives

`|theta_1|,|theta_2| >= sqrt(1-p)L`,

hence

`|det D| >= (1-p)L^2`.                                          (3.4)

Equation (2.1) with `x=0` gives

`tau:=||(I-UU^T)b|| >= L sqrt((1-p)/p)>0`.                       (3.5)

Define

`w=(I-UU^T)b/tau`,                                               (3.6)

so `w` is unit and orthogonal to `range(U)`.  Write the full star exactly as

`b=tau w+U beta`, `beta in R^2`.                                 (3.7)

Set

`W=[w,U]`.                                                       (3.8)

Then `W^T W=I_3`.  Assume the assigned diffuse physical-frame gate

`nu:=max_j ||W_{j,*}||^2 <=1/48`.                               (3.9)

Apply the completed account02/B08 partner half-cut (2.4) to this **actual** `W`.  We obtain a partition of the child original coordinates

`{1,...,n-1}=S disjoint_union T`                                (3.10)

such that, with

`G_S=W_S^T W_S`, `G_T=W_T^T W_T`,                              (3.11)

we have

`G_S>=I_3/4`, `G_T>=I_3/4`.                                     (3.12)

Put the deleted hub coordinate `i` on the `T` side.  The literal ORIGINAL-coordinate crossing block of the **actual matrix A** is

`M=[ C[S,T] , b_S ]`.                                           (3.13)

There is no coefficient remainder in (3.13): because `s_3(C)=0`, (3.3) is exact.

### Theorem 3.1 — `QFORM-DELETE1-RANK2-ANGLEFREE-VOLUME-v1`

Under (3.1)--(3.12), `M` has exact rank three and

`boxed:
 s_1(M)s_2(M)s_3(M)
   = tau |det D| sqrt(det G_S * det(U_T^T U_T))
   >= tau |det D|/32.
}`                                                                 (3.14)

In particular,

`boxed:
 s_1(M)s_2(M)s_3(M)
 >= [(1-p)^(3/2)/(32 sqrt p)] L^3
 >= [47 sqrt(47)/1536] L^3.
}`                                                                 (3.15)

The lower bound is completely independent of the aligned coefficient `beta`, equivalently independent of the sine-angle of `b` from `range(U)`.

#### Proof

Express the crossing through the physical frame `W_S`.  For the `T` child columns,

`C[S,T]=U_S D U_T^T
       =W_S [0; D U_T^T]`.                                      (3.16)

For the hub column, (3.7) gives

`b_S=W_S z`, `z=(tau,beta_1,beta_2)^T`.                         (3.17)

Hence

`M=W_S H`,                                                       (3.18)

where `H` is the `3 x (|T|+1)` matrix whose child part is `[0;D U_T^T]` and whose final hub column is `z`.

Let

`G_{T,U}:=U_T^T U_T`.                                           (3.19)

Then

`H H^T
 = [[0,0],[0,D G_{T,U}D]] + z z^T`.                            (3.20)

Because the upper-left base direction is exactly the `w` null direction, the determinant is elementary.  Writing out the blocks,

`H H^T
 = [[tau^2, tau beta^T],
    [tau beta, D G_{T,U}D+beta beta^T]]`.                        (3.21)

Take the Schur complement of the scalar block `tau^2`.  The `beta beta^T` term cancels **exactly**:

`det(HH^T)
 =tau^2 det(D G_{T,U}D)
 =tau^2 (det D)^2 det(G_{T,U}).`                                 (3.22)

This is the key identity.  It is why arbitrarily strong child/star alignment does not cost three-volume.

Since `G_S>0`, `W_S` has full column rank.  The product of the three nonzero eigenvalues of

`MM^T=W_S(HH^T)W_S^T`                                          (3.23)

is

`pdet(MM^T)=det(G_S)det(HH^T)`.                                 (3.24)

Equations (3.22)--(3.24) imply the equality in (3.14).

By (3.12),

`det G_S >=(1/4)^3`.                                            (3.25)

The matrix `G_{T,U}` is the `U` principal block of `G_T`, so (3.12) also gives

`G_{T,U}>=I_2/4`, `det G_{T,U}>=(1/4)^2`.                       (3.26)

Taking square roots in (3.25)--(3.26) yields the factor `1/32`, proving (3.14).

Finally insert (3.4)--(3.5):

`tau |det D|/32
 >= [(1-p)^(3/2)/(32 sqrt p)]L^3`.                              (3.27)

The right-hand side decreases on `0<p<=1/48`, so its minimum there is

`(47/48)^(3/2)*sqrt(48)/32
 =47 sqrt(47)/1536`.                                            (3.28)

This proves (3.15).  In particular the right side is positive, so `rank M=3`.  QED.

## 4. Density consequence: the exact zero-tail diffuse endpoint is paid for all angles

The two banks `X_S` and `X_{T union {i}}` are disjoint collections of the original independent scalar coordinates.  Decompose the full quadratic form using the cut (3.10):

`Q=F(X_S)+2X_S^T M X_{T union {i}}+G(X_{T union {i}})`,          (4.1)

where `F` and `G` are the **actual** within-bank quadratic functions.  No coefficient is dropped, no random variable is rotated, and no moment is invoked.

Apply the exact-rank-three crossing theorem (2.6) to the actual `M`.  Combining (2.6) and (3.15),

`||p_Q||_infinity
 <=6 [1536/(47 sqrt(47))]^(1/3) L^(-1)
 =10.097938622915146... L^(-1).`                                (4.2)

Thus:

### Corollary 4.1 — `QFORM-DIFFUSE-DELETE1-RANK2-ALLANGLES-PAID-v1`

If a symmetric `A` has a selected orthonormal three-eigenvector frame with eigenvalues of modulus at least `L`, and for some original coordinate deletion

`p=||R_{i,*}||^2<=1/48`,
`s_3(C)=0`,
`max_j ||[w,U]_{j,*}||^2<=1/48`,                                (4.3)

with `U,w` defined above, then for every independent cap-one product input law the full quadratic form has a continuous `C_0` density satisfying

`boxed: ||p_Q||_infinity <10.098/L.`                            (4.4)

No condition is placed on

`d=||(I-UU^T)b||/||b||`.

In particular (4.4) remains uniform as `d downarrow0` and the aligned coefficient `||beta||` tends to infinity.

## 5. Why this advances the current near-alignment obstruction

The r36 `s_3`-stability mechanism needed a lower bound on the star angle because, with fixed transverse amplitude `tau`, the structured crossing can have

`s_1(M) ~ tau/d`, `s_2(M)~L`, `s_3(M)~dL`                       (5.1)

as `d downarrow0`.  Paying only `s_3(M)` therefore loses the factor `d`.

The new identity pays instead

`s_1(M)s_2(M)s_3(M)`,                                           (5.2)

and the `d^{-1}` and `d` factors cancel exactly.  Equation (3.22) is stronger than a rough determinant estimate: the entire aligned star vector `beta` disappears algebraically.

Therefore **exact child/star alignment is not itself an obstruction at zero leakage**.  The remaining hard point is that when `s_3(C)=xL>0`, the actual crossing contains the additional bilinear block `C_tail[S,T]`.  Even though `||C_tail||=xL`, it is invalid to call the associated random quadratic term small without moment assumptions, and when `d` is comparable to or below `x`, ordinary smallest-singular-value perturbation can fail.  The current problem is consequently a leakage-uniform product-measure receiver, not an angle problem.

## 6. Concrete use of the newest account02/B08 physical-pair gate

The newest designated-partner theorem gives the following actual dichotomy before invoking Corollary 4.1:

- if some ORIGINAL `2 x 2` principal block `B_pair` has

  `sigma_min(B_pair)>=L/64`,                                    (6.1)

  then account02/B08 gives

  `||p_Q||_infinity<619/L`;                                     (6.2)

- if every ORIGINAL `2 x 2` principal block fails (6.1), the partner's local pair mechanism is unavailable, but Corollary 4.1 still yields the stronger continuous bound `<10.098/L` under the diffuse exact-rank-two-child hypotheses (4.3).

Thus the new endpoint theorem is not merely rediscovering the partner pair gate: it explicitly covers the diffuse all-physical-pairs-near-singular endpoint where a local pair certificate may fail.

## 7. Checks

`CHECKS.md` in this run directory records a deterministic-seed finite-matrix diagnostic.  On 1000 Hadamard-frame trials with random column rotations, balanced physical cuts, signed child eigenvalues, transverse amplitudes, and aligned coefficients spanning several orders of magnitude:

- the exact identity (3.14) had zero violations;
- maximum relative numerical error was `1.45329225428863e-11`;
- the lower bound `prod s_j(M)>=tau|det D|/32` had zero violations.

This computation is only a bookkeeping sanity check.  The proof is (3.16)--(3.28).

## 8. Precise remaining implication

The first remaining B08 implication is

`QFORM-ANGLEFREE-VOLUME-WITH-SPECTRAL-TAIL-v1`:

> Starting from the same diffuse deletion geometry, extend the angle-free zero-tail volume payment uniformly to `0<s_3(C)<<L`, or route the actual spectral tail into a source-valid localized/grouped receiver.  The argument must retain the full bilinear crossing generated by `C_tail`, preserve original-coordinate product provenance, allow arbitrary signs and arbitrary additional spectrum, and remain uniform as both the star angle and `s_3(C)/L` tend to zero.

The zero-tail calculation shows that a proof which still loses solely because `d ->0` is using the wrong currency.  A successful continuation should aggregate crossing volume (or an equivalent product-law invariant) before any reciprocal local-pivot payment.  If tail directions are localized, condition in original coordinates; if diffuse, seek a projected-crossing or volume-sampled estimate for the **actual** tail rather than treating it as a small random error.

Full QFORM status: **OPEN**.  Full-target continuity: **OPEN**.
