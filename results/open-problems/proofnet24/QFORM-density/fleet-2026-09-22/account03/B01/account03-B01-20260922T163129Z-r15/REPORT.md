# QFORM account03/B01 — translation-uniform rank-two half-Riesz theorem

Programme: `QFORM-DENSITY-3EIG-20260922`  
Current control revision at pre-publication refresh: `2026-09-22.7`  
Run: `account03-B01-20260922T163129Z-r15`  
Assignment: `Oscillatory replacement`  
Status: `PROVED_SUPPORTING_THEOREM / FULL_TARGET_OPEN / WITHOUT_VERIFIED_BRAIN`

## 1. Target and why this run changes the live proof boundary

The full target remains open: for arbitrary dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix with at least three eigenvalues of modulus at least one, prove one universal finite essential bound for the density of `Q=X^T A X`, or give a target-valid counterexample. Continuity is a separate requested conclusion.

The current proof-first owner continuation explicitly identifies a missing `rank-two half-Riesz theorem for arbitrary projection orientation` as a priority. This report proves such a theorem. It is translation-uniform, dimension-free, and has no row-leverage restriction. It therefore removes the mixed-leverage obstruction from the **rank-two residual** in the existing rank-three Schur branch. It does not solve the zero/near-zero physical-pivot branch, nor the higher-rank structural reduction, so it is not a full proof.

All live corrections are preserved. In particular, no law-uniform pointwise scalar Fresnel decay is assumed: phase-aligned fragmented supports still refute that premise. No post-rotation independence, compact support, moments, log-concavity, Gaussianity, or connected support are used.

## 2. Two one-dimensional singular-integral lemmas

### Lemma 2.1 — conditional square half-kernel

Let `F` be a probability law on `R` with density `f<=1`. For every nonzero real `s`,

`int |x^2-s|^(-1/2) f(x) dx <= 4 sqrt(2) |s|^(-1/4)`.       (2.1)

Proof. If `s=r^2>0`, then on `x>=0`,

`|x^2-r^2|^(-1/2) <= r^(-1/2)|x-r|^(-1/2)`.

For every subprobability density bounded by one,

`int |x-a|^(-1/2)g(x)dx <= 2sqrt(2)`,                       (2.2)

because the decreasing rearrangement is maximized by filling an interval of length one centered at `a`. Apply (2.2) separately on the positive and negative half-lines to obtain `4sqrt(2)r^(-1/2)`.

If `s=-r^2<0`, use `x^2+r^2>=2r|x|` and (2.2) at `a=0`; this gives the stronger bound `2r^(-1/2)`, hence (2.1). QED.

The exceptional value `s=0` is intentionally excluded: the kernel can then be nonintegrable. In the conditional application below, the equation producing `s=0` has probability zero because the conditioning variable has a density.

### Lemma 2.2 — uniform quadratic negative quarter moment

If `Y` has a probability density bounded by one, then for every `c in R`,

`E |Y^2-c|^(-1/4) <= 4`.                                      (2.3)

Proof. For every `delta>0`, elementary interval geometry gives

`Leb{x: |x^2-c|<delta} <= 4 sqrt(delta)`                       (2.4)

for all real `c`: for `c>=delta` it is two annuli with total length `2(sqrt(c+delta)-sqrt(c-delta))`; for `0<=c<delta` it lies inside `(-sqrt(c+delta),sqrt(c+delta))`; for `c<0` it is empty unless `|c|<delta`, in which case it lies in an interval of length at most `2sqrt(delta)`.

Thus

`P(|Y^2-c|<delta) <= min(1,4sqrt(delta))`.

Layer cake with `delta=s^(-4)` yields

`E|Y^2-c|^(-1/4)`
` = int_0^infinity P(|Y^2-c|<s^(-4)) ds`
` <= int_0^infinity min(1,4s^(-2)) ds = 4`.                  (2.5)

QED.

## 3. Dependence-safe binary half-Riesz lemma

### Lemma 3.1 — `QFORM-CONDITIONAL-BINARY-HALFRIESZ-v1`

