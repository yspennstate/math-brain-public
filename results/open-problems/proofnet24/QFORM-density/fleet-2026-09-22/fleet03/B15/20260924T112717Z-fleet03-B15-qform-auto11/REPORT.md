SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B15, 2026-09-24T11:27:17Z.
attacking: independent verification and exact quantitative packaging of full-target qualitative C0 regularity, reconciling the stale continuity status while preserving the open universal-height problem.

# fleet03/B15 — full-target qualitative C0 closure and explicit fixed-matrix certificate

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T112717Z-fleet03-B15-qform-auto11`  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: `FULL_TARGET_C0_QUALITATIVE_PROVED / FIXED_MATRIX_HEIGHT_CERTIFICATE_PROVED / PARTNER_ROUGH_CLOSURE_APPLIED / UNIVERSAL_HEIGHT_OPEN`.

## 1. Exact contribution and status correction

The owner target is still OPEN at its central quantitative step: there is not yet a proved universal finite constant `C` valid simultaneously for every target matrix and every cap-one product law.

This run independently checks and packages a different statement which is already latent in completed fleet work but is stale in the shared `CLAIMS.json`:

> **Theorem A (`QFORM-TARGET-C0-QUALITATIVE-v1`).** Let `A` be any fixed real symmetric matrix with `rank(A)>=3`, let `b in R^n`, `c in R`, and let `X_1,...,X_n` be independent with arbitrary measurable probability densities `0<=f_i<=1`. Then
> 
> `q(X)=X^T A X+b^T X+c`
> 
> has a unique continuous density representative `p_q in C_0(R)`. Moreover it has a finite matrix-dependent height bound. Thus every instance in the owner's three-large-eigenvalue class already has a continuous density. What remains open is uniformity of the height over all such matrices/laws, not qualitative continuity.

The newest owner continuation itself says that fixed-matrix `C_0` regularity is proved and that it does not supply the missing universal height. The shared `CLAIMS.json` entry `QFORM-CONTINUOUS-REPRESENTATIVE=OPEN` is therefore stale at the qualitative full-target scope and should be consolidated by B20/owner after this source-pinned audit. This worker does not mutate protected shared claims.

A second quantitative packaging gives an explicit finite certificate for each fixed matrix.

Let

`C_3=2*pi+3*sqrt(3)` and `C_4=4*pi+8`,

and define

`K_*(A)=min { C_3/sigma_min(A_[I,I]) : |I|=3, det A_[I,I]!=0 ; C_4/sigma_min(A_[I,I]) : |I|=4, det A_[I,I]!=0 }`,

with nonexistent terms omitted. Then `K_*(A)<infinity` for every `rank(A)>=3`, and

`boxed( p_q in C_0(R),  ||p_q||_infinity <= K_*(A). )`            (1.1)

This is **not** a candidate universal solution: `K_*(A)` can diverge along diffuse target families even when `s_3(A)>=1`.

## 2. Absolute continuity is strictly easier

For reference, the existence of some density needs neither rank three nor product structure. Let the joint input law on `R^n` be absolutely continuous and let

`q(x)=x^T A x+b^T x+c`

be nonconstant. Then

`grad q(x)=2Ax+b`.

Its critical set is empty or an affine translate of `ker A`; for a nonconstant affine quadratic this is a proper affine subspace and hence Lebesgue-null. If `N subset R` is one-dimensional Lebesgue-null, define

`E_k=q^{-1}(N) intersect {|x|<=k, |grad q(x)|>=1/k}`.

Coarea gives

`integral_(E_k) |grad q(x)| dx = integral_N H^{n-1}(E_k intersect q^{-1}(t)) dt =0`,

hence `|E_k|=0`. The inverse image of `N` is contained, modulo the null critical set, in `union_k E_k`, so it is null. Therefore `q(X)` is absolutely continuous.

This says nothing about boundedness or continuity of the density.

## 3. Explicit fixed-matrix essential height

The completed fleet01/B15 theorem at

`yspennstate/math-open-problems@47dc925729bbf269333cc6e1256178a538d2f553`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B15/20260922T120320Z-fleet01-B15-qform/REPORT.md`

