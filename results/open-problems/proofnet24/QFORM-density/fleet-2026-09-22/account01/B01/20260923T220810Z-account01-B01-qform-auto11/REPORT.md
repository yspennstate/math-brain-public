SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T22:08:10Z.
attacking: the exact/near rank-one W2=0 residual by replacing the false critical half-Riesz shortcut with a source-preserving square-root small-ball estimate and subcritical fractional potentials.

# account01/B01 — rank-one same-bank oscillatory replacement

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T220810Z-account01-B01-qform-auto11`  
Role: Oscillatory replacement  
Status: **NEW SUPPORTING THEOREM + REFUTED CRITICAL INTERFACE / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and correction boundary

The owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No moment, support, iid, Gaussian, log-concavity, connected-support, diagonal-basis, or post-rotation-independence hypothesis is added.

The live correction that scalar bounded density does not imply a law-uniform pointwise quadratic Fresnel decay is preserved. The phase-aligned fragmented-support construction still defeats every proposed bound of the form `|E exp(itX^2)| <= C |t|^{-alpha}` uniformly over cap-one laws. Nothing below uses such a bound.

The latest completed designated partner result used below is account02/B01, canonical mathematics

`yspennstate/math-open-problems@1760a61be07cc456da3f69e703d025e74c3877eb`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T210057Z-account02-B01-QFORM-auto11/REPORT.md`.

It proves, inside exact `W2=0`, that the relevant matrices are diagonal plus rank at most two, this structure survives literal scalar Schur completion, and its high-diagonal survivor reduces either to an already paid branch or to an ORIGINAL-coordinate residual cross block `N` satisfying

`rank N <=2`, `||N||_F^2 >3969/8192`, `s2(N)<1/256`,

and therefore

`s1(N)>sqrt(31751)/256=0.6960472767...`.                         (1.1)

The partner explicitly leaves the rank-one-dominant third-curvature routing unpaid.

## 2. Main theorem: arbitrary same-bank phases, rank-one cross

Let `I,J` be disjoint ORIGINAL-coordinate banks. Let `X_I,X_J` be independent product vectors, each original scalar coordinate having density at most one. Let `u in R^I`, `v in R^J` be nonzero, `sigma !=0`, and let `F:R^I->R`, `G:R^J->R` be arbitrary measurable real functions. Put

`Y=u^T X_I`, `Z=v^T X_J`,

`R=F(X_I)+G(X_J)+2 sigma Y Z`.                                  (2.1)

Write `m_Y=||p_Y||_infinity`, `m_Z=||p_Z||_infinity`. The standard one-dimensional product-projection bound used throughout the current QFORM package gives

`m_Y <=sqrt(2)/||u||_2`, `m_Z <=sqrt(2)/||v||_2`.               (2.2)

Define the scale

`kappa=|sigma| ||u||_2 ||v||_2`.                                (2.3)

### Theorem 2.1 — `QFORM-RANK1-SAMEBANK-SQRT-SMALLBALL-v1`

For every `epsilon>0`,

`boxed:
 sup_s P(|R-s|<=epsilon)
 <= min{1, 8 sqrt(pi m_Y m_Z epsilon/|sigma|)}
 <= min{1, 8 sqrt(2 pi epsilon/kappa)}.}`                        (2.4)

Thus a rank-one crossing retains a universal square-root concentration estimate even with completely arbitrary, possibly nonseparable-within-source, same-bank phases `F` and `G`.

### Proof

For each frequency `t`, push the phase-twisted complex measures

`exp(itF(X_I)) dP_I`, `exp(itG(X_J)) dP_J`

through `Y` and `Z`. Their complex densities `alpha_t,beta_t` obey pointwise

`|alpha_t(y)|<=p_Y(y)`, `|beta_t(z)|<=p_Z(z)`,

hence

`||alpha_t||_2<=sqrt(m_Y)`, `||beta_t||_2<=sqrt(m_Z)`.           (2.5)

The characteristic function is

`phi_R(t)=int int alpha_t(y) beta_t(z) exp(i2 sigma t y z) dy dz`. (2.6)

Let

`(T_t f)(y)=int exp(i2 sigma t y z) f(z) dz`.

With the Fourier convention `hat f(xi)=int exp(i xi z)f(z)dz`, Plancherel gives exactly

`||T_t||_(2->2)=sqrt(pi/(|sigma t|))`.                            (2.7)

