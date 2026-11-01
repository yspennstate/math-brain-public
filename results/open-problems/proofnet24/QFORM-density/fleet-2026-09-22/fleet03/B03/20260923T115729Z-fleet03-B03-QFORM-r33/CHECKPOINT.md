SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B03, 2026-09-23T11:57:29Z.
attacking: dependence-safe Plancherel selectors — keep an entire dependent coefficient vector intact in the independent-copy estimate, and quantify exactly when one, two, or three genuine original-coordinate scalar channels cross from fractional energy to linear small-ball scaling.

# Early substantive checkpoint — dependent-coefficient selector Plancherel estimate

Programme `QFORM-DENSITY-3EIG-20260922`; run `20260923T115729Z-fleet03-B03-QFORM-r33`.

Let `X_1,...,X_k` be independent real variables with densities `f_j<=1`. Let `W` be independent of the whole `X`-bank. Let `C(W)=(C_1,...,C_k)` have a (possibly highly dependent) joint density `g_C<=M`, and let `R(W)` be arbitrary. For nonzero reals `beta_j` and arbitrary measurable real one-coordinate phases `P_j`, set

`Q = R(W) + sum_{j=1}^k [P_j(X_j)+2 beta_j X_j C_j(W)]`.

Write `B=prod_j |beta_j|` and `phi(t)=E exp(itQ)`.

For each `j`, define the twisted Fourier transform

`F_{j,t}(xi)=int f_j(x) exp(i t P_j(x)+i xi x) dx`.

Conditioning on `W` preserves the product over the genuine original-coordinate `X_j`'s:

`phi(t)=E_W[ exp(itR(W)) prod_j F_{j,t}(2 beta_j t C_j(W)) ]`.

Cauchy-Schwarz is taken only over the whole `W`-bank, not coordinatewise over sums/differences:

`|phi(t)|^2 <= E_W prod_j |F_{j,t}(2 beta_j t C_j(W))|^2`.

Using only the true JOINT density cap of `C`, then changing variables in all `k` coefficient coordinates,

`|phi(t)|^2
 <= M int_{R^k} prod_j |F_{j,t}(2 beta_j t c_j)|^2 dc
 = M prod_j [ (2|beta_j t|)^(-1) int_R |F_{j,t}(xi)|^2 dxi ].`

Plancherel and `int f_j^2<=int f_j=1` give

`int |F_{j,t}|^2 = 2 pi int f_j^2 <=2 pi`, hence

`boxed: |phi(t)|^2 <= min{1, A_k |t|^{-k}},
        A_k = M pi^k / B.}`

No independence is assumed among the `C_j`, and no conditional density cap for `X-X'` given `X+X'` or conversely appears.

Consequences:

1. `k=1`: for every `0<alpha<1`,

`int_R |t|^{-alpha}|phi(t)|^2 dt
 <= 2 A_1^(1-alpha)/[alpha(1-alpha)].`

At `alpha=1/2`,

`boxed: int |t|^{-1/2}|phi(t)|^2 dt <= 8 sqrt(pi M/|beta_1|).}`

Since `|phi(t)|^2=E exp(it(Q-Q'))` for the independent copy of the WHOLE `Q`, this is a dependence-safe independent-copy half-Riesz estimate. With the standard one-dimensional Riesz identity it also gives

`E|Q-Q'|^{-1/2} <=4 sqrt(2) sqrt(M/|beta_1|)`.

2. `k=2`: `phi in L^2` and

`int |phi(t)|^2 dt <=4 sqrt(A_2)`,
`boxed: ||p_Q||_2^2 <=2 sqrt(M/(|beta_1 beta_2|)).}`

Thus the valid fleet04/B03 collision lemma immediately gives the actual linear collision estimate

`boxed: P(|Q-Q'|<=eps)
 <=4 eps sqrt(M/(|beta_1 beta_2|)).}`

3. `k>2`: taking square roots of the envelope and integrating at the exact crossover `T=A_k^(1/k)` gives

`int_R |phi(t)| dt <= [2k/(k-2)] A_k^(1/k).`

Therefore `Q` has a continuous `C_0` density and

`boxed: ||p_Q||_infinity
 <= [k/(k-2)] (M/B)^(1/k).}`

In particular the first linear-output-small-ball endpoint is exactly `k=3`:

`boxed: ||p_Q||_infinity
 <=3 [M/(|beta_1 beta_2 beta_3|)]^(1/3),`

and so

`P(Q in I) <=3 [M/(|beta_1 beta_2 beta_3|)]^(1/3) |I|`.

This is the requested integrability threshold in a form which keeps the dependent coefficient vector whole. The selector count explains the one/two/three transition: one channel yields only fractional independent-copy energy; two yield `L^2` density and linear collision small-ball; three yield `L^1` characteristic function and linear output small-ball.

A target-valid control family is

`Q=2 sum_{j=1}^3 X_j Y_j + Y^T C_0 Y`,

where `Y=V^T Z`, `V^T V=I_3`, `Z` is a disjoint original-coordinate cap-one product bank, and `C_0` is arbitrary symmetric. The weighted product-projection theorem gives `||p_Y||_infinity<=e^(3/2)`, so the selector theorem yields

`||p_Q||_infinity <=3 sqrt(e)=4.946163812...`

with a continuous density, and the valid fleet04/B03 collision lemma yields

`P(|Q-Q'|<=eps)<=6 sqrt(e) eps`.

The actual matrix on `span(X_1,X_2,X_3) plus range(V)` has block form `[[0,I],[I,C_0]]`; after diagonalising `C_0` inside this deterministic six-dimensional coefficient calculation, each `2x2` block has eigenvalues solving `lambda^2-mu lambda-1=0`, so one eigenvalue in each pair has modulus at least one. Thus this is genuinely inside the three-large-eigenvalue target for every `C_0`.

This does NOT solve the unrestricted theorem: a general surviving QFORM packet need not expose three disjoint genuine original-coordinate scalar selectors with a bounded joint coefficient density, and cross-quadratic terms among the selector coordinates destroy the product factorisation above. The next step is to test whether the r32 near-coloop / near-three-coordinate alternatives force such a selector packet after the already-paid exact-coloop and finite-coordinate exits, or identify the exact residual curvature obstruction.
