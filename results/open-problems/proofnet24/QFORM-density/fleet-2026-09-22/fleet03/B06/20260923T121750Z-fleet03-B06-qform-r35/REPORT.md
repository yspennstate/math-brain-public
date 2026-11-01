SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B06, 2026-09-23T12:17:50Z.
attacking: the shared-bank-square survivor by composing the curved one-sided half-Riesz kernel with a conditionally capped translated square, then applying it to a genuinely coupled near-coloop target family.

# fleet03/B06 r35 — translated-square half-Riesz transducer and coupled near-coloop family

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Curved fiber integration  
Status: **NEW SUPPORTING THEOREM + COUPLED TARGET FAMILY CLOSED / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Fresh state and exact obligation


The live correction state forbids law-uniform pointwise quadratic-phase decay, post-rotation independence, arbitrary-joint rank-three coarea, unrestricted spectral-fiber suprema, positive moments of worst conditional projection caps, and extraction of one uniformly good physical minor. None is used below.

The exact designated partner directory `fleet04/B06` was absent from the current QFORM handoff tree at startup, so no result from that slot is fabricated. A completed fleet04 theorem is nevertheless applied at an actual equation in Section 7.

## 2. Source-valid inputs actually used

### 2.1 fleet02/B16 semi-aligned near-null kernel

`yspennstate/math-open-problems@f13d13f2dd1d240c98505a03afebe80f64d4bf10`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B16/20260923T082859Z-fleet02-B16-QFORM-r11/REPORT.md`.

For

`Y=gamma X+H`, `R=delta Y^2+2kUY`,

with `X` independent of the pair `(H,U)`, it proves the one-sided half-Riesz estimate which, after an independent square, gives

- if `delta beta>=0`: all-line density constant `8 L_V sqrt(L_X L_U/|beta gamma k|)`;
- if `delta=0`: constant `4` instead of `8`.

Its proof retains the original scalar `X` and never demands a conditional density cap for `U|H`.

### 2.2 fleet03/B06 r34 opposite-sign shell

`yspennstate/math-open-problems@cbcf1a98b7e64f0bd053155a36ec557d1985e12a`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B06/20260923T111729Z-fleet03-B06-qform-r34/REPORT.md`.

For `delta beta<0`, on the two-sheet side `t beta<0`, its exact shell-length calculation gives the corresponding half-Riesz constant `4 sqrt(2)`.

### 2.3 Claude ruled one-sheet theorem

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/COUNTEREXAMPLE_SEARCH.md`.

Theorem C states that an exact rank-three product projection with signature `(+, +, -)` and all three spectral moduli at least one satisfies

`p_Q(t)<=pi sqrt(2)` on the one-sheet side `t>=0`.

It uses original-product two-dimensional marginals along ruled hyperboloid lines; it does not assert independence of spectral coordinates.

### 2.4 fleet04/B18 dependent square smoothing

`yspennstate/math-open-problems@441e5c1ae4b8aa71ba1bb68aa07d26d83afafcd3`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T113729Z-fleet04-B18-qform-r1/REPORT.md`.

Its completed theorem says that a base density cap `M` plus a conditionally cap-one translated square gives final cap `2 sqrt(M/|a|)`. Section 7 applies it after the new coupled family has already been paid.

## 3. New general transducer: conditional square over a one-sided half-Riesz base

### Theorem 3.1 — `QFORM-CONDITIONAL-SQUARE-HALF-RIESZ-v1`

Let `F` be a sigma-field. Let `R` and `Psi` be `F`-measurable real random variables. Let `Z` be a real random variable whose conditional law given `F` has a density `h_F` satisfying

`||h_F||_infinity <= L_Z`

almost surely. Let `a!=0` and

`Q=R+a(Z+Psi)^2`.

Then `Q` is absolutely continuous on every side where the following expectation is finite, and for almost every `t`,

`boxed:
 p_Q(t)
 <= L_Z |a|^(-1/2)
    E[ 1_{a(t-R)>0} |t-R|^(-1/2) ].`                              (3.1)

In particular, if the one-sided half-Riesz quantity on the right is uniformly at most `H`, then

`||p_Q||_infinity <= L_Z H/sqrt(|a|)`

on that side.

### Proof

Condition on `F`. Translation by `Psi` preserves the conditional density cap. For fixed `F`, the law of

`S=a(Z+Psi)^2`

has density, on `a s>0`,

`g_F(s)
 = [h_F(-Psi+sqrt(s/a))+h_F(-Psi-sqrt(s/a))]
   /(2 sqrt(|a| |s|))`

with the obvious sign interpretation when `a<0`. Therefore

`g_F(s)<=L_Z/(sqrt(|a|)|s|^(1/2)) 1_{a s>0}`.

Since `R` is `F`-measurable, disintegration gives exactly (3.1). No independence between the numerical base value `R` and the translated square is required. QED.

### Why this is not the completed fleet04/B18 theorem

