SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B03, 2026-09-24T10:57:46Z.
attacking: a nonzero-pivot-stable decoupled time estimate for a same-bank square plus one independent hyperbolic scalar, without any marginal cap on the hyperbolic same-bank coordinate.

# account03/B03 r53 — square-hyperbolic weighted collision theorem

Status: **new supporting theorem proved; full QFORM OPEN; full-target continuity OPEN; WITHOUT_VERIFIED_BRAIN**.

Owner/control at final prepublication refresh: math-research-brain main `7e776fffb3cdb145111713d8a29f59a126dc7838`, OWNER CONTROL revision `2026-09-22.15`, QFORM-only, no account03/B03 pause. Live correction inbox was reread. This proof uses no pointwise quadratic van-der-Corput decay, no independence of sum/difference variables, no conditional cap for a conjugate pair, no arbitrary-joint 3D coarea theorem, and no positive conditional projection-density moment.

## 1. Main theorem

### `QFORM-SQUARE-HYPERBOLIC-WEIGHTED-COLLISION-v1`

Let `(S,R)` have an arbitrary joint probability density `g` with

`||g||_infinity <= M`.

Let `V` be independent of `(S,R)` with probability density `h` satisfying

`||h||_infinity <= N`.

Let `a,b` be nonzero real numbers and let `G,H,K` be arbitrary measurable real functions for which

`Q = a (S+G(R))^2 + 2 b R V + H(R) + K(V)`

is well defined. Then

`A_-(Q) := integral_R |t|^(-1/2) |phi_Q(t)|^2 dt`

is finite and obeys

`A_-(Q) <= 3 sqrt(6 pi) (M N)^(1/3) |a|^(-1/6) |b|^(-1/3).`      (1.1)

Equivalently, if `Q'` is an independent copy of the **whole scalar output** `Q`, then

`E |Q-Q'|^(-1/2) <= 3 sqrt(3) (M N)^(1/3) |a|^(-1/6) |b|^(-1/3).` (1.2)

The theorem is stable under an arbitrary scalar phase `K(V)`. In particular, `K(V)=dV^2+ell V+c` may contain an arbitrarily large or arbitrarily small **nonzero physical scalar pivot**. It is also stable under arbitrary same-bank baggage `H(R)` and arbitrary triangular same-bank shear `G(R)`. Crucially, no density bound for the marginal law of `R` is assumed or needed.

This is a weighted collision/time estimate. By itself it does **not** assert that `Q` has a bounded one-copy density.

## 2. Slice fourth-moment estimate

Shear `S` by `G(R)`. The map `(s,r) -> (s+G(r),r)` has Jacobian one, so the transformed joint density is still bounded by `M`. Thus take `G=0`.

For almost every `r`, put

`m(r)=integral g(s,r) ds`,

`A_r(t)=integral g(s,r) exp(i a t s^2) ds`.

Let `k_r(y)` be the pushforward density of the finite measure `g(s,r) ds` under `s -> s^2`. Then

`integral k_r = m(r)`,

and for `y>0`,

`k_r(y)=[g(sqrt(y),r)+g(-sqrt(y),r)]/(2 sqrt(y)) <= M y^(-1/2).`  (2.1)

Hence

`integral k_r(y)^(4/3) dy`
` <= M^(1/3) integral k_r(y) y^(-1/6) dy`
` =  M^(1/3) integral g(s,r) |s|^(-1/3) ds.`                    (2.2)

Among functions `0<=f<=M` of mass `m`, the integral against the decreasing symmetric kernel `|s|^(-1/3)` is maximized by the centered interval of length `m/M`. Therefore

`integral g(s,r)|s|^(-1/3) ds`
` <= 3*2^(-2/3) M^(1/3)m(r)^(2/3).`                            (2.3)

Combining (2.2)-(2.3),

`||k_r||_(4/3) <= [3*2^(-2/3)]^(3/4) M^(1/2)m(r)^(1/2).`       (2.4)

Use the Fourier convention `hat f(xi)=integral exp(i xi y) f(y)dy`. Interpolating `L1->Linf` with Plancherel gives Hausdorff-Young

`||hat f||_4 <= (2 pi)^(1/4)||f||_(4/3).`

Since `A_r(t)=hat k_r(a t)`, (2.4) yields

`||A_r||_4^2 <= (3/2) sqrt(6 pi) M m(r) |a|^(-1/2).`            (2.5)

Now define

`F(t)=integral |A_r(t)|^2 dr.`

Minkowski and `integral m(r)dr=1` give the dimension-free estimate

