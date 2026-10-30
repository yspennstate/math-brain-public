SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B18, 2026-09-24T05:03:55Z.
attacking: the near-rank-one cross collar and the exact-private-square extraction barrier; transfer the full Rudelson--Vershynin spectral-tail equation to fractional negative moments, then stress the resulting receiver against a diffuse harmonic rank-three frame.

# fleet02/B18 — spectral-tail fractional moments and a harmonic-frame extraction obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: literature-to-proof transfer / complementary constructions  
Status: **NEW SUPPORTING THEOREM + SOURCE-VALID STRUCTURAL OBSTRUCTION / FULL QFORM OPEN**  
Continuity: separated from essential boundedness below.  
Execution: **WITHOUT_VERIFIED_BRAIN**.

## 1. First unpaid implication

The full owner target is still OPEN. The next structural implication should **not** be formulated as “extract an exact spectral eigen-square on a private original-coordinate bank”. Section 6 below gives an exact rank-three projection family in which every nonzero spectral direction uses at least `n-2` original coordinates, although the pinned diffuse theorem pays the whole family by `12`.

A source-valid replacement is the following overlap-aware obligation.

### `QFORM-OVERLAP-AWARE-SQUARE-OR-FRAME-EXIT-v1` — still unpaid

Starting only from `s_3(A)>=1`, force either

1. an ORIGINAL-coordinate packet `I disjoint J disjoint {w} disjoint K` with
   `A_II=0`, `A_Iw=0`, `a=A_ww!=0`, and
   `|a| S_1(A_IJ) >= c>0`,
   while retaining all `J-J`, `J-w`, and conditioned `K` terms; or
2. an already-paid aggregate frame / projected-crossing / hub / physical-pair exit with universal parameters.

The theorem proved in Sections 3--5 pays branch 1. The harmonic family proves that a stronger extraction principle requiring the square direction itself to be a sparse/private spectral eigenvector is false as a universal proof interface. Small nonzero coefficients are never deleted.

## 2. Latest designated partner and exact primary source

The latest compatible designated-partner result observed before publication is fleet03/B18 auto18:

- scientific commit `5c462c1aa1cd2ce2fd59eae1fbe4ac2c6136c0d6`;
- theorem `QFORM-RV-SPECTRAL-TAIL-CROSS-v1`;
- check commit `46a6d528974534e55be0617a4bfa2a1beee34d98`, status PASS.

For disjoint original-coordinate cap-one product banks `X,Y`, deterministic `alpha`, arbitrary measurable `G(Y)`, and a real matrix `M`, it obtains a density bound from the Hilbert--Schmidt singular-value tail

`S_r(M)^2 = sum_{j>r} s_j(M)^2`.

For `r=2` it gives a whole-line essential-density estimate proportional to `S_2(M)^(-1)`. Its key source is Mark Rudelson and Roman Vershynin, *Small ball probabilities for linear images of high dimensional distributions*, arXiv:1402.4492v2 / IMRN 2015.

I checked the two primary-source statements actually used here.

1. **Theorem 1.2.** For independent real variables with densities bounded by `K` and a coefficient vector of Euclidean norm one, the scalar linear combination has density at most `sqrt(2) K` a.e. Thus for cap-one original product coordinates and nonzero `v`,

   `||p_(v^T X)||_infinity <= sqrt(2)/||v||_2`.                      (2.1)

2. **Proof of Theorem 8.1, equation (8.4).** The paper defines, for every integer `r>=0`,

   `S_r(M)^2 = sum_{j=r+1}^infinity s_j(M)^2`,                       (2.2)

   and proves

   `L(MY, M0 t S_r(M)) <= (C M0 p)^r`                               (2.3)

   whenever the independent coordinates obey `L(Y_i,t)<=p`; here `L` is the Euclidean-ball concentration function and `C` is absolute. The statement really is for every integer `r`, not only the floored stable rank.

For a cap-one scalar density, `L(Y_i,t)<=2t` under the paper's radius convention. Taking `M0=1` and `t=u/S_r(M)`, and using the supremum over centers in the definition of `L`, gives an absolute constant

`C_* := 2 C`                                                        (2.4)

such that for every deterministic shift `alpha`,

`P{||MY+alpha||_2 <= u} <= min{1,(C_* u/S_r(M))^r}`.                (2.5)

The exact numerical value of the source's universal `C` is not exposed, so I do not invent one. No moment, bounded-support, iid, centering, symmetry, log-concavity, or smoothness hypothesis is added. No projected coordinates are declared independent.

## 3. New source transfer: all fractional spectral-tail negative moments

