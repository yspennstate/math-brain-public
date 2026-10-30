# B12 / A058 — exact two-sign posterior center and fixed-sign gap

**Run:** `20261014T071851Z-fleet01-B12-gu-two-sign-posterior`  
**Stable gap:** `B12-A058-SHARED-COORDINATE-OVERLAP`  
**Attempt:** `A058-GU-TWO-SIGN-POSTERIOR-11`  
**Status:** ensemble identity PROVED pending independent review; posterior-only
root payment REFUTED; universal GU OPEN; full FEI OPEN.

## Frozen candidate and implication

Candidate: for arbitrary Boolean actual/companion signs `f_+,f_-` on the
same reused physical cube, express their average `U`, average `G`, and average
GU defect exactly as a sign-blind upper-set functional minus one binary
posterior KL reserve.  Then identify the residual fixed-sign projection and
test whether the nonnegative root posterior pays the active companion from
the preceding run.

Prior bound: the active-policy identity paid all-coordinate multiplicity by
`LC=C+P^q-R_qP^q_child`, but the grouped product remainder was

\[
 (1-b)C+2aJ+P^q-R_qP^q_{child},
\]

with no signed payment.  Fixed-sign ensemble projection and the unsigned
coefficient-four shortcut were already refuted.

Implication: if the exact pair center is nonpositive and the actual sign has
no larger GU defect than its companion, then one fixed `a>=0, b<1` gives
universal `G<=aI+bU`; the reviewed reduction gives
`H<=(2+2a/(1-b))I`.  The new identity removes fresh-selector,
Fourier-orthogonality, positive collision-energy and minimum-activation
hypotheses from the **ensemble center**.  It does not assume or prove the
remaining sign projection.

## Mathematical result

For `p_epsilon=fhat_epsilon^2`, let

\[
q=(p_++p_-)/2,\qquad m=(\pi_++\pi_-)/2=q^\uparrow.
\]

Let `r_epsilon=p_epsilon/(2q)` be the sign posterior at an exact spectral
set and `s_epsilon=pi_epsilon/(2m)` the sign posterior given only its upper
cone.  Define

\[
 M=\sum_Sq(S)\log_2(m(S)/q(S)),\qquad
 K=\sum_Sq(S)D_2(r(S)\Vert s(S)).
\]

Then, for every Boolean pair on every finite cube,

\[
 \frac{U(f_+)+U(f_-)}2=M-K,
\]

and after applying the same identity to all restrictions,

\[
 \frac{G(f_+)+G(f_-)}2=LM-LK.
\]

Consequently

\[
 \frac{D_{a,b}(f_+)+D_{a,b}(f_-)}2
 =LM-a\overline I-bM+bK-LK.
\]

This is an exact signed center identity; `LK` has no universal sign.

For the product companion `f_+=gh,f_-=g`, the fixed-sign projection is

\[
2Z_{a,b}=D_{a,b}(h)+(1-b)C+2aJ+P^q-R_qP^q_{child}.
\]

Thus the active companion is part of the actual/companion projection and can
only be assessed jointly with the factor defect, posterior drift and child
companion.  This is a sharper statement of the remaining universal gap.

## Certified obstruction to root-posterior payment

For

`g=(-1,-1,-1,-1,-1,-1,-1,1)` and
`h=(-1,1,1,1,1,1,1,-1)`, the pair `gh,g` has identical squared Fourier
laws and identical upper masses.  Hence `K(gh,g)=0` exactly.  But

\[
C=-1/2,\quad LC=3/2,\quad P^q=1,\quad
R_qP^q_{child}=-1,\quad J=3/4.
\]

Therefore `P^q<=lambda K` is false for every finite `lambda`.  In addition
`LK=-0.521384822086...`, so `-LK` is adverse.  Exact cancellation is supplied
by `D(h)`: `gh` and `g` are isometric one-point defects, and their projection
gap is zero.  This is not a GU or FEI counterexample.

The checker exhausts all 65,808 ordered product pairs through dimension
three, tests 180 deterministic random pairs through dimension six, and checks
the positive three-bit collision, negative two-bit collision, a two-fold
tensor, and rare half-activation.  It verifies the ensemble, `G`, center
defect, active-companion and product-projection identities.

## Before/after

Before: the all-coordinate signed remainder was isolated but had no
companion-sign/posterior interpretation.

After: the ensemble center is paid exactly for arbitrary overlap and changing
activation, and the entire old remainder is identified as the fixed-sign
projection after retaining `D(h)`.  Root posterior positivity is eliminated
as a standalone payment mechanism by an exact three-bit witness.  No
dimension, bias, overlap, depth, activation or tensor-count loss enters the
proved identities.

## Remaining obstacle and next action

Universal GU remains open.  The exact unpaid estimate is a **joint signed
projection inequality** for

\[
D(h)+(1-b)C+2aJ+P^q-R_qP^q_{child},
\]

coupled to `bK-LK` in the pair center.  It cannot be split into a positive
root `K` payment plus an independent companion bound.

Next: change mechanism within the same gap.  Construct a branchwise
posterior martingale that carries the companion factor label `h` itself, so
that `D(h)` and `P^q-RP^q_child` are owned by one terminal law; test its exact
drift first on the zero-`K` isometric-defect witness and then on the prior
positive collision tensor.

## Evidence and delivery state

`PROOF.md` contains the full derivation.  `CHECK.py`, `CHECK.out`, and
`COMMANDS.md` preserve the deterministic verification.  Source pins are in
`SOURCES.md`.  Independent review: none observed.  Native Brain ingestion:
not observed.  Saving and mirror readback are recorded separately in
`PROGRESS.json`; they do not constitute mathematical review.
