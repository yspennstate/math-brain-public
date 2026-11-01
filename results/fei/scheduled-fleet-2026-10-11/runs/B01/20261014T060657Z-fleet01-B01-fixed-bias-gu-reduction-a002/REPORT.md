# B01 / A002 — fixed-bias hardness reduction for GU

**Run:** `20261014T060657Z-fleet01-B01-fixed-bias-gu-reduction-a002`  
**Primary packet:** A002, hardness-preserving transformations  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim version:** `B01-A002-FIXED-BIAS-GU-REDUCTION-v1`  
**Status:** **PROVED reduction pending independent review; universal GU OPEN**  
**Full FEI:** **OPEN**

## Exact candidate, prior bound, and implication

The previous B01 reduction proved that it suffices to bound the signed
residual \(M+(1+\eta)U-cI\) on balanced functions, allowing an
\(o(N)\) terminal.  It did not reduce GU itself to one fixed nonzero
output bias.

This run freezes the smaller unpaid inequality:

\[
\boxed{
G(F)\le aI(F)+bU(F)+e_N
\quad\text{for every Boolean }F\text{ with }\mathbb EF=\frac12,
} \tag{FB-GU}
\]

where \(a<\infty\), \(0\le b<1\), and
\(|e_N|/N\to0\), uniformly over the fixed-bias slice on every
\(N\)-cube.

`PROOF.md` proves that (FB-GU) implies the exact universal inequality

\[
G(f)\le aI(f)+bU(f)
\]

with the **same pair** \((a,b)\).  Hence the reviewed induction would
give

\[
H(f)\le\left(2+\frac{2a}{1-b}\right)I(f).
\]

No admissible pair is proved here; this is a hardness-preserving reduction,
not a solution of GU.

## Exact embedding

For fresh uniform signs \(y,z\), define

\[
\mathcal T(q)(z,y,x)=1\quad(z=+1),\qquad
\mathcal T(q)(z,y,x)=yq(x)\quad(z=-1).
\]

Every image has \(\mathbb E\mathcal T(q)=1/2\), and direct spectral and
restriction calculations give

\[
U(\mathcal T(q))=1+\frac12U(q),\qquad
I(\mathcal T(q))=1+\frac12I(q),
\]

\[
G(\mathcal T(q))=\frac12G(q)+\kappa(\mathbb Eq),
\qquad
\frac14\le\kappa\le\frac52.
\]

For an arbitrary seed \(q\), apply (FB-GU) to
\(\mathcal T(q^{\otimes t})\).  Tensor additivity turns the slice
inequality into

\[
G(q)\le aI(q)+bU(q)
+\frac{2(a+b-\kappa((\mathbb Eq)^t))}{t}
+\frac{2e_{tn+2}}t.
\]

Both errors vanish as \(t\to\infty\).  Constants are handled
separately.  Conversely, universal GU trivially implies (FB-GU) with
\(e_N=0\), so the two statements are equivalent at each fixed pair.

## Why this matters and what it does not prove

The output bias and empty Fourier mass are now frozen:

\[
\mathbb EF=\frac12,qquad p_F(\varnothing)=\frac14.
\]

Therefore rare or near-constant output bias cannot by itself explain the
universal GU gap.  Any hard seed can be embedded into this single slice
with only bounded overhead, erased by tensor powers.

This also sharpens the scope of B05's balanced-preconditioned activation:
its transfer is effective when the child residual is already paid.
Extending a GU estimate uniformly to all images \(\mathcal T(q)\), with
arbitrary children, is already equivalent to universal GU.

The fixed-bias slice is not restriction-closed; revealing \(y\) exposes
the unbalanced activations \(A(q)\) and \(A(-q)\).  No overlap,
reused-variable, or biased-selector payment is established.

## Verification

`CHECK_FIXED_BIAS.py` independently reconstructs Walsh masses from
character sums, rather than importing the producer checker.  It verifies
the three exact embedding identities, tensor transfer, fixed output bias,
and a compactness bound for \(\kappa\).

Command:

```text
python3 CHECK_FIXED_BIAS.py
```

Output:

```text
status=PASS
boolean_cores_checked=1302
fixed_bias_checks=1302
embedding_formula_checks=3906
tensor_transfer_checks=66
scalar_bound_checks=500001
max_U_error=2.220e-16
max_I_error=0.000e+00
max_G_error=1.332e-15
max_transfer_error=0.000e+00
observed_kappa_range=[1.000000000000000,2.000000000000000]
seed=202610140606
```

The finite checker is corroborative; the theorem is the analytic argument.

## Exact next action

The named unpaid inequality is now `FB-GU-o(N)`: prove one pair
\((a,b)\), \(b<1\), on the fixed slice \(\mathbb EF=1/2\), with a
uniform sublinear terminal.  The next mechanism is to use the fixed
\(p_{\varnothing}=1/4\) packet to bound the aggregate mismatch
\(\sum_i(K_i-\Gamma_i)\), while testing embedded tensors of the
five-bit activation witness and the accepted shared-coordinate
counterfamily.

A005 or A094 should reconstruct equations (1)--(9).  No independent
review or native ingestion is claimed.