### Theorem 3.1 — `QFORM-RV-SPECTRAL-TAIL-FRACTIONAL-MOMENT-v1`

Let `Y` be an ORIGINAL-coordinate product bank with every one-dimensional density bounded by one. Let `M` be a finite real matrix, let `alpha` be deterministic, let `r>=1` be an integer with `S_r(M)>0`, and let `0<q<r`. Then

`boxed:
 sup_alpha E ||MY+alpha||_2^(-q)
 <= [r/(r-q)] (C_*/S_r(M))^q .`                                  (3.1)

### Proof

Put `Z=||MY+alpha||_2`. By (2.5),

`P{Z<=u} <= min{1,(C_*u/S)^r}`, `S=S_r(M)`.                        (3.2)

In particular `P{Z=0}=0`. Layer cake for a negative power gives

`E Z^(-q) = q int_0^infinity u^(-q-1) P{Z<=u} du`.                 (3.3)

Split at `u_0=S/C_*`. The lower piece is

`q (C_*/S)^r int_0^u0 u^(r-q-1)du
 = [q/(r-q)] (C_*/S)^q`,                                          (3.4)

and the upper piece is

`q int_u0^infinity u^(-q-1)du = (C_*/S)^q`.                       (3.5)

Adding proves (3.1).

Two endpoints matter here.

- `(r,q)=(2,1)` gives

  `E ||MY+alpha||^(-1) <= 2 C_*/S_2(M)`,                           (3.6)

  which is exactly the negative-moment engine in the newest fleet03/B18 theorem, up to the same harmless convention absorbed into `C_*`.

- `(r,q)=(1,1/2)` gives the new rank-one-tail endpoint

  `boxed: E ||MY+alpha||^(-1/2) <= 2 sqrt(C_*/S_1(M)).`            (3.7)

Thus the primary source supplies a continuum of fractional currencies, and the latest partner's inverse-first-moment estimate is one point on that scale.

## 4. New analytic receiver: rank-one cross tail plus one genuinely private physical square

### Theorem 4.1 — `QFORM-RANK1TAIL-CROSS-PRIVATE-SQUARE-v1`

Let `X` and `Y` be disjoint ORIGINAL-coordinate product banks and let `W` be one further original coordinate, all mutually independent, every scalar density bounded by one. Let

- `M` be a real matrix with `S_1(M)>0`;
- `alpha` be deterministic;
- `a!=0`;
- `G,h` be arbitrary measurable real functions of `Y`;
- `c` be constant.

Set

`T = X^T M Y + alpha^T X + G(Y) + a W^2 + h(Y)W + c`.             (4.1)

Then `T` has an essentially bounded density and

`boxed:
 ||p_T||_infinity
 <= 2^(9/4) sqrt(C_*) / sqrt(|a| S_1(M)).`                         (4.2)

Generic continuity is **not** claimed by this proof.

### Proof

Condition on the genuine original bank `Y=y` and write

`z_y=||My+alpha||_2`.                                               (4.3)

By (2.5) with `r=1`, `P{z_Y=0}=0`. For almost every `y`, Theorem 1.2 gives the conditional linear form

`L_y=(My+alpha)^T X`

a density `f_y` with

`||f_y||_infinity <= K_y := sqrt(2)/z_y`.                          (4.4)

The live correction about nonzero affine square slopes is respected exactly. Completing the square,

`aW^2+h(y)W = a(W+h(y)/(2a))^2 - h(y)^2/(4a)`.                    (4.5)

The shift of `W` does not improve the quadratic singularity. If `g_y` is the density of the random variable in (4.5), reflection for `a<0` and the two-root formula imply the translation-uniform rearrangement bound

`g_y^*(t) <= |a|^(-1/2) t^(-1/2),   t>0`.                         (4.6)

Indeed, for a scalar density bounded by one, the density of `aU^2` is pointwise at most `(|a|s)^(-1/2)` on its half-line; the same bound holds after translating `U` and the output, hence also for decreasing rearrangements.

For any probability density `f` with `||f||_infinity<=K`, the bathtub inequality gives

`int_0^infinity t^(-1/2) f^*(t)dt
 <= K int_0^(1/K) t^(-1/2)dt
 = 2 sqrt(K)`.                                                       (4.7)

Conditional on `Y=y`, `L_y` and the square variable are independent because they use the disjoint original sources `X` and `W`. Hardy--Littlewood therefore yields

`||p_(T|Y=y)||_infinity
 <= int f_y^*(t) g_y^*(t)dt
 <= 2 |a|^(-1/2) sqrt(K_y)
 <= 2^(5/4)|a|^(-1/2) z_y^(-1/2)`.                                (4.8)

