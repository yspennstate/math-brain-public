# B05 / A023 — sliding width-two history closes the rare point-defect hierarchy

**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claims:** `B05-A023-FULL-BLOCK-POINT-DEFECT-NOGO-v1`, `B05-A023-WIDTH-TWO-POINT-DEFECT-SOLD-v1`  
**Status:** **ROUTE REFUTED; PARAMETRIC CLASS PROVED PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Frozen candidate and implication

For

\[
q(t)=t\log_2(1/t)+\frac{2t}{\ln2},\qquad
L_c=M+2U-cI,
\]

the reviewed signed-orbit telescope reduces a complete restriction tree to
the local charge

\[
\Delta_xL_c(f)+2\Theta_Y(f)
-\sum_{\sigma=\pm1}\Theta_Z(f_{x=\sigma})\le0. \tag{SOLD}
\]

I tested the first genuinely internal changing-core transition
`{x,y}->{y,z}` on the rank-`r` one-point defect.  A complete SOLD tree at
coefficient `c` implies `G<=(c+2)I` on that class.

## Mathematical delta

The fixed-full-block policy is impossible: on the rank-`r` point defect its
required coefficient is

\[
c_r^{\rm full}=4r-3+\frac4{\ln2}+o(1).
\]

Thus opening every surviving coordinate repeatedly spends the rare logarithm
again.  This is a policy obstruction, not a GU or FEI counterexample.

The width-two sliding policy removes that loss.  Query one member of an
inherited two-coordinate block, retain the other, and insert one new surviving
coordinate.  For every rank `r>=3`, the exact required coefficient obeys

\[
\boxed{c_{r,2}\le c_0:=14+\frac4{\ln2}<
c_*:=\frac{29}{2}+\frac4{\ln2}.}
\]

The constant child terminates and the nonconstant child is the rank-`r-1`
point defect.  The rank-two and rank-one endpoint charges are also below
`c0`.  Consequently every point defect has a complete adapted SOLD tree of
physical-history width at most two, with no rank, depth, or rarity loss.

Hence, pending independent review, the signed-tree mechanism proves on this
whole infinite family

\[
G\le\left(16+\frac4{\ln2}\right)I,
\qquad
H\le\left(34+\frac8{\ln2}\right)I.
\]

This advances the accepted one-node history transfer to a complete changing-
core hierarchy for a mandatory rare-event falsifier.  It does **not** prove a
width-two selection theorem for arbitrary Boolean cores.

## Verification

- `CHECK.py` evaluates the formulas through rank 40, confirms the
  full-block divergence, and exhaustively tests the displayed width-two
  transition for complement-reduced Boolean functions through four inputs.
- `CERTIFY.py` uses exact rational linear combinations of logarithms and
  outward intervals.  It certifies the rank-five full-block failure at `c*`,
  the ranks 1–6 width-two/endpoint charges at `c0`, and the status predicates.
- The infinite-rank step is analytic, not inferred from finite search; it is
  given in `PROOF.md`.

## Exact remaining obstacle

For an arbitrary nonconstant Boolean core carrying an inherited block
`{x,y}`, prove that some physical query and entering coordinate give

\[
\Delta_xL_{c_*,1}(f)+2\Theta_{\{x,y\}}(f)
-\sum_\sigma\Theta_{\{y,z\}}(f_{x=\sigma})\le0,
\]

with correct endpoint conventions, or construct a genuine Boolean
counterfamily.  Finite survival through four inputs is not a universal proof.

Model: Codex. Reasoning-effort metadata: UNKNOWN.
