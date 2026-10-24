# QFORM-ADAPTIVE-LEVERAGE-DETERMINANT-v1

Status: **proved supporting improvement; not an unconditional reduction of the 17-eigenvalue theorem**.

Pinned baseline manuscript: source commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, source blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

This theorem interpolates continuously between the baseline fourth-power determinant estimate (`q=2`) and the preceding B04 leverage-half second-power estimate (`q=1`). It preserves original-coordinate product provenance and allows arbitrary measurable within-bank phases.

## Theorem

Let `X_I,X_J` be disjoint original-coordinate subvectors with independent coordinate densities bounded by one, let `F,G` be arbitrary real measurable functions finite almost surely, and

`Z = F(X_I) + 2 X_I^T M X_J + G(X_J)`.

Write the physical rows of `M` as `m_i^T`, and define their row leverages

`ell_i = m_i^T (M^T M)^dagger m_i`,

with `ell_i=0` for a zero row. Put `beta=max_i ell_i`.

For every `q in [1,2]` satisfying

`beta <= q/2`,

one has for all real `t`

`|phi_Z(t)| <= det(I + q t^2 M^T M/(2*pi^2*e^2))^(-1/(4q)).`       (1)

Consequently, for any integer `k>=1` with `Z_k(M)>0` and `k>2q`, the law of `Z` has a bounded continuous density and

`||p_Z||_infinity <= [sqrt(2)*e/sqrt(q)] * [k/(k-2q)] * Z_k(M)^(-1/(2k)).`       (2)

The endpoint `q=2` reproduces the baseline determinant theorem and, at `k=5`, exactly reproduces the baseline constant `5e Z_5^{-1/10}`.

## Proof of (1)

The baseline second-power decoupling inequality is

`|phi_Z(t)|^2 <= E_D Y(D)`,

where

`Y(D)=prod_i |hat f_i(2t(MD)_i)|`,

and `D=X_J-X'_J` has independent coordinate densities `g_j<=1`.

For `q>=1`, Jensen gives

`|phi_Z(t)|^(2q) <= (E Y)^q <= E Y^q`.

Set

`a=2t`,

`alpha_q = 8*pi^2*e^2/q = [2*pi*e*sqrt(2/q)]^2`,

`H=alpha_q I + a^2 M^T M`,

and define the graph-frame weights

`c_j = alpha_q e_j^T H^{-1}e_j`,

`d_i = a^2 m_i^T H^{-1}m_i`.

Exactly as in the baseline proof,

`sum_j c_j u_j u_j^T + sum_i d_i v_i v_i^T = I`

after normalizing the corresponding vectors, and

`theta=sum_i d_i=sum_j(1-c_j)`.

The crucial leverage comparison is

`d_i <= ell_i <= beta <= q/2`.       (3)

Indeed, on an eigenvector of `G=M^T M` with eigenvalue `lambda>0`,

`a^2/(alpha_q+a^2 lambda) <= 1/lambda`,

and each row vector `m_i` lies in `range(G)`, so Loewner comparison on that range gives (3).

Now apply geometric rank-one Brascamp--Lieb after `x=H^{-1/2}z` to the coordinate factors `g_j` and row factors

`h_i(u)=|hat f_i(u)|^q`.

The difference-density factors satisfy `||g_j||_{1/c_j}<=1`. For a nonzero row weight `d_i`, (3) gives

`p_i=q/d_i >=2`.

The baseline scalar Fourier-power lemma therefore yields

`||h_i||_{1/d_i}
 = (int |hat f_i(u)|^(q/d_i) du)^(d_i)
 <= [2*pi*sqrt(2e*d_i/q)]^(d_i).`

The row Jacobian contributes `d_i^(-d_i/2)`, so all powers of `d_i` cancel. The coordinate entropy factor satisfies

`prod_j c_j^(-c_j/2) <= e^(theta/2)`.

Thus the total scalar factor left after Brascamp--Lieb is

`[2*pi*sqrt(2e/q) * sqrt(e) / sqrt(alpha_q)]^theta
 = [2*pi*e*sqrt(2/q)/sqrt(alpha_q)]^theta
 =1`.

Factoring `alpha_q^d` from `det H`, we obtain

`E Y^q <= det(I+a^2 M^T M/alpha_q)^(-1/2)`.

Taking the `1/(2q)` power and using `a=2t` gives exactly

`|phi_Z(t)| <= det(I+q t^2 M^T M/(2*pi^2*e^2))^(-1/(4q))`.

Rows with `d_i=0` contribute Fourier factor one and are omitted, exactly as in the baseline proof.

## Volume consequence and constant

Cauchy--Binet gives

`det(I+z M^T M) >= z^k Z_k(M)`.

Applying this to (1),

`|phi_Z(t)| <= min(1,(u/|t|)^(k/(2q)))`,

with

