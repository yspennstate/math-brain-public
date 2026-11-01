# Logarithmic two-coordinate smoothing without a nonzero scalar pivot

Programme QFORM-DENSITY-3EIG-20260922. Interactive record 20260922T180015Z-pair-log.

Status: complete supporting analytic argument supplied; independent end-to-end review pending. This does not prove the unrestricted conjecture. No literature-wide novelty claim is made.

## 1. Exact result

Let X have independent real coordinates with probability densities bounded by one. Suppose an original-coordinate principal block A_II has rank exactly three and its three nonzero eigenvalues have absolute value at least s>0. Suppose two coordinates in I give an invertible indefinite principal pair B. Put

`D=|det B|`, `kappa=sigma_min(B)>0`.

Then the FULL ambient quadratic form, with all outside coefficients and couplings arbitrary, has an essentially bounded density satisfying

`||p_(X^T A X)||_infinity <= 8 sqrt(5) (D*kappa*s)^(-1/4)`.    (1.1)

In particular, both scalar diagonal entries of B may be zero. The proof does not divide by either one; it inverts the pair as a whole. It also permits arbitrary original-coordinate affine terms in the full form. Continuity is not claimed by this argument.

The proof gives a more general statement: after completing a fixed indefinite two-coordinate block, it suffices that the remaining scalar random variable R obey

`sup_t P(|R-t|<rho) <= H sqrt(rho)` for every rho>0.           (1.2)

Then

`||p_Q||_infinity <= 4 sqrt(2H) (D*kappa)^(-1/4)`.            (1.3)

The shifts of the two independent input coordinates may depend arbitrarily on R and on every other remaining variable. They need not be independent of the remainder.

This replaces a scalar-pivot obstruction by a quantitative two-coordinate certificate. The bare three-large-eigenvalue assumption does not guarantee one such pair with D*kappa bounded below. Thus the dimension-free aggregation problem is still present; the supporting theorem is not an exhaustive structural reduction.

## 2. Sources and dependencies

The rank-one affine small-ball input used in Section 5 is Lemma 4.1 of the preceding interactive report:

`yspennstate/math-open-problems@e542b1a6ef471b329e4e88a6553e1aacb45acc1a:proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`.

It states, for a unit vector u, nonzero lambda, arbitrary b,d, and independent cap-one coordinates W,

`sup_t P(|lambda*(u dot W)^2+b dot W+d-t|<rho)`
` <= min(1,10 sqrt(rho/|lambda|))`.                         (2.1)

Its proof was read in full and is recalled in Section 7. It uses sharp Hausdorff--Young and geometric rank-one Brascamp--Lieb only in the diffuse one-dimensional case. Classical sources:

* W. Beckner, Inequalities in Fourier analysis, Annals of Mathematics 102 (1975), 159--182, DOI 10.2307/1970980; https://annals.math.princeton.edu/1975/102-1/p11 .
* G. Livshyts, G. Paouris, P. Pivovarov, On sharp bounds for marginal densities of product measures, Theorem 3.3 (geometric Brascamp--Lieb), https://arxiv.org/pdf/1507.07949 .

The present two-coordinate logarithmic envelope is obtained below directly from product conditioning and a two-dimensional change of variables. Neither an arbitrary three-dimensional joint-density coarea bound nor a conditional projection-density moment is used; both are refuted in the companion CORRECTIONS.md.

## 3. A uniform logarithmic envelope for an indefinite physical pair

Let U,V be independent, with density caps one, and let

`F=(U,V) B (U,V)^T+2 ell dot (U,V)+c`,

where B is invertible indefinite. Write D=|det B| and kappa=sigma_min(B). The critical value is `t_0=c-ell^T B^(-1)ell`.

For EVERY gradient cutoff r>0, F has a density for which, almost everywhere,

`p_F(t) <= 2 sqrt(2)/r`
`          + D^(-1/2) log_+(2*r^2/(kappa*|t-t_0|))`.         (3.1)

At t=t_0 the logarithmic expression is allowed to be infinite. The logarithmic singularity, rather than a nonexistent uniform pair density bound, is retained.

### Proof

Translate the two inputs by B^(-1)ell and subtract t_0 from the output. The translated variables remain independent and retain their density caps. It suffices to handle F=y^T B y with joint density f(y_1)g(y_2).

Split the input domain into `N_r={|By|<=r}` and its complement.

