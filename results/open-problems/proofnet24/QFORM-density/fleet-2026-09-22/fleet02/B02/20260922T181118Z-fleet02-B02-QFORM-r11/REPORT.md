SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B02, 2026-09-22T18:11:18Z.
attacking: translation-uniform indefinite-pair Lp synthesis with a Schur-residual density resource.

# QFORM-PAIR-LP-TRANSLATION-SYNTHESIS-v1

Programme: `QFORM-DENSITY-3EIG-20260922`  
Owner control read this run: revision `2026-09-22.11` (later than the assignment card's activation revision).  
Status: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN**.  
Secondary classification: **CANDIDATE_REFUTED** for the structural rule “dimension-free aggregate pivot-pair determinant mass forces one uniformly conditioned physical pair.”

## 1. Exact target and corrections consumed

The target is: for independent real inputs with densities bounded by one and real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal essential-density bound for `Q=X^T A X`, or give a valid counterexample.

This report does not claim the full theorem. It does not use the refuted law-uniform pointwise Fresnel estimate, post-rotation independence, a conditional projected-density cap, the arbitrary-joint 3-D coarea claim, or the refuted positive conditional-moment gate. The fresh proof-first correction `20260922T180015Z-pair-log` was consumed before this derivation. Its source-valid physical-pair logarithmic envelope is independently re-derived below at the exact part needed here.

Source pins:

* logarithmic-pair proof: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`;
* named partner fleet03/B02 completed theorem: brain handoff `yspennstate/math-research-brain@58beb5929b82638976b9f35e5d9659bac2878af7`, canonical mathematics `yspennstate/math-open-problems@c080587ef3f1458c8d1fecff9083d5a8c0d0f6bb`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260922T142939Z-fleet03-B02-QFORM-r11b/REPORT.md`;
* one-dimensional normalized-sum density cap used only in the stress-family application: Rudelson--Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, Theorem 1.2: a normalized linear combination of independent densities bounded by `K` has density bounded by `sqrt(2) K`.

A fresh fleet02/B03 correction, `QFORM finite-coordinate TT* Hölder closure is nonuniform` (`yspennstate/math-open-problems@e43c2e6afdf2063d5ce3f517d37f066acbda7b12`), was also read. The proof here does not move absolute values through a decoupled `u`-integral and is not affected by that obstruction.

## 2. Translation-uniform pair-to-residual theorem

Let `X=(X1,X2)` have independent real coordinates with densities bounded by one, let `Z` be independent of `X`, and let `B` be a fixed real symmetric invertible **indefinite** `2x2` matrix. Put

`D=|det B|`, `kappa=sigma_min(B)`.

Let `m(Z)` be arbitrary measurable and let `R=R(Z)` be arbitrary except for the density hypothesis below. Consider

`Q=(X+m(Z))^T B (X+m(Z)) + R(Z)`.                         (2.1)

For `p>2` put `q=p/(p-1)`. If `R` has a probability density `r_R in L^q(R)`, then `Q` has an essentially bounded density and

`||p_Q||_infinity <= C_p D^(1/p-1/2) kappa^(-1/p) ||r_R||_q`,          (2.2)

where

`C_p^p = 4 int_0^infinity (2sqrt(2)+s)^p e^(-s) ds`
`        + 2^(2+3p/2)/(p/2-1)`.                                      (2.3)

Crucially, **no independence between the random translation `m(Z)` and the residual `R(Z)` is assumed**. Only the original two coordinates are independent of the remaining original-coordinate bank.

For `p=4`,

`C_4=(992+448sqrt(2))^(1/4)=6.34967158837028...`,                      (2.4)

so

`||p_Q||_infinity <= C_4 (D kappa)^(-1/4) ||r_R||_(4/3)`.             (2.5)

Two convenient consequences are

`||r_R||_2 <= L  =>  ||p_Q||_infinity <= C_4 (D kappa)^(-1/4) L^(1/2)`, (2.6)

and

`||r_R||_infinity <= M  =>  ||p_Q||_infinity <= C_4 (D kappa)^(-1/4) M^(1/4)`. (2.7)

These follow by interpolation with `||r_R||_1=1`.

### Proof

Fix `Z=z`. Translating `X1,X2` preserves their independence and their density caps. It therefore suffices to control the density of `Y^T B Y`, uniformly over the translation of the two one-dimensional input densities.

For every cutoff `rho>0`, split the physical pair domain into `|B y|<=rho` and its complement. On the complement, one of the two original-coordinate derivatives has magnitude greater than `sqrt(2) rho`. Conditioning on the other original coordinate, the inverse image of an output interval of length `eta` on the monotone pieces has total length at most `sqrt(2) eta/rho`; summing the two coordinate choices gives the density contribution

`2sqrt(2)/rho`.                                                       (2.8)

On `|B y|<=rho`, use only the joint cap `<=1`. Orthogonally diagonalize `B` with eigenvalues `beta_+>0>beta_-`, rescale to `z_1^2-z_2^2`, and then put `u=z_1+z_2`, `v=z_1-z_2`. The Jacobian is `D^(-1/2)/2`, while `|B y|^2>=kappa |z|^2`. The transformed near region lies in the square

`|u|,|v| <= sqrt(2) rho/sqrt(kappa)`.

The pushforward of `(1/2)du dv` by `uv` has density `log(L^2/|t|)` with `L=sqrt(2)rho/sqrt(kappa)`. Hence, for the conditional output centered at its critical value,

`h_z(t) <= 2sqrt(2)/rho + D^(-1/2) log_+(2 rho^2/(kappa |t-R(z)|))`.   (2.9)

This is the same logarithmic envelope as the fresh pair-log source, but the derivation above records the exact part used here.

Set `T=2D/kappa`. From (2.9), choose `rho=sqrt(D)` when `|tau|<=T` and `rho=sqrt(kappa |tau|/2)` when `|tau|>T`. We obtain the translation-independent majorant

`Psi(tau)=D^(-1/2)[2sqrt(2)+log(T/|tau|)]`,  `0<|tau|<=T`,

`Psi(tau)=4/(sqrt(kappa) sqrt(|tau|))`,       `|tau|>T`.               (2.10)

For every `p>2`, direct integration gives

`||Psi||_p^p`
` <= [4 int_0^infinity (2sqrt(2)+s)^p e^(-s) ds`
`     +2^(2+3p/2)/(p/2-1)] D^(1-p/2)/kappa`.                         (2.11)

For `p=4`, `int_0^infinity(2sqrt(2)+s)^4e^(-s)ds=184+112sqrt(2)`, and (2.11) is exactly

`||Psi||_4^4 <= (992+448sqrt(2))/(D kappa)`.                          (2.12)

Averaging (2.9) over `Z` gives, almost everywhere,

`p_Q(t) <= E Psi(t-R)=int Psi(t-r) r_R(r)dr`.                          (2.13)

Hölder with exponents `p,q` proves (2.2). This averaging is the key point: the random translation `m(Z)` may be maximally correlated with `R(Z)` and simply disappears because the envelope is uniform over translations. No conditional density cap or independence-after-rotation premise enters. QED.

## 3. Named partner fleet03/B02 applied to an actual inequality

The completed partner theorem at the source pin above states, in particular, that for a genuine original-coordinate scalar pivot `d` in a residual quadratic form and a disjoint physical cross block `C` of its Schur remainder,

`||r_R||_infinity <= 17.315056318 |d|^(-1/2) E_3(C)^(-1/12)`           (3.1)

at its unconditional determinant endpoint (`q_det=2,k=3,r=3/2`). Substitution of (3.1) into (2.7) yields the new composite branch

`||p_Q||_infinity`
` <= 12.952609 (D kappa)^(-1/4) |d|^(-1/8) E_3(C)^(-1/48)`.           (3.2)

This allows arbitrary pair translations depending on the entire residual bank. It is not a convolution-independence argument.

At the partner's leverage-compatible rank-two endpoint,

`||r_R||_infinity <=11.6791522071 |d|^(-1/2) E_2(C)^(-1/8)`,           (3.3)

and the same calculation gives

`||p_Q||_infinity`
` <=11.738270 (D kappa)^(-1/4) |d|^(-1/8) E_2(C)^(-1/32)`.            (3.4)

Thus the named OTHER-account result is used as an input to a genuinely new inequality, rather than merely cited.

A second useful splice uses B02's earlier inverse-free hyperbolic `L^2` packet. If the Schur residual has a density satisfying

`||r_R||_2 <=2 sqrt(M/|a|)`,                                          (3.5)

then (2.6) gives

`||p_Q||_infinity <=8.979792 (D kappa)^(-1/4) (M/|a|)^(1/4)`.         (3.6)

This is the analytic interface needed for an indefinite physical pair plus one product-preserving `L^2` bank packet.

## 4. Exact target-class stress family: one-pair extraction is genuinely insufficient

For every integer `m>=1`, use `1+3m` independent cap-one original coordinates, grouped as

`X0`, `A_1,...,A_m`, `B_1,...,B_m`, `C_1,...,C_m`.

Define

`Y1 = X0/sqrt(2) + (1/sqrt(2m)) sum_j A_j`,
`Y2 = (1/sqrt(m)) sum_j B_j`,
`Y3 = (1/sqrt(m)) sum_j C_j`,

and

`Q_m=2 Y1 Y2 + Y3^2`.                                                  (4.1)

This is an exact rank-three target matrix. Indeed, let `U` have rows

`u_0=(1/sqrt(2),0,0)`,
`u_(A_j)=(1/sqrt(2m),0,0)`,
`u_(B_j)=(0,1/sqrt(m),0)`,
`u_(C_j)=(0,0,1/sqrt(m))`,

so `U^T U=I_3`, and put

`M=[[0,1,0],[1,0,0],[0,0,1]]`.

Then `A=U M U^T` and the nonzero eigenvalues are exactly `{-1,1,1}`. The physical row `0` has leverage `1/2` but scalar pivot `A_00=0`.

For every `B_j`, the physical principal pair on `{0,B_j}` is

`[[0,1/sqrt(2m)],[1/sqrt(2m),0]]`.

Therefore

`D_j=1/(2m)`, `kappa_j=1/sqrt(2m)`, and `D_j kappa_j=(2m)^(-3/2)`.       (4.2)

Every single-pair reciprocal certificate diverges like `(2m)^(3/8)`, even though

`sum_j |det A[{0,B_j},{0,B_j}]| = 1/2`                                (4.3)

for every `m`. Hence dimension-free aggregate pair determinant mass does **not** imply one uniformly conditioned pair. This is a source-valid target-class falsifier for that structural extraction rule, not a counterexample to QFORM.

The correct grouped-coordinate mechanism remains uniformly bounded. The three variables `Y1,Y2,Y3` depend on disjoint original-coordinate banks and are therefore independent. Each is a normalized linear combination of cap-one independent coordinates, so Rudelson--Vershynin Theorem 1.2 gives density cap at most `sqrt(2)`.

For completeness, if `W` has density cap one then the density of `bW^2` satisfies

`||p_(bW^2)||_(4/3) <= C_sq |b|^(-1/4)`,
`C_sq=3^(3/4)/sqrt(2)=1.61185489773531...`.                            (4.4)

To see this, for `b=1`, write `g(y)=[f(sqrt(y))+f(-sqrt(y))]/(2sqrt(y))`; after `y=x^2`, convexity and the one-dimensional bathtub bound for the decreasing weight `|x|^(-1/3)` give

`int g^(4/3) <= 3*2^(-2/3)`,

which is (4.4), and scaling supplies `b`.

Rescale `U=sqrt(2)Y1`, `V=sqrt(2)Y2`, `W=sqrt(2)Y3`, whose density caps are one. Then

`Q_m=U V + W^2/2`.

The pair matrix is `[[0,1/2],[1/2,0]]`, so `D=1/4`, `kappa=1/2`. Combining (2.5) and (4.4) gives, for **every m and every admissible product input law**,

`||p_(Q_m)||_infinity`
` <=2 C_4 C_sq`
` =20.4694984974508...`.                                               (4.5)

Thus bank aggregation completely repairs the vanishing individual-pair scale in this exact target family.

## 5. What this pays and the first unpaid implication

The fresh owner correction asks for a translation-uniform fractional-trace synthesis and for an exhaustive product-preserving reduction. Equation (2.2) pays the analytic translation part for an indefinite physical pair: once the Schur residual has any `L^q`, `q>1`, density resource, random translations of the pair are harmless. Equations (3.2)--(3.6) make this quantitative for two already-proved residual resources.

The third-compound overlap ledger from B02's preceding run gives dimension-free O0/O1/O2/O3 aggregate mass, but the new stress family (4.1) shows why a proof cannot turn aggregate pair mass into a single good pair before smoothing. The first unpaid implication is therefore now structural and narrower:

> From the surviving O1/O2/principal third-compound aggregate mass (or the complementary high-leverage branch), produce either (i) an indefinite physical pair with controlled `D kappa` whose Schur residual has one of the proved `L^2/L^infinity` product-bank resources, or (ii) a bank-level analogue of (2.2) that aggregates the spread pair mass before reciprocal conditioning.

This must retain arbitrary additional eigendirections and original-coordinate product provenance. Fixed-pair selection is not enough; (4.1)--(4.3) prove that directly.

The target-wide uniform `||phi_Q||_1` criterion remains neither proved nor source-validly refuted for the exact product-input target in this run. The present mechanism deliberately continues toward bounded density without assuming that stronger criterion.

## 6. Classification

Primary run classification: **ESSENTIAL_STEP_APPLIED**.

Also established: **CANDIDATE_REFUTED** for the intermediate extraction rule “aggregate pivot-pair determinant mass forces one uniformly conditioned physical pair.”

Full conjecture: **OPEN**. No continuity claim is made by (2.2) alone.
