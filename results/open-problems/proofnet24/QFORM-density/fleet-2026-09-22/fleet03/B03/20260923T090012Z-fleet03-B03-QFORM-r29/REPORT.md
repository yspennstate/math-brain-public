SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T09:00:12Z.
attacking: replace the exact angular-cancellation compiler's outer-pivot loss by a right-bank Fresnel/Hausdorff-Young slice; keep the cancelled physical coordinate as an independent random linear receiver, and obtain a target-scale L2 time integral and linear collision small-ball bound uniform as the outer pivot a -> 0.

# fleet03/B03 r29 — target-scale exact-cancellation L2 time receiver

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Decoupled time integral  
**Status:** `NEW SUPPORTING THEOREM / OUTER-PIVOT LOSS REMOVED AT EXACT CANCELLATION / FULL QFORM OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

The unrestricted owner target remains OPEN, and the unrestricted continuity claim remains OPEN.  This report does not rotate the independent physical coordinates into eigen-coordinates, does not condition on a sum/difference variable, does not use law-uniform pointwise quadratic-phase decay, does not invoke arbitrary-joint coarea, and does not take a worst conditional projection-density supremum.

## 1. Why a new mechanism is needed

The immediate B03 predecessor is

`yspennstate/math-open-problems@b4633364805377102bf4e9da285a695fcb7b55ff`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B03/20260923T062811Z-fleet03-B03-QFORM-auto11/REPORT.md`.

At the exact heavy-row angular cancellation `h_r=0`, that run proved an `L2` density/collision estimate by retaining the original scalar pivot square.  Its normalized estimate still carried an outer-pivot factor `|a|^(-2/3)`, so its own first remaining implication was to remove that loss as `a -> 0` while preserving product provenance.

A later completed curved-fiber source, fleet01/B06 r25,

`yspennstate/math-open-problems@3f8e20afcd53d32515b7c451b1a06c5c54290f4e`,

shows that the current one-sided packet may be organized by the physical right-plane vectors without changing basis in probability space.  Its heavy-set addendum

`yspennstate/math-open-problems@43345308f06f3224ef0c03a181a7a8c1937dfa97`

shows that the plane leverage numbers `ell_j=v_j^2+q_j^2` sum to two, there are at most three heavy rows `ell_j>1/2`, and in the still-unpaid state every heavy row obeys `|h_j|/rho<1/8`.

I also use the completed Fourier/Hausdorff-Young input from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`:
for a cap-one probability density `f` and any unit-modulus coordinatewise phase, if `Psi` is the resulting twisted characteristic function, then for `p>=2`,

`int_R |Psi(s)|^p ds <= 4 pi/sqrt(p)`.                              (1.1)

Finally, the designated fleet04/B03 source is

`yspennstate/math-open-problems@28681f9af7c2307f80968df86010084019599e38`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B03/20260922T193150Z-fleet04-B03-collision-l2-r1/REPORT.md`.

Its advertised weighted-L2 compiler is not used because the later B03 correction found a missing time weight and wrong coefficient homogeneity.  I use only its valid elementary collision lemma

`P(|Y-Y'|<=eps) <= 2 eps ||p_Y||_2^2`.                             (1.2)

## 2. A one-dimensional shifted product-Fourier lemma

Let `Y_1,...,Y_m` be independent cap-one variables.  For a fixed final time frequency, permit arbitrary coordinatewise phases and write the corresponding twisted characteristic functions as `Psi_j`.  Let `h=(h_1,...,h_m)!=0`, and assume

`max_j h_j^2/||h||_2^2 <= 1/2`.                                    (2.1)

Then for every collection of real shifts `c_j`,

`boxed:
 int_R prod_j |Psi_j(s h_j+c_j)| ds <= 4 pi/||h||_2.
}`                                                                   (2.2)

### Proof

