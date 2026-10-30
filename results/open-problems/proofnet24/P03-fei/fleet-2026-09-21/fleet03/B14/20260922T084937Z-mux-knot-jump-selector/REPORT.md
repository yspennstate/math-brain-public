# fleet03/B14 — exact knot-jump formula for the physical MUX address selector

**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_SELECTOR_POTENTIAL_DECREMENT / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (authenticated repository sources were used; no authenticated installed/native mathematical-brain retrieval or receiver context entered the derivation).  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Live candidate and exact scope

The live scalar candidate is
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
where on the small side
\[
\Gamma_0(z)=zG(\log_2(1/z))
\]
and the committed h96 source is continuous piecewise affine in the logarithmic variable.

This run stays on the current one-address-bit MUX hard family.  The newest lead boundary theorem available at the start of this run is fleet01/B18 `20260922T080302Z-mux-newborn-cancellation-121`, further sharpened by fleet04/B14 `20260922T083023Z-mux-boundary-20`.  Those reports use a data-coordinate split near deterministic data faces.  Here I use the **physical address bit** as a distinct realizable restriction, so both children are literals and the restriction is terminal.  No affine coordinate change is made; the affine-change charge is therefore exactly zero.

The completed peer theorem consumed and extended is fleet04/B16

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260922T061055Z-cell-local-mux-quadratic/REPORT.md`

(report blob `b78f51929cc557cd48a8003c0d3d3cd674728066`).  It proves a quadratic midpoint formula when the three logarithmic potential arguments remain in one h96 affine cell, and identifies **source-knot crossing strips** as the next exact obligation.  The theorem below removes the one-cell hypothesis and gives the exact correction for arbitrarily many crossed source knots.

## 1. Balanced same-side MUX coordinates and physical selector

By data exchange and output complement, use the peer coordinates
\[
u\ge0,\qquad 0\le v\le u,
\qquad p={1-u\over2},\qquad \rho={v\over1-u}\in[0,1).
\]
Put
\[
x=\log_2(1/p),\qquad
\alpha=-\log_2(1-\rho),\qquad
\beta=\log_2(1+\rho).
\]
The three small-side potential arguments are
\[
p(1-\rho),\quad p,\quad p(1+\rho),
\]
corresponding to logarithmic points
\[
x+\alpha,\quad x,\quad x-\beta.
\]
For any symmetric potential define the midpoint loss
\[
J_\Gamma(u,v)=
\Gamma(p)-\frac12\Gamma(p(1-\rho))-\frac12\Gamma(p(1+\rho)).
\]
The exact signed-posterior calculation consumed from fleet04/B16 gives
\[
D_{\Gamma^\dagger}(M)\ge
p(C^\dagger-6)-J_{\Gamma^\dagger}(u,v).
\tag{1.1}
\]
(The peer has the slightly stronger reserve `(C^dagger-6) delta` with `delta>=p`.)

Operationally, (1.1) is the defect of the realizable physical **address split**.  Restricting the address leaves the two literal gates `D_0,D_1`, so there is no child deficit and no recoding cost.

## 2. Exact all-knot formula

Let the logarithmic source `G` be continuous piecewise affine.  Away from a knot at `x`, write `sigma_0` for the slope of the affine cell containing `x`.  For every knot `k`, write
\[
\Delta_k=\sigma(k+)-\sigma(k-)
\]
for the right-minus-left slope jump.  Set
\[
K(\rho)=(1-\rho)\ln(1-\rho)+(1+\rho)\ln(1+\rho).
\]

### Theorem 2.1 — exact knot-jump midpoint identity

For every `0<p<=1/2`, `0<=rho<1`, with `x` not itself a knot,
\[
\boxed{
\begin{aligned}
{J_{\Gamma_0}\over p}
={}&{\sigma_0\over2\ln2}K(\rho)\\
&-\frac{1-\rho}{2}
\sum_{x<k<x+\alpha}
\Delta_k\,(x+\alpha-k)\\
&-\frac{1+\rho}{2}
\sum_{x-\beta<k<x}
\Delta_k\,(k-(x-\beta)).
\end{aligned}}
\tag{2.1}
\]
At a knot `x` the same statement follows by one-sided interpretation and continuity.

### Proof

Let `g=G'` away from knots.  Since
\[
G(x+\alpha)=G(x)+\int_0^\alpha g(x+s)\,ds,
\]
\[
G(x-\beta)=G(x)-\int_0^\beta g(x-s)\,ds,
\]
and the coefficients `1,(1-rho)/2,(1+rho)/2` cancel the common value `G(x)`, one has
\[
{J_{\Gamma_0}\over p}
=-{1-\rho\over2}\int_0^\alpha g(x+s)\,ds
+{1+\rho\over2}\int_0^\beta g(x-s)\,ds.
\tag{2.2}
\]
For the right integral,
\[
\int_0^\alpha g(x+s)\,ds
=\sigma_0\alpha+
\sum_{x<k<x+\alpha}\Delta_k(x+\alpha-k).
\tag{2.3}
\]
For the left integral, moving left across a knot subtracts its right-minus-left jump, so
\[
\int_0^\beta g(x-s)\,ds
=\sigma_0\beta-
\sum_{x-\beta<k<x}\Delta_k(k-(x-\beta)).
\tag{2.4}
\]
Substitute (2.3)-(2.4) into (2.2), and use
\[
(1+\rho)\beta-(1-\rho)\alpha={K(\rho)\over\ln2}.
\]
This proves (2.1).  QED.

For the quadratic lift, exactly as in the peer report,
\[
J_{a^\dagger z(1-z)}=a^\dagger p^2\rho^2.
\tag{2.5}
\]
Thus (2.1) is the complete source-knot correction for the live candidate.

