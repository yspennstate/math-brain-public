SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B01, 2026-09-22T23:55:24Z.
attacking: random-slope Plancherel and fractional small-ball smoothing; average over a bounded-density coefficient before taking any pointwise Fresnel supremum.

# fleet03/B01 r21 — random-slope Plancherel and overlapping-source smoothing

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: `Oscillatory replacement` / FOURIER  
Run: `fleet03-B01-20260922T235524Z-r21`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING THEOREMS / NEW TARGET-LEVEL BRANCHES / FULL QFORM OPEN**.

The full target remains open: for every dimension, every independent original-coordinate input with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one, prove one universal essential density bound for `X^T A X`, or give a valid target counterexample. No moment, Gaussian, log-concavity, compact-support, connected-support, centering, or post-rotation independence assumption is introduced below.

The phase-aligned fragmented-support obstruction is preserved: there is no law-uniform positive pointwise power decay for a fixed scalar quadratic phase over all densities `f<=1`. The new decay below is obtained only after averaging a genuinely random linear slope having a bounded density. It therefore does not revive the refuted fixed-slope Fresnel assertion.

## 1. Source-valid dependencies

The run uses three completed source-pinned inputs.

1. `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`, fleet02/B06, canonical mathematics `yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`. If `U` is a `k x m` matrix with `UU^T=I_k` and `Z` has independent cap-one coordinates, then `UZ` has a density bounded by `e^(k/2)`.

2. `QFORM-LOG-FRACTIONAL-RIESZ-COMPILER-v1`, own previous B01 report, canonical `yspennstate/math-open-problems@1155c0d3d79c1d0ecc07e0e8a971fbca0f4e9121`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260922T213051Z-auto11/REPORT.md`. For an invertible indefinite original-coordinate pair with `D=|det B|`, `kappa=sigma_min(B)`, and Schur remainder `R`, if `H_alpha=sup_s E|R-s|^(-alpha)`, then

`||p_Q||_infinity <= K_alpha D^(-1/[2(2alpha+1)]) kappa^(-alpha/(2alpha+1)) H_alpha^(1/(2alpha+1))`.

At `alpha=1/4`, the prefactor before `H_(1/4)^(2/3)` is `3*2^(4/3)*e^(-2/3)=3.881190213873266...`.

3. Designated partner fleet04/B01 has completed grouped-square / signed-Fejer report at `yspennstate/math-open-problems@88003dc06af684cc4bc178a7dfe8e7cbebb0f987`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260922T234537Z-fleet04-B01-grouped-square-fejer-r2/REPORT.md`. It records both
`||p_(a dot Z)||_infinity <= sqrt(2)/||a||_2`
for original-coordinate product inputs and the exact signed triangular Fejer identity
`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`.

## 2. Random-slope Plancherel theorem

### Theorem 2.1 — `QFORM-RANDOM-SLOPE-PLANCHEREL-v1`

Let `k>=1`. Let `X=(X_1,...,X_k)` have independent probability densities `f_j<=1`. Let `Y` be independent of `X`. Let `L=L(Y) in R^k` have density `rho_L` with `||rho_L||_infinity <= K`. Let `B` be any real symmetric `k x k` matrix, and let `R=R(Y)` be arbitrary and possibly dependent on `L`. Define

`T = X^T B X + 2 L^T X + R`.

Then for every `t!=0`,

`|phi_T(t)| <= min(1, K^(1/2) (pi/|t|)^(k/2)).`                 (2.1)

No nonsingularity or sign condition on `B` is required.

#### Proof

Put `F(x)=prod_j f_j(x_j)`. Since every `f_j<=1` and integrates to one,
`int F(x)^2 dx = prod_j int f_j(x_j)^2 dx_j <= 1`.
For fixed `t!=0` define
`G_t(l)=int F(x) exp(i t[x^T Bx+2 l dot x]) dx`.
The quadratic factor is unimodular. With Fourier convention `hat h(xi)=int h(x)exp(i xi dot x)dx`, Plancherel and `xi=2t l` give
`int |G_t(l)|^2 dl = (2|t|)^(-k)(2pi)^k int F(x)^2 dx <= (pi/|t|)^k`.
Disintegrate `Y` over `L` and set `m_t(l)=E[exp(i t R)|L=l]`, so `|m_t(l)|<=1`. Independence gives
`phi_T(t)=int G_t(l)m_t(l)rho_L(l)dl`.
Cauchy-Schwarz and `rho_L<=K` give
`|phi_T(t)| <= (int rho_L |G_t|^2)^(1/2)(int rho_L |m_t|^2)^(1/2) <= K^(1/2)(int |G_t|^2)^(1/2) <= K^(1/2)(pi/|t|)^(k/2)`.
Together with `|phi_T|<=1`, this proves (2.1). QED.

