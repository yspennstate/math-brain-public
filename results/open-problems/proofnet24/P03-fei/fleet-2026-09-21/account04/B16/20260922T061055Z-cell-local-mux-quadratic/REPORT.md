# account04/B16 — cell-local quadratic control for the balanced unequal-MUX gate

**Classification:** `ESSENTIAL_STEP_APPLIED / ALL_GATE_MUX_REDUCTION / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Publication priority:** unverified; no novelty claim is made.

## 0. Live direction and exact scope

The live OWNER CONTROL is revision `2026-09-22.2`. Its later natural-language OWNER MESSAGE supersedes the older interface-C-only phase-switch assignment where the two conflict: every FEI worker is to converge on the all-gate reformulation and either prove the gate extremality mechanism or falsify it. This run therefore attacks the current all-gate candidate rather than reopening a retired positive-current route.

The source-exact gate equivalence is

`proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`

(report blob observed earlier as `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`). The current Campaign-A candidate used by the completed MUX line is

\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
where on the small side
\[
\Gamma_0(z)=zG(\log_2(1/z))
\]
and the committed h96 source has piecewise-affine `G` with `|G'|<31`.

This report proves a new exact reduction on the balanced-address, same-side unequal-MUX sector. It does **not** prove all MUX biases, all prime gates, or FEI.

## 1. Exact completed inputs consumed