`u = sqrt(2)*pi*e*q^(-1/2) Z_k(M)^(-1/(2k)).`

If `k>2q`, the exponent `p=k/(2q)` is greater than one. The baseline power-envelope lemma gives

`||p_Z||_infinity <= u*p/[pi(p-1)]
 = [sqrt(2)*e/sqrt(q)] [k/(k-2q)] Z_k(M)^(-1/(2k))`,

which is (2). The envelope is integrable, so Fourier inversion also gives continuity on this branch.

## Exact useful specializations

Let `beta=max_i ell_i` and choose the smallest admissible `q=max(1,2 beta)`.

### Order three

If `beta<3/4`, order-three crossing volume is directly density-integrable.

For `beta<=1/2`,

`||p_Z||_infinity <= 3*sqrt(2)*e*Z_3(M)^(-1/6)`.

For `1/2<beta<3/4`, taking `q=2beta` gives

`||p_Z||_infinity <= [3e/(sqrt(beta)(3-4beta))] Z_3(M)^(-1/6)`.       (4)

Thus the previous hard leverage cap `1/2` is not intrinsic: the true threshold of this interpolation for cubic volume is `3/4`, with the expected blow-up at the endpoint.

### Order four

If `beta<1`, order-four crossing volume already gives a bounded density. For `1/2<beta<1`,

`||p_Z||_infinity <= [e/(sqrt(beta)(1-beta))] Z_4(M)^(-1/8)`.       (5)

The only unresolved leverage endpoint for order four is `beta=1` (or a sequence tending to one if a uniform constant is required).

### Order five

At the worst possible leverage `beta=1`, choose `q=2`. Formula (2) becomes

`||p_Z||_infinity <= 5e Z_5(M)^(-1/10)`,

exactly the manuscript's unrestricted order-five receiver. Thus the baseline theorem is the `q=2` endpoint of this same family.

## Counterexample to an automatic order-four leverage gap

The adaptive theorem does **not** by itself reduce the fixed multiplicity from 17 to 13, because target-scale order-four volume does not automatically imply `beta<1` for the particular physical crossing carrying that volume.

Here is an explicit no-pivot `s_13>=1` matrix exhibiting this obstruction.

Let `eta=1/100` and `kappa=1/80^2`, as in the manuscript. Take the direct sum of:

1. seven disjoint star adjacency matrices, each with 400 leaves and edge weight `c=1/20`; and
2. the `8x8` pure-cross block

`A_small = [[0, delta I_4],[delta I_4,0]]`, with `delta=9/100`.

Each weighted star has spectrum `{+c sqrt(400), -c sqrt(400), 0,...,0}={+1,-1,0,...,0}`. Therefore the seven stars contribute fourteen singular values equal to one, so the full symmetric matrix satisfies

`s_13(A)=1`.

All diagonal entries vanish. Every nonzero physical off-diagonal entry has magnitude either `1/20` or `9/100`; hence every principal two-coordinate determinant has magnitude at most

`max((1/20)^2,(9/100)^2)=81/10000 < 1/100=eta`.

So the matrix has **no manuscript eta-pivot**.

Now choose a physical partition with the four left coordinates of `A_small` on the row side, its four right coordinates on the column side, and put every star coordinate on the row side. The crossing matrix consists of `delta I_4` together with zero rows. Hence

`Z_4(M)=delta^8=(9/100)^8=43046721/10^16 ~= 4.3046721e-9`,

while the manuscript's order-four random-cut target would be only

`4^(-4) kappa^4 = 1/429496729600000000 ~= 2.3283064e-18`.

Thus this crossing has enormously more than target-scale fourth volume. Nevertheless each of its four nonzero rows has leverage exactly one, so

`beta=1`.

This construction does **not** prove that every useful crossing of the full matrix has leverage one; in fact other partitions may exploit the diffuse star leaves. What it rigorously rules out is the shortcut

`target-scale Z_4 on a selected physical crossing => a uniform leverage gap below 1`.

Any complete 13-eigenvalue proof using order-four volume therefore needs an additional selection theorem guaranteeing a different diffuse crossing, or a genuine endpoint/high-leverage receiver. Formula (5) alone is not enough.

## Threshold status

This run does **not** claim an unconditional reduction below 17. The complete baseline 17-eigenvalue theorem remains the only fixed-multiplicity theorem established here. The new result sharpens the analytic side of the lower-threshold problem:

- order 3 is enough when physical row leverage is `<3/4`;
- order 4 is enough whenever physical row leverage is `<1`;
- order 5 handles the endpoint `beta=1` uniformly and recovers the baseline.

The next exact obligation for a 17-to-13 reduction is therefore an endpoint dichotomy for the no-pivot order-four crossing: force a uniform physical leverage gap, or pay the `beta~1` carrier by a separate product-preserving argument. No unrestricted three-eigenvalue conclusion is asserted.
