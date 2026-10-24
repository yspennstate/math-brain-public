SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B09, 2026-09-22T23:41:38Z.
attacking: external-smoother routing for the indefinite lightcone residual via disjoint coordinate banks and conditional linear anti-concentration.

# account02/B09 QFORM r12 — a gapped hyperbolic Schur pair automatically pays a disjoint external square

Programme: `QFORM-DENSITY-3EIG-20260922`, revision `2026-09-22.5`  
Assignment: `Bilinear block mechanism`  
Method: complementary constructions / source-valid stress families  
Outcome: **ESSENTIAL_STEP_APPLIED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The full conjecture remains open. No moment, support, centering, identical-law, log-concavity, or post-rotation independence assumption is used below. The argument is entirely in original-coordinate product geometry. It does not use probability squaring or convert a square-root small-ball estimate back to the target scale.

## First unpaid implication, stated up front

The new analytic/algebraic step reduces the B09 debt to the following structural routing statement.

`QFORM-EXTERNAL-SMOOTHER-PACKET-OR-OVERLAPPING-OPERATOR-ROUTING-v2`: from the bare hypothesis `s_3(A)>=1`, product-preservingly expose at least one of

1. a three-bank scalar compression whose Schur complement across one disjoint scalar bank is a nondegenerate pure hyperbolic pair (Theorem 4 below);
2. two quantitatively strong disjoint hyperbolic packets (the completed designated-partner theorem account03/B09 r19 applies);
3. an already-paid definite/ridge/triangle/physical-pair exit;

or isolate a genuinely overlapping higher-rank curvature operator that admits none of these product-compatible packets and must be estimated without conditioning its third direction away.

The important new point is that branch 1 needs **no separate lower bound on the external square coefficient**. The scalar spectral gap itself forces exactly the coefficient product required by the bilinear/square smoothing estimate.

## Sources and corrections consumed

Fresh brain control was read at `yspennstate/math-research-brain@a8293374154bdde63ae77be6877476933763f51d` and refreshed before publication. OWNER CONTROL is revision `2026-09-22.15`; QFORM remains the sole target. The current state still marks the full theorem open.

The live negative constraints were retained: law-uniform pointwise quadratic-phase decay is false; spectral-fiber suprema can lose dimension; spectral rotations do not preserve independence; the arbitrary-joint 3D coarea bound and positive conditional-projection-density moments are false; one good cross minor or one Schur rank-two extraction is not forced; and overlapping square curvature need not be an external smoother.

The newer Claude synthesis was also consumed from the brain handoff `scheduled_tasks/work/shared/qform-density-2026-09-22/handoffs/interactive/20260922T225732Z-claude-synthesis.md`: its reduction leaves a no-small-physical-pivot class `N3` as a sufficient remaining global target. The theorem below is useful precisely because it works at **aggregate bank scale** and therefore does not require a large physical pivot.

Related completed square-plus-one-hyperbolic smoothing: `yspennstate/math-open-problems@4098649c3810c9c525c6d357b3d2c5417a333f6b:proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260922T182919Z-account03-B02-qform-r12/REPORT.md`. The proof below is self-contained in its narrower pure-Schur-hyperbolic scope and improves the constant there by avoiding an `L^3` interpolation.

For bank compression we use the source-audited Livshyts--Paouris--Pivovarov marginal theorem recorded at `yspennstate/math-open-problems@d85479c4a40760a42120c5b0816e809013acf539:proofnet24/QFORM-density/fleet-2026-09-22/account03/B18/B18-20260922T155856Z-r13/REPORT.md`: a unit linear form in independent cap-one coordinates has density at most `sqrt(2)`.

The designated partner result actually applied below is account03/B09 r19, canonical source `yspennstate/math-open-problems@e8c7ac4f0294a028d4bc883d1e4bf1c805e11085:proofnet24/QFORM-density/fleet-2026-09-22/account03/B09/20260922T224649Z-account03-B09-QFORM-r19/REPORT.md`.

## 1. A one-dimensional half-kernel bound

### Lemma 1 — capped density against `|x-c|^{-1/2}`