This does not contradict the phase-aligned counterexample: the false claim fixes a scalar slope, whereas (2.1) spends the bounded density of a genuinely random slope. If `L` is deterministic, `K=infinity` and the theorem is void.

## 3. Integrated-frequency and fractional-potential consequences

If `k>2`, put `t_0=pi K^(1/k)`. Integrating (2.1) yields
`int_R |phi_T(t)|dt <= 2pi K^(1/k) k/(k-2)`.
Thus Fourier inversion gives a continuous density vanishing at infinity and

`boxed: ||p_T||_infinity <= [k/(k-2)] K^(1/k).`                 (3.1)

At `k=3`,
`boxed: ||p_T||_infinity <= 3 K^(1/3), p_T in C_0(R).`           (3.2)

For `0<alpha<min(1,k/2)`, the Riesz representation gives

`boxed: sup_s E|T-s|^(-alpha) <= C_(alpha,k) K^(alpha/k),`       (3.3)
where
`C_(alpha,k)=pi^alpha k/[Gamma(alpha+1) cos(pi alpha/2)(k-2alpha)]`.
At `k=2, alpha=1/2`,

`boxed: sup_s E|T-s|^(-1/2) <= 4 sqrt(2) K^(1/4).`              (3.4)

## 4. Overlapping-source physical cross-block theorem

Partition original coordinates into `I,J`, with `|I|=k>=3`, and write
`Q = X_I^T B X_I + 2 X_I^T C X_J + R(X_J)`.
Assume physical cross block `C` has full row rank `k`. Put `S=(CC^T)^(1/2)` and `U=S^(-1)C`, so `UU^T=I_k`. The weighted affine-fiber theorem gives cap at most `e^(k/2)` for `UX_J`, hence
`K=||p_(CX_J)||_infinity <= e^(k/2)/sqrt(det(CC^T))`.
Apply (3.1):

`boxed: ||p_Q||_infinity <= sqrt(e)[k/(k-2)] det(CC^T)^(-1/(2k)), p_Q in C_0(R).`     (4.1)

At `k=3`,
`boxed: ||p_Q||_infinity <= 3 sqrt(e) det(CC^T)^(-1/6) < 4.947 det(CC^T)^(-1/6).`      (4.2)

