SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-23T21:26:17Z.
attacking: endpoint L-infinity*L1 regularization and a product-preserving double-pivot branch that keeps the external coordinate jointly with the near-null curved coordinate.

# account03/B15 auto12 — endpoint regularity compiler and a near-null double-pivot branch

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T212617Z-account03-B15-qform-auto12`  
Status: `ENDPOINT_C0_COMPILER / PHYSICAL_DIAGONAL_TRIPLE_C0 / NEAR_NULL_DOUBLE_PIVOT_BOUND_4 / FULL_QFORM_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary


The completed designated-partner results used below are:

1. account04/B15 pivot-neutral hyperbolic estimate, corrected source
   `yspennstate/math-open-problems@cff8e1368d32302e6d649f776579a5c1951929b1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T151702Z-account04-B15-pivoted-convolution-r6/REPORT.md`:
   for independent cap-one `X,Y`, arbitrary `a,u,v,k`, and `b!=0`,
   
   `||p_(aX^2+2bXY+2uX+2vY+k)||_p <= p |b|^(-1+1/p)` for every `1<p<infinity`.

2. account04/B15 rough conditional-convolution compiler,
   `yspennstate/math-open-problems@d734abaae2eedafe9572b4215107c9637807acaa`,
   `proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T211918Z-account04-B15-rough-mixture-c0-r7/REPORT.md`:
   measurable conditional `L^p*L^q` convolutions with integrable norm product mix to a canonical `C_0` density with the averaged height bound.

This run supplies the missing endpoint `(p,q)=(infinity,1)` regularity compiler and then applies the partner theorem to a genuine nonzero near-null physical branch.

## 2. Endpoint conditional-convolution regularity

### Theorem 2.1 — `QFORM-ENDPOINT-ROUGH-MIXTURE-C0-v1`

Let `(Omega,F,pi)` be a probability space. For almost every `omega`, let `mu_omega` and `nu_omega` be probability measures on `R` with densities

`a_omega in L^1 cap L^infinity`, `b_omega in L^1`.

Assume

`||a_omega||_infinity <= M(omega)` with `M in L^1(pi)`.

Let

`rho(E)=int (mu_omega * nu_omega)(E) d pi(omega)`.

Then `rho` has a canonical density `h in C_0(R)` satisfying

`boxed( ||h||_infinity <= int M(omega) d pi(omega) ).`            (2.1)

No continuity, support bound, moment bound, or modulus is assumed for either input density.

### Proof

For fixed `omega`, define

`h_omega(x)=int a_omega(x-y)b_omega(y)dy`.

Changing either density on a null set changes no value of this convolution. Since `b_omega` is a probability density,

`|h_omega(x)| <= ||a_omega||_infinity <= M(omega)`.                (2.2)

For every real `t`, after the change of variable `z=y-t`,

`h_omega(x+t)-h_omega(x)`
` = int a_omega(x-z)[b_omega(z+t)-b_omega(z)] dz`.

Hence

`sup_x |h_omega(x+t)-h_omega(x)|`
` <= ||a_omega||_infinity ||tau_t b_omega-b_omega||_1 ->0`        (2.3)

because translations are strongly continuous in `L^1`. Thus `h_omega` is uniformly continuous. It is also an `L^1` probability density. A uniformly continuous `L^1` function must vanish at infinity: otherwise one can choose a sequence `|x_m|->infinity` on which `|h_omega(x_m)|>=epsilon`, then uniform continuity supplies disjoint intervals on which `|h_omega|>=epsilon/2`, contradicting integrability. Therefore

`h_omega in C_0(R)`.                                               (2.4)

Define

`h(x)=int h_omega(x)d pi(omega)`.

Equation (2.2) is an integrable dominator. Pointwise continuity and pointwise vanishing of every `h_omega`, followed by dominated convergence, show `h in C_0`. For every interval `I`, Tonelli gives

