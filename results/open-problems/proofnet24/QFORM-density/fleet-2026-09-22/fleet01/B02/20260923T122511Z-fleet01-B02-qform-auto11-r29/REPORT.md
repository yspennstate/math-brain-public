SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B02, 2026-09-23T12:25:11Z.
attacking: integrated Fourier estimate — optimize the collective-tail fractional-volume gate, retaining every volume-marginal constraint and converting failure into an explicit high-leverage physical-hub alternative.

# fleet01/B02 r29 — optimized two-plus-tail fractional-volume Fourier certificate

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Integrated Fourier estimate  
**Status:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Continuity:** proved on the explicit Fourier-`L1` branches below; unrestricted continuity remains open.  
**Target-wide universal Fourier-L1:** `OPEN_NOT_REFUTED`.

The full target remains unchanged: independent ORIGINAL real coordinates with probability densities at most one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No Gaussianity, moments, compact support, connected support, log-concavity, iid assumption, or independence after a spectral rotation is used.

## 1. Current sources actually applied

The new collective-tail marginal certificate is taken from

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`,

`proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/PEER_TAIL_EXTENSION.md`.

For an ORIGINAL-coordinate physical cross block `M`, if

`T2=sum_(j>=3) s_j(M)^2`,

and `P` is any orthogonal projection on the row-index space, with `ell_i=P_ii` and

`epsilon=||(I-P)M||op`,

then the third-volume row marginals obey

`sqrt(alpha_i)<=sqrt(ell_i)+sqrt(3) epsilon/sqrt(T2) sqrt(1-ell_i)`.   (1.1)

The q-dependent sharp Hausdorff--Young three-volume theorem is in the same package. The designated partner fleet02/B02 independently re-audits this calculation, including the admissible endpoint `q=1`, in its current report

`yspennstate/math-open-problems@3c4c6882813d9530dc5c3884ce3e25f5993c7062`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B02/20260923T110948Z-fleet02-B02-QFORM-r11/REPORT.md`.

I apply that partner-checked theorem below to the new exact scalar inequality (2.4); this is equation-level use, not a copied citation.

## 2. Exact optimized marginal envelope

Let `M` have singular values

`s1>=s2>=s3>=...`,

and assume `rank(M)>=3`. Put

`T2=sum_(j>=3)s_j^2>0`.                                        (2.1)

For an orthogonal projection `P`, define

`h=max_i P_ii`,
`beta=sqrt(3)||(I-P)M||op/sqrt(T2)`.                           (2.2)

For `0<=u<=1` set

`F_beta(u)=(sqrt(u)+beta sqrt(1-u))^2`,

and define the exact gate envelope

`A(h,beta)=max_(0<=u<=h) F_beta(u)`.                           (2.3)

Equation (1.1) gives immediately

`alpha_i<=A(h,beta)` for every physical row i.                 (2.4)

The scalar maximization is explicit. Since

`d/du [sqrt(u)+beta sqrt(1-u)]
 =1/(2sqrt(u))-beta/(2sqrt(1-u))`,

the unique interior maximizer is

`u0=1/(1+beta^2)`.

Hence

`A(h,beta)=
  (sqrt(h)+beta sqrt(1-h))^2,  if h<=1/(1+beta^2),
  1+beta^2,                    if h>=1/(1+beta^2).`            (2.5)

In particular, every useful case `A(h,beta)<3/4` automatically lies in the first line of (2.5).

## 3. New theorem — `QFORM-OPTIMIZED-TWOPLUSTAIL-L1-v1`

Let `M=A[I,J]` be any ORIGINAL-coordinate physical cross block with `rank(M)>=3`. Let `P` be any row-index orthogonal projection and define `T2,h,beta,A` as in Section 2. If

`A:=A(h,beta)<3/4`,                                             (3.1)

put

`q_*=max(1,2A)`.                                                (3.2)

Then `1<=q_*<3/2`, and the full ambient quadratic-plus-affine form satisfies

`boxed:
 ||p_Q||infinity
 <= C(A) E3(M)^(-1/6)
 <= C(A) [s1^2 s2^2 T2]^(-1/6),
`

where

`C(A)=3e/[(3-2q_*)sqrt(q_*)]`.                                 (3.3)

More importantly for this slot,

`boxed:
 integral_R |E exp(it X^T A X)| dt
 <=2pi C(A) E3(M)^(-1/6)
 <=2pi C(A)[s1^2 s2^2 T2]^(-1/6).
}`                                                                  (3.4)

