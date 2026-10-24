SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B14, 2026-09-23T18:57:32Z.
attacking: rough-center aggregation before fractional scale inversion—average arbitrary translation labels for the full Gaussian-mixture theorem, identify the exact T^{-1/3} localization debt at k=3, and sharpen the partner rough-hub square receiver with a mass-homogeneous L^{3/2} estimate.

# QFORM-CENTER-AGGREGATION-FRACTIONAL-SCALE-BARRIER-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_THEOREMS_PROVED / FULL_QFORM_OPEN`  
Continuity: separate; partner branch continuity remains available after the receiver sharpening below.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. First unpaid implication

`QFORM-FINAL-CAP-BEFORE-FRACTIONAL-SCALE-v1`: after arbitrary random translation labels are averaged, the k=3 Gaussian certificate still pays the fractional component-scale moment `E T^{-1/3}`. In every surviving rough/no-pivot configuration, either replace that reciprocal component scale by a quantity controlled by the **final** cap-one marginal with no fragment/support/moment parameter, or force a whole-law D'/D5/projected-crossing/hub/pair/ridge/rough-core certificate before active component normalization.

The theorem below proves that random centers themselves are not the debt. The following obstruction proves that even the weaker `T^{-1/3}` debt cannot remain uniformly bounded on arbitrary finite-fragment cap-one laws.

## 2. Exact zero-tax aggregation of random centers

Use the proved full Gaussian-mixture theorem in its conditional form. Let

`X_i = M_i + sqrt(T_i) G_i`,

where the coordinate pairs `(M_i,T_i)` are independent, `T_i>0`, and the `G_i` are independent standard Gaussians independent of the pairs. No independence between `M_i` and `T_i` inside one pair is assumed. Let

`Q=X^T A X+b^T X+c`,

and for fixed `T=(T_i)` write `D=diag(T_i)`,

`B(T)=D^(1/2) A D^(1/2)`, `W_k(T)=e_k(B(T)^2)`.

The completed Gaussian calculation gives, for every fixed `(M,T)` and every `3<=k<=rank(A)`,

`||p_{Q|M,T}||_infinity <= I_k/(2 pi) W_k(T)^(-1/(2k))`.                 (2.1)

The right side is independent of the center vector `M`: all center and affine dependence enters only through a Gaussian linear phase/exponential factor of modulus at most one. Therefore, conditioning only on `T` and averaging over the complete conditional law of `M` gives the **same** bound,

`||p_{Q|T}||_infinity <= I_k/(2 pi) W_k(T)^(-1/(2k))`.                   (2.2)

A second mixture step gives

`boxed{ ||p_Q||_infinity <= I_k/(2 pi) E W_k(T)^(-1/(2k)). }`            (2.3)

Equation (2.3) requires only finiteness of its displayed expectation to be useful; it does not require the stronger inverse-half moment hypothesis used by the full theorem to make that expectation uniformly bounded in terms of `e_k(A^2)`.

This proves `QFORM-GAUSSIAN-CENTER-AGGREGATION-v1`: arbitrary component-center translations—including arbitrarily remote centers and arbitrary dependence of each center on its own scale—cost **exactly zero** when they are averaged before reciprocal scale is paid. This is the precise safe localization ordering for the Gaussian branch.

### k=3 diagonal stress specialization

For `A=I_3`,

`B=D`, `W_3=e_3(D^2)=(T_1 T_2 T_3)^2`.

Independence across coordinate pairs therefore turns (2.3) into

`boxed{ ||p_Q||_infinity <= I_3/(2 pi) prod_{i=1}^3 E T_i^(-1/3). }`     (2.4)

Thus the true residual scale quantity at this endpoint is `T^{-1/3}`, not the sufficient `T^{-1/2}` budget from the full arbitrary-matrix theorem.

## 3. Fractional Besov inequality for arbitrary Gaussian location-scale mixtures

Let

`g(x)=E phi_T(x-M)`,

where `phi_T` is the `N(0,T)` density and `M,T` may be arbitrarily dependent. For every `h`, the exact L1 distance between a Gaussian and its translate is

`||tau_h phi_T-phi_T||_1 = 4 Phi(|h|/(2 sqrt(T)))-2`.

Hence

`||tau_h phi_T-phi_T||_1 <= min(2, sqrt(2/pi)|h| T^(-1/2)).`              (3.1)

For `0<s<1`, `min(2,x)<=2^(1-s)x^s`, so convexity of the L1 norm under mixing gives

`boxed{ ||tau_h g-g||_1 <= C_s |h|^s E T^(-s/2), }`                      (3.2)

where

`C_s=2^(1-s)(2/pi)^(s/2)`.

At the exponent dictated by (2.4), `s=2/3`, this is

