SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T21:00:09Z.
attacking: overlapping-source localization — keep the whole original-coordinate receiver projection aggregated while allowing its driver coordinates to parameterize the L^p core, and make arbitrary positive driver localization zero-tax when one score anchor stays whole.

# fleet02/B14 — overlapping-driver mixed-norm localization

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T210009Z-fleet02-B14-QFORM-auto11`  
Status: `SUPPORTING_THEOREM_PROVED / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

The first unpaid implication is now

`QFORM-STOCHASTIC-OVERLAP-LP-BUDGET-OR-WHOLE-ACTIVE-EXIT-v1`:

> In every surviving no-pivot / N3 state, before active-fragment normalization, either expose a whole-law D'/D5/projected-crossing/ridge/hub/pair certificate, or choose one original-coordinate receiver row so that after fixing the row's driver coordinates the remaining core has a finite probability-weighted conditional `L^p` density budget. The genuinely unresolved overlap is where those same driver coordinates are themselves essential to create the core smoothing, so even the mixed conditional `L^p` budget is not yet controlled.

This sharpens the newest fleet03/B14 gap: **source-disjointness is stronger than necessary**. Parametric reuse of the receiver drivers by the core is harmless; only failure of the conditional mixed `L^p` budget remains.

## 2. Inputs: product projection and a layer-cake Riesz bound

For independent cap-one original coordinates `W=(W_1,...,W_m)` and `a!=0`, the source-pinned product-projection bound used by fleet03/B14 gives

\[
\|p_{a^TW}\|_\infty\le
\mathcal C(a):=
\min\left\{\|a\|_\infty^{-1},\sqrt2\,\|a\|_2^{-1}\right\}.
\tag{2.1}
\]

I use the following version of the negative-moment estimate by layer cake, so no unattained infinite-line bathtub optimizer is assumed. If a positive measure `mu` on `R` has total mass `m` and density cap `L`, then for `0<alpha<1`,

\[
\boxed{
\sup_s\int |y-s|^{-\alpha}\,d\mu(y)
\le {2^\alpha\over1-\alpha}L^\alpha m^{1-\alpha}.
}
\tag{2.2}
\]

Indeed

\[
\mu\{|y-s|<t^{-1/\alpha}\}
\le \min\{m,2Lt^{-1/\alpha}\},
\]

and integration in `t` gives (2.2) at the crossover `t=(2L/m)^alpha`. For a probability density with cap `C`, this becomes

\[
\mathbb E|Y-s|^{-\alpha}
\le {2^\alpha C^\alpha\over1-\alpha}.
\tag{2.3}
\]

No support, moment, connectedness, fragment-count or translation parameter occurs.

## 3. Main theorem — overlapping driver, mixed conditional core

### Theorem 3.1 — `QFORM-OVERLAPPING-DRIVER-LP-RECEIVER-LOCALIZATION-v1`

Let `1<q<2`, `p=q/(q-1)`, and `alpha=q-1`. Let

\[
(U,V_1,\ldots,V_m)
\]

be independent original-coordinate cap-one variables, and let `Xi` be an auxiliary product block independent of `(U,V)`. For almost every driver value `v`, let `T_v=T(Xi;v)` have density and define

\[
K(v):=\|p_{T_v}\|_p,
\qquad
\mathcal K_p:=\bigl(\mathbb E K(V)^p\bigr)^{1/p}<\infty.
\tag{3.1}
\]

The dependence of `T_v` on the **same** `v` used below is arbitrary; in the quadratic application it may contain all conditioning-generated affine leakage into the core. Let `d in R`, `c in R^m`, `(d,c)!=0`, let `e in R`, and let `R(v)` be arbitrary measurable. Put

\[
Q=T_V+dU^2+2(c^TV+e)U+R(V).
\tag{3.2}
\]

Then `Q` has an essentially bounded density and, with `a=(d,c)`,

\[
\boxed{
\|p_Q\|_\infty
\le
\mathcal K_p
\left({2^{q-1}\over2-q}\right)^{1/q}
\mathcal C(a)^{(q-1)/q}.
}
\tag{3.3}
\]