Let `Z` have a density bounded by `M`, and suppose the conditional law of `V|Z=z` has a density bounded by `L` for almost every `z`. No independence between `V` and `Z` is required. If `a,b` are nonzero reals, then

`sup_t E |aV^2+bZ^2-t|^(-1/2)`
` <= 16sqrt(2) (LM)^(1/2) |ab|^(-1/4)`.                     (3.1)

Proof. Set `X=LV`, `Y=MZ`. Then the conditional density of `X|Y` is at most one and the marginal density of `Y` is at most one. After factoring `|a|/L^2`, the remaining expression has the form

`X^2 + sigma rho^2 Y^2 - A`,

where `sigma in {+1,-1}` and

`rho^2=|b|L^2/(|a|M^2)`.

Condition on `Y`. Except on a null set, the scalar parameter in Lemma 2.1 is nonzero, so

`E_X |X^2+sigma rho^2Y^2-A|^(-1/2)`
` <=4sqrt(2)|A-sigma rho^2Y^2|^(-1/4)`.

Factor `rho^2` and apply Lemma 2.2 to `Y`; this gives at most `16sqrt(2)rho^(-1/2)`. Restoring the outer factor `L/sqrt(|a|)` gives exactly (3.1). QED.

This lemma is the key dependence-safe replacement: it requires only one bounded marginal and one bounded conditional density, rather than independence of the two square variables.

## 4. Main theorem: every exact rank-two quadratic orientation has a uniform half-Riesz bound

Let `H` be a real symmetric matrix of rank exactly two. Write

`H=U Lambda U^T`,

where `U` has two orthonormal columns and `Lambda` is invertible symmetric `2x2`. Put

`Delta=|det Lambda|`,

and let `X` have independent coordinates, each with probability density bounded by one. Define

`R=X^T H X`.

Let `C_RV` denote the universal one-dimensional bounded-density projection constant from the Rudelson--Vershynin projection theorem already source-transferred in the QFORM archive: every normalized linear form in independent cap-one coordinates has density at most `C_RV`.

Define

`C_H=4^(3/4) 3^(1/4)+(4/3)^(3/4) <4.964`,

and

`C_* = max{ C_H sqrt(3e), 16*2^(3/4) C_RV^(1/2) }`.          (4.1)

### Theorem 4.1 — `QFORM-RANK2-TRANSLATION-HALFRIESZ-v1`

For every real `t`,

`boxed( E |R-t|^(-1/2) <= C_* Delta^(-1/4) ).`              (4.2)

The constant is universal and the theorem has **no leverage assumption** on the rows of `U`.

### Proof: diffuse rows

Write `u_i` for the rows of `U` and `c_i=||u_i||^2`, so `sum_i c_i=2`. If `max_i c_i<=1/2`, the already-proved diffuse rank-two averaged theorem gives a density `h` for `R` satisfying

`||h||_3 <= (3e)^(2/3) Delta^(-1/3)`.                       (4.3)

For any probability density `h` with `||h||_3<=N`, split the half-Riesz integral at radius `r`:

`int h(s)|s-t|^(-1/2)ds`
` <= 4N r^(1/6)+r^(-1/2)`.                                  (4.4)

Indeed, Holder on `|s-t|<=r` uses

`int_|u|<=r |u|^(-3/4)du=8r^(1/4)`,

and the tail is bounded by `r^(-1/2)`. Optimizing at

`r=(3/(4N))^(3/2)`

gives

`sup_t int h(s)|s-t|^(-1/2)ds <= C_H N^(3/4)`.              (4.5)

Applying (4.3) yields

`sup_t E|R-t|^(-1/2) <= C_H sqrt(3e) Delta^(-1/4)`,          (4.6)

where `C_H sqrt(3e)<14.174`.

### Proof: a heavy row and nonzero physical quadratic pivot

Assume instead that some row, relabeled `i`, has leverage

`c=||u_i||^2>1/2`.

Let `J` be the remaining coordinates, set

`a=H_ii=u_i^T Lambda u_i`,

and `b=H[J,i]`.

Suppose first `a!=0`. Completing the square gives

