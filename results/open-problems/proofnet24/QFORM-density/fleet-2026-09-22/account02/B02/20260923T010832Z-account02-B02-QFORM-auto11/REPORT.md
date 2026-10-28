SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-23T01:08:32Z.
attacking: the Integrated Fourier high-volume-coloop collar; independently audit the new fractional-volume constants, then combine sharp D'/D5 with the latest account03/B02 endpoint without selecting a local minor.

# account02/B02 — adaptive sharp-HY volume compiler, D5 tail extraction, and a near-coloop row deletion

Programme: `QFORM-DENSITY-3EIG-20260922`.  
Run: `20260923T010832Z-account02-B02-QFORM-auto11`.  
Full target: **OPEN / NOT PROVED / NOT DISPROVED**.  
Execution label: `WITHOUT_VERIFIED_BRAIN`; repository retrieval plus the worker-owned prior memory snapshot were actually consumed, but no native learned-memory receiver state is claimed.

The full target remains: independent original real coordinates with scalar densities at most one, arbitrary real symmetric `A` having at least three eigenvalues of modulus at least one, and one dimension/law/matrix-independent essential density bound for `X^T A X`. Nothing below assumes moments, bounded support, log-concavity, independence after a spectral rotation, or a diagonal input basis.

## 1. Sources actually consumed


`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

in `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`: `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

I also read the later sharp-Hausdorff--Young review

`yspennstate/math-open-problems@9844891a9fbe96a65e37f71122bf0300b53dcc80:proofnet24/QFORM-density/interactive/20260922T220600Z-claude-review/REVIEW.md`

