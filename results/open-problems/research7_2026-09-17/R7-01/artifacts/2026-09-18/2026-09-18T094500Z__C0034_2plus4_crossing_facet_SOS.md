Model actually running: **GPT-5.6 Sol. Reasoning level: UNVERIFIED** — this is **not GPT-6 at maximum**; no authenticated runtime reasoning-effort telemetry or binding selector is exposed.

# C0034 — a second genuinely colored facet orbit has an exact rank-two occupation sum-of-squares certificate

Target: Russell Lyons, *Determinantal Probability: Basic Properties and Conjectures* (ICM 2014), Question 2.8. This artifact continues the admitted R7-01 C0034 track. It proves a new restricted theorem on the minimal six-point rank-`2+2` core; it does **not** solve the full source question and does not move the frozen source metric `R_univ`.

## 1. Six-point colored marginal polytope

Let `C^6 = H_1 \oplus H_2 \oplus H_3`, `dim H_r=2`. For each color `r` and edge `e={i,j} subset [6]`, write `w^r_e = |Delta^r_e|^2`, where `Delta^r_e` is the corresponding `2 x 2` Pluecker minor of an orthonormal two-row basis of `H_r`.

As in the preceding C0034 reduction, feasibility of Lyons's union coupling on this minimal core is equivalent to membership of `(w^1,w^2,w^3)` in the convex hull `P_col` of the ninety ordered rainbow perfect matchings `(A,B,C)` partitioning `[6]` into three labeled pairs.

Fix a two-set `X subset [6]` and put `Y=[6]\X`. For each color define the crossing mass

`c_r(X) := sum_{i in X, j in Y} w^r_{ij}`.

We prove that for every permutation `(r,s,t)` of the three colors,

`c_r(X) <= c_s(X)+c_t(X)`.                                      (1.1)

The family (1.1) is a genuinely colored facet orbit of `P_col`, and every member of the orbit has an exact nonnegative Pluecker certificate.

## 2. B16: exact facet statement on the 90 deterministic vertices

At a deterministic colored perfect matching, let `chi_r` be the indicator that the color-`r` edge crosses the cut `X|Y`.

Because `|X|=2`, a perfect matching has either zero or two crossing edges across this cut. Thus `chi_1+chi_2+chi_3 in {0,2}`. Therefore, for every singled color `r`, `chi_r <= chi_s+chi_t`, which proves validity of (1.1) on every vertex of `P_col`.

The exact checker `research7_2026-09-17/R7-01/artifacts/2026-09-18/2026-09-18T094200Z__check_C0034_2plus4_crossing_facet.py` uses only integer/Fraction arithmetic and verifies:

- 90 colored-perfect-matching vertices;
- linear rank `38` and affine dimension `37`;
- for the canonical cut `{0,1}|{2,3,4,5}` and singled color 1, 66 tight vertices and 24 vertices with slack exactly 2;
- tight-face affine dimension `36`, so the inequality is a genuine facet;
- full `S_6 x S_3` orbit size `45`, exactly `15` two-sets times `3` singled colors.

The archived output ends `ALL_EXACT_CHECKS_PASS`.

This orbit is distinct from the preceding 30-element balanced-`3+3` internal-edge orbit: here the coordinate cut has type `2+4`, and the inequality is on crossing rather than same-side mass.

## 3. B18: translate the crossing mass into a rank-two auxiliary DPP occupation event

Fix the cut `X|Y` with `|X|=2`. Let `P_X` be the coordinate projection onto `span{e_i:i in X}`. Choose an orthonormal basis of `C^6` adapted to the decomposition `H_1\oplus H_2\oplus H_3`, and express `P_X` in this basis. The resulting matrix `Q` is a rank-two orthogonal projection on a six-dimensional space split into three two-dimensional blocks `B_1,B_2,B_3`. Write its `2 x 2` diagonal blocks as `Q_rr`.

For color `r`, Cauchy--Binet gives

`Pr_{P^{H_r}}(both selected coordinates lie in X) = det Q_rr`,

and

`Pr_{P^{H_r}}(both selected coordinates lie in Y) = det(I_2-Q_rr)`.