Put `ell_j=h_j^2/||h||_2^2`; zero coefficients are harmless.  Then `sum ell_j=1` and `ell_j<=1/2`.  After the change `z=||h||_2 s`, Holder with exponents `1/ell_j` gives

`int prod_j |Psi_j(sign(h_j)sqrt(ell_j) z+c_j)| dz`
`<= prod_j [ell_j^(-1/2)
             int |Psi_j(r+c_j)|^(1/ell_j) dr]^(ell_j).`            (2.3)

Since `1/ell_j>=2`, (1.1) implies

`ell_j^(-1/2) int |Psi_j|^(1/ell_j)
 <= ell_j^(-1/2) 4pi sqrt(ell_j)=4pi`.                              (2.4)

Because `sum ell_j=1`, the product is `4pi`.  Restoring the Jacobian proves (2.2).  The estimate is translation-uniform in every `c_j`.

## 3. Main analytic theorem: cancelled physical row plus diffuse square bank

### Theorem 3.1 — `QFORM-CANCELLED-ROW-RIGHTBANK-L2-v1`

Let

- `X` be a real cap-one variable;
- `Y=(Y_1,...,Y_m)` be an independent cap-one product bank;
- `Omega` be independent of `(X,Y)`;
- `U=U(Omega)` have density bounded by `L`;
- `S(Omega),F(Omega)` be arbitrary measurable functions;
- `h,g in R^m`, `h!=0`, satisfy (2.1);
- `A,d,g_0` be nonzero real constants.

Allow arbitrary coordinatewise phases `phi_j(Y_j)` and define

`T=A(h.Y+S(Omega))^2
  +2d U(Omega)[g_0 X+g.Y]
  +F(Omega)+sum_j phi_j(Y_j).`                                     (3.1)

Then, with

`K = 2 pi sqrt(L)/[ ||h||_2 sqrt(|A d g_0|) ],`                    (3.2)

the characteristic function obeys

`boxed: |phi_T(t)| <= min(1,K/|t|).`                               (3.3)

Consequently

`boxed: int_R |phi_T(t)|^2 dt <= 4K,`                              (3.4)

`boxed: ||p_T||_2^2 <= 2K/pi
       =4 sqrt(L)/[||h||_2 sqrt(|A d g_0|)],`                       (3.5)

and

`boxed:
 int_R |t|^(-1/2)|phi_T(t)|^2 dt <= (16/3) sqrt(K).
}`                                                                   (3.6)

In particular, for an independent copy `T'`, the designated partner lemma gives the linear collision estimate

`boxed:
 P(|T-T'|<=eps)
 <= 8 sqrt(L)/[||h||_2 sqrt(|A d g_0|)] eps.
}`                                                                   (3.7)

### Proof

For `t!=0`, apply the source damped Fresnel linearization to the square in (3.1), remove the damping by dominated convergence exactly as in the source package, and take absolute values only after retaining the complete original product bank.  With `chi_X(r)=E exp(irX)` and the twisted `Psi_j` from Section 2,

`|phi_T(t)|
 <=(4pi |tA|)^(-1/2)
   int_R E_Omega[
      |chi_X(2tdg_0 t U)|
      prod_j |Psi_j(s h_j+2tdt U g_j)|] ds.`                        (3.8)

The crucial exact-cancellation feature is that `X` does **not** occur in the square.  Therefore the factor `chi_X(2tdg_0 t U)` is independent of the Fresnel variable `s` and can stay outside the one-dimensional product integral.  Applying (2.2) for each fixed value of `U`,

`|phi_T(t)|
 <= [2sqrt(pi)/(sqrt(|A|)||h||_2)] |t|^(-1/2)
    E |chi_X(2tdg_0 t U)|.`                                        (3.9)

Now use the true marginal density cap of `U`; no conditional density is introduced.  Plancherel and `f_X<=1` give

`int_R |chi_X(r)|^2 dr
 =2pi int f_X(x)^2 dx <=2pi`.                                      (3.10)

