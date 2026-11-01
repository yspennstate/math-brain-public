# B12 FEI sprint: region-2 curvature tightening for the two-block enclosure

Status: **new rigorous curvature identities and a fail-safe v3 enclosure delivered; the pinned M=96, c=0.003 fleet01 x in [1,2] shard is NOT claimed certified in this run. Full FEI remains OPEN.**

## Live assignment and inherited state

The live three-hour sprint assigns fleet01/B12 to the unfinished read-once region-2 certificate, x in [1,2], for the pinned `M=96, K=40, C0=6.4548, c=0.003` candidate. The pinned candidate remains `cert_vi_h96k40.npz`, 70,354 bytes, Git blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.

The preceding B12 run rewrote the normalized region-2 quantity as

\[
\frac{\Phi}{v}
 = \frac{K_0(x)-K_0(x+\lambda)}{v}+J(x,y),
\]

where \(p=2^{-x}\), \(v=2^{-y}\), \(\lambda=-\log_2(1-v)\),
\(K_0(t)=G_{\rm num}(t)+\Psi(2^{-t})\), and

\[
J(x,y)=\frac{G_{\rm num}(y)}{1-v}+\frac{\widetilde\Psi(v)}{v}
+c(1-p)-8[1+p(x-1)]
-\frac{8(1-p)(1-v)\ell(v)}{\ln 2},
\]

with \(\widetilde\Psi(v)=\Psi(1-v)\).  It proved that \(J\) is strictly decreasing in x on \(1\le x\le2\), so a cell is reduced exactly to \(x=x_{\rm hi}\).  The remaining loss in v2 occurs only in the one-dimensional y enclosure when the interval for \(J_y\) crosses zero.

This run attacks that exact remaining mechanism rather than subdividing the old two-dimensional bound.

## 1. Exact second derivative on a y-node segment

Fix \(x_*=x_{\rm hi}\), \(p_*=2^{-x_*}\).  On one candidate y-node segment,
\(G_{\rm num}(y)=G_0+s(y-y_0)\) is affine.  Write \(L=\ln2\).  The first derivative inherited from v2 is

\[
J_y
 = \frac{s}{1-v}-\frac{L\,vG_{\rm num}(y)}{(1-v)^2}
 -L\left(\widetilde\Psi'(v)-\frac{\widetilde\Psi(v)}{v}\right)
 +8(1-p_*)[1-\ell(v)].
\]

Differentiate once more using \(v_y=-Lv\).  The affine-G term gives

\[
\frac{d^2}{dy^2}\frac{G_{\rm num}(y)}{1-v}
 =
-\frac{2Lsv}{(1-v)^2}
+\frac{L^2vG_{\rm num}(y)(1+v)}{(1-v)^3}.
\]

For
\[
C(y)=\frac{\widetilde\Psi(v)}{v}
     =\frac{-2(1-2v)^2\ln(1-2v)}{L\,v(1-v)}
\qquad (0<v<1/2),
\]
direct differentiation gives the cancellation-friendly expression

\[
C_{yy}
=
\frac{2L}{v(1-v)^3}
\left[
  2v^3-2v+(-4v^2+3v-1)\ln(1-2v)
\right].
\]

Finally,
\[
\frac{d^2}{dy^2}
\left[-\frac{8(1-p_*)(1-v)\ell(v)}{L}\right]
=
8L(1-p_*)
\left[\frac1{1-v}-\ell(v)\right].
\]

Hence the exact scalar curvature is

\[
\boxed{
J_{yy}
=
-\frac{2Lsv}{(1-v)^2}
+\frac{L^2vG_{\rm num}(y)(1+v)}{(1-v)^3}
+\frac{2L\{2v^3-2v+(-4v^2+3v-1)\ln(1-2v)\}}{v(1-v)^3}
+8L(1-p_*)\left[\frac1{1-v}-\ell(v)\right].
}
\]

The implementation intervalizes this formula only when a cell has \(y_{\rm lo}>1\), equivalently \(v_{\rm hi}<1/2\), so the logarithm is bounded away from its singular endpoint.  Any cell touching \(y=1\) falls back unchanged to the already-rigorous v2 enclosure.

## 2. Two new cell reductions

The curvature identity yields two safe improvements.

**Concave cell.** If an outward interval evaluation proves \(J_{yy}\le0\) on the full y-cell, then \(J\) is concave there and therefore

\[
\min_{y\in[a,b]}J(y)=\min\{J(a),J(b)\}.
\]

This remains valid even when the v2 interval for \(J_y\) contains zero.

**Strongly convex cell.** If the interval proves \(J_{yy}\ge k>0\), let \(y_c=(a+b)/2\).  Taylor's integral remainder gives, for every \(y\in[a,b]\),

\[
J(y)\ge J(y_c)+J_y(y_c)(y-y_c)+\frac{k}{2}(y-y_c)^2.
\]

If \(D\) is any certified upper bound on \(|J_y(y_c)|\), minimizing the right-hand quadratic over all real \(y-y_c\) gives the simple safe lower bound

\[
\boxed{\min_{[a,b]}J\ge
\operatorname{lower}(J(y_c))-\frac{D^2}{2k}.}
\]

Minimizing over all of R rather than only the cell makes this conservative, so no root-existence assumption is needed.  The v3 driver takes the maximum of this lower bound, the concave-endpoint lower bound, and every v2 lower bound.  Thus v3 cannot weaken a previously valid certificate.

This specifically targets the v2 branch where the first-derivative interval straddles zero; no extra two-dimensional splitting is introduced.

## 3. Independent high-precision sanity check

`selfcheck_twoblock_v3.py` was run at 80 decimal digits on arbitrary affine G segments, not on the pinned certificate.  It is therefore an algebra/calculus implementation check only.

Results:

```
derivative_trials: 3000
max_abs_Jpp_formula_error: 7.08445029457961402e-74
max_rel_Jpp_formula_error: 7.08444085077131091e-74

curvature_cell_trials: 1200
convex_sampled_cells: 657
concave_sampled_cells: 543
curvature_lemma_sampled_violations: 0
largest_sampled_quadratic_vs_center_MVT_gain: 0.00167471754453075298
```

The second block uses dense high-precision sampling only to stress the calculus reductions; it is not promoted to interval-certificate evidence.  The actual production driver uses outward interval curvature bounds.

The v3 source and self-check both syntax-compile.

## 4. What this does and does not establish

This is a new rigorous enclosure mechanism, not a completed read-once certificate and not a proof of full FEI.  The exact M=96 candidate bytes are authenticated in the private repository, but this invocation still lacks an approved connector-to-native binary materialization path.  Therefore the v3 driver was not run on the pinned NPZ and no production shard result is claimed.

The previous v2 route is not repeated.  The new work advances the analytic enclosure precisely where v2 had to use a centered first-derivative mean-value bound.

## 5. Next execution step

Run `r2_two_block_enclosure_v3.py` against the exact pinned NPZ on bounded y-index shards.  Record separately how many cells are discharged by:

1. v2,
2. the new concave-endpoint rule,
3. the new strongly-convex quadratic rule.

If survivors remain, export only those cells.  A survivor with curvature interval containing zero is then a genuinely higher-order transition cell and should be attacked by a third-derivative/interval-Newton refinement; a survivor with fixed curvature sign identifies loss in the K0 divided-difference block rather than J.

No settled FEI certificate was rerun, no FEI audit was performed, and full FEI remains OPEN.