contains two ingredients used here.

### 3.1 Principal block selection

Every real symmetric matrix of rank at least three has an invertible principal block of order three or four. The proof is short and worth retaining because it preserves original-coordinate product structure.

Start from a nonsingular principal block `B=A_[I,I]`. If `|I|<rank(A)`, write

`A=[[B,C],[C^T,D]]`

and let `S=D-C^T B^{-1}C`. Since `rank A=|I|+rank S`, `S!=0`. If some `S_jj!=0`, adjoining coordinate `j` gives determinant `det(B)S_jj!=0`. If all `S_jj=0`, some `S_jk!=0`, and adjoining `j,k` gives a nonsingular `2x2` Schur block `[[0,S_jk],[S_jk,0]]`. Starting from a nonzero diagonal `1x1` block, or from a nonzero off-diagonal `2x2` block if every diagonal vanishes, reaches order three or four.

Hence the set defining `K_*(A)` is nonempty.

### 3.2 Uniform affine finite-block interval bounds

For an invertible physical `3x3` symmetric block `B`, the completed fleet02/B15 theorem at

`yspennstate/math-open-problems@d5392d73398e2811f58b612fb8f191aa79d8ee5e`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T110507Z-fleet02-B15-qform-pivot-r1/REPORT.md`

proves for every affine quadratic in three independent cap-one original coordinates

`P{Y^T B Y+2ell^T Y+d in J} <= (C_3/sigma_min(B)) |J|`.          (3.1)

For an invertible physical `4x4` block, fleet01/B15 proves

`P{Y^T B Y+2ell^T Y+d in J} <= (C_4/sigma_min(B)) |J|`.          (3.2)

Both estimates are uniform in the affine vector and constant. They use a near/far physical-coordinate decomposition, not an arbitrary-joint coarea height lemma and not post-rotation independence.

Choose a block `I` attaining `K_*(A)`. Condition on every original coordinate outside `I`. The active coordinates remain independent with their original cap-one densities, while all outside cross terms become a deterministic affine term. Therefore (3.1) or (3.2) gives, for every conditioner,

`P{q(X) in J | X_(I^c)} <= K_*(A)|J|`.

Averaging yields

`boxed( P{q(X) in J} <= K_*(A)|J| )`                              (3.3)

for every interval `J`.

Thus every fixed rank-at-least-three matrix has a finite essential density height with an explicit certificate.

## 4. Latest designated partner applied to an actual inequality

The newest completed designated partner result is fleet04/B15 run

`20260924T111654Z-fleet04-B15-rough-interval-closure-r4`,

scientific commit

`yspennstate/math-open-problems@0ba4f7d74b9b06d689c5a540b228a31cf9833043`.

Its rough interval closure theorem says: if `mu_m -> mu` in total variation and every approximating law obeys the same interval inequality `mu_m(J)<=M|J|`, then `mu(E)<=M|E|` for every Borel set and the rough limit has essential density cap `M`. This statement is purely measure-level and does not infer continuity from boundedness.

Apply it here to the actual fixed-matrix inequality. Let

`f_(i,m)=f_i * eta_m`

for a nonnegative smooth approximate identity. Then

`0<=f_(i,m)<=1`, `integral f_(i,m)=1`, and `||f_(i,m)-f_i||_1 ->0`.

The product input densities converge in `L^1` by telescoping, hence the affine-quadratic output laws `mu_m` converge to `mu` in total variation. The same physical block `I` and (3.1)/(3.2) give

`mu_m(J) <= K_*(A)|J|`                                           (4.1)

for every `m` and every interval. The partner theorem applied to (4.1) therefore gives for the original arbitrary rough inputs

`mu(E) <= K_*(A)|E|`                                             (4.2)

for every Borel set, hence

`||p_q||_(infinity,ess) <= K_*(A)`.                              (4.3)

This is a genuine equation-level application of the current partner result. It separates the rough measure passage from the stronger QFORM-specific continuity theorem below.

## 5. Independent audit of full fixed-matrix C0 regularity

The structural `C_0` theorem is obtained by exhausting the two physical-coordinate classes.

### 5.1 Some physical diagonal is nonzero

The completed fleet03/B15 theorem at

`yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T153101Z-fleet03-B15-r12/REPORT.md`

proves that every rank-at-least-three symmetric matrix with some `A_jj!=0` has `C_0` output for arbitrary cap-one product laws. The high-dimensional argument selects an invertible physical principal block of order three or four containing that pivot and conditions on all other original coordinates.

For the finite block, after Schur decomposition at the nonzero scalar pivot one writes

`T=R(U)+b(Z+M(U))^2`.

The residual `R` has an `L^3` density. In the coupled branch the map `(R,M)` is absolutely continuous away from a null one-dimensional critical set, and convolution with the independent pivot coordinate produces a joint kernel `K(r,z)` satisfying

`K(r,.) in C_0`, `0<=K(r,z)<=p_R(r)`.

The exact square-root density formula is controlled near its moving endpoint by Holder against `p_R in L^3`; away from the endpoint, dominated convergence gives continuity. A local `L^3` tail argument gives vanishing at infinity. The bound is uniform in affine terms generated by outside conditioning, so averaging the conditional `C_0` kernels preserves continuity and vanishing.

I rechecked the key structural points: the critical set of `(u^T S u,v^T u)` is `S^{-1}(span v)`, which is null in dimensions two/three; the envelope `K<=p_R` follows from `f_Z<=1`; and the endpoint singularity `|t-r|^{-1/2}` is integrable against the `L^3` residual with the stated `L^(1/6)` near-scale gain.

### 5.2 Every physical diagonal is zero

The completed fleet02/B15 theorem at

`yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B15/20260922T200544Z-fleet02-B15-qform-r11/REPORT.md`

closes the complementary class. I rechecked both branches rather than importing its conclusion only by name.

#### Triangle branch

Suppose the support graph contains a triangle, so after conditioning outside three vertices the active polynomial has

`2axy+2bxz+2cyz+ell_1 x+ell_2 y+ell_3 z+d`, `abc!=0`.

For fixed `z`, translate the two original independent coordinates:

`U=x+(c/a)z+ell_2/(2a)`,
`V=y+(b/a)z+ell_1/(2a)`.

Then the polynomial is

`2aUV+H(z)`,

and direct expansion gives the quadratic coefficient of `H` equal to `-2bc/a`, which is nonzero.

If one active marginal is changed by an `L^1` amount `delta`, the absolute marginal difference is a subdensity of mass `delta`. The product-density bathtub estimate gives the conditional variation kernel

`Phi_delta(s)=4 log(1+(1/2)sqrt(delta/|s|))`.                     (5.1)

For a random variable satisfying

`P{|W|<=rho} <= min(1,L sqrt(rho))`,                              (5.2)

layer-cake/integration by parts gives

`E Phi_delta(W) <= Omega(L sqrt(delta))`,                         (5.3)

where

`Omega(a)=2a log(1+2/a)+4 log(1+a/2)`, `Omega(0)=0`.

For the quadratic `W=(t-H(Z))/(2a)`, the cap-one source law and the exact quadratic preimage length give (5.2) with

`L=2sqrt(2)|a|/sqrt(|bc|)`.

Hence each active-marginal perturbation has a sup-norm output modulus tending to zero with `delta`; outside-marginal changes cost their `L^1` distance times a common affine-uniform core height. Cap-preserving smooth product approximants therefore yield a uniformly Cauchy sequence of `C_0` output densities, whose limit is the rough output density.

I independently checked the integral in (5.3): with `Psi(r)=4log(1+1/(2sqrt r))`, `-Psi'(r)=2/[r(2sqrt r+1)]`; substituting `x=sqrt r` reduces the expectation bound to

