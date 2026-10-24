SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B16, 2026-09-22T19:14:43Z.

# account04/B16 — all positive conditional projection-height moments fail

Run `20260922T191443Z-account04-B16-QFORM-r3`.

**Outcome:** `ESSENTIAL_STEP_APPLIED / REFUTED_INTERMEDIATE_MECHANISM / FULL_TARGET_OPEN`.

The full conjecture remains open. This report proves only an obstruction to a broad class of projection-then-coarea proofs; it is not a counterexample to the conjecture. Continuity is not proved. Execution is `WITHOUT_VERIFIED_BRAIN`.

## 1. The family and the partner input

Use the completed account01/B16 construction at scientific commits `35d90f2c7e1f35fd5ead04e6c746a9df2fb46487` and `f4015ac297ee13a2840eb4f3bf49e2db81034537`.

For an integer `m>=2`, let all physical coordinates be independent `Uniform[-1/2,1/2]`. There are one singleton coordinate and two disjoint blocks of size `m`. In each block let `u=m^{-1/2}(1,...,1)`. Put

`E=span{e_0,u_1,u_2}`, `F=E^perp`, `Y=P_E X`, `Z=P_F X`.

The exact-rank-three form

`Q_0=Y_0^2+Y_1^2-Y_2^2`

has nonzero eigenvalues `{1,1,-1}`. For `0<epsilon<1`,

`A_epsilon=e_0e_0^T+u_1u_1^T-u_2u_2^T+epsilon P_F`

is full rank and has exactly three eigenvalues of modulus at least one. Conditioning on `Z` only translates the target level by `epsilon||Z||^2`; the conditional density of `Y` is unchanged.

Account01/B16 computed the one-block fiber length

`L(z)=sqrt(m)(1-R(z))_+`,

where `R` is the coordinate range, and used it at exponent `1/3`. The following theorem evaluates every positive conditional-height moment.

## 2. Exact all-moment theorem

### Theorem — `QFORM-CONDITIONAL-PROJECTION-ALL-POSITIVE-MOMENTS-FALSE-v1`

Let

`M_m(Z)=||rho_{Y|Z}||_infinity`.

Then for every `0<alpha<2`,

`E M_m(Z)^alpha`
`= [ m^{-alpha/2} Gamma(m+1) Gamma(2-alpha) / Gamma(m+1-alpha) ]^2`,

and therefore

`E M_m(Z)^alpha = Gamma(2-alpha)^2 m^alpha (1+o(1)) -> infinity`.

For every `alpha>=2`,

`E M_m(Z)^alpha=+infinity`

already for each fixed `m>=2`.

Thus no positive power moment of the conditional projection density height admits a universal bound—not merely the previously tested exponent `2/3`. This remains true for the full-rank matrices `A_epsilon` above.

### Proof

For one diffuse block the orthogonal change of variables has Jacobian one. If `beta>-1`, the partner's fiber identity gives

`int_{u^perp} L(z)^beta dz = E L(P_{u^perp}X)^{beta-1}`.

The range `R` of `m` iid `Uniform[0,1]` variables has density

`m(m-1) r^{m-2}(1-r)`, `0<r<1`.

Consequently

`int L(z)^beta dz`
`=m^{(beta-1)/2} m(m-1) B(m-1,beta+1)`
`=m^{(beta-1)/2} Gamma(m+1)Gamma(beta+1)/Gamma(m+beta)`.

The two blocks factor. Their joint fiber volume is `H(z_1,z_2)=L(z_1)L(z_2)`. Since the ambient cube density equals one, the marginal density of `Z` is `H`, while the conditional density of `Y|Z=z` is uniform on its fiber and has height `H^{-1}`. Hence

`E M_m(Z)^alpha = int H^{1-alpha}`.

Set `beta=1-alpha`. When `0<alpha<2`, `beta>-1`, and the preceding formula factors twice to give

`E M_m(Z)^alpha`
`=[m^{-alpha/2} Gamma(m+1)Gamma(2-alpha)/Gamma(m+1-alpha)]^2`.

The gamma-ratio asymptotic `Gamma(m+1)/Gamma(m+1-alpha)=m^alpha(1+o(1))` proves the stated growth. When `alpha>=2`, `beta<=-1`; near a collapsing fiber, the range density contributes one power of `1-R`, so the integral is proportional to `int_0 (1-R)^beta d(1-R)` and diverges. QED.

## 3. Concrete implications

At `alpha=2/3` the theorem recovers account01/B16 exactly:

`E M_m^{2/3}`
`=[m^{-1/3}Gamma(m+1)Gamma(4/3)/Gamma(m+1/3)]^2`
`~Gamma(4/3)^2 m^{2/3}`.

At `alpha=1` it sharpens to the especially transparent identity

`E M_m=m`.

At `alpha>=2` the conditional height does not even have a finite moment for a fixed-dimensional member of the family.

Therefore every proof interface of the form

`||p_Q||_infinity <= C Phi(E M_m^alpha)`

with any fixed `alpha>0` and any dimension-independent increasing payment `Phi` cannot prove the target through a universal conditional-height estimate. The failure persists if one first invokes the correct bounded-density theorem for the unconditional three-dimensional projection: that theorem controls `rho_Y`, not the disintegrated heights `rho_{Y|Z}`.

This is an actual application of the completed partner result: its exact fiber formula is extended from `alpha=2/3` to every `alpha>0`, eliminating the whole positive-moment family rather than a single exponent.

## 4. Why this does not refute QFORM

For the exact-rank-three member `Q_0`, account01/B16 already applied a product-preserving disjoint-bank theorem and obtained

`||p_{Q_0}||_infinity <= 27.8162566595...`

uniformly in `m`. Hence the conditional-height moments diverge while the actual nonlinear pushforward remains uniformly bounded. The lost information is the translation and overlap of the conditional profiles together with the original disjoint-bank product structure.

The source-valid next implication is therefore not another conditional sup moment. It is an overlap-sensitive trace estimate that averages the translated conditional quadratic profiles before taking an output supremum, or a product-coordinate decomposition that extracts a disjoint innovation bank before conditioning.

## 5. Status and quantifiers

- Full QFORM conjecture: `OPEN / NOT PROVED / NOT DISPROVED`.
- New all-positive-moment obstruction: proved for cap-one independent cube coordinates, exact rank three, and the full-rank extension with exactly three eigenvalues of modulus at least one.
- No Gaussianity, log-concavity, moment, connected-support, or post-rotation independence assumption is used.
- The result does not claim a density bound for the full-rank `A_epsilon` family; it only shows that the conditional-height route fails there as well.
- Continuity is not proved.
