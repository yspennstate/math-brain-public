# B19 / A094 — adversarial review of the width-two point-defect SOLD tree

**Reviewed claim:** `B05-A023-WIDTH-TWO-POINT-DEFECT-SOLD-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED POINT-DEFECT SCOPE; NO REPAIR**  
**Universal GU / full FEI:** **OPEN**

## Audited statement

For

\[
c_0=14+\frac4{\ln2},
\]

every finite-rank Boolean one-point defect has a complete adapted signed-orbit
restriction tree of physical history width at most two.  Consequently

\[
G\le\left(16+\frac4{\ln2}\right)I,
\qquad
H\le\left(34+\frac8{\ln2}\right)I
\]

on this family.

## Independent reconstruction

I reconstructed the Walsh spectrum and did not use the producer's truth-table
code.  With `t=2^{1-r}`, the point defect has constant coefficient `1-t` and
every nonempty Walsh coefficient of magnitude `t`.  This gives independently
the producer's formulas for `U_r`, `B_r`, `D_r`, `M_r`, and

\[
\Theta_{r,k}=kq(t)+(r-k)q(2^kt^2).
\]

For the transition `{x,y}->{y,z}`, the exact coefficient threshold is

\[
c_{r,2}=\frac{M_r-\frac12M_{r-1}+2D_r
+2\Theta_{r,2}-\Theta_{r-1,2}}t.
\]

The all-rank proof checks out:

- `D_r<=3t` follows from the exact positive-coefficient expansion of
  `-(1-s)^2 ln(1-s)`.
- The asserted fourth-derivative bound in the producer proof reduces, after
  `u=1-2s`, `v=u^2`, to
  \[
  P^{(4)}(s)=\frac{32(1+6v-3v^2)}{v(1+v)^3}.
  \]
  It lies in `[0,48]` for `v in [225/256,1]`; the upper sign reduces to the
  increasing polynomial
  `3v^4+9v^3+15v^2-9v-2`, whose lower-end value is
  `41135274883/4294967296>0`.
- Hence `M_r-M_{r-1}/2<=0` for `r>=7`; the dyadic remainder is strictly
  positive with an explicit margin.
- The orbit identity
  \[
  \frac{2\Theta_{r,2}-\Theta_{r-1,2}}t
  =4-\frac{2(r-4)q(4t^2)}t+32(r-3)t
  \]
  is exact and is at most `6` for `r>=7`.
- Therefore `c_{r,2}<=12<c0` for `r>=7`.

`REVIEW_CHECK.py` independently uses the closed formulas and exact rational
linear combinations of logarithms.  It certifies negative node charge at
`c0` for ranks 1–6, including the two terminal transitions, and positive
rank-five full-block charge at the larger reviewed `c*`.

The tree assembly is also valid: the empty-history root is dominated by any
two-coordinate comparison block, every nonconstant child is the next
point defect, and the other child is constant.  No terminal `U` or `Theta`
reserve is omitted.

## Scope objections resolved

- **Reused inputs:** only a two-coordinate physical block is reused; signed
  openings and refunds telescope, so no positive credit is double-spent.
- **Rare limit:** constants are uniform as `t->0`; the proof is analytic for
  every rank, not inferred from the rank-40 diagnostic.
- **Leaf circularity:** rank two and rank one are separately certified; no
  unproved leaf inequality is assumed.
- **Fixed-sign projection:** not used.
- **Universal overreach:** the proof covers point defects only.  It does not
  prove the arbitrary-core width-two Bellman sign or universal GU.

The companion full-block no-go is also correct: its threshold is
`4r-3+4/ln(2)+o(1)`.  This refutes that policy, not GU or FEI.

## Remaining obstacle

The next universal object is the branch-adapted width-two Bellman residual
for arbitrary Boolean cores.  Its nonpositivity remains unproved.  The
point-defect theorem is now accepted evidence that the mandatory rare family
does not obstruct that mechanism.

Model: Codex. Reasoning-effort metadata: UNKNOWN.