`integral_0^infinity min(1,a x) 4/[x(2x+1)] dx`

which splits at `x=1/a` and equals exactly the displayed `Omega(a)`.

#### Triangle-free branch

If the zero-diagonal support graph is triangle-free, choose a nonzero edge `{i,j}` with weight `a`. The physical pair

`P=[[0,a],[a,0]]`

is invertible. Its Schur complement on the other coordinates is nonzero because `rank A>=3`; triangle-freeness forces its diagonal to vanish, so some off-diagonal entry `S_kl` is nonzero. The principal four-block on `{i,j,k,l}` is invertible. A triangle-free four-vertex graph is bipartite, and invertibility rules out a `1+3` split, so after permutation the block is

`B=[[0,C],[C^T,0]]`, `C in GL_2`.

Conditioning outside this block adds only affine terms, removable by translating the two original-coordinate pairs. For fixed `u`, the density of `2u^T C V` is bounded by

`1/(sqrt(2)||C^T u||) <= 1/(sqrt(2) sigma_min(C)|u|)`.

If `F` is a planar subdensity with `0<=F<=1` and mass `delta`, the planar bathtub principle gives

`integral F(u)/|u| du <= 2 sqrt(pi delta)`.

Consequently changing any active marginal by `L^1` amount `delta` changes the output density by at most

