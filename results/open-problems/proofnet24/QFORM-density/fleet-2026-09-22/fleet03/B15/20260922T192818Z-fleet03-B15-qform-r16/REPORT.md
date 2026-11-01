# QFORM B15 r16 — quantitative product-marginal stability and rough-input continuity

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Worker:** `fleet03/B15`  
**Run:** `20260922T192818Z-fleet03-B15-qform-r16`  
**Status:** `ESSENTIAL_STEP_APPLIED / CANDIDATE_FULL_ROUGH-CONTINUITY / UNIVERSAL_HEIGHT_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact target and what is proved here

The central conjecture remains OPEN: for independent real coordinates with probability densities `0<=f_i<=1` and a real symmetric `A` with at least three eigenvalues of modulus at least one, one still needs one matrix- and dimension-independent finite constant `C` with

`||p_{X^T A X}||_infinity <= C`.

This run addresses the separate stronger regularity request. It proves a quantitative stability theorem for the entire physical zero-diagonal class. Combined with the already completed B15 nonzero-diagonal theorem, it gives the following candidate target-level regularity conclusion, pending independent review:

> **Candidate theorem.** For every real symmetric `A` with `rank(A)>=3` and every product law with independent one-dimensional probability densities bounded by one, `Q=X^TAX` has an essentially bounded density with a representative in `C_0(R)`.

The bound furnished here is matrix-dependent. Therefore this theorem does **not** solve the universal-height conjecture.

The important new ingredient is an explicit `L^1`-input to `L^infinity`-output modulus for the two physical zero-diagonal geometries. It is strong enough to transfer the assigned partner's smooth-output `C_0` theorem to arbitrary measurable cap-one marginals without assuming input continuity.

## 2. Source-corrected premises actually used

I re-read the live state and corrections at `math-research-brain@f9c9de562645a66900820391f4959519d09842d0`. In particular I do **not** use the refuted arbitrary-joint rank-three coarea estimate, the refuted conditional positive-moment estimate, pointwise law-uniform van der Corput decay, independence after spectral rotation, or fiber-supremum dimension-free claims.

Assigned partner actually applied:

- `fleet04/B15`, `yspennstate/math-open-problems@07672b7beb8f867c7a7b973aa3157a42ae506460`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B15/20260922T152333Z-b15-qform-continuous-envelope-r3/REPORT.md`.

That result proves `C_all=C_C0=C_sm`, and its source chain supplies cap-preserving compactly supported smooth approximants of arbitrary one-dimensional cap-one marginals; every all-smooth target output has a `C_0` density. I apply those approximants to the explicit stability inequalities below.

For the complementary nonzero-physical-diagonal branch I use my completed prior theorem:

- `fleet03/B15`, `yspennstate/math-open-problems@d73760eb784a86c356c64f05dd92f84655618f02`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B15/20260922T153101Z-fleet03-B15-r12/REPORT.md`.

It proves `p_Q in C_0(R)` whenever `rank(A)>=3` and some original-coordinate diagonal entry is nonzero. Its proof retains product structure through a Schur kernel and does not use the later-refuted arbitrary-joint coarea gate.

## 3. A product-variation kernel

Let `h,g` be nonnegative measurable functions on `R` with `0<=h<=1`, `integral h=delta`, `0<=g<=1`, `integral g=1`. For `s!=0`, the subdensity of the product of independent variables with these densities is

`k(s)=integral h(u)g(s/u)du/|u|`.

Define

`Phi_delta(s)=4 log(1+(1/2)sqrt(delta/|s|))`, `s!=0`,

and set `Phi_delta(0)=+infinity`.

### Lemma 3.1

For every `s!=0`, `k(s)<=Phi_delta(s)`.

### Proof

Fix `r>0`. On `|u|>=r`, use `g<=1`. Among cap-one subdensities of mass `delta`, the integral of `1/|u|` over this exterior set is maximized by filling the two intervals adjacent to `+r` and `-r`; concavity of `log` makes the optimal mass split equal. Thus

`integral_{|u|>=r} ... <=2 log(1+delta/(2r))`.

On `|u|<r`, substitute `v=s/u`, so `du/|u|=dv/|v|`, use `h(s/v)<=1`, and perform the same bathtub argument for the cap-one probability density `g`. This gives

`integral_{|u|<r} ... <=2 log(1+r/(2|s|))`.

Choose `r=sqrt(delta|s|)`. The two terms coincide and give the claim. QED.

## 4. Exact quadratic averaging of the kernel

Let `W` satisfy

`P(|W|<=rho)<=min(1,L sqrt(rho))` for all `rho>0`.

Put

`Omega(a)=2a log(1+2/a)+4 log(1+a/2)` for `a>0`, and `Omega(0)=0`.

### Lemma 4.1

For every `delta>=0`,

`E Phi_delta(W) <= Omega(L sqrt(delta))`.

Hence the right side tends to zero as `delta->0`, with order `sqrt(delta) log(1/delta)`.

### Proof

For `delta>0`, scale `R=|W|/delta` and let `a=Lsqrt(delta)`. With

`Psi(r)=4log(1+1/(2sqrt(r)))`,

we have `-Psi'(r)=2/[r(2sqrt(r)+1)]`. The small-ball estimate excludes an atom at zero and integration by parts gives

