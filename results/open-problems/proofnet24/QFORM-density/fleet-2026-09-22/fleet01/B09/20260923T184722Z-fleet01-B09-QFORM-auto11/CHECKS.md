# Deterministic checks — fleet01/B09 20260923T184722Z

These are exact algebraic/arithmetic regressions for the proof in `REPORT.md`; they are not substitutes for the analytic argument.

## 1. Constants

The projected-crossing coefficient at `k=0, ell=3` is

`3 * 2^(3/2) * exp(1/2) = 6 sqrt(2e) = 13.98986388958...`.

With `gamma=1/4`, the diffuse-carrier coefficient is

`24 sqrt(2e) = 55.95945555833... < 56`.

For the exact half-frame family, `Z_3>=1/64`, so

`6 sqrt(2e) * (1/64)^(-1/6) = 12 sqrt(2e) = 27.97972777917...`.

The small-fourth-direction threshold in the auxiliary disjoint-volume lemma is

`1/(4 sqrt(30)) = 0.0456435464588...`.

## 2. Exact Hadamard carrier family

Use

`O=(1/2) [[1,1,1,1],[1,-1,1,-1],[1,1,-1,-1],[1,-1,-1,1]]`

and

`K_e = O diag(1,1,-1,e) O^T`.

Direct multiplication gives

`4 K_e =
 [[e+1, -(e+1), 3-e, e+1],
  [-(e+1), e+1, e+1, 3-e],
  [3-e, e+1, e+1, -(e+1)],
  [e+1, 3-e, -(e+1), e+1]].`

Because `O` is orthogonal,

`spec(K_e)={1,1,-1,e}`.

Relative to the two `2+2` coefficient banks, both same-side `2 x 2` blocks have determinant zero. The cross coefficient block has determinant

`det K_e[1:2,3:4]=(1-e)/2`.

Thus at `e=0` it has rank two, as required by the partner exact-dual-zero normalization; for `0<e<1` it remains rank two. At `e=1` it drops to rank one, so the partner's rank-four dual-zero theorem is **not** invoked there. The new balanced-crossing theorem itself remains valid at `e=1`.

At `e=0`, the same-side coefficient blocks have rank one and their physical rows are combinations of the two opposite-bank cross-frame rows, so each singleton-augmented three-volume aggregate in the partner normalization vanishes. Hence the exact endpoint is a legitimate application of fleet02/B09 r20.

## 3. Exact balanced cut

In each physical bank, the two-frame rows are `(1,s_i)/sqrt(N)`, with equally many signs. Take exactly half of the `+` rows and half of the `-` rows into `I`, and the rest into `J`. Then in each bank

`sum_{i in I} p_i p_i^T = (1/2) I_2 = sum_{j in J} p_j p_j^T`.

Therefore for `U=diag(P_N,R_N)`,

`U_I^T U_I=U_J^T U_J=(1/2) I_4`.

The cross block is unitarily equivalent to `(1/2)K_e`, so its singular values are

`1/2, 1/2, 1/2, e/2`.

Hence

`Z_3=e_3(BB^T)
 = 3*(1/4)^2*(e^2/4) + (1/4)^3
 = (1+3e^2)/64 >= 1/64`.

The normalized left frame is `sqrt(2) U_I` times a coefficient orthogonal matrix. Every physical row therefore has squared full-frame leverage

`2*(2/N)=4/N<=1/2` for `N>=8`.

## 4. Random balancing second moment

For `U^T U=I_r`, physical rows `u_i`, and iid Rademacher signs `eps_i`, put

`E=(1/2) sum_i eps_i u_i u_i^T`.

Then cross terms vanish in expectation and

`E ||E||_F^2
 = (1/4) sum_i tr((u_i u_i^T)^2)
 = (1/4) sum_i ||u_i||^4
 <= (q/4) sum_i ||u_i||^2
 = rq/4`.

So some sign choice has `||E||op<=sqrt(rq)/2`, yielding both side Grams at least `(1-sqrt(rq))I_r/2`.

For `r<=4,q<=1/16`, this gives `gamma>=1/4` and `q/gamma<=1/4<1/2`.

## 5. Exterior-power error used only in the auxiliary lemma

If the carrier singular values are `s1>=s2>=s3>=a` and `s4=sigma`, and `S3` is the top-three spectral truncation, then exactly

`|| wedge^3 S - wedge^3 S3 ||_F^2
 = sigma^2(s1^2 s2^2+s1^2 s3^2+s2^2 s3^2)
 <= 3(s1 s2 s3)^2 (sigma/a)^2`.

At `sigma/a<=1/(4sqrt(30))`, this error is at most half the square-root of the `1/40` disjoint Pluecker mass certificate from `EARLY_CHECKPOINT.md`, giving the stated `a^6/160` lower bound after squaring.
