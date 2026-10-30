SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B07, 2026-09-24T11:00:08Z.
attacking: the r52 bounded-heavy captured packet — replace the contaminated bordered-minor compiler by a joint top-two principal/boundary row-carrier cut, retaining the full operator tails and aggregate volume.

# fleet02/B07 r52 — joint principal/boundary carrier compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: coordinate minor selection / complementary constructions and source-valid counterexamples  
Status: **NEW JOINT-R4 PHYSICAL-CUT THEOREM / CAPTURED DIFFUSE BRANCH PAID / <=64-COORDINATE CARRIER-HEAVY RESIDUAL / PINNED-e5 FRACTIONAL INEQUALITY APPLIED / FULL QFORM OPEN**.

The full unrestricted conjecture and full-target continuity remain OPEN. Every coordinate in this report is an original physical coordinate. No moment, compact-support, connected-support, iid, log-concavity, post-rotation independence, pointwise stationary-phase estimate, arbitrary-joint coarea estimate, or universally good individual minor is used. Small matrix tails are retained as matrix tails in the actual crossing, not discarded as small random quadratic perturbations.

## 1. First unpaid implication after this run

`QFORM-R52-JOINT-CARRIER-HEAVY64-OR-SPECTRAL-ESCAPE-RECEIVER-v1`.

On the latest completed fleet03/B07 r52 captured packet, the two separate mixed `1 principal + 2 boundary` and `2 principal + 1 boundary` bordered-compilation debts can be bypassed. The entire captured packet is now paid whenever the joint top-two principal/boundary row carrier is diffuse after removing a bounded heavy set. What remains is a physical set of at most 64 coordinates carrying at least half of one direction of that joint carrier, plus the partner's separate spectral-escape branch, the T-side three-curvature branch, and the earlier same-bank-star branch.

The old one-pivot route is intentionally not used: a previously constructed exact target family has order-one edge-times-`E_2` currency but its pair Schur correction cancels a rank-one component and leaves the far `E_2` exactly zero. Any compiler that silently assumes the partner's `E_2` bank survives bordered Schur completion is therefore false.

## 2. Fresh incoming state and dependencies

Latest completed designated partner consumed before publication:

`yspennstate/math-open-problems@4f5ee2dc112f258cb5dad4c9be03a9ae3573be6b`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B07/20260924T104017Z-fleet03-B07-qform-r52/REPORT.md`.

Its r51/r52 state provides a literal physical packet `K` with

`m=|K|<=895`,

and selected target eigenvectors `U` for three eigenvalues of modulus at least one. Writing

`B=A[K,K]`, `D=A[K,K^c]`,
`a_K=lambda_min(U_K^T U_K)`,

it separates spectral escape `a_K<1/4`. On the captured branch `a_K>=1/4`, unless an earlier physical-core exit has already paid the law, one has `m>=3` and

`s_3(B)<1/64`.                                             (2.1)

The partner's exact spectral ladder is

`s_{3-k}(D)^2 >= (a_K-s_{k+1}(B)^2)_+`, `k=0,1,2`,

and its mixed determinant packets spend row-deleted `E_2` weights without claiming a single good minor.

For analytic payment I use the completed marginal-free physical-crossing theorem

`QFORM-Z3-CROSSING-MARGINAL-FREE-v1`

from fleet02/B03, source-pinned at `math-open-problems@df738b7f0821d9af56dfd992cab10ecc6704e3fb`: for every literal physical cut `M=A[I,J]` with

`Z_3=e_3(MM^T)>0`,

all same-side blocks, outside coordinates and affine terms arbitrary,

`||p_Q||_infinity <= C3 Z_3^(-1/6)`,
`C3=3*2^(4/3)*e^(1/3)=10.550168831164775...`,             (2.2)

and the density on that branch is continuous.

The mandatory pinned source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` is used separately in Section 6 at an actual live partner inequality.

## 3. Joint rank-four carrier theorem

### Theorem 3.1 — `QFORM-CAPTURED-JOINT-R4-CARRIER-CUT-v1`

Assume the captured state

`a_K>=1/4`, `s_3(B)<eps`, `eps=1/64`.                         (3.1)

If `s_3(D)>=eps`, the physical boundary cut `K|K^c` itself gives

`Z_3(D)>=s_3(D)^6>=eps^6`,

so (2.2) yields

`||p_Q||_infinity <= C3/eps
                    =64 C3
                    =675.2108051945456... .`                    (3.2)

Hence suppose also

`s_3(D)<eps`.                                                   (3.3)

Let `B_2` be the best rank-at-most-two spectral truncation of the symmetric `B`, and let `D_2` be the best rank-at-most-two SVD truncation of `D`. Define the positive semidefinite joint row carrier

`C_0=B_2^2+D_2D_2^T`.                                         (3.4)

Then

`lambda_3(C_0) >= gamma:=1/4-2eps^2=511/2048`.                 (3.5)

In particular `r_0:=rank(C_0)` is 3 or 4.

Let `R` be an `m x r_0` orthonormal frame spanning `range(C_0)`, and let

