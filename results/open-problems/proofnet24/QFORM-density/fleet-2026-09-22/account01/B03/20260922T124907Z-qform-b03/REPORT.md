# account01/B03 — rank-two averaged cross-cut regularity and a dependent-pivot upgrade

**Run:** `20260922T124907Z-qform-b03`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`, owner revision `2026-09-22.5`  
**Assignment:** `Decoupled time integral`  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING_THEOREMS / FULL_TARGET_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; repository retrieval occurred, but no authenticated native brain receiver/context was used.

## 1. Exact target and fresh dependencies

The full target remains open: for every dimension, independent real coordinates with probability densities bounded by one, and every real symmetric matrix `A` with at least three eigenvalues of absolute value at least one, prove one universal finite `L^infinity` bound for the density of `Q=X^T A X`, or give a genuine counterexample. Continuity is a separate desired conclusion.


- `QFORM-CROSSMINOR-ALONE-FALSE`: rank two cannot be promoted directly to `L^infinity` under arbitrary same-side curvature;
- `QFORM-UNIVERSAL-PI-FALSE-AND-DIFFUSE-BRANCH`;
- `QFORM-TWOSHEET-XRAY-ONLY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`: conditioning one conjugate sum/difference coordinate on the other does not preserve the marginal density cap;
- `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE`: the three-large-eigenvalue hypothesis does not force a single nonzero physical pivot whose Schur complement contains a rank-two disjoint cross block.

The named partner result actually consumed is account02/B03, latest handoff `20260922T124226Z-b03-qform-auto11`, canonical proof `yspennstate/math-open-problems@0d99f085f5378d267057cc5b9bcbf8e53ca494b5:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T124226Z-b03-qform-auto11/REPORT.md`. It proves the conditional-cap correction and therefore rules out an apparently natural independent-copy conditioning step. I also apply the partner's preceding exact overlap-collapse family from `yspennstate/math-open-problems@27f37883345691606e91d38e9bcfeaa9d6d5af28:proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260922T121352Z-b03-qform-auto11/REPORT.md` to the new inequality in Section 5.

A second source-backed input used in Section 4 is account01/B11, `yspennstate/math-open-problems@2279571f59ade7a9ec478af1e4818f6c117ac224:proofnet24/QFORM-density/fleet-2026-09-22/account01/B11/QFORM-B11-20260922T121344Z/REPORT.md`, specifically its dependent-square `L^3 -> L^infinity` smoothing lemma.

## 2. Why the mechanism changes at rank two

The exact independent-copy identity is

`|phi_Q(t)|^2 = E exp(i t (X-X')^T A (X+X'))`.

For each physical coordinate, the sum and difference remain dependent. The latest account02/B03 correction gives, already for iid `Uniform[0,1]`,

`||p_{U|V=v}||_infinity = 1/[2(1-|v|)]`,

which diverges at the boundary. More generally the valid conditional cap contains a reciprocal marginal density, and the resulting Renyi-spread factors are not law-uniform. Therefore this run does not condition the `(U_i,V_i)` pairs apart.

Instead, it spends the same `L^2` resource directly in the original product coordinates before any square-root/symmetrization loss. At rank two the resulting time envelope is not `L^1`, but it is `L^q` for every `q>1`. Hausdorff--Young converts that averaged time information into output `L^p` regularity, and a third original-coordinate square pivot can then upgrade `L^3` to `L^infinity` even when the square shift depends on all residual variables.

## 3. Cross-cut Hausdorff--Young ladder

### Theorem 3.1 — `QFORM-CROSSCUT-AVERAGED-LP-v1`

Let `S,T` be disjoint original-coordinate sets. Put `B=A[S,T]` and suppose `rank(B)=r>=2`. Let `s_1,...,s_r` be its nonzero singular values and

`D=prod_{j=1}^r s_j(B)>0`.

For any `q in [1,2]` satisfying `r q>2`, let `p=q/(q-1)`, with `p=infinity` when `q=1`. Then the law of `Q=X^T A X` has a density in `L^p` and

`boxed( ||p_Q||_p <= [2 r q/(r q-2)]^(1/q) D^(-1/(r q)). )`    (3.1)

No restriction is imposed on either same-side principal block, on signs, on outside couplings, on support, or on moments.

If additionally `|S|=|T|=r`, then `D=|det B|` and the factor two disappears:

`boxed( ||p_Q||_p <= [r q/(r q-2)]^(1/q) |det B|^(-1/(r q)). )`  (3.2)

For `r=2,q=3/2` this yields

`boxed( ||p_Q||_3 <= 6^(2/3) D^(-1/3) )`                       (3.3)

for an arbitrary rank-two cut, and for a physical `2 x 2` invertible cross block `C`,

`boxed( ||p_Q||_3 <= 3^(2/3) |det C|^(-1/3). )`                (3.4)

Consequently every interval `I` obeys

`P(Q in I) <= 3^(2/3)|det C|^(-1/3)|I|^(2/3)`                 (3.5)

on the square-block branch. This is deliberately `2/3`-power small-ball control, not the target linear estimate.

### Proof

Condition on all coordinates outside `S union T`. Write `u=X_S`, `v=X_T`. The conditional phase is

`g(u)+2 u^T B v+h(v)+c`,

where `g,h` are arbitrary real quadratic-affine functions. Let `B=U Sigma V^T` be a thin singular-value decomposition with `Sigma=diag(s_1,...,s_r)`.

After completing `U,V` to orthogonal coordinate systems, integrate out the null directions and define the complex marginal amplitudes `a_t(y),b_t(z)`. Their absolute values are bounded by the genuine `r`-dimensional orthogonal marginals of the original product densities. The standard bounded-marginal theorem gives those marginal densities `L^infinity` norm at most `2^(r/2)`; since they have mass one,

`||a_t||_2, ||b_t||_2 <= 2^(r/4)`.

The conditional characteristic function is

`Phi(t)=e^(itc) int int a_t(y)b_t(z) exp(2 i t y^T Sigma z) dy dz`.

Cauchy--Schwarz, the change of variables `xi=-2t Sigma y`, and Plancherel give

`|Phi(t)| <= (2pi)^(r/2) D^(-1/2)|t|^(-r/2)`.

Averaging over the conditioned outside variables preserves the same estimate, hence

`|phi_Q(t)| <= min(1,K |t|^(-r/2)),`
`K=(2pi)^(r/2)D^(-1/2).`                                      (3.6)

Put `t0=K^(2/r)=2pi D^(-1/r)`. For `rq>2`,

`int_R |phi_Q(t)|^q dt`
`<=2[t0+K^q int_(t0)^infinity t^(-rq/2)dt]`
`=2 t0 [rq/(rq-2)]`
`=4pi [rq/(rq-2)] D^(-1/r).`                                  (3.7)

Thus

`||phi_Q||_q <= [4pi rq/(rq-2)]^(1/q) D^(-1/(rq)).`

For the inverse Fourier convention `g(x)=(2pi)^(-1)int exp(-itx)h(t)dt`, interpolation between `L^1 -> L^infinity` and Plancherel gives

`||g||_p <= (2pi)^(-1/q)||h||_q`.

As in the standard distributional Hausdorff--Young identification, since `phi_Q` is a characteristic function in `L^q`, its inverse transform is the density of the underlying probability law. Applying the last inequality to (3.7) proves (3.1).

When `|S|=|T|=r`, no projection theorem is needed: the original block product densities have `L^2` norm at most one. The same calculation has

`K=pi^(r/2)|det B|^(-1/2),`

so `t0=pi|det B|^(-1/r)` and yields (3.2). Setting `r=2,q=3/2` gives (3.3)-(3.5). QED.

### Exact relation to the previous B03 theorem

At `q=1`, Theorem 3.1 is available precisely when `r>=3` and recovers the earlier cross-cut `L^infinity` theorem. At `r=2`, `q=1` is excluded because the time tail is `1/|t|`, exactly matching the logarithmic singularity correction. The new content is to retain that endpoint in averaged form rather than discard it.

## 4. A dependent physical pivot upgrades rank-two `L^3` to linear small-ball scaling

### Theorem 4.1 — `QFORM-SCHUR-CROSS2-DEPENDENT-SQUARE-v1`

Choose an original coordinate `k` with

`d=A_kk !=0`.

Write, after relabeling,

`A=[[d,b^T],[b,C0]]`

and let

`S0=C0-bb^T/d`

be the Schur complement. Suppose `S0` has disjoint original-coordinate sets `I,J` whose cross block `S0[I,J]` has rank two, with nonzero singular product `D>0`. Then `Q=X^TAX` has an essentially bounded density satisfying

`boxed( ||p_Q||_infinity <= 4 sqrt(6) |d|^(-1/2) D^(-1/4). )`  (4.1)

If `I,J` are each exactly two coordinates and `delta=|det S0[I,J]|`, the sharper square-block constant is

`boxed( ||p_Q||_infinity <= 4 sqrt(3) |d|^(-1/2) delta^(-1/4). )`  (4.2)

Hence on this certificate branch

`P(Q in L) <= 4 sqrt(6)|d|^(-1/2)D^(-1/4)|L|`

for every interval `L`. This recovers the target's linear small-ball scaling on the stated structural branch.

### Proof

Let `Y` denote all coordinates except `X_k`. Completing the square in the **original physical coordinate** gives exactly

`Q=d (X_k + b^T Y/d)^2 + R(Y),`
`R(Y)=Y^T S0 Y.`                                                (4.3)

Apply Theorem 3.1 with `r=2,q=3/2` to the residual form `R`. It gives

`||p_R||_3 <= 6^(2/3)D^(-1/3),`                                (4.4)

or `3^(2/3)delta^(-1/3)` in the square-block case.

Set

`V=X_k+b^T Y/d`.

For almost every value `R=r`, the conditional law of `V` is a mixture, over `Y|R=r`, of translations of the original law of `X_k`. Since `X_k` is independent of `Y` and its density is at most one, every such mixture still has density at most one.

Account01/B11's source-pinned dependent-square lemma therefore applies to (4.3): if `M=||p_R||_3`, then

`||p_Q||_infinity <=4 |d|^(-1/2) M^(3/4).`

Substitution of (4.4) gives (4.1), and the square-block value gives (4.2). QED.

### Continuity status

Theorem 3.1 at rank two proves absolute continuity with an `L^3` density. Theorem 4.1 proves an essentially bounded density through dependent square smoothing. This argument, as stated, does **not** prove that the resulting density has a continuous representative. No continuity claim is promoted here.

## 5. Direct application of the named account02/B03 overlap-collapse family

Use the partner's exact family with nonzero spectrum `(1,1,-1)`. In its spectral basis `(e,p,q)`, the quadratic matrix is

`[[0,1,0],[1,0,0],[0,0,1]]`,

and the physical frame rows are

`a e, p/sqrt(2), p/sqrt(2), q/sqrt(2), q/sqrt(2), epsilon e`,
`a=sqrt(1-epsilon^2)`.

The partner proved that every disjoint invertible `3 x 3` crosspacket has determinant `a epsilon/4`, so every rank-three crosspacket certificate collapses at one endpoint.

Let `m=max(a,epsilon)>=1/sqrt(2)`. Choose the physical row carrying `m e`, one `q/sqrt(2)` row for the first side, and one `p/sqrt(2)` row plus the other `q/sqrt(2)` row for the second side. The resulting `2 x 2` cross block is exactly

`diag(m/sqrt(2), 1/2)`,

so

`delta=m/(2sqrt(2)) >=1/4.`                                    (5.1)

Applying the new square-block inequality (3.4) gives the actual uniform bound

`boxed( ||p_Qepsilon||_3 <= 3^(2/3) 4^(1/3)=36^(1/3)<3.302 )`  (5.2)

for every `0<=epsilon<=1`, even though the partner's rank-three cross determinant tends to zero.

This is a concrete application of the named partner's exact construction, not a citation-only handoff. It identifies what survives the overlap collapse: **rank-two averaged regularity remains uniformly nondegenerate**. The missing task is to spend the third direction without forcing a single disjoint rank-three packet.

The latest account02/B03 correction is also applied structurally: (3.6)-(3.7) work entirely with original-coordinate product amplitudes and therefore introduce none of the invalid conditional caps `||p_{U|V=v}||infinity`; in particular there is no law-dependent Renyi-spread factor in (5.2).

## 6. What the new pivot theorem does not imply

A tempting next statement would be:

> every matrix with three large eigenvalues has one nonzero physical pivot whose Schur complement contains a rank-two cross cut with dimension-free resource.

The fresh correction `QFORM-SINGLE-SCHUR-RANK2-EXTRACTION-FALSE` rules this out even qualitatively. Its exact target family can leave only a rank-one star after every allowable scalar pivot while remaining uniformly bounded through a high-cardinality hyperbolic-square aggregation.

Therefore Theorem 4.1 is a **smoother/certificate**, not a universal extraction theorem. The source-valid next implication must be overlap-aware and aggregate before reciprocal local determinant costs are paid.

A compact conditional end-to-end route now is:

1. rank `>=3` cross cuts: use the existing `L^1_t` Plancherel theorem directly;
2. rank-two cross cuts: use Theorem 3.1 to get determinant-scale `L^3` regularity without any false `U|V` cap;
3. where a physical third square pivot survives Schur complementation, Theorem 4.1 converts that `L^3` resource to a linear small-ball bound;
4. when every single-pivot route collapses, use a high-cardinality hyperbolic/overlap-aware aggregation before conditioning or determinant inversion.

The first unpaid implication is item 4 in general form: prove a product-preserving aggregation theorem that turns the spectral three-direction hypothesis into either a rank-`>=3` direct cross smoother, a rank-two `L^3` packet plus a valid third-direction smoother, or the already-observed high-cardinality hyperbolic-square branch, with constants uniform under extra spectral components and cancellation.

## 7. Status ledger

- `QFORM-FULL`: **OPEN**.
- `QFORM-CROSSCUT-AVERAGED-LP-v1`: **PROVED** in Theorem 3.1.
- `QFORM-RANK2-CROSS-L3-v1`: **PROVED** as (3.3)-(3.4).
- `QFORM-SCHUR-CROSS2-DEPENDENT-SQUARE-v1`: **PROVED** in Theorem 4.1.
- Named partner account02/B03 conditional-cap correction: **APPLIED**; no conjugate-variable conditioning is used.
- Named partner overlap-collapse family: **APPLIED** to obtain the uniform explicit `L^3` estimate (5.2).
- Universal single-pivot extraction: **REJECTED**, consistently with the fresh account02/B09 correction.
- Continuous density on the full target, and even on the generic dependent-pivot theorem as presently proved: **NOT ESTABLISHED**.

No simulation, Gaussian/log-concave/support/moment assumption, post-rotation independence, pointwise Fresnel decay, public release, paid call, or native-memory claim is used.
