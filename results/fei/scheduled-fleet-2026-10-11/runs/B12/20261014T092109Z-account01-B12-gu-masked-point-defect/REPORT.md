# B12 / A058 — GU for same-variable parity-masked point defects

**Run:** `20261014T092109Z-account01-B12-gu-masked-point-defect`  
**Stable gap:** `B12-A058-SHARED-COORDINATE-OVERLAP`  
**Attempt:** `A058-GU-MASKED-POINT-DEFECT-13`  
**Status:** new overlap class PROVED pending independent review; universal GU OPEN.

## Frozen candidate and implication

For every `n`, point `z`, sign `sigma`, and parity mask `A subseteq [n]`,
set

\[
 f_{n,A,z,\sigma}(x)=\sigma\chi_A(x)(1-2\mathbf1_{x=z}).
\]

The parity mask and rare defect use the **same** physical variables.  The
candidate was the fixed pair

\[
\boxed{G(f)\le16I(f)}\tag{1}
\]

for every such factor and every disjoint product of such factors and pure
characters.  This fixes `(a,b)=(16,0)` before testing.

The previously proved character-core theorem required the character core to
be physically disjoint from each residual factor.  The sharp point-defect
theorem covered only the unmasked case.  Equation (1) removes that
disjoint-core hypothesis for this all-parameter family.

The generated class is restriction closed.  Hence the reviewed GU reduction
gives, on this class,

\[
U(f)\le16I(f),\qquad H(f)\le34I(f).
\]

If (1) were proved for every Boolean function, the same displayed conclusion
would be universal and would settle FEI with constant 34.  This run proves
it only for the stated proper class.

## Exact signed restriction law

Put `r=|A|`, `N=2^n`, `tau=2/N`,
`p=(1-tau)^2`, and `q=tau^2`.  Multiplication by `chi_A` translates the
point-defect spectrum, so

\[
p_f(A)=p,\qquad p_f(S)=q\quad(S\ne A),
\]

but the upper-set order is not translation invariant.  Direct summation
gives the exact coherent upper mass

\[
\pi_f(S)=q2^{n-|S|}+(p-q)\mathbf1_{S\subseteq A}.\tag{2}
\]

This yields an explicit scalar formula `U_{n,r}` recorded in `PROOF.md`.
If a physical coordinate lies outside `A`, the active child is
`f_{n-1,r}` and the other child is a pure character.  If it lies inside
`A`, the active child is `f_{n-1,r-1}` and the other is again a pure
character.  Therefore the complete changing-activation remainder is

\[
\boxed{G_{n,r}=nU_{n,r}
-\frac{n-r}{2}U_{n-1,r}
-\frac r2U_{n-1,r-1}.}\tag{3}
\]

Terms with zero coefficient are omitted.  The influence is exactly

\[
\boxed{I_{n,r}=rp+q(n2^{n-1}-r).}\tag{4}
\]

Equations (2)--(4) retain the realized mask, the physical active branch, the
one-half posterior weight, and the terminal pure-character child.  There is
no favorable-sign projection and no unsigned coefficient-four shortcut.

## Dimension-free payment

For `r>=1`, nonnegativity of child `U` gives `G_{n,r}<=nU_{n,r}`.  Also
`U<=H(p_f)`, because every upper mass is at most one, and (4) gives
`I_{n,r}>=p`.  The common spectral entropy satisfies

\[
nH(p_f)\le16p.
\]

For `n=2` this is equality; for `n=3` it follows from
`H(p_f)<=log_2(8)=3` and `p=9/16`.  For `n>=4`,
`tau<=1/8`, `1/ln 2<3/2`, and

\[
H(p_f)\le \tau(4(n-1)+3).
\]

The sequence `n(4n-1)/2^(n-1)` decreases from `15/2` at `n=4`, whereas
`16p>=49/4`.  Thus (1) follows for every nonempty mask.  The empty-mask case
uses the already proved sharper point-defect bound
`G<=kappa_pd I`, where

\[
\kappa_{pd}=\frac14+\frac94\log_2\frac{16}{9}
=2.1176687467547968\ldots<16.
\]

Exact `U/G/I` additivity on disjoint products then proves (1) for an
arbitrary number of factors, with no dimension, factor-count, mask-weight,
or depth loss.

## Controls and scope

The checker reconstructs 160 masked factors directly, all masks through
dimension six and all mask sizes through dimension eight, plus three
multi-factor tensors.  It checks the scalar formulas through dimension 100.
The designated positive non-affine three-bit collision has
`G/I=1.3933893155687962<16`, but this is only a finite control and is not
covered by the masked-defect theorem.

The class now allows arbitrary same-variable character/defect overlap and
arbitrary mask weight.  It does **not** cover a general non-character source
or a hierarchy in which both children remain coherently nontrivial.  The
unpaid universal step is a source-influence bound for the oriented kernel
when neither child is a terminal character.

Independent review and native Brain ingestion are not observed.  Universal
GU and full FEI remain **OPEN**.