`rho(I)=int int_I h_omega(x) dx d pi(omega)=int_I h(x)dx`,         (2.5)

so `h` is the density of `rho`. Equation (2.1) follows from (2.2). QED.

### Meaning

The account04/B15 finite-conjugate theorem pays continuity through `L^p*L^q`, `1<p<infinity`. Theorem 2.1 shows a different endpoint mechanism: once one independent original-coordinate group has already created a bounded probability density, convolution with **any** absolutely continuous independent probability group upgrades the result to `C_0` with zero height loss. There is no source-uniform continuity modulus claim.

## 3. A physical diagonal triple has a continuous density with the same beta height

Let `i,j,k` be three distinct original coordinates. Assume their physical principal block is diagonal,

`A_ij=A_ik=A_jk=0`,                                                (3.1)

and `A_ii,A_jj,A_kk` are all nonzero. Suppose, after relabeling, that `A_ii` and `A_jj` have the same sign. Then for arbitrary coefficients and couplings involving every outside coordinate,

`boxed( p_Q in C_0(R),  ||p_Q||_infinity <= pi/sqrt(|A_ii A_jj|) ).` (3.2)

In particular, if all three physical diagonal coefficients have modulus at least `s>0`, then two have the same sign and

`boxed( p_Q in C_0(R),  ||p_Q||_infinity <= pi/s ).`              (3.3)

### Proof

Condition on every outside original coordinate `W=w`. Because (3.1) contains no mutual cross terms among the selected three coordinates, the conditional random part is

`a_i X_i^2+l_i(w)X_i + a_j X_j^2+l_j(w)X_j + a_k X_k^2+l_k(w)X_k`, (3.4)

plus a constant. Completing each square only translates the corresponding original marginal and therefore preserves independence and the density cap one.

For a shifted cap-one variable `Z` and `a!=0`, the density of `aZ^2` obeys

`g_a(y) <= (|a||y|)^(-1/2)`                                       (3.5)

on the appropriate half-line. Since `a_i,a_j` have the same sign, the beta integral gives for their sum

`||p_(a_i Z_i^2+a_j Z_j^2)||_infinity`
` <= 1/sqrt(|a_i a_j|) int_0^1 [u(1-u)]^(-1/2)du`
` = pi/sqrt(|a_i a_j|).`                                          (3.6)

This two-square density is also a probability density, hence belongs to `L^1 cap L^infinity`. The third nonzero shifted square has an arbitrary `L^1` probability density. Theorem 2.1 at a fixed `w` therefore yields a conditional `C_0` density with the height (3.6). The bound is independent of `w`, while all outside couplings are retained in the shifts `l_r(w)`. Mixing over `W` and applying Theorem 2.1/dominated convergence once more gives (3.2). QED.

This adds the stronger continuity conclusion without altering the elementary beta height. It also shows exactly why a third nonzero independent square can regularize a bounded but potentially rough two-square density.

## 4. Actual partner application: retain the external coordinate jointly with the near-null curved coordinate

The previous B15 run proved that for

`gamma Z^2+2rZ`

one cannot obtain a law-uniform improvement from a large affine slope `r`: the source may translate onto the moving critical point. Therefore the correct near-null move is to keep an external original coordinate jointly with `Z` until smoothing is created.

Consider four distinct original independent coordinates `(X,Y,Z,U)` whose physical principal block is

`B = [[a,b,0,0],`
`     [b,0,0,0],`
`     [0,0,gamma,c],`
`     [0,0,c,0]],`                                                 (4.1)

with `b*c !=0`. Here `a` and, crucially, the near-null curvature `gamma` are **arbitrary real numbers**, including zero and arbitrarily small nonzero values. Every outside quadratic coefficient and every coupling from outside coordinates into these four coordinates is arbitrary.

Condition on all outside original coordinates `W=w`. The conditional random part splits into two independent pair outputs

