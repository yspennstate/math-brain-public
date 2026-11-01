# fleet01/B05 improvement — multiplicity nine review and overlap-one frequency Jacobian

Run: `20260924T145314Z-fixed-multiplicity-audit-r11`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status:

1. **PASS review** of the sharpened multiplicity-nine candidate `||p_Q||_infinity <=400 K^2/s`. This run is one independent worker review of that sharpened constant; it does not self-award the owner's two-review validation gate.
2. **New exact structural theorem** `QFORM-OVERLAP1-FREQUENCY-JACOBIAN-v1`, converting every shared-anchor overlap-one minor into the determinant of the three physical frequencies in the dependence-safe retained-copy formula.
3. Multiplicity eight remains **OPEN/GAP**. The new identity localizes the missing analytic factor but does not claim an `s_8` density theorem.

# I. Independent review of the sharpened multiplicity-nine theorem

The candidate reviewed is:

> For arbitrary real symmetric `A`, arbitrary affine `b,c`, and independent real coordinates with densities bounded by `K`, if `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density and
> 
> `||p_Q||_infinity <=400 K^2/s`.

I reconstructed the proof rather than inheriting the claimed status.

## I.1 Grouped compiler and rough-law passage

For disjoint literal source banks `H,I,J`, with `k=|H|` promoted hub coordinates and residual exterior order `ell`, the grouped compiler has

`|phi_Q(t)| <= min(1,B_(k,ell)|t|^(-(k+ell)/2))`.

The delicate rough-law step is valid as follows. First mollify the phase-weighted pushforward through the full-rank `J` coefficient map. Conditional on the original `I` bank, translation does not change the mollified `L^2` norm. Jensen in the Hilbert space `L^2`, expansion with an independent `J` copy, and only then integration over the original independent `I` coordinates leaves the physical characteristic factors. Weighted Holder is taken against the nonnegative mollifier kernel. The deterministic map

`D -> (M_J D,(c_i D)_(i in T))`

has Gram determinant

`det(M_JM_J^T) det(C_TC_T^T)`

because the `c_i` are orthogonal to `row(M_J)`. The product-projection theorem is therefore used only as a joint density theorem for a deterministic linear image, not as post-rotation independence. The bound is uniform in the mollifier scale and passes to the rough law by the approximate-identity/Fourier limit.

Heavy determinant marginals are promoted only as literal physical coordinates. The entropy identity

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`

pays the determinant geometric mean without a dimension/cardinality loss.

For order three this yields

`||p_Q||_infinity <= C3 E_3(M)^(-1/6)`,

`C3=3 sqrt(2)e(9/2)^(1/6)=14.818337662843... <15`.

For order two it yields the full half-potential endpoint

`sup_a E|Q-a|^(-1/2) <= C2 E_2(M)^(-1/8)`,

`C2=8 sqrt(e)2^(-1/8)=12.095072570796... <14`.

The order-two result is not misused as a bounded-density theorem.

## I.2 Retuned structural parameters

The sharpened proof uses

`d=3/40`, `p=1/400`, `h=2/25`, `kappa=h^2=4/625`.

With no scalar pivot and no two-coordinate determinant pivot,

`|A_ii|<d`,

`|A_ij|^2<p+d^2=13/1600`, hence `|A_ij|<1/11`.

For `k=1,2,3`, the baseline interpolation proof retunes to

`no pivot and s_(4k-3)(A)>=1  =>  V_k(A)>=kappa^k`.

If a bad ratio occurs at `r=0`, then `||off A||_F<h`, so `||A||<d+h<1`, contradiction. For `r=1,2`, completion gives `epsilon<=(r+1)h`; the restricted diagonal-dominance surplus is

- `r=1`: `1-d-1/11-4h = 1131/2200 >0`;
- `r=2`: `1-d-2/11-9h = 51/2200 >0`.

Thus the restricted rank contradiction still closes. A fair physical cut then gives

`E_k(M)^(-1/(2k)) <= 2/h =25`.

Consequently the no-pivot `s_9` branch has

`||p_Q||_infinity <25 C3 =370.459 <375`.

## I.3 Improved small-ball/log and pair half-potential inputs

