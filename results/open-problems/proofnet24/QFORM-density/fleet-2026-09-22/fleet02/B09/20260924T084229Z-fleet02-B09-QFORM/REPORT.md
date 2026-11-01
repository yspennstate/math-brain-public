SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-24T08:42:29Z.
attacking: the tiny-polynomial-star survivor after the new fleet03/B09 definite-pair theorem; spend a source-coordinate mixed frame before paying any reciprocal pair-star currency.

# fleet02/B09 — Schur-star ledger and a target-valid tiny-H mixed-frame obstruction

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Partner: fleet03/B09  
Run: `20260924T084229Z-fleet02-B09-QFORM`  
Status: **NEW STRUCTURAL IDENTITY + TARGET-VALID OBSTRUCTION + COMPLETED MIXED-FRAME RECEIVER APPLIED / FULL QFORM OPEN**  
Execution: authenticated fresh repository retrieval was used in the mathematical receiver; native learned-memory ingestion is not separately verified.

All stochastic coordinates below are literal ORIGINAL source coordinates and are independent with probability densities at most one. No moments, bounded support, connected support, log-concavity, iid hypothesis, Gaussianity, law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea estimate, or post-rotation independence is used. Continuity is asserted only for the integrable-Fourier branch explicitly proved below.

## 1. First unpaid implication

The newest completed designated partner, fleet03/B09 r47, removes the punctured **nonnegative physical-pair** obstruction whenever its polynomial star

`H=a v-c u`

is nonzero. It keeps the whole remaining same-bank quadratic matrix arbitrary and gives

`||p_Q||_infinity <= 2^(5/4) pi sqrt(3) ||H||_2^(-1/2)`.

This is determinant-free and passes through `det B=0`, but it is not uniform as `H -> 0` and has no hypothesis at `H=0`.

The first unpaid B09 implication is therefore sharpened to

### `QFORM-TINY-SCHUR-STAR-TO-AGGREGATE-FRAME-OR-CROSSING-v1`

After one literal scalar pivot, do **not** try to force a universal lower bound on one nonnegative pair's `||H||`. Either a macroscopic polynomial star pays by r47, or the small-star survivor must be compiled, before pair selection, into a source-coordinate mixed frame / grouped crossing / bounded physical core. The compiler must retain arbitrary same-bank curvature and may not discard a small coefficient as a small random perturbation.

This run proves an exact Schur-star ledger, shows that `H` can vanish or tend to zero in a fully target-valid family, and pays that family uniformly by the pinned mixed-hub theorem with the exact constant `3` while retaining a dense same-side leaf square.

## 2. Sources actually consumed


The required fixed source was reread at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,

including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The completed input used below is Theorem H. Split literal coordinates as hubs `H`, leaves `I`, conditioned bank `J`, and suppose

`A_II=sum_{k=1}^r lambda_k v_k v_k^T + D`,

with `D` physical diagonal. For mixed rows

`rho_i=((v_k)_i ; A_{ih}, h in H)`

and Gram `G=sum_i rho_i rho_i^T`, if `G>0` and every normalized leverage satisfies

`rho_i^T G^(-1) rho_i <=1/2`,

then

`|phi_Q(t)|
 <=(2|t|)^(-|H|)
   prod_k (4 pi |t lambda_k|)^(-1/2)
   (4 pi)^(r+|H|) det(G)^(-1/2)`.

Crucially, `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. Thus an entire conditioned source bank and all of its dense same-side couplings remain in the theorem rather than being deleted by decoupling.

The newest completed designated partner is fleet03/B09 r47,

`yspennstate/math-open-problems@99292d434fe013bcced66702de127ef781852baa`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260924T074738Z-fleet03-B09-QFORM-r47/REPORT.md`.

Its deterministic checker is committed at `14abaffb2e571a3201bbd98fbcb3e33fddf203fe` and records `QFORM_B09_R47_CHECK_PASS` with the definite-pair constant `12.941898654808462`.

