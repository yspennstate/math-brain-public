SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B16, 2026-09-24T08:24:44Z.
attacking: QFORM-HUBSTAR-PAIR-PREABSOLUTE-THIRDRESOURCE-v1, with a mechanism change to a three-disjoint-bank projection-product L^(3/2)-by-L^3 receiver before returning to the genuinely shared-bank collar.

# account03/B16 r44 — projected square plus aggregate hyperbolic bank

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T082444Z-account03-B16-QFORM-auto11-r2`  
Role: Projection-product interaction  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `NEW SUPPORTING TARGET-LEVEL THEOREM / FULL QFORM OPEN`  
Full-target continuity: `OPEN`.

## 1. Scope and correction boundary

The owner target is unchanged: the physical coordinates are independent, each scalar density is at most one, there are no moment/support/log-concavity/iid assumptions, and a general rotation of the matrix is not allowed to create fake independence. The full conjecture remains open. The startup owner control was `math-research-brain@9c2ae26836e7b31d7ccf1ce3f11093ab66a23660`, revision `2026-09-22.15`; immediately before this report was written I refreshed `main` to `d0bea7d1b4fbfb49b86150f6b0282c9147bb5c50` and reread the owner control and live correction inbox. No later redirect invalidated this run.

The previous B16 run showed that the apparently natural mixed obligation

`int |t|^(-1/2) ||G_t||_2 dt < infinity`

is not universally available even in a strict three-large-eigenvalue small-pivot target. Therefore this run does not repeat that absoluteized Fourier route. Instead it spends all three smoothing resources while the relevant original-coordinate banks are still independent.

Two source-valid ingredients are used.

1. The one-dimensional bounded-density projection theorem, in the normalization already used by the fleet, says that for a nonzero coefficient vector `r`, if `S=r^T X` is a linear projection of an original product bank with scalar density caps one, then

`||p_S||_infinity <= sqrt(2)/||r||_2`.                                    (1.1)

A source-pinned fleet use is account02/B04,
`yspennstate/math-open-problems@07305f53ba9b8a1d3e6e79f8c851f415f007d4a7`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/B04-20260922T181702Z-dac07509/REPORT.md`.
This is a marginal density statement, not independence after rotation.