`R=aV^2+Y^T S Y`,

`V=X_i+a^(-1)b^T Y`,

`S=H[J,J]-bb^T/a`.                                          (4.7)

Since `H` has rank two, `S` has rank one. More precisely,

`S=kappa w w^T`

for a unit physical vector `w`, with the exact determinant identity

`|a kappa| = c Delta`.                                      (4.8)

To verify (4.8), rotate the two-dimensional spectral coordinate system so that `u_i=(sqrt(c),0)`. Then

`U_J^T U_J=diag(1-c,1)`.

Writing `Lambda=[[alpha,beta],[beta,gamma]]`, one has `a=c alpha`, while

`Lambda - Lambda u_i u_i^T Lambda/a`
` = diag(0, det(Lambda)/alpha)`.

The second column of `U_J` has norm one, hence `kappa=det(Lambda)/alpha=c det(Lambda)/a`, proving (4.8).

Put `Z=w^T Y`. The one-dimensional projection theorem gives `||p_Z||_infinity<=C_RV`. Conditional on `Z`, the variable `V` is a mixture of translates of the original independent variable `X_i`, hence

`||p_(V|Z)||_infinity<=1`.                                  (4.9)

Apply Lemma 3.1 with `L=1`, `M=C_RV`, `b=kappa`. From (4.8),

`sup_t E|R-t|^(-1/2)`
` <=16sqrt(2) C_RV^(1/2)(c Delta)^(-1/4)`
` <=16*2^(3/4) C_RV^(1/2) Delta^(-1/4)`,                   (4.10)

because `c>1/2`.

### Proof: a heavy row with zero physical quadratic pivot

It remains to treat the case `a=0`. Then necessarily `Lambda` is indefinite. We have

`R=2X_i b^T Y+Y^T H[J,J]Y`.                                (4.11)

Condition on `Y` and write `ell=b^T Y`. For a cap-one density,

`int |alpha x+s|^(-1/2)f(x)dx <=2sqrt(2)|alpha|^(-1/2)`.

With `alpha=2ell`, this becomes

`E[|R-t|^(-1/2)|Y] <=2|ell|^(-1/2)`.                        (4.12)

The cross vector has the exact norm

`||b||^2=c Delta`.                                          (4.13)

Indeed,

`||b||^2=u_i^T Lambda(I-u_i u_i^T)Lambda u_i`
`       =u_i^T Lambda^2 u_i-a^2`.

Since `a=0`, Cayley--Hamilton in dimension two gives

`u_i^T Lambda^2 u_i=-(det Lambda)c=c Delta`.

The normalized linear form `Z=ell/||b||` has density at most `C_RV`. For every density bounded by `M`, rearrangement gives

`E|Z|^(-1/2) <=2sqrt(2M)`.

Therefore (4.12)-(4.13) imply

`sup_t E|R-t|^(-1/2)`
` <=4sqrt(2C_RV)(c Delta)^(-1/4)`
` <=4*2^(3/4)C_RV^(1/2)Delta^(-1/4)`,                      (4.14)

which is smaller than the heavy nonzero-pivot constant in (4.10). The diffuse and heavy cases together prove (4.2). QED.

## 5. Rank-three Schur consequence: the residual leverage restriction disappears

The existing exact spectral-Schur identity for a rank-exactly-three form gives the following. Let

`A=U_3 Lambda_3 U_3^T`,

with `U_3` having orthonormal columns and `Lambda_3` invertible. Fix an original coordinate `i`, put

`c=||u_i||^2>0`, `d=A_ii`,

and suppose `d!=0`. Completing the physical coordinate gives

`Q=dV^2+R`,                                                 (5.1)

where the conditional law of `V|R` has density bounded by one, the residual form `R` has rank two on the remaining independent physical coordinates, and

`|pdet(R)| = c |det Lambda_3|/|d|`.                         (5.2)

Theorem 4.1 applies to this residual **for every orientation**, with no max-row-leverage condition. Conditional square disintegration gives

`p_Q(t) <= |d|^(-1/2) E|R-t|^(-1/2)`