Because the rank-two projection DPP `P^{H_r}` always selects exactly two coordinates,

`c_r(X) = 1-det Q_rr-det(I_2-Q_rr) = tr Q_rr - 2 det Q_rr`.       (3.1)

Now choose a `2 x 6` matrix `Z` with orthonormal rows and `Q=Z^*Z`. Let `S` be the rank-two projection DPP with kernel `Q`, so `Pr(S=T)=|det Z_T|^2` for `|T|=2`. Define block occupations `N_r := |S cap B_r|`.

Then `N_1+N_2+N_3=2` almost surely. Standard projection-DPP inclusion identities give `E N_r = tr Q_rr` and `Pr(N_r=2)=det Q_rr`. Hence

`Pr(N_r=1)=E N_r-2Pr(N_r=2)=tr Q_rr-2det Q_rr=c_r(X)`.           (3.2)

Thus the colored cut statistic has become a one-line occupation probability of an auxiliary rank-two DPP.

## 4. Pointwise occupation inequality and exact SOS gap

Since `N_1+N_2+N_3=2`, for every permutation `(r,s,t)` we have pointwise

`1_{N_r=1} <= 1_{N_s=1}+1_{N_t=1}`.                              (4.1)

Indeed, if `N_r=1`, the remaining one particle lies in exactly one of the other two blocks. Taking expectations and using (3.2) proves (1.1) for every orthogonal `2+2+2` flag.

More precisely, the random variable `1_{N_s=1}+1_{N_t=1}-1_{N_r=1}` is zero in every occupation pattern except `(N_r,N_s,N_t)=(0,1,1)`, where it equals two. Consequently

`c_s(X)+c_t(X)-c_r(X) = 2 Pr(N_r=0,N_s=1,N_t=1)`.                (4.2)

Because `S` has size two, the event on the right is exactly the event that one selected basis index lies in `B_s` and one in `B_t`. Therefore

`c_s(X)+c_t(X)-c_r(X)`

`= 2 sum_{i in B_s} sum_{j in B_t} |det Z_{\{i,j\}}|^2 >= 0`.     (4.3)

Equation (4.3) is an explicit four-square Pluecker certificate for the entire 45-facet orbit. Equality holds exactly when every mixed `2 x 2` minor between blocks `B_s` and `B_t` vanishes.

## 5. B24: exact extremal slack

The representation (4.2) immediately identifies the extremal value of the facet slack over the full orthogonal flag manifold:

`0 <= c_s+c_t-c_r <= 2`.                                         (5.1)

The upper bound is attained. Choose the rank-two auxiliary projection `Q` to project onto one basis direction in `B_s` and one basis direction in `B_t`. Then its rank-two DPP selects exactly those two directions, so `Pr(N_r=0,N_s=1,N_t=1)=1` and the slack equals two. Every rank-two projection is unitarily conjugate to the coordinate projection `P_X`, so such a `Q` arises from an actual orthogonal `2+2+2` flag.

Thus the facet is not only valid; its full allowed slack interval `[0,2]` is attained on the Pluecker image.

## 6. Scope boundary and cumulative meaning

Combining this artifact with the preceding balanced-cut artifact proves two complete genuinely colored facet orbits of the six-point marginal polytope:

- 30 balanced-`3+3` internal-edge facets;
- 45 `2+4` crossing facets.

Both orbits admit exact low-degree occupation/SOS certificates on every orthogonal Pluecker flag.

This is strong evidence for a more general mechanism: colored matching facets may correspond to pointwise occupation inequalities of auxiliary projection DPPs after choosing a coordinate cut of the appropriate rank. However, no irredundant exhaustive facet theorem for `P_col` is proved here. In particular, it is not yet established that nonnegativity plus these 75 colored cut facets generate the entire dual cone. Therefore the six-point rank-`2+2` coupling theorem, the total-rank-four theorem, and the unrestricted Lyons source question all remain open in this track.

Frozen source metric remains `R_univ >= 3`.

Status of this artifact: **complete restricted theorem / source PARTIAL**.
