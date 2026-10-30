# B05 improvement note — safe projection/slice interface and nine-direction review

Pinned manuscript blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d` (`SHA-256 9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`).

Fresh replacement reviewed: fleet02/B10 `NINE_THRESHOLD_REPLACEMENT.md`, blob `070c26607338258ae6feca3dd5d40427cc3dbc91`.

Status: **proved interface lemma + independent B05 reconstruction of the complete s9 replacement; not a release certificate.**

## 1. Safe exceptional-slice mixing lemma

Let `Y` be a conditioning random element. Suppose that for almost every `y` there is a conditional output measure `mu_y` and a jointly measurable nonnegative kernel `K(z,y)` such that, for every nonnegative measurable test function `phi`,

`int phi(z) mu_y(dz) <= int phi(z) K(z,y) dz`.

Then the mixed output law `mu=E mu_Y` satisfies

`int phi dmu <= int phi(z) E[K(z,Y)] dz`

for every nonnegative measurable `phi`; hence `mu` is dominated by `E[K(z,Y)] dz` whenever the latter is locally integrable.

**Proof.** Integrate the conditional test-function inequality in `y` and apply Tonelli to the nonnegative right side. No common exceptional set in the output variable is selected. This is exactly the form needed for rough square and hyperbolic conditional profiles.

The lemma is strictly safer than a pointwise conditional-density assertion. For independent `W_1,W_2~Unif[-1/2,1/2]`, `2W_1W_2` has density `log(1/(2|z|))`, so its critical fiber is genuinely unbounded. Adding an independent `Y~Unif[-1/2,1/2]` moves that singularity to `z=Y`; the exceptional point sweeps an interval. Test-function domination/Tonelli remains valid while any attempt to choose one common pointwise exceptional set fails.

## 2. Deterministic projection-density transfer used by the new compiler

If `D` has independent cap-one coordinates and `L` is a full-row-rank `d x n` deterministic matrix, write an SVD on its row space as `L=T U^T`, where `U^T U=I_d` and `|det T|=sqrt(det(LL^T))`. The pinned product-projection lemma gives

`||p_{U^T D}||_inf <= e^(d/2)`.

Changing variables by `T` gives

`||p_{LD}||_inf <= e^(d/2)/sqrt(det(LL^T))`.

This transfer uses no independence of projected coordinates and is uniform under shifts.

In the grouped compiler, for a fixed promoted hub block `M_J` and projected physical rows `c_i`, the map

`D -> (M_J D, (<c_i,D>)_{i in T})`

has Gram determinant `S^2 det(C_T C_T^T)`, where `S` is the product of nonzero singular values of `M_J`. Therefore its joint density cap is exactly bounded by

`e^((k+ell)/2)/(S sqrt(det(C_T C_T^T)))`.

This is the only projection-density input to the weighted physical-minor argument.

## 3. Rough complex pushforwards do not create a conditional cap

For the hub bank, push the complex measure `e^{itF}dP_H` through its orthogonal projection `W`. Total-variation domination by the ordinary law of `W` gives a density `a_t` with `|a_t|<=p_W`, hence `||a_t||_2^2<=M_H`.

For the residual complex pushforward, mollify before taking an `L^2` norm. Expanding the squared mollified norm uses an independent copy only of the literal original `J` bank. Conditional on the original `I` bank, pure `I` phases cancel and pure `J` phases have modulus one; averaging `I` produces scalar Fourier factors. The difference coordinates in `J` are still independent and have density caps at most one. Uniform `L^2` bounds on the mollifications pass to the unsmoothed pushforward by Fourier/Fatou or weak `L^2` compactness. Thus the proof never asserts a conditional projection-density cap.

This point survives the sharp rotated counterexample: if `X_1,X_2~Unif[-1/2,1/2]` and

`Y=(X_1+X_2)/sqrt2`, `Z=(X_1-X_2)/sqrt2`,

then `p_Y(y)=sqrt2-2|y|` but `p_{Z|Y=y}` has height `1/(sqrt2-2|y|)`, unbounded near the boundary. Any proof requiring a conditional cap for `Z|Y` would therefore be false; the grouped compiler does not.

## 4. Nine-direction replacement constants checked

For the order-three diffuse branch, the compiler at `(k,ell,d)=(0,3,3)` gives

`C_3=3 sqrt2 e (9/2)^(1/6)=14.818337662843...`.

The promotion identities

`J_i=||w||^2 e_2(CC^T)`

and

`H_ij=det(PP^T)||C_2||_F^2`

are Gram--Schmidt/Cauchy--Binet identities. A third heavy row is a literal three-row Gram determinant, so the promotion tree terminates without rotated independence. Hence every physical crossing with `E_3(M)=Z>0` has

`||p_Q||_inf <= C_3 Z^(-1/6)`.

At order two, the analogous Riesz calculation gives

`C_2=8 sqrt(e) 2^(-1/8)=12.095072570796...`

and

`sup_a E|Q-a|^(-1/2) <= C_2 E_2(M)^(-1/8)`.

Under no pivot and `s_9(A)>=1`, the pinned structural proposition gives `V_3>=kappa^3`; a fair original-coordinate cut gives `E_3>=4^-3 kappa^3`, so `E_3^-1/6<=160` and

`||p_Q||_inf < 2370.935`.

At a scalar pivot, the Schur complement retains eight unit directions. If the residual has a pivot, its full half potential is at most `201+120 log16`; if it has no pivot, `s_5>=1`, order two gives `<152.992`. Multiplying the worst residual bound by `eta^-1/2=10` yields

`2010+1200 log16 = 5337.106466687737... < 5338`.

Two-coordinate pivot branches are smaller. The normalized theorem therefore closes, and the baseline scaling gives

`||p_Q||_inf < 5338 K^2/s`

under `s_9(A)>=s>0`.

## 5. Why this note does not claim eight

For independent `U,V~Unif[-1,1]`, the density of `U^2` is `1/(2sqrt y)` on `(0,1)`, so the density of `U^2-V^2` at zero has the divergent integral

`int_0^1 [1/(2sqrt y)]^2 dy`.

Thus an order-two crossing lower bound by itself is not a bounded-density receiver. This blocks the naive endpoint route from nine to eight; it does not disprove an eight-eigenvalue theorem.

**Conclusion.** The pinned 17 theorem is sound in this B05 audit, and the fresh complete replacement proof lowers the currently proved candidate threshold to nine with constant `<5338`, subject to the owner's required separate-review/release gate. The unrestricted three-eigenvalue problem remains open.