On the complement, at least one component satisfies `|(By)_i|>r/sqrt(2)`. Conditional on the other ORIGINAL coordinate, F is a univariate quadratic with derivative `2(By)_i`. The region where its derivative has absolute value greater than sqrt(2)r has at most two monotone intervals. For an output interval of length eta, its inverse image on these intervals has total length at most `sqrt(2)*eta/r`. The density of the remaining scalar input is at most one. Sum over the two coordinate choices, then average the conditioning, to obtain the subprobability density bound `2 sqrt(2)/r` for the complement of N_r.

On N_r we use only the joint density bound f(y_1)g(y_2)<=1. Diagonalize B orthogonally with eigenvalues beta_+>0>beta_-. Set

`z_1=sqrt(beta_+)*(O^T y)_1`,
`z_2=sqrt(|beta_-|)*(O^T y)_2`.

Then `F=z_1^2-z_2^2`, `dy=D^(-1/2)dz`, and

`|By|^2=beta_+ z_1^2+|beta_-| z_2^2 >= kappa |z|^2`.

Thus the transformed N_r lies in the disk `|z|<=r/sqrt(kappa)`. Set `u=z_1+z_2`, `v=z_1-z_2`; then F=uv and `dz=(1/2)du dv`. The disk is contained in the square `|u|,|v|<=L`, where `L=sqrt(2)r/sqrt(kappa)`.

The pushforward of measure `(1/2)du dv` on this square has density, for t!=0,

`(1/2) integral_(|t|/L<=|u|<=L) du/|u|`
` = log(L^2/|t|)` when 0<|t|<L^2, and zero otherwise.

Multiplying by D^(-1/2) proves the near-region term. Adding the far-region bound proves (3.1). All changes of variables are on Lebesgue measures; no independence after diagonalizing B is asserted. Absolute continuity also follows from these measures, since uv has no positive-measure constant level set. QED.

## 4. Averaging the logarithm without conditioning on a spectral complement

Let Z be a vector independent of the two original coordinates U,V. Suppose that, conditional on Z, Q is an affine perturbation of the same indefinite pair B. After completing the pair, write

`Q=( (U,V)+m(Z) )^T B ( (U,V)+m(Z) )+R(Z)`.

Assume R satisfies (1.2). The conditional law of the pair is still a product law with caps one; its two shifts are deterministic for fixed Z. Applying (3.1) conditionally gives

`p_Q(t) <= 2 sqrt(2)/r`
` + D^(-1/2) E log_+(2r^2/(kappa*|t-R|))`.                 (4.1)

For every a>0, layer cake and (1.2) give

`E log_+(a/|t-R|)`
` = integral_0^infinity P(|t-R|<a exp(-v)) dv`
` <= 2H sqrt(a)`.                                         (4.2)

Therefore

`p_Q(t) <= 2 sqrt(2)/r + 2 sqrt(2) H r / sqrt(D*kappa)`.

Choosing `r^2=sqrt(D*kappa)/H` proves (1.3). The bound is an essential supremum bound; the exceptional conditional null sets cause no difficulty by Tonelli on the measurable change-of-variables densities.

This argument permits arbitrary dependence of m(Z) on R(Z). It does not replace independence of the original pair from Z by a mere conditional density cap on one projected scalar.

An optional sharper logarithmic bound retains probability normalization in (4.2). Set a=2kappa by choosing r=kappa, and let H=10/sqrt(lambda). Since

`integral_0^infinity min(1,H sqrt(a) exp(-v/2)) dv`
` <= 2+2 log_+(H sqrt(a))`,

one also has

`||p_Q||_infinity <= [2sqrt(2)+2+2log_+(10sqrt(2kappa/lambda))]/kappa`,

using D>=kappa^2. This can improve the numerical constant in individual cases.

## 5. Why a rank-three block leaves a quantitatively curved rank-one remainder

First work inside an ORIGINAL-coordinate principal block A_II of exact rank three, with nonzero eigenvalues of absolute value at least s. Write

`A_II=V M V^T`, `V^T V=I_3`, `sigma_min(M)>=s`.

Reorder the selected two physical coordinates first. Their invertible principal block B ensures that the corresponding two rows of V have rank two. Choose an orthonormal SPECTRAL basis in which

`V_pair=[F,0]`, `V_rest=[G,h]`,

where F is an invertible 2-by-2 matrix. Write

`M=[[L,k],[k^T,d]]`.

Then `B=F L F^T`, so L is invertible. Orthonormality of V gives `h^T h=1` and `G^T h=0`. Direct block multiplication shows that the Schur complement of B is exactly

`S=lambda h h^T`, `lambda=d-k^T L^(-1)k`.

Since M is invertible, lambda!=0, and the block inverse identity gives

`1/lambda=(M^(-1))_(33)`.

