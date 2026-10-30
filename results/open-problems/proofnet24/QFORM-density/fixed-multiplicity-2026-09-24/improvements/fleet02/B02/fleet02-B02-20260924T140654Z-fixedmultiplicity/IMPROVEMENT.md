# fleet02/B02 — independent review of the nine-direction replacement and 549 retuning

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Canonical manuscript pin: blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Retuned candidate reviewed here: `fleet01/B02` artifact at commit `dc13ef5fa9e4a90ab8fc07a89a714beda7b70050`, blob `6d01aea567d60fe837eb1f59cdfd837aa61e7f24`.

## Verdict

**PASS in this independent mathematical review:** the full nine-eigenvalue theorem is valid under the original hypotheses, and the retuned explicit constant `<549 K^2/s` is supported by a complete replacement argument.

Precisely: if the coordinates are independent real variables with densities bounded by `K`, `A=A^T` is arbitrary, `b,c` are arbitrary, and `s_9(A)>=s>0`, then `Q=X^TAX+b^TX+c` has an essentially bounded density with

`||p_Q||_infinity < 549 K^2/s`.

No moment, support, sign, log-concavity, exact-rank, diagonal-basis, leverage, smoothness, or post-rotation-independence assumption is added. Global continuity is not asserted. This review does **not** self-award owner/release validation status; the retuned `<549` version still requires another genuinely separate complete review under the owner gate. The unrestricted three-eigenvalue conjecture remains open.

## 1. Grouped product-Fourier engine — independent reconstruction

The nine-direction replacement changes the analytic endpoint from fifth crossing volume to third crossing volume. For literal original-coordinate banks `H,I,J`, keep all same-bank quadratic/affine phases inside complex pushforwards. If `W` is a `k`-dimensional projection of the hub bank with density cap `M_H`, the hub pushforward `a_t` satisfies

`|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`, and Plancherel with the manuscript convention gives

`int |ahat_t(2t(l+beta))|^2 dl <= M_H (pi/|t|)^k`.

For the light bank, condition only on original coordinates, mollify the complex pushforward, expand its `L^2` norm with one independent copy of the appropriate physical bank, and pass to the limit by weak `L^2` compactness/lower semicontinuity. Pure same-bank phases have modulus one or cancel; the remaining factors are scalar characteristic functions of independent original coordinates. No projected-coordinate independence is asserted.

For an `ell`-subset `T`, after projecting rows off the promoted row space, the deterministic map has Gram determinant

`S^2 det(C_T C_T^T)`.

The canonical product-projection bound gives density cap `e^((k+ell)/2)/(S sqrt(det(C_T C_T^T)))`. Weighted Holder uses inclusion marginals `alpha_i`; when `alpha_i<=1/2`, the scalar Fourier-power lemma applies at `p=1/alpha_i`. Uniformly ordering the sampled subset gives

`H(w)+sum_i alpha_i log alpha_i <= ell log ell-log(ell!)`.

Combining the factors yields the reviewed compiler

`|phi_Q(t)| <= min(1,K_{k,ell}|t|^{-(k+ell)/2})`

with

`K_{k,ell}=M_H^(1/2) pi^((k+ell)/2) 2^(ell/4) e^((k+2ell)/4)
 (ell^ell/ell!)^(1/4) S^(-1/2) Z_ell^(-1/4)`.

This directly gives the marginal-free physical-crossing receivers

`||p_Q||_infinity <= C_3 E_3(M)^(-1/6)`,
`C_3=3 sqrt(2) e (9/2)^(1/6)<15`,

