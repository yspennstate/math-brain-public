SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 01, slot B01, 2026-09-23T00:12:42Z.
attacking: mixed-order minor Fourier synthesis: combine heavy 3-volume with complementary 2-volume before reciprocal coordinate selection.

# QFORM fleet01/B01: mixed-order minor Fourier theorem and one-heavy-row closure

## Status

**ESSENTIAL_STEP_APPLIED / NEW AVERAGED-FREQUENCY THEOREM / FULL QFORM OPEN.**

The exact owner target remains open. This report does not assert the unrestricted three-large-eigenvalue theorem and does not assert a universal continuity theorem. The new theorem below gives an L1 characteristic-function bound, hence a bounded continuous density, in its stated cross-block scope. It preserves the known phase-aligned fragmented-support counterexample to every law-uniform pointwise scalar quadratic-phase decay estimate.

Fresh control source before the run: `yspennstate/math-research-brain`, owner revision `2026-09-22.15`, QFORM-only. Source analytic premise: `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/FOURIER_ROUTE_REPORT.md`, whose fixed-order volume-sampling Brascamp--Lieb theorem is extended below. Assigned partner used: fleet02/B01 r31, canonical report `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B01/20260922T233020Z-fleet02-B01-qform-r31/REPORT.md`.

## 1. Mixed-order minor Fourier theorem

Let `I,J` be disjoint sets of original coordinates, condition all remaining original coordinates, and let `M=A_{IJ}`. As in the proved decoupling route, for the conditioned quadratic polynomial one has

`|phi(t)|^2 <= int prod_{i in I} h_i(<r_i,w>) prod_{j in J} g_j(w_j) dw`,

where `r_i` is row `i` of `M`, `h_i(s)=|psi_i(2ts)|`, `psi_i` is the characteristic function of the corresponding original input, and each `g_j` is a probability density with `0<=g_j<=1`.

Let `Omega` be any probability distribution on **nonzero square physical minors of varying order** `(S,T)`, with `S subset I`, `T subset J`, `|S|=|T|=k(S,T)>=1`, and `det M_{ST} !=0`. Define

`alpha_i = P_Omega(i in S)`,
`beta_j  = P_Omega(j in T)`,
`kbar    = E_Omega |S| = sum_i alpha_i = sum_j beta_j`,

and the entropy-determinant currency

`K(Omega) = exp( E_Omega log det(M_ST)^2 + H(Omega) ).`

### Theorem 1 (mixed-order Brascamp--Lieb/Fourier)

Assume

`alpha_i <= 1/2` for every `i in I`,

and `kbar>2`. Then, uniformly over all self-blocks, all conditioned outside coordinates, and all induced affine terms,

`|phi(t)| <= min(1, e^(kbar/4) (2 pi)^(kbar/2) K(Omega)^(-1/4) |t|^(-kbar/2))`,

and therefore

`||p_Q||_infinity <= 2 sqrt(e) * kbar/(kbar-2) * K(Omega)^(-1/(2 kbar)).`      (1.1)

In particular the conditioned and hence unconditional law has a continuous density vanishing at infinity.

### Proof

Put BL exponents `c_i=alpha_i` on the row maps `w -> <r_i,w>` and `d_j=1-beta_j` on the coordinate maps `w -> w_j`. Since

`sum_i c_i + sum_j d_j = kbar + |J|-kbar = |J|`,

the Brascamp--Lieb scaling condition holds. Rows with `alpha_i=0` can be dropped because `h_i<=1`; coordinates with `beta_j=1` can be dropped because `g_j<=1`.

For Gaussian BL parameters `u_i>0`, `v_j>0`, the exact diagonal-plus-PSD expansion is

`det(D + M^T D_I M)`
` = sum_{T subset J} sum_{|S|=|T|} det(M_ST)^2 prod_{i in S}(alpha_i u_i) prod_{j notin T}((1-beta_j)v_j).`

Every support point of `Omega` is one term in this positive expansion. Weighted AM--GM therefore gives

`det(D + M^T D_I M)`
` >= K(Omega) prod_i (alpha_i u_i)^(alpha_i) prod_j ((1-beta_j)v_j)^(1-beta_j).`

Thus Lieb's Gaussian formula yields

`BL <= K(Omega)^(-1/2) prod_i alpha_i^(-alpha_i/2) prod_j (1-beta_j)^(-(1-beta_j)/2).`

Because `alpha_i<=1/2`, the source Lp lemma applies with `p=1/alpha_i>=2`:

`int |psi_i(s)|^(1/alpha_i) ds <= 4 pi sqrt(alpha_i)`.

After the scaling `s=2t x`,

`|| h_i^(1/alpha_i) ||_1^(alpha_i)
 <= (2 pi/|t|)^(alpha_i) alpha_i^(alpha_i/2).`