`ell_h=||R_{h,*}||_2^2`, `delta=max_h ell_h`.                  (3.6)

If

`delta<=1/(4r_0)`,                                             (3.7)

there is a literal physical partition `K=I disjoint_union J` for which, after putting every coordinate of `K^c` on the `J` side,

`M=A[I,J union K^c]`                                          (3.8)

satisfies

`boxed:
 s_3(M) >= mu_0
 :=(1/4)sqrt(511/2048)-sqrt(2)/64
 =0.1027807831124968... .`                                    (3.9)

Consequently the entire ambient law has continuous density and

`boxed:
 ||p_Q||_infinity <= C3/mu_0
 =102.64728981114382... .`                                    (3.10)

No individual `3x3` minor is selected.

### Proof

Because the chosen three eigenvalues have squared magnitudes at least one,

`A^2>=UU^T`.                                                   (3.11)

Taking the `K x K` principal block gives

`B^2+DD^T>=U_KU_K^T`.                                         (3.12)

Since `a_K>=1/4`, the third eigenvalue of the left side is at least `1/4`. The discarded squared tails

`B^2-B_2^2` and `DD^T-D_2D_2^T`

are PSD and have operator norms `s_3(B)^2<eps^2` and `s_3(D)^2<eps^2`. Weyl therefore gives (3.5). Since each summand in (3.4) has rank at most two, `3<=r_0<=4`.

Apply the balanced physical-cut lemma to the orthonormal row frame `R`. With independent Rademacher signs, the signed Gram matrix has expected squared Frobenius norm at most `r_0 delta`; hence some sign choice yields a partition `K=I union J` with

`R_I^T R_I, R_J^T R_J >= g I_{r_0}`,
`g=(1-sqrt(r_0 delta))/2>=1/4`.                                (3.13)

Define the base crossing

`M_0=[B_2[I,J], D_2[I,:]]`.                                   (3.14)

The range of `B_2` is contained in `range(C_0)`: for positive semidefinite `P,Q`, `ker(P+Q)=ker P intersect ker Q`, so `range(P)` and `range(Q)` are contained in `range(P+Q)`. Writing `B_2=W Lambda W^T`, the lower Gram bound on `R_J` therefore implies

`W_J^T W_J>=gI`,

and hence

`B_2[I,J]B_2[I,J]^T
 =W_I Lambda(W_J^TW_J)Lambda W_I^T
 >=g(B_2^2)[I,I]`.                                            (3.15)

The outside block is not cut on its column side, so

`D_2[I,:]D_2[I,:]^T=(D_2D_2^T)[I,I]
                    >=g(D_2D_2^T)[I,I]`,                      (3.16)

because `g<=1`. Thus

`M_0M_0^T>=g C_0[I,I]`.                                       (3.17)

Write `C_0=R Theta R^T` on its range. The nonzero spectrum of `C_0[I,I]` is that of `Theta^(1/2)(R_I^TR_I)Theta^(1/2)`, so (3.13) gives

`lambda_3(C_0[I,I])>=g lambda_3(C_0)>=g gamma`.                (3.18)

Combining (3.17)-(3.18),

`s_3(M_0)>=g sqrt(gamma)>=(1/4)sqrt(gamma)`.                   (3.19)

The actual crossing differs by the horizontal concatenation

`E=[(B-B_2)[I,J], (D-D_2)[I,:]]`.

Therefore

`||E||_op^2
 <=||(B-B_2)[I,J]||_op^2+||(D-D_2)[I,:]||_op^2
 <2eps^2`.                                                     (3.20)

Weyl gives (3.9). Then `Z_3(M)>=s_3(M)^6` and (2.2) gives (3.10). QED.

The proof uses the entire aggregate third volume of the actual crossing. It does not infer a universally large individual minor, and the nonzero tails remain in `M` through (3.20).

## 4. Removing all heavy carrier rows: a <=64-coordinate residual

The pointwise condition (3.7) can be sharpened into a bounded physical localization alternative.

### Corollary 4.1 — `QFORM-JOINT-CARRIER-HEAVY64-v1`

In the state (3.1)-(3.5), put

`H={h in K: ell_h>1/(4r_0)}`.                                 (4.1)

Since `sum_h ell_h=r_0`,

`|H|<4r_0^2<=64`.                                             (4.2)

Let `L=K\H` and `G_L=R_L^T R_L`. If

`lambda_min(G_L)>1/2`,                                        (4.3)

then a physical cut with row side contained in `L` pays the full ambient law with

`boxed:
 ||p_Q||_infinity <728.664.`                                  (4.4)

If (4.3) fails, then there is a unit carrier vector `z in R^{r_0}` such that the bounded physical set `H` captures at least half its squared coordinate mass:

`boxed:
 ||R_H z||_2^2>=1/2,
 |H|<=64.`                                                     (4.5)

Thus failure of the paid diffuse carrier branch forces an actual bounded physical carrier-heavy packet.

### Proof

Assume (4.3). Normalize the residual frame by

`V=R_L G_L^(-1/2)`, so `V^TV=I_{r_0}`.                         (4.6)

Every residual row has normalized leverage