Average over `Y` and apply (3.7):

`||p_T||_infinity
 <= 2^(5/4)|a|^(-1/2) E z_Y^(-1/2)
 <= 2^(9/4) sqrt(C_*) / sqrt(|a| S_1(M))`.                         (4.9)

This also proves absolute continuity, because the conditional laws possess densities for almost every `y` and their essential suprema are integrable. QED.

## 5. Full ambient physical-coordinate corollary

Split the ORIGINAL coordinates as

`I disjoint_union J disjoint_union {w} disjoint_union K`.

Assume only

`A_II=0`, `A_Iw=0`, `a=A_ww!=0`,                                 (5.1)

and put `B=A_IJ`. Every block not displayed in (5.1) is arbitrary: `A_JJ`, `A_Jw`, all couplings to `K`, and `A_KK` are retained.

Condition on `X_K`. The quadratic form becomes

`Q = 2 X_I^T B X_J + alpha_K^T X_I + G_K(X_J)
     + a X_w^2 + h_K(X_J)X_w + c_K`,                              (5.2)

where the new functions and shifts may depend arbitrarily on the conditioned value. Apply Theorem 4.1 uniformly with `M=2B`; since

`S_1(2B)=2S_1(B)`,                                                  (5.3)

we obtain

`boxed:
 ||p_Q||_infinity
 <= 2^(7/4) sqrt(C_*) / sqrt(|A_ww| S_1(A_IJ)).`                   (5.4)

This is a whole-line essential-density estimate under arbitrary additional spectrum and arbitrary outside conditioning. It makes no moment or support assumption. It is precisely a **one-sided** source-separation theorem: if `A_Iw` is nonzero, the square source and the conditional cross smoother share `X_I`, and this proof no longer applies.

A useful consistency check is the newest partner theorem. If instead no private square is available but `S_2(B)>0`, fleet03/B18 auto18 pays directly by an inverse-first-moment argument. Here the private square reduces the needed negative moment from order one to order one-half and therefore permits `r=1` in the same primary-source equation.

## 6. Structural obstruction: diffuse harmonic frames have no sparse spectral direction

### Proposition 6.1 — `QFORM-HARMONIC-FRAME-NO-SPARSE-SPECTRAL-DIRECTION-v1`

For every `n>=6`, let

`theta_j=2 pi j/n`, `j=0,...,n-1`,

and define rows

`r_j = n^(-1/2) (1, sqrt(2) cos theta_j, sqrt(2) sin theta_j) in R^3`.  (6.1)

Let `R` be the `n x 3` matrix with rows `r_j`, and let

`A_n = R R^T`.                                                       (6.2)

Then:

1. `R^T R=I_3`, so `A_n` is an exact rank-three orthogonal projection and

   `spec_nonzero(A_n)={1,1,1}`.                                    (6.3)

2. Every physical row leverage is

   `||r_j||_2^2=3/n <= 1/2`.                                       (6.4)

3. Every nonzero vector `u` in the spectral range `range(R)` has at least `n-2` nonzero ORIGINAL coordinates:

   `|supp(u)| >= n-2`.                                              (6.5)

### Proof

The root-of-unity identities give

`sum cos theta_j = sum sin theta_j = sum sin theta_j cos theta_j =0`,

`sum cos^2 theta_j = sum sin^2 theta_j = n/2`,                      (6.6)

which proves `R^T R=I_3` and (6.4).

For `0!=w=(a,b,c)` and `u=Rw`,

`u_j=n^(-1/2)[a+sqrt(2)b cos theta_j+sqrt(2)c sin theta_j]`.         (6.7)

If `(b,c)=(0,0)`, this never vanishes. Otherwise the bracket is

`a+D cos(theta_j-phi)`                                               (6.8)

for some `D>0`; a nonconstant first harmonic has at most two zeros on the circle. Hence (6.5).

Consequently, any proof interface that insists that an **exact spectral eigen-square** `(u^T X)^2` be measurable with respect to a private original-coordinate bank disjoint from every other smoothing bank must allocate at least `n-2` sources to that square. At most two original coordinates remain outside. If those two are split into two nonempty banks, their single physical cross coefficient satisfies

`|A_ij|=|r_i . r_j| <= ||r_i|| ||r_j|| = 3/n`.                     (6.9)

Thus any reciprocal-cross certificate attached to the complement necessarily deteriorates with `n`. This is a statement about that proof extraction, not about the true output density, and it does not permit discarding the many small coefficients of `u`.

## 7. Required pinned-e5f result spent on the obstruction

The completed pinned `e5f71d79eff325201dd0274053d20268ce65b837` Theorem F applies **literally** to the same family `A_n`.

