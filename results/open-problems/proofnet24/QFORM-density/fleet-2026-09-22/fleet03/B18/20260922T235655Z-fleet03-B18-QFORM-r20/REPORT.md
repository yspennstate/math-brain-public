SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B18, 2026-09-22T23:56:55Z.
attacking: a sharp primary-source maximum-density transfer for diffuse original-coordinate linear banks, then an equation-level splice into fleet04/B18's completed zero-pivot three-bank theorem on a strict no-pivot target family.

# fleet03/B18 r20 — König–Koldobsky / Rogozin diffuse-bank transfer

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Assignment:** Literature-to-proof transfer  
**Owner control observed at entry:** revision `2026-09-22.15`; QFORM only  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Classification:** `PROVED_SUPPORTING_TARGET_LEVEL_BRANCH / FULL_TARGET_OPEN`  
**Continuity:** proved for the new three-bank branch below; unrestricted continuity remains open.

## 1. Exact target and live gap

The owner target remains the universal statement for every dimension, every family of independent real coordinates with probability densities bounded by one, and every real symmetric matrix having at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, iid, or post-rotation-independence hypothesis is introduced here.

The newest owner synthesis reduces the global structural debt to the strict no-pivot class `N3`: after fixing a universal threshold `tau`, all physical diagonals and all physical `2x2` principal determinants are small. That structural reduction is not reproved here. This run attacks a source-valid N3 subfamily where the surviving curvature is carried by disjoint original-coordinate aggregate banks.

The designated completed partner is fleet04/B18 r2,

`yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

It proves that if `X` is a cap-one scalar, `U=<u,X_I>` and `V=<v,X_J>` are normalized linear banks on disjoint original-coordinate blocks also disjoint from `X`, and `K` is a nonsingular symmetric `3x3` matrix with `K_11=0`, then

`||p_((X,U,V)^T K (X,U,V))||_infinity
 <= 6 [R(u) R(v)]^(2/3) |det K|^(-1/3)`,                 (1.1)

with a continuous density. Here `R(a)` is the maximum density of the centered-uniform comparator associated with the coefficient vector `a`.

The partner used the sharp Rogozin rearrangement theorem but left `R(a)` coefficient-dependent. The source transfer below gives a new dimension-free closed form when the bank has no leverage exceeding `4/9`.

## 2. Primary sources and exact hypotheses

### 2.1 Juškevičius–Lee sharp rearrangement

T. Juškevičius and J. D. Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190, Theorem 1 and its maximum-density corollary:

if independent real variables `Z_j` have density caps `K_j`, the maximum density of their sum is no greater than that of independent centered uniform variables having the same density caps. No moment, centering, compact-support, log-concavity, identical-law, or smoothness assumption is imposed on the original variables.

For independent cap-one `X_j` and coefficients `a_j`, the variable `a_j X_j` has density cap `1/|a_j|`. Hence, after discarding zero coefficients,

`||p_(sum a_j X_j)||_infinity <= R(a)`,                            (2.1)

where `R(a)` is the maximum density of `sum a_j U_j` for iid `U_j~Unif[-1/2,1/2]`.

### 2.2 König–Koldobsky sinc integral

H. König and A. Koldobsky, *On the maximal perimeter of sections of the cube*, Advances in Mathematics 346 (2019), 773–804, arXiv:1806.08659, Proposition 7. In their normalization, for every `p>=9/4`,

`integral_R |sin t/t|^p dt <= sqrt(6*pi/p)`.                        (2.2)

This is the only new external analytic input in the proof below. It is a deterministic sinc-integral estimate; no probabilistic assumptions are hidden in it.

For comparison, Livshyts–Paouris–Pivovarov, arXiv:1507.07949, gives the universal one-dimensional projection cap `sqrt(2)` for normalized product linear forms. The new estimate improves that constant on the diffuse coefficient regime identified below.

## 3. Main lemma — sharp diffuse-bank maximum density

### Theorem `QFORM-DIFFUSE-BANK-KK-ROGOZIN-v1`

Let `X_1,...,X_m` be independent real random variables with probability densities bounded by one. Let `a in R^m` satisfy

`sum_j a_j^2 = 1`,

and assume the leverage condition

`max_j a_j^2 <= 4/9`.                                                (3.1)

Then `S=sum_j a_j X_j` has a continuous density and

`boxed: ||p_S||_infinity <= sqrt(6/pi) = 1.381976597885... .`        (3.2)

This improves the general LPP/Ball cap `sqrt(2)=1.41421356...` on this regime.

### Proof

By Juškevičius–Lee, it suffices to bound the centered-uniform comparator

`S_0=sum_j a_j U_j`, `U_j~Unif[-1/2,1/2]` independent.                (3.3)

Each summand is symmetric unimodal, so the convolution density of `S_0` is symmetric unimodal and its maximum is attained at zero. Its characteristic function is

`phi_(S_0)(t)=prod_j sinc(a_j t/2)`, `sinc x=sin x/x`.                 (3.4)

For every nonzero `a_j`, put

`p_j=1/a_j^2`.                                                        (3.5)

The leverage assumption gives `p_j>=9/4`, while

`sum_j 1/p_j=sum_j a_j^2=1`.                                        (3.6)

König–Koldobsky (2.2) and the substitution `s=a_j t/2` give

`integral_R |sinc(a_j t/2)|^(p_j) dt
 = (2/|a_j|) integral_R |sinc s|^(p_j) ds
 <= (2/|a_j|) sqrt(6*pi/p_j)
 = 2 sqrt(6*pi)`.                                                     (3.7)

Hölder with exponents `(p_j)` therefore yields

`integral_R prod_j |sinc(a_j t/2)| dt
 <= prod_j [2 sqrt(6*pi)]^(1/p_j)
 = 2 sqrt(6*pi)`.                                                     (3.8)

Fourier inversion at the maximum point gives

`R(a)=p_(S_0)(0)
 = (1/(2*pi)) integral_R prod_j sinc(a_j t/2) dt
 <= sqrt(6/pi)`.                                                      (3.9)

Combining (2.1) and (3.9) proves the essential-supremum bound.

Condition (3.1) forces at least three nonzero coefficients. The law of `S` is therefore a convolution containing at least two nontrivial `L^1` densities; the convolution of two `L^1(R)` functions is continuous and vanishes at infinity, and further convolution preserves continuity. Thus `S` has a continuous density. QED.

### Leverage-sensitive companion bound

If `h=max_j a_j^2>4/9`, isolate a largest coefficient `a_*` and let the remaining normalized coefficient vector have Euclidean mass `sqrt(1-h)`. Convolution cannot increase maximum density, while Ball/LPP gives the normalized remainder cap `sqrt(2)`. Hence, without any extra source input,

`R(a) <= min{ h^(-1/2), sqrt(2/(1-h)) }`.                            (3.10)

Together, (3.2) and (3.10) give an explicit coefficient-sensitive envelope. It correctly leaves the classical two-coordinate extremizer `h=1/2` at the possible value `sqrt(2)`.

## 4. Required application of fleet04/B18

Take the exact hypotheses of fleet04/B18 (1.1), and assume in addition that both normalized bank coefficient vectors satisfy

`max_i u_i^2 <=4/9`, `max_j v_j^2 <=4/9`.                            (4.1)

Theorem 3.1 gives

`R(u),R(v) <= sqrt(6/pi)`.                                            (4.2)

Insert (4.2) into the partner inequality (1.1). This produces the new closed-form branch

`boxed:
 ||p_((X,U,V)^T K (X,U,V))||_infinity
 <= 6 (6/pi)^(2/3) |det K|^(-1/3)
 < 9.237 |det K|^(-1/3).`                                            (4.3)

The density is continuous by the completed partner theorem. This is an actual equation-level application of fleet04/B18, not merely a citation.

For comparison, using only the generic one-dimensional LPP caps in (1.1) gives

`6*2^(2/3)|det K|^(-1/3)=9.5244... |det K|^(-1/3)`.                  (4.4)

Thus the published sinc estimate gives a strict source-valid improvement throughout the leverage-diffuse bank chamber.

## 5. Strict no-pivot target family

Let three disjoint original-coordinate blocks consist of one scalar coordinate `X_0` and two normalized bank vectors `u,v`, and take

`K = [[0,1,1],[1,0,1],[1,1,0]]`.                                    (5.1)

The physical matrix is `A=W K W^T`, where the three columns of `W` are the disjoint unit vectors defining `X_0,U,V`. Hence the nonzero spectrum of `A` is exactly

`{2,-1,-1}`,                                                         (5.2)

so this is an exact target-normalized indefinite rank-three family. Also `det K=2`.

Whenever both bank leverage caps satisfy (4.1), (4.3) gives

`boxed:
 ||p_(X^T A X)||_infinity
 <= 6 (6/pi)^(2/3) 2^(-1/3)
 = 7.330644692530... .`                                              (5.3)

Moreover, for any prescribed strict no-pivot threshold `0<tau<=4/9`, choose the banks so that

`max_i u_i^2<tau`, `max_j v_j^2<tau`.                                (5.4)

Every physical diagonal of `A` is then zero. Every nonzero physical `2x2` principal determinant is one of

`-u_i^2`, `-v_j^2`, or `-u_i^2 v_j^2`,                               (5.5)

so its absolute value is `<tau`. Therefore (5.1)–(5.5) give a genuine family inside the live strict `N3` class, with all three large eigenvalues retained and with an explicit continuous-density bound (5.3) for every admissible product input law.

This does not solve N3 generally: the structural problem is to derive a payable aggregate-bank certificate from an arbitrary N3 matrix. The theorem only pays the certificate once it exists.

## 6. Primary-theorem non-transfer checks

Two tempting published results were checked and are deliberately not promoted beyond their hypotheses.

1. Banks–Garza-Vargas–Kulkarni–Srivastava, arXiv:2005.08930, Theorem 2.1 and Corollary 2.4, treat a genuinely bilinear-plus-affine expression in two independent entry arrays. The scalar corollary can use two or more bilinear singular directions, but arbitrary same-side quadratic curvature is not among its hypotheses. It therefore does not by itself settle the surviving rank-two-cross-cut N3 chamber.

2. Meka–Nguyen–Vu, arXiv:1507.00829, Theorem 1.8, is a fixed-scale small-ball theorem for multilinear polynomials under a nonconcentration hypothesis. Cap-one input densities can be rescaled to meet a universal version of their one-variable spread hypothesis, but the theorem does not yield the linear-in-interval-length estimate required for an `L^infinity` output density, and diagonal quadratic terms are not part of its multilinear model. It is therefore not an exact solution to the owner target.

## 7. What changed and what remains

**New proved implication:** every two-bank zero-pivot certificate from fleet04/B18 whose two normalized banks have leverage at most `4/9` is paid by the explicit source-pinned continuous-density constant (4.3). The strict N3 target family (5.1) is an exact application with bound `7.331`.

**Full target:** `OPEN / NOT PROVED`.

The first structural debt is still to force, from arbitrary N3 data, either a diffuse/ridge certificate, a determinant/pair certificate, a grouped zero-pivot certificate such as the one paid here, or another already-paid branch. This report makes no fixed-minor extraction claim and does not use any of the live-refuted interfaces (post-rotation independence, arbitrary-joint coarea, positive conditional projection moments, fiber suprema, law-uniform pointwise van der Corput decay, or coefficient-smallness as a probabilistic perturbation).

## 8. Source pins

- Juškevičius–Lee, *Small ball probabilities, maximum density and rearrangements*, arXiv:1503.09190.
- König–Koldobsky, *On the maximal perimeter of sections of the cube*, Adv. Math. 346 (2019), 773–804, arXiv:1806.08659, Proposition 7.
- Livshyts–Paouris–Pivovarov, *On sharp bounds for marginal densities of product measures*, arXiv:1507.07949.
- Banks–Garza-Vargas–Kulkarni–Srivastava, arXiv:2005.08930, Theorem 2.1 / Corollary 2.4 (hypothesis audit only).
- Meka–Nguyen–Vu, arXiv:1507.00829, Theorem 1.8 (hypothesis audit only).
- Designated partner: `yspennstate/math-open-problems@ce50e74f705c49f66524aa6565d4aa4a9be88061`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B18/20260922T182500Z-fleet04-B18-QFORM-r2/REPORT.md`.

Repository synchronization is not native mathematical-brain ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
