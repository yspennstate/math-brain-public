SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B13, 2026-09-24T10:42:46.175924Z.
attacking: consume partner account03/B13 r48 against the completed arbitrary-rank physical-pair receiver; eliminate its non-ultracollapse branch and sharpen the surviving exact-rank-two normal form without deleting rough tails.

# account02/B13 r13 — partner-r48 pair branch eliminated; forced ultracollapse and scope correction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T104246Z-account02-B13-QFORM-r13`  
Role: extremal product laws / complementary constructions and source-valid counterexamples  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **NEW SUPPORTING REDUCTION / FULL UNRESTRICTED QFORM OPEN / FULL-TARGET CONTINUITY OPEN**.

No moment, compact-support, log-concavity, connected-support, diagonal-basis, post-rotation-independence, bounded-diameter, fixed-fragment-count, or attained-bathtub-optimizer assumption is used. No coefficient-small quadratic random term is deleted.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-ULTRACOLLAPSE-RANK1-4DIAG-ROUGH-RECEIVER-v1`:

> In the forced high-density diffuse exact-rank-two survivor, prove a product-preserving density/small-ball receiver for
> \[
> A=D_C+\lambda_1vv^T+E_{\rm sep}+\lambda_2ww^T,\qquad |C|\le4,
> \]
> with
> \[
> \|E_{\rm sep}\|_{op}\le 2\sqrt{30\pi}\,\rho^{-1},\qquad
> |\lambda_2|<32\sqrt6\,e\,\rho^{-2},
> \]
> while retaining both tails inside the actual phase for arbitrary fragmented/unbounded cap-one product laws. Equivalently, construct a genuine finite-union/unit-product counterexample in this sharpened normal form if such a receiver fails.

The secondary entangled carrier is now two powers of `rho` below unit scale; the genuinely rough obstruction is the separable `O(rho^-1)` diagonal tail together with the affine/grouping issue described in Section 6.

## 2. Fresh compatible inputs

Fresh brain-main control remained QFORM-only under OWNER CONTROL revision `2026-09-22.15`, with no account02/B13 stop. The full theorem and full-target continuity remain open.

The newest completed designated-partner result is account03/B13 r48:

`yspennstate/math-open-problems@ba4c0f14cf9ca505e346b284a530662c6522b514`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B13/20260924T095803Z-account03-B13-qform-r48/REPORT.md`.

In the surviving diffuse exact-rank-two chamber
\[
A=D+U\Lambda U^T,\qquad U^TU=I_2,\qquad
\max_i\|u_i\|^2\le\frac13,\qquad s_3(A)\ge1,
\tag{2.1}
\]
put
\[
H:=\sqrt{1536e^2}=16\sqrt6\,e,
\qquad
\rho_0:=8\sqrt H=82.572423603571\ldots .
\tag{2.2}
\]
R48 proves for every slab witness with `rho>=rho_0` the dichotomy
\[
|\det\Lambda|<6144e^2\rho^{-4}
\tag{2.3}
\]
or there are two ORIGINAL coordinates `k,j` for which the physical principal pair
\[
B=A[\{k,j\},\{k,j\}]
\tag{2.4}
\]
is indefinite and satisfies
\[
|\det B|\ge D_0:=\frac{1001}{12544},
\qquad
\sigma_{\min}(B)\ge\kappa_0:=\frac{13}{112}.
\tag{2.5}
\]

