# B01 / A004 — complete signed fair-activation correction

**Run:** `20261014T101433Z-fleet01-B01-complete-activation-correction-a004`  
**Primary packet:** A004, constant and unit ledger  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B01-A004-COMPLETE-ACTIVATION-CORRECTION-v1`  
**Status:** **AUTHOR-PROVED PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Frozen candidate and implication

The previous three A004 attempts lower-bounded the sufficient signed-mismatch
constant and proved that tensor-suspension amplification has a finite ceiling.
This run changed mechanism as required and froze the full one-step correction
for a fresh fair activation `A(f)`.

For `0<eta<=1`, define

\[
 L_{c,\eta}(f)=M(f)+(1+\eta)U(f)-cI(f),
 \qquad M=G-B.
\]

The signed-mismatch reduction proves that universal `L_{c,eta}<=0` implies
GU with `(a,b)=(c+2,1-eta)`, hence

\[
 H\le\left(2+\frac{2(c+2)}\eta\right)I.
\]

## Result

For every genuine Boolean core `f`, every dimension, every bias
`m=E f`, and every `0<eta<=1`,

\[
\boxed{
 L_{c,\eta}(Af)
 \le\frac12L_{c,\eta}(f)+\Phi(f)
 +\left(\frac{21}{2}-c\right)\frac{1-m}{2},}
\]

where

\[
 \Phi(f)=\sum_i q(\widehat f(\{i\})^2),\qquad
 q(t)=t\log_2(1/t)+2t/\ln2.
\]

The proof uses the exact activation recurrence.  If `a_i=fhat({i})`, its
complete signed coordinate correction is

\[
 P(m,a_i)=R(m)-\frac{R(m-a_i)+R(m+a_i)}2-C(m,a_i^2).
\]

The new analytic inequality is

\[
\boxed{P(m,a)\le q(a^2)}.
\]

It holds throughout the Boolean feasibility triangle
`|a|<=1-|m|`.  The midpoint curvature consumes at most `q/2`; the signed
entropy correction consumes at most the other `q/2`.  The root/selector
term is at most `(21/2)(1-m)/2`.  Thus every normalization, sign, and
selector reserve is retained.

## Before / after

| Quantity | Previous state | New state |
|---|---|---|
| Complete activation correction | no universal upper bound recorded | bounded by one `Phi(core)` packet plus `21/2` times selector influence |
| Dimension/bias dependence | open | none in the one-step theorem |
| Positive/negative pieces | risk of separate overcharge | combined before payment |
| Repeated activations | same packet could be reused | still open, now isolated as packet ownership only |

For `c>=21/2`, the selector term is nonpositive.  Hence the only unpaid
object in a fair activation is `Phi(core)`.  The accepted B05 signed-orbit
theorem telescopes such a packet on one changing-block physical restriction
tree.  The precise remaining assembly lemma is to embed all core packets of
a complete activation hierarchy into one such signed ledger without
duplicating a packet at different activation ancestors.  This is named
`ACTIVATION-PACKET-OWNERSHIP`.

This is strictly smaller than the original aggregate mismatch, but it is
not yet a universal GU pair: simply replacing every `Phi` by
`2I/ln2` at every ancestor would double-spend descendant influence.

## Verification

`CHECK.py` checks the two scalar half-payments, their sum, the root bound,
the exact activation recurrence, and the displayed theorem.  It covers
249,500 points on a uniform two-dimensional scalar grid and 374 genuine
Boolean cores: exhaustive through three variables plus seeded cores through
seven variables.  The
proof is analytic; the floating checks are regression evidence only.

## Next action

Use the independently reviewed signed-orbit telescope to prove or falsify
`ACTIVATION-PACKET-OWNERSHIP` first on a two-level hierarchy with one reused
physical coordinate.  Preserve signed opening refunds and terminal
`Theta`; do not replace `Phi` by an all-node positive influence charge.

Route to A086/A090 for independent reconstruction and to B20 for assembly.
Model: Codex. Reasoning-effort metadata: UNKNOWN.