If a real random variable `X` has probability density bounded by `N`, then, uniformly in `c`,

`E |X-c|^(-1/2) <= 2 sqrt(2N).`                                           (1)

Proof. Among functions `0<=f<=N` of mass one, the integral against the symmetric decreasing kernel `|x-c|^{-1/2}` is maximized by `f=N` on the centered interval of length `1/N`. Therefore

`int |x-c|^(-1/2) f(x) dx
 <= N * 2 int_0^(1/(2N)) u^(-1/2) du
 =2 sqrt(2N).`

No moment or support assumption enters. `QED`

## 2. Bilinear half-Riesz smoothing from conditional linear anti-concentration

### Lemma 2 — pure hyperbolic residual

Let `U,V` be independent real random variables with density caps `N_U,N_V`, let `a!=0`, and let `b,c,e` be arbitrary real numbers. Put

`R=2aUV+bU+cV+e.`                                                        (2)

Then

`boxed: sup_t E |R-t|^(-1/2)
 <= 4 sqrt(2) sqrt(N_U N_V) / sqrt(|a|).`                                (3)

Proof. Completing the bilinear rectangle gives

`R=2a (U+c/(2a))(V+b/(2a)) + e'`.                                       (4)

Translations preserve independence and density caps. Write the translated variables as `U',V'`. For fixed `U'=u!=0`, the dependence on `V'` is linear, so Lemma 1 (equivalently the density cap under a linear map) gives

`E[ |uV'-s|^(-1/2) | U'=u ]
 <= 2 sqrt(2N_V) |u|^(-1/2).`                                           (5)

A second application of Lemma 1 to `U'` gives

`sup_s E |U'V'-s|^(-1/2) <= 8 sqrt(N_U N_V).`                            (6)

Scaling by `2a` turns (6) into (3). The null event `U'=0` causes no difficulty because `U'` has a density. `QED`

This is the exact conditional-linear step requested by the B09 card. It is an averaged fractional estimate, not a squared-probability decoupling.

## 3. A genuinely disjoint external square converts (3) into an `L^infinity` density

### Theorem 3 — `QFORM-HYPERBOLIC-EXTERNAL-SQUARE-v1`

Let `U,V,W` be mutually independent real random variables with density caps `N_U,N_V,N_W`. Let `a,d` be nonzero and let all affine parameters be arbitrary. Define

`Q = 2aUV+bU+cV + d (W+alpha U+beta V+gamma)^2 + e.`                     (7)

Then `Q` has an essentially bounded density and

`boxed: ||p_Q||_infinity
 <= 4 sqrt(2) N_W sqrt(N_U N_V) / sqrt(|a d|).`                          (8)

Consequently every interval `L` satisfies

`P{Q in L} <= [4 sqrt(2) N_W sqrt(N_U N_V)/sqrt(|ad|)] |L|.`             (9)

Proof. Condition on `(U,V)`. For every deterministic center `m`, the density of `d(W+m)^2` is bounded on its supporting half-line by

`p(y) <= N_W / [sqrt(|d|) sqrt(|y|)].`                                  (10)

Indeed the two inverse branches have Jacobians `2 sqrt(|d y|)` and each input density is at most `N_W`. Therefore, for every `t`,

`p_Q(t)
 <= N_W |d|^(-1/2) E |t-(2aUV+bU+cV+e)|^(-1/2).`                        (11)

Lemma 2 gives (8), and integrating over an interval gives (9). `QED`

The square center may overlap the two hyperbolic variables arbitrarily through `alpha,beta`. What is essential is that the scalar `W` itself comes from a genuinely disjoint source bank; this avoids the previous B09 overlapping-square counterexample in which no independent third smoother survived.

## 4. Spectral gap automatically pays the coefficient product

The analytic bound (8) appears to require a structural lower bound on `|ad|`. In the exact three-scalar Schur geometry this lower bound is automatic.

Let the quadratic coefficient matrix of (7), before affine terms, be

`G = [[d alpha^2, a+d alpha beta, d alpha],
      [a+d alpha beta, d beta^2, d beta],
      [d alpha, d beta, d]].`                                            (12)

