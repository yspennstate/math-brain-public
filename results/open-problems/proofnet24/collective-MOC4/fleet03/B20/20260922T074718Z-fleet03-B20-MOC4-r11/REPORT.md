# fleet03/B20 MOC4 report — full-Hessian cross-split Lyapunov–Schmidt payment

Run: `20260922T074718Z-fleet03-B20-MOC4-r11`  
Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Outcome: `ESSENTIAL_STEP_APPLIED`; full MOC4 remains **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution: `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 1. Exact target and current state

For every pair of complex normal `4 x 4` matrices `A,B`, with spectra `a_1,...,a_4` and `b_1,...,b_4`, prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\},
\]

including singular and repeated spectra.

The newest complete campaign-lead report consumed is fleet03/B07
`20260922T064004Z-fleet03-B07-MOC4-r12`, report blob
`ec11bc9937109dc0059b8e2ab78a485a9f646e3e`, theorem
`MOC4-KERNEL-QUARTIC-RESERVE-v1`.  It reduces a hypothetical positive-gap global support
maximizer to the mixed-Schur boundary branch `MSQR` or the all-pair negative-definite branch
`NDI`, and on `MSQR` proves the Lyapunov–Schmidt necessity

\[
q+3\langle \ell^\#,(-H_{\rm pair})^+\ell^\#\rangle\le0.
\tag{1}
\]

The assigned OTHER-account partner result consumed and applied is fleet04/B09
`20260922T060924Z-b09-moc4-r12`, report blob
`d61d1dae159fd54105764b822385ba7389f0bddb`, theorem
`MOC4-ROOT-SATURATION-EXCLUSION-v1`.  It proves that at a positive-gap true-unitary maximizer every
left/right scalar pair gate is strict; hence the only surviving singular pair boundary is the
genuinely mixed-Schur one, not scalar Spin(4) saturation.

I also use the compatible fleet04/B07 report
`20260922T071214Z-fleet04-B07-MOC4-r14`, theorem
`MOC4-MIXED-SCHUR-SVD-PAYMENT-v1`, which evaluates the pair-only reserve in exact SVD variables.
For a simple mixed-Schur block it writes

\[
R_{\rm pair}=
A r_1^2+
\frac{AB(A r_2^2+2\sigma_2 r_2s_2+B s_2^2)}{AB-\sigma_2^2}
\tag{2}
\]

and the pair-only lead gate is `R_pair <= AB delta`.

The previous B20 same-pair trust-region route was proved redundant with this pair reserve.  The
first genuinely new obligation is therefore to force payment from directions *outside* that
Spin(4) pair slice.

## 2. New theorem — `MOC4-GLOBAL-LS-CROSS-SPLIT-PAYMENT-v1`

The following is a finite-dimensional local-max theorem, applied below to the actual `SU(4)`
support function.  It does not introduce a stochastic, bistochastic, or independent-minor
surrogate.

Let `F` be `C^4` near a local maximum at `0` in a real inner-product space `V`.  Put

\[
\mathcal A=-D^2F(0)\succeq0.
\]

Let `z in ker(\mathcal A)`, define

\[
\ell(Y)=D^3F(0)[z,z,Y],\qquad q=D^4F(0)[z,z,z,z],
\]

and split the tangent space orthogonally as

\[
V=S\oplus T,\qquad z\in S.
\]

Write

\[
\mathcal A=
\begin{pmatrix}
A_0&C\\ C^T&D
\end{pmatrix},
\qquad
\ell^\#=\binom{u}{v}.
\tag{3}
\]

Then:

1. `u in range(A_0)` and the generalized Schur complement
   \[
   \Sigma=D-C^TA_0^+C
   \tag{4}
   \]
   is positive semidefinite;
2. with
   \[
   x_0=A_0^+u,
   \qquad
   g=v-C^Tx_0,
   \tag{5}
   \]
   one has `g in range(Sigma)`;
3. the **full** Lyapunov–Schmidt reserve decomposes exactly as
   \[
   \boxed{
   \langle\ell^\#,\mathcal A^+\ell^\#\rangle
   =u^TA_0^+u+g^T\Sigma^+g;
   }
   \tag{6}
   \]
4. hence local maximality forces the sharpened cross-split gate
   \[
   \boxed{
   q+3u^TA_0^+u+3g^T\Sigma^+g\le0.
   }
   \tag{7}
   \]

The second term in (6) is nonnegative and vanishes **if and only if**

\[
\boxed{v=C^TA_0^+u.}
\tag{8}
\]

Thus the pair-only reserve is the full reserve only on a specific cubic/Hessian compatibility
locus across the complementary tangent directions.

### Proof

The lead local-max lemma applied in the full space gives

\[
\ell^\#\perp\ker\mathcal A,
\qquad
q+3\langle\ell^\#,\mathcal A^+\ell^\#\rangle\le0.
\tag{9}
\]

Because `mathcal A` is positive semidefinite, if `w in ker A_0` then
`(w,0)^T mathcal A (w,0)=0`, hence `mathcal A(w,0)=0`.  Therefore `C^Tw=0` and, by (9),
`u.w=0`.  So `u in range(A_0)`.  The standard generalized-Schur argument then gives
`Sigma >= 0`.

Use the variational identity, valid because `ell# in range(mathcal A)`,

\[
\langle\ell^\#,\mathcal A^+\ell^\#\rangle
=
\sup_{x\in S,\,y\in T}
\left(2u^Tx+2v^Ty-x^TA_0x-2x^TCy-y^TDy\right).
\tag{10}
\]

For fixed `y`, `u-Cy` lies in `range(A_0)` because `C^T ker(A_0)=0`.  Maximizing (10) over
`x` gives

\[
u^TA_0^+u+2g^Ty-y^T\Sigma y.
\tag{11}
\]