At `p=3`, `q=3/2`,

\[
\boxed{
\|p_Q\|_\infty
\le 2\mathcal K_3\,\mathcal C(a)^{1/3}
\le 2^{7/6}\mathcal K_3\,\|a\|_2^{-1/3}.
}
\tag{3.4}
\]

The same estimate holds uniformly after conditioning on arbitrary outside original coordinates, provided their effect is only to change `e`, `R`, and the family `T_v` while preserving the same mixed core budget.

### Proof

Fix `v`. Write

\[
q_v(u)=du^2+2(c^Tv+e)u.
\]

Let `h_v` be the pushforward density of `U` by `q_v`. If `d!=0`, each regular output has at most two preimages and their derivative magnitudes coincide. Since `f_U<=1`,

\[
h_v(q_v(U))
\le |dU+c^Tv+e|^{-1}.
\tag{3.5}
\]

If `d=0`, then `c!=0`; outside the null hyperplane `c^Tv+e=0`, the map is affine and the same weaker bound (3.5) holds. Therefore

\[
\|h_v\|_q^q
=\mathbb E\,h_v(q_v(U))^{q-1}
\le
\mathbb E_U|dU+c^Tv+e|^{-\alpha}.
\tag{3.6}
\]

This identity also shows explicitly why there is no hidden two-preimage tax: the quadratic multiplicity and derivative factor cancel at the required power.

Conditional on `V=v`, `T_v` is independent of `U`. Translation by `R(v)` costs nothing, so Young-Hoelder gives

\[
\|p_{Q\mid V=v}\|_\infty
\le
K(v)
\left(\mathbb E_U|dU+c^Tv+e|^{-\alpha}\right)^{1/q}.
\tag{3.7}
\]

Average in `v`, then apply Holder with exponents `p,q` **before** any fragment normalization:

\[
\begin{aligned}
\|p_Q\|_\infty
&\le
\mathbb E_V K(V)G(V)^{1/q}\\
&\le
\bigl(\mathbb E K(V)^p\bigr)^{1/p}
\bigl(\mathbb E G(V)\bigr)^{1/q},
\end{aligned}
\tag{3.8}
\]

where `G(v)=E_U|dU+c^Tv+e|^{-alpha}`. The final expectation in (3.8) is exactly

\[
\mathbb E|a^T(U,V)+e|^{-\alpha}.
\]

By (2.1) the whole original-coordinate projection has cap at most `C(a)`, and (2.3) gives

\[
\mathbb EG(V)
\le {2^\alpha\over1-\alpha}\mathcal C(a)^\alpha.
\tag{3.9}
\]

Since `alpha=q-1` and `1-alpha=2-q`, (3.3) follows. No rotated variable is declared independent. QED.

### What changed relative to fleet03/B14

The newest partner theorem assumes the complete receiver bank is source-disjoint from the `L^p` core. The proof above shows that this is unnecessary. The driver coordinates `V` may parameterize the core arbitrarily, and even a uniform core bound is unnecessary: the exact quantity is the mixed norm

\[
\boxed{\mathcal K_p=(E\|p_{T_V}\|_p^p)^{1/p}.}
\tag{3.10}
\]

Only the selected receiver coordinate `U` must remain independent of the conditional core after fixing `V`.

## 4. Zero-tax positive localization when one score anchor remains whole

The mixed-norm form has a useful mass-homogeneous consequence. Assume `d!=0` and decompose the complete driver law of `V` into arbitrary positive submeasures `nu_j` of masses `m_j`, with no restriction on count, locations, diameters, gaps or tails. Keep the receiver coordinate `U` whole.

For a piece `nu_j`, the unnormalized score measure of

\[
dU+c^TV+e
\]

has mass `m_j` and density cap at most `m_j/|d|`, simply by conditioning on `V` and using the cap-one law of the whole `U`. By (2.2),

\[
\int G(v)d\nu_j(v)
\le
{2^\alpha\over1-\alpha}\,m_j|d|^{-\alpha}.
\tag{4.1}
\]

Holder on that unnormalized piece gives