All self-curvature, complement curvature, signs, affine terms, and extra spectrum remain. No diagonalization is used. This is not full QFORM because the live correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` shows three large eigenvalues do not force such a physical cut.

Applying the partner signed-Fejer identity to (4.1),
`sup_(T0>0,y) D_(T0) law(Q)(y) <= sqrt(e)[k/(k-2)] det(CC^T)^(-1/(2k))`.
This is an actual averaged-frequency application, not citation-only.

## 5. Two-slope half-Riesz plus outer scalar square

Suppose an exact scalar pivot gives
`Q = a(X_0+h(Y))^2 + T(Y)`, `a!=0`, with `X_0` independent of `Y`. Suppose in `T` two original coordinates have residual cross block `C` to the rest with rank two. Then `K<=e/sqrt(det(CC^T))`, and (3.4) gives
`sup_s E|T-s|^(-1/2) <= 4sqrt(2)e^(1/4) det(CC^T)^(-1/8)`.
The shifted square has density envelope `|a|^(-1/2)|u|^(-1/2)`, so

`boxed: ||p_Q||_infinity <= 4sqrt(2)e^(1/4)|a|^(-1/2)det(CC^T)^(-1/8) < 7.264 |a|^(-1/2)det(CC^T)^(-1/8).`   (5.1)

This proves essential boundedness; continuity is not claimed from this transducer alone.

## 6. Dependence-safe scalar random-slope small ball

### Lemma 6.1 — `QFORM-SCALAR-RANDOM-SLOPE-SMALLBALL-v1`

Let `X` be independent of `(L,S)`, `f_X<=1`, and assume only that the marginal density of `L` is bounded by `K`. For arbitrary `a`, put `T=aX^2+2LX+S`. Then for every `t` and `rho>0`,

`boxed: P(|T-t|<=rho) <= min(1,4 sqrt(K rho)).`                  (6.1)

Proof for `a!=0`: set `b=|a|`, complete the square, and put `Y=X+L/a`. Its marginal density is a convolution and has cap `m<=min(1,bK)`. For `r>0`, `P(|Y|<=r)<=2mr`. Conditional on `(L,S)`, on each of `Y>r` and `Y<-r` the completed quadratic is monotone with derivative magnitude at least `2br`; an interval of width `2rho` therefore has total preimage length at most `2rho/(br)`. Since the conditional density of `Y` is a translate of `f_X`,
`P(|T-t|<=rho)<=2mr+2rho/(br)`.
Optimize at `r=sqrt(rho/(bm))` to get `4sqrt(mrho/b)<=4sqrt(Krho)`.
For `a=0`, split at `|L|<=delta`: cost at most `2Kdelta`; on the complement the conditional affine preimage has length at most `rho/delta`. Optimization gives `2sqrt(2Krho)<4sqrt(Krho)`. QED.

Layer cake gives, for `0<alpha<1/2`,
`boxed: sup_t E|T-t|^(-alpha) <= (16K)^alpha/(1-2alpha).`        (6.2)
At `alpha=1/4`, `sup_t E|T-t|^(-1/4) <=4K^(1/4)`.

## 7. Pair plus spread-hub branch; partner applied inside inequality

Complete an invertible indefinite original-coordinate pair, with `D=|det B|`, `kappa=sigma_min(B)`. In its Schur residual isolate one original coordinate:
`R=aX^2+2X(h dot Z+beta/2)+S(Z)`, with `h!=0`, no restriction on `a,S`.

Partner fleet04/B01 gives
`K=||p_(h dot Z+beta/2)||_infinity <= sqrt(2)/||h||_2`.
Insert (6.2) at `alpha=1/4` into the log-to-Riesz compiler:

`||p_Q||_infinity <= 3*2^(8/3)e^(-2/3) D^(-1/3)kappa^(-1/6)K^(1/6)`.

Using the partner estimate yields

`boxed: ||p_Q||_infinity <= 3*2^(11/4)e^(-2/3) D^(-1/3)kappa^(-1/6)||h||_2^(-1/6) <10.362 D^(-1/3)kappa^(-1/6)||h||_2^(-1/6).`     (7.1)

This is dependence-safe: `h dot Z` may be arbitrarily dependent on `S(Z)`. Applying the partner signed-Fejer identity again,
`sup_(T0>0,y)D_(T0)law(Q)(y) <10.362 D^(-1/3)kappa^(-1/6)||h||_2^(-1/6)`.
This proves essential boundedness, not continuity in the argument given.

## 8. Frontier and first unpaid implication

The newest fleet01/B06 handoff forces a spread physical hub in an exact-rank-three high-leverage no-pivot survivor and leaves dependence-safe gluing to the residual open. Lemma 6.1 removes the analytic dependence issue once an independent multiplier coordinate is present. It does not supply a uniformly conditioned indefinite endpoint pair.

The clean remaining B01 question is `QFORM-OVERLAP-LOW-RANK-GLUING-v1`: in a matrix with three large eigenvalues surviving the paid diffuse/ridge/grouped-square branches, turn forced spread hub or low-rank cross-bank mass into either (i) a three-dimensional random slope with bounded joint density, closing continuously by (4.1), or (ii) an aggregate of rank-one/two random-slope packets whose logarithmic endpoint costs are averaged before any reciprocal local pair determinant is paid.

The live correction `QFORM-LOCAL-CROSS-RANK3-DICHOTOMY-FALSE` rules out simply requiring one rank-three physical cross cut. The partner grouped-square theorem shows exact disjoint innovation banks are sufficient. The surviving structural task is therefore an overlapping-source/disjointification theorem, not another fixed-coordinate selection.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. The phase-aligned pointwise-decay counterexample remains valid. The `k>=3` cross-block branch has a continuous density; the `k=2` square-transduced and pair-plus-hub branches establish only essential boundedness in the proofs above.
