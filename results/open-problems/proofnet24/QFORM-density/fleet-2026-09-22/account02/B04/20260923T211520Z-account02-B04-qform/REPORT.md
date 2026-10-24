SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B04, 2026-09-23T21:15:20Z.
attacking: zero-pivot overlap-one compound mass by a grouped clean-bank top-two rearrangement receiver; optimize physical volume weights and compare pinned volume/ridge routes on the same target-valid matrix.

# account02/B04 — grouped clean-bank receiver for the zero-pivot C1 star branch

Programme: `QFORM-DENSITY-3EIG-20260922`.
Role: Product Fourier rearrangement / complementary constructions and source-valid counterexamples.
Status: `ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / SAME-MATRIX VOLUME-RIDGE OBSTRUCTION / FULL TARGET OPEN`.
Execution context: `WITHOUT_VERIFIED_BRAIN`.
Continuity: not claimed for the new clean-bank theorem; full-target continuity remains separate and OPEN.

The unrestricted QFORM conjecture is **not** proved here. All variables below are original-coordinate product variables until an explicitly stated deterministic coefficient-space projection. No rotated random coordinates are declared independent. No moment, support, centering, log-concavity, connectedness, or smoothness assumption is added.

## 0. First unpaid implication

The first unpaid B04 implication is now

`QFORM-C1-STAR-FACTOR-ROUGH-ZCURVATURE-RECEIVER-v1`:

> Start from the zero-anchor factorization of account03/B04 r41,
> `2(b^T Y_N)(X_h+p^T Y_N)+2Y_N^T E_NZ Y_Z+Y_Z^T E_ZZY_Z`,
> with every surviving overlap-one minor unchanged by the star subtraction. The clean-bank case `E_ZZ=0` is paid in this run by grouping *all* zero-hub coordinates before any reciprocal minor is selected. What remains is the rough-curvature case `E_ZZ!=0`: prove that either the Z-bank curvature itself enters a completed pair/D5/ridge/projected-crossing/grouped-hub endpoint, or retain a target-scale top-two coefficient norm through a product-preserving rearrangement without pointwise oscillatory decay or division by a vanishing local minor.

This is strictly narrower than the preceding zero-pivot C1 extraction problem: the analytic grouped clean-bank endpoint is now complete.

## 1. Fresh sources and completed inputs actually used

Fresh owner control remained QFORM-only, revision `2026-09-22.15`, with the full target OPEN and no applicable stop. The live correction ledger was re-read. In particular this run does **not** use the refuted law-uniform pointwise quadratic-phase decay, arbitrary-joint rank-three coarea, worst-fibre supremum, conditional projection-cap moment, post-rotation independence, a uniformly good single physical minor, or a universally available rank-three physical cross cut.

The required pinned Claude/e5 source was read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

The completed results used below are:

1. Theorem D and its arbitrary-minor-weight determinant/weighted-AM-GM form, with row-marginal gate `alpha_i<=1/2` and density bound `6 sqrt(e) G_3(w)^(-1/6)`.
2. The proved D' extension with row marginals `<3/4`.
3. The proved fifth-volume theorem D5, `||p||_infinity <=5 sqrt(2e) Z5^(-1/10)`, with no marginal gate.
4. The product-projection/Ball-Rogozin linear-form cap used in the source's physical-coordinate arguments.

The latest compatible account03/B04 result observed before publication is

