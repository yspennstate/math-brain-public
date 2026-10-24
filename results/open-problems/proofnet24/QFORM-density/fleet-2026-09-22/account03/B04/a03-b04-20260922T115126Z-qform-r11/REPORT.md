# QFORM account03/B04 — product Fourier rearrangement

Run: `a03-b04-20260922T115126Z-qform-r11`  
Programme: `QFORM-DENSITY-3EIG-20260922`, control revision `2026-09-22.5`  
Assignment: product Fourier rearrangement  
Status: `PROVED_SUPPORTING_THEOREM`; full conjecture remains open  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Scope and live corrections

The target is the arbitrary-dimensional, arbitrary independent input-law, rotated/indefinite quadratic-form conjecture under `0 <= f_i <= 1` and at least three eigenvalues of modulus at least one. The known uniform pointwise oscillatory-decay claim is false and is not used here. The result below is an averaged Fourier theorem for three independent square directions, followed by a genuinely rotated indefinite example.

At the coherent pre-publication snapshot no completed `account04/B04` QFORM handoff existed. I therefore did not fabricate a partner result. I did consume the compatible `account04/B14` extreme-product reduction (`20260922T114319Z-b14-qform-extreme-reduction-r1`, brain blob `1cc6b030bb92579d97e4826914a248f5037d054b`; full report pinned there to math-open-problems commit `8fcc9ba5db68dfd4cd5daeb181a39666ceeda322`, blob `30ebe93170ba26fb57dc128ee0116762de1d9f26`). Its bathtub/extreme-point logic is compatible with the rearrangement step below and confirms that no regularity, moment, or connected-support hypothesis should be inserted. The proof here in fact works directly for every admissible density.

## 2. Single-square averaged Fourier lemma

### Lemma 2.1
Let `Y` be real-valued with probability density `h` satisfying `0 <= h <= M`. Let `lambda != 0`, and define

`F_lambda(t) = E exp(i t lambda Y^2)`.

With Fourier convention

`hat g(t) = integral_R exp(i t y) g(y) dy`,

one has

`||F_lambda||_{L^3(R)} <= 2 (2 pi)^(1/3) M^(2/3) |lambda|^(-1/3)`.

This is an integrated-frequency statement; it makes no pointwise-decay assertion.

### Proof
Let `Z=Y^2`. For `z>0`, a version of the density of `Z` is

`g(z) = [h(sqrt z)+h(-sqrt z)]/(2 sqrt z)`,

hence

`0 <= g(z) <= M z^(-1/2)`,  and  `integral_0^infty g(z) dz = 1`.

Let `g*` be the decreasing rearrangement of `g`. Since the majorant `M z^(-1/2)` is already decreasing,

`g*(s) <= M s^(-1/2)` for every `s>0`,

and `integral_0^infty g*(s) ds = 1`.

Among all nonnegative decreasing `u` with `u(s) <= M s^(-1/2)` and integral one, the convex functional `integral u^(3/2)` is maximized by filling the cap from the origin. The filling endpoint `a` is determined by

`integral_0^a M s^(-1/2) ds = 2 M sqrt(a) = 1`,

so `a=1/(4M^2)`. Therefore

`||g||_(3/2)^(3/2) = integral (g*)^(3/2)
 <= integral_0^a M^(3/2) s^(-3/4) ds
 = 4 M^(3/2) a^(1/4)
 = 2 sqrt(2) M`.

Equivalently,

`||g||_(3/2) <= 2 M^(2/3)`.

Riesz-Thorin between the `L^1 -> L^infty` Fourier bound of norm one and Plancherel

`||hat g||_2 = sqrt(2 pi) ||g||_2`

gives Hausdorff-Young at `(p,q)=(3/2,3)` with

`||hat g||_3 <= (2 pi)^(1/3) ||g||_(3/2)`.

Finally `F_lambda(t)=hat g(lambda t)`, so scaling in `L^3` gives

`||F_lambda||_3 = |lambda|^(-1/3)||hat g||_3
 <= 2(2 pi)^(1/3) M^(2/3)|lambda|^(-1/3)`.

QED.

## 3. Three independent square directions

### Theorem 3.1
Let `Y_1,Y_2,Y_3` be independent real random variables with densities bounded respectively by `M_1,M_2,M_3`. Let `lambda_j != 0`. Let `R` be any random variable independent of the triple `(Y_1,Y_2,Y_3)`; no density assumption on `R` is needed. Put

`Q = R + lambda_1 Y_1^2 + lambda_2 Y_2^2 + lambda_3 Y_3^2`.

Then `Q` has a bounded continuous density and

`||p_Q||_infty <= 8 (M_1 M_2 M_3)^(2/3) / |lambda_1 lambda_2 lambda_3|^(1/3)`.