Therefore

`|phi_R(t)|
 <=min{1, sqrt(pi m_Ym_Z/(|sigma t|))}.`                         (2.8)

Set

`K=sqrt(pi m_Ym_Z/|sigma|)`.                                    (2.9)

For `T>0`, the Fejer kernel

`K_T(x)=(1/(2pi)) int_{-T}^T (1-|t|/T) exp(itx) dt
       =(1-cos(Tx))/(pi T x^2)`

satisfies `K_T(x)>=T/(4pi)` whenever `|x|<=1/T`, since `1-cos y>=y^2/4` for `|y|<=1`. Thus

`P(|R-s|<=1/T)
 <=(4pi/T) E K_T(R-s)
 <=(4/T) int_0^T |phi_R(t)|dt`.                                 (2.10)

If `T>=K^2`, (2.8) gives

`int_0^T |phi_R(t)|dt
 <=K^2+2K(sqrt(T)-K)
 <=2K sqrt(T)`.                                                   (2.11)

Putting `T=epsilon^{-1}` yields `P<=8K sqrt(epsilon)`. If `T<K^2`, then `8K sqrt(epsilon)>8`, so the trivial bound one is stronger. This proves the first inequality in (2.4); (2.2) gives the second. QED.

This is a distribution-function replacement for the false pointwise scalar Fresnel estimate. It is dimension free, translation uniform, and uses only the independence of the two ORIGINAL source banks.

## 3. Sharper subcritical fractional-potential estimate

The same frequency estimate gives a more precise fractional trace.

### Theorem 3.1 — `QFORM-RANK1-SAMEBANK-SUBCRITICAL-RIESZ-v1`

For every `0<beta<1/2`,

`H_beta(R):=sup_s E|R-s|^{-beta}`

obeys

`boxed:
 H_beta(R)
 <= [ (pi m_Ym_Z/|sigma|)^beta ]
    /[Gamma(beta) cos(pi beta/2) beta(1-2beta)]`                 (3.1)

and hence

`boxed:
 H_beta(R)
 <= C_beta kappa^{-beta},
 C_beta=(2pi)^beta/[Gamma(beta)cos(pi beta/2)beta(1-2beta)].}`   (3.2)

At the useful value `beta=1/4`,

`boxed: H_(1/4)(R) <=3.781277348735447 kappa^{-1/4}.}`           (3.3)

### Proof

For `0<beta<1`, the one-dimensional Riesz identity is

`|x|^{-beta}
 =[Gamma(beta)cos(pi beta/2)]^{-1}
  int_0^infinity t^{beta-1} cos(tx) dt`.                        (3.4)

To avoid any a-priori regularity assumption on `R`, first replace `R` by `R+delta G` with an independent standard Gaussian `G`. Its characteristic function gains the factor `exp(-delta^2t^2/2)`. Applying (3.4) to the smoothed law, taking absolute values, and using (2.8) gives a bound independent of `delta`; Fatou as `delta downarrow0` recovers the original law.

Using `K` from (2.9), split the frequency integral at `t=K^2`:

`int_0^infinity t^{beta-1} min(1,K t^{-1/2}) dt
 =K^{2beta}[1/beta+1/(1/2-beta)]
 =K^{2beta}/[beta(1-2beta)].`                                   (3.5)

Equations (3.4)-(3.5) prove (3.1); (2.2) proves (3.2). QED.

As a direct distribution corollary,

`P(|R-s|<=epsilon) <= epsilon^beta H_beta(R)`                   (3.6)

for every `beta<1/2`. The explicit square-root estimate (2.4) is stronger at the endpoint scale, while (3.1) is the sharper currency for subcritical fractional-potential gluing.

## 4. The critical half-Riesz endpoint is genuinely false

The restriction `beta<1/2` cannot be removed if arbitrary same-bank quadratic curvature is retained.

### Proposition 4.1 — `QFORM-RANK1-SAMEBANK-HALFRIESZ-FALSE-v1`

There are independent cap-one variables and quadratic same-bank phases for which

`sup_s E|R-s|^{-1/2}=infinity`.                                  (4.1)

Take independent `Y,Z ~ Uniform[-1/2,1/2]`, `sigma=1`,

`F(Y)=-Y^2`, `G(Z)=-Z^2`.

Then