The Schur complement of the last scalar pivot `d` is exactly

`E = [[0,a],[a,0]].`                                                      (13)

Hence

`det G = -a^2 d`,                                                        (14)

and the upper-left `2x2` principal block of `G^(-1)` is

`E^(-1)=[[0,1/a],[1/a,0]].`                                              (15)

### Lemma 4 — `QFORM-HYPERBOLIC-SCHUR-GAP-PRODUCT-v1`

If `sigma_min(G)>=s>0`, then

`boxed: |a d| >= s^2.`                                                    (16)

Proof. Put `H=G^(-1)`. Then `||H||_op<=1/s`. Let its ordered eigenvalues be `h_1<=h_2<=h_3`. By Cauchy interlacing applied to the principal block (15), whose eigenvalues are `-1/|a|` and `1/|a|`,

`-1/|a| <= h_2 <= 1/|a|`,

so `|h_2|<=1/|a|`; also `|h_1|,|h_3|<=1/s`. Therefore

`|det H| <= 1/(|a| s^2).`                                                (17)

But (14) gives `|det H|=1/(|a|^2 |d|)`. Comparing with (17) yields (16). `QED`

Combining Theorem 3 and Lemma 4 gives the direct scalar bound

`boxed: ||p_Q||_infinity
 <= 4 sqrt(2) N_W sqrt(N_U N_V) / s.`                                    (18)

In particular, for three independent original scalar cap-one coordinates,

`boxed: ||p_Q||_infinity <= 4 sqrt(2)/s.`                                (19)

### Theorem 4 — `QFORM-THREE-BANK-HYPERBOLIC-SCHUR-GAP-v1`

Let `I,J,K` be pairwise disjoint original-coordinate banks. Let `u,v,w` be unit vectors supported on the respective banks and set

`U=<u,X_I>`, `V=<v,X_J>`, `W=<w,X_K>`.

Assume that, after conditioning only further disjoint outside coordinates, all active quadratic dependence factors through `(U,V,W)`, its `3x3` scalar matrix has the form (12), and `sigma_min(G)>=s>0`. Arbitrary conditioned affine terms in `U,V,W` are allowed.

Then, for every product input law with original coordinate densities at most one,

`boxed: ||p_Q||_infinity <= 8 sqrt(2)/s.`                                (20)

Thus every interval `L` obeys

`boxed: P{Q in L} <= (8 sqrt(2)/s)|L|.`                                  (21)

Proof. The three bank projections are mutually independent and each has density cap at most `sqrt(2)` by the source-audited product-marginal theorem. Insert `N_U=N_V=N_W=sqrt(2)` into (18). Conditional outside coordinates only change affine parameters and output translations, so averaging preserves (20). `QED`

For the target scale `s=1`, the constant is `8sqrt(2)<11.314`.

This is an aggregate-bank statement: it does not require any one physical coordinate inside the `W` bank to have a large diagonal coefficient.

## 5. Target-valid stress family: the external square coefficient may vanish

A separate lower bound on the scalar square coefficient `d` is false even under a unit three-eigenvalue gap in this exact Schur geometry.

Fix `epsilon>0` and set

`c_e=(epsilon+sqrt(epsilon^2+4))/2`,
`a_0=1/epsilon`, `d_0=epsilon`,
`alpha=1/(sqrt(2)epsilon)`, `beta=-1/(sqrt(2)epsilon)`.

The unscaled matrix (12) is

`G_0 = [[1/(2epsilon), 1/(2epsilon), 1/sqrt(2)],
        [1/(2epsilon), 1/(2epsilon),-1/sqrt(2)],
        [1/sqrt(2),   -1/sqrt(2),    epsilon]].`                         (22)

Its characteristic polynomial factors exactly as

`-(epsilon lambda-1)(epsilon lambda-lambda^2+1)/epsilon`,                (23)

so its eigenvalues are

`1/epsilon`, `c_e`, `-1/c_e`.                                            (24)