The density on this branch is continuous and vanishes at infinity. All same-bank quadratic terms, arbitrary outside original-coordinate couplings, and affine terms remain present.

### Proof

By (2.4), every third-volume row marginal satisfies

`alpha_i<=A<=q_*/2`.                                           (3.5)

The partner-checked q-dependent three-volume theorem therefore applies to the ACTUAL block `M` and gives

`||p_Q||infinity <=[3e/((3-2q_*)sqrt(q_*))]E3(M)^(-1/6)`.      (3.6)

Its proof gives the genuine integrable envelope

`|phi_Q(t)|<=min(1,K|t|^(-3/(2q_*)))`,                         (3.7)

whose integral is exactly bounded by `2pi` times the right side of (3.6). This proves the first inequalities in (3.3)--(3.4).

Finally

`E3(M)=e3(s1^2,s2^2,...)
 >= sum_(j>=3)s1^2 s2^2 s_j^2
 =s1^2 s2^2 T2`,                                               (3.8)

which gives the second inequalities. Since `q_*<3/2`, the exponent in (3.7) is strictly larger than one; Fourier inversion gives a continuous `C_0` density. QED.

### Sharp choice of q within this compiler

For fixed admissible marginal cap `A`, the sharp-HY coefficient

`C_q=3e/[(3-2q)sqrt(q)]`

is strictly increasing for `q>=1`, because

`d/dq log C_q
 =2/(3-2q)-1/(2q)
 =(6q-3)/[2q(3-2q)]>0`.                                       (3.9)

Therefore (3.2) is the best q allowed by this exact compiler; there is no need to keep the previous convenient but nonoptimal choice `q=4/3` when the actual marginal certificate is better.

## 4. Two-sided singular-plane version

Take `P_L` to be the projection onto the top two LEFT singular vectors of `M`, and `P_R` the projection onto the top two RIGHT singular vectors. Put

`h_L=max_i (P_L)_ii`, `h_R=max_j(P_R)_jj`,
`R_tail=T2/s3^2`,
`beta=sqrt(3/R_tail)`.                                         (4.1)

Indeed, for either orientation,

`||(I-P_L)M||op=||(I-P_R)M^T||op=s3`.                         (4.2)

Define

`A_L=A(h_L,beta)`, `A_R=A(h_R,beta)`,
`A_*=min(A_L,A_R)`.                                            (4.3)

If

`A_*<3/4`,                                                      (4.4)

apply Theorem 3 to the better orientation (`M` or `M^T`) and obtain (3.3)--(3.4) with `A=A_*`.

This is a strictly larger collective-tail Fourier branch than the previously recorded `h<=1/2`, `R_tail>=225` certificate.

## 5. Quantitative improvement at the old `R_tail=225` threshold

At

`R_tail=225`, `beta=sqrt(3)/15`.                               (5.1)

The exact leverage threshold solving

`A(h,beta)=3/4`                                                 (5.2)

is most conveniently expressed with

`y=sqrt(h/(1-h))`.

Equation (5.2) becomes

`4(y+beta)^2=3(1+y^2)`,

whose positive root is

`y_*=sqrt(3+12beta^2)-4beta`.                                  (5.3)

Thus

`h_*=y_*^2/(1+y_*^2)=0.63386337224069...`.                     (5.4)

Hence at the same tail-stable-rank threshold 225, the Fourier compiler is valid whenever

`min(h_L,h_R)<0.6338633722...`,                                (5.5)

not merely when that minimum is at most `1/2`.

There is also a constant improvement at the old `h=1/2` boundary. With `h=1/2` and `R_tail=225`,

`A=(1+sqrt(3)/15)^2/2
 =0.62213672050459...`,

so

`q_*=1.24427344100918...`,

and

`C(A)=14.2939411744...`.                                       (5.6)

The previous convenient `q=4/3` choice gave `9sqrt(3)e/2=21.1869...`; the optimized coefficient is about one third smaller. The corresponding Fourier-integral coefficient is

`2pi C(A)=89.8114811688...`.                                   (5.7)

## 6. High-tail-stable-rank failure becomes a physical hub alternative

The optimized formula also sharpens the geometry of failure. Let

`beta_0=3/2-sqrt(2)=0.0857864376...`.

If `h<=2/3`, then

`sqrt(h)+beta sqrt(1-h)
 <=sqrt(2/3)+beta/sqrt(3)`.                                    (6.1)

