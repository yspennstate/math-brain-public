SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B20, 2026-09-23T15:02:20Z.
attacking: sharpen the nested rank-one tail collar with the pinned D5 theorem, then test whether the partner's E2 half-Riesz branch can be upgraded to L-infinity without explicitly spending the third target spectral direction.

# account02/B20 auto11c — D5 thin-tail sharpening and an exact obstruction to a bare E2 half-Riesz upgrade

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T155833Z-account02-B20-QFORM-auto11c`.
Status: **ESSENTIAL_STEP_APPLIED / D5-TAIL-COLLAR-SHARPENED / E2-HALFRIESZ-ALONE-REFUTED / FULL-QFORM-OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and fresh source pins

The target is unchanged: independent ORIGINAL-coordinate real random variables with probability densities at most one, arbitrary real symmetric `A`, and at least three eigenvalues of `A` of modulus at least one. No Gaussian, log-concave, moment, compact/connected-support, iid, diagonal-basis, or post-rotation-independence assumption is introduced. Continuity is separate.


The newest compatible completed designated partner at the fresh read was account03/B20 r33:

`yspennstate/math-open-problems@82fb3ecce909f03acbbe69b2e9d0def93f85194b`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B20/20260923T144528Z-account03-B20-QFORM-r33/REPORT.md`.

Its first unresolved E2 branch has a literal original-coordinate cross block with fixed `e2` currency and gives either a half-Riesz estimate `<38.907` (or `<39.919` after the nested cut), a paid physical pair, a fixed double-star product, a fixed residual core, or a nested absolute-rank-one packet. The half-Riesz estimates are explicitly fractional credit, not density theorems.

The current same-hour account02/B20 predecessor is

`yspennstate/math-open-problems@c58c4f25cd1d804d03dcc9636465a85879b94fb5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B20/20260923T153203Z-account02-B20-QFORM-auto11b/REPORT.md`.

It leaves, in the nested rank-one packet,

`W=s1 u v^T+R`, `||R||op<1/64`,
`||M||F^2>961/4096` for `M=A[P,Q]`,
`||L||op>sqrt(749373/2097152)` for `L=A[P,K]`,

and proves a D5 payment when `||R||F^2>=1/64`.

The required pinned interactive source is

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`.

Its unrestricted physical fifth-volume theorem D5 says for every literal original-coordinate cross block `T`, with `Z5=e5(T^T T)`,

`||p_Q||inf <= 5 sqrt(2e) Z5^(-1/10)`,

with arbitrary same-bank quadratic blocks and all outside couplings retained. I apply this theorem below at a strictly smaller tail threshold than the predecessor.

I also use the completed physical E2 determinant-law half-Riesz theorem from account03/B06 r37,

`yspennstate/math-open-problems@fa9d5dd3cc78a092484480b536872d332e22c90a`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B06/20260923T141825Z-account03-B06-qform-r37/REPORT.md`,

and the product-projection theorem `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1`,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

All live corrections are retained: no law-uniform pointwise phase decay, no worst-fiber supremum, no arbitrary-joint three-dimensional coarea bound, no post-rotation independence, no one-good-minor inference from aggregate volume, and no deletion of a small nonzero quadratic tail.

## 2. Pinned D5 sharpens the nested Frobenius collar by a factor four in norm

Keep the predecessor notation

`W=s1 u v^T+R`, `x_r=s_r(W)^2` for `r>=2`,
`T=||R||F^2=sum_(r>=2)x_r`,

with every `x_r<1/4096` because `||R||op=s2(W)<1/64`.
The partner's strong arm gives `s1>19/32`, hence `s1^2>361/1024`.

The predecessor proved the elementary whole-tail inequality

`e4(x_2,x_3,...) >= T(T-c)(T-2c)(T-3c)/24`, `c=1/4096`,

whenever `T>=3c`.

Take the new threshold

`T>=1/1024=4/4096`.

Then, exactly,

`T(T-c)(T-2c)(T-3c)/24
 >= (4*3*2*1)/(24*4096^4)
 =1/4096^4`.

Therefore

`Z5=e5(W^T W)
 >= s1^2 e4(x_2,x_3,...)
 > (361/1024)/4096^4
 =361/288230376151711744.`

Apply the pinned D5 theorem to the literal original-coordinate cut `P | (Q union K)`:

`||p_Q||inf
 <5 sqrt(2e) (361/288230376151711744)^(-1/10)
 =360.4586881... <360.459.`

Thus every still-unpaid nested absolute-rank-one state obeys the sharper deterministic collar

`boxed: ||R||F^2<1/1024, hence ||R||F<1/32.`

No random tail was discarded; its fifth symmetric singular volume pays the complementary branch.

This also improves one of the two top-rank-one physical arms. Since `||M||F>31/64` and `M=s1uv_Q^T+R_Q`,

`s1||v_Q|| >= ||M||F-||R_Q||F >31/64-1/32=29/64.`

The other arm remains

`s1||v_K|| > sqrt(749373/2097152)-1/64
 =0.5821449321... >37/64`,

using the stronger inherited operator tail bound on `R_K`.

Hence the current thin nested packet can be recorded with

`boxed: ||R||F<1/32, ||R||op<1/64, s1||v_Q||>29/64, s1||v_K||>37/64,`

in addition to the predecessor's transverse same-bank curvature resource `>63/64` and literal internal physical cross energy `>3721/65536`.

## 3. Exact route counterexample: E2 half-Riesz credit alone cannot imply L-infinity

The next question is whether the partner's `<38.907` / `<39.919` half-Riesz branches can be upgraded abstractly to a density bound without spending the third target spectral direction. The answer is **no**, even inside the product quadratic class and even with a stronger physical E2 packet than the current lower bound.

### Theorem — `QFORM-E2-HALFRIESZ-ALONE-NOT-LINF-v1`

There is an explicit family of symmetric matrices and cap-one independent product laws such that:

1. all physical diagonals vanish and all physical `2x2` principal determinant magnitudes are `<1/64`;
2. there is a literal original-coordinate cross cut `N` with
   `||N||F^2=25/32>11907/16384`, `s3(N)=0<1/64`, and
   `e2(N^T N)=49/4096`;
3. the canonical squared-`2x2`-minor law has row and column pair-disjointness at least `13/28`, so the completed E2 theorem gives the finite uniform half-Riesz bound `<17.015`;
4. nevertheless the quadratic output density is logarithmically unbounded.

The matrices have only two large eigenvalues, so this is **not** a counterexample to QFORM. It refutes only the proposed implication “E2 half-Riesz credit by itself upgrades to L-infinity.”

### Construction and proof

Let `m>=8` be divisible by four and put `n=4m`. Split the physical coordinates into two groups `P0,M0`, each of size `2m`. Define orthonormal vectors

`r_+=n^(-1/2)(1,...,1)`,
`r_-=n^(-1/2)(+1 on P0, -1 on M0)`,

and

`A_m=r_+r_+^T-r_-r_-^T`.

Thus `A_m` has nonzero spectrum exactly `{1,-1}`. Its diagonal is zero, and

`(A_m)_{ij}=0` on a same-sign pair,
`(A_m)_{ij}=1/(2m)` on an opposite-sign pair.

Accordingly every physical principal pair determinant has magnitude either zero or

`1/(4m^2)<=1/256<1/64`.

Now make an original-coordinate cut `J | K` as follows. Put `7m/4` coordinates of `P0` and `m/4` coordinates of `M0` in `J`, with the complementary coordinates in `K`. In the sign-group bases the cross block is

`N=[[0, c 1_{(7m/4)x(7m/4)}],
    [c 1_{(m/4)x(m/4)},0]],    c=1/(2m)`.

Therefore its only nonzero singular values are exactly

`s1(N)=7/8`, `s2(N)=1/8`,

so

`||N||F^2=49/64+1/64=25/32
       =11907/16384+893/16384`,

and

`Z2=e2(N^T N)=s1^2s2^2=49/4096`.

Every nonzero `2x2` cross minor uses one row from each sign group and one column from each sign group, and all such minors have the same squared magnitude. Hence the row-pair marginal is uniform on

`(7m/4)*(m/4)`

opposite-sign row pairs, and the column marginal is the same with the factors exchanged. Two independent row-pair samples are disjoint with probability

`delta_R=(1-4/(7m))(1-4/m)`,

and `delta_C=delta_R`. At `m=8`,

`delta_R=delta_C=13/28`,

and this is the smallest value in the stated family.

Apply the completed E2 half-Riesz theorem to this literal two-bank quadratic form. At `m=8`,

`sup_t E|Q-t|^(-1/2)
 <=4 sqrt(2e) (49/4096)^(-1/8) (13/28)^(-1/16)
 =17.01447806... <17.015.`