The owner-pinned source was reread at exactly

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`.

Its completed `RESULTS.md` physical-block conclusion states that an invertible indefinite ORIGINAL-coordinate pair with quantitative determinant and least singular value gives an arbitrary-rank density bound once `s_3(A)>=1`; the supporting theorem is source-pinned at

`yspennstate/math-open-problems@742ac943440e41925fe09db9a8c02a96cbd83dbc`

`proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/FULL_MATRIX_PAIR_EXTENSION.md`.

Precisely, if `s_3(A)>=s>0`, `D=|det B|`, `kappa=sigma_min(B)`, then for arbitrary affine terms and arbitrary remaining spectrum,
\[
\boxed{
\|p_Q\|_\infty
\le 3\,400^{1/3}(D^2\kappa s)^{-1/6}.
}
\tag{2.6}
\]
The proof retains all couplings and uses the arbitrary-rank remainder small-ball estimate
\[
\sup_w\Pr\{|Z^TSZ+b^TZ+d-w|<r\}
\le \min\{1,5(r/\|S\|)^{1/4}\}.
\tag{2.7}
\]
Thus it is not the false mechanism “pair plus one innovation absorbs an arbitrary remainder”; it is a separate proved full-matrix pair theorem.

The pinned counterexample search still reports no valid counterexample. Its numerical observations are not used below.

## 3. Main theorem: r48's physical-pair branch is impossible

### Theorem 3.1 — `QFORM-R48-INDEFINITE-BRANCH-ELIMINATED-v1`

Under (2.1), every slab witness with `rho>=rho_0` must satisfy the ultra-collapse alternative (2.3).

#### Proof

Suppose instead r48's physical-pair branch occurs. Apply (2.6) with
\[
D=D_0=\frac{1001}{12544},\qquad
\kappa=\kappa_0=\frac{13}{112},\qquad s=1.
\]
Then
\[
\|p_Q\|_\infty
\le C_{\rm pair},
\qquad
C_{\rm pair}:=
3\,400^{1/3}
\left[
\left(\frac{1001}{12544}\right)^2
\frac{13}{112}
\right]^{-1/6}.
\tag{3.1}
\]
Direct arithmetic gives
\[
\boxed{C_{\rm pair}=73.51134228393067\ldots .}
\tag{3.2}
\]
For every interval `J`, its slab ratio obeys
\[
\frac{\Pr\{Q\in J\}}{|J|}\le\|p_Q\|_\infty\le C_{\rm pair}.
\tag{3.3}
\]
But
\[
C_{\rm pair}<73.512<82.5724<\rho_0\le\rho,
\tag{3.4}
\]
a contradiction. Therefore the pair branch cannot occur. QED.

This is an equation-level application of a completed result from the required pinned package to the newest designated-partner dichotomy.

## 4. Forced ultracollapse and two literal large diagonals

### Corollary 4.1 — `QFORM-DIFFUSE-R2-FORCED-ULTRACOLLAPSE-v1`

For every diffuse exact-rank-two slab witness with `rho>=rho_0`,
\[
\boxed{
|\det\Lambda|<6144e^2\rho^{-4}.
}
\tag{4.1}
\]
If `|lambda_1|>=|lambda_2|`, then
\[
|\lambda_2|\le\sqrt{|\lambda_1\lambda_2|}
=\sqrt{|\det\Lambda|},
\]
so
\[
\boxed{
|\lambda_2|<32\sqrt6\,e\,\rho^{-2}
=213.06891061773865\ldots\rho^{-2}.
}
\tag{4.2}
\]
At the threshold itself,
\[
\frac{32\sqrt6 e}{\rho_0^2}=\frac1{32},
\tag{4.3}
\]
so `|lambda_2|<1/32` for every `rho>=rho_0`.

R48/r45's rank inequality
\[
s_2(D)\ge1-|\lambda_2|
\tag{4.4}
\]
therefore sharpens to
\[
\boxed{
s_2(D)>1-32\sqrt6\,e\,\rho^{-2}
\ge\frac{31}{32}.
}
\tag{4.5}
\]
Because `D` is diagonal, at least two ORIGINAL physical diagonal coefficients obey
\[
\boxed{
|d_i|,|d_j|>1-32\sqrt6\,e\,\rho^{-2}.
}
\tag{4.6}
\]
No coordinate rotation or support assumption is involved.

Equivalently, if
\[
M_0:=D+\lambda_1vv^T,
\]
then Weyl gives
\[
\boxed{
s_3(M_0)>1-32\sqrt6\,e\,\rho^{-2}\ge31/32.
}
\tag{4.7}
\]
Thus the dominant rank-one-plus-diagonal coefficient core itself carries essentially the full three-large-singular-value requirement.

## 5. Sharpen the partner r45 four-diagonal normal form

R45 plus the designated diagonal-sparsification theorem gives
\[
A=D_C+\lambda_1vv^T+E_{\rm sep}+\lambda_2ww^T,
\qquad |C|\le4,
\tag{5.1}
\]
where
\[
E_{\rm sep}=D_{C^c},
\qquad
\|E_{\rm sep}\|_{op}\le C_D\rho^{-1},
\qquad
C_D:=2\sqrt{30\pi}=19.41625912555699\ldots .
\tag{5.2}
\]
By Corollary 4.1 the same survivor now obeys
\[
\boxed{
\|\lambda_2ww^T\|_{op}=|\lambda_2|
<213.068910617739\,\rho^{-2}.
}
\tag{5.3}
\]
This replaces the preceding `O(rho^-7/6)` secondary-carrier scale by an explicit `O(rho^-2)` scale.

Let
\[
M_C:=D_C+\lambda_1vv^T.
\tag{5.4}
\]
Since `s_3(A)>=1`, Weyl gives
\[
\boxed{
 s_3(M_C)
 \ge
 1-\frac{2\sqrt{30\pi}}{\rho}
   -\frac{32\sqrt6\,e}{\rho^2}.
}
\tag{5.5}
\]
At `rho=rho_0`, the right side is
\[
1-\frac{2\sqrt{30\pi}}{82.572423603571\ldots}-\frac1{32}
=0.7336078268845\ldots .
\tag{5.6}
\]
Hence throughout the r48 high-density chamber,
\[
\boxed{s_3(M_C)>0.7336>1/2.}
\tag{5.7}
\]
So there is no residual `s_3(M_C)<1/2` spectral side branch once r48 and the completed physical-pair theorem are combined.

This is only a coefficient-level spectral statement. Equations (5.3)-(5.7) do **not** permit deleting `E_sep` or `lambda_2ww^T` from the random quadratic form on arbitrary fragmented/unbounded inputs.

## 6. Scope correction to account02/B13 r12

The preceding r12 report stated that the finite-direction grouping theorem supplied a bound for **every affine** `M_C`-form with the same constant used in its affine-defect application. Fresh source comparison shows that the canonical theorem

`QFORM-FINITE-DIRECTION-FINITE-DIAGONAL-GROUPING-v1`

was proved at its stated **homogeneous/no-affine** scope. The proof groups each rank-one physical bank into one scalar variable; a completely arbitrary physical linear term can have components inside the same bank orthogonal to that grouped direction and is not represented by the grouped scalar.

Therefore the following correction wins over r12:

### Correction 6.1 — `QFORM-R12-AFFINE-CORE-SCOPE-CORRECTION-v1`

The abstract slab-mass-trimmed affine-defect theorem in r12 remains valid **conditional on** an affine-uniform core density bound. The claimed application to `M_C=D_C+lambda_1 vv^T` using the previously proved grouping theorem is not yet justified by that theorem alone and is withdrawn pending an affine-uniform extension or a direct rough receiver.

The spectral gate from r12 is not needed anymore anyway: (5.7) supplies a stronger unconditional gate in the r48 chamber. The new unpaid receiver must handle the affine/grouping issue explicitly rather than assuming it away.

## 7. Required pinned D5 obstruction remains simultaneous

The completed unconditional `D_5` theorem in the owner-pinned Fourier report gives, for every disjoint ORIGINAL-coordinate physical cross block `B=A[I,J]`,
\[
\|p_Q\|_\infty
\le5\sqrt{2e}\,e_5(B^TB)^{-1/10}.
\tag{7.1}
\]
Hence every ratio-`rho` slab witness obeys
\[
\boxed{
e_5(B^TB)
\le\left(\frac{5\sqrt{2e}}{\rho}\right)^{10}
}
\tag{7.2}
\]
and therefore
\[
\boxed{
s_5(B)\le\frac{5\sqrt{2e}}{\rho}
=11.6582199079856\ldots\rho^{-1}.
}
\tag{7.3}
\]
This controls every physical cut in the general survivor. In the exact-rank-two endpoint every physical cross block has rank at most two, so `D_5` is structurally blind there; the forced-ultracollapse theorem above is genuinely complementary.

## 8. Extremal product laws: exact scope

Partner r48 proves self-containedly that for every nonnegative slab kernel the supremum over arbitrary cap-one mass-one product densities equals the supremum over arbitrary unit-measure product indicators. By Lebesgue regularity, strict witnesses may be approximated with arbitrarily small loss by bounded finite unions of intervals of total measure one in each coordinate.

No optimizer is asserted to exist. No single interval, centering, bounded diameter, or uniform fragment-count conclusion follows. Thus a counterexample sequence to the remaining rough receiver may still exploit increasingly remote or fragmented supports, and the `O(rho^-1)` coefficient tail cannot be discarded perturbatively.

## 9. Net progress and next target

The newest partner's apparently difficult “ultracollapse OR physical indefinite pair+star” endpoint no longer has two branches: the completed arbitrary-rank physical-pair theorem pays the pair branch below the partner's own high-density threshold. Therefore every high-density diffuse exact-rank-two survivor is forced into
\[
|\det\Lambda|=O(\rho^{-4}),\qquad
|\lambda_2|=O(\rho^{-2}),
\]
with at least two literal physical diagonals `>=31/32` in magnitude and a rank-one-plus-four-diagonal core whose third singular value is already `>0.7336`.

The next mathematical obligation is accordingly narrower: retain the `O(rho^-1)` distributed diagonal tail and `O(rho^-2)` secondary carrier in a product-preserving receiver for this strongly curved rank-one-plus-finite-diagonal core, with arbitrary fragmented/unbounded cap-one inputs and without relying on an unproved affine grouping extension.

Full unrestricted QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains **OPEN**.