`T_w=aX^2+2bXY+2u_1(w)X+2v_1(w)Y`,                               (4.2)

`S_w=gamma Z^2+2cZU+2u_2(w)Z+2v_2(w)U`,                          (4.3)

plus an output constant. No spectral rotation is used.

Let `1<p<infinity` and `q=p/(p-1)`. Applying the completed account04/B15 pivot theorem first to `(X,Y)` and then, with the roles `(X,Y)=(Z,U)`, to `(Z,U)`, gives

`||p_(T_w)||_p <= p |b|^(-1+1/p) = p |b|^(-1/q)`,                (4.4)

`||p_(S_w)||_q <= q |c|^(-1+1/q) = q |c|^(-1/p)`.                (4.5)

The newest account04/B15 rough-mixture `C_0` theorem now applies to the actual conditional convolution and yields

`boxed(
 p_Q in C_0(R),
 ||p_Q||_infinity
 <= p q |b|^(-1/q)|c|^(-1/p)
)`                                                                  (4.6)

for every conjugate pair `(p,q)`. In particular, taking `p=q=2`,

`boxed( p_Q in C_0(R),  ||p_Q||_infinity <= 4/sqrt(|bc|) ).`      (4.7)

The important feature is that (4.6)-(4.7) are completely independent of `gamma`. Thus this branch remains finite through the nonzero near-null limit `gamma ->0`. The external coordinate `U` is not conditioned away; its cross coupling `cZU` is used as the second smoothing resource.

### A genuine owner-target family with constant 4

The eigenvalues of

`[[a,b],[b,0]]`

both have modulus at least one whenever

`b^2 >= |a|+1`.                                                   (4.8)

The second block

`[[gamma,c],[c,0]]`

has eigenvalue product `-c^2`, so if `|c|>=1` at least one of its two eigenvalues has modulus at least one, for every real `gamma`. Hence (4.1) has at least three eigenvalues of modulus at least one whenever (4.8) and `|c|>=1` hold. By interlacing, every ambient symmetric extension is in the owner's target class. Under these conditions `|b|>=1`, and therefore

`boxed( ||p_Q||_infinity <=4,  p_Q in C_0(R) )`                  (4.9)

uniformly in the near-null parameter `gamma`, all input laws, all dimensions, and all outside coefficients/couplings.

This is a true nonzero-near-null branch, not the invalid one-coordinate affine-slope shortcut corrected in the previous run.

## 5. What this does and does not settle

The new endpoint compiler cleanly separates the central height question from continuity:

- once a product-preserving group supplies a bounded density and an independent group supplies any `L^1` density, continuity follows with no height loss;
- no uniform continuity modulus is required;
- the double-pivot theorem gives a concrete full-target family with universal constant `4`, uniformly through `gamma=0` and `gamma!=0`.

The unrestricted conjecture is still open. A general three-large-eigenvalue matrix need not contain the sparse original-coordinate pattern (4.1), and the live corrections forbid asserting a uniformly good single physical minor or removing cross-pair couplings by rotation. The next missing analytic step is therefore a grouped version of (4.6) tolerating nonzero couplings between the two physical pairs, or a decomposition theorem showing that another already-proved branch pays for those couplings before any fiber supremum.

The result does not use Gaussianity, log-concavity, moments, compact support, connected support, post-rotation independence, arbitrary-joint coarea, uniform pointwise oscillatory decay, or Monte Carlo evidence.

## 6. Regularity ledger

- Absolute continuity: the present branch has explicit densities; no separate coarea premise is needed.
- Essential boundedness: (3.2) and (4.6) are quantitative.
- Continuous density: independently proved by Theorem 2.1 / the partner rough-mixture theorem, not inferred from essential boundedness.
- Full QFORM: `OPEN / NOT PROVED / NOT DISPROVED`.

The first unpaid full-target implication remains the product-preserving treatment of dense transverse couplings under only `s_3(A)>=1`.