for almost every `t`. Hence

`boxed(
 ||p_Q||_infinity
 <= C_* (|d| c |det Lambda_3|)^(-1/4).
 )`                                                         (5.3)

This is `QFORM-RANK3-SCHUR-HALFRIESZ-v1`. It upgrades the preceding B01 Schur branch by removing the residual diffuse/mixed-leverage hypothesis entirely. It proves essential boundedness in its stated branch; continuity is not established by this argument.

## 6. Assigned partner account04/B01 applied to the new inequality

The completed partner theorem `QFORM-SIGNED-FEJER-EXACT-INTERFACE-v1` states that for any probability law `mu`,

`D_T mu(y)=(1/(2pi))int_(-T)^T(1-|t|/T) Re(e^(-ity)phi_mu(t))dt`

obeys

`||p_mu||_infinity = sup_(T>0,y) D_T mu(y)`

when a bounded density exists, and a uniform Fejer cap conversely yields such a density.

Applying that theorem to (5.3) gives the actual averaged-frequency inequality

`boxed(
 sup_(T>0,y) D_T law(Q)(y)
 <= C_* (|d| c |det Lambda_3|)^(-1/4).
 )`                                                         (6.1)

Thus the new translation-uniform half-Riesz result pays the exact signed averaged quantity relevant to the target on the nonzero rank-three Schur branch, rather than demanding false pointwise scalar decay or absolute Fourier `L1`.

Canonical partner source: `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B01/20260922T141507Z-b01-qform-fejer-r1/REPORT.md`.

## 7. Rigorous finite algebra diagnostics

A numerical identity checker was run only as a diagnostic, not as proof:

- 1,800 random orthonormal rank-two frames and invertible symmetric `Lambda` matrices: the Schur identity `kappa=c det(Lambda)/a` agreed to maximum relative error below `1.7e-15`.
- 1,000 exact indefinite constructions satisfying `u^T Lambda u=0`: the identity `||b||^2=c|det Lambda|` agreed to maximum relative error below `7e-16`.

The analytic proofs above are independent of these checks.

## 8. What is now paid and what remains

Paid in this run:

1. a translation-uniform half-Riesz estimate for **every rank-two spectral orientation** under the exact cap-one product hypothesis;
2. a dependence-safe binary square lemma requiring only one marginal density cap plus one conditional density cap;
3. removal of the rank-two residual leverage assumption from the existing nonzero-pivot rank-three Schur branch;
4. direct transfer to the partner's exact signed-Fejer density criterion.

Still unpaid for the full conjecture:

- the `d=0` and quantitatively near-zero physical-pivot branch at rank three;
- an exhaustive product-preserving reduction from a general matrix with at least three large eigenvalues to paid rank-three/ridge/grouped-coordinate branches while retaining arbitrary additional spectrum;
- the separate continuity conclusion in the branches proved here.

The next direct mathematical step is therefore the proof-first owner's second priority: use the new arbitrary-orientation half-Riesz theorem to attack the **zero/near-isotropic physical pivot** without replacing original-coordinate product provenance by a false conditional-independence assertion.

## 9. Sources and integrity


Key proved dependencies used at their exact scope:

- diffuse rank-two `L^3` theorem: `yspennstate/math-open-problems@d54e3a5d40a1d9837d39a1e525781fcf44ec0d9d`, prior account03/B01 averaged-frequency report;
- bounded-density projection theorem source transfer and random-slope proof: `yspennstate/math-open-problems@508b0985ba8bb658a7f6a935af5138a195cb89de`, account01/B01 report;
- assigned signed-Fejer partner: `yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`, account04/B01 report;
- exact rank-three spectral-Schur identity: prior QFORM rank-three archive consumed at its proved scope.

Privacy review: changed-file allowlist is this report only at this commit. Manual narrow scan found no credentials, scheduler IDs, machine paths, private personal material, email content, signed URLs, or unrelated data. No public release, paid call, remote workflow, task mutation, or cross-account authentication occurred. Repository use is not native learned-memory ingestion; status remains `WITHOUT_VERIFIED_BRAIN`.
