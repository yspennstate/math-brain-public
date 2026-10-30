SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B14, 2026-09-23T13:59:12Z.
attacking: active-fragment critical-budget localization — quantify exactly what is lost when a single whole smoothing marginal is partitioned and normalized before the partner critical-Fourier/pair compiler, while retaining arbitrary translations and no support/moment assumptions in the general localization statement.

# fleet02/B14 r37 — exact active-interval partition tax for the square-root critical budget

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T135912Z-fleet02-B14-QFORM-r37`  
Status: `NEW EXACT PROOF-INTERFACE OBSTRUCTION + LOCALIZATION IDENTITY / FULL QFORM OPEN / CONTINUITY OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and immutable premises

The target remains the full one: for every finite `n`, independent real coordinates with probability densities at most one, and every real symmetric `A` having at least three eigenvalues of modulus at least one, prove a universal essential density bound for `X^T A X`, or give a valid counterexample. No support, moment, centering, identical-law, log-concavity, diagonal-coordinate, or post-rotation independence assumption is added.

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The live corrections still exclude law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint rank-three coarea, worst normalized spectral-fiber caps, bounded-diameter localization, and fixed-fragment-count localization.

Two immutable premises are used.

1. This slot's preceding r36 report, `yspennstate/math-open-problems@d2180eded43f3c299ecff739c67109d342c032b7`, proves `QFORM-FULL-SMALLBALL-EXTREME-LOCALIZATION-v1`: the exact full small-ball supremum is unchanged when every marginal is restricted to indicators of arbitrary compact finite unions of intervals of total length one. This is a law-level reduction and imposes no fixed fragment count or diameter.

2. The designated partner fleet03/B14 r35, canonical `yspennstate/math-open-problems@29096949260b7ec2e9659c1379bd0a0882a37387`, proves `QFORM-SQRT-CRITICAL-BUDGET-MIXTURE-v1`. For a fixed original-coordinate invertible indefinite physical pair with `D=|det B|`, `kappa=s_min(B)`, define

`F_(D,kappa)(K)=inf_(y>0)[4 sqrt(K/(kappa y))+D^(-1/2) Omega(y)]`,

where `Omega(y)=c_E y(2+log(1/y))` for `0<y<=1`, `Omega(y)=log y+2c_E` for `y>=1`, and `c_E=1/[2 sin^2(1/2)]`. If positive unnormalized remainder pieces `nu_j` have masses `m_j` and satisfy

`|hat nu_j(t)| <= min(m_j,k_j/|t|)`,

then the effective square-root budget is

`B=sum_j sqrt(m_j k_j)`

and the resulting output density is bounded by `F_(D,kappa)(B^2)`. If `k_j<=K0 m_j`, the fragmentation is zero-tax.