`yspennstate/math-open-problems@f5e2f6935273fd126982d1e66f83b6c5623f430d`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T211945Z-account03-B04-QFORM-auto11/REPORT.md`.

It proves the zero-pivot three-coordinate receiver

`||p||_infinity <=3*2^(2/3)|det B|^(-1/3)`

for a nonsingular physical principal `3x3` block with a zero diagonal pivot. The stress family below has **every** physical principal `3x3` block singular, so this fresh theorem is applied as a precise local obstruction rather than falsely extended beyond its determinant hypothesis.

The immediately preceding compatible account03/B04 r41 source

`yspennstate/math-open-problems@fc213cf50d21dd7e00a36fbb2ad2c4e7ad55f056`

supplies the exact zero-anchor C1 star factorization used at an equation below. Its later correction addendum `1b06210571e34985efd1a96869ceedaf510d251f` changes only one unrelated comparison decimal and leaves the theorem intact.

For the optional lower-order volume comparison, I also use the already proved B04 theorem `QFORM-ENTROPY-WEIGHTED-RANK2-HALFRIESZ-v1`, source-pinned at

`yspennstate/math-open-problems@10a74bd7d75466fe46f4ff6ecf3362fba6cb2e5d`,

whose exact arbitrary-weight currency is `G_2(w)=exp(E_w log det^2+H(w))`.

The direct ridge gate compared below is the completed ridge-window criterion source-pinned at

`yspennstate/math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`:

for `K_gamma=B B^T(gamma^2 I+B B^T)^(-1)`, an exponent `q>=1` requires

`max_i (K_gamma)_ii <=q/2`, `theta_gamma=tr K_gamma>2q`.

## 2. New theorem: clean-bank top-two product rearrangement

### Theorem 2.1 — `QFORM-CLEANBANK-TOPTWO-REARRANGEMENT-v1`

Let `X=(X_i)_{i in I}` and `Y=(Y_j)_{j in J}` be disjoint banks of original independent coordinates, every scalar density bounded by one. Let `M` be a real `|I| x |J|` matrix whose two largest singular values satisfy

`s1>=s2>0`.

Consider

`Q = F(X) + 2 X^T M Y + b^T Y + c`,                                  (2.1)

where `F` is an arbitrary measurable function of the whole X-bank. In particular `F` may contain arbitrary X-X quadratic curvature and arbitrary affine terms. There is **no** Y-Y quadratic term.

Then `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity <= 2 sqrt(pi) (s1 s2)^(-1/2).`                      (2.2)

No rank-two hypothesis is imposed on `M`: all lower singular directions may remain. The estimate uses only the top two coefficient-space directions.

### Proof

Condition on the original X-bank at `X=x`. The Y-random part is the linear form

`<2M^T x+b,Y>`

plus a deterministic shift. The product linear-form density theorem gives, for almost every `x`,

`||p_(Q|X=x)||_infinity
 <= sqrt(2)/||2M^T x+b||_2
 = 1/(sqrt(2)||M^T x+b/2||_2).`                                      (2.3)

Choose a singular-value decomposition of `M` only as deterministic coefficient algebra. Let `U_2,V_2` denote its top-two left/right singular frames. Orthogonal projection of a Euclidean norm can only decrease it, so

`||M^T x+b/2||_2
 >= ||diag(s1,s2) U_2^T x + V_2^T b/2||_2.`                           (2.4)

Set

`Z=U_2^T X`.

The crucial statement is a **joint density** statement, not independence: the two-dimensional projection of an original cap-one product law satisfies

`||p_Z||_infinity <=2.`                                               (2.5)

Consequently

`W=diag(s1,s2)Z+V_2^T b/2`

has a probability density `g` satisfying

`0<=g<=K:=2/(s1s2)`.                                                  (2.6)

For any probability density `g` on `R^2` bounded by `K`, decreasing rearrangement for the radial kernel `|w|^(-1)` gives

`int_R2 g(w)/|w| dw
 <= K int_{|w|<=R} |w|^(-1)dw,
 K*pi*R^2=1,
 =2 sqrt(pi K).`                                                      (2.7)

Averaging (2.3) and using (2.4)-(2.7),

`p_Q(t)
 <= (1/sqrt(2)) E |W|^(-1)
 <= (1/sqrt(2))*2 sqrt(2pi/(s1s2))
 =2 sqrt(pi)(s1s2)^(-1/2)`                                           (2.8)

for almost every output level `t`. This proves (2.2). QED.

### Scope

The theorem is deliberately asymmetric. Arbitrary curvature is permitted on the X-bank because X is conditioned first. Curvature on the Y-bank is **not** covered; that is exactly the first unpaid implication stated above. The deterministic singular-frame projection is applied only to the coefficient norm after conditioning and therefore does not invoke post-rotation independence.

## 3. Actual application of the partner C1 factorization

Take a physical coordinate `h` with `A_hh=0`, write `b_i=A_hi`, and let `C=A_{-h,-h}`. Account03/B04 r41 proves that if every physical principal triangle through `h` is singular, then with

`N={i:b_i!=0}`, `Z={i:b_i=0}`

one has

`C=bp^T+pb^T+E`, `E_NN=0`, `E_ii=0`,                               (3.1)

and hence

`2X_h b^T Y+Y^T C Y
 =2(b^T Y_N)(X_h+p^T Y_N)
  +2Y_N^T E_NZ Y_Z
  +Y_Z^T E_ZZ Y_Z.`                                                   (3.2)

Moreover the anchored overlap-one mixed minors are unchanged by replacing `C` with `E`.

If the residual clean-bank condition

`E_ZZ=0`                                                               (3.3)

holds, take the curved bank in Theorem 2.1 to be `Y_N`, and the clean bank to be the original coordinates `(X_h,Y_Z)`. The physical crossing matrix is

`K=[b,E_NZ]`.                                                          (3.4)

Thus, whenever its top two singular values are positive,

`boxed:
 ||p_Q||_infinity
 <=2 sqrt(pi) [s1(K)s2(K)]^(-1/2).`                                  (3.5)

This is the promised actual use of the designated-partner structural result: it pays the clean-bank subcase of the partner's unpaid zero-anchor C1 star branch while grouping the entire zero-hub bank before any local coefficient is inverted.

The newest account03/B04 zero-pivot `3x3` receiver is complementary. If any physical principal triangle is nonsingular it pays that local branch immediately; if all are singular, r41 supplies (3.2), and (3.5) now pays its clean-bank `E_ZZ=0` subbranch.

## 4. A diffuse zero-pivot stress family

For every integer `m>=1`, let

`b0=(1,1,1)/sqrt(3)`,
`c0=(1,2,-3)/sqrt(14)`.                                               (4.1)

These are orthonormal. Let the left physical bank be

`N={1,2,3}`

and the right physical bank be

`L={h,z_1,...,z_m}`.

Define the `3 x (m+1)` physical cross block

`K_m=[2b0, (2/sqrt(m))c0, ..., (2/sqrt(m))c0]`                        (4.2)

with `m` copies of the second column, and put

`A_m=[[0_3,K_m],[K_m^T,0_(m+1)]].`                                   (4.3)

Every one of the `3(m+1)` physical cross coefficients is nonzero. The form is zero-diagonal, genuinely nonseparable in the original product coordinates, and indefinite.

Because

`K_m K_m^T=4(b0b0^T+c0c0^T)`,                                       (4.4)

the nonzero singular values of `K_m` are exactly `2,2`. Therefore

`spec(A_m)={2,2,-2,-2,0^(m)}`.                                       (4.5)

So **every** `A_m` satisfies the exact owner target, with four eigenvalues of modulus two.

Every physical principal `3x3` block of this bipartite matrix is singular. In particular the fresh account03/B04 theorem at `f5e2...` cannot trigger anywhere: its determinant currency is exactly zero on every physical triple. This is a valid obstruction to that local theorem, not to QFORM.

For the anchor `h`, every principal triangle is singular and the partner r41 factorization has `p=0`, `E_ZZ=0`; (3.4) is exactly the entire `K_m`. Therefore Theorem 2.1 gives immediately

`boxed:
 ||p_(X^T A_m X)||_infinity <= sqrt(pi)
 =1.772453850905516...`                                               (4.6)

uniformly in `m` and in every admissible independent input law.

### Sharpening the same family using its exact physical frame

The normal to the plane `span{b0,c0}` is

`d=b0 x c0=(-5,4,1)/sqrt(42).`                                       (4.7)

For

`Z=(b0^T X_N,c0^T X_N)`,

write each fibre as `x=Uz+td` with an orthogonal Jacobian. Dropping every density factor except the original coordinate whose `|d_i|` is largest gives the exact elementary projection cap

`||p_Z||_infinity <=1/max_i|d_i|=sqrt(42)/5.`                         (4.8)

Repeating the proof of Theorem 2.1 with (4.8) instead of the universal cap two yields

`boxed:
 ||p_(X^T A_m X)||_infinity
 <= sqrt(pi sqrt(42)/10)
 =1.426879370091898... .}`                                            (4.9)

Again the bound is uniform in `m`. No assertion of independence is made for the pair `Z`.

## 5. Why local-minor selection loses the aggregate C1 currency

The family is designed to occupy the exact zero-pivot overlap geometry rather than merely supply another easy rank-two example.

Write

`b=2b0`, `c_z=2c0/sqrt(m)`.

The complementary physical `2x2` minors of `[b,c_z]` are the coordinates of

`b x c_z=(4/sqrt(m))d`.                                               (5.1)

Since every `b_n^2=4/3`,

`sum_n b_n^2 det([b,c_z]_(N\{n}))^2=64/(3m).`                         (5.2)

There are `m` choices of `z` and both row/column orientations in the ordered anchored overlap-one compound sum. Hence

`boxed: C_(1,h)(A_m)=128/3}`                                         (5.3)

for every `m`.

But each individual physical packet `{h,z}` has only

`||b wedge c_z||=4/sqrt(m)`.                                         (5.4)

So a mechanism that first selects one `z` before spending rank-two area incurs an artificial reciprocal `m^(1/4)` loss. Equations (4.6)-(4.9) show that grouping the whole clean bank removes this loss exactly. This is an aggregate-before-inversion phenomenon in the literal partner C1 survivor.

## 6. Global optimization of the physical two-volume weights

This same matrix also gives an exact entropy optimization rather than a chosen symmetric ansatz.

The only nonzero physical `2x2` minors of `K_m` use one column `h` and one column `z`. Summed over `z`, their squared-minor masses on row pairs `(23),(13),(12)` are proportional to

`25:16:1`.                                                            (6.1)

Thus

`Z_2=e_2(K_m^T K_m)=16`,                                              (6.2)

and the canonical aggregated volume law is

`nu=(25/42,16/42,1/42).`                                              (6.3)

For arbitrary supported weights, the entropy at fixed row-pair masses is globally maximized by distributing uniformly over the `m` equivalent `z` columns. If

`x=(x_23,x_13,x_12)`,

then exactly

`G_2(w)=16 exp[-D_KL(x||nu)].`                                        (6.4)

The fractional row gate `alpha_i<=q/2` is equivalent to

`x_23,x_13,x_12 >= ell:=1-q/2`,                                      (6.5)

so it is feasible iff

`q>=4/3`.                                                             (6.6)

The exact KL projection of `nu` onto (6.5) is

`x*(q)=
 (q-1,1-q/2,1-q/2),                     4/3<=q<=82/57;
 (25q/82,8q/41,1-q/2),                   82/57<=q<=41/21;
 nu,                                     41/21<=q<2.`                 (6.7)

At the minimal feasible exponent,

`q=4/3`, `x*=(1/3,1/3,1/3)`,

and

`boxed:
 G_(2,opt)=16(50/343)^(1/3)
 =8.42064342546374... .}`                                             (6.8)

For the previously proved entropy-weighted rank-two half-Riesz compiler,

`B_half(q)=4sqrt(2e) q^(-1/4)(2-q)^(-1)G_(2,opt)(q)^(-1/8).`           (6.9)

Direct differentiation on all three KL branches shows `B_half` is strictly increasing, hence its exact global optimum is

`boxed:
 B_half,opt=B_half(4/3)=9.97494811429056... .}`                        (6.10)

This comparison is intentionally labelled correctly: (6.10) controls the half-Riesz potential and is **not by itself** an L-infinity density certificate for the pure bilinear output. The new planar rearrangement changes mechanism and reaches L-infinity directly.

## 7. Pinned e5 volume routes fail globally on the same physical matrix

This is the required application of the pinned e5 results to an actual obstruction, and it is stronger than checking only the natural `N|L` cut.

Let `I,J` be **any** disjoint physical coordinate sets. Split them by the two physical banks. After reordering rows and columns,

`A_m[I,J]
 =diag(K_m[I_N,J_L], K_m[J_N,I_L]^T).`                                (7.1)

Hence

`rank A_m[I,J]
 <= |I_N|+|J_N|
 <=3.`                                                                (7.2)

Therefore for every physical cut

`boxed: e_5(A_m[I,J]^T A_m[I,J])=0.}`                                 (7.3)

The pinned marginal-free D5 theorem has no finite certificate anywhere on this target family.

For D or D', a positive third volume requires cross rank exactly three. That can happen only with

`|I_N|=1` or `|I_N|=2`                                                 (7.4)

and the complementary N-coordinates on the other side. In either case every supported full-rank `3x3` cross minor must contain **every** constrained row in `I_N`: the corresponding block has rank exactly `|I_N|` and there are exactly `|I_N|` such N-rows available. Hence every possible probability weight on nonzero third minors has at least one row marginal

`alpha_i=1.`                                                          (7.5)

Thus there is no admissible weighting at all for either the pinned D gate `alpha_i<=1/2` or the proved D' gate `alpha_i<3/4`, even after globally optimizing over every cut and every supported weight.

This is a source-valid obstruction to those volume compilers, not a counterexample to QFORM. The same matrix is controlled by (4.9).

## 8. The completed direct ridge gate also fails on every cut

Use the same arbitrary cut and write

`B=A_m[I,J]`,
`K_gamma=B B^T(gamma^2I+B B^T)^(-1)`,
`theta=tr K_gamma`.                                                  (8.1)

If `rank B<=2`, then automatically

`theta<2<=2q`                                                         (8.2)

for every admissible `q>=1`, so the ridge trace gate cannot hold.

Suppose `rank B=3`. By (7.4) there are two cases.

**Case `|I_N|=2`.** The rank-two block is supported on exactly those two constrained rows. If the ridge leverage gate holds, its trace is at most `q`. The remaining block has rank one, hence ridge trace strictly below one. Therefore

`theta<q+1<=2q.`                                                      (8.3)

**Case `|I_N|=1`.** The rank-one block on that single N-row contributes at most `q/2`. Rank three forces the other rank-two block to contain the physical row `h`; after deleting that row, all `z`-rows are proportional, so the `z`-compression of its ridge matrix has rank at most one and operator norm strictly below one. Its trace is therefore less than `1+q/2`. Consequently again

`theta<q+1<=2q.`                                                      (8.4)

Thus

`boxed:
 no completed direct-ridge certificate exists for A_m
 on any physical cut, at any gamma>0, for any q>=1.}`                  (8.5)

This is a gate obstruction, not a lower bound on the true density. On the identical matrices, the grouped rearrangement gives the explicit uniform density bound (4.9).

## 9. Same-matrix mechanism comparison

For every `m>=1`, the single target-valid physical matrix `A_m` has all of the following properties simultaneously:

- exact spectrum `{2,2,-2,-2,0^(m)}`;
- every physical principal `3x3` block singular, so the fresh account03/B04 local zero-pivot theorem has no determinant to spend;
- target-scale anchored overlap currency `C_(1,h)=128/3`;
- every selected local `{h,z}` area shrinks like `4/sqrt(m)`;
- globally optimized pair-volume currency remains target-scale (`G_2,opt=8.42064...` at its minimal feasible exponent), but the completed rank-two volume theorem reaches only a fractional potential here;
- every third/fifth-volume e5 density certificate fails on every physical cut;
- every direct ridge certificate fails on every physical cut;
- grouping the entire clean bank before coefficient-space projection gives

`boxed:
 ||p_(X^T A_m X)||_infinity
 <=sqrt(pi sqrt(42)/10)
 <1.427.`                                                             (9.1)

The structural lesson is therefore sharper than “find a better minor”: in the zero-pivot C1 survivor, the right currency can be an **aggregate top-two coefficient norm of an entire original-coordinate clean bank**, even when all fixed local receivers and all higher-volume/ridge gates on the same physical matrix fail.

## 10. Exact remaining gap

The new theorem does not pay a general partner factorization when `E_ZZ` carries quadratic curvature. A small operator norm of `E_ZZ` is not a small random perturbation for arbitrary unbounded input laws, so no perturbative shortcut is licensed. The next useful step must keep product provenance while spending either:

1. lower-order cross currency after conditioning/grouping enough original Z-coordinates to neutralize their self-curvature; or
2. a completed higher-order volume/ridge/projected-crossing endpoint forced quantitatively by that curvature.

No claim beyond this scope is promoted. Full QFORM remains OPEN.

## 11. Deterministic audit and privacy

Exact frame algebra, spectrum, C1 mass, projection constant, pair-volume KL optimizer, and the all-cut volume/ridge obstruction are recorded in `CHECKS.md` in this run directory. No Monte Carlo or benchmark claim is used.

Manual changed-file privacy review: this report, `EARLY_CALC.md`, and `CHECKS.md` contain mathematical research only. They contain no credentials, private personal archives, tokens, scheduler identifiers, machine paths, gold/benchmark answers, or unrelated data. No public release, permission expansion, remote workflow, paid call, email, notification, installation, or task/schedule mutation was performed.