Take its three Fresnel directions to be the columns of `R`, take `lambda_1=lambda_2=lambda_3=1`, take the coordinate set `I` to be all coordinates, and take the residual diagonal part to be zero. Then

`G_I = sum_j r_j r_j^T = R^T R = I_3`,                             (7.1)

and each normalized leverage is exactly `3/n<=1/2`. Therefore Theorem F gives, for every product law allowed by the owner target,

`boxed: ||p_(X^T A_n X)||_infinity <= 12.`                         (7.2)

The theorem's `L^1` characteristic-function proof also supplies a continuous `C_0` representative for this **specific** branch. I do not transfer that continuity claim to Theorem 4.1.

So the harmonic family is a genuine target-valid separation:

- exact private spectral-square extraction becomes maximally source-entangled as `n` grows;
- the aggregate Fresnel--Brascamp--Lieb receiver remains uniformly bounded by `12`.

This is why the next global structural lemma must allow aggregate/overlap-aware frame payment rather than insist on a sparse private eigen-square.

## 8. Secondary target stress test for the new fractional-moment receiver

For `N>=5`, put `delta=(N-1)^(-1/2)` and consider independent cap-one coordinates in

`Q_N = 2 delta sum_{j=1}^N X_j Y_j + 2UV + W^2`.                   (8.1)

The physical matrix has eigenvalues

`+/-delta` (each with multiplicity `N`), together with `-1,+1,+1`.  (8.2)

Hence it has exactly three eigenvalues of modulus at least one. For the cross block `B=delta I_N`,

`S_1(B)=delta sqrt(N-1)=1`.                                        (8.3)

The new physical corollary therefore gives the dimension-free source-valid estimate

`||p_QN||_infinity <= 2^(7/4) sqrt(C_*)`.                          (8.4)

This stress test is not needed for target validity—the pinned aggregate cross theorem also sees it—but it makes the new currency transparent: the top cross singular value tends to zero while the rank-one Hilbert--Schmidt tail remains exactly one.

For completeness, the pinned D5 theorem also applies to this same physical cross cut. Here

`Z_5=e_5(B^T B)=binom(N,5)/(N-1)^5`.                               (8.5)

For `N>=5`,

`Z_5 = (1/120)[N/(N-1)][(N-2)/(N-1)][(N-3)/(N-1)][(N-4)/(N-1)]
 >= (1/120)(1)(3/4)(1/2)(1/4)=1/1280`.                            (8.6)

Thus the pinned no-marginal-condition D5 estimate gives the explicit real whole-line inequality

`boxed:
 ||p_QN||_infinity
 <= 5 sqrt(2e) 1280^(1/10)
 < 23.843.`                                                         (8.7)

Again, this is a proof-certificate comparison, not a lower bound on the true density.

## 9. What remains

The unrestricted theorem remains **OPEN / NOT PROVED / NOT DISPROVED**. The pinned counterexample search reported no valid counterexample, but that search miss is not used as novelty evidence.

This run changes the local proof graph in two ways.

First, the newest fleet03/B18 spectral-tail theorem is not an isolated inverse-first-moment trick: the exact primary equation supplies all negative moments below its integer exponent. The `r=1,q=1/2` endpoint is enough to convolve a one-sided cross bank with one genuinely independent translated square, giving (5.4).

Second, the harmonic-frame family forbids a universal strategy based on finding a sparse/private **spectral** square. A viable global bridge must instead be overlap-aware: use a physical square packet with exact original-source separation when it exists, or pay the diffuse spectral mass in aggregate (Theorem F / projected crossing / grouped hubs) while retaining every nonzero residual term.

The first still-unpaid concrete bridge is therefore:

`QFORM-OVERLAP-AWARE-SQUARE-OR-FRAME-EXIT-v1`.

In particular, the difficult case is when every physical square candidate with useful `|A_ww|` is coupled back into both cross banks or carries unavoidable same-bank residual curvature, while no pinned aggregate-volume/frame gate has universal parameters. Post-rotation independence, perturbative deletion of small coefficients, and arbitrary-joint coarea remain unavailable.

## 10. Source pins

- Primary: Rudelson--Vershynin, arXiv:1402.4492v2, Theorem 1.2 and proof of Theorem 8.1 equation (8.4).
- Latest compatible designated partner: `yspennstate/math-open-problems@5c462c1aa1cd2ce2fd59eae1fbe4ac2c6136c0d6`, fleet03/B18 auto18; PASS check `46a6d528974534e55be0617a4bfa2a1beee34d98`.
- Required pinned source: `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md`.