Now take all input coordinates iid Uniform[-1/2,1/2], whose densities equal one. Let

`S_P=sum_{i in P0}X_i`, `S_M=sum_{i in M0}X_i`.

These are independent, and if `h_m` is their common density, then `h_m` is continuous with `h_m(0)>0`. Directly,

`Q=X^T A_m X
 =[(S_P+S_M)^2-(S_P-S_M)^2]/n
 =S_P S_M/m.`

Choose `d>0` and `c0>0` such that `h_m(x)>=c0` for `|x|<=d`. For `q>0` with `mq<d^2`, the product-density formula gives

`p_Q(q)=m int_R h_m(y) h_m(mq/y) dy/|y|`

and therefore, restricting to `y in [mq/d,d]`,

`p_Q(q) >= m c0^2 int_(mq/d)^d dy/y
         = m c0^2 log(d^2/(mq)) -> infinity`

as `q downarrow0`.

Thus `||p_Q||inf=infinity` although the physical E2 half-Riesz potential is uniformly finite and all the stated local no-pivot/cross-tube inequalities hold. The missing hypothesis is precisely the third target spectral direction.

## 4. A quantitatively useful replacement: a source-separated third square does upgrade half-Riesz to density

The obstruction above also identifies the right positive interface.

### Lemma — `QFORM-HALFRIESZ-PLUS-DISJOINT-SQUARE-v1`

Let `R0` be any real random variable satisfying

`H:=sup_t E|R0-t|^(-1/2)<infinity`.

Let `X_K` be an ORIGINAL-coordinate product bank independent of `R0`, each coordinate having density at most one. Let `r` be a deterministic unit vector on that bank, `c` a constant, and

`S=lambda (r^T X_K+c)^2`, `lambda!=0`.

Then

`boxed: ||p_(R0+S)||inf <= sqrt(e) H / sqrt(|lambda|).`

Proof. The completed weighted affine-fiber Brascamp-Lieb theorem with `k=1` gives a density `g` for `r^T X_K+c` with `||g||inf<=sqrt(e)`. Therefore the square variable `S` has the one-sided density bound

`p_S(s)<=sqrt(e) |lambda|^(-1/2)|s|^(-1/2)`

(on the sign-compatible side). Independence gives, for every `t`,

`p_(R0+S)(t)=E p_S(t-R0)
 <=sqrt(e)|lambda|^(-1/2)E|t-R0|^(-1/2)
 <=sqrt(e)H/sqrt(|lambda|).`

This uses the full projected density before the square singularity and never asserts independence of rotated coordinates within the bank.

Applied to the partner's exact credits, a genuinely source-separated square with `|lambda|>=1` would give

`H<38.907  => ||p||inf<64.147`,
`H<39.919  => ||p||inf<65.816`.

The current unresolved QFORM branch does not yet supply such a disjoint square for free; its third spectral resource is entangled with the same original banks. The lemma therefore states a useful paid replacement, not a completion of the target.

## 5. Updated first unpaid implication

The route counterexample changes the proof map. A generic “upgrade the E2 half-Riesz branch” is false unless the third target direction is used simultaneously. The sharp current obligation is therefore:

`QFORM-N3-THIRDRESOURCE-COUPLED-HALFRIESZ-OR-THIN-NESTED-PAYMENT-v1`.

Under the original independent cap-one product hypotheses and `A in N3(1/64)` with `s3(A)>=1`, prove a universal density estimate by combining the third spectral resource with either:

- the partner's E2 high-disjointness half-Riesz packet, rather than treating that packet alone; or
- the double-star/residual-core alternatives; or
- the sharpened nested packet
  `||R||F<1/32`, `||R||op<1/64`, `s1||v_Q||>29/64`, `s1||v_K||>37/64`, plus rank-one-subtracted same-bank curvature `>63/64` and a literal internal cross energy `>3721/65536`.

A viable next mechanism must spend the third direction before reciprocal localization: e.g. extract a genuinely source-separated square/hyperbolic bank, or prove an aggregate three-resource Brascamp-Lieb/volume estimate on the existing physical banks. Bare half-Riesz interpolation cannot close the target, and perturbative deletion of the nonzero tail remains forbidden.

Full QFORM remains OPEN. No valid target counterexample was found. Global continuity remains OPEN separately.
