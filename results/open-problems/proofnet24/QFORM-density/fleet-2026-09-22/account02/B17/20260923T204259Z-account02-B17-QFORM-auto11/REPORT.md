SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B17, 2026-09-23T20:42:59Z.
attacking: the first unpaid global implication in the dense Householder fragmentation family — upgrade the partner's countable-fragment cone-tip theorem to an all-output density barrier, preserving cap-one supports and exact spectrum.

# QFORM B17 — global countable-fragment barrier for the dense Householder stress family

Run: `20260923T204259Z-account02-B17-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: sharp constant and witnesses  
Status: **NEW SUPPORTING GLOBAL WITNESS EXCLUSION; FULL QFORM OPEN**  
Continuity: **not claimed for the unrestricted target**.  
Native learned-memory status: **WITHOUT_VERIFIED_BRAIN**.

The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. This report proves a global all-output density bound for a source-valid exact-spectrum six-variable family with arbitrary finite or countable interval fragmentation, provided the nonkernel cell-center gap is positive at the explicit scale below. It removes the two gaps left after the latest partner theorem: fragment count had already been removed at the cone tip, but the bound was stated only at output zero; the present argument shows that the same six-chart mechanism is uniform in the output level, while the kernel aggregate is dominated as a measure by the connected triangular-bank control law.

Fresh initial brain control was resolved at `cfd0d0ef51c48679957bf648422676b15207031c`; a prepublication refresh saw brain main `0082f302e675e9ab32b727c257b59cb67559d105`. OWNER CONTROL revision remains `2026-09-22.15`, QFORM-only. The live correction inbox was reread. No law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint coarea cap, conditional projection-density moment, fixed fragment-count reduction, or generic two-sheet X-ray shortcut is used.

## 1. Exact physical matrix and source-valid fragmented laws

Let

\[
T={1\over\sqrt2}\begin{pmatrix}
1&1&0&0&0&0\\
0&0&1&1&0&0\\
0&0&0&0&1&1
\end{pmatrix},
\qquad
B=I_3-{2\over3}{\bf1}{\bf1}^T,
\]

and

\[
A=T^TBT={1\over6}\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\tag{1.1}
\]

Since `TT^T=I_3` and `B^2=I_3`, `B` has eigenvalues `1,1,-1`, and `T^T` is an isometry from `R^3` into `R^6`. Hence

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}}.
\tag{1.2}
\]

The exact checker also verifies `A^3=A`, `rank(A)=3`, and `tr(A)=1`, which independently forces the same nonzero spectrum for this symmetric matrix.

For each physical coordinate `i=1,...,6`, let

\[
E_i=\bigsqcup_{k\in K_i}
[c_{i,k}-\ell_{i,k}/2,c_{i,k}+\ell_{i,k}/2],
\qquad
\ell_{i,k}>0,
\qquad
\sum_{k\in K_i}\ell_{i,k}=1,
\tag{1.3}
\]

with `K_i` finite or countable and the intervals pairwise disjoint. Take independent `X_i` with density `1_{E_i}`. Thus every physical marginal is a probability density exactly bounded by one. No moment, bounded-diameter, connected-support, identical-law, or log-concavity assumption is imposed on these fragmented marginals.

A product cell has center `c=(c_{1,k_1},...,c_{6,k_6})`. Call it **kernel** if `Tc=0`, and **nonkernel** otherwise. Define

\[
\Delta:=\inf\{|Tc|:Tc\ne0\},
\qquad
M:=\Delta-\frac{\sqrt6}{2}.
\tag{1.4}
\]

The result below assumes only `M>0` inside this explicit witness class.

## 2. Latest partner input and the first unpaid implication

The latest completed designated partner result is `account03/B17`, report

`yspennstate/math-open-problems@e79bba262d16c5f629722431a39f563c0d8c4094:proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260923T200542Z-account03-B17-QFORM-auto11/REPORT.md`

(the mathematical theorem first appeared at `aa3701dba95126ebd65b11e54428db66dfc7f9dc`; later commits record/fix the checker output).

It proves two facts for exactly (1.1)--(1.4):

1. after summing **all** exact-kernel cells, each pair-sum bank subdensity `h_{j,0}` obeys

\[
0\le h_{j,0}(y)\le h_*(y):=\sqrt2(1-\sqrt2|y|)_+;
\tag{2.1}
\]

2. on the union of nonkernel cells, `|Ax|>=M`, and six derivative charts give the cone-tip error `6sqrt(6)/M`, with no factor depending on the number of cells.

The partner states the resulting theorem at output zero. The first unpaid implication is therefore: **does the same fragment-count-free control hold for the true global density norm, including off-tip positive and negative levels?** The answer is yes.

## 3. Main theorem: all-output countable-fragment aggregation

### Theorem `QFORM-DENSE-FRAGMENT-GLOBAL-AGGREGATE-v1`

For (1.1)--(1.4), if `M>0`, the law of `Q=X^TAX` has an essentially bounded density and

\[
\boxed{
\|p_Q\|_\infty
\le
\|p_*\|_\infty+{6\sqrt6\over M},
}
\tag{3.1}
\]

where `p_*` is the output density for six independent centered unit intervals under the same matrix. The connected control is known exactly and globally:

\[
\boxed{
\|p_*\|_\infty=p_*(0)
=4.0630706168060372601\ldots<3\sqrt2.
}
\tag{3.2}
\]

Consequently

\[
\boxed{
\limsup_{\Delta\to\infty}\|p_Q\|_\infty\le p_*(0)<3\sqrt2,
}
\tag{3.3}
\]

uniformly over finite or countable fragment counts and arbitrarily many exact pairwise remote cancellations. In particular, the exact rational certificate

\[
\boxed{
\Delta\ge84
\quad\Longrightarrow\quad
\|p_Q\|_\infty<{140\over33}<3\sqrt2
}
\tag{3.4}
\]

holds for every fragmented law in this theorem.

The proof is short once the partner's aggregation is used at the correct level.

## 4. Kernel sector: measure domination is automatically global

The kernel condition `Tc=0` is equivalent to exact center cancellation in each of the three disjoint physical pairs. Hence the union of all kernel product cells factorizes bank by bank. Let `h_{j,0}` be the resulting (subprobability) density of the `j`th pair sum

\[
Y_j={X_{2j-1}+X_{2j}\over\sqrt2}.
\]

The partner's exact interval-overlap argument gives (2.1). Therefore the three-dimensional kernel subdensity satisfies

\[
0\le \rho_{\rm ker}(y)=\prod_{j=1}^3h_{j,0}(y_j)
\le
\prod_{j=1}^3 h_*(y_j)=:\rho_*(y)
\quad\text{pointwise}.
\tag{4.1}
\]

Now avoid any delicate pointwise delta manipulation. For every Borel set `E` in the output line,

\[
\begin{aligned}
\mu_{\rm ker}(E)
&=\int_{\{y:y^TBy\in E\}}\rho_{\rm ker}(y)\,dy\\
&\le\int_{\{y:y^TBy\in E\}}\rho_*(y)\,dy
=\mu_*(E).
\end{aligned}
\tag{4.2}
\]

Since the connected control law `mu_*` has density `p_*`, (4.2) implies absolute continuity of the kernel submeasure and

\[
\boxed{p_{\rm ker}(s)\le p_*(s)\quad\text{for a.e. }s.}
\tag{4.3}
\]

This is the key global upgrade: the partner's pointwise bank domination already dominates the **entire output measure**, not merely its cone-tip trace.

## 5. Nonkernel sector: the partner's six charts are uniform in the output level

Take `x` in a nonkernel product cell of center `c`, and write `x=c+u`. Every fragment length is at most one, hence

\[
|u|\le{\sqrt6\over2}.
\]

Moreover, because `T^T` is an isometry and `B` is orthogonal,

\[
|Ac|=|T^TBTc|=|Tc|,
\qquad \|A\|_{op}=1.
\]

Thus on the whole nonkernel union

\[
|Ax|\ge |Ac|-|Au|
\ge\Delta-{\sqrt6\over2}=M.
\tag{5.1}
\]

Partition this union measurably into six charts `N_j` according to the first coordinate attaining `max_k |(Ax)_k|`. On `N_j`,

\[
|(Ax)_j|\ge {M\over\sqrt6},
\qquad
|\partial_{x_j}(x^TAx)|=2|(Ax)_j|
\ge {2M\over\sqrt6}.
\tag{5.2}
\]

Fix the other five physical coordinates and now fix an **arbitrary** output level `s`. As a function of `x_j`,

\[
x^TAx-s
\]

is a polynomial of degree at most two. It has at most two roots on `N_j`; an identically constant zero fiber is impossible on `N_j` because (5.2) forces a nonzero derivative. The one-dimensional root/coarea formula and `f_j<=1` therefore give, for a.e. `s`,

\[
\int 1_{N_j}(x)f_j(x_j)\delta(x^TAx-s)\,dx_j
\le
2\,{\sqrt6\over2M}
={\sqrt6\over M}.
\tag{5.3}
\]

Integrating the remaining five independent physical densities costs exactly one. Hence every chart pushforward is absolutely continuous with density bounded by `sqrt(6)/M`, uniformly in `s`, and

\[
\boxed{
\|p_{\rm nonker}\|_\infty\le{6\sqrt6\over M}.
}
\tag{5.4}
\]

The same equation in the partner report was written with `delta(x^TAx)` because that report targeted the cone tip. Nothing in the gradient bound, root count, or Fubini step depends on zero: replacing it by `delta(x^TAx-s)` proves (5.4) for the full output line.

Combining (4.3) and (5.4) proves (3.1).

## 6. Required application of the pinned `e5f71d79...` result

I read the required source at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The completed result used here is **Theorem C** from `COUNTEREXAMPLE_SEARCH.md`. For a rank-three `(+,+,-)` form, on the one-sheet side `s>=0` it gives the exact ruled identity; in the normalized `(1,1,-1)` case,

\[
p_*(s)={\pi\over\sqrt2}\operatorname{avg}_{\theta}
\rho_\theta(\sqrt{s}\,e_\theta).
\tag{6.1}
\]

For the connected triangular-bank control, `rho_*` is centrally symmetric and log-concave. Orthogonal rotation preserves those properties, and Prékopa preserves them in every two-dimensional marginal `rho_theta`. Hence each `rho_theta` is maximized at zero, and the pinned identity pays the real inequality

\[
\boxed{
p_*(s)\le {\pi\over\sqrt2}\operatorname{avg}_{\theta}\rho_\theta(0)
=p_*(0),\qquad s\ge0.
}
\tag{6.2}
\]

This is stronger than merely invoking Theorem C's generic ceiling `pi sqrt(2)`, which is **larger** than `3sqrt(2)` and therefore would not settle the proposed sharp value. The source identity plus the special control law's log-concavity is what pays the positive-output obstruction. Failure of the generic `pi sqrt(2)` constant to prove sharpness is a proof-constant limitation, not a QFORM counterexample.

For the two-sheet side `s<0`, I use the completed account01/B17 proof

`yspennstate/math-open-problems@9cee470f9b774f59ad36ba4bbcdbc6339de4abe6:proofnet24/QFORM-density/fleet-2026-09-22/account01/B17/20260923T195220Z-account01-B17-QFORM-auto11/REPORT.md`.

That argument respects the live `QFORM-TWOSHEET-XRAY-ONLY-FALSE` correction: it derives a special polar coarea formula for the triangular product density, proves strict sub-tip control near zero by a deleted-cone-segment versus inward-shift estimate, and handles the far negative side using its cyclic/log-concave envelope. It concludes exactly (3.2). Thus the present proof does not resurrect the refuted generic two-sheet X-ray shortcut.

## 7. Exact global certificate for arbitrary countable fragmentation

The partner report supplies the certified inequalities

\[
p_*(0)<{508\over125},
\qquad
\sqrt6<{49\over20}.
\tag{7.1}
\]

If `Delta>=84`, then

\[
M=\Delta-{\sqrt6\over2}
>84-{49\over40}={3311\over40},
\]

so

\[
{6\sqrt6\over M}<{588\over3311}.
\]

Therefore (3.1) gives

\[
\|p_Q\|_\infty
<{508\over125}+{588\over3311}.
\]

Exactly,

\[
{140\over33}-\left({508\over125}+{588\over3311}\right)
={148\over177375}>0,
\tag{7.2}
\]

and

\[
140^2=19600<19602=18\cdot33^2,
\]

so `140/33<3sqrt(2)`. This proves (3.4) without floating-point dependence.

## 8. Explicit adversarial stress: the partner's two-fragment law is globally subcritical already at `R>=110`

Set `eta=10^{-3}` and take all six independent physical marginals to have density

\[
f_R(x)=
1_{[-(1-\eta)/2,(1-\eta)/2]}(x)
+1_{[R,R+\eta]}(x).
\tag{8.1}
\]

Each support has total length `(1-eta)+eta=1`, so (8.1) is a genuine cap-one probability density. All remote centers are positive; hence the only exact-kernel product cell is the all-central cell. If `L=1-eta=999/1000`, scaling the six central physical coordinates by `L` scales its probability mass by `L^6` and the quadratic output by `L^2`. Thus its **global** output subdensity is

\[
p_{\rm central}(s)=L^4p_*(s/L^2),
\qquad
\|p_{\rm central}\|_\infty=L^4p_*(0).
\tag{8.2}
\]

Every noncentral cell has at least one pair-sum center of magnitude at least `(R+eta/2)/sqrt(2)`, so

\[
\Delta\ge{R+\eta/2\over\sqrt2}>{R\over\sqrt2}.
\]

Equations (5.4) and (8.2) therefore give the all-output inequality

\[
\boxed{
\|p_{Q_R}\|_\infty
\le
\left({999\over1000}\right)^4p_*(0)
+{6\sqrt6\over R/\sqrt2-\sqrt6/2}.
}
\tag{8.3}
\]

This is a genuine global strengthening of the partner's cone-tip estimate.

For `R>=110`, use additionally `1/sqrt(2)>7/10`. Then

\[
M>{7R\over10}-{49\over40}
\ge {3031\over40},
\qquad
{6\sqrt6\over M}<{588\over3031}.
\tag{8.4}
\]

The central term has the clean exact bound

\[
\left({999\over1000}\right)^4p_*(0)
<\left({999\over1000}\right)^4{508\over125}
<{506\over125},
\tag{8.5}
\]

because

\[
506\cdot1000^4-508\cdot999^4=28,954,031,492>0.
\]

Finally,

\[
{140\over33}-\left({506\over125}+{588\over3031}\right)
={766\over1786125}>0.
\tag{8.6}
\]

Hence the explicit source-valid stress family satisfies

\[
\boxed{
\|p_{Q_R}\|_\infty<{140\over33}<3\sqrt2
\qquad(R\ge110).
}
\tag{8.7}
\]

The partner's preceding exact rational certificate was `R>=120` **at the cone tip**. The present argument is global and improves the displayed finite threshold to `R>=110` by using the exact `L^4` scaling of the only kernel cell.

## 9. Sharp-constant interpretation and remaining witness frontier

This result does **not** prove that `3sqrt(2)` is the unrestricted sharp constant, and it does not prove the full universal QFORM bound. It excludes a substantial adversarial family:

- the exact physical spectrum is always `{1,1,-1,0,0,0}`;
- every physical marginal is an independent cap-one interval-indicator law;
- each marginal may have finitely or countably many disconnected fragments;
- arbitrarily many product cells may cancel **exactly** into the pair-sum kernel;
- fragment count may grow without bound;
- the estimate is for the true global essential density norm, on both output signs.

What remains unpaid in this architecture is **near-kernel resonance**: nonkernel cell centers with `|Tc|=O(1)` even while physical centers become remote, so that `Delta` does not grow. More generally, arbitrary rough cap-one laws not represented by interval-indicator fragments, different shared/intermediate-leverage geometries, and additional active spectrum remain outside this theorem.

The distinction required for witness work is important. If the six-chart estimate degenerates as `Delta` tends to zero, that is only failure of this mechanism. A valid source example with a finite peak above `3sqrt(2)` would refute the **candidate sharp constant** but would still not refute existence of some larger universal constant. A genuine counterexample to QFORM would require failure of every finite universal bound (for example, an unbounded output density or a family with peaks tending to infinity) under the original independent cap-one hypotheses.

## 10. Verification and source status

`CHECK.py` and `CHECK_OUTPUT.txt` in this run directory verify exactly:

- `A^3=A`, `rank(A)=3`, `tr(A)=1`, hence nonzero spectrum `{1,1,-1}`;
- the certified connected value `p_*(0)<508/125<3sqrt(2)` numerically against its exact closed form;
- the `Delta>=84` rational global certificate;
- the `R>=110` exact two-fragment certificate, including the integer inequality behind (8.5) and rational margin (8.6).

Checker status: `PASS QFORM-DENSE-FRAGMENT-GLOBAL-AGGREGATE-v1`.

The theorem is deliberately scoped as `SUPPORTING_GLOBAL_WITNESS_EXCLUSION`. Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`, and unrestricted continuity remains separate.