`boxed{ ||tau_h g-g||_1 <= (4/pi)^(1/3)|h|^(2/3) E T^(-1/3). }`          (3.3)

No support, moment, center-location, center-separation, or center/scale independence assumption occurs.

## 4. A sharp finite-fragment obstruction at the k=3 fractional scale

For an integer `N>=1`, let

`E_N = union_{j=1}^N [4j,4j+1/N]`, `f_N=1_{E_N}`.                         (4.1)

This is a legal compact finite-fragment cap-one probability density. Put

`h_N=1/(2N)`.

Because the components in (4.1) are separated by much more than `h_N`, each interval overlaps its translate in exactly half its length, so

`boxed{ ||tau_{h_N} f_N-f_N||_1=1. }`                                    (4.2)

Suppose a Gaussian location-scale mixture `g` obeys

`delta=||g-f_N||_1<1/2`.

Translation invariance plus the triangle inequality yields

`1-2 delta <= ||tau_{h_N}g-g||_1`.                                       (4.3)

Combining (3.3)-(4.3), and using

`(4/pi)^(1/3)(2N)^(-2/3)=pi^(-1/3)N^(-2/3)`,

gives the explicit lower bound

`boxed{ E T^(-1/3) >= pi^(1/3) N^(2/3)(1-2 delta). }`                    (4.4)

This is `QFORM-GAUSSIAN-MIXTURE-BESOV-2/3-BARRIER-v1`.

If three independent marginal approximants each have L1 error at most `delta<1/2`, then the right side of the center-aggregated `A=I_3` certificate (2.4) is forced to be at least

`boxed{ (I_3/2) N^2 (1-2 delta)^3 }`,                                    (4.5)

because the three factors of `pi^(1/3)` cancel the denominator `pi` in (2.4). Numerically

`I_3/2 = 1.471234099084729...`.

Thus **center aggregation repairs every translation loss but cannot repair fractional scale inversion**: no L1 approximation of the arbitrary finite-fragment extreme class can both converge to the target law and keep the actual k=3 Gaussian-mixture certificate uniformly bounded. This is a proof-interface obstruction only, not an output-density lower bound and not a QFORM counterexample.

## 5. Required Claude result applied to the same exact-target obstruction

Let `X_1,X_2,X_3` be independent with density `f_N` from (4.1), and take

`Q_N=X_1^2+X_2^2+X_3^2`, `A=I_3`.                                      (5.1)

The spectrum is exactly `{1,1,1}`, so (5.1) lies in the owner's full target. The fixed source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `COUNTEREXAMPLE_SEARCH.md`, proves Theorem A: in dimension three, when all three eigenvalues have modulus at least `sigma`, arbitrary cap-one product laws and affine terms satisfy

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

Applying it to (5.1),

`boxed{ ||p_{Q_N}||_infinity <= 6 sqrt(pi) = 10.6347231054... }`          (5.2)

for every `N`, with no fragment-location or support parameter. Hence the same exact-target family has a fixed whole-law source certificate while any Gaussian-mixture approximation certificate compatible with `delta->0` diverges at least quadratically by (4.5). The missing bridge cannot be a center-averaging trick alone; it must eliminate reciprocal fractional component scale or bypass the Gaussian decomposition.

## 6. Partner application: sharp mass-homogeneous L^{3/2} square receiver

The newest compatible designated partner account03/B14 (`20260923T183544Z`) proves a rough-hub compiler whose core has a uniform `L^3` density and closes the endpoint with a disjoint translated square. Its receiver estimate was

`||p_{aW^2+bW+c}||_(3/2) <= 5^(2/3)|a|^(-1/3)`

for a cap-one probability density. The following exact finite-mass refinement improves the constant and records the localization homogeneity.

### Lemma `QFORM-SQUARE-L32-SUBPROBABILITY-SHARP-v1`

Let `0<=f<=1` have mass `m<=1`, and let

`S=aW^2+bW+c`, `a!=0`,

where `W` carries the positive submeasure with density `f`. Then the pushforward submeasure has an `L^{3/2}` density and

`boxed{ ||p_S||_(3/2) <= 2 |a|^(-1/3) m^(1/3). }`                         (6.1)

The constant 2 is sharp.

### Proof

Complete the square and absorb the resulting translations into input/output coordinates. It suffices to treat `Z=U^2`, where the translated subdensity is still cap one and has mass `m`. For `r>0` set

`F(r)=f_U(r)+f_U(-r)`.

Then `0<=F<=2`, `int_0^infinity F(r)dr=m`, and

`p_Z(r^2)=F(r)/(2r)`.

Therefore

`int p_Z(z)^(3/2) dz = 2^(-1/2) int_0^infinity F(r)^(3/2) r^(-1/2) dr`.

Since `F^(3/2)<=sqrt(2)F`, the right side is at most