and, as explicitly requested by the later owner continuation, the new volume-stability package

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba:proofnet24/QFORM-density/interactive/20260923T002323Z-volume-stability/{REPORT.md,PEER_TAIL_EXTENSION.md}`.

The latest compatible designated-partner result is `account03/B02` r18,

`yspennstate/math-open-problems@99fb7a9461b77e83cc900042eefa33d4f2ef9913:proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T000148Z-account03-B02-QFORM-r18/REPORT.md`.

I also use its immediately preceding exact-rank-three physical-cross-block theorem at commit
`484c89f85cda352b2c4318364a6206ebc4154950`.

Live corrections were refreshed before publication. In particular I preserve `QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1`, `QFORM-ANCHOR-PACKET-ONE-LOCAL-MINOR-FALSE-v1`, `QFORM-TWOBANK-NONZERO-LEAKAGE-RANK3-CROSS-UNIFORM-FALSE-v1`, and the partner's `QFORM-MIXED-SKELETON-DETERMINANT-ONLY-L1-FALSE-v1`. The arguments below keep determinant/volume mass aggregated and retain original-coordinate product provenance.

## 2. Independent analytic check of the new fractional-volume theorem — PASS

Let `M=A[I,J]` be an original-coordinate cross block, let

`Z=e_3(M^T M)>0`,

and let `alpha_i,beta_j` be the row/column inclusion marginals under squared `3x3`-minor volume sampling. Thus `sum alpha=sum beta=3`. After the standard original-coordinate decoupling,

`|phi_Q(t)|^2 <= E_D product_i |psi_i(2t(MD)_i)| =: E F_t`.

For `q>=1`, Jensen gives `E F_t <= (E F_t^q)^(1/q)`. The volume-sampling Brascamp--Lieb determinant estimate gives the Gaussian constant

`Z^(-1/2) product_i alpha_i^(-alpha_i/2) product_j (1-beta_j)^(-(1-beta_j)/2)`.

For a row with `alpha_i>0`, sharp Hausdorff--Young at output exponent `q/alpha_i` is available exactly when `alpha_i<=q/2`. With the Fourier convention of the source package,

`|| |psi_i(2t .)|^q ||_(1/alpha_i)`

`<= (pi/|t|)^alpha_i (alpha_i/q)^(alpha_i/2) (1-alpha_i/q)^(-(q-alpha_i)/2)`.

The `alpha_i` powers cancel the Brascamp--Lieb normalization. Since

`-(1-x) log(1-x) <= x` for `0<=x<=1`,

both row and column entropy products cost at most `e^(3/2)`. Therefore

`E F_t^q <= e^3 q^(-3/2) (pi/|t|)^3 Z^(-1/2)`.

Consequently

`|phi_Q(t)| <= min(1,K |t|^(-b))`,

where

`b=3/(2q)`,
`K=[e^3 q^(-3/2) pi^3 Z^(-1/2)]^(1/(2q))`.

For `b>1`,

`int_R min(1,K|t|^(-b)) dt = 2b K^(1/b)/(b-1)`.

Dividing by `2pi` gives exactly

**(2.1)**
`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`

for

`1<=q<3/2`, `max_i alpha_i<=q/2`.

Verdict: **PASS** for the assigned analytic scope. The equality gate `alpha_i=q/2` is legal: the corresponding scalar Hausdorff--Young output exponent is exactly two, so Plancherel is the endpoint. The strict endpoint is `q<3/2`, because at `q=3/2` the time exponent becomes exactly one. Rows with `alpha_i=0` and columns with `beta_j=1` are continuous/drop-factor endpoints of the same determinant inequality and do not require division by zero.

For `q=4/3`, (2.1) is

`||p_Q||_inf <= (9 sqrt(3) e/2) Z^(-1/6)`

with coefficient `21.1869100628...`. The perturbative calculation in the source report is also correct: if `M=M0+E`, `s_3(M0)>=a`, `max diag P_range(M0)<=1/2`, and `||E||op<=a/16`, then `s_3(M)>=15a/16`, the row-volume gate is below `2/3`, and the reported bound `(24 sqrt(3)e)/(5a)<23/a` follows.

## 3. New result I: adaptive projection gate improves the perturbation endpoint

The source proof actually contains more room than the fixed choice `q=4/3` uses.

Let `P` be an orthogonal projection on the row index space, put

`ell_i=P_ii`, `kappa=s_3(M)`, `epsilon=||(I-P)M||op`,

and

`rho := sqrt(3) epsilon/kappa`.

The source marginal matrix estimate gives

`sqrt(alpha_i) <= sqrt(ell_i)+rho sqrt(1-ell_i)`.

If `max ell_i<=1/2` and `rho<=1`, the right side is increasing on `[0,1/2]`, hence

`max_i alpha_i <= (1+rho)^2/2`.

The coefficient in (2.1) is increasing in `q` for `q>=1`, so the cheapest admissible choice is

`q=(1+rho)^2`.

It is integrable precisely while

`(1+rho)^2<3/2`, i.e.

`rho < rho_* := sqrt(3/2)-1 = 0.22474487139158894...`.

Substitution in (2.1) gives the adaptive theorem

### Theorem 3.1 — `QFORM-ADAPTIVE-SHARP-HY-VOLUME-v1`

If

`max_i P_ii<=1/2`,
`rho=sqrt(3)||(I-P)M||op/s_3(M) < sqrt(3/2)-1`,

then the full quadratic form, with arbitrary same-bank quadratic terms and arbitrary outside couplings, has a continuous density and

**(3.1)**
`||p_Q||_inf <= C(rho) e_3(M^T M)^(-1/6)`,

where

`C(rho)=3e / [(1+rho)(1-4rho-2rho^2)]`.

No post-rotation independence is used; `P` enters only a deterministic matrix inequality.

For `M=M0+E` with `s_3(M0)>=a`, `max diag P_range(M0)<=1/2`, and `theta=||E||op/a`, we have `kappa>=(1-theta)a` and

`rho <= sqrt(3) theta/(1-theta)`.

Thus the actual perturbative endpoint of this argument is

`theta < theta_* := rho_*/(sqrt(3)+rho_*) = 0.11485351986824861...`.

A clean rational corollary is

**(3.2)**
`||E||op<=a/10  =>  ||p_Q||_inf < 48.670/a`.

Indeed then `rho<=sqrt(3)/9`, `q=(1+sqrt(3)/9)^2=1.4219372165...`, the coefficient in (3.1) is `43.8027621437...`, and `s_3(M)>=0.9a`.

This enlarges the proved perturbation window from `a/16` to `a/10`. It is a scope improvement, not an exhaustive structural theorem.

## 4. New result II: an ungated D5 compiler from tail stable rank

The reviewed sharp-HY calculation has a useful general `k`-volume form. If `Z_k=e_k(M^T M)>0`, `q>=1`, `max alpha_i^(k)<=q/2`, and `k>2q`, the same calculation gives

**(4.1)**
`||p_Q||_inf <= e q^(-1/2) [k/(k-2q)] Z_k^(-1/(2k))`.

For `k=5`, take `q=2`. Every volume marginal is at most one, so the gate is automatic and

**(4.2)**
`||p_Q||_inf <= (5e/sqrt(2)) e_5(M^T M)^(-1/10)`

with coefficient `9.6105775704...`. This is an unweighted `L^1` characteristic-function theorem and hence yields a continuous density.

Now write the squared singular values of `M` as

`lambda_1>=lambda_2>=lambda_3>=...>=0`,

put

`T=sum_(j>=3) lambda_j`, `m=lambda_3`, `R=T/m` when `m>0`.

The quantity `R` is the stable rank of the singular-value tail beginning at the third direction.

### Lemma 4.1 — exact cap-concentration lower bound for tail third volume

For nonnegative numbers `x_j<=m` of sum `T=Rm`, let `k=floor(R)` and `vartheta=R-k`. Then

**(4.3)**
`e_3(x) >= [binom(k,3)+vartheta binom(k,2)] m^3`.

Proof. Hold all coordinates except two fixed. With their sum fixed, `e_3` has the form

`x y S_rest + (x+y)e_2(rest)+e_3(rest)`.

The only variable term is `xy S_rest`, with nonnegative coefficient. It is minimized by pushing one of the two coordinates to the boundary `0` or `m`. Repeating leaves `k` coordinates equal to `m`, at most one coordinate equal to `vartheta m`, and all others zero. Evaluating `e_3` there proves (4.3).

For `R>2`, define

`F_3(R)=[binom(k,3)+(R-k)binom(k,2)]/R^3 >0`.

Then the tail satisfies `e_3(lambda_3,lambda_4,...)>=F_3(R)T^3`. Since the positive terms of `Z_5` that contain the first two singular directions already contribute

`lambda_1 lambda_2 e_3(lambda_3,lambda_4,...)`,

we obtain:

### Theorem 4.2 — `QFORM-D5-TAIL-STABLERANK-v1`

If `R=T/lambda_3>2`, then

**(4.4)**
`||p_Q||_inf <= (5e/sqrt(2)) F_3(R)^(-1/10) (s_1 s_2)^(-1/5) T^(-3/10)`.

There is **no leverage or marginal condition** in (4.4). Same-bank quadratic curvature and all outside couplings are arbitrary.

This identifies a clean meaning of the surviving “effective-rank-at-most-four collar”: from the viewpoint of a live cross block, a tail with stable rank strictly above two automatically creates enough fifth exterior volume for D5. What remains difficult is the quantitatively small/low-stable-rank tail, not a high-cardinality diffuse tail by itself.

### Actual application to the newest source stress family

`PEER_TAIL_EXTENSION.md` considers

`M=U diag(1,1,N^(-1/2),...,N^(-1/2)) U^T`,

with `N=m-2` weak singular directions. Here `s_1=s_2=1`, `T=1`, `R=N`, and already

`Z_5 >= binom(N,3)/N^3`.

Therefore the sharp D5 route gives

**(4.5)**
`||p_Q||_inf <= (5e/sqrt(2)) [binom(N,3)/N^3]^(-1/10)`.

For the source's explicit no-pivot choice `m=512`, `N=510`, this is

**(4.6)**
`||p_Q||_inf < 11.504`.

Thus that stress sequence is paid even without the projection gate, and with a smaller constant than the source's convenient `9sqrt(3)e/2=21.187`. The source D' tail theorem remains useful in the two-direction-plus-small-tail regime where fifth volume can be tiny or zero.

## 5. New result III: delete a heavy four-volume row before paying D'

The direct sharp-HY `k=4` theorem has a constant that blows up as a four-volume row marginal tends to one. The near-coloop can instead be paid by deleting the heavy physical row and using the third-volume resource that its star forces.

Let

`Z_4=e_4(M^T M)>0`,

and let `h_i` be the row inclusion probability under squared `4x4`-minor volume sampling. Write `r_i` for row `i` of `M`, and let `N=M[-i,:]` be the physical block after deleting that original-coordinate row.

By Cauchy--Binet, `h_i Z_4` is the sum of squared four-row wedges containing `r_i`. For every row triple `S` of `N`,

`||r_i wedge r_S||^2 <= ||r_i||^2 ||r_S||^2`.

Summing gives the aggregate inequality

**(5.1)**
`h_i Z_4 <= ||r_i||^2 e_3(N^T N)`.

No single minor is selected.

Suppose the third-volume row marginals of `N` are all at most `q/2` for some `1<=q<3/2`. Condition on the deleted original coordinate. The conditional quadratic form has the same physical cross block `N`; every new term is merely an arbitrary same-bank/affine phase, so (2.1) applies uniformly. Combining it with (5.1) yields:

### Theorem 5.1 — `QFORM-4VOL-HEAVY-ROW-DELETE-DPRIME-v1`

**(5.2)**
`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] ||r_i||^(1/3) h_i^(-1/6) Z_4^(-1/6)`.

Since `||r_i||<=s_1(M)` and

`Z_4>=s_1^2 s_2^2 s_3^2 s_4^2`,

this simplifies to

**(5.3)**
`||p_Q||_inf <= [3e/((3-2q)sqrt(q))] h_i^(-1/6) (s_2 s_3 s_4)^(-1/3)`.

In particular, if

`h_i>=3/4` and the deleted block `N` has all third-volume row marginals at most `2/3`,

then `q=4/3` gives

**(5.4)**
`||p_Q||_inf < 22.228 (s_2 s_3 s_4)^(-1/3)`.

This removes the `1/(1-h_i)` blow-up of the direct D4 compiler on a substantial near-coloop branch.

## 6. Designated partner applied at the exact coloop endpoint

The preceding theorem still uses a D' gate after deletion. At the exact coloop endpoint that gate is unnecessary, because the completed `account03/B02` exact-rank-three theorem applies directly.

If `h_i=1`, then

`e_4(N^T N)=(1-h_i)Z_4=0`.

Since `Z_4>0`, `rank(M)>=4`; deleting one row changes rank by at most one, so necessarily

`rank(M)=4`, `rank(N)=3`.

Thus `N` is an **exact rank-three physical cross block**. The partner theorem at commit `484c89f85cda352b2c4318364a6206ebc4154950` gives

`||p_Q||_inf <= 6 e_3(N^T N)^(-1/6)`

with a continuous density and with arbitrary self blocks/outside couplings retained. Using (5.1) with `h_i=1` gives the actual new inequality

### Corollary 6.1 — `QFORM-4VOL-EXACT-COLOOP-PARTNER-CLOSURE-v1`

**(6.1)**
`||p_Q||_inf <= 6 ||r_i||^(1/3) Z_4^(-1/6)`

and hence

**(6.2)**
`||p_Q||_inf <= 6 (s_2 s_3 s_4)^(-1/3)`.

This is an equation-level use of the designated partner, not a citation-only handoff. It also shows that an exact four-volume coloop is not itself the obstruction; the hard collar is genuinely **near** coloop plus a concentrated third-volume residue.

I also consumed the partner's newer r18 theorem at commit `99fb7a9461b77e83cc900042eefa33d4f2ef9913`. On the exact-rank-two span-aligned endpoint

`q(z,x,y)=d z^2+2z(a^T x+b^T y+c)+F(x)+G(y)+2x^T B y`,

`a in Col(B)`, `b in Row(B)`, `Delta=s_1(B)s_2(B)`, `kappa=b^T B^+ a`,

its Schur-gap branch gives the actual inequality

**(6.3)**
`|d-kappa|>=|d|/3  =>  ||p_q||_inf <=16 |d|^(-1/2) Delta^(-1/4)`.

The complementary mixed-skeleton determinant branch is **not** declared paid: the same partner run supplied the admissible Gaussian counterexample showing that a nonzero mixed-skeleton determinant alone does not force unweighted `L^1` after arbitrary same-bank curvature is discarded.

## 7. Compatibility with fresh corrections

The new results deliberately avoid the live failures.

- `QFORM-PROJECTION-CAP-NONZERO-PIVOT-BARRIER-v1` shows that an arbitrary projected two-dimensional density cap cannot by itself be fed through a nonlinear pivot. The proofs here instead apply D'/D5 directly to original product-coordinate banks through decoupling and Brascamp--Lieb. Corollary 6.1 conditions only an original coordinate before invoking the partner's original-product cross-block theorem.
- `QFORM-ANCHOR-PACKET-ONE-LOCAL-MINOR-FALSE-v1` forbids extracting one good local minor from aggregate mass. Equations (4.3)--(5.3) keep the entire elementary-symmetric/wedge mass aggregated.
- `QFORM-TWOBANK-NONZERO-LEAKAGE-RANK3-CROSS-UNIFORM-FALSE-v1` forbids turning merely nonzero leakage into a uniform third singular scale. Corollary 6.1 assumes an actual exact-rank-three row-deleted block and keeps its measured exterior volume.
- `QFORM-MIXED-SKELETON-DETERMINANT-ONLY-L1-FALSE-v1` is retained exactly. I use only the r18 Schur-gap branch and leave its critical mixed branch open.

No law-uniform pointwise Fresnel decay is asserted anywhere.

## 8. Deterministic checks

Independent scalar recomputation gives

`rho_*=0.22474487139158894`,
`theta_*=0.11485351986824861`,
`C(sqrt(3)/9)=43.8027621437`,
`C(sqrt(3)/9)/0.9=48.6697357152`,
`9sqrt(3)e/2=21.1869100628`,
`(9sqrt(3)e/2)(4/3)^(1/6)=22.2275064943`,
`5e/sqrt(2)=9.6105775704`.

On 30 seeded random `6x6` matrices, direct minor enumeration verified the wedge inequality (5.1); the largest observed ratio `(h_i Z_4)/(||r_i||^2 Z_3(N))` was `0.79344<1`. On 10,000 seeded random capped tail vectors, the ratio `e_3(x)` divided by the concentration lower bound (4.3) was always at least one; the smallest observed ratio was `1.000051`. These finite checks are regressions only; the displayed exterior-algebra and pairwise-compression arguments are the proofs.

## 9. First unpaid implication after this run

The new hierarchy removes three pieces of the previous high-volume-coloop collar:

1. diffuse near-rank-three cross blocks through the adaptive sharp-HY theorem (3.1);
2. tails with enough fifth exterior volume, quantitatively including every tail stable-rank `R>2` once the local singular scales are controlled, through (4.4);
3. a heavy four-volume row whose deletion leaves a D'-admissible third-volume block, and the exact coloop endpoint with no gate, through (5.2)--(6.2).

The sharpened first unpaid interface is therefore:

**`QFORM-NESTED-COLOOP-OR-CRITICAL-RANK2-GLOBAL-THIRD-v1` — OPEN.**

On a quantitatively useful physical cut, handle the nested concentration chain in which a four-volume row is near-coloop **and**, after deleting it, the residual third-volume measure is itself concentrated; in the low-tail exact-rank-two endpoint, handle the r18 critical alignment by combining the genuinely global third spectral/grouped-coordinate resource **before** taking absolute values. A valid bridge must preserve original product-coordinate provenance and aggregate volume/star mass; it cannot select one vanishing local minor, replace a projected law by an arbitrary bounded joint density, or spend the mixed-skeleton determinant after same-bank curvature has been discarded.

No target-valid counterexample to the full universal bounded-density conjecture was found. No target-valid counterexample to the stronger target-wide unweighted criterion `int |phi_Q(t)| dt<infinity` was found either; that stronger criterion remains open at full scope.