The required Claude directory was freshly read at the current compatible master version of `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. Section 5 below applies its proved Theorem A to the same target-valid stress form.

## 2. First unpaid implication, stated early

`QFORM-ONE-SHOT-EXTREME-LOCALIZATION-THEN-WHOLE-CERTIFICATE-v1`:

> Exact extreme-product localization may be used once at the law level with zero change in the optimal QFORM small-ball constant. But after an extreme law is selected, a certificate-active marginal must remain whole until a whole-active volume/ridge/hub/bank/Schur-slope/fractional-trace certificate is paid. Recursive normalization of its interval components is valid only when the analytic certificate has a genuinely mass-homogeneous unnormalized constant.

The calculation below shows this condition fails already when the active law is the single interval `Unif[0,1]`: an artificial `N`-cell partition changes no probability law at all, yet it makes the partner r35 critical budget grow by exactly `sqrt(N)` and its optimized certificate diverge.

## 3. Exact partition identity for a translated active interval

Fix `z!=0`. Let `V` have density `1_[a,a+1]`, and partition `[a,a+1]` into finitely many intervals `I_j` of lengths `ell_j>0`, `sum_j ell_j=1`. Let `nu_j` be the unnormalized restriction `1_(I_j)(v) dv`, of mass

`m_j=ell_j`.

Push `nu_j` forward by `v -> 2 z v`. A direct integral gives, for some phase `theta_j(t)`,

`hat nu_j^z(t)=exp(i theta_j(t)) sin(z ell_j t)/(z t)`.

Therefore the smallest coefficient in an unnormalized critical tail is exactly

`k_j^*(z):=sup_(t!=0) |t| |hat nu_j^z(t)| = 1/|z|`.              (3.1)

It is independent of the fragment length and location. After normalizing the piece, the exact critical constant is

`K_j^*(z)=k_j^*(z)/m_j = 1/(|z| ell_j)`.                         (3.2)

Consequently the partner r35 budget of this partition is exactly

`boxed: B_P(z)=|z|^(-1/2) sum_j sqrt(ell_j).`                     (3.3)

For the one-piece decomposition, `B_whole(z)=|z|^(-1/2)`. For `N` equal cells, `ell_j=1/N`,

`boxed: B_N(z)=sqrt(N/|z|).`                                     (3.4)

Thus the Hellinger-type budget pays an exact factor `sqrt(N)` for equal active refinement.

This also pinpoints why the zero-tax condition from partner r35 does not apply. Here

`k_j^*(z)/m_j = 1/(|z| ell_j)`,

so any inequality `k_j<=K0 m_j` needs `K0 >= 1/(|z| min_j ell_j)`. There is no fragment-uniform `K0` under arbitrarily fine active subdivision.

The result is translation invariant: `a` enters only through the unimodular phase. No moment or support-radius parameter occurs.

### Cancellation lost by fragment-first absolute values

If the pieces are recombined before taking an absolute Fourier majorant, their transforms telescope back to the whole interval transform:

`sum_j hat nu_j^z(t) = exp(i theta(t)) sin(z t)/(z t)`,

whose exact whole critical coefficient is again only `1/|z|`. In contrast, every individual unnormalized piece separately has the same coefficient `1/|z|`. Thus the active-fragment loss is not caused by a worse underlying law; it is caused by discarding inter-fragment Fourier phase cancellation before the physical-pair optimization.

This distinction matters because r36's extreme localization is a positive law-level supremum identity. It does not assert that absolute-value Fourier certificates commute with arbitrary refinements of an active extreme marginal.

## 4. A fixed exact-target law whose fragment-first certificate diverges

Take independent cap-one variables `X_1,X_2,Z,V`, with

`Z ~ Uniform[1,2]`, `V ~ Uniform[0,1]`,

and let `X_1,X_2` be any independent cap-one probability laws. Consider

`Q = 2 X_1 X_2 + 2 Z V`.                                        (4.1)

Its homogeneous matrix is the direct sum of two hyperbolic blocks `[[0,1],[1,0]]`, hence has spectrum

`{1,-1,1,-1}`.                                                   (4.2)

So (4.1) lies inside the owner's exact QFORM class.

Use `(X_1,X_2)` as the physical pair. Then `D=kappa=1`. Conditioning on the original coordinate `Z=z`, the whole remainder `2zV` is uniform on an interval of length `2z`, with exact critical constant

`K_whole(z)=1/z`.                                                 (4.3)

The whole-law square-root budget is therefore

`b_1 = int_1^2 z^(-1/2) dz = 2(sqrt(2)-1)`,                      (4.4)

and its effective parameter is

`K_eff,1=b_1^2=12-8sqrt(2)=0.6862915010...`.                     (4.5)

For example, simply evaluating the r35 envelope at `y=1` already gives the finite numerical whole-law certificate

`F_(1,1)(K_eff,1) <= 4 b_1 + 2 c_E = 7.6643937984...`.           (4.6)

Now do nothing to the probability law except partition `[0,1]` into `N` equal cells and apply the r35 positive-piece compiler only after normalizing those cells. From (3.4), for each fixed `z`,

`B_N(z)=sqrt(N/z)`.

Using the discrete fragment index together with the outside variable `z` as the mixture parameter gives

`b_N = sqrt(N) b_1`,                                             (4.7)

hence

`boxed: K_eff,N = b_N^2 = (12-8sqrt(2)) N.`                      (4.8)

The underlying joint law of `(X_1,X_2,Z,V)` and the law of `Q` are literally independent of `N`; only the proof decomposition changed.

### The optimized black-box certificate still diverges

For `D=kappa=1`, write `F(K)=F_(1,1)(K)`. For every `K>=1`, split the infimum at `y=sqrt(K)`.

- If `y<=sqrt(K)`, then `4 sqrt(K/y) >= 4 K^(1/4)`.
- If `y>=sqrt(K)`, then `y>=1` and `Omega(y)=log y+2c_E >= (1/2)log K+2c_E`.

Therefore

`boxed: F(K) >= min{4 K^(1/4), (1/2)log K+2c_E}.`                (4.9)

Both terms tend to infinity. Applying (4.9) to (4.8) proves

`F(K_eff,N) -> infinity`.                                        (4.10)

Moreover choosing `y=4K` for large `K` gives

`F(K) <= 2 + log(4K) + 2c_E`,                                   (4.11)

so the forced fragment-first optimized certificate grows logarithmically up to absolute factors for large `N`.

This proves `QFORM-ACTIVE-INTERVAL-PARTITION-SQRT-BUDGET-BARRIER-v1`:

> Even on one fixed cap-one product law with a single connected active interval, positive active fragmentation followed by normalized critical-Fourier payment is not a universal proof interface. The r35 square-root mixture improvement reduces the raw `N` loss to `sqrt(N)` before pair optimization and then to a logarithmic density-certificate loss, but it cannot make that loss disappear.

There is no contradiction with partner r35: its theorem gives a valid upper bound for any chosen decomposition; the one-piece decomposition is good. The obstruction is to a proof strategy that first forces arbitrarily fine active decomposition and then only retains the separate absolute tail constants.

## 5. Required Claude result applied to the same obstruction

The freshly read `COUNTEREXAMPLE_SEARCH.md` proves Theorem A: if all eigenvalues of an `n`-dimensional quadratic part have modulus at least `sigma`, with arbitrary linear terms, then

`||p_Q||_infinity <= (n/sigma) [d/(d-1)] kappa_d^(1/d)`, `d=n-1`.

For (4.1), `n=4`, `sigma=1`, `d=3`. Therefore

`boxed: ||p_Q||_infinity <= 6 kappa_3^(1/3).`                    (5.1)

This is independent of `N` and in fact applies to every admissible product law for the same matrix. Thus the true exact-target output stays uniformly bounded while the normalized-fragment r35 certificate in (4.10) diverges. Equation (5.1) is the required completed Claude result applied to a real obstruction.

The other freshly read Claude reports remain compatible with the same conclusion. In particular, the D5 whole-cross-volume theorem is law-uniform and therefore survives r36's exact law-level localization without a fragment tax; the dangerous operation is not localization of the supremum itself but paying a non-mass-homogeneous absolute certificate after refining a certificate-active factor.

## 6. Consequence for localization/mixture order

Combining r36, r35, and Sections 3-5 yields a precise order-of-operations rule.

Safe:

`exact law-level extreme localization -> keep certificate-active extreme marginals whole -> pay a whole-active D'/D5/ridge/mixed-hub/grouped-bank/Schur-slope/fractional-trace certificate -> condition/localize genuinely outside original coordinates`.