A still newer Claude-attributed source commit observed before publication is `8edfa020d8904154efd9488a01828e22e2e7b2d4`, which adds average-over-leak and average-over-shift estimates in the single-hub continuation. Those are averaged parameter statements, not a pointwise uniform rough-law closure. Nothing below conflicts with them; the family in Section 5 is paid pointwise by Theorem H, so no averaging in its parameters is used.

The fixed-source counterexample search still reports no valid counterexample to the unrestricted QFORM conjecture.

## 3. Exact Schur-star ledger

Fix a literal physical pivot `p` with

`a=A_pp !=0`.

Write the full quadratic matrix, after merely reordering literal coordinates, as

`A=[[a,u^T],[u,C]]`,

and let

`S=C-a^(-1)u u^T`

be the exact Schur complement on the remaining ORIGINAL coordinates `R`.

For each `q in R`, let `L=R\{q}` and consider the literal physical pair `(p,q)`. Its pair core is

`B_q=[[a,u_q],[u_q,C_qq]]`.

Its two outside arm vectors are `u_L` and `C[q,L]`. Define, exactly as in the partner theorem,

`H_q=a C[q,L]-u_q u_L`.

### Lemma 3.1 — `QFORM-SCHUR-POLYNOMIAL-STAR-LEDGER-v1`

For every `q in R`,

`boxed: det B_q = a S_qq`,

and

`boxed: H_q = a S[q,R\{q}]`.

Consequently

`boxed:
 sum_{q in R} ||H_q||_2^2
 =a^2 ( ||S||_F^2-sum_q S_qq^2 ).
`

If

`P_+={q in R: det B_q>=0}={q:aS_qq>=0}`, 

then

`boxed:
 sum_{q in P_+} ||H_q||_2^2
 =a^2 sum_{q in P_+} sum_{j!=q} S_qj^2.
`

In particular, if `H_q=0` for every nonnegative pair `q in P_+`, then every such `q` is an isolated coordinate of the Schur complement: after reordering,

`S = diag(S_qq:q in P_+) direct_sum S_-`,

and every diagonal entry of `S_-` has sign opposite to `a`.

### Proof

The determinant identity is immediate:

`det B_q=a C_qq-u_q^2=a(C_qq-u_q^2/a)=aS_qq`.

For `j in L`,

`(H_q)_j=a C_qj-u_q u_j=a(C_qj-u_q u_j/a)=aS_qj`.

Squaring and summing over `j!=q` gives the row identity. Summing over `q` gives the Frobenius ledger; both sides count an off-diagonal entry twice, once from each ordered row. Finally, if `H_q=0`, every off-diagonal entry in row `q` of `S` is zero. Symmetry then also kills the corresponding column. QED.

### Interpretation

The partner's nonnegative-pair resource is not an opaque post-completion quantity: after a fixed scalar pivot it is **exactly an off-diagonal Schur row**. Thus r47 pays any same-sign Schur diagonal carrying a nonzero row, with no determinant loss. At the exact zero-star endpoint all same-sign Schur coordinates split off diagonally. The genuinely hard interface is quantitative: an order-one Frobenius ledger may be spread over many rows with each `||H_q||` tiny, and arbitrary cap-one laws do not permit deleting those small coefficients probabilistically.

## 4. Exact one-hub/one-square mixed-frame constant

The next statement is a specialization of the completed pinned Theorem H, recorded here because its exact constant is the receiver used on the obstruction family.

Let `p` be one literal hub, `I` a literal product leaf bank, and put every other original coordinate in `J`. Suppose

`A_II=lambda v v^T + D`,

where `v` is unit, `lambda!=0`, and `D` is physical diagonal. Let

`g=A[I,p]`,

`rho_i=(v_i,g_i)`,

`G=sum_i rho_i rho_i^T`.

Assume `G>0` and every leaf leverage is at most `1/2`.

Pinned Theorem H with `h=r=1` gives

`|phi_Q(t)|
 <=4 pi^(3/2) |lambda|^(-1/2) det(G)^(-1/2) |t|^(-3/2)`.

Let

`K=4 pi^(3/2)|lambda|^(-1/2)det(G)^(-1/2)`.