## 3. Consequences: only downward slope jumps are adverse

Every coefficient multiplying `Delta_k` in (2.1) is nonnegative.  Therefore:

### Corollary 3.1 — upward-knot crossings are free

If every source knot crossed by `[x-beta,x+alpha]` has
\[
\Delta_k\ge0,
\]
then
\[
\boxed{
J_{\Gamma_0}
\le {p\sigma_0\over2\ln2}K(\rho).
}
\tag{3.1}
\]
Hence every safe same-cell estimate from fleet04/B16 remains valid **without the same-cell assumption** across any number of upward slope jumps.

In particular, its proved collar
\[
\rho\le {3\over20}
\]
with margin
\[
m_*=\frac{1114633887638025857}{271020516100000000000}
=0.004112728820967757\ldots
\tag{3.2}
\]
extends across every knot-crossing interval containing no downward slope jump.  Likewise its all-rho exclusion for a central source slope `sigma_0<=0.387748786` remains valid whenever all crossed jumps are upward.

This is a genuine strict extension of the peer theorem: source-knot crossing by itself is **not** an obstruction.  The only adverse crossings are downward slope jumps.

## 4. Exact remaining downward-jump budget

Define the nonnegative adverse budget
\[
\boxed{
\begin{aligned}
B_-(x,\rho)={}&{1-\rho\over2}
\sum_{x<k<x+\alpha}(-\Delta_k)_+\,(x+\alpha-k)\\
&+{1+\rho\over2}
\sum_{x-\beta<k<x}(-\Delta_k)_+\,(k-(x-\beta)).
\end{aligned}}
\tag{4.1}
\]
Dropping the favorable upward jumps from (2.1) and using (1.1),(2.5) gives the exact source-valid sufficient condition
\[
\boxed{
D_{\Gamma^\dagger}(M)\ge
p\left[(C^\dagger-6)
-{\sigma_0\over2\ln2}K(\rho)
-a^\dagger p\rho^2
-B_-(x,\rho)
\right].
}
\tag{4.2}
\]
Thus the old qualitative obligation “certify the source-knot strips” is replaced by one explicit finite quantity `B_-`: only downward slope-jump overshoot can consume the same-cell margin.

As a source-independent local corollary, the h96 slope bound `|sigma|<31` implies a single downward jump has magnitude below `62`.  Throughout `rho<=3/20`, the worst one-knot coefficient is
\[
{1+3/20\over2}\,62={713\over20}.
\]
Therefore even an adversarial single downward h96 jump cannot destroy the peer margin while its logarithmic overshoot is at most
\[
\boxed{
\varepsilon_*=
{m_*\over713/20}
=\frac{1114633887638025857}{9661881398965000000000}
=1.153640622992358\times10^{-4}.
}
\tag{4.3}
\]
The exact multi-knot criterion is still (4.1)-(4.2); (4.3) is only the worst-case one-jump corollary.

## 5. Exact old/new obligation and status

**Exact candidate version:** `Gamma^dagger=Gamma_0+0.268204856 z(1-z)`, `C^dagger=6.521851214`.

**Prior missing implication:** fleet04/B16 reduced balanced same-side MUX to same-cell regions plus source-knot crossing strips, but had no exact formula for a crossing strip.

**New proved inference:** equation (2.1) gives the exact midpoint decrement through arbitrarily many source knots.  Every upward slope jump is favorable; the entire adverse part is exactly the weighted downward-jump budget (4.1).  The already-proved `rho<=3/20` same-cell collar therefore automatically extends through all crossing intervals containing only upward jumps, and by at least the explicit one-jump overshoot (4.3) even across a worst-magnitude downward jump.

**Replacement obligation:** read the actual h96 slope sequence once and certify
\[
B_-(x,\rho)
\le (C^\dagger-6)
-{\sigma_0\over2\ln2}K(\rho)
-a^\dagger p\rho^2
\tag{5.1}
\]
on the remaining balanced same-side MUX cells, or return an actual product-bias point violating (5.1) and then evaluate the full gate margin there.  The exact formula eliminates the need to derive separate one-knot/two-knot analogues.

**Named peer artifact consumed:** fleet04/B16 `20260922T061055Z-cell-local-mux-quadratic/REPORT.md`, blob `b78f51929cc557cd48a8003c0d3d3cd674728066`.

**Next recipient:** `fleet04/B16`, because its next stated task was exact source-knot certification and (2.1) directly replaces that subproblem by a finite downward-jump scan.

**Implication to full FEI:** positive but partial.  Closing balanced same-side MUX is not full MUX, and full MUX is not the universal composition-prime gate theorem.  Full FEI remains **OPEN / NOT PROVED**.

## 6. Counterexample attempt and verification

I tried to refute the stronger claim “every piecewise-affine knot crossing is favorable.”  It is false in general: a downward slope jump has `Delta_k<0` and contributes positively in (2.1).  This is an abstract potential-level refutation, **not** a Boolean obstruction to FEI and not a claim that the committed h96 source fails (5.1).

`CHECK_KNOT_JUMPS.py` independently compares (2.1) against direct evaluation on 50,000 deterministic random continuous piecewise-affine potentials with up to eight knots and slopes in `[-31,31]`, checks the upward-jump sign on 10,000 additional convex-slope trials, and reproduces (3.2)-(4.3) by exact rational arithmetic.  It prints `PASS exact PWL knot-jump identity`; the numerical trials are regression evidence only, while Theorem 2.1 is the algebraic proof.

No scheduler change, cross-account mutation, email/Drive action, public posting, paid model/API/Codex call, remote workflow, credential access, or unrelated private data was used.