These powers cancel the row factors in `BL`. Also `g_j<=1`, `int g_j=1`, hence

`int g_j^(1/(1-beta_j)) <=1`.

Finally

`prod_j (1-beta_j)^(-(1-beta_j)/2) <= exp( (1/2) sum_j beta_j ) = e^(kbar/2)`,

using `-(1-x)log(1-x)<=x`. Therefore

`|phi(t)|^2 <= e^(kbar/2) (2 pi/|t|)^kbar K(Omega)^(-1/2).`

Taking square roots gives the displayed pointwise envelope. With `a=kbar/2>1` and `B=e^(kbar/4)(2pi)^(kbar/2)K^(-1/4)`,

`int_R min(1,B|t|^(-a)) dt = 2a/(a-1) B^(1/a)`.

Fourier inversion then gives exactly (1.1), since

`B^(1/a)=sqrt(e) (2pi) K^(-1/(2kbar))`.

QED.

This theorem is not a forbidden law-uniform scalar Fresnel estimate. The decay appears only after decoupling, original-coordinate product structure, Brascamp--Lieb, and an **averaged minor-order currency** have been combined.

## 2. Heavy 3-volume + 2-volume gives exponent 5/4

Let `w0` be the natural 3-volume law on nonzero physical `3x3` minors of `M`:

`w0(S,T)=det(M_ST)^2/Z`,

where

`Z=e_3(M^T M)>0`.

Fix a row `i` with

`alpha=P_w0(i in S)>0`,

write `r=r_i`, and let

`w3 = w0(. | i in S)`.

Then

`K(w3)=alpha Z`.

Let `a_k=P_w3(k in S)` for `k!=i`; hence `sum_{k!=i} a_k=2`.

### Corollary 2A (direct partner-r31 application)

Delete row `i` and call the remaining matrix `N`. Let `v2` be the natural 2-volume law on nonzero physical `2x2` minors of `N`, with row marginals `q_k`, and put

`Z2=e_2(N^T N)=K(v2)`.

If

`a_k+q_k <=1` for every `k!=i`,                                    (2.1)

then the half-half mixed law

`Omega=(1/2) w3 + (1/2) v2`

has every row marginal at most `1/2` and mean order

`kbar=(3+2)/2=5/2`.

Moreover, because the order-3 and order-2 supports are disjoint,

`K(Omega)=2 sqrt( (alpha Z) Z2 ).`                                  (2.2)

Applying Theorem 1 gives

`||p_Q||_infinity <= 10 sqrt(e) [2 sqrt(alpha Z Z2)]^(-1/5).`        (2.3)

Now apply the completed assigned-partner fleet02/B01 r31 inequality

`Z2=e_2(N^T N) >= alpha Z / ||r||_2^2`.

Substitution into (2.3) gives the actual quantitative inequality

**`||p_Q||_infinity <= 10 sqrt(e) [ 2 alpha Z / ||r||_2 ]^(-1/5).`** (2.4)

Thus a 3-volume-heavy row can be paid without any `(1-alpha)^(-c)` endpoint loss whenever its conditional pair occupancy is compatible with the natural complementary 2-volume law.

### Corollary 2B (self-matched pair law; no natural-2 marginal assumption)

There is a second construction which requires only

`max_{k!=i} a_k <=1/2`.                                             (2.5)

For each unordered pair `R={j,k}` not containing `i`, define

`W_R = sum_{|T|=3} det M_{{i} union R,T}^2 = ||r_i wedge r_j wedge r_k||^2`,

and

`D_R = sum_{|U|=2} det M_{R,U}^2 = ||r_j wedge r_k||^2`.

Under `w3`, the row-pair distribution is

`eta_R=W_R/(alpha Z)`.

Whenever `eta_R>0`, the wedge inequality gives

`D_R >= W_R/||r||^2`.

Define a 2-minor law by first drawing `R~eta`, then drawing the physical column pair `U` with probability

`det(M_RU)^2/D_R`.

Call this law `v2*`. Its row marginals are **exactly** `a_k`. Its entropy-determinant currency obeys

`log K(v2*)
 = H(eta) + sum_R eta_R log D_R
 >= H(eta) + sum_R eta_R log(eta_R alpha Z/||r||^2)
 = log(alpha Z/||r||^2).`

Hence

`K(v2*) >= alpha Z/||r||^2`.                                       (2.6)

Mixing `w3` and `v2*` equally gives row marginal `1/2` at `i` and row marginal `a_k<=1/2` elsewhere, while

`K(Omega)=2 sqrt(K(w3)K(v2*)) >= 2 alpha Z/||r||`.

Theorem 1 again gives exactly (2.4).