The B18 theorem starts from `||p_R||_infinity<=M`. The present transducer instead starts from a one-sided half-Riesz estimate. This matters for the rank-two hyperbolic base `R=2UY`, whose density can have a logarithmic singularity even though its half-Riesz potential is uniformly bounded. Thus (3.1) handles coupled translated squares in a regime where density-to-square smoothing cannot even start.

## 4. Immediate extension of the scalar/dependent-pair kernel

### Corollary 4.1 — `QFORM-SEMI-ALIGNED-TRANSLATED-SQUARE-v1`

Let `(H,U)` be an arbitrary real pair. Let `X` be independent of `(H,U)`, with

`||p_X||inf<=L_X`, `||p_U||inf<=L_U`.

Put

`Y=gamma X+H`,
`R=delta Y^2+2kUY`,

where `gamma k!=0`. Let `Z`, conditional on `F=sigma(X,H,U)`, have a density capped by `L_Z`, and let `Psi=Psi(X,H,U)` be arbitrary measurable. For `beta!=0`, set

`Q=R+beta[Z+Psi]^2`.

Then:

1. if `delta beta>=0`,

`boxed: ||p_Q||inf <= 8 L_Z sqrt(L_X L_U/|beta gamma k|);`          (4.1)

2. at the exact-null endpoint `delta=0`,

`boxed: ||p_Q||inf <= 4 L_Z sqrt(L_X L_U/|beta gamma k|);`          (4.2)

3. if `delta beta<0`, then on the two-sheet side `t beta<0`,

`boxed: p_Q(t) <= 4 sqrt(2) L_Z sqrt(L_X L_U/|beta gamma k|).`       (4.3)

### Proof

The source proofs in Sections 2.1 and 2.2 establish precisely the required one-sided half-Riesz estimates for the base `R`, before the independent square is inserted. Apply Theorem 3.1. The translation `Psi` never changes the conditional scalar density cap. QED.

This is the first point of the run: the smoothing square may now share both the value and the source coordinates of the base through an arbitrary translation. What must remain fresh is only one conditionally capped scalar direction.

## 5. A genuinely coupled target family

Fix even `m`, balanced signs `eps_j in {+1,-1}`, and `c in (0,1)`. Let

`a0=1-c`,
`T=m^(-1/2) sum_j X_j`,
`U=m^(-1/2) sum_j eps_j X_j`,
`V=m^(-1/2) sum_j Z_j`,

where `X_0`, the whole `X_j` bank, and the whole `Z_j` bank are disjoint collections of independent cap-one original coordinates. Put

`Y=sqrt(c) X_0+sqrt(a0)T`.

The coefficient vectors of `Y,U,V` are orthonormal: balanced signs give `<T,U>=0`, while the `V` bank is disjoint.

Let `r=(theta,zeta)`, `rho=sqrt(theta^2+zeta^2)`, and define the coupled square

`S_r=V+theta Y+zeta U`.                                             (5.1)

The final square now shares **both** spectral pair variables `Y` and `U`; it is not an independent convolution factor.

### 5.1 Positive/null pivot family

For `delta>=0`, put `k=sqrt(1+delta)` and

`Q^+_{delta,r}=delta Y^2+2kUY+S_r^2`.                              (5.2)

In the orthonormal spectral frame `(Y,U,V)`, its matrix is

`B^+_{delta,r}=B^+_{delta,0}+Delta_r`,

`B^+_{delta,0}=[[delta,k,0],[k,0,0],[0,0,1]]`,

`Delta_r=[[theta^2,theta zeta,theta],
          [theta zeta,zeta^2,zeta],
          [theta,zeta,0]].`                                       (5.3)

The uncoupled matrix has eigenvalues

`{1+delta,-1,1}`.                                                   (5.4)

Conditionally on the first source bank, `V` retains its marginal density cap. The one-dimensional product-projection estimate gives

`||p_U||inf, ||p_V||inf <=sqrt(2)`.

Corollary 4.1 therefore yields

`||p_{Q^+_{delta,r}}||inf
 <=2^(15/4)[c(1+delta)]^(-1/4)`                                   (5.5)

for every measurable translation, in particular every `theta,zeta`. At `delta=0`,

`||p_{Q^+_{0,r}}||inf<=2^(11/4)c^(-1/4)`.                         (5.6)

### 5.2 Opposite-sign family

For `eta>=0`, put `k=sqrt(1+eta)` and

`Q^-_{eta,r}=-eta Y^2+2kUY+S_r^2`.                               (5.7)

The uncoupled spectral matrix has eigenvalues

`{1,-(1+eta),1}`.                                                  (5.8)

Corollary 4.1 gives on the two-sheet side `t<0`, for `eta>0`,

`p_{Q^-_{eta,r}}(t)
 <=2^(13/4)[c(1+eta)]^(-1/4).`                                   (5.9)

At `eta=0`, (5.6) applies globally.

## 6. Exact spectral repair: the coupled family stays inside QFORM after one harmless scaling

The perturbation in (5.3) has an exact two-dimensional spectrum. Let `rho=||r||`. In the decomposition of the first two coordinates into the direction `r/rho` and its orthogonal complement, `Delta_r` is zero on the latter and equals