The principal live input is the balanced-address unequal-MUX identity from

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`

and its sharpened collar continuation at scientific commit

`ad0f62b702b9301e401ac9102e8b85b140e26caf`.

For selector bias `t=1/2`, define
\[
u=1-q_0-q_1,\qquad v=q_1-q_0,
\qquad |u|+|v|\le1,
\]
\[
J_\Gamma(u,v)=
\Gamma\!\left(\frac{1-u}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u-v}{2}\right)
-\frac12\Gamma\!\left(\frac{1-u+v}{2}\right).
\]
The exact signed-posterior calculation gives
\[
D_\Gamma(M;1/2,q_0,q_1)=R_C(u,v)-J_\Gamma(u,v),
\tag{1.1}
\]
with the source-independent reserve
\[
R_C(u,v)\ge(C-6)\delta,
\qquad
\delta=\frac{1-u^2+v^2}{2}.
\tag{1.2}
\]
The negative Shannon/posterior credit is already retained in (1.1)-(1.2); it is not discarded or spent again below.

The previous completed same-side theorem used only the global slope bound and proved positivity for relative separation `|v|/(1-|u|)<=1/86`. The present result uses the **actual piecewise-affine source geometry** and is therefore substantially stronger away from source knots.

For continuity with the inherited signed mechanism, I also re-read the exact sources requested by the standing B16 prompt:

* account02/B16, `proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260921T184541Z-actual-current-parent-mask-incidence/REPORT.md`, theorem creation revision `7f9fdcbbba89432301a5e32985ae2bd3e7b1ac5e`; its authentic central parent weights satisfy `sum_j mu_j=E_cen<=11W/192` only **after** signed syndrome aggregation;
* account03/B18, `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260921T185340Z-signed-flag-curvature/REPORT.md`, theorem creation revision `4843e50690013fd18b85dd8763b53bdc75da79e8`; its physical sink is `kappa=p+4o`, with ordered-flag payments `sum E kappa<=2J`, `sum E kappa^2<=4J`, and `sum E o<=J/2` in the minimizing-character gauge.

Those older interface-C ledgers are **not** re-spent in the MUX calculation. Their orientation, opposite-sign overlap, dual-code multiplicity, negative credits and terminal/remainder terms remain at their proved scopes.

## 2. Same-side MUX coordinates

By the usual data-exchange/output-complement symmetries it suffices to take
\[
u\ge0,\qquad 0\le v\le u.
\]
Put
\[
p=\frac{1-u}{2},\qquad
\rho=\frac{v}{1-u}.
\tag{2.1}
\]
Then `0<p<=1/2`, `0<=rho<1`, and the three potential arguments are
\[
p,\qquad p(1-\rho),\qquad p(1+\rho).
\tag{2.2}
\]
Moreover
\[
\delta=\frac{1-u^2+v^2}{2}\ge p.
\tag{2.3}
\]
Hence (1.1)-(1.2) reduce the problem to a sharp upper bound on the midpoint gap `J_{Gamma^dagger}`.

## 3. New exact theorem: within one source cell the loss is quadratic

Let
\[
x=\log_2(1/p),\qquad
\alpha=-\log_2(1-\rho),\qquad
\beta=\log_2(1+\rho).
\]
Thus the three arguments of `G` are
\[
x+\alpha,\qquad x,\qquad x-\beta.
\]
Assume these three points lie in **one affine source segment** of the committed h96 potential, so
\[
G(y)=A+\sigma y
\]
throughout that interval.

### Theorem 3.1 — exact cell-local midpoint formula
Under that one-cell hypothesis,
\[
\boxed{
J_{\Gamma_0}(u,v)
=\frac{p\sigma}{2\ln2}
K(\rho),
}
\tag{3.1}
\]
where
\[
K(\rho)=(1-\rho)\ln(1-\rho)+(1+\rho)\ln(1+\rho).
\tag{3.2}
\]
The quadratic lift contributes exactly
\[
\boxed{
J_{a^\dagger z(1-z)}(u,v)=a^\dagger p^2\rho^2.
}
\tag{3.3}
\]
Therefore
\[
\boxed{
J_{\Gamma^\dagger}(u,v)
=\frac{p\sigma}{2\ln2}K(\rho)
+a^\dagger p^2\rho^2.
}
\tag{3.4}
\]

### Proof
Substitute
\[
\Gamma_0(p(1\pm\rho))
=p(1\pm\rho)
G\!\left(x-\log_2(1\pm\rho)\right)
\]
into the midpoint gap. The common affine intercept and common `sigma*x` terms cancel exactly. What remains is
\[
-\frac{p\sigma}{2}
\left[(1-\rho)\log_2\frac1{1-\rho}
-(1+\rho)\log_2(1+\rho)\right],
\]
which is (3.1). Equation (3.3) is the direct midpoint identity for `z(1-z)`. \(\square\)

This is the key change from the previous global-Lipschitz collar: **inside a source cell the adverse source term is second-order in the data separation, not first-order.**

## 4. Analytic certified collar `rho <= 3/20`

For `0<=rho<1`,
\[
K'(\rho)=\ln\frac{1+\rho}{1-\rho}=2\operatorname{atanh}(\rho).
\]
Since
\[
\operatorname{atanh}(s)\le\frac{s}{1-s^2},
\]
integration gives the convenient elementary bound
\[
\boxed{
K(\rho)\le\frac{\rho^2}{1-\rho^2}.
}
\tag{4.1}
\]
The source slope satisfies `sigma<=31`; also `p<=1/2`. Combining (1.1), (2.3), (3.4) and (4.1),
\[
D_{\Gamma^\dagger}(M)
\ge p\left[
(C^\dagger-6)
-\frac{31}{2\ln2}\frac{\rho^2}{1-\rho^2}
-\frac{a^\dagger}{2}\rho^2
\right].
\tag{4.2}
\]
The bracket is decreasing in `rho`. Using the exact rational logarithm bound already proved in the MUX collar line,
\[
\frac1{\ln2}<\frac{10^7}{6931471},
\tag{4.3}
\]
at `rho=3/20` the right-hand bracket is exactly bounded below by
\[
\boxed{
\frac{1114633887638025857}
{271020516100000000000}
=0.004112728820967757\ldots>0.
}
\tag{4.4}
\]
Hence:

### Theorem 4.1 — cell-local same-side MUX exclusion
If the balanced-address same-side MUX satisfies
\[
\rho=\frac{|q_1-q_0|}{1-|1-q_0-q_1|}\le\frac3{20}
\tag{4.5}
\]
and the three small-side logarithmic arguments in (2.2) lie in a single affine h96 source segment, then
\[
\boxed{
D_{\Gamma^\dagger}(M)
>0.0041127288\,p>0.
}
\tag{4.6}
\]
Thus no such gate/bias point can falsify the live all-gate candidate.

The new relative radius `3/20=0.15` is nearly thirteen times the unconditional earlier radius `1/86` on the same-side sector. The price is explicit: source-knot crossing strips are excluded from Theorem 4.1 and remain to be certified separately.

## 5. Stronger slope-sensitive exclusion

Equation (3.4) gives more than a fixed collar.

If the containing source segment has `sigma<=0`, then the entire `Gamma_0` midpoint term is favorable. Consequently, for every `0<=rho<1`,
\[
D_{\Gamma^\dagger}(M)
\ge p\left[(C^\dagger-6)-\frac{a^\dagger}{2}\rho^2\right]
>p\left[(C^\dagger-6)-\frac{a^\dagger}{2}\right].
\]
The last reserve is exactly
\[
\boxed{
\frac{193874393}{500000000}=0.387748786>0.
}
\tag{5.1}
\]
So **every same-cell MUX point in a nonpositive-slope source cell is safe for arbitrary relative data separation**.

More generally, because `K(rho)<2 ln 2` for `rho<1`, every same-cell point is safe for all `rho` whenever
\[
\sigma\le(C^\dagger-6)-\frac{a^\dagger}{2}=0.387748786.
\tag{5.2}
\]
Thus a same-cell counterexample, if one exists at all, must lie in a genuinely positive and sufficiently steep source segment.

## 6. What is now left for this MUX family

For the balanced same-side MUX, the continuous two-dimensional obstruction has been reduced to two sharply specified sets:

1. **source-knot crossing strips**, where `x-beta`, `x`, and `x+alpha` do not lie in one affine h96 segment; and
2. **positive-slope same-cell regions beyond the certified radius**, with slope above the threshold in (5.2).

The source has only finitely many h96 affine segments. The next decisive step is therefore finite and source-exact: enumerate those knot-crossing strips and prove the exact two-segment analogue of (3.4), using the actual adjacent slopes rather than reverting to the global `31*rho` Lipschitz loss. That is the natural route to close the balanced same-side MUX plane or exhibit a genuine violation.

This is directly on the live all-gate target. It does not claim that MUX closure alone proves FEI.

## 7. Verification

`check_cell_local_mux.py` performs two independent sanity checks in addition to the analytic proof above:

* exact rational evaluation of the `rho=3/20` reserve and the all-rho nonpositive-slope reserve;
* 20,000 random affine-cell parameter trials comparing the closed formula (3.1) with direct evaluation of `z G(log2(1/z))`;
* 19,999 mesh points checking the elementary `K(rho)` envelope.

The observed maximum affine-formula discrepancy was `1.4330550635044403e-14`; the largest sampled ratio of `K(rho)` to the right side of (4.1) was `0.9999999979174824`. These finite tests are sanity checks only; Theorems 3.1, 4.1 and the slope corollary are analytic.

## 8. Status

**ESSENTIAL STEP APPLIED on one explicit live obstruction family.** The exact MUX midpoint loss is now quadratic on every individual h96 source cell, giving a `rho<=3/20` certified same-cell collar and an all-rho exclusion for nonpositive/low-slope cells. Source-knot crossings remain open. Full FEI remains OPEN / NOT PROVED.
