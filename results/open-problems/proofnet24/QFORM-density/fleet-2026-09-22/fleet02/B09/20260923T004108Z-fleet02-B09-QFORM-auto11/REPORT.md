SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B09, 2026-09-23T00:41:08Z.
attacking: mixed-hub smoothing for an actual source-coordinate star while retaining dense same-side low-rank couplings, with a direct linear interval bound and no square-root decoupling loss.

# fleet02/B09 — mixed-hub wedge smoothing inside the no-pivot class

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T004108Z-fleet02-B09-QFORM-auto11`  
Role: Bilinear block mechanism / complementary constructions and source-valid counterexamples  
Status: **ESSENTIAL STEP APPLIED / FULL TARGET OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

## 1. First unpaid implication

`QFORM-N3-MIXED-HUB-WEDGE-OR-PAID-EXIT-v1`: in the remaining no-small-physical-pivot class N3, force either

1. a source-coordinate hub and a disjoint leaf bank whose mixed star/same-side frame has a universal wedge determinant and bounded row leverage, so the theorem below gives a direct `O(|L|)` bound;
2. two genuinely independent hyperbolic packets, a gapped scalar-Schur packet, a definite/ridge/physical-pair exit already paid elsewhere; or
3. isolate the genuinely overlapping higher-rank leaf operator for a new product-provenance estimate.

This run pays item 1 for the exact low-rank-plus-diagonal leaf geometry and gives an explicit target-valid N3 family. It does **not** prove the structural extraction of such a frame from arbitrary N3 matrices.

## 2. Source theorem actually used

The completed source is Theorem H of

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837:proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`,

with the compatible Fourier audit in `FOURIER_ROUTE_REPORT.md` at the same commit. The theorem works in original coordinates. Split the variables as `H union I union J`; if

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,

with `D` diagonal, and for each `i in I`

`rho_i = ((v_1)_i,...,(v_r)_i, A_{ih}: h in H)`,

then with `G=sum_i rho_i rho_i^T`, positive definite, and row leverages `rho_i^T G^{-1} rho_i <=1/2`, it gives

`|phi_Q(t)| <= (2|t|)^(-|H|) prod_k (4 pi |t lambda_k|)^(-1/2) (4 pi)^(r+|H|) det(G)^(-1/2)`.