### Proof
Independence gives

`phi_Q(t) = phi_R(t) product_{j=1}^3 F_{lambda_j,j}(t)`

with `|phi_R(t)|<=1`. Hence Holder with exponents `(3,3,3)` and Lemma 2.1 yield

`integral_R |phi_Q(t)| dt
 <= product_j ||F_{lambda_j,j}||_3
 <= 16 pi (M_1 M_2 M_3)^(2/3) / |lambda_1 lambda_2 lambda_3|^(1/3)`.

Thus `phi_Q in L^1`. Fourier inversion gives a bounded continuous density and

`||p_Q||_infty <= (1/(2 pi)) ||phi_Q||_1`,

which is exactly the displayed constant eight. QED.

### Why this survives the known pointwise counterexample
The phase-aligned-density construction can make one `F_lambda(t_0)` arbitrarily close to one at a selected large frequency. Lemma 2.1 does not prohibit that. It controls the total `L^3` frequency budget, and the product of three such budgets is integrable by Holder. This is precisely the averaged mechanism that the pointwise-decay correction leaves available.

## 4. Product-coordinate corollary

Let the coordinate sets `S_1,S_2,S_3` be pairwise disjoint and let

`Y_j = sum_{i in S_j} a_{ji} X_i`,  with  `alpha_j := max_{i in S_j}|a_{ji}| >0`.

If the `X_i` are independent with densities bounded by one, then conditioning on all coordinates except an index attaining `alpha_j` shows that `Y_j` has density bounded by

`M_j <= alpha_j^(-1)`.

Because the sets `S_j` are disjoint, the three `Y_j` are independent. Consequently, for any independent remainder `R` based on coordinates outside `S_1 union S_2 union S_3`,

`Q = R + sum_{j=1}^3 lambda_j Y_j^2`

has a continuous density with

`||p_Q||_infty <= 8 (alpha_1 alpha_2 alpha_3)^(-2/3)
                     |lambda_1 lambda_2 lambda_3|^(-1/3)`.

This is dimension-free whenever the three block directions have a dimension-free coordinate localization lower bound.

## 5. Explicit genuinely rotated indefinite quadratic form

Take six independent admissible inputs and define

`Y_1=(X_1+X_2)/sqrt(2)`,
`Y_2=(X_3+X_4)/sqrt(2)`,
`Y_3=(X_5+X_6)/sqrt(2)`.

Each sum `X_{2j-1}+X_{2j}` has density of `L^infty` norm at most one by convolution, so each `Y_j` has density at most `sqrt(2)`. The `Y_j` are independent. For

`Q = Y_1^2 + Y_2^2 - Y_3^2`

Theorem 3.1 gives

`||p_Q||_infty <= 8 ((sqrt(2))^3)^(2/3) = 16`.

In the original coordinate basis the matrix of `Q` is block diagonal with blocks

`(1/2) [[1,1],[1,1]]`, `(1/2) [[1,1],[1,1]]`, and `-(1/2) [[1,1],[1,1]]`.

Hence it is genuinely non-coordinate-diagonal and indefinite, with eigenvalues

`1,1,-1,0,0,0`.

It therefore has exactly three eigenvalues of modulus at least one and satisfies the target hypotheses. The bound `16` is uniform over all six input laws with densities bounded by one.

## 6. What is and is not proved

Proved here:

1. A law-uniform `L^3` bound for the quadratic characteristic function of one bounded-density scalar input.
2. A law-uniform `L^1` characteristic-function bound for a sum of three independent square directions.
3. An explicit continuous-density bound `16` for a genuinely rotated indefinite six-variable form with eigenvalues `1,1,-1,0,0,0`.
4. The more general disjoint-block estimate above with explicit dependence on `alpha_j` and `lambda_j`.

Not proved:

The full conjecture has overlapping spectral directions after rotation. In that case the three spectral coordinates are generally dependent, so the exact product factorization used in Theorem 3.1 disappears. A marginal density bound for the three-dimensional spectral projection is not enough by itself, and the known fiber-supremum route loses dimension.

## 7. First unpaid implication

The next B04 implication is an **overlap replacement for the product Holder step**. One needs a product-space/rearrangement inequality for

`phi(t)=E exp(i t sum_{j=1}^3 lambda_j <r_j,X>^2)`

with orthonormal `r_j`, which recovers an `L^1_t` bound from three averaged one-direction square budgets without assuming the supports of the `r_j` are disjoint. Any candidate inequality must retain the original coordinate-product law and must pass the rank-two opposite-sign logarithmic-singularity control. The present theorem supplies the exact endpoint constant and scaling that such an overlap inequality should reproduce in the disjoint-support case.

No full-solution or novelty claim is made.
