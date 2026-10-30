# fleet02/B09 — complete review of the nine-eigenvalue replacement and the eight-direction boundary

Run: `20260924T131358Z-fleet02-B09-fixedmult-r11`  
Baseline pin: `7c0d6e60946b19423e6400a12d34b473cf0591e2`, manuscript blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 pin `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.  
Improvement source independently reviewed: fleet03/B04 commit `8ff490c177d0cd7d6f33130f1431785e312a9d10`, report blob `054facef834d29927713c5d42a1f09a541c5644b`. I reconstructed the argument rather than accepting its PASS label or the later peer verdicts.

## Verdict

**PASS: complete nine-eigenvalue replacement proof.** The currently reviewed argument proves, preserving all baseline hypotheses,

\[
\boxed{
 s_9(A)\ge s>0
 \quad\Longrightarrow\quad
 \|p_{X^TAX+b^TX+c}\|_\infty\le6010\,K^2/s .
}
\]

Here the coordinates are arbitrary independent real variables with densities bounded by `K`, `A=A^T` is arbitrary, and `b,c` are arbitrary. No moment, support, sign, log-concavity, diagonal-basis, exact-rank, leverage, Gaussian, or post-rotation-independence assumption is introduced. Global continuity is not claimed. The unrestricted three-eigenvalue conjecture remains open.

This run is a genuinely separate mathematical reconstruction. It does not itself alter the canonical manuscript or self-award the repository release gate; synthesis of independent reviews remains a keeper/B20 responsibility.

## 1. Grouped product-Fourier compiler — PASS

Let `H,I,J` be disjoint original-coordinate banks, let `W` be a `k`-dimensional orthogonal projection of `X_H` with density cap `M_H`, and consider

\[
Q=F(X_H)+2\langle W,MX'+\beta\rangle+R(X'),\qquad X'=(X_I,X_J),
\]

with arbitrary measurable `F`, arbitrary quadratic/affine `R`, and `M_J` of row rank `k`. Let `S` be the product of the nonzero singular values of `M_J`. Project the literal residual cross rows `A_R[I,J]` orthogonally off `row(M_J)` and call the resulting row matrix `C`. For determinant-squared weights on `ell`-subsets with volume

\[
Z_\ell=\sum_{|T|=\ell}\det(C_TC_T^T)>0
\]

and inclusion marginals `alpha_i≤1/2`, put `d=k+ell`.

The claimed characteristic-function bound is

\[
|\phi_Q(t)|\le
\min\{1,K_{k,\ell}|t|^{-d/2}\},
\]

where

\[
K_{k,\ell}=M_H^{1/2}\pi^{d/2}2^{\ell/4}e^{(k+2\ell)/4}
\left(\frac{\ell^\ell}{\ell!}\right)^{1/4}
S^{-1/2}Z_\ell^{-1/4}.
\]

I checked the delicate steps independently:

1. Push `e^{itF}dP_H` to `W`. Its complex density `a_t` obeys `|a_t|≤p_W`, hence `||a_t||_2^2≤M_H`. `k`-dimensional Plancherel under the manuscript convention and the scale `2t` gives
   \[
   \int|\widehat a_t(2t(\ell+\beta))|^2d\ell
   \le M_H(\pi/|t|)^k.
   \]

2. For the light-bank complex pushforward `mu_t`, condition first on the original `X_I`. Expanding the squared mollified pushforward uses only an independent copy of `X_J`: pure `I` phases cancel, pure `J` phases have modulus one, and the cross phase is linear in the original independent `X_i`, `i∈I`. Integrating those original coordinates produces exactly the scalar Fourier factors. No conditional density cap is inferred from an unconditional projection.

3. For a chosen `ell`-set, the linear map
   \[
   D\mapsto(M_JD,(\langle c_i,D\rangle)_{i\in T})
   \]
   has Gram determinant `S^2 det(C_T C_T^T)`. The baseline product-projection theorem therefore gives the correct cap `e^{d/2}/[S sqrt(det(C_TC_T^T))]`.

4. The scalar Fourier-power estimate at `p=1/alpha_i≥2`, including the `2t` scale, is
   \[
   \int|\psi_i(2t(y+u))|^{1/\alpha_i}dy
   \le \pi\sqrt{2e\alpha_i}/|t|.
   \]

5. For weights `w_T=det(C_TC_T^T)/Z_ell`, the determinant geometric mean is exactly `Z_ell^{-1/2}exp(H(w)/2)`. The marginal factors contribute `exp((1/2)sum alpha_i log alpha_i)`. Ordering the sampled `ell`-subset uniformly and using entropy subadditivity gives
   \[
   H(w)+\sum_i\alpha_i\log\alpha_i
   \le \ell\log\ell-\log(\ell!).
   \]

6. Squaring/unsquaring the preceding constants gives the displayed `K_{k,ell}` exactly. If `d>2`, integration of `min(1,K|t|^{-d/2})` and the manuscript `1/(2pi)` inversion factor yield
   \[
   \|p_Q\|_\infty\le
   \frac d{d-2}M_H^{1/d}2^{\ell/(2d)}e^{(k+2\ell)/(2d)}
   \left(\frac{\ell^\ell}{\ell!}\right)^{1/(2d)}
   S^{-1/d}Z_\ell^{-1/(2d)}.
   \]

The approximate-identity removal is valid by uniform `L^2` bounds plus weak compactness/lower semicontinuity. No moment assumptions are used.

## 2. Marginal-free `E_3` density receiver — PASS

For a literal original-coordinate cross block `M`, put `Z=E_3(M)=e_3(MM^T)`. Let `J_i` be the incident third-volume mass of physical row `i`; `sum_i J_i=3Z`.

- If all `J_i/Z≤1/2`, use the compiler at `(k,ell,d)=(0,3,3)`.
- If `J_i>Z/2`, promote row `w=m_i`. Orthogonal Gram–Schmidt gives exactly
  \[
  J_i=\|w\|^2e_2(CC^T).
  \]
- If a residual row is heavy for this `E_2`, promote it. With two promoted rows `P` and the remaining rows projected off their span,
  \[
  H_{ij}=\det(PP^T)\|C_2\|_F^2>J_i/2>Z/4.
  \]
- If a residual row is again heavy, promote it; the three physical rows then have Gram determinant `>H_ij/2>Z/8`.

The four branches are respectively `(0,3)`, `(1,2)`, `(2,1)`, and the exact physical rank-three endpoint. The largest constant is

\[
C_3=3\sqrt2\,e\,(9/2)^{1/6}=14.818337662843\ldots,
\]

so

\[
\boxed{\|p_Q\|_\infty\le C_3E_3(M)^{-1/6}}.
\]

Every branch has an integrable characteristic-function envelope.

## 3. Marginal-free `E_2` full half-potential receiver — PASS

The same promotion tree one dimension lower gives

\[
\boxed{
\sup_a\mathbf E|Q-a|^{-1/2}
\le C_2E_2(M)^{-1/8},
\qquad C_2=8\sqrt e\,2^{-1/8}=12.095072570796\ldots .
}
\]

The diffuse branch uses `(k,ell,d)=(0,2,2)` and the exact weighted integral

\[
\int_\mathbb R|t|^{-1/2}\min(1,L/|t|)dt=8\sqrt L.
\]

One heavy row uses `(1,1,2)`; a second heavy row terminates at the exact physical rank-two half-potential estimate. This conclusion is deliberately a half-potential estimate, not a rank-two bounded-density claim.

## 4. Complete nine-eigenvalue theorem — PASS

Normalize `K=s=1`, keep `eta=1/100`, `kappa=1/80^2`.

### No pivot

The audited baseline spectral-to-volume proposition with `k=3` uses exactly `s_9(A)≥1` and gives

\[
V_3(A)\ge\kappa^3.
\]

The fair physical cut has a literal cross block with

\[
E_3(M)\ge4^{-3}\kappa^3,
\qquad E_3(M)^{-1/6}\le160.
\]

Therefore

\[
\|p_Q\|_\infty\le160C_3
=2370.93402605488\ldots<2400.
\]

### Scalar pivot

A scalar pivot removes one original coordinate. The Schur complement retains at least eight unit spectral directions.

- If that Schur complement has an `eta`-pivot, the baseline pivot proposition requires only two directions and gives truncated half potential `≤600`; the tail outside distance one contributes at most one.
- If it has no pivot, then `s_5≥1`. The baseline `k=2` spectral-to-volume proposition and fair cut give `E_2≥4^{-2}kappa^2`, so the new full half-potential receiver gives
  \[
  C_2\sqrt{160}=152.99191115498\ldots<153.
  \]

Thus the Schur full half potential is at most `601`, and the scalar-square profile yields

\[
\|p_Q\|_\infty\le10\cdot601=6010.
\]

### Pair pivots

A definite pair is bounded directly by `pi/sqrt(eta)<32`. An indefinite pair leaves at least seven Schur directions; the baseline logarithmic argument needs only one nonzero unit direction and remains `<251`.

Hence the normalized theorem is `≤6010`. Rescaling `Y=KX` gives the stated `6010 K^2/s` theorem.

### Dependency map

`baseline BL + projection + scalar Fourier powers`
`-> grouped product-Fourier compiler`
`-> marginal-free E3 density + E2 half potential`
`+ baseline spectral-to-volume/cut`
`+ baseline Schur/pivot endpoints`
`-> s9 bounded-density theorem`.

No dependency on a rotated-coordinate product law, Gaussianity, support, moments, or an exact-rank spectral truncation appears.

## 5. Eight directions: exact structural boundary, but no complete density theorem

I also independently checked the subsequent fleet03/B04 structural collar at commit `5dc3b183bf69c8ab69f725c4464d5073f5c803cd`. It is a correct sharpening of the B09 rank count, not yet a complete theorem.

Assume no pivot, `s_8(A)≥1`, and `V_3<kappa^3`.

1. `V_1≥kappa`; otherwise `||A||<eta+sqrt(kappa)<1`.
2. `V_2≥kappa V_1`: if the `r=1` ratio were bad, `||E||<1/40`, global rank loss three gives `s_5(D)≥39/40`, and two large entries of `D` in `L` produce a strictly diagonally dominant `2x2` block of `R[L,L]`, contradicting restricted rank one.
3. Therefore `V_2≥kappa^2` and `V_3/V_2<kappa`. Sampling order-two seeds and retaining those with `||F||_F^2≤18kappa` keeps at least half the determinant-squared mass. For such a seed, `epsilon_*:=sqrt(18kappa)=3sqrt2/80`; rank loss six from `s_8` forces two diagonal entries `D_h` in `L` of modulus at least `c_*=1-epsilon_*`.
4. The exact bordered identity gives, for each selected anchor,
   \[
   \det A[S\cup\{h\},T\cup\{h\}]=\det(B)D_h.
   \]
   Summation yields the overlap-one currency
   \[
   \Omega_1\ge c_*^2\kappa^2.
   \]
5. On the two-anchor set `H`, the interpolation block obeys
   \[
   |P_{hh}|>1-\epsilon_*-\eta,
   \qquad |P_{hh'}|<\sqrt{\eta^2+\eta}+\epsilon_*.
   \]
   Hence
   \[
   |\det P[H,H]|\ge
   \delta_*:=(1-\epsilon_*-\eta)^2-(\sqrt{\eta^2+\eta}+\epsilon_*)^2
   =0.854335140191\ldots>0.
   \]
   Since `P[H,H]=A[H,T]B^{-1}A[S,H]`, summing good seeds yields
   \[
   \Xi_2:=\sum_{S,H,T}\det A[S,H]^2\det A[H,T]^2
   \ge(\delta_*^2/2)\kappa^2.
   \]

So `s_8` does not merely leave an unstructured rank-equality case: it forces a quantitative overlap-one/two-sided collar. However the repeated physical anchor in the large bordered minors is precisely why the existing disjoint-cut `E_3` receiver does not directly apply. A complete product-preserving analytic receiver for this collar, valid when every physical anchor diagonal may vanish and while retaining arbitrary same-bank curvature, is still missing.

Accordingly **nine is the lowest complete bounded-density threshold established in this review**. I do not claim an eight-eigenvalue theorem, and I do not claim the unrestricted three-eigenvalue conjecture.