For `beta<beta_0`, the right side is strictly below `sqrt(3)/2`, because

`sqrt(2/3)+beta_0/sqrt(3)=sqrt(3)/2`.                          (6.2)

Thus if

`R_tail>R_0:=3/beta_0^2
 =407.6467529817...`,                                          (6.3)

then

`min(h_L,h_R)<=2/3  =>  A_*<3/4`,                              (6.4)

and the L1 theorem applies.

Contrapositively, for a cross block with `R_tail>R_0`, failure of the optimized three-volume Fourier gate forces simultaneously

`h_L>2/3`, `h_R>2/3`.                                          (6.5)

Since each rank-two projection has trace two, the set of physical rows with left leverage `>2/3` has cardinality at most two, and the same holds for columns. Therefore the only failure of this collective-tail compiler at very high tail stable rank contains a literal finite physical **hub set** on both sides; it is not a fully diffuse obstruction.

This does not by itself solve the hub case: large leverage does not guarantee a nonzero scalar edge or an invertible physical `2x2` pivot because cancellations remain possible. It does, however, reduce the next structural receiver to at most two super-`2/3` hub candidates per side while every small singular tail is still retained.

## 7. Relation to fleet02/B02's current grouped receiver

The designated partner's current theorem `QFORM-CROSS-SCHUR-SHEAR-GROUPED-L1-v1` states that for a genuine invertible physical `k x k` cross pivot `P`, with cross-Schur residual `S` of rank `r` and `d=k+r>2`,

`||p_Q||infinity
 <=[d/(d-2)] exp(r/d)
   (|det P| Delta_r(S))^(-1/d)`,                               (7.1)

with a genuine `L1_t` characteristic-function proof and no post-shear independence claim.

Thus Section 6 identifies a concrete handoff to that partner mechanism: after the optimized collective-tail exit is removed, one only needs to turn one of the at-most-two heavy physical row/column hubs into either a true invertible physical pivot satisfying (7.1), or prove that every such pivot is singular/near-singular and use the existing nested-coloop, rank-two affine, mixed-hub or ridge mechanisms. I do **not** assert that the pivot automatically exists; the live `QFORM-CROSSMINOR-ALONE-FALSE` correction forbids that shortcut.

The actual partner theorem applied in this run is the q-dependent sharp-HY result at (3.5)--(3.7); equation (7.1) is recorded as the compatible next receiver for the failure geometry.

## 8. Correction audit

No refuted premise is used:

* no law-uniform pointwise quadratic-phase decay;
* no independence after spectral rotation or bankwise shear;
* no arbitrary-joint coarea density theorem;
* no conditional-density cap after sum/difference transformations;
* no deletion of a small quadratic coefficient tail on unbounded laws;
* no inference from a single good physical minor to the full theorem;
* no Gaussian, moment, support, interval-extremality or Monte Carlo assumption.

The only rotations are algebraic singular-vector projections used inside matrix inequalities; the random inputs remain in ORIGINAL independent coordinates throughout the Fourier theorem.

## 9. Remaining implication

The first unpaid interface after this run is

`QFORM-HIGHTAIL-TWOHUB-OR-LOWTAIL-CLOSURE-v1`.

For a candidate cross block, either:

1. the optimized certificate `A_*<3/4` applies, giving the explicit universal-scale Fourier bound (3.4); or
2. at very high tail stable rank, both top-two singular planes have a physical leverage hub `>2/3`, with at most two such hubs per side; or
3. the total tail stable rank/scale is too small for this compiler and must be routed to the existing low-tail/rank-two-tube/nested-coloop programme.

The missing full-target step is still to obtain, from the bare three-large-eigenvalue hypothesis on the FULL symmetric matrix, either a cross block with a dimension-free lower bound on

`[s1^2 s2^2 T2]^(1/6)`

and admissible optimized marginal gate, or a product-preserving hub/low-tail receiver. The full spectral hypothesis does not automatically give that cross-block certificate.

I found no source-valid counterexample to the stronger target-wide statement

`integral_R |E exp(it X^T A X)| dt <= C`.

Accordingly universal Fourier-L1 remains `OPEN_NOT_REFUTED`; the unrestricted bounded-density conjecture and unrestricted continuity conclusion remain OPEN.

## 10. Source status

This report is a supporting analytic theorem and structural reduction, not a full solution. The q-dependent Fourier input has a current fleet02/B02 analytic audit; the new optimized projection/tail synthesis itself has not yet received an independent end-to-end review.
