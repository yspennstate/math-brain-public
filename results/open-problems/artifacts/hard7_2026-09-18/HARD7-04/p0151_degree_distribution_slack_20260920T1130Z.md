Model actually run: **GPT-5.6 Sol. Reasoning level: UNVERIFIED — this is not GPT-6 at maximum, and I do not claim otherwise.**

# P0151 analytic artifact — finite-degree slack in the capped current-birth bridge

This is a self-derived theorem-sized proof artifact for `HARD7-04`, for the exact sequential fixed-outdegree affine preferential-attachment model frozen in `operations/claims/P0151.md`. It strengthens the one-sided exponent bound from the preceding `b12` theorem **without changing the exploration process at all**: the improvement comes from proving that the old convex envelope for the current-birth bridge is not asymptotically sharp on an affine preferential-attachment degree sequence.

It does **not** determine the critical window, prove a matching upper bound, establish `sqrt(n)/log n` scaling, or identify a scaling-limit law. The source problem remains open.

## Proposition

Fix an integer `m>=2` and `delta>0`. Put

`a:=m+delta`, `A:=2m+delta`, `pi:=pi_c`,

where

`pi_c:=delta/[2( m a + sqrt(m(m-1)a(a+1)) )]`.

Let

`gamma_E:=liminf_{n->infinity} log E|C_max(n,pi_c)| / log n`.

Inherit the connected shadow and every symbol/rule from

`artifacts/hard7_2026-09-18/HARD7-04/p0151_low_high_depth_two_bypass_20260920T1030Z.md`,

in particular the proved bound

`gamma_E>=b12`,

its unchanged upper coefficient `U12<1/2`, and `E W_t^2=O(t)`.

The inherited current-birth capped bridge uses

`c(w):=min(w,2A)`

and had only used the pointwise convex envelope

`w c(w)>=2Aw-A^2`.

Define the nonnegative envelope slack

`s(w):=w c(w)-(2Aw-A^2)
     = (w-A)^2, 0<=w<=2A,
       A^2,       w>=2A`.                                        (P.1)

Let

`K0:=ceil(2A-delta)=ceil(4m+delta)`.                              (P.2)

For integer degrees `k=m,...,K0-1`, define the usual affine-PA degree proportions recursively by

`p_m:=A/[A+m(m+delta)]`,                                         (P.3)

`p_k:= m(k-1+delta)p_{k-1}/[A+m(k+delta)]`, `k>m`.               (P.4)

Set

`D_k:=A^2-(k+delta-A)^2>0`,                                      (P.5)

and the exact saturated-slack constant

`S_*:=A^2-sum_{k=m}^{K0-1} D_k p_k`.                             (P.6)

Equivalently, if `p_tail:=1-sum_{k=m}^{K0-1}p_k`,

`S_* = sum_{k=m}^{K0-1} p_k (k+delta-A)^2 + A^2 p_tail`.         (P.7)

The two forms agree because the slack has saturated to `A^2` for every degree `k>=K0`.

Let

`eta_*:=m(m-1)pi_c^2`,                                           (P.8)

and define

`b13:=b12+eta_* S_*/A^2`.                                       (P.9)

Then

`gamma_E>=b13>b12`,                                               (P.10)

and the same exploration still satisfies `b13<U12<1/2`.

Moreover

`S_*>=p_m m^2 = A m^2/[A+ma]`,                                  (P.11)

so the strict gain has the explicit all-parameter lower bound

`b13-b12 >= m^3(m-1)pi_c^2/[A(A+ma)]>0`.                        (P.12)

The point is that this gain consumes **zero new upper-budget margin**: it is hidden slack in a bridge mechanism that was already present before `b12`.

---

## 1. B1 — change category: attack the claim that the old convex envelope is sharp

The previous current-birth bridge proof reduced the outside weighted mass to

`F_t:=sum_{u outside Q_t, u ordinary} w_u(t)c(w_u(t))`

and used only

`w c(w)>=2Aw-A^2`.                                                (1.1)

The negation attack is: suppose (1.1) were asymptotically sharp enough that there were no further first-order drift to harvest. For `w<=2A`, equality in (1.1) requires `w=A`; for `w>=2A`, the gap is the positive constant `A^2`. Thus asymptotic sharpness would require essentially all degree mass to sit at the single degree

`d=A-delta=2m`.