Thus

`1/|lambda| <= ||M^(-1)|| <=1/s`, so `|lambda|>=s`.          (5.1)

This statement retains the spectral scale without choosing a third physical coordinate with a large entry.

Now condition on all ambient coordinates outside I. Inside I the original coordinates remain independent. Outside couplings only add deterministic affine terms. Completing the physical pair leaves

`R=lambda*(h dot X_rest)^2 + b_w dot X_rest+d_w`,

with `|h|=1` and `|lambda|>=s`. The affine vector b_w need not be in the span of h. By (2.1), (1.2) holds with `H=10/sqrt(|lambda|)<=10/sqrt(s)`, uniformly in the outside conditioning. Substitution into (1.3) gives

`4 sqrt(20/sqrt(s)) (D*kappa)^(-1/4)`
` =8 sqrt(5) (D*kappa*s)^(-1/4)`.

Averaging the outside conditional laws proves (1.1). QED.

For a definite physical pair B, no rank or Schur condition is needed: integrating the capped two-coordinate joint density over an entire ellipse gives the simpler bound `pi/sqrt(|det B|)` for every affine perturbation, and this survives outside conditioning.

## 6. Zero diagonal pivots and explicit scope

If B=[[0,b],[b,0]], b!=0, then D=b^2 and kappa=|b|, so (1.1) becomes

`||p_Q||_infinity <=8sqrt(5) |b|^(-3/4) s^(-1/4)`.

Thus the method stays valid when BOTH candidate scalar pivots are exactly zero. It also covers arbitrary correlated shifts of both pair coordinates before the residual smoothing is averaged.

For an exact-rank-three target matrix with nonzero eigenvalue magnitudes at least one, suppose some off-diagonal entry has magnitude at least 1/2 while both associated diagonals have magnitude at most 1/4. The pair is a diagonal perturbation of [[0,b],[b,0]], so it is indefinite and kappa>=1/4. The optional logarithmic bound gives

`||p_Q||_infinity <=4*(2sqrt(2)+2+log(50)) <35`.

To justify replacing kappa by 1/4: the function `(2sqrt(2)+2+log_+(200kappa))/kappa` is decreasing on (0,infinity), by differentiating on its two smooth intervals and checking continuity at 1/200.

The theorem still does not cover every target matrix. The family `[1] direct_sum J_m/m direct_sum (-J_m/m)` has eigenvalues 1,1,-1 but every nonzero indefinite physical pair has kappa at most 1/m. More generally, the quantitative pair can be distributed across many original coordinates. An exhaustive aggregation argument is required before declaring the full conjecture solved.

Claim IDs: QFORM-PHYSICAL-PAIR-LOG-ENVELOPE-v1; QFORM-PAIR-LOG-SMALLBALL-SMOOTHING-v1; QFORM-RANK3-INDEFINITE-PAIR-PIVOT-v1.

## 7. Verification of the rank-one affine input

For completeness, the only programme-specific input (2.1) follows as follows. For `R=lambda(u dot W)^2+b dot W+d` with |u|=1:

* If some u_i^2>=1/2, condition on all other original coordinates. The inverse image of an interval of length 2rho under the resulting quadratic has length at most `2sqrt(2rho/(|lambda|u_i^2))<=4sqrt(rho/|lambda|)`. Its input density is at most one.
* Otherwise all u_i^2<=1/2. At frequency t, multiply each f_i by exp(it b_i x); its L^p norms are unchanged and at most one. Geometric Brascamp--Lieb with weights u_i^2 and sharp Hausdorff--Young give an L^1 Fourier bound `(2pi)*sqrt(e)` for the complex pushforward under u dot W. Gaussian-regularized one-dimensional Fresnel inversion then gives `|phi_R(t)|<=sqrt(e*pi)/sqrt(|lambda*t|)`. The beta/linear terms were retained as phases, not discarded.

Using `1_(|x|<rho)<=exp(v)exp(-v x^2/rho^2)`, Gaussian Fourier inversion and this envelope yield

`P(|R-w|<rho) <= exp(v)*sqrt(e)*Gamma(1/4)/(sqrt(2)*v^(1/4)) * sqrt(rho/|lambda|)`.

Set v=1/4. The prefactor is `exp(3/4)*Gamma(1/4)<10`: the elementary bound `Gamma(1/4)<=4+exp(-1)` suffices. This establishes (2.1), including arbitrary affine terms, without moments or regular input supports.

All novel supporting conclusions in this report remain pending independent mathematical review. Finite algebra and matrix checks do not certify the universal theorem.