and

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`,
`C_2=8 sqrt(e) 2^(-1/8)<13`.

I checked the promotion identities and terminal exact-rank cases. Heavy third-volume rows are promoted physically; Gram--Schmidt gives `J_i=||w||^2 E_2(C)`, then `H_ij=det(PP^T)||C_2||_F^2`, and the last heavy row gives a physical three-row Gram determinant. The order-two tree is the same one dimension lower. All branches retain arbitrary same-bank curvature.

## 2. Retuned structural constants — PASS

The `<549` candidate chooses

`eta=1/21`, `sqrt(kappa)=1/18`, `kappa=1/324`.

No pivot implies

`|a_ii|<1/21`, `|a_ij|<sqrt(22)/21`.

For crossing orders `k<=3`, the canonical sampled completion still gives `A=D+R+E`, global `rank R<=3r`, restricted `rank R[L,L]<=r`, zero diagonal `E`, and `D=0` on the seed. If a bad ratio occurs at `r<=2`, then `||E||_F<(r+1)/18`.

The only tight structural case is `r=2`. Three forced diagonal entries satisfy

`|R_ii|>1-1/6-1/21=11/14`,

whereas each row's two off-diagonal entries total less than

`2(sqrt(22)/21+1/6)`.

Strict dominance is equivalent to `4 sqrt(22)<19`, whose square is the exact check `352<361`. For `r=1`, the diagonal is `>53/63` while the one off-diagonal entry is `<22/63`. For `r=0`, `1/21+1/18=13/126<1`. Therefore the retuned proposition

`s_{4k-3}(A)>=1`, no pivot, `1<=k<=3`  =>  `V_k(A)>=kappa^k`

is valid. A fair physical cut gives

`E_k^(-1/(2k)) <= 2 kappa^(-1/2)=36`,

and for the order-two half-potential branch specifically

`(4^-2 kappa^2)^(-1/8)=6`.

## 3. Sharpened pivot constants — PASS

### Singular kernel

For

`J(d)=int_{-1}^1 |x|^(-1/2)|x-d|^(-1/2) dx`,

direct substitutions give, for `0<d<=1`,

`J(d)=2 asinh(d^-1/2)+pi+2 acosh(d^-1/2)`,

and for `d>=1`,

`J(d)=2 asinh(d^-1/2)+2 asin(d^-1/2)`.

The first formula implies

`J(d)<=pi+4 log2+2 log(1/d)<6+2 log(1/d)`,

while the second is `<6`. Hence

`J(d)<6+2 log_+(1/|d|)`.

I also numerically stress-tested the exact formulas at `d=10^-8,10^-4,10^-2,0.1,0.5,0.99,1,1.01,2,10,100`; they agree with direct quadrature and retain positive margin to the displayed envelope. This numerical check is diagnostic; the preceding substitutions are the proof.

### Quarter-power coefficient

The exact smoothing coefficient is

`C_q=2^(5/8) pi^(-1/4) e^(3/8) Gamma(3/8)=3.9952593615...`.

The candidate's rational certificate is valid:

`2^(5/8)<31/20`, `pi^(-1/4)<19/25`, `e^(3/8)<22/15`, and
`Gamma(3/8)<12665/5016<81/32`.

The last bound follows by integrating `e^-x<=1-x+x^2/2` on `[0,1]` against `x^-5/8` and bounding the tail by `e^-1<3/8`. The product is exactly `174933/40000<35/8`. The fifth-order positive Taylor lower bound verifies `log(35/8)<119/80`. Therefore

`sup_a E log_+(1/|R-a|) < 199/20`

whenever the quadratic matrix of `R` has operator norm at least one.

### Hyperbolic retuning

For a hyperbolic branch `w(t)=u e^t+v e^-t` with `|u|=|v|`, choose a physical coordinate with `|u_i|>=|u|/sqrt2`. With `q=2/9`, the cutoff

`T_1=log3-(1/4)log2`

makes the backward exponential at most `q` times the forward one, and the physical-coordinate change of variables costs `(1+q)/(1-q)=11/7`. Carrying both tails gives exactly

`p(z)<=D^-1/2 [ C_0+log_+(B sqrt(D)/|z-v|) ]`,

`C_0=2log3+(37/14)log2`, `B=36sqrt2/49`.

The derivative of the resulting half-potential envelope is negative after the logarithm activates, and before activation it is a constant times `D^-1/2`; hence for `D>=1/21` its maximum is at `D=1/21`. The stated bound `(121/5)sqrt21` follows.

Combining scalar, definite, and indefinite pivots therefore gives the truncated half-potential

`H(Q)<(259/10)sqrt21`

under two surviving unit directions, and the full half-potential is less than this plus one.

## 4. Complete nine-direction assembly at constant 549

Normalize `K=s=1`.

* **No pivot:** `s_9>=1` gives `V_3>=kappa^3`; a fair cut and the `E_3` receiver give `||p_Q||_infinity<15*36=540`.
* **Scalar pivot:** the Schur complement retains eight unit directions. If it has a pivot, use the preceding full half-potential; if not, `s_5>=1`, the order-two retuned structure and `E_2` receiver give full half-potential `<13*6=78`. The outer square profile therefore gives
  `||p_Q||_infinity < sqrt21[(259/10)sqrt21+1]=5439/10+sqrt21<549`.
* **Definite pair:** `||p_Q||_infinity<=pi sqrt21<16`.
* **Indefinite pair:** seven Schur directions remain; one suffices for the logarithmic-potential argument, giving `<95` with the displayed retuned constants.

Thus the maximum is `<549`. Scaling `Y=KX` and `Q=(s/K^2)Qtilde` gives `<549 K^2/s` exactly.

As a margin diagnostic, using the exact special-function constants rather than the deliberately rational envelopes gives approximately `533.46` in the retuned no-pivot branch and `531.28` in the retuned scalar-pivot branch; these numbers are not needed for the theorem.

## 5. Why this does not prove eight directions

Two independent obstructions remain.

1. **Structural rank arithmetic:** at the bad order-two seed under only `s_8>=1`, global rank subtraction by `rank R<=6` forces only two large diagonal coordinates, while the restricted interpolation rank is also at most two. A diagonally dominant `2x2` residual block can have rank exactly two, so the `r+1` contradiction that closes at nine simply does not fire. Improving scalar Fourier or projection constants cannot change this count.

2. **Order-two analytic endpoint:** take independent `U,V~Unif[-1,1]` (density cap `1/2`). The density of `U^2` is `1/(2 sqrt s)` on `(0,1)`, so the density of `U^2-V^2` at zero contains
   `int_0^1 [1/(2 sqrt s)]^2 ds=infinity`.
   Thus an `E_2`/rank-two indefinite crossing certificate alone cannot be a universal bounded-density endpoint.

Current eight-direction structural work extracts additional overlap-one/two-sided collar information, so these obstructions do **not** disprove an eight-eigenvalue theorem. They identify the remaining obligation: a dependence-safe receiver that uses the collar's overlapping structure rather than only a disjoint `E_2` crossing or the old rank count.

## Review-state conclusion

- canonical 17-direction manuscript: PASS in this run;
- complete 9-direction replacement mechanism: PASS in this run;
- retuned `<549 K^2/s` constant: PASS in this run, but retain `CANDIDATE_PENDING_ANOTHER_SEPARATE_COMPLETE_REVIEW` for release-state purposes;
- 8-direction theorem: GAP / unproved;
- unrestricted 3-direction theorem: OPEN.