That is incompatible with the affine preferential-attachment degree law: a positive linear fraction of vertices remain at their birth degree `m`. In fact the degree-`m` atom alone contributes slack

`s(a)=(a-A)^2=m^2`.                                               (1.2)

So the old extremal bound was sharp among arbitrary weight configurations with only total mass fixed, but it is **not** sharp on the chronological PA ensemble. The problem changes from an exploration inequality into a finite-degree occupation problem.

**B1 outcome:** successful. It identifies a strictly positive first-order resource already present in the old bridge, so no new capture mechanism or extra variance budget is needed.

---

## 2. B17 — recover the exact finite-degree law needed by the bridge

For fixed integer `k>=m`, let `N_k(t)` be the number of ordinary non-seed vertices of degree `k` at completed time `t`. The two finite seeds change all formulas below only by `O(1)`.

### 2.1 One-birth drift

For every fixed finite cutoff `K`, uniformly for `m<=k<=K`,

`E[N_k(t+1)-N_k(t)|F_t]
 = 1_{k=m}
   + [m/(At)] [(k-1+delta)N_{k-1}(t)-(k+delta)N_k(t)]
   +O(t^-1)`.                                                     (2.1)

For `k=m`, omit the `N_{m-1}` term.

**Justification.** During each of the fixed `m` sequential target choices, a still-degree-`k` vertex has target weight `k+delta`; a degree-`k-1` target enters class `k`. Every denominator is `At+O(1)`. Replacing it by `At` costs `O(N_k/t^2)=O(t^-1)` for fixed `k`. Events in which two labels of the same birth hit the same bounded-degree vertex, or a vertex first enters class `k` and is hit again before the birth ends, have total conditional probability `O(t^-1)`: there are `O(t)` bounded-weight candidates and only `O(1)` label pairs. Those events account for the remaining error. The new vertex contributes `1_{k=m}`.

If `N_k(t)~p_k t`, comparing the constant terms in (2.1) gives

`p_k = 1_{k=m} + [m/A][(k-1+delta)p_{k-1}-(k+delta)p_k]`,         (2.2)

which is exactly (P.3)--(P.4).

This recurrence is classical degree-count machinery, not a novelty claim. A fresh literature check also recovered the standard explicit affine-PA law

`p_k=(2+delta/m) Gamma(k+delta) Gamma(m+2+delta+delta/m)
     /[Gamma(m+delta) Gamma(k+3+delta+delta/m)]`,

which satisfies the same recurrence. The present proof needs only the finite recursion above.

### 2.2 Quantitative concentration for every fixed finite degree window

For each fixed `K`,

`E[(N_k(t)-p_k t)^2]=O_K(t)`, `m<=k<=K`.                         (2.3)

Here is a self-contained induction. Put `X_k(t):=N_k(t)-p_k t`. From (2.1)--(2.2),

`E[X_k(t+1)|F_t]
 = (1-beta_k/t)X_k(t)+(alpha_k/t)X_{k-1}(t)+O(t^-1)`,            (2.4)

where

`beta_k:=m(k+delta)/A>0`,
`alpha_k:=m(k-1+delta)/A`,

and `alpha_m X_{m-1}` is absent. The martingale difference between `X_k(t+1)` and its conditional mean is bounded by a constant depending only on `(m,K)`, since one birth changes each fixed degree count by at most `m+1`.

For `k=m`, squaring (2.4), using the bounded martingale increment and discrete Gronwall gives `E X_m(t)^2=O(t)`. Inductively suppose the assertion holds at `k-1`. In the square of (2.4), use Young's inequality on

`2 alpha_k X_k X_{k-1}/t`

to absorb a fixed fraction of `beta_k X_k^2/t`; the remainder is `O(X_{k-1}^2/t)`, whose expectation is `O(1)` by the induction hypothesis. The `O(t^-1)` deterministic remainder and bounded martingale variance are also `O(1)` forcing terms. A second discrete Gronwall step gives `E X_k(t)^2=O(t)`. This proves (2.3).

Consequently, for every fixed `epsilon>0`, with

`G_t(epsilon):={max_{m<=k<K0}|N_k(t)-p_k t|<=epsilon t}`,         (2.5)

Chebyshev plus the finite union bound gives

`P(G_t(epsilon)^c)<=C_epsilon/t`.                                (2.6)

**B17 outcome:** successful. The solved finite-degree statistics can be imported with an explicit `O(t^-1)` bad-event probability, strong enough to multiply by the deterministic shadow bound `W_t=O(t)`.