Since

`int_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`, 

Fourier inversion gives the exact corollary

### Corollary 4.1 — `QFORM-CONDITIONED-ONEHUB-ONESQUARE-v1`

`boxed:
 ||p_Q||_infinity
 <=3*2^(4/3) (|lambda| det G)^(-1/3).
`

The characteristic function is integrable, so this branch has a continuous density and

`P{Q in I_0}
 <=3*2^(4/3)(|lambda|det G)^(-1/3)|I_0|`

for every interval `I_0`.

All hub-core coefficients, all couplings to the conditioned source bank `J`, the entire quadratic block on `J`, all leaf-to-`J` couplings, and all affine terms are retained exactly. There is no Cauchy--Schwarz probability squaring and therefore no square-root small-ball loss.

## 5. A target-valid two-parameter tiny-H family paid uniformly by the mixed frame

Let `m>=8` be a Sylvester--Walsh size and choose three flat orthonormal Walsh vectors

`c,d,w in R^m`.

Thus every coordinate has squared magnitude `1/m`. For arbitrary independent cap-one source variables

`X_1,X_2,Y_1,...,Y_m`, 

and parameters

`0<=delta<=1`, `epsilon>=0`,

define

`Q_{delta,epsilon}
 =X_1^2+2X_1X_2+(1+delta)X_2^2
  +8X_1<c,Y>
  +8X_2<c+epsilon d,Y>
  +<w,Y>^2`.                                             (5.1)

The literal physical pair `{1,2}` has

`B_delta=[[1,1],[1,1+delta]]`,

so

`det B_delta=delta>=0`.

Its outside arms are

`u=4c`,
`v=4(c+epsilon d)`.

Therefore the partner polynomial star is

`boxed: H=v-u=4 epsilon d`,

hence

`boxed: ||H||_2=4 epsilon`.                              (5.2)

For every `epsilon>0`, the newest fleet03/B09 theorem applies to this actual full law and gives

`||p_{Q_{delta,epsilon}}||_infinity
 <=2^(5/4)pi sqrt(3)(4epsilon)^(-1/2)`

or

`boxed:
 ||p_{Q_{delta,epsilon}}||_infinity
 <=6.470949327404231 epsilon^(-1/2).
}`                                                          (5.3)

This is the requested application of the newest partner result to a real inequality. It is already determinant-free, but it diverges as `epsilon->0` and does not apply at `epsilon=0`.

Now spend the source-coordinate mixed frame **before** this pair-star currency. Put the literal coordinate `X_2` into the conditioned bank `J`, keep `X_1` as the single physical hub, and keep every `Y_i` in the active product leaf bank. The active quadratic leaf block is the dense physical matrix

`w w^T`,

and the hub-to-leaf star is

`g=4c`.

Every term containing the conditioned `X_2` becomes only an affine term or conditioned constant, all of which Theorem H allows. In particular **no** `delta`- or `epsilon`-dependent term is deleted from the original law.

For Corollary 4.1,

`lambda=1`,

`rho_i=(w_i,4c_i)`,

`G=diag(1,16)`,

`det G=16`,

and

`rho_i^T G^(-1)rho_i=w_i^2+c_i^2=2/m<=1/4`.

Hence

`|phi_{Q_{delta,epsilon}}(t)|
 <=pi^(3/2)|t|^(-3/2)`

uniformly in both parameters, and

`boxed:
 ||p_{Q_{delta,epsilon}}||_infinity <=3
}`                                                          (5.4)

for every `0<=delta<=1` and every `epsilon>=0`. Moreover

`boxed:
 P{Q_{delta,epsilon} in I_0}<=3|I_0|
}`                                                          (5.5)

for every interval, and the density is continuous.

The same-side leaf coupling `w w^T` is dense in the physical source coordinates because every Walsh entry is nonzero. It remains active throughout the estimate. Thus (5.4) is genuinely a mixed-hub/source-coordinate smoothing statement with dense same-side coupling, not a diagonal-basis argument.