`||F||_2 <= (3/2) sqrt(6 pi) M |a|^(-1/2).`                    (2.6)

No marginal cap for `R` appears.

## 3. Bilinear Plancherel with arbitrary scalar pivot retained

Set

`q_t(r)=A_r(t) exp(i t H(r))`,

`w_t(v)=h(v) exp(i t K(v))`.

Then

`phi_Q(t)=integral integral q_t(r) w_t(v) exp(i 2 b t r v) dr dv.` (3.1)

The arbitrary `K(V)` is only a unit-modulus factor. Since `h<=N` and `integral h=1`,

`||w_t||_2^2=integral h(v)^2 dv <= N.`                          (3.2)

Cauchy-Schwarz in `v`, the change of variables `xi=2btv`, and Plancherel in `r` give, for `t!=0`,

`|phi_Q(t)|^2 <= [pi N/(|b t|)] F(t).`                         (3.3)

This step never splits a conjugate sum from its difference; it works in the genuine independent physical banks `(S,R)` and `V`.

## 4. Exact weighted-time optimization

For `T>0`, use `|phi_Q|<=1` on `|t|<=T` and (3.3) outside:

`A_-(Q)`
` <= 4 sqrt(T)`
`   + [pi N/|b|] integral_(|t|>T) |t|^(-3/2) F(t) dt.`         (4.1)

By Cauchy-Schwarz and (2.6),

`integral_(|t|>T)|t|^(-3/2)F(t)dt`
` <= ||F||_2 [integral_(|t|>T)|t|^(-3)dt]^(1/2)`
` <= [(3/2)sqrt(6 pi) M |a|^(-1/2)] / T.`                     (4.2)

Thus

`A_-(Q) <= 4 sqrt(T) + D/T`,

`D=(3 pi/2)sqrt(6 pi) M N |a|^(-1/2)|b|^(-1).`                (4.3)

The minimum occurs at `T^(3/2)=D/2`, and

`min_T [4 sqrt(T)+D/T] = 3*2^(2/3)D^(1/3)`
` = 3 sqrt(6 pi)(M N)^(1/3)|a|^(-1/6)|b|^(-1/3),`             (4.4)

proving (1.1).

Using the regularized Fourier-Riesz identity

`integral_R |t|^(-1/2) exp(i t x) dt = sqrt(2 pi)|x|^(-1/2)`,

with `|phi_Q(t)|^2=E exp(i t(Q-Q'))` for an independent copy of the **whole** output, (1.2) follows from (1.1).

## 5. How the assigned time estimate recovers linear small-ball scaling

The negative-half weighted energy in (1.1) becomes a density estimate once there is a genuinely source-disjoint positive-half Fourier resource.

Let `X,Y` be independent two-dimensional physical-coordinate banks, independent also of `Q`, with joint densities bounded by one. Let `C` be an invertible `2x2` matrix and let `F_0(X),G_0(Y)` be arbitrary measurable phases. Define

`T_0=F_0(X)+G_0(Y)+X^T C Y.`

Two-bank Plancherel gives

`|phi_(T_0)(t)| <= min{1, 2 pi |det C|^(-1/2)|t|^(-1)}.`       (5.1)

Consequently

`A_+(T_0):=integral |t|^(1/2)|phi_(T_0)(t)|^2 dt`
` <= (16/3)(2 pi)^(3/2)|det C|^(-3/4).`                       (5.2)

Because `Q` and `T_0` are independent,

`phi_(Q+T_0)=phi_Q phi_(T_0)`.

Cauchy-Schwarz with the complementary weights `|t|^(-1/2)` and `|t|^(1/2)` gives

`integral |phi_(Q+T_0)(t)|dt <= sqrt(A_-(Q) A_+(T_0)).`        (5.3)

Fourier inversion therefore gives a continuous `C_0` density and the explicit bound

`||p_(Q+T_0)||_infinity`
` <= 4*3^(1/4) (M N)^(1/6)|a|^(-1/12)|b|^(-1/6)|det C|^(-3/8).` (5.4)

Hence every interval `I` obeys the genuine linear small-ball estimate

`P(Q+T_0 in I) <= RHS(5.4) * |I|.`                            (5.5)

This is a sufficient branch with an actual source-disjoint complementary crossing. The theorem does **not** claim that every unresolved QFORM matrix automatically supplies such a crossing.

## 6. Strict target-valid nonzero-pivot example

Let independent cap-one physical variables be `X1,X2,X3`, and set

`S=(X1+X2)/sqrt(2)`,
`R=(X1-X2)/sqrt(2)`,
`V=X3`.