2. A fresh completed account03/B17 argument gives a distribution-free `L^3` estimate for a physical hyperbolic product. I reproduce the needed estimate below, so the theorem here is self-contained apart from (1.1). Its source is
`yspennstate/math-open-problems@fb5c117ab00bebd6a8cc573940b38ce9bd15be13`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B17/20260924T080644Z-account03-B17-QFORM-r12/REPORT.md`.

The closest earlier theorem is account03/B04's `QFORM-SQUARE-RANK1-BANK-LP-CLOSURE-v1`, source
`yspennstate/math-open-problems@bef7cbf7ca6be3fdbe3d63a59f834e1dcb112f6a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/B04-20260922T185416Z-r16/REPORT.md`.
That theorem has a *physical singleton* square. The result below replaces that singleton by an arbitrary projected scalar from a third disjoint product bank. Consequently all three nonzero eigendirections in the exact-rank-three witness may be fully delocalized in the physical coordinates.

## 2. Two quantitative endpoint lemmas

### Lemma 2.1 — square of an arbitrary bounded-density scalar

Let `S` have a probability density `f` with `||f||_infinity<=M`. For `a!=0` and any deterministic shift `d`, let `h` denote the density of

`a(S+d)^2`.

Then

`boxed: ||h||_(3/2) <= 2 M^(2/3) |a|^(-1/3).`                  (2.1)

**Proof.** Reflection of the output reduces to `a>0`, and translating `S` absorbs `d`. For `y>0`, set

`F(r)=f(r)+f(-r)`, `r>0`.

Then `F<=2M`, `int_0^infinity F=1`, and

`h(y)=F(sqrt(y/a))/(2 sqrt(a y))`.

With `y=a r^2`,

`int h(y)^(3/2) dy
 =2^(-1/2) a^(-1/2) int_0^infinity F(r)^(3/2) r^(-1/2) dr`.

Since `F^(3/2)<=sqrt(2M)F`, this is at most

`sqrt(M) a^(-1/2) int_0^infinity F(r) r^(-1/2) dr
 =sqrt(M) a^(-1/2) E|S|^(-1/2)`.

Among probability densities bounded by `M`, the decreasing weight `|x|^(-1/2)` is maximized by height `M` on the centered interval of length `1/M`; hence

`E|S|^(-1/2) <= 2 sqrt(2M)`.

Therefore `int h^(3/2) <=2sqrt(2) M a^(-1/2)`. Taking the power `2/3` gives (2.1). QED.

### Lemma 2.2 — distribution-free `L^3` product endpoint

Let `Y,Z` be independent probability densities bounded by one and let `k` be the density of `2YZ`. Put

`I_* = 1152/25 +(48/5)log 5 +(144/25)(log 5)^2 +(32/25)(log 5)^3`

and

`C_* = I_*/4 = 20.44672085774479...`.                          (2.2)

Then

`boxed: ||k||_3^3 <= C_*`,                                    (2.3)

so for any `c!=0` the density `k_c` of `2cYZ` satisfies

`boxed: ||k_c||_3 <= C_*^(1/3)|c|^(-2/3).`                    (2.4)

The same bound holds after arbitrary deterministic translations of `Y` and `Z`.

**Proof.** For the density `r` of `YZ`, the product formula gives

`r(p)=int f(y) g(p/y) dy/|y|`.

Cauchy--Schwarz, followed by `v=p/y`, gives

`r(p)^2 <= (int f(y)g(p/y)dy)(int f(y)g(p/y)dy/y^2) <= |p|^(-1)`,

so `r(p)<=|p|^(-1/2)`. For `0<|p|<1/4`, split the product integral into
`|y|<2|p|`, `2|p|<=|y|<=1/2`, and `|y|>1/2`. The two outside pieces are each at most `2`, while the middle piece is at most `2 log(1/(4|p|))`. Hence

`r(p)<=4+2log(1/(4|p|))` for `0<|p|<1/4`.                     (2.5)

Use (2.5) on `|p|<=1/100` and the power bound outside. Direct integration gives

`int r^3 <= I_*`.

Since `k(t)=r(t/2)/2`, `int k^3=(1/4)int r^3<=C_*`. Scaling the output by `c` gives (2.4). Translating the input laws preserves independence, normalization and the density caps, so the same proof applies. QED.

## 3. Main theorem: three disjoint projected banks

Let `K,I,J,W` be pairwise disjoint sets of original physical coordinates. Put

`S=r^T X_K`, `U=u^T X_I`, `V=v^T X_J`,

with

`rho=||r||_2>0`, `s=||u||_2>0`, `t=||v||_2>0`, `sigma=st`.

Let `d(W), alpha(W), beta(W), R(W)` be arbitrary measurable real functions of the disjoint bank `W`, and let `a!=0`. Define

`Q = a(S+d(W))^2 + 2(U+alpha(W))(V+beta(W)) + R(W).`          (3.1)

### Theorem 3.1 — `QFORM-THREEBANK-PROJECTEDSQUARE-HYPERBOLIC-LP-v1`

The law of `Q` has a bounded continuous density and

`boxed:
 ||p_Q||_infinity
 <= D_* [ |a| rho^2 sigma^2 ]^(-1/3),`                         (3.2)

where

`D_* = 4 C_*^(1/3) = 10.93791508120834...`.                   (3.3)

In particular, whenever

`|a| rho^2 >=1` and `sigma>=1`,

`boxed: ||p_Q||_infinity <10.938.`                             (3.4)

No projected coordinates inside a bank are declared independent. Independence is used only between the four *disjoint original-coordinate banks*.

**Proof.** Condition on `W=w`. The three random variables `S,U,V` remain independent because their original-coordinate supports are disjoint.

By (1.1),

`||p_S||_infinity <= sqrt(2)/rho`,
`||p_U||_infinity <= sqrt(2)/s`,
`||p_V||_infinity <= sqrt(2)/t`.                               (3.5)

Apply Lemma 2.1 to the square term. Uniformly in the deterministic conditional shift `d(w)`, its density `h_w` obeys

`||h_w||_(3/2)
 <=2 (sqrt(2)/rho)^(2/3)|a|^(-1/3)
 =2^(4/3)(|a|rho^2)^(-1/3).`                                  (3.6)

For the hyperbolic term set

`U'=(sqrt(2)/s)U`, `V'=(sqrt(2)/t)V`.

Then `U',V'` are independent scalar laws with density caps one and

`2(U+alpha)(V+beta)
 =2(sigma/2)(U'+alpha')(V'+beta')`                            (3.7)

for deterministic shifts `alpha',beta'`. Lemma 2.2 therefore gives the conditional density `g_w`

`||g_w||_3
 <= C_*^(1/3)(sigma/2)^(-2/3)
 =2^(2/3) C_*^(1/3) sigma^(-2/3).`                            (3.8)

The square and hyperbolic terms are conditionally independent. Young's inequality at conjugate exponents `3/2` and `3` gives

`||h_w*g_w||_infinity
 <=4 C_*^(1/3)[|a|rho^2 sigma^2]^(-1/3),`                     (3.9)

uniformly in `w`. The term `R(w)` is only a translation. Averaging the conditional densities proves (3.2).

For every fixed `w`, `h_w in L^(3/2)` and `g_w in L^3`, so their convolution is continuous. The uniform bound (3.9) lets dominated convergence pass continuity through the mixture over `W`. Thus `Q` has a continuous representative with the same cap. In the special case with no `W`-mixture, the convolution is in `C_0(R)` by the standard `L^p*L^q` approximation argument. QED.

## 4. Fully delocalized exact-rank-three target family

The theorem is not merely a singleton-coordinate control. For every integer `m>=2`, take three disjoint banks of `m` independent cap-one coordinates and define the flat unit vectors

`r=u=v=m^(-1/2)(1,...,1)`.

Let

`S=r^T X_K`, `U=u^T X_I`, `V=v^T X_J`,

and

`Q_m=S^2+2UV`.                                                (4.1)

Its original-coordinate matrix is

`A_m = rr^T direct_sum [[0,uv^T],[vu^T,0]].`                  (4.2)

The nonzero spectrum is exactly

`boxed: {-1,+1,+1}.`                                          (4.3)

Thus every `Q_m` is a strict exact instance of the owner target. All three nonzero eigendirections are spread over growing original-coordinate banks, while every nonzero physical matrix coefficient has magnitude exactly `1/m`.

Nevertheless Theorem 3.1 gives, for every admissible choice of the `3m` independent input laws,

`boxed: ||p_(Q_m)||_infinity <=10.93791508120834...<10.938,`  (4.4)

and here the density is continuous and belongs to `C_0(R)`.

This extends the earlier B04 family `Z^2+2UV`: the third spectral direction no longer needs a large physical singleton. In particular, demanding a constant-size physical diagonal or mixed entry is unnecessary for this whole three-bank exact-rank-three chamber.

## 5. Designated partner account04/B16 applied to an actual inequality

The newest completed designated-partner result consumed is account04/B16 r4:

`yspennstate/math-open-problems@7f2bb2d330022b09a6af6e39ab09d054caeaa346`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B16/20260924T041516Z-account04-B16-QFORM-r4/REPORT.md`.

