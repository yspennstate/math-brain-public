SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B05, 2026-09-23T20:05:16Z.
attacking: the fresh affine-shear caveat in the curved two-sheet tube; prove a Borel square-root tube profile and a full null-hub density theorem before any full partner slicing.

# account02/B05 — affine-shear Borel tube and null-hub receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.  
**Status:** `PROVED_SUPPORTING_THEOREM / NEW PARTNER-PLANE CHAMBER CLOSED / FULL QFORM OPEN`.  
**Regularity:** essential boundedness is proved in the stated scope; continuity is not claimed.

## 1. First unpaid implication and the new correction

The freshest compatible interactive handoff is the curved-dyadic-product-tube report at

`yspennstate/math-open-problems@728e325d9c432026bd364c676c6b293f13b41256:`
`proofnet24/QFORM-density/interactive/20260923T202000Z-curved-dyadic-product-tube/REPORT.md`.

It proves an `O(a r^2)` tube bound for three independent physical axes when the center has no affine-in-`L` shear, but it also gives an explicit independent cap-one saddle showing that after the canonical term `beta L^2+2 epsilon L P` is divided by `2 epsilon L`, the induced affine term `dL` can force tube mass of order

`a r^2 log(1/r)`.

So the stronger `O(a r^2)` statement is unavailable uniformly in `d`. The same report points out that any gain `a r^(1+alpha)` with `alpha>0` is still sufficient for the small-`L` dyadic summation. This run proves such a gain with `alpha=1/2` whenever the smoothing scalar comes from a disjoint original-coordinate bank. It is a Borel estimate, not an interval-to-Borel promotion.

The first unpaid implication after the theorem below is therefore

`QFORM-PARTNER-PLANE-MIXED-ONLY-TRACE-v1`:

retain one independent scalar hub and one partner coordinate random in the chamber where the transverse square currencies `T_Y,T_Z` vanish or become too small, and spend the same-plane mixed currency `U` before full partner slicing. The present theorem pays the nonzero transverse-square chamber uniformly through arbitrary affine shear and through `tau -> 0` after the exact partner normalization.

## 2. A Borel square-root tube lemma uniform in affine shear

### Theorem 2.1 — `QFORM-AFFINE-SHEAR-BOREL-TUBE-v1`

Let `(L,V)` have a joint probability density `rho` satisfying

`||rho||_infinity <= M_2`.

Let `P` be independent of `(L,V)`, with probability density `f_P` and

`||f_P||_infinity <= M_1`.

Fix arbitrary real `c,d,gamma`, `r>0`, and define the shell submeasure

`nu_r(E)=P(r<=|L|<=2r, dL+c+(gamma+V^2)/(2L) in E)`.

Then for every Borel set `E` of finite Lebesgue measure `m`,

`boxed{ nu_r(E) <= K_0 M_2 r^(3/2) m^(1/2), }`                         (2.1)

where

`K_0=(8/3)(4-sqrt(2))=6.895430500338... < 6.896`.                     (2.2)

Moreover the shell-restricted law of

`P+dL+c+(gamma+V^2)/(2L)`

has an essentially bounded density `h_r` with

`boxed{ ||h_r||_infinity <= K_0 M_2 sqrt(M_1) r^(3/2). }`             (2.3)

Consequently every width-`2a` tube obeys

`boxed{ P(r<=|L|<=2r, |P+dL+c+(gamma+V^2)/(2L)-q|<=a)`
`        <=2 K_0 M_2 sqrt(M_1) a r^(3/2). }`                          (2.4)

All constants are uniform in `c,d,gamma,q`. No support, moment, continuity, log-concavity, or independence between `L` and `V` is assumed.

### Proof

Fix `l != 0`. Translation by `d l+c+gamma/(2l)` does not affect inverse-image length, so only the map

`v -> v^2/(2l)`

matters. Its pushforward of one-dimensional Lebesgue measure has density

`sqrt(2|l|) |y|^(-1/2)`

on the half-line with sign `sign(l)`. Therefore, for any Borel set of length `m`, decreasing rearrangement of `|y|^(-1/2)` gives

`Leb{v: v^2/(2l) in E-shift} <= sqrt(2|l|) int_0^m y^(-1/2)dy`
`                                  =2 sqrt(2|l|m).`                   (2.5)

Using `rho<=M_2` and integrating over both sign components of the shell,

`nu_r(E)`
` <=2 sqrt(2) M_2 sqrt(m) int_{r<=|l|<=2r} sqrt(|l|) dl`
` =(8 sqrt(2)/3)(2^(3/2)-1) M_2 r^(3/2) sqrt(m)`
` =K_0 M_2 r^(3/2) sqrt(m)`,

which proves (2.1). This is directly a Borel-set estimate; no frozen-slice interval profile is promoted to an arbitrary-set profile.

For (2.3), write the shell convolution at a point `q` and use layer cake:

