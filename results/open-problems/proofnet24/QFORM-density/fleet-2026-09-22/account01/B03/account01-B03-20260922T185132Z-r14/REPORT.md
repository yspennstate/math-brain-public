SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), slot B03, 2026-09-22T18:51:32Z.
attacking: exact square-collision half-Riesz time integration that retains the dependent sum/difference geometry, then reconciliation of the whole-bank rank-two endpoint against the latest fragmentation obstruction.

# account01/B03 r14 — exact square-collision Riesz energy and the genuine rank-two endpoint

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control observed before write:** revision `2026-09-22.11`; QFORM is the sole research target.  
**Assignment:** Decoupled time integral.  
**Classification:** `ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`.  
**Continuous-density conclusion:** not proved by the new square-collision branch; the earlier direct cross-rank >=3 branch does prove continuity in its scope.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact target and current obstruction

The full target remains open: for every dimension, every collection of independent real random variables with one-dimensional probability densities bounded by one, and every real symmetric matrix `A` having at least three eigenvalues of absolute value at least one, prove that `Q=X^T A X` has an essentially bounded density with one universal finite bound, or give a target-valid counterexample. No moment, support, log-concavity, Gaussian, or eigen-coordinate independence assumption is introduced here.

The latest assigned-partner result, account02/B03 run `20260922T182232Z-account02-B03-QFORM-r12`, canonical mathematics

`yspennstate/math-open-problems@e43c2e6afdf2063d5ce3f517d37f066acbda7b12`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T182232Z-account02-B03-QFORM-r12/REPORT.md`,

proves that a fixed-coordinate Tonelli/Hölder/Plancherel closure loses an unbounded fragmentation factor even for `A=I_3`. Its explicit density

`f_N=(1/N) sum_{k=1}^N R_k^{-1} 1_[R_k,2R_k]`, `R_k=L^k`, `L>=4`,

has cap at most one, while the surrogate factors

`T_p=int (f_N*f_N)(u)^(1-1/p) u^(-1/p) du`

grow as `T_p >= c_p N^(1/p)`. Thus a proof cannot take absolute values separately through the sum/difference displacement variable and then pay finitely many such Renyi factors. That correction is accepted, not challenged.

The new result below shows that the corresponding **exact collision Riesz energy stays uniformly bounded**. In other words, the divergence belongs to the majorant, not to the true independent-copy time integral. This is a direct implementation of the partner's proposed repair: retain the joint sum/difference geometry before taking absolute values.

## 2. New theorem: exact square-collision half-Riesz energy

### Theorem `QFORM-SQUARE-COLLISION-RIESZ-v1`

Let `X` have an arbitrary real probability density `f` with

`0<=f<=M < infinity`,

and let `X'` be an independent copy. Then

`E |X^2-X'^2|^(-1/2) <= C_sq M`,

where

`C_sq = 1 + 4 sqrt(2) + 8[log(3/2)+(1/2)log 3]`

`     = 14.295024269030135...`.

Consequently, for every nonzero real `a`, if

`psi_a(t)=E exp(i t a X^2)`,

then the exact independent-copy identity and the one-dimensional Riesz kernel give

`int_R |t|^(-1/2) |psi_a(t)|^2 dt
 <= sqrt(2*pi) C_sq M |a|^(-1/2)`

` <= 35.83231201928728... M |a|^(-1/2)`.

No pointwise oscillatory decay is asserted or used.

### Proof, step 1: a translation-free small-ball bound for the exact collision

By scaling it is enough first to take `M=1`. Put

`D=|X^2-X'^2|`.

For fixed `x` and `epsilon>0`, consider

`E_x(epsilon)={y: |y^2-x^2|<=epsilon}`.

If `|x|<=sqrt(epsilon)`, then

`|E_x(epsilon)| <= 2 sqrt(x^2+epsilon) <= 2 sqrt(2 epsilon)`.

If `|x|>sqrt(epsilon)`, then `E_x(epsilon)` is the union of the two intervals adjacent to `+|x|` and `-|x|`, and its total length is

`2[sqrt(x^2+epsilon)-sqrt(x^2-epsilon)]
 =4 epsilon/[sqrt(x^2+epsilon)+sqrt(x^2-epsilon)]
 <=4 epsilon/|x|`.

Since the conditional law of `X'` has density at most one,

`P(D<=epsilon)
 <=2 sqrt(2epsilon) int_{|x|<=sqrt(epsilon)} f(x)dx
   +4epsilon int_{|x|>sqrt(epsilon)} f(x)/|x| dx`.

The first integral is at most `2sqrt(epsilon)`, so the first contribution is `4sqrt(2) epsilon`.

For the second integral, the decreasing weight `1/|x|` and the constraints `0<=f<=1`, `int f=1` imply by the elementary bathtub principle that the maximum mass is packed as close as possible to `+/-sqrt(epsilon)`. Hence, writing `a=sqrt(epsilon)`,