Unsafe in general:

`exact law-level extreme localization -> recursively split an active interval into tiny cells -> normalize each cell -> replace its transform by an absolute critical constant -> pay the reciprocal/Fourier certificate -> sum`.

The failure already occurs without remote fragments, large translations, unbounded supports, or moments. Hence adding bounded diameter would not repair the logical issue and is disallowed by the live correction in any case.

A positive fragment compiler remains available exactly when its unnormalized analytic coefficient carries a full mass power (`k_j<=K0 m_j`), or when cancellation/aggregation is retained before the absolute value. The interval identity (3.1)-(3.4) gives a concrete diagnostic for deciding which side a proposed localization lies on.

## 7. Remaining debt

Full QFORM remains open. The first unpaid implication is now:

`QFORM-WHOLE-ACTIVE-CERTIFICATE-BEFORE-REFINEMENT-v1`.

In every surviving no-pivot/N3 state, after any exact law-level extreme reduction, expose before active refinement one of:

- a whole-law D'/D5/volume-stability exit;
- a whole-active ridge/mixed-hub/grouped-bank/Schur-slope exit;
- a product-preserving fractional-trace or positive-copy estimate whose unnormalized subprobability coefficient is mass-homogeneous;
- or a new aggregate phase-sensitive estimate that explicitly keeps cancellation across active fragments until after reciprocal inversion.

The bare three-large-eigenvalue hypothesis has not yet been shown to force one of these branches with universal parameters. Fixed fragment counts, bounded diameter, law-uniform pointwise quadratic-phase decay, and post-rotation independence remain unavailable.

## 8. Integrity

- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.
- New exact identity: equations (3.1)-(3.4).
- New proof-interface obstruction: `QFORM-ACTIVE-INTERVAL-PARTITION-SQRT-BUDGET-BARRIER-v1`, equations (4.7)-(4.10).
- Designated partner fleet03/B14 r35 is used at the actual mixture budget.
- Required Claude Theorem A is used at the target-valid inequality (5.1).
- No support, moment, log-concavity, centering, fixed fragment count, bounded diameter, or post-rotation independence assumption is used.
- Essential boundedness only; continuity remains separate.
- Repository retrieval/publication is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