`h_r(q)=int f_P(q-z) nu_r(dz)`
`      =int_0^M1 nu_r({z:f_P(q-z)>t}) dt`.

By (2.1), followed by Cauchy-Schwarz and the layer-cake identity for the probability density `f_P`,

`h_r(q)`
` <=K_0 M_2 r^(3/2) int_0^M1 |{f_P>t}|^(1/2) dt`
` <=K_0 M_2 r^(3/2) sqrt(M_1 int_0^M1 |{f_P>t}|dt)`
` = K_0 M_2 sqrt(M_1) r^(3/2).`

This proves (2.3), and (2.4) follows by integrating the density over an interval of length `2a`. QED.

The fresh saddle counterexample is consistent with (2.4): `a r^2 log(1/r)=o(a r^(3/2))` as `r downarrow 0`. Thus it falsifies the stronger exponent `2` but not the `3/2` estimate proved here.

## 3. Full-line null-hub density theorem

The shell estimate can be summed without any support assumption.

### Theorem 3.1 — `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1`

Let `H` be independent of `(L,V)`, with density cap `m`, and let `(L,V)` have joint density cap `M`. For arbitrary real coefficients and `c_2 != 0`, put

`Q=2HL+aL^2+2bLV+c_2 V^2+dL+eV+f`.                                  (3.1)

Then for every interval `I`,

`P(Q in I) <= C_* (M m)^(2/3) |c_2|^(-1/3) |I|`,                     (3.2)

where

`C_* = 3*2^(-2/3) * [(K_0/2)(1+sqrt(2))]^(2/3)`
`    =7.761982175235... <7.762`.                                      (3.3)

Hence `Q` has a density and

`boxed{ ||p_Q||_{infinity,ess} <= 7.762 (M m)^(2/3)|c_2|^(-1/3). }`   (3.4)

### Proof

First make the determinant-one shear/translation

`V'=V+(b/c_2)L+e/(2c_2)`.

The pair `(L,V')` still has joint density cap `M`, and

`Q=2HL+c_2 V'^2+A L^2+D L+F`                                        (3.5)

for suitable real `A,D,F`. Let `I` have length `h` and center `t`. On the shell `r<=|L|<=2r`, the event `Q in I` implies

`|H+(A/2)L+D/2+(F-t+c_2 V'^2)/(2L)| <= h/(4r).`                       (3.6)

Scale the square variable in Theorem 2.1; the factor becomes `|c_2|^(-1/2)`. Therefore

`P(Q in I, r<=|L|<=2r)`
` <= (K_0/2) M sqrt(m) |c_2|^(-1/2) h sqrt(r).`                       (3.7)

For the large-`L` region, condition on `(L,V)`. Since `Q` is affine in `H` with slope `2L`,

`P(Q in I | L,V) <= m h/(2|L|).`                                     (3.8)

Fix `R>0`. Sum (3.7) over shells

`2^(-k-1)R <= |L| <= 2^(-k)R`, `k>=0`.

Because

`sum_{k>=0} sqrt(2^(-k-1)R) = (1+sqrt(2)) sqrt(R)`,

the small-`L` contribution is at most

`A_0 M sqrt(m)|c_2|^(-1/2) h sqrt(R)`,
`A_0=(K_0/2)(1+sqrt(2))=8.323520916159...`.                           (3.9)

Sum (3.8) over `2^k R<=|L|<=2^(k+1)R`; the large-`L` contribution is at most

`m h/R`.                                                             (3.10)

Optimising `A sqrt(R)+m/R` gives `R^(3/2)=2m/A` and the minimum

`3*2^(-2/3) A^(2/3)m^(1/3)`.

Substituting the value of `A` in (3.9) gives exactly (3.2)-(3.3). Since the interval bound is uniform over all intervals, the law is absolutely continuous with essential density bounded by the same constant. No continuity conclusion is used. QED.

## 4. Application to the newest account03/B05 partner-plane theorem

The newest compatible partner report is