Its phase-aligned source-preserving theorem proves for the strict-target carrier

`R_theta = theta H^2 +(X+Y)^2 +2(H+Z)(X-Y)`                   (5.1)

that

`boxed: ||p_(R_theta)||_infinity
 <=8(sqrt(5)-1)^(-1/4)
 =7.587162715951975...<7.588`                                 (5.2)

for every real `theta` and all allowed cap-one source laws in its stated disjoint-bank construction; the carrier already has at least three eigenvalues of modulus at least two.

Now take an additional disjoint product bank `K`, any coefficient vector `r`, and any real `b`. The random variable

`T=b(r^T X_K)^2`                                              (5.3)

is independent of `R_theta`, with no restriction on the law of `T`. Convolution with an independent probability law cannot increase an `L^infinity` density. Therefore the actual enlarged strict-target family satisfies

`boxed:
 ||p_(R_theta + b(r^T X_K)^2)||_infinity <7.588.`              (5.4)

The added square may itself be fully delocalized over arbitrarily many physical coordinates. Equation (5.4) is the designated partner result applied to a concrete new projection-product inequality; it does not rely on any independence created by rotating a bank.

## 6. What this pays, and what it does not

The theorem pays the entire chamber in which the three rank directions can be assigned to three disjoint original-coordinate source banks: one projected square and one aggregate rank-one hyperbolic interaction. It remains stable under arbitrary *aligned affine contamination* and arbitrary additional quadratic/random baggage from a fourth disjoint bank through (3.1).

It does **not** close the genuinely shared-bank near-coloop/leaking-hub state. If the projected square and one side of the hyperbolic packet use the same original coordinates, the conditional convolution in (3.9) is no longer justified. This is exactly the dependence barrier emphasized by the live corrections and by the earlier same-bank `L^3 x L^(3/2)` counterexamples; a bounded joint projection density alone cannot replace the independence used above.

The next B16 implication is therefore

`QFORM-SHAREDBANK-PROJECTEDSQUARE-HYPERBOLIC-PREABSOLUTE-v1`:

> retain the source provenance when the square projection and one hyperbolic factor overlap, and prove a determinant-homogeneous replacement for (3.9), or route every failure to an already-paid definite-plane / phase-aligned / fresh-source exit. The new three-bank theorem is the exact disjoint endpoint that such an overlap theorem must recover.

A fresh interactive source also advanced the simpler curved marginal `U+cV^2` under bounded-square/bounded-support hypotheses, but that does not remove the unbounded fragmented shared-bank case; this report therefore does not promote it to the unrestricted theorem.

## 7. Deterministic checks and final status

The run checker verifies

- `I_*=81.78688343097915...`, `C_*=20.44672085774479...`;
- `D_*=4 C_*^(1/3)=10.93791508120834...`;
- the designated-partner constant `7.587162715951975...<7.588`;
- for `m=7`, the fully delocalized matrix (4.2) has nonzero spectrum numerically `[-1,1,1]` and maximum physical coefficient exactly `1/7`.

The checker ends `STATUS=PASS`. It is regression evidence; Sections 2--5 contain the proofs.

Final status:

- `QFORM-THREEBANK-PROJECTEDSQUARE-HYPERBOLIC-LP-v1`: **PROVED supporting target-level theorem**.
- Exact fully delocalized rank-three family (4.1): **continuous `C_0` density and universal cap `<10.938`**.
- Designated account04/B16 result: **applied to actual enlarged strict-target inequality (5.4)**.
- Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full-target continuous-density conclusion: **OPEN**.
- Execution: **WITHOUT_VERIFIED_BRAIN**; repository access is not native learned-memory ingestion.