`E Psi(R)<=integral_0^infinity min(1,a sqrt(r)) 2/[r(2sqrt(r)+1)]dr`.

Set `x=sqrt(r)`. The integral is

`integral_0^infinity min(1,ax) 4/[x(2x+1)]dx`.

Splitting at `x=1/a` evaluates it exactly as

`2a log(1+2/a)+4log(1+a/2)=Omega(a)`. QED.

A direct quadrature check at `a=0.01,0.1,1,10` agrees with this closed form to numerical precision; the displayed integration is the proof.

## 5. Triangle branch: explicit marginal stability

Assume a zero-diagonal physical `3x3` block contains a triangle. After relabeling, its homogeneous part is

`q(x,y,z)=2a xy+2b xz+2c yz`, with `abc!=0`.

Conditioning on all outside coordinates adds only affine terms `ell_1x+ell_2y+ell_3z+d`; every bound below is uniform in them. For fixed `z`, put

`U=x+(c/a)z+ell_2/(2a)`,

`V=y+(b/a)z+ell_1/(2a)`.

Then the polynomial is `2aUV+H(z)`, where `H` is quadratic with coefficient `-2bc/a`.

Compare two admissible `x`-marginals with `delta_x=||f_x-g_x||_1`. Their absolute difference is a cap-one subdensity of mass `delta_x`. Lemma 3.1 therefore bounds the conditional output-density difference by

`(1/(2|a|)) Phi_{delta_x}((t-H(z))/(2a))`.

The variable `W=(t-H(Z))/(2a)` is quadratic in the independent original coordinate `Z` with quadratic coefficient magnitude `|bc|/a^2`. For a cap-one one-dimensional density, the inverse image of an interval of length `2rho` under `alpha(z-z0)^2+d` has length at most `2sqrt(2rho/|alpha|)`. Consequently

`P(|W|<=rho)<=L_xy sqrt(rho)`,

`L_xy=2sqrt(2)|a|/sqrt(|bc|)`.

Lemma 4.1 yields

`boxed( ||p_f-p_g||_infinity <= omega_xy(delta_x) )`,

`omega_xy(delta)=[1/(2|a|)] Omega(L_xy sqrt(delta))`.

The same modulus holds for replacing the `y`-marginal. To replace `z`, use the pair `(x,z)` and obtain

`omega_xz(delta)=[1/(2|b|)] Omega([2sqrt(2)|b|/sqrt(|ac|)]sqrt(delta))`.

All these moduli tend to zero.

Taking `delta=1` in the same estimate gives a finite affine-uniform conditional core height

`M_T=[1/(2|a|)]Omega(2sqrt(2)|a|/sqrt(|bc|))`.

Therefore replacing any outside marginal changes the full density by at most

`M_T ||f_j-g_j||_1`,

because after conditioning on outside coordinates the triangle conditional density is uniformly bounded by `M_T`.

## 6. Triangle-free zero-diagonal branch: bilinear block and square-root modulus

Suppose `diag(A)=0`, the physical support graph has no triangle, and `rank(A)>=3`.

Choose a nonzero edge `{i,j}`. The `2x2` pivot `P=[[0,A_ij],[A_ij,0]]` is invertible, and its Schur complement `S` has `rank(S)=rank(A)-2>=1`. Triangle-freeness forces `S_kk=-2A_kiA_kj/A_ij=0` for every remaining `k`. Hence some off-diagonal `S_kl` is nonzero. The principal block on `{i,j,k,l}` is invertible because its Schur complement relative to `P` is `[[0,S_kl],[S_kl,0]]`.

The four-vertex support graph is triangle-free, hence bipartite; invertibility forces a `2+2` bipartition. After permutation,

`B=[[0,C],[C^T,0]]`, with `C in GL_2(R)`.