Hence Cauchy-Schwarz yields, for every `t!=0`,

`E |chi_X(2tdg_0 t U)|`
`<= [ L/(2|tdg_0|) int |chi_X(r)|^2 dr ]^(1/2)`
`<= [ pi L/(|tdg_0|) ]^(1/2).`                                     (3.11)

Combining (3.9)-(3.11) gives `|phi_T(t)|<=K/|t|`; adjoining the trivial `|phi_T|<=1` proves (3.3).

The exact integrals are

`int_R min(1,K^2/t^2) dt=4K`,                                      (3.12)

and

`int_R |t|^(-1/2)min(1,K^2/t^2)dt=(16/3)sqrt(K)`.                  (3.13)

Thus (3.4) and (3.6) follow.  Since the Fourier transform of the probability law is in `L2`, Plancherel/uniqueness gives an `L2` density and (3.5).  Applying (1.2) gives (3.7).  QED.

### Independent-copy interpretation

Equation (3.4) is literally the complete-copy collision time integral because

`|phi_T(t)|^2=E exp(it(T-T'))`.                                     (3.14)

The proof never writes a duplicated physical coordinate as an independent sum and difference.  All dependence inside `(X-X',X+X')` or `(Y_j-Y_j',Y_j+Y_j')` remains untouched.

## 4. Exact application to the heavy-row angular cancellation

Return to the exact-rank-three one-sided packet

`Q=a^(-1)H^2+2sigma U V`,                                          (4.1)

with

`H=aX_i+h_L.X_L+h_R.X_R+h_K.X_K`,
`U=u.X_L`, `V=v.X_R`,                                               (4.2)

and

`h_R=beta v+m q`, `q perpendicular v`, `||q||=||v||=1`,
`m=rho y`, `y^2>1/2`, `rho^2=a^2+||k||^2`.                         (4.3)

The source spectral inequality is

`(rho^2/|a|)|sigma| >= s_3(A)^2`.                                  (4.4)

Put

`theta^2=beta^2+m^2`,
`g=m v-beta q`.                                                      (4.5)

Then

`h_R perpendicular g`, `||h_R||=||g||=theta`,
`v=(beta h_R+m g)/theta^2`.                                        (4.6)

Completing only the `U h_R.X_R` term gives the exact product-preserving identity

`Q=(1/a)[h_R.X_R+Xi(Omega)]^2
  +2 d U (g.X_R)+F(Omega),`                                        (4.7)

where

`d=sigma m/theta^2`,                                                (4.8)

`Omega` contains only original coordinates outside the right bank,

`Xi= aX_i+h_L.X_L+h_K.X_K
    +a sigma beta U/theta^2`,                                      (4.9)

and

`F= -2sigma beta U[aX_i+h_L.X_L+h_K.X_K]/theta^2
    -a sigma^2 beta^2 U^2/theta^4`.                               (4.10)

No random term is discarded.

Let `r` be a heavy right-plane row,

`ell_r=v_r^2+q_r^2>1/2`,                                           (4.11)

and impose the exact angular cancellation

`h_r=beta v_r+m q_r=0`.                                            (4.12)

Then from the orthogonal change `(v,q)->(h_R/theta,g/theta)`,

`|g_r|=theta sqrt(ell_r)`.                                         (4.13)

Remove coordinate `r` from the square bank.  Because `h_r=0`, its remaining square vector still has norm `theta`.

We now verify the diffuseness gate (2.1) in the genuinely still-unpaid state.  Let `H={j:ell_j>1/2}`.  The completed r25 heavy-set consequence says that if the branch has not already been paid by a noncancelled heavy-row theorem, then every `j in H` satisfies

`|h_j|<rho/8`.                                                       (4.14)

Since `theta^2>=m^2=rho^2 y^2>rho^2/2`, every such heavy row satisfies