---

## 3. B29 — add one point at infinity and collapse the entire tail

The raw degree law is infinite-dimensional. The bridge slack is not: by (P.1), once `w>=2A` it is exactly the constant `A^2`. Therefore every degree `k>=K0` may be identified with a single compactified state `infinity` **for this observable**.

Let

`S_t^all:=sum_{ordinary u} s(w_u(t))`.                            (3.1)

Since every ordinary degree is at least `m` and `s(k+delta)=A^2` for `k>=K0`,

`S_t^all
 = A^2 t - sum_{k=m}^{K0-1} D_k N_k(t)+O(1)`,                   (3.2)

where the `O(1)` absorbs the finite seed convention. On `G_t(epsilon)`,

`S_t^all >= [S_*-epsilon D_*]t-C`,                               (3.3)

where

`D_*:=sum_{k=m}^{K0-1}D_k<infinity`.                             (3.4)

This is why no uniform-in-`k` degree-count theorem, tail moment, or third moment is needed.

The slack lost by deleting the current shadow is at most `A^2` per shadow vertex. Since every ordinary shadow vertex has attractiveness at least `a`,

`sum_{u outside Q_t, ordinary}s(w_u(t))
 >= S_t^all-(A^2/a)W_t-C`.                                       (3.5)

Combine (3.5) with the exact decomposition

`w c(w)=2Aw-A^2+s(w)`                                             (3.6)

and the inherited identities

`sum_{u outside Q_t, ordinary}w_u=T_t-W_t-Z_t`,
`T_t=At+O(1)`.

Using only that the number of eligible outside ordinary vertices is at most `t+O(1)`, on `G_t(epsilon)` we obtain

`F_t
 >= [A^2+S_*-epsilon D_*]t
    -C W_t-C Z_t-C`.                                              (3.7)

Compare this with the old bound `F_t>=A^2 t-CW_t-CZ_t-C`: (3.7) is a genuine first-order gain.

**B29 outcome:** successful. Compactifying all sufficiently high degrees into one saturated state converts the apparent infinite-tail problem into finitely many degree counts.

---

## 4. Feed the slack into the already-existing gate--bridge term

No exploration rule is changed in this section.

The inherited current-birth bridge proof pairs one retained gate into `Q_t` with one distinct retained capped bridge. Before lower-order duplicate corrections, its conditional reward contains

`m(m-1)pi^2 W_t F_t/(At+K)^2`.                                  (4.1)

The old `A^2 t` part of `F_t` is exactly the `eta_* W_t/t` term already included in `b6` and therefore already included in `b12`.

On `G_t(epsilon)`, the additional slack in (3.7) contributes

`Delta_epsilon W_t/t`,                                           (4.2)

where

`Delta_epsilon
 :=eta_* (S_*-epsilon D_*)/A^2`.                                (4.3)

All error terms are of the same inherited forms

`W_t^2/t^2`, `W_t Z_t/t^2`, `W_t N_t^rep/t^2`, `W_t/t^2`, `1/t`.

On the bad event we simply discard the new slack and retain the old `b12` lower bound. By (2.6) and deterministic `W_t<=At+O(1)`,

`E[W_t 1_{G_t(epsilon)^c}]<=C_epsilon`.                          (4.4)

Hence taking expectations in the full inherited `b12` recurrence gives

`mu_{t+1}
 >= [1+(b12+Delta_epsilon)/t-C/t^2]mu_t
    -C_epsilon/t-C t^(h-1)-C log(t)/t`,                          (4.5)

with `mu_t:=E W_t` and `h=m/A<1/2`.

The same normalized-product bootstrap used in the preceding theorems therefore gives

`gamma_E>=b12+Delta_epsilon`                                     (4.6)

for every sufficiently small fixed `epsilon>0`. Letting `epsilon downarrow0` proves

`gamma_E>=b12+eta_* S_*/A^2=b13`.                               (4.7)

No interchange of limits inside the graph process is being used: `gamma_E` is a fixed number, and (4.6) holds separately for every fixed epsilon, so it is at least the supremum of those lower bounds.

---

## 5. Strictness and unchanged upper/square budgets

Every slack is nonnegative. The degree-`m` atom gives

`s(a)=m^2`,
`p_m=A/(A+ma)>0`,

hence (P.11) and the explicit strict bound (P.12).