\[
\|p_Q^{(j)}\|_\infty
\le
A_q |d|^{-\alpha/q}
\left(\int K(v)^p d\nu_j(v)\right)^{1/p}m_j^{1/q},
\tag{4.2}
\]

where `A_q=[2^alpha/(1-alpha)]^(1/q)`. Summing (4.2) and applying Holder across the pieces yields exactly

\[
\boxed{
\sum_j\|p_Q^{(j)}\|_\infty
\le
A_q |d|^{-\alpha/q}
\left(\mathbb E K(V)^p\right)^{1/p}.
}
\tag{4.3}
\]

Thus **arbitrary positive localization of every driver coordinate is zero-tax** once a nonzero quadratic receiver coefficient `d` keeps one whole score anchor. At `p=3,q=3/2`, the factor is `2 K_3 |d|^{-1/3}`. If `d=0` but one coordinate with `c_k!=0` is kept whole while only the other driver coordinates are fragmented, the identical argument uses `|c_k|` instead.

This is the localization/mixture rule relevant to the full target: aggregate the whole anchor before reciprocal payment; fragments may then be arbitrarily translated, remote and unbounded.

## 5. Exact-target overlapping family

Let `m>=2`. Take mutually independent arbitrary cap-one variables

\[
X_0,X_1,X_2,X_3,X_4,U,W_1,\ldots,W_m
\]

and set

\[
L={X_1+X_2+X_3+X_4\over2},\qquad
V={X_1+X_2-X_3-X_4\over2},\qquad
S_m={1\over\sqrt m}\sum_{j=1}^mW_j.
\]

Define

\[
\boxed{
Q_m^{\rm ov}
=4X_0L+4X_0S_m+{1\over2}V^2+4US_m.
}
\tag{5.1}
\]

The same diffuse bank `S_m` appears both inside the core as an affine hub leakage and in the receiver row. Conditional on the `W`-bank, with `S_m=s`, define

\[
T_s=4X_0L+4sX_0+{1\over2}V^2.
\tag{5.2}
\]

The newest fleet03/B14 report derives from the valid fleet04/B14 slice-Fresnel equation the affine-uniform rough-hub estimate

\[
\|p_T\|_3
\le
3^{4/3}2^{8/9}|h|^{-4/9}|\gamma|^{-2/9}.
\tag{5.3}
\]

For its stress core `2X_0L+(1/2)V^2`, that report identifies `|h|=2^{-1/2}`, `|gamma|=1`. Doubling the hub slope to (5.2) doubles `h`, while `4sX_0` is exactly the arbitrary affine hub leakage already allowed. Hence uniformly in `s`,

\[
\boxed{
\|p_{T_s}\|_3
\le K_*:=3^{4/3}2^{2/3}.
}
\tag{5.4}
\]

For the receiver `4US_m`, Theorem 3.1 has `d=0` and

\[
c_j={2\over\sqrt m},\qquad
\|c\|_2=2,\qquad
\|c\|_\infty={2\over\sqrt m}.
\]

Thus for every `m>=2`,

\[
\mathcal C(c)=\min\{\sqrt m/2,1/\sqrt2\}=1/\sqrt2.
\tag{5.5}
\]

Using (3.4) and (5.4),

\[
\boxed{
\|p_{Q_m^{\rm ov}}\|_\infty
\le
3^{4/3}2^{3/2}
=12.2378934159\ldots
}
\tag{5.6}
\]

uniformly in `m`, every admissible product law, arbitrary translations, distant fragments and unbounded supports.

This family is genuinely inside the owner target. In the deterministic orthonormal basis `(X_0,U,L,S_m,V)`, the four-dimensional cross block has bipartite matrix

\[
M=\begin{pmatrix}2&2\\0&2\end{pmatrix},
\]

whose singular values are `sqrt(5)+1` and `sqrt(5)-1`. Therefore the nonzero spectrum of the quadratic matrix is

\[
\boxed{
\{\,\sqrt5+1,-(\sqrt5+1),\sqrt5-1,-(\sqrt5-1),1/2\,\},
}
\tag{5.7}
\]

