# B05 / A023 — coefficient-one signed orbit ownership

**Run:** `20261014T093107Z-account01-B05-signed-orbit-ownership-a023`  
**Primary packet:** A023  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B05-A023-SIGNED-ORBIT-OWNERSHIP-v1`  
**Status:** **AUTHOR-PROVED BRIDGE, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Frozen candidate and prior bound

The previous fixed-block account used
`|X| q(E_X(empty))`; its coefficient grew with the number of shared
coordinates. The latest fixed-dimension obstruction then showed that
discarding negative block-change refunds produces unbounded recharge.

The frozen candidate was a coefficient-one potential that (i) pays the
singleton charge of a product with arbitrary shared coordinates, (ii)
contracts when one physical coordinate is first revealed, and (iii)
telescopes with signs when overlap blocks change arbitrarily.

## Result

Define

\[
\Theta_X(f)=\sum_{x\in X}q(Inf_x(f))
+\sum_{i\notin X}q(E_X^f(\{i\})),
\qquad
q(t)=t\log_2(1/t)+2t/\ln2.
\]

Three statements are proved.

1. If `f(X,U)` and `g(X,V)` are Boolean with disjoint private variables,
   then
   \[
   \Phi(fg)\le\Theta_X(f)+\Theta_X(g),
   \quad \Phi(h)=\sum_iq(\widehat h(\{i\})^2).
   \]
   Every shared coordinate has coefficient one; there is no `|X|` loss.

2. For `x in X`,
   \[
   E_\sigma\Theta_{X-\{x\}}(f|x=\sigma)
   \le\Theta_X(f)-q(Inf_x(f)).
   \]
   The whole influence packet is closed once at first physical revelation.

3. On an arbitrary physical restriction tree, permit the active block to
   change at every node. If `O_v` is the signed block-opening cost and `R_v`
   the reveal credit, then
   \[
   \sum_vw_v(R_v-O_v)=
   \Phi(f)-\sum_\ell w_\ell\Theta_{Y_\ell}(f_\ell).
   \]
   This is uniform in dimension, depth, bias, block size, overlap pattern,
   and coordinate re-entry into active blocks. It retains the negative
   refunds that the preceding no-go proves are indispensable.

## Exact implication and remaining inequality

The result isolates the following sufficient local drift statement:

\[
\Delta_{x_v}U(f_v)
\le K Inf_{x_v}(f_v)+\lambda(R_v-O_v) \tag{D}
\]

on one complete adapted physical restriction tree, with absolute
`K,lambda`. If (D) is proved, exact tree telescoping and
`Phi(f)<=2I(f)/ln2` give

\[
U(f)\le(K+2\lambda/\ln2)I(f),
\qquad
H(f)\le(2+2K+4\lambda/\ln2)I(f).
\]

This is an explicitly sufficient U-drift route, not a renamed proof. The
unpaid line is now analytic rather than combinatorial: dominate the actual
signed `B_i-Gamma_i+K_i` node charge by (D). Universal GU and FEI remain
open.

## Before / after

| Feature | Prior state | New state |
|---|---|---|
| Shared empty-orbit coefficient | `|X|` | eliminated |
| Shared-coordinate account | coarse empty orbit | `q(Inf_x)` per coordinate |
| First physical reveal | fixed block only | explicit single-use drop |
| Changing blocks | positive variation refuted | exact signed telescope |
| Terminal reserve | not assembled | retained exactly |
| Link to `Delta U` | open | still open as criterion (D) |

The tradeoff is explicit: `q(Inf_x)` is not pointwise `O(Inf_x)`. It is not
charged directly; it is stored until physical revelation. Treating it as an
ordinary nonnegative local fee would recreate the rare logarithm and is not
claimed.

## Verification

`CHECK.py` passed:

- 3,140 exhaustive reveal-contraction cases through three variables;
- 65,792 exhaustive shared-product pairs (`|X|=1,2` with one private bit
  per factor); and
- 14,400 nodes in seeded branch-dependent changing-block trees through six
  variables.

The maximum telescope error was `2.67e-15`; the proof is analytic and does
not rely on this floating check.

## Next action

Test criterion (D) using the exact `Delta U=B-Gamma+KL` decomposition on the
smallest nontrivial two-level rare activation with overlap
`{x,y}->{y,z}`. Freeze `lambda` and derive the residual as an explicit
function of the four orbit energies and signed correlations; either prove
it or return a genuine Boolean falsifier. Route this bridge to A087/A094 for
independent review and to B20 as a sufficient U-drift interface.

Model: Codex. Reasoning-effort metadata: UNKNOWN.