Conditioning outside this block creates affine terms; invertibility of `C` removes them by translations of the two original-coordinate pairs, leaving `2U^TCV` up to an output translation.

For fixed `u`, the Rogozin--Ball scalar projection estimate gives the conditional density in the independent pair `V` at most

`1/(sqrt(2)||C^Tu||)`.

If `F` is any planar subdensity with `0<=F<=1` and mass `delta`, the planar bathtub principle gives

`integral F(u)/|u|du <=2sqrt(pi delta)`.

Therefore replacing any one of the four block marginals at `L^1` distance `delta` changes the output density by at most

`boxed( sqrt(2pi delta)/sigma_min(C) )`.

At `delta=1` this yields the affine-uniform conditional block bound

`M_B=sqrt(2pi)/sigma_min(C)`.

Replacing any outside marginal hence changes the full density by at most `M_B||f_j-g_j||_1`.

## 7. Assigned-partner application: arbitrary zero-diagonal rough outputs are C_0

Fix zero-diagonal `A` with `rank(A)>=3` and arbitrary cap-one independent marginals `f_1,...,f_n`.

Using the cap-preserving smooth-approximation source chain consumed by fleet04/B15, choose compactly supported smooth cap-one probability densities `f_i^(m)` with `||f_i^(m)-f_i||_1->0`. Let `p_m` be the all-smooth quadratic output density. The assigned partner theorem supplies `p_m in C_0(R)`.

If the graph contains a triangle, telescope the marginals. For its three coordinates use the Section 5 moduli and for every outside coordinate use the `M_T` Lipschitz estimate:

`||p_m-p||_infinity <= omega_xy(delta_x,m)+omega_xy(delta_y,m)+omega_xz(delta_z,m)+M_T sum_{j outside}delta_j,m ->0`.

If the graph is triangle-free, use the bilinear block:

`||p_m-p||_infinity <= [sqrt(2pi)/sigma_min(C)] sum_{j in block}sqrt(delta_j,m)+M_B sum_{j outside}delta_j,m ->0`.

This is the actual partner application: the partner supplies `C_0` smooth outputs, while the new inequalities give **uniform**, not merely total-variation, convergence to the rough output.

The product input laws converge in total variation, so their pushforwards do as well; thus the uniform limit is indeed a density of the original `Q`. Because `C_0(R)` is closed under uniform convergence,

`boxed( diag(A)=0, rank(A)>=3 => p_Q in C_0(R) cap L^infinity(R). )`

The bound is finite for each fixed matrix but is not universal.

## 8. Candidate complete rough-continuity theorem

The prior B15 report at `d73760eb784a86c356c64f05dd92f84655618f02` proves the complementary branch

`rank(A)>=3` and `some A_jj!=0 => p_Q in C_0(R) cap L^infinity(R)`.

Together with Section 7, this gives, pending independent review,

`boxed( rank(A)>=3 => p_{X^TAX} has a C_0 representative and finite instance-dependent L^infinity norm. )`

Thus the stronger continuity request would hold for every target instance, since three eigenvalues of modulus at least one imply rank at least three.

This is strictly separate from the universal-height conjecture. The constants above contain local quantities such as `1/|a|`, `1/sqrt(|bc|)` and `1/sigma_min(C)`; the nonzero-diagonal proof likewise uses a selected physical block. Diffuse valid matrices can make such local constants arbitrarily poor. Hence no matrix-independent `C` follows.

## 9. First unpaid implication and next recipient

The regularity conclusion now needs an independent end-to-end check before the shared claim `QFORM-CONTINUOUS-REPRESENTATIVE` is promoted. Primary recipient: `fleet04/B15`, with special attention to the product-kernel bathtub bound, the exact `Omega` integral, and the four-variable Schur graph reduction.

For the main conjecture, the unpaid step is unchanged: aggregate original-coordinate product structure before paying reciprocal local-minor costs. The new continuity theorem removes a regularity side issue but does not solve near-degenerate/diffuse universal height.

## 10. Integrity ledger

- Full universal QFORM constant: **OPEN / NOT PROVED**.
- Essential boundedness for each fixed rank-`>=3` matrix: candidate proof across the two physical diagonal cases, with matrix-dependent constants.
- Rough-input continuous representative: candidate full proof from this report plus the prior nonzero-diagonal theorem; independent review pending.
- No Gaussian, moment, compact-support, connected-support, log-concavity, spectral-coordinate independence, or input-density continuity assumption was added.
- No refuted arbitrary-joint coarea, conditional positive-moment, pointwise van-der-Corput, or fiber-supremum lemma was used.