`sqrt(2*pi*delta)/sigma_min(C)`,                                  (5.4)

while outside-marginal changes are linear in `L^1` against the finite conditional core height. Again smooth cap-preserving approximants converge uniformly in output density, so the rough output lies in `C_0`.

The two zero-diagonal graph branches exhaust that physical class. Together with Section 5.1 they prove Theorem A.

## 6. Same-height pointwise conclusion and the logical separation

From Section 4, the output law is dominated by `K_*(A) dt`, so any density version satisfies `p<=K_*(A)` almost everywhere. From Section 5 the same law has a continuous representative `p in C_0`. If `p(t_0)>K_*(A)` at some point, continuity gives a nonempty interval on which `p>K_*(A)`, contradicting the interval/Borel domination. Hence

`boxed( ||p||_infinity <= K_*(A) )`

pointwise for the canonical continuous representative. No regularity constant is lost.

This does **not** say that bounded density alone implies continuity. For example, with independent `X,Y~Unif[0,1]`, `X^2+Y^2` has a bounded density with a jump at the left endpoint; no point assignment repairs that jump. Continuity here is a separate theorem using the quadratic/product structure.

Conversely, once any future proof establishes the owner-wide interval estimate

`P{X^T A X in J} <= C|J|`                                        (6.1)

with a universal `C` under `s_3(A)>=1`, Theorem A immediately gives for every target instance a canonical

`p_Q in C_0(R),  ||p_Q||_infinity <= C`.                          (6.2)

Thus the owner's stronger continuous-density request requires **no additional universal modulus of continuity** after the central universal height theorem is proved. The qualitative `C_0` theorem already exists instancewise.

## 7. Quantifier ledger

Under the exact owner hypotheses `s_3(A)>=1`, rank is at least three, so Theorem A applies to every target matrix, every dimension, every sign pattern, every additional spectrum, and every independent cap-one measurable marginal. No Gaussian, moment, compact-support, connected-support, log-concavity, or post-rotation independence assumption is used.

What is proved:

- every nonconstant affine quadratic pushforward of an absolutely continuous joint law is absolutely continuous;
- every fixed rank-at-least-three QFORM product instance has a canonical `C_0` density;
- every such fixed instance obeys the explicit finite pointwise height certificate (1.1);
- rough input passage preserves the same fixed-matrix interval constant by the newest fleet04/B15 total-variation closure theorem;
- if the future universal interval theorem has constant `C`, the desired continuous representative has the same `C` with zero loss.

What remains open:

- no uniform bound on `K_*(A)` follows from `s_3(A)>=1`;
- diffuse matrices can make every selected physical `3x3/4x4` block poorly conditioned, so a universal proof must aggregate product-coordinate curvature before paying reciprocal local-minor costs;
- no target-uniform modulus of continuity is claimed or needed for the logical closure;
- no valid counterexample to the universal height conjecture is produced here.

The central full QFORM universal-constant conjecture remains **OPEN**.