`int_{|x|>a} f(x)/|x| dx
 <=2 int_a^(a+1/2) dx/x
 =2 log(1+1/(2a)).`

Therefore, for `0<epsilon<=1`,

`P(D<=epsilon)
 <=4sqrt(2) epsilon
   +8epsilon log(1+1/(2sqrt(epsilon))).`                       (2.1)

This estimate treats `D=|(X-X')(X+X')|` as one joint object. It never conditions `X+X'` on `X-X'` or conversely.

### Proof, step 2: layer cake

Using

`E D^(-1/2)=int_0^infinity P(D<s^(-2)) ds`,

bound the part `0<s<1` by one. For `s>=1`, apply (2.1) with `epsilon=s^(-2)`. This gives

`E D^(-1/2)
 <=1+4sqrt(2) int_1^infinity s^(-2)ds
     +8 int_1^infinity s^(-2)log(1+s/2)ds`.

The remaining elementary integral is exact:

`int_1^infinity s^(-2)log(1+s/2)ds
 =log(3/2)+(1/2)log 3`.

Thus `E D^(-1/2)<=C_sq`.

For a density cap `M`, set `Y=MX`. Then `Y` has density at most one and

`|X^2-X'^2|^(-1/2)=M |Y^2-Y'^2|^(-1/2)`,

which proves the stated scaling.

### Proof, step 3: exact time integral

For the Fourier convention used throughout the QFORM project,

`widehat{|x|^(-1/2)}(t)=sqrt(2*pi)|t|^(-1/2)`.

Apply the positive Riesz identity to `a(X^2-X'^2)`, first with a harmless Gaussian cutoff and then pass to the limit. Since the preceding expectation is finite, the limit is legitimate and gives

`E |a(X^2-X'^2)|^(-1/2)
 =(2*pi)^(-1/2) int_R |t|^(-1/2)|psi_a(t)|^2 dt`.

The claimed weighted `L^2` estimate follows.

## 3. Translation-uniform two-square half-Riesz potential

The preceding exact collision energy converts immediately into a translation-uniform potential estimate without any pointwise characteristic-function decay.

### Corollary `QFORM-TWO-SQUARE-HALF-RIESZ-v1`

Let `U,V` be independent real random variables with density caps `M_U,M_V`. For any nonzero real `a,b`, put

`S=aU^2+bV^2`.

Then

`sup_z E|z-S|^(-1/2)
 <= C_sq sqrt(M_U M_V) |ab|^(-1/4).`                           (3.1)

Both signs of `a,b` are allowed.

### Proof

Absolute Fourier inversion for the half-Riesz potential, followed by Cauchy-Schwarz, gives

`E|z-S|^(-1/2)
 <=(2*pi)^(-1/2) int |t|^(-1/2)|psi_a(t) psi_b(t)|dt`

` <=(2*pi)^(-1/2)
    [int |t|^(-1/2)|psi_a(t)|^2dt]^(1/2)
    [int |t|^(-1/2)|psi_b(t)|^2dt]^(1/2).`

Apply Theorem 2 to each factor. The constants `sqrt(2*pi)` cancel exactly, yielding (3.1).

This is the desired integrated, translation-uniform estimate. It is finite even when `a` and `b` have opposite signs, where the density of the two-square form itself can have a logarithmic singularity.

## 4. Linear small-ball scaling after one further independent square

Let `W,U,V` be independent, with density caps `M_W,M_U,M_V`, and let `d,a,b` be nonzero. Put

`T=dW^2+aU^2+bV^2`.

For fixed `S=aU^2+bV^2`, the density of `dW^2` is bounded by

`M_W |d|^(-1/2)|y|^(-1/2)`

on the appropriate half-line. Therefore

`p_T(x)
 <= M_W |d|^(-1/2) E|x-S|^(-1/2)`

and (3.1) yields

`boxed{ ||p_T||_infinity
 <= C_sq M_W sqrt(M_U M_V)
    |d|^(-1/2)|ab|^(-1/4). }`                                  (4.1)

Equivalently every interval `J` satisfies

`P(T in J)
 <= C_sq M_W sqrt(M_U M_V)
    |d|^(-1/2)|ab|^(-1/4) |J|.`                                (4.2)

This is a genuine linear small-ball estimate obtained from an independent-copy time integral. It is a supporting theorem, not the full QFORM theorem.

## 5. Required application of the latest account02/B03 result

Apply Theorem 2 to the partner's fragmented density `f_N`. Their result gives, for example, `T_2(f_N)>=c sqrt(N)`, and more generally proves that every fixed-coordinate Tonelli/Hölder closure of the indicated type pays an unbounded factor.