## 6. Uniform target certificate

The family (5.1) satisfies the owner's spectral hypothesis uniformly in both parameters.

Consider the deterministic three-dimensional subspace

`E=span{e_1,c,w}`, 

where `e_1` is the first physical hub coordinate and `c,w` are viewed as vectors in the `Y` bank. The compression of the full symmetric coefficient matrix to `E` is

`A|_E = [[1,4,0],[4,0,0],[0,0,1]]`.

Its eigenvalues are

`mu_1=(1+sqrt(65))/2=4.5311288741...`,

`mu_2=1`,

`mu_3=(1-sqrt(65))/2=-3.5311288741...`.

These Ritz values do not depend on `delta` or `epsilon`; the extra `X_2` couplings disappear only in the deterministic compression, not in the stochastic proof.

By Poincare separation for a compression of a real symmetric matrix,

`lambda_1(A)>=mu_1>1`,

`lambda_2(A)>=mu_2=1`,

and

`lambda_min(A)<=mu_3<-1`.

Therefore every member of (5.1) has at least **three** eigenvalues of modulus at least one. The example lies inside the exact full target, including at `delta=0` and `epsilon=0`.

## 7. What the family obstructs

The two parameters expose two independent pair-first losses.

First,

`det B_delta=delta ->0`,

so any receiver that first pays a reciprocal positive power of the physical pair determinant degenerates although the true density remains at most `3`.

Second,

`||H||=4epsilon ->0`,

so even the new denominator-free nonnegative-pair theorem cannot be made into a full structural closure by asserting that the target spectrum forces a macroscopic polynomial star. It does not: `epsilon=0` is target-valid and (5.4) still gives `3`.

Thus the correct order of operations is genuinely aggregate. A source-coordinate square/star frame can contain the third smoothing resource even when every pair-first currency under consideration is tiny or zero.

The Schur-star ledger in Section 3 sharpens the exact endpoint. If, after a fixed pivot, every nonnegative pair has `H_q=0`, then the same-sign part of the Schur complement is already physical-coordinate diagonal and the remaining dense block has diagonal sign opposite to the pivot. So exact zero is structurally rigid. The hard problem is the **quantitative tiny-H** regime: approximate diagonalization is not enough, because a small quadratic coefficient need not be a small random perturbation for arbitrary unbounded cap-one inputs.

## 8. Relation to the current single-hub leak continuation

The freshest Claude continuation observed during this run proves that, in its specialized leaking-hub model, averaging over a shift parameter or over a dyadic leak window controls the average density. That result is compatible with the obstruction here but does not replace (5.4): an average in `epsilon` does not imply a pointwise bound at each fixed rough source law.

In (5.1), conditioning one literal source coordinate removes the parameter-dependent partner arm from the active quadratic frame while leaving a full hub star plus a dense leaf square. Hence the pinned Theorem H gives a pointwise parameter-uniform estimate. This identifies one concrete chamber in which the rough leak disappears by an ORIGINAL-coordinate conditioning rather than by smoothing or parameter averaging.

## 9. Remaining implication

No full-target counterexample was found. The fixed-source search also reports none.

The next B09 implication is precisely

### `QFORM-TINY-SCHUR-STAR-TO-AGGREGATE-FRAME-OR-CROSSING-v1`

Given a scalar pivot and a Schur complement retaining at least the needed target spectral resource, assume every nonnegative-pair polynomial star is below the scale at which r47 is useful. Use the exact ledger

`sum ||H_q||^2 = a^2 ||offdiag S||_F^2`

together with the opposite-sign block to produce, **before selecting one pair**, either

- a literal source-coordinate mixed frame with enough determinant and leverage control,
- a grouped crossing / volume receiver,
- or a bounded-dimensional physical core.

The exact zero-H branch block-diagonalizes as proved above; what remains unpaid is a quantitative aggregation theorem robust to arbitrarily fragmented and unbounded cap-one laws. No perturbative deletion of the tiny off-diagonal Schur rows is permitted.

This is a supporting advance, not a proof of unrestricted QFORM.