The off-diagonal quarter-power smoothing coefficient is bounded by `<5`; combined with the scalar-diagonal branch this gives

`sup_a P(|R-a|<u) <= min(1,5(u/L)^(1/4))`

when `L=||A||`. Therefore, for `L>=1`,

`sup_a E log_+(1/|R-a|) <= L0=4+4log5`.

The sharpened two-kernel identity is

`J(d)<=J0+2log_+(1/|d|)`, `J0=pi+4log2`.

For an arbitrary quadratic polynomial in two independent cap-one physical coordinates with two-by-two quadratic determinant modulus `D>0`, the full half potential satisfies

`sup_a E|Q-a|^(-1/2) <16 D^(-1/4)`.

For a definite pair this follows from the density cap `pi/sqrt(D)`. For an indefinite pair, after output scaling by `sqrt(D)`, the density envelope is

`h(z)<=6+log_+(16/|z|)`.

Splitting at `delta=1/64`, the far contribution is `8` and the near contribution is at most `4+5log2`, so the total is `12+5log2<16`. This is a full half potential and hence can be averaged uniformly over random affine/critical translations.

## I.4 Final normalized cases

Under `s_9(A)>=1`:

- no pivot: `<375`;
- scalar pivot, Schur remainder no pivot: the order-two full half potential is `<70`, so the outer square profile is `<70/sqrt(d)<280` (actual checked value using `C2` is about `220.825`);
- scalar pivot followed by scalar pivot: `d^(-1/2)+(J0+2L0)/d <383` (actual value about `360.848`);
- scalar pivot followed by two-coordinate pivot: `<16 p^(-1/4)d^(-1/2)<320` (actual value about `261.279`);
- definite pair pivot: `pi/sqrt(p)<80`;
- indefinite pair pivot: `p^(-1/2)(6+log16+L0)+1/e <392.5` (actual value about `384.575`).

The cases exhaust the pivot/no-pivot alternatives. Scaling `Y=KX` and `A -> A/s` gives `K^2/s` exactly.

**Review verdict:** PASS for the sharpened multiplicity-nine theorem as a mathematical candidate. I do not change the owner-level validation state in this run.

# II. New theorem: overlap-one minors are exact retained-copy frequency Jacobians

The terminal multiplicity-eight work now supplies strong shared-anchor overlap-one determinant mass. The missing link in the B05 lens is to identify exactly what that determinant measures before any rotated conditional law is introduced.

## Theorem `QFORM-OVERLAP1-FREQUENCY-JACOBIAN-v1`

Let `A=A^T`. Fix three distinct outside coordinates

`U={i,j,k}`

and a disjoint literal physical anchor pair

`H={h_1,h_2}`.

Write the full quadratic polynomial as a function of the original-coordinate bank `X_U` and the disjoint bank containing `X_H`. Apply the dependence-safe one-copy identity to the `U` bank, retaining the same-bank quadratic phase on `U` rather than discarding it.

Let

`d=(d_i,d_j,d_k)=X_U-X'_U`.

The three physical frequencies consisting of

1. the retained sum-frequency for the shared coordinate `i`, and
2. the two ordinary Fourier frequencies generated by the anchor coordinates `h_1,h_2`,

are, apart from the common scalar factor `t` or `2t`, the linear forms

`xi_i(d)=A[i,U] d`,

`y_1(d)=A[h_1,U] d`,

`y_2(d)=A[h_2,U] d`.

Therefore the Jacobian of the frequency map

`d -> (xi_i(d),y_1(d),y_2(d))`

is exactly

`boxed: det A[{i,h_1,h_2},U]`.

In particular, every fixed-anchor overlap-one third minor is not merely a combinatorial exterior-volume token: it is exactly the physical three-frequency Jacobian present in the retained-copy product integral.

### Proof

For the copied bank `U`, the retained same-bank phase is

`X_U^T A[U,U] X_U - X'_U^T A[U,U] X'_U
 = d^T A[U,U](X_U+X'_U)`.

Hence the partial Fourier transform in the `i`-th sum coordinate is evaluated at the frequency

`(A[U,U]d)_i=A[i,U]d`.

The bilinear interaction with the two literal anchor variables is

`2 X_H^T A[H,U] X_U`.