Nothing in the stochastic process changed. Therefore every upper first-moment and square-jump estimate from the `b12` artifact remains valid verbatim. For an internal consistency check, the old current-bridge upper allowance was

`eta_U=2 eta_* (A+m)/A`.                                         (5.1)

Since `0<S_*<=A^2`, the **entire refined** current-bridge lower coefficient is at most `2 eta_*`, while

`eta_U=2 eta_*(A+m)/A>2eta_*`.                                   (5.2)

Thus the refined lower coefficient still fits strictly inside the already-paid current-bridge upper allowance. All later historical lower/upper pairs were already dominated individually. Hence

`b13<U12<1/2`,                                                    (5.3)

and the inherited `E W_t^2=O(t)` proof is unchanged.

This is the key advantage of the present route: the exponent moves, but the variance budget does not get any tighter.

---

## 6. Exact specialization `m=2, delta=1`

This finite arithmetic check is **orientation only**, not evidence for the all-parameter theorem. It was executed with exact rational arithmetic in

`artifacts/hard7_2026-09-18/HARD7-04/p0151_degree_slack_exact_20260920T1130Z.py`

and the executed output is archived in

`artifacts/hard7_2026-09-18/HARD7-04/p0151_degree_slack_exact_20260920T1130Z.out`.

Here `A=5`, `K0=9`, and the finite recursion gives

`p_2=5/11`,
`p_3=30/143`,
`p_4=16/143`,
`p_5=160/2431`,
`p_6=1920/46189`,
`p_7=1280/46189`,
`p_8=20480/1062347`,

with compactified tail mass `73728/1062347`. The saturated slack is exactly

`S_*=439710/96577=4.5529473891...`,                              (6.1)

so `S_*/A^2=0.1821178955...`. At the exact critical `pi_c=1/(12+4sqrt(6))`, the free improvement over `b12` is

`eta_*S_*/A^2 = 0.000766568479065366...`.                        (6.2)

Using the preceding run's orientation value `b12≈0.4594477159927709`, this puts the strengthened lower exponent at approximately `0.4602142844718363` in this specialization. The proof itself is symbolic and uniform in `m>=2, delta>0`.

---

## 7. Literature/status boundary

Fresh bounded searches on 20 September 2026 again recovered:

1. Hazra--van der Hofstad--Ray, *Percolation on preferential attachment models*, arXiv:2312.14085 / EJP 31 (2026): exact threshold and giant/no-giant transition for the fixed-outdegree affine model, but not this finite-size critical-window theorem.
2. Jorritsma--Maillard--Mörters, *The critical percolation window in growing random graphs*, arXiv:2512.18937 (22 Dec 2025): `(log n)^(-2)` window and `sqrt(n)/log n` critical component scale for a class where each new vertex connects independently to earlier vertices. That independent-edge hypothesis does not automatically include the exact fixed-`m` sequential model here.
3. Mörters--Schätze, *Critical percolation on preferential attachment graphs with infinite variance*, arXiv:2606.27844 (26 Jun 2026): a different inhomogeneous preferential-attachment-kernel ensemble in the infinite-variance regime.
4. Standard affine preferential-attachment degree-count literature gives the explicit `p_k` above and concentration of finite-degree proportions. Those degree-count facts are **input/folklore here, not claimed as new**; the new route is their use to recover the convex-envelope slack in the existing connected bridge.

No source-matching fixed-outdegree critical-window resolution surfaced in this bounded refresh. This is negative search evidence only, not a worldwide novelty certificate.

---

## 8. What this changes and what it does not

**Changed:** the frozen source-relevant metric moves strictly from

`gamma_E>=b12`

to

`gamma_E>=b13=b12+m(m-1)pi_c^2 S_*/A^2>b12`.

**Unchanged:** the source remains **OPEN**. This proves neither `gamma_E=1/2` nor a matching upper bound, the `(log n)^(-2)` finite-graph window, `sqrt(n)/log n` component scaling, tightness, nor a limiting law.

The strongest next research route suggested by this proof is to stop adding new tickets and instead **re-optimize old inequalities against exact finite-dimensional occupation statistics**. The current cap has now yielded its entire degree-distribution slack. A genuinely different subsequent route should either (i) replace the scalar cap by a Perron-weighted age/type profile tied to the killed-PPT eigenfunction, or (ii) prove a finite-to-local transfer on a fixed log-age slab and then let the slab width grow after the `n->infinity` exponent limit.