`||V_{h,*}||^2
 <= ell_h/lambda_min(G_L)
 <1/(2r_0)`.                                                   (4.7)

The same Rademacher argument therefore partitions `L=I union J_L` with relative Gram lower bound

`V_I^TV_I,V_{J_L}^TV_{J_L}
 >=a_* I`,
`a_*=(1-1/sqrt(2))/2`.                                        (4.8)

Returning to the original carrier,

`R_I^TR_I,R_{J_L}^TR_{J_L}
 >=g_* I`,
`g_*:=a_*/2=(1-1/sqrt(2))/4
       =0.07322330470336313... .`                              (4.9)

Put `J=J_L union H` and again all `K^c` on the `J` side. Adding the `H` columns can only increase the internal-column Gram, so the proof of Theorem 3.1 applies with `g_*` in place of `g`. Hence

`s_3(M)
 >=g_*sqrt(gamma)-sqrt(2)/64
 =0.014478794397986532... .`                                  (4.10)

The marginal-free physical-`E_3` receiver gives

`||p_Q||_infinity
 <=C3/[g_*sqrt(gamma)-sqrt(2)/64]
 =728.6634882136261...`,                                      (4.11)

proving (4.4).

If (4.3) fails, choose unit `z` with `z^TG_Lz<=1/2`. Since `R^TR=I` and `G_H=I-G_L`,

`||R_Hz||^2=z^TG_Hz>=1/2`,

which is (4.5). QED.

This is the promised integration into coordinate-core extraction: the diffuse joint carrier is paid before any minor inversion; otherwise a literal set of at most 64 physical coordinates captures a fixed fraction of an actual carrier direction. The next receiver must use this bounded heavy packet together with the remaining carrier/boundary structure rather than pretend that the packet itself already has three large principal eigenvalues.

## 5. Why the bordered-`E_2` compiler is not used

The exact B07 regression from the earlier no-pivot work remains mandatory. There are target-valid matrices with four eigenvalues of modulus at least one, every fixed-cardinality physical principal core degenerating, and an incoming anchor-edge-times-`E_2` bank of order one, but an exact zero-diagonal pair Schur correction cancels one rank-one component of the far crossing and leaves its `E_2` equal to zero.

Therefore partner r52's inequalities

`B_hk^2 Z_{-h}>1/(2048m^2)`

and

`t_h Z^B_{-h}>1023/(1048576m)`

are genuine aggregate structural currency but cannot, by themselves, be inverted through a pair completion. Theorem 3.1 avoids the obstruction by forming the joint PSD carrier `B_2^2+D_2D_2^T` before the physical cut and by restoring both operator tails only after the crossing has acquired a third singular value.

## 6. Mandatory pinned `e5f71d79...` result applied to the live packet

The exact pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

proves the `D_k` volume argument and the Fourier-to-fractional-potential conversion. Running its `q=2` Jensen form at `k=2` gives, for every actual physical cut with

`Z_2=e_2(MM^T)>0`,

`H_(1/4)(Q):=sup_s E|Q-s|^(-1/4)
 <=3.929132 Z_2^(-1/16)`.                                     (6.1)

No two-volume marginal gate is needed, and arbitrary same-side quadratic curvature and affine terms remain.

On the partner's live mixed `1 principal + 2 boundary` state,

`Z_2(D)>=1/64`.                                                (6.2)

Hence the actual physical boundary cut satisfies the concrete inequality

`boxed:
 H_(1/4)(Q)
 <=3.929132*64^(1/16)
 =5.09545379304503... .`                                      (6.3)

This is a real analytic payment of the partner's aggregate determinant bank, but it is only quarter-Riesz currency. It is not relabelled as a bounded density. The exact cancellation construction of Section 5 explains why trying to turn (6.3) into a density merely by one hyperbolic pair peel is invalid. The new third-singular-value compiler in Sections 3-4 is what upgrades the diffuse captured branch to actual density currency.

## 7. Remaining endpoint

After this run the captured bounded packet has the following rigorous route:

1. `s_3(D)>=1/64` -> paid physical `E_3`, bound `675.211`;
2. `s_3(D)<1/64` and the joint rank-3/4 carrier remains sufficiently diffuse after removing heavy rows -> paid physical `E_3`, bound `<728.664` (and `<102.648` under the stronger global diffuse gate);
3. otherwise a literal set `H`, `|H|<=64`, captures at least half of one joint-carrier direction.

The first unpaid implication is therefore

`QFORM-R52-JOINT-CARRIER-HEAVY64-OR-SPECTRAL-ESCAPE-RECEIVER-v1`:

consume the bounded `H` packet of (4.5) without assuming it already supplies three principal eigenvalues; preserve the residual carrier, all `H` couplings and arbitrary same-side curvature. Separately return the partner's `a_K<1/4` spectral escape to the diffuse finite-carrier machinery. The r51 T-side three-curvature branch and earlier `E_star>1` same-bank-star branch remain distinct and unpaid.

**Full unrestricted QFORM: OPEN / not proved / not disproved. Full-target continuity: OPEN.** Continuity is established only on the physical-`E_3` exits used above.