so four eigenvalues have modulus strictly greater than one. The deterministic basis is used only to calculate the spectrum; no independence after rotation is invoked.

### Why the overlap is real for the partner compiler

The natural rough-hub core in (5.2) is not source-disjoint from the receiver bank. One can algebraically move `4X_0S_m` into a receiver affine coefficient only by conditioning on `X_0`; but that destroys the available uniform `L^3` core certificate.

For example, take `X_1,...,X_4` uniform on `[-1/2,1/2]`. Conditional on `X_0=x`, the candidate core is

\[
4xL+{1\over2}V^2.
\tag{5.8}
\]

As `x->0` these laws converge weakly to `(1/2)V^2`. The density of `V` is continuous and positive at zero, so the density of `(1/2)V^2` behaves like `c y^{-1/2}` at the origin and is not in `L^3`. If the `L^3` norms in (5.8) were uniformly bounded along `x->0`, reflexive weak compactness in `L^3`, tested against compactly supported bounded functions, would force the weak limit to have an `L^3` density, a contradiction. Thus the source-disjoint recoding has no uniform `L^3` budget. Theorem 3.1 instead conditions the diffuse driver bank and keeps the hub `X_0` unconditioned, which is exactly the safe direction.

## 6. Required Claude result applied to the same family

I freshly read the fixed source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem B gives, with `P` the orthogonal projection onto the range of the quadratic matrix,

\[
\boxed{
\|p_Q\|_\infty
\le2\sqrt{2\pi}\sum_i|Pe_i|.
}
\tag{6.1}
\]

For (5.1), the range is exactly

\[
\operatorname{span}\{X_0,U,L,S_m,V\}.
\]

Hence the two physical coordinates `X_0,U` contribute `2`; each of `X_1,...,X_4` has projection norm `1/sqrt(2)`, contributing `2sqrt(2)`; and each `W_j` has projection norm `1/sqrt(m)`, contributing `sqrt(m)`. Therefore Claude's theorem gives the real inequality

\[
\boxed{
\|p_{Q_m^{\rm ov}}\|_\infty
\le
2\sqrt{2\pi}\bigl(2+2\sqrt2+\sqrt m\bigr).
}
\tag{6.2}
\]

This is valid but grows like `sqrt(m)`. The new overlapping-driver compiler gives the dimension-free bound (5.6) on the very same target-valid family. Thus (6.2) is also a concrete obstruction to closing the full theorem by paying the projection-coordinate sum before diffuse receiver aggregation: the physical leverage sum can diverge even when one aggregate receiver row plus the conditional rough-hub core stay uniformly controlled.

The fixed Claude counterexample search still reports no valid counterexample to full QFORM; this run does not produce one.

## 7. Scope and remaining gap

What is now paid:

- receiver-driver coordinates may also parameterize the core;
- the conditional core need not have a uniform `L^p` norm, only the exact mixed budget `(E||p_{T_V}||_p^p)^(1/p)`;
- arbitrary shifts and same-driver remainder terms are free;
- a whole nonzero score anchor makes arbitrary positive driver fragmentation zero-tax;
- diffuse receiver rows are aggregated in `l2` before any reciprocal coefficient is paid.

What is not paid:

- the case where fixing the driver destroys the core smoothing so severely that the mixed conditional `L^p` budget diverges;
- a structural theorem forcing one of the existing whole-law volume/ridge/hub/pair exits or the new mixed-budget receiver branch from the bare hypothesis `s_3(A)>=1`.

That is the next B14 target. Continuity of the unrestricted target remains separate.

## 8. Integrity

No moment, support, log-concavity, connected-support, bounded-diameter, fixed-fragment, Gaussian or post-rotation-independence assumption is used. The cap-only negative-moment estimate is proved by layer cake rather than an unattained infinite-line optimizer. The newest fleet03/B14 result is used at its actual `L^p` receiver equation and extended only in the source-overlap direction proved above. The latest fleet03/B15 correction on translated nonzero quadratic folds is respected; no large affine slope is treated as a gain when scalar curvature remains. Full QFORM is not claimed solved.