`yspennstate/math-open-problems@c4e5d92483b9f6f0992fc3df61dc78d2f6eba272:`
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B05/20260923T190745Z-account03-B05-QFORM-r30/REPORT.md`.

Its exact packet has a first product bank

`W=(S,R)=Gamma^T X`,

and two independent scalar product banks `Y,Z`. With partner vectors `p=(alpha,r)` and `q=(beta,s)`, `tau=det(p q) !=0`, it defines

`ell_Y=p^T W`, `ell_Z=q^T W`,
`u=(-r,alpha)`, `v=(-s,beta)`,
`T_Y=u^T C u`, `T_Z=v^T C v`, `U=u^T C v`.

The partner proves the exact identity

`W^T C W = tau^(-2)(T_Z ell_Y^2 -2U ell_Y ell_Z +T_Y ell_Z^2)`.       (4.1)

It also proves that slicing on both `ell_Y,ell_Z` freezes `T_Y,T_Z,U`; hence a valid proof must spend some of this partner-plane curvature before the full slice.

Theorem 3.1 does exactly that in the zero-diagonal one-partner chamber. Suppose, for example, the physical scalar bank `Z` has zero quadratic diagonal in the packet. Condition on `Y` and every disjoint outside variable, but **do not** condition on the first product bank or on `Z`. Then `Z` is a null hub coupled to `ell_Z` (up to a conditioned translation), while `(ell_Z,ell_Y)` is a two-dimensional linear image of the product projection `W`.

The two-dimensional product-projection density bound used in the pinned ruled theorem gives

`M <= 2/|tau|`.                                                       (4.2)

By (4.1), the coefficient of the transverse square `ell_Y^2` is

`c_2=T_Z/tau^2`.                                                      (4.3)

All mixed partner-plane curvature `-2U ell_Y ell_Z/tau^2`, every conditioned affine term, and every resulting affine shear are allowed by Theorem 3.1. Therefore

`boxed{ ||p_Q||_infinity <= C_* (2 m_Z)^(2/3) |T_Z|^(-1/3), }`        (4.4)

uniformly in `tau`, `U`, the conditioned value of `Y`, and all outside affine translations. The powers of `tau` cancel exactly:

`(2m_Z/|tau|)^(2/3) (|T_Z|/tau^2)^(-1/3)=(2m_Z)^(2/3)|T_Z|^(-1/3).`

For a normalized scalar product projection, the standard one-dimensional Rogozin/Ball projection cap gives `m_Z<=sqrt(2)`, and hence

`boxed{ ||p_Q||_infinity < 15.524 |T_Z|^(-1/3). }`                   (4.5)

The symmetric statement holds if the `Y` diagonal is zero, with `T_Y` in place of `T_Z`.

This is the substantive partner application: the partner's exact coordinate formula identifies the correct transverse coefficient, while the new Borel tube theorem spends it **before** both partner coordinates are frozen. It also repairs the newest affine-shear counterexample automatically. What remains is the genuine mixed-only chamber in which the available zero-diagonal hub has vanishing transverse-square currency; there the moving `U` slope must be used directly rather than hidden in an unrestricted fiber supremum.

## 5. Required pinned e5f source applied to the real obstruction

The required source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:`
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`

was read through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Its completed Theorem F says that an exact-rank-three spectral frame whose every original-coordinate leverage is at most `1/2` already has

`||p_Q||_infinity <=12`                                               (5.1)

at target normalization. Therefore the new partner-plane bridge is not needed in the diffuse exact-rank-three class: an unpaid exact-rank-three instance must enter the high-leverage side. This is a real reduction of the remaining obstruction, not a restatement of the source.

The same pinned source's ruled Theorem C gives the complementary one-sheet half-line estimate

`p_Q(s)<=pi sqrt(2)` for `s>=0` in signature `(2,1)`.                  (5.2)

Thus the curved receiver above is aimed at the genuinely complementary convex/two-sheet/high-leverage geometry; it does not replace the ruled calculation or flatten its fibers.

## 6. Why the live corrections are respected

1. **No post-rotation independence.** `L,V` are allowed to be dependent; only their honest joint density cap is used. The only independence is between the disjoint scalar bank `H` and the first product bank.
2. **No arbitrary-joint 3D coarea.** The proof uses a two-dimensional product-projection cap plus a separate independent scalar convolution. It would be false for an arbitrary three-dimensional joint density.
3. **No unrestricted curved-fiber supremum.** The key estimate is the exact Borel inverse-image integral (2.5), averaged against the actual pair density.
4. **No interval-to-Borel promotion.** Equation (2.1) is proved directly for every Borel set before the scalar receiver is applied.
5. **No small-coefficient-as-small-error argument.** The affine shear `d` is completely arbitrary and disappears by translation in the exact inverse-image calculation.

## 7. Remaining exact gap

The new theorem closes the disjoint-scalar, nonzero-transverse-square null-hub chamber, uniformly in the partner determinant `tau` and in the affine shear that falsifies the stronger `r^2` tube claim. It does **not** close the partner's mixed-cancellation chamber where the available transverse square `T_Z` (or symmetrically `T_Y`) tends to zero while `U` remains the relevant partner-plane currency.

The next implication is therefore:

`QFORM-PARTNER-PLANE-MIXED-ONLY-TRACE-v1` — prove a partial-slice `O(epsilon)` estimate that keeps one partner coordinate random and spends the moving mixed slope `U`, with the second scalar bank retained as an independent product source. Any proof must remain stable as `T_Y,T_Z ->0`, avoid a full two-partner slice, and avoid replacing the resulting curved trace by a worst fiber supremum.

Full QFORM remains OPEN. Independent review of the new theorem is PENDING.