`h_j^2/theta^2<1/32`.                                               (4.15)

For every nonheavy row, simply

`h_j^2/theta^2<=ell_j<=1/2`.                                       (4.16)

Thus after removing `r`, all coefficients satisfy (2.1).  Theorem 3.1 applies to (4.7) with

`A=1/a`, `g_0=g_r`, `||h||=theta`, `d=sigma m/theta^2`.            (4.17)

The completed scalar product-projection theorem gives

`L=||p_U||_infinity<=sqrt(e)`.                                     (4.18)

Therefore

`K
 <=2pi e^(1/4)
   sqrt[ |a|/(|sigma| m theta sqrt(ell_r)) ].`                      (4.19)

Now use `m=rho y`, `theta>=rho y`, (4.4), `y^2>1/2`, and `ell_r>1/2`:

`|sigma|m theta sqrt(ell_r)/|a|
 >=s_3(A)^2 y^2 sqrt(ell_r).`                                      (4.20)

Hence

`boxed:
 K < 2^(7/4) pi e^(1/4)/s_3(A)
   =13.568317125581782.../s_3(A).
}`                                                                   (4.21)

This is the key improvement over the predecessor: **the outer-pivot `a` has disappeared completely.**

Consequently

`boxed:
 int_R |phi_Q(t)|^2 dt
 < 2^(15/4) pi e^(1/4)/s_3(A)
 =54.27326850232713.../s_3(A),
}`                                                                   (4.22)

and

`boxed:
 ||p_Q||_2^2
 <2^(11/4)e^(1/4)/s_3(A)
 =8.637858959899031.../s_3(A).
}`                                                                   (4.23)

The weighted independent-copy time integral is also target-scale:

`boxed:
 int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <(16/3)sqrt[2^(7/4)pi e^(1/4)] s_3(A)^(-1/2)
 =19.64543821560657... s_3(A)^(-1/2).
}`                                                                   (4.24)

## 5. Designated partner applied to an actual target-scale inequality

Apply the valid fleet04/B03 collision lemma (1.2) to (4.23).  For an independent copy `Q'`,

`boxed:
 P(|Q-Q'|<=eps)
 <2^(15/4)e^(1/4) s_3(A)^(-1) eps
 =17.27571791979806... s_3(A)^(-1) eps.
}`                                                                   (5.1)

Under the owner normalization `s_3(A)>=1`, this is a universal linear collision small-ball bound with coefficient `<17.276`, uniform all the way through the previously problematic limit `a->0`.

This is not merely a restatement of the previous exact-cancellation result: the previous normalized collision certificate retained `|a|^(-2/3)`.  Here the whole remaining right-bank square direction is aggregated by the shifted product-Fourier inequality before the cancelled physical row is spent in `L2`, and that aggregation exactly restores target homogeneity.

## 6. What this does and does not close

The exact angular-cancellation endpoint now has a **target-scale** dependence-safe `L2` density certificate, a target-scale half-Riesz independent-copy integral, and a target-scale linear collision small-ball estimate.  In particular, the collision/time-integral obstruction identified in the previous B03 report is no longer singular as the original outer pivot tends to zero.

This still does **not** prove the owner's one-copy `L^infinity` target.  The envelope `min(1,K/|t|)` is the exact logarithmic endpoint for absolute Fourier inversion: it is square-integrable but not integrable.  Thus continuity is not proved here either.

The sharper first unpaid implication for B03 is now:

`QFORM-TARGETSCALE-L2-TO-LINF-NEARCOLOOP-v1` — combine the target-scale endpoint (4.22)-(4.24) with the strict-margin hub-density-augmented Brascamp-Lieb theorem and the exact-coloop real-space closure, in a way that stays uniformly bounded across the strict near-coloop collar without deleting the small transverse direction or taking a conditional projection supremum.

The full arbitrary-dimensional QFORM conjecture remains OPEN.  No target counterexample is produced.