This is the key new closure: if a natural 3-volume row is heavy but **not conditionally co-heavy with any other row**, the averaged-frequency route closes with a dimension-free fifth-root bound. The remaining one-heavy-row obstruction is therefore not `alpha ->1` by itself; it is a genuinely clustered co-heavy configuration with some `a_k>1/2`.

## 3. Why the exponent improves

For the half-half 3/2 mixture, `kbar=5/2`, so the characteristic function has tail

`|phi(t)| = O(|t|^(-5/4))`.

That is integrable. A fixed 2-volume theorem alone gives only `|t|^-1`, which is borderline and nonintegrable; a fixed 3-volume theorem may fail because one row marginal exceeds `1/2`. The mixed-minor determinant expansion spends **half of the third direction** and all of the transverse two-volume before taking absolute values. This is precisely an averaged-in-frequency replacement for the false scalar pointwise van-der-Corput step.

## 4. Diffuse-column stress family: every physical endpoint vanishes but the mixed theorem stays uniform

Take the partner r31 six-row Parseval frame `U_alpha` (`0<alpha<1`):

`u_1=(sqrt(alpha),0,0)`,

and rows `u_2,...,u_6` given by the regular pentagon construction in fleet02/B01 r31. Then

`U_alpha^T U_alpha=I_3`,
`Z=e_3(U_alpha^T U_alpha)=1`,
`alpha_1=alpha`,
`P(k in S | 1 in S)=2/5` for `k=2,...,6`.

Now let `m=3r` and let `V_m` be the `m x 3` frame whose three columns are normalized indicators of three disjoint `r`-element physical coordinate blocks. Put

`M_{alpha,m}=U_alpha V_m^T`.

Then the three nonzero singular values of `M_{alpha,m}` are all one. The symmetric bipartite target matrix

`A_{alpha,m} = [[0,M_{alpha,m}],[M_{alpha,m}^T,0]]`

has nonzero spectrum

`{1,1,1,-1,-1,-1}`

for every `alpha,m`, so it lies inside the exact target for arbitrary independent cap-one physical input laws.

The distinguished heavy row still has norm `||r_1||=sqrt(alpha)`, but every physical entry in that row is at most

`sqrt(alpha/r)`,

which tends to zero as `m -> infinity`. Thus any proof paying the reciprocal of one endpoint coefficient loses dimension.

Corollary 2B does not. Since all conditional co-marginals are `2/5`, it gives

`||p_Q||_infinity <= 10 sqrt(e) [2 sqrt(alpha)]^(-1/5).`             (4.1)

For `alpha>=1/2`,

`||p_Q||_infinity <= 10 sqrt(e) 2^(-1/10) = 15.3831133942...`.      (4.2)

As `alpha ->1`, the bound tends to

`10 sqrt(e) 2^(-1/5)=14.3529523093...`.

So the new theorem remains uniformly effective exactly when the natural 3-volume law can concentrate almost completely on one **diffuse physical row** and every individual endpoint coefficient tends to zero.

For `alpha<1/2`, the already-proved natural D/D' branches are available. Hence this whole two-parameter exact-target family is uniformly controlled without selecting one physical cross edge.

## 5. Phase-aligned scalar counterexample remains intact

For every frequency `s>0` and small `delta>0`, the set

`{x: dist(s x^2,2pi Z)<=delta}`

has infinite Lebesgue measure. Taking a finite union of components of total length one gives an admissible density `f<=1` for which

`Re int exp(i s x^2) f(x) dx >= cos(delta)`.

Therefore no uniform scalar `C|s|^-gamma` decay can hold for any `gamma>0`. The mixed-order theorem does not contradict this: it obtains integrability only after the coupled decoupling/BL determinant structure is used.

## 6. What remains

The immediate unpaid case is now sharper:

**QFORM-CLUSTERED-COHEAVY-MIXED-MINOR-v1.** Suppose a useful physical cross block has 3-volume `Z` bounded below, but every row whose 3-volume marginal is `>1/2` has a conditional partner with `a_k>1/2`, so Corollary 2B cannot be applied, while the fleet02/B01 r31 one-row entropy rebalance is also blocked by conditional co-heaviness. Route this finite co-heavy cluster, without reciprocal single-edge/minor loss, to one of:

1. a variable-order minor law `Omega` with `E|S|>2`, all row marginals `<=1/2`, and dimension-free `K(Omega)`;
2. an already-paid ridge / mixed-hub / endpoint-pair branch;
3. a grouped-square or grouped two-slope branch.

The mixed-order theorem shows that one need not preserve order three throughout: **any entropy-determinant minor mixture of mean order strictly greater than two is sufficient**. This changes the structural target from “find a good 3-volume distribution” to “find more than two units of determinant order after capping row occupancy at one half.”

Full QFORM remains OPEN. Continuity is proved only in the scope of Theorem 1/Corollaries 2A--2B, through `phi in L1`.