`[[rho^2,rho],[rho,0]]`

on `span{r,e_3}`. Hence

`spec(Delta_r)
 ={0, (rho^2+rho sqrt(rho^2+4))/2,
      (rho^2-rho sqrt(rho^2+4))/2}.`                              (6.1)

Thus

`epsilon(rho):=||Delta_r||op
 =(rho^2+rho sqrt(rho^2+4))/2.`                                   (6.2)

A direct calculation gives

`epsilon(rho)<1  iff  rho<1/sqrt(2).`                              (6.3)

For either uncoupled family, the ordered eigenvalues have absolute values at least one. Weyl's eigenvalue inequality therefore gives, whenever `rho<1/sqrt(2)`,

`min_j |lambda_j(B^{+/-}_{.,r})| >=1-epsilon(rho)>0`.              (6.4)

Define the scaled form

`widetilde Q = Q/(1-epsilon(rho)).`                               (6.5)

Because `(Y,U,V)` is an orthonormal physical frame, (6.4) implies that `widetilde Q` has exactly three nonzero eigenvalues and every one has absolute value at least one. It is therefore a genuine instance of the owner's target for every `rho<1/sqrt(2)`.

Scaling only improves the density norm:

`||p_{widetilde Q}||inf
 =(1-epsilon(rho)) ||p_Q||inf
 <=||p_Q||inf.`                                                   (6.6)

Consequently, in the live near-coloop collar `c>63/64`:

### Positive/null family

For every `delta>=0` and every `rho<1/sqrt(2)`,

`boxed: ||p_{widetilde Q^+_{delta,r}}||inf<13.508.`                (6.7)

At `delta=0`,

`boxed: ||p_{widetilde Q^+_{0,r}}||inf<6.754.`                     (6.8)

### Opposite-sign family

For `eta>0`, the scaled matrix has signature `(2,1)`. On `t<0`, (5.9)-(6.6) give

`p(t)<9.552`.                                                       (6.9)

On `t>=0`, Claude Theorem C applies directly to the scaled exact rank-three product projection and gives

`p(t)<=pi sqrt(2)=4.4428829381...`.                               (6.10)

Therefore

`boxed: ||p_{widetilde Q^-_{eta,r}}||inf<9.552}`                  (6.11)

for every `eta>0`, `c>63/64`, and `rho<1/sqrt(2)`. The endpoint `eta=0` is already covered by (6.8).

This is a genuinely coupled near-coloop family: the final square contains both `Y` and `U`, and the base `2UY` may have the rank-two logarithmic singularity. The proof does not require a bounded density for that base. The only fresh reserve is the original disjoint scalar projection `V`, retained conditionally through the square kernel.

## 7. Completed fleet04 theorem applied at an actual equation

The designated fleet04/B06 artifact remained unavailable at the startup source check, so no theorem from that exact slot is claimed. The compatible completed fleet04/B18 theorem is applied as follows.

Let `R` be any scaled coupled target form from (6.7) or (6.11), with a valid density cap `M` (`M=13.508` on the positive family or `M=9.552` on the opposite-sign family). Suppose an additional untouched original scalar `W`, after conditioning on the sources defining `R`, has conditional density cap one and enters through

`Q_*=R+a[W+Phi]^2`, `a!=0`,                                      (7.1)

where `Phi` is allowed to depend on the base sources. Fleet04/B18 gives the actual inequality

`||p_{Q_*}||inf<=2 sqrt(M/|a|).`                                  (7.2)

Hence

- from the positive coupled family,

`||p_{Q_*}||inf<7.351/sqrt(|a|)`;

- from the opposite-sign coupled family,

`||p_{Q_*}||inf<6.181/sqrt(|a|)`.

No independence between the numerical base value and the translated square is assumed.

## 8. What changed and what remains

New theorem:

`QFORM-CONDITIONAL-SQUARE-HALF-RIESZ-v1`.

New source-valid extension:

`QFORM-SEMI-ALIGNED-TRANSLATED-SQUARE-v1`.

New target-valid closed family:

`QFORM-COUPLED-NEAR-COLOOP-SQUARE-v1`, consisting of both nonzero pivot signs, exact null, and every coupling vector `(theta,zeta)` with norm `<1/sqrt(2)` after the explicit scaling (6.5).

This is not the full theorem. The exact next B06 debt is narrower:

`QFORM-NO-FRESH-SCALAR-SHARED-BANK-v1`:

> remove the final genuinely fresh capped scalar reserve. In other words, handle the case in which every scalar direction entering the smoothing square is built entirely from the same original-coordinate bank that also carries the dependent pair. A valid proof must use the product law before any worst conditional density or fiber supremum, and cannot treat a small matrix tail as a uniformly small random perturbation on unbounded inputs.

The full QFORM conjecture remains `OPEN / NOT PROVED / NOT DISPROVED`. Universal continuity also remains open. The new transducer establishes absolute continuity and essential boundedness in its exact scoped branches; the Claude one-sheet branch supplies a bounded density on its side, but no global continuous representative is asserted here.