For generic non-Gaussian inputs, `S` and `R` are dependent. Their joint density is merely the orthogonal image of the product density, hence has cap `M<=1`; `V` has cap `N<=1`.

Take

`Q_*=S^2+4 R V+V^2.`                                         (6.1)

In `(S,R,V)` coordinates the coefficient matrix is

`B_*=[[1,0,0],[0,0,2],[0,2,1]]`,

whose eigenvalues are

`1, (1-sqrt(17))/2, (1+sqrt(17))/2`.

All three have modulus strictly larger than one. In the original independent coordinates,

`A_*=[[1/2,1/2,sqrt(2)], [1/2,1/2,-sqrt(2)], [sqrt(2),-sqrt(2),1]]`,

so this is a literal rotated target instance with a **nonzero scalar pivot** `V^2` retained.

Here `a=1`, `b=2`, `M=N=1`. The new theorem gives

`A_-(Q_*) <= 3 sqrt(6 pi) 2^(-1/3)`
`           = 10.337808534221727...`,                         (6.2)

and

`E|Q_*-Q_*'|^(-1/2) <= 3 sqrt(3) 2^(-1/3)`
`                      = 4.124188910995808...`.               (6.3)

If one adds an independent physical two-bank crossing with `det C=1`, (5.4) gives

`||p||_infinity <= 4*3^(1/4)*2^(-1/6)`
`                  = 4.689954604468751...`,                  (6.4)

with a continuous `C_0` density and linear interval scaling. The original three large eigenvalues persist in the enlarged block.

This example lies outside r52's exact zero-pivot hypothesis; the new time estimate keeps the `V^2` term exactly rather than deleting it as a perturbation.

## 7. Required partner application: account04/B03 r5

The latest completed designated-partner report is

`yspennstate/math-open-problems@fbe1dfba05eea312d8f12f22f2132476758039a8`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B03/20260924T101358Z-account04-B03-pivot-crossing-r5/REPORT.md`.

Its theorem states that for a physical pivot `d` and a disjoint `3x3` pivot-crossing minor `M_3`,

`||p_P||_infinity <= 4 sqrt(2) |d det M_3|^(-1/4).`            (7.1)

Apply it to its explicit five-coordinate target block, where `d=1` and `M_3=I_3`. Then

`||p_P||_infinity <= 4 sqrt(2).`                              (7.2)

The cap-to-half-Riesz / whole-copy conversion gives the concrete assigned-weight inequality

`integral |t|^(-1/2)|phi_P(t)|^2 dt`
` <= 4 sqrt(pi ||p_P||_infinity)`
` <= 8 sqrt(pi sqrt(2))`
` = 16.862517844086494... .`                                  (7.3)

This is an equation-level application of the completed account04/B03 result, with its exact hypotheses retained.

## 8. What changed and what remains open

The new analytic point is that the r52 zero-pivot architecture has a **weighted-collision extension through an arbitrary nonzero scalar pivot**. The scalar phase `K(V)` disappears inside the `L2` norm in the bilinear Plancherel step; the same-bank coordinate `R` needs no marginal density bound. This closes a real time-integral gap that r50's random-slope theorem could not cover when the `R` marginal is highly concentrated.

It does not by itself convert the bare nonzero-pivot `2+1` packet to a one-copy `L-infinity` density bound. The missing implication is now precise: either

1. manufacture a source-disjoint positive-half Fourier resource and use (5.4), or
2. exploit additional product provenance inside the same packet to upgrade the negative-half collision estimate to one-copy height without an independent complement.

The unrestricted three-large-eigenvalue conjecture remains **OPEN**. Full-target continuity remains **OPEN**. Continuity is proved only in the complementary-crossing branch (5.4).

## 9. Source pins

- fresh control at final refresh: `yspennstate/math-research-brain@7e776fffb3cdb145111713d8a29f59a126dc7838`, OWNER CONTROL `2026-09-22.15`;
- assignment: `scheduled_tasks/work/shared/qform-density-2026-09-22/assignments/account03/B03.json`;
- live corrections reread from the same fresh main;
- prior r52 zero-pivot report: `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260924T095801Z-account03-B03-QFORM-auto11-r52/REPORT.md`;
- completed partner r5: `yspennstate/math-open-problems@fbe1dfba05eea312d8f12f22f2132476758039a8`, path given in Section 7.

Repository use is not native learned-memory ingestion. Execution remains `WITHOUT_VERIFIED_BRAIN` unless a separate authenticated receiver use is actually observed.