`int_0^infinity F(r) r^(-1/2) dr`.                                       (6.2)

Put `R=m/2` and `G=2 1_(0,R)`. The weight `w(r)=r^(-1/2)` decreases. Because `F-2<=0` on `(0,R)` and `F>=0` on `(R,infinity)`,

`int (F-G)w
 <= w(R)[ int_0^R(F-2)dr + int_R^infinity F dr ]
 = w(R)(m-2R)=0`.

Thus (6.2) is at most

`int_0^R 2 r^(-1/2)dr = 2 sqrt(2m)`.

Taking the `2/3` power gives `||p_Z||_(3/2)<=2m^(1/3)`, and scaling the output by `a` gives (6.1). Equality is attained by a unit-height symmetric interval subdensity of mass `m`, so the constant is sharp. QED.

### Consequences for the partner compiler

If the rough-hub core has `||p_T||_3<=K`, then Young gives the subprobability output bound

`||p_{T+S}||_infinity <= 2K |a|^(-1/3)m^(1/3)`.                           (6.3)

For a probability receiver (`m=1`), this replaces the partner factor `5^(2/3)` by `2`. In the partner's equation-level application, where

`K = 9^(2/3) 2^(8/9)|h|^(-4/9)|gamma|^(-2/9)`,

the improved completed inequality is

`boxed{ ||p_Q||_infinity <= 9^(2/3)2^(17/9)
        |a|^(-1/3)|h|^(-4/9)|gamma|^(-2/9). }`                            (6.4)

For its exact-target stress family (`a=h=1`, `gamma=1/2`),

`boxed{ ||p_Q||_infinity <= 9^(2/3)2^(19/9)
        =18.69258833188512... }`                                          (6.5)

instead of `27.32872992777147...`. The partner's convolution continuity argument remains unchanged.

The same lemma gives a complementary localization warning: if the **active square receiver itself** is split into equal positive pieces and (6.3) is paid separately, the mass factor sums as

`sum_{j=1}^N (1/N)^(1/3)=N^(2/3)`.

Thus outside-coordinate localization is zero-tax when the square is kept whole, but square-fragment-first payment has the same `2/3` fractional homogeneity seen in the Gaussian scale obstruction. This is again a proof-order obstruction, not a lower bound on the actual output density.

## 7. Structural interpretation

Two translation/localization facts are now cleanly separated.

First, **translation labels are free before reciprocal payment**: for the Gaussian theorem, center labels can be averaged exactly before `W_k(T)^(-1/(2k))`; for the rough-hub/square branch, arbitrary affine translations of the square are invisible to the `L^{3/2}` norm.

Second, **fractional active-scale payment is not mass homogeneous**: the k=3 Gaussian endpoint naturally exposes a `T^{-1/3}` scale, and arbitrary fragmented cap-one laws force this moment to grow as `N^(2/3)` in every good Gaussian approximation; the active square submeasure similarly carries only `m^(1/3)` before summation.

Accordingly, the safe proof order is

`whole active marginal / aggregate translation labels -> whole-law Fourier/volume/core certificate -> reciprocal curvature/scale -> outside conditioning or convex mixing`.

The unsafe order remains

`active fragments -> normalize or narrow each fragment -> pay reciprocal scale/curvature -> sum`.

## 8. Remaining connection to full QFORM

Full QFORM is OPEN / NOT PROVED / NOT DISPROVED. The present work removes random centers as the obstruction in the Gaussian branch and identifies the exact fractional regularity that still fails on rough extreme laws. It also strengthens the newest partner's structured rough-hub branch but does not force a disjoint square from `s_3(A)>=1`.

The next useful implication is `QFORM-FINAL-CAP-BEFORE-FRACTIONAL-SCALE-v1`: derive an aggregate positive-copy/Fourier/physical-space inequality in which the final marginal cap replaces `E T^{-1/3}` (or in which reciprocal scale appears only after a whole-active cancellation), or force one of the already-completed whole-law exits in every remaining no-pivot/N3 state.

## 9. Sources and correction discipline

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. Required fixed source consumed at exact ref `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`; completed Theorem A was applied at (5.2). Full Gaussian source consumed: `NEW_GAUSSIAN_MIXTURE_FULL_THEOREM.md` at `9dabaf2aaf66687c2b4437fdb359b1aeb4a804bc`. Newest compatible partner consumed: account03/B14 `20260923T183544Z`, canonical math `78e87f9d9fe723b40aa38e71426458283366f8a5`.

No bounded support, bounded diameter, fixed fragment count, log-concavity, moments, diagonal-basis assumption for the full target, post-rotation independence, or continuity premise is introduced. The fixed-source theorem is used only on its valid three-dimensional principal/full-matrix scope. Repository retrieval is source transport, not native receiver-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.