After the independent-copy expansion on `U`, integration in the two original anchor variables produces their scalar Fourier factors at frequencies proportional to

`(A[H,U]d)_1=A[h_1,U]d`,

`(A[H,U]d)_2=A[h_2,U]d`.

Thus the coefficient matrix of the three displayed frequencies, in the coordinate order `(i,j,k)`, is precisely

`A[{i,h_1,h_2},U]`.

Taking its determinant proves the identity. No random coordinate rotation occurs anywhere in this derivation. QED.

## Seed/Schur form of the identity

Suppose additionally that the two-by-two seed

`B=A[H,{j,k}]`

is invertible. Put

`r=A[H,{i}]`,

`q^T=A[i,{j,k}]`,

`a=A[ii]`,

and

`Delta=det A[{i} union H,{i,j,k}]`.

Changing only deterministic integration variables from `(d_j,d_k)` to

`y=A[H,U]d = r d_i + B(d_j,d_k)^T`

has Jacobian `|det B|`. The retained frequency becomes

`xi_i = sigma d_i + q^T B^(-1)y`,

where

`boxed: sigma=a-q^T B^(-1)r=Delta/det B`.

This is just the bordered-determinant/Schur identity, but here it has a direct analytic meaning: `sigma` is the residual slope of the retained ambiguity frequency after the two anchor Fourier frequencies are fixed.

# III. What this does and does not close at multiplicity eight

Let

`Omega_H^(1)=sum_{i,U: i in U} det A[H union {i},U]^2`

be the current fixed-anchor overlap-one mass. The recent terminal reduction gives a dimension-free positive lower bound for this quantity in the unpaid normalized `s_8` collar. By Theorem II, this is therefore **aggregate squared Jacobian mass for the actual retained-copy frequency maps**. This eliminates a conceptual gap: the overlap currency lives in exactly the analytic variables needed by a product-preserving proof.

However, a naive packet-by-packet change of variables pays

`|det B|^(-1)`

before it can use the residual slope `sigma=Delta/det B`. Individual seed determinants may be arbitrarily small even when the aggregate overlap mass is bounded below. Thus selecting and inverting one seed first can reintroduce an uncontrolled reciprocal-minor factor.

There is a second endpoint deficit. The ambiguity function for one copied original coordinate obeys

`int |H_i(d,xi)|^2 dxi <= pi g_i(d)`,

and the anchor Fourier factors have only the source-valid scalar `L^p`, `p>=2`, control. A direct Holder/Brascamp--Lieb allocation using one ambiguity `L^2` factor and two scalar Fourier `L^2` factors produces only a `|t|^(-3/2)` gain at the squared-characteristic-function level in the natural three-frequency packet. That is weaker than the `|t|^(-2-epsilon)` squared-level decay needed for an integrable characteristic function. This calculation is a diagnosis of the straightforward norm allocation, not an impossibility theorem.

Accordingly, the exact remaining B05 obligation is:

**GAP `QFORM-S8-OVERLAP1-AGGREGATE-FREQUENCY-RECEIVER`.** Prove a product-preserving inequality that aggregates the nonzero Jacobians

`det A[H union {i},U]`

*before reciprocal seed inversion* and combines them with the already available critical order-four / robust-anchor endpoint to gain any integrable improvement beyond `|phi_Q(t)|=O(1/|t|)`, or prove an equivalent direct interval bound `P{Q in I}<=C|I|`.

The retained-copy formula is the correct place to attempt this because it keeps the true dependence between difference and sum coordinates. Conditioning on an orthogonally rotated/projected coordinate and reusing a marginal projection cap would be invalid.

# IV. Current threshold status

- Baseline 17-eigenvalue manuscript: PASS in the sibling full audit.
- Multiplicity nine: complete mathematical theorem; the sharpened constant-400 version receives a PASS from this run but is not self-promoted to owner validation.
- Multiplicity eight: OPEN. Existing finite-`L^r` / critical `1/|t|` estimates do not imply `L^infinity`; the hyperbolic product example shows that endpoint is genuinely insufficient.
- Unrestricted three-eigenvalue conjecture: OPEN.
- Global continuity is not asserted for the pivot branches; the claims here concern essential density bounds unless a specific Fourier branch supplies a continuous `C_0` representative.