`R=-Y^2-Z^2+2YZ=-(Y-Z)^2`.                                      (4.2)

The difference `D=Y-Z` has triangular density `1-|d|` on `[-1,1]`. Therefore

`E|R|^{-1/2}=E|D|^{-1}
 =int_{-1}^1 (1-|d|)/|d| dd=infinity`.                          (4.3)

This example is not a counterexample to the owner target: its two-variable quadratic matrix `[[ -1,1],[1,-1]]` has only one nonzero eigenvalue. It is a rigorous counterexample to the tempting intermediate claim that a rank-one bilinear packet plus arbitrary same-bank quadratic curvature should have a universal half-Riesz bound.

The failure is exactly critical: Theorem 3.1 controls every exponent below one half, and the square-root small-ball exponent in Theorem 2.1 remains valid.

## 5. Actual application to the latest account02/B01 result

Apply Theorems 2.1 and 3.1 to the partner's exact-rank-one residual endpoint. In the partner's ORIGINAL-coordinate cut, if `rank N=1`, write

`N=s_1 u v^T`, `||u||=||v||=1`.

All same-side residual quadratic and affine terms are absorbed into `F(X_I)` and `G(X_J)`, while the cross term is exactly

`2s_1 (u^T X_I)(v^T X_J)`.

By the partner bound (1.1),

`s_1>sqrt(31751)/256=0.6960472767876026...`.                    (5.1)

Therefore the new subcritical theorem gives the concrete inequality

`boxed:
 H_(1/4)(R)
 <3.781277348735447*(sqrt(31751)/256)^(-1/4)
 =4.139795121814236.}`                                          (5.2)

The square-root small-ball theorem simultaneously gives

`boxed:
 sup_s P(|R-s|<=epsilon)
 <min{1,24.0359090403 sqrt(epsilon)}.}`                          (5.3)

This is an actual quantitative use of the newest completed designated-partner result, not a restatement of it.

Equations (5.2)-(5.3) show that the exact rank-one limit of the partner's rank-one-dominant tube has no subcritical concentration blow-up at all. However Proposition 4.1 proves that one cannot simply replace the partner's rank-two half-Riesz estimate by a rank-one half-Riesz estimate. The outer scalar square in the partner route is therefore genuinely critical: a square convolved with a rank-one residual that itself collapses to an opposite-sign square may retain the familiar logarithmic singularity.

## 6. Structural consequence and first unpaid implication

The remaining debt is sharper than “rank-one crossing is bad.” Exact rank one is quantitatively controlled at every subcritical exponent and at square-root small-ball scale. What fails is specifically the **critical half-Riesz interface in the presence of a parabolic same-bank cancellation**.

Thus the next implication should be formulated as

`QFORM-W2ZERO-RANK1-CRITICAL-SIGN-OR-THIRD-RESOURCE-ROUTING-v1`:

> In the partner's diagonal-plus-rank-two, rank-one-dominant survivor, either route the same-bank quadratic curvature away from the parabolic cancellation so that a genuine rank-two/half-Riesz receiver fires, or identify a source-disjoint/grouped third curvature whose sign regularizes the critical square-vs-square logarithm. For a nonzero but tiny second cross singular value, retain the tail exactly and interpolate to an existing rank-two receiver; do not delete the tail on unbounded inputs.

This is precisely where the global `s_3(A)>=1` hypothesis must be spent. Proposition 4.1 shows that rank-one crossing plus the already-present outer square alone is not a universally sufficient analytic interface; a third spectral resource or a nondegenerate two-dimensional packet is necessary.

The newest proof-assembly handoff also reduces a full proof to principal-minimal target matrices with only three or mixed-sign four target-scale eigenvalues; this makes the third-resource routing above compatible with the current global induction rather than requiring control of arbitrarily many >=1 eigenvalues.

## 7. Status

The full QFORM conjecture remains OPEN. The full continuity conclusion remains OPEN. Theorem 2.1 is a rigorous dimension-free small-ball estimate, Theorem 3.1 a rigorous averaged-frequency fractional-potential estimate, and Proposition 4.1 a rigorous counterexample to a critical intermediate interface. None is promoted to a full density theorem.

The phase-aligned density counterexample to law-uniform scalar pointwise Fresnel decay is preserved. No Monte Carlo or histogram is used. No rotations are declared to preserve independence. No small nonzero tail is discarded.