Scale the whole form by `c_e`. The resulting matrix `G_e=c_e G_0` has eigenvalues

`c_e/epsilon`, `c_e^2`, `-1`,                                           (25)

and therefore satisfies the target spectral threshold exactly. Yet its external-square coefficient is

`d_e=c_e epsilon ->0`,                                                    (26)

while its hyperbolic Schur coefficient is `a_e=c_e/epsilon` and

`a_e d_e=c_e^2>=1`.                                                       (27)

Thus paying `1/sqrt(|d|)` by itself would diverge on a perfectly target-valid family, whereas the correct product `|ad|` remains paid. Theorem 3 yields the uniform scalar bound

`||p_Q||_infinity <=4sqrt(2)/c_e <=4sqrt(2)`.                            (28)

The same compressed matrix on three disjoint unit-projection banks is bounded by `8sqrt(2)/c_e`. This stress family is a regression test for any proposed pivot-only extraction lemma.

The earlier B09 diffuse family `2UV+W^2` is the special case `a=d=1`, `alpha=beta=0`; the present theorem improves its previous bank bound from `16sqrt(60)` to `8sqrt(2)`.

## 6. Designated partner result applied to an actual target inequality

The latest completed designated partner account03/B09 r19 proves `QFORM-FOUR-BANK-HYPERBOLIC-CONVOLUTION-v1`: for four mutually independent scalar bank projections and two bilinear packets, the product singularity is in `L^2`, so two such independent packets convolve to `L^infinity`; for unit original-coordinate bank projections with aggregate strengths `s_1,s_2`,

`||p_(2aUV+2bWR+affine)||_infinity <=16/sqrt(s_1 s_2).`                  (29)

Apply this to four disjoint unit-projection banks and

`T=2UV+2WR.`                                                              (30)

Its compressed coefficient matrix is the direct sum of two hyperbolic `2x2` blocks and has spectrum

`{-1,-1,1,1}`.                                                           (31)

Thus it is an actual target-valid form. Here `s_1=s_2=1`, and the designated partner theorem gives

`boxed: ||p_T||_infinity <=16`,
`boxed: P{T in L} <=16 |L|.`                                             (32)

This partner exit is complementary to Theorem 4: (32) pays a second disjoint hyperbolic packet, while Theorem 4 pays a disjoint scalar square whose center may strongly overlap the first hyperbolic pair.

## 7. Connection to the newest no-pivot synthesis and remaining debt

The newest synthesis reduces the global proof to a class in which all physical diagonal entries and physical `2x2` principal determinants are small. Theorem 4 does not contradict that geometry and does not require escaping it by a physical pivot: the three active scalars may each be diffuse projections over large disjoint banks, with every individual physical coefficient tending to zero.

What remains is therefore structural, not analytic, in this branch. Starting from the actual three-large-eigenvalue matrix, one must either extract the gapped scalar Schur pattern (12)-(13), extract two independent hyperbolic packets as in the designated-partner theorem, route to another completed branch, or prove a new estimate for the strongly overlapping operator left after all such packet extractions fail.

No claim is made that the bare spectral hypothesis already forces Theorem 4's scalar factorization. No claim of full continuity is made for arbitrary outside mixtures; (20)-(21) establish essential boundedness in the stated conditional scope.

## Status

- Full QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- New proved analytic lemma: `QFORM-HYPERBOLIC-EXTERNAL-SQUARE-v1`.
- New proved exact algebraic bridge: `QFORM-HYPERBOLIC-SCHUR-GAP-PRODUCT-v1`.
- New target-level branch: `QFORM-THREE-BANK-HYPERBOLIC-SCHUR-GAP-v1`, density constant `8sqrt(2)/s`.
- Designated partner account03/B09 r19 applied at the target-valid inequality `2UV+2WR`, giving density at most `16`.
- Interval dependence: exactly `O(|L|)`.
- Square-root decoupling: not used.
- Post-rotation independence: not used.
- First unpaid implication: `QFORM-EXTERNAL-SMOOTHER-PACKET-OR-OVERLAPPING-OPERATOR-ROUTING-v2`.