Nevertheless, if `X_N,X_N'` are iid with this exact same `f_N`, Theorem 2 gives uniformly in `N`

`E |X_N^2-X_N'^2|^(-1/2) <= C_sq`,

and hence

`boxed{
 int_R |t|^(-1/2)
 |E exp(i t X_N^2)|^2 dt
 <= sqrt(2*pi) C_sq <35.833.
}`                                                               (5.1)

Thus the partner's divergent `T_2` majorant can grow like `sqrt(N)` while the exact weighted collision time integral is bounded by an absolute constant. This is an actual inequality-level use of the partner result: it proves quantitatively that the loss occurs specifically when the dependent `(X-X',X+X')` geometry is broken into separate positive factors.

The present mechanism keeps that geometry through the exact set

`{|y^2-x^2|<=epsilon}`

before taking absolute values. It therefore supplies a concrete dependence-safe replacement for that failed finite-pair majorant.

## 6. Reconciliation: the whole-bank rank-two endpoint is already analytically paid

A separate current fleet handoff, account03/B03 run `20260922T182338Z-account03-B03-QFORM-r17`, correctly proves that the **regularized-determinant plus fractional-collision splice** needs at least three residual cross singular directions; at two directions its particular power envelope reaches a logarithmic endpoint. That is a limitation of that splice, not a limitation of the full decoupled-time method.

The earlier B03 theorem, re-read in full this run from

`yspennstate/math-open-problems@3d6fefe9c92674dff38c97ef8a502787ec3426a2`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B03/account01-B03-20260922T144815Z/REPORT.md`,

proves for any disjoint original-coordinate cross bank `B=A[I,J]` of rank `r`, with positive singular-value product `Delta_r`, that

`|phi_Q(t)|^2
 <=min{1,(2*pi)^r |t|^(-r) Delta_r^(-1)}.`                       (6.1)

The proof projects the **entire cross bank** onto its singular spaces and then performs one `2r`-dimensional bilinear Plancherel estimate. It does not form the partner's coordinatewise `T_p` factors. Consequently the latest fragmentation counterexample does not touch (6.1).

At `r=2`, (6.1) gives the exact whole-bank endpoint

`boxed{
 sup_z E|z-Q|^(-1/2) <=8 Delta_2(B)^(-1/4).
}`                                                               (6.2)

In particular, if both nonzero singular values are at least `sigma`, then

`sup_z E|z-Q|^(-1/2) <=8 sigma^(-1/2).`                           (6.3)

After a genuine independent physical square pivot

`Q_total=d(Z+h(W))^2+R(W)`,

if the residual has such a rank-two original-coordinate cross bank, then

`boxed{
 ||p_Qtotal||_infinity
 <=8 |d|^(-1/2) Delta_2(B)^(-1/4)
 <=8 |d|^(-1/2) sigma^(-1/2).
}`                                                               (6.4)

So the current analytic debt should not be phrased as "pay the two-effective-direction whole-bank endpoint": that endpoint is already paid by a dependence-safe argument and survives the newest partner correction. What remains is to **force or aggregate** a quantitative rank-two resource from the bare spectral hypothesis, or else pass to the genuinely rank-one/star/grouped branch.

## 7. Exact remaining implication

The full theorem is not proved. The first unpaid implication is now structural/product-preserving:

> From only `s_3(A)>=1`, derive a dimension-free exhaustive alternative that either (i) produces a direct ridge/cross-rank >=3 certificate, (ii) produces a physical square pivot whose residual has rank-two whole-bank resource with controlled `|d|^2 Delta_2`, or (iii) detects a rank-one/star/grouped geometry and aggregates independent coordinate banks before any reciprocal local-minor payment.

The already source-validated correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` forbids claiming branch (ii) alone. Its hard family

`Q=2 X_0 Y_m+Z_m^2`

has spectrum `{1,-1,1}` but every nonzero scalar pivot leaves only a rank-one star. That family is a mandatory regression test. The new square-collision theorem suggests a possible analytic ingredient for grouped square packets, but it does not itself solve the star geometry or the exhaustive structural alternative.

## 8. Status and provenance

- `QFORM-SQUARE-COLLISION-RIESZ-v1`: proved here.
- `QFORM-TWO-SQUARE-HALF-RIESZ-v1`: proved here.
- Linear small-ball corollary (4.2): proved here.
- Whole-bank rank-two endpoint (6.2): prior B03 theorem re-read and checked against the latest partner obstruction; not a newly claimed theorem.
- Full QFORM target: **OPEN**.
- Full-target continuous density: **OPEN**. The new branch proves an essentially bounded density only in the stated three-independent-square scope.
- Named partner account02/B03 result: consumed and applied quantitatively in (5.1).
- Repository transport is not native learned-memory ingestion: `WITHOUT_VERIFIED_BRAIN`.