If `y in ker Sigma`, the generalized-Schur kernel vector
`(-A_0^+Cy,y)` lies in `ker mathcal A`.  Orthogonality in (9) therefore gives `g.y=0`, so
`g in range(Sigma)`.  Maximizing (11) over `y` now gives exactly

\[
u^TA_0^+u+g^T\Sigma^+g,
\]

proving (6).  Substitute into (9) to get (7).  Since `Sigma^+` is positive definite on
`range(Sigma)`, its quadratic form vanishes exactly when `g=0`, which is (8). `QED`

## 3. Direct MOC4 mixed-Schur consequence

Take `F` to be the genuine MOC4 support functional in an exponential chart on `SU(4)` at a
hypothetical positive-gap global maximizer.  Let `S` be the four-dimensional genuine Spin(4)
pair tangent slice containing one mixed-Schur kernel vector `z`, and let `T=S^perp` inside the
full `15`-dimensional `SU(4)` tangent space.

The pair restriction has `z^T mathcal A z=0`.  Since the **full** Hessian is negative
semidefinite at the global maximizer, `mathcal A>=0`, and therefore zero quadratic form implies
`mathcal A z=0` in the full tangent space.  Thus the theorem applies without assuming that the
pair is dynamically decoupled from the other roots.

In the exact fleet04/B07 SVD notation, the pair-only term in (6) is precisely `R_pair` from
(2), while the lead quartic is

\[
q=-3AB\,\delta.
\]

Consequently every genuine positive-gap mixed-Schur maximizer satisfies the strictly stronger
full-group payment

\[
\boxed{
R_{\rm pair}+R_{\rm cross}\le AB\,\delta,
\qquad
R_{\rm cross}:=g^T\Sigma^+g\ge0.
}
\tag{12}
\]

Equivalently, if

\[
s_{\rm pair}:=AB\delta-R_{\rm pair},
\]

then

\[
\boxed{R_{\rm cross}\le s_{\rm pair}.}
\tag{13}
\]

For every transverse tangent direction `w in T`, Cauchy–Schwarz in the `Sigma` seminorm gives
the scalar family

\[
\boxed{
(g\cdot w)^2\le s_{\rm pair}\,(w^T\Sigma w).
}
\tag{14}
\]

Most importantly, **pair-reserve saturation is no longer merely a same-pair event**:

\[
R_{\rm pair}=AB\delta
\quad\Longrightarrow\quad
\boxed{v=C^TA_0^+u.}
\tag{15}
\]

Thus every cubic coupling into the other eleven tangent directions is then exactly determined by
the cross-Hessian block and the pair cubic covector.  Any one transverse root violating (14), or
violating (15) on pair-reserve saturation, excludes that mixed-Schur candidate.

This is the requested cross-split bridge: the same true unitary supplies `A_0,C,D,u,v`; no
independent pair certificates are glued by hand.

## 4. Why this is a genuine advance over the previous same-pair trust gate

The previous B20 theorem showed that optimizing the complete `S^2 x S^2` orbit of the *same*
Spin(4) pair does not improve the lead Lyapunov–Schmidt reserve.  Equation (12) instead applies
the lead lemma in the full `SU(4)` tangent space and isolates the exact nonnegative payment from
all complementary directions.  Therefore it is not another same-pair reformulation.

The assigned partner fleet04/B09 is used essentially at the proof-tree level: its
`MOC4-ROOT-SATURATION-EXCLUSION-v1` removes scalar saturation, so this cross-split identity is
applied on exactly the surviving genuine mixed-Schur boundary `A,B>0`.  Fleet04/B07 supplies
the source-bound closed form (2), so (12) is immediately evaluable once the full Hessian cross
block and transverse cubic covector are written in the existing Spin(6) coordinates.

## 5. Exact calibration

The adjacent verifier uses exact rational arithmetic on the singular block matrix

\[
A_0=\operatorname{diag}(0,2),\quad
C=\begin{pmatrix}0&0\\1&0\end{pmatrix},\quad
D=\operatorname{diag}(7/2,5),
\]

with `u=(0,4)` and `v=(3,10)`.  It checks

\[
\Sigma=\operatorname{diag}(3,5),\quad
R_{pair}=8,\quad
g=(1,10),\quad
R_{cross}=61/3,
\]

and the full pseudoinverse reserve

\[
R_{full}=85/3=8+61/3.
\]

This finite example is only an exact algebra calibration; the proof is the variational argument
above.

## 6. Updated first unpaid implication

`MOC4-MIXED-SCHUR-CROSS-SPLIT-EVALUATION-v1` remains open:

> Compute `C`, `v` and the generalized Schur complement `Sigma` in the campaign's explicit
> Spin(6)/spectral variables for each of the six left/right pair choices, then combine (12)-(15)
> with the 144 same-unitary cofactor identities from fleet03/B09 and the endpoint roofs.  Prove
> that at least one transverse direction overdraws the available pair slack, or construct a true
> unitary/spectrum witness satisfying all these equations while retaining positive support gap.

This is strictly narrower than the previous instruction to “couple the singular pair to the
other five certificates”: the coupling and its exact payment are now proved; only its structured
MOC4 evaluation remains.

The separate `NDI` branch (all six pair Hessians negative definite) is unaffected and remains
open.

## 7. Verdict

`ESSENTIAL_STEP_APPLIED`.

A mixed-Schur pair boundary at a genuine MOC4 global maximizer must pay not only the known
pair-SVD Lyapunov–Schmidt reserve but an exact nonnegative full-Hessian Schur-complement reserve
from the complementary `SU(4)` tangent directions.  Pair-reserve saturation forces an exact
cross-root cubic/Hessian matching identity.  Full MOC4 remains **OPEN**.