Crucially, `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. Conditioning `J` only changes affine terms; the proof integrates the actual source-coordinate hubs and uses Brascamp--Lieb on the product leaf variables. It does not assert independence after rotating to the `v_k` directions and it does not square a small-ball probability.

## 3. One-hub mixed-frame theorem

### Theorem `QFORM-ONE-HUB-RANKR-MIXEDFRAME-v1`

Let the original independent coordinates be partitioned as `{h} union I union J`. Allow arbitrary affine terms. Assume

`A_II = D + sum_{k=1}^r lambda_k v_k v_k^T`,                    (3.1)

where `r>=1`, `D` is diagonal, and every `lambda_k !=0`. Put

`c=A_{Ih}`,
`rho_i=((v_1)_i,...,(v_r)_i,c_i) in R^(r+1)`,
`G=sum_{i in I} rho_i rho_i^T`.                                 (3.2)

Assume `G` is positive definite and

`max_i rho_i^T G^{-1} rho_i <=1/2`.                             (3.3)

No restriction is imposed on `A_hh,A_hJ,A_IJ,A_JJ`. Then `Q=X^TAX+b^TX+d` has a bounded continuous density and

`boxed: ||p_Q||_infinity <= C_r [ det(G) prod_{k=1}^r |lambda_k| ]^(-1/(r+2)),`   (3.4)

where

`C_r = 4 (r+2)/r * 2^(-2/(r+2)).`                               (3.5)

Consequently every interval `L` satisfies

`boxed: P{Q in L} <= C_r [ det(G) prod |lambda_k| ]^(-1/(r+2)) |L|.`            (3.6)

#### Proof

Apply source Theorem H with the single physical hub `H={h}`. Its exponent is

`alpha = 1 + r/2 = (r+2)/2 >1`.

The source estimate becomes

`|phi_Q(t)| <= K |t|^(-alpha)`,

with

`K = [(4 pi)^(1+r/2)/2] [det(G) prod |lambda_k|]^(-1/2).`        (3.7)

Use also `|phi_Q(t)|<=1`. For `alpha>1`,

`integral_R min(1,K|t|^(-alpha)) dt
 = 2 alpha/(alpha-1) K^(1/alpha).`                              (3.8)

Fourier inversion therefore gives

`||p_Q||_infinity <= alpha/[pi(alpha-1)] K^(1/alpha)`.

Since

`[(4 pi)^((r+2)/2)/2]^(2/(r+2)) = 4 pi 2^(-2/(r+2))`,

this is exactly (3.4)-(3.5). The characteristic function is integrable, so the density obtained by inversion is continuous. `QED`

The proof is directly linear in interval length. There is no Cauchy--Schwarz/Weyl differencing of the target small-ball event and hence no square-root loss.

## 4. Rank-one leaf curvature: a wedge invariant

For `r=1`, write `A_II=D+lambda vv^T`. Then

`G = [[||v||_2^2, <v,c>], [<v,c>, ||c||_2^2]]`

and

`det G = ||v||_2^2 ||c||_2^2 - <v,c>^2 = ||v wedge c||^2`.       (4.1)

The theorem becomes

`boxed: ||p_Q||_infinity <= 3*2^(4/3) [ |lambda| ||v wedge c||^2 ]^(-1/3)`  (4.2)

with

`3*2^(4/3) = 7.559526299...`.                                   (4.3)

Thus a physical source-coordinate star is smoothed by a dense same-side rank-one leaf curvature precisely through the aggregate transversality of the two source vectors. Arbitrary diagonal leaf curvature, arbitrary hub self-curvature, arbitrary conditioned outside quadratic terms, and arbitrary cross couplings to the conditioned bank `J` are retained.

The quantity in (4.2) is representation-scale invariant: replacing `v` by `a v` and `lambda` by `lambda/a^2` leaves `|lambda| det G` unchanged.

### Why the wedge condition is real for this mechanism

If `v` is parallel to `c`, `G` is singular and the active hub/leaf core has only rank two. This is not a removable technicality. For iid `X,Y~Uniform[-1/2,1/2]`,

`2XY+Y^2 = Y(2X+Y)`.

With `u=Y`, `w=2X+Y`, the joint density of `(u,w)` equals `1/2` on the square `[-1/4,1/4]^2`. Hence, for `0<q<1/16`, the product change of variables gives

`p_(2XY+Y^2)(q) >= log(1/(16q))`,                              (4.4)

so the density is logarithmically unbounded. This is only a rank-two obstruction, not a QFORM counterexample; it shows that a third transverse or external smoother must genuinely be retained when the mixed wedge collapses. It is consistent with the existing correction `QFORM-ONESTAR-ARBITRARY-SELF-HALFRIESZ-FALSE-v1` and does not reintroduce that false extension.

## 5. A target-valid diffuse N3 family paid by the mixed hub

Let `m>=4` be even. On a leaf bank `I` of size `m`, set

`c = m^(-1/2)(1,...,1)`,
`v = m^(-1/2)(1,...,1,-1,...,-1)`,

with `m/2` plus and `m/2` minus signs, so `c perp v` and both are unit vectors. Add one disjoint physical hub coordinate `h`, and define the matrix by

`A_hh=0`, `A_hI=c^T`, `A_II=vv^T`,                            (5.1)

with all other entries zero. Then

`Q_m = 2 X_h <c,X_I> + <v,X_I>^2`.                            (5.2)

In the orthonormal basis `{e_h,c,v}`, the nonzero compression is

`[[0,1,0],[1,0,0],[0,0,1]]`,                                  (5.3)

so

`spec(A_m) = {1,-1,1,0,...,0}`.                               (5.4)

This is an exact instance of the full three-large-eigenvalue target.

Every physical diagonal is `0` or `1/m`. Every leaf-leaf `2x2` principal determinant is zero, while every hub-leaf determinant is

`det [[0,c_i],[c_i,v_i^2]] = -c_i^2 = -1/m`.                  (5.5)

Therefore for every fixed N3 threshold `tau>0`, all sufficiently large `m` satisfy the strict no-pivot conditions `|A_ii|<tau` and `|det A[{i,j},{i,j}]|<tau`. At the same time all hub coefficients are only `m^(-1/2)` and every dense same-side leaf coefficient is `O(1/m)`.

But the aggregate mixed Gram is exactly `G=I_2`; each row leverage is

`c_i^2+v_i^2 = 2/m <=1/2`.                                    (5.6)

Taking `lambda=1` in (4.2) gives the dimension-free target bound

`boxed: ||p_(Q_m)||_infinity <= 3*2^(4/3) < 7.560,`             (5.7)

and hence

`boxed: P{Q_m in L} < 7.560 |L|}`                              (5.8)

for every interval `L` and every admissible collection of independent cap-one source laws.

This is an actual no-pivot family whose third direction is stored in dense same-side couplings on the *same leaf bank* as the star. The projections `<c,X_I>` and `<v,X_I>` are generally dependent; the proof never treats them as independent.

## 6. Designated partner result applied to a real target inequality

The latest completed designated-partner result found and read in full is fleet03/B09 r19,

`QFORM-FOUR-BANK-HYPERBOLIC-CONVOLUTION-v1`,

at

`yspennstate/math-open-problems@e8c7ac4f0294a028d4bc883d1e4bf1c805e11085:proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B09/20260922T224649Z-fleet03-B09-QFORM-r19/REPORT.md`.

For four disjoint original-coordinate unit-projection banks it gives

`||p_(2UV+2WR)||_infinity <=16`.                               (6.1)

Now take a fifth disjoint unit-projection bank and call its projection `Z`. Since `Z^2` is independent of the first four-bank block, convolution with its probability law cannot increase an `L^infinity` density. Thus the partner theorem gives the actual target-valid inequality

`boxed: ||p_(2UV+2WR+Z^2)||_infinity <=16`,                    (6.2)

and

`boxed: P{2UV+2WR+Z^2 in L} <=16 |L|.`                         (6.3)

The scalar compression has spectrum `{1,-1,1,-1,1}`. With flat unit projections on five size-`m` banks, every physical coefficient is `O(1/m)`, including the dense same-side coefficients of `Z^2`, while (6.2) remains dimension-free. This partner exit is complementary to the mixed-hub theorem: it spends a second genuinely independent hyperbolic packet when same-bank mixed-frame transversality is unavailable.

## 7. What this changes in the global proof map

The source Theorem H is not merely a Fourier curiosity: it pays an explicit, genuinely N3 source-coordinate geometry that the physical-pivot reduction is designed to leave behind. The right aggregate certificate for one hub plus one dense leaf square is not a single entry or a physical `2x2` determinant but

`|lambda| (||v||^2||c||^2-<v,c>^2)`.                         (7.1)

The new structural target is therefore to extract a quantitatively nondegenerate mixed frame before conditioning away the third direction. If the leaf operator is exactly low-rank plus diagonal, the theorem above already handles arbitrary outside blocks. The unresolved survivor is a hub whose leaf-side quadratic operator is genuinely higher rank and overlapping, with no useful low-rank mixed-frame wedge and no disjoint second hyperbolic packet.

No moment, support, log-concavity, centeredness, identical-law or post-rotation independence assumption was used. Full QFORM remains OPEN; global continuity remains separate.

## 8. Source/correction ledger

Positive source actually applied:
- `e5f71d79eff325201dd0274053d20268ce65b837`, `RESULTS.md` Theorem H and compatible `FOURIER_ROUTE_REPORT.md`;
- designated partner fleet03/B09 r19 at `e8c7ac4f0294a028d4bc883d1e4bf1c805e11085`.

Compatible later source/control read before the proof: the owner continuation requires the later `2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926` geometric update; its N3/no-pivot reduction and hub framing were retained. The report does not claim that update proves the open gluing step.

Corrections enforced include: law-uniform pointwise quadratic-phase decay is false; arbitrary-joint rank-three coarea is false; positive moments of worst conditional projection-density caps are false; independence cannot be inferred after spectral rotation; a universal single physical Schur rank-two extraction is false; same-square one-heavy-row absorption is false; overlapping square curvature is not automatically an external smoother; and `QFORM-ONESTAR-ARBITRARY-SELF-HALFRIESZ-FALSE-v1` forbids extending this result to an arbitrary same-bank operator without a new argument.

Privacy/integrity review: changed mathematical allowlist contains this report only; manual inspection found no credentials, scheduler identifiers, machine paths, private unrelated data, benchmark gold, or public-release material. No external paid/runtime workflow was used.
