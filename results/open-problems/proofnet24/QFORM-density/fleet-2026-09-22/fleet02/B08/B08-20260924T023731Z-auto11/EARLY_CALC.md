SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B08, 2026-09-24T02:37:31.932715Z.
attacking: the near-rank-one aligned large-twist/localized transition: force an explicit actual spectral gate and either pay it with a product-safe compiler or isolate a target-valid obstruction.

# Early substantive calculation

Full target remains OPEN. Work below is in the exact aligned rank-one carrier state

\[
A=\begin{pmatrix}B&M\\M^T&\lambda ww^T+D\end{pmatrix},\qquad
w=M^Tr,\quad \|r\|_2=1,
\]

where the first two coordinates are ORIGINAL physical hubs, `M` is `2 x m` of row rank two, `G=MM^T`, and `D` is a physical diagonal matrix. All inputs remain arbitrary independent cap-one laws. Outside coordinates may be conditioned and only create affine terms.

The first unpaid implication identified here is:

`QFORM-RANK1-RESONANT-HUB-ALIGNMENT-COMPILER-v1`: after the actual physical-pair gate and the two product-safe Fourier gates below, consume the residual chamber in which the rank-one carrier is weak in total volume, the carrier/hub Schur discriminant is almost or actually negative-resonant, and the carrier direction is quantitatively aligned with the resulting large ORIGINAL hub scalar. No post-rotation independence or small-random-perturbation step is allowed.

## 1. One retained physical hub already pays a rank-one carrier

Condition the other original hub and retain hub `p`. The light block is `D+lambda w w^T`. Normalize `v=w/||w||`; its rank-one coefficient is `lambda_c=lambda ||w||^2`. Choose `p` so that the opposite coefficient `|r_perp|>=1/sqrt(2)`. The augmented Theorem-H frame consists of `v` and the retained physical arm row `m_p`.

Its row space is exactly `row(M)`, hence its normalized physical leverages equal those of `M`. Moreover

\[
|\lambda_c|\det \widetilde G
=|\lambda|\,r_\perp^2\det G
\ge {1\over2}|\lambda|\det G.
\]

Therefore the fixed-source hub theorem gives, whenever `max_i m_i^T G^{-1}m_i<=1/2`,

\[
\boxed{\|p_Q\|_\infty
\le 3\,2^{5/3} (|\lambda|\det G)^{-1/3}},
\]

with a continuous `C_0` density. In particular

\[
|\lambda|\det G\ge L^3/4096
\quad\Longrightarrow\quad
\|p_Q\|_\infty<152.391/L.
\]

This does not use any physical twist `d_j` and is therefore complementary to the newest fleet03/B08 cancelled-twist shear theorem.

## 2. Real product-safe carrier-killing shear

Put `b_r=r^TBr` and

\[
\kappa=1-\lambda b_r.
\]

For `kappa>0`, choose a real root of

\[
b_r\alpha^2-2\alpha+\lambda=0
\]
(and `alpha=lambda/2` if `b_r=0`). Make the triangular ORIGINAL-coordinate change in the integral

\[
h=h'-\alpha r\,(r^TMx).
\]

This is only a light-dependent translation of each original hub variable, so each shifted hub density is still pointwise at most one. The light rank-one carrier cancels exactly. The new two-hub arm is

\[
C=(I-\alpha Br r^T)M.
\]

The determinant lemma gives

\[
\det(I-\alpha Br r^T)=1-\alpha b_r=\pm\sqrt\kappa,
\]
so

\[
\det(CC^T)=\kappa\det G.
\]

Because the left multiplier is invertible, the physical row leverages of `C` are exactly those of `M`. Fixed-source Theorem H with two physical hubs and diagonal light block therefore gives

\[
\boxed{\|p_Q\|_\infty\le4\kappa^{-1/4}(\det G)^{-1/4}},
\]

again with a continuous `C_0` density.

If `s_2(M)>=L/8` and `kappa>=1/4096`, this is at most `256/L`.

## 3. Quantitative residual after the actual pair gate

Assume the previous proved actual gate is unpaid: every physical `2 x 2` principal block has least singular value `<L/64` or is singular. Also assume the diffuse/isotropic arm gate

\[
\mu:=\max_i m_i^TG^{-1}m_i\le1/3,\qquad s_2(M)\ge L/8.
\]

If neither of the two new Fourier gates pays, then

\[
|\lambda|\det G<L^3/4096,
\qquad
\kappa<1/4096.
\]

Since `det G=(s_1s_2)^2>=L^4/4096`, the first inequality implies `|lambda|<1/L`. The second says

\[
\lambda r^TBr>4095/4096.
\]

Thus `||B||op>(4095/4096)L`. But the unpaid physical-pair gate gives `sigma_min(B)<L/64`. For a real symmetric `2 x 2` matrix with singular values `s_1>=s_2`, some ORIGINAL diagonal obeys

\[
|B_{pp}|\ge(s_1-s_2)/2.
\]

Consequently the residual chamber necessarily has an actual localized physical hub scalar

\[
\boxed{\max_p |B_{pp}|>{4031\over8192}L=0.4920654296875\,L.}
\]

This is an actual spectral/localization gate, not a spectral-basis pivot.

## 4. A further half-potential gate at that localized hub

For such a hub `p`, write `q` for the other hub and `a=B_pp`. Square-peeling the ORIGINAL coordinate `p` leaves, after conditioning hub `q`, the light block

\[
D+M^TR_pM,\qquad R_p=\lambda rr^T-a^{-1}e_pe_p^T.
\]

If `r_q!=0`, then

\[
|\det R_p|={|\lambda|r_q^2\over |a|},
\quad
P:=|\det R_p|\det G.
\]

The fixed-source rank-two Fresnel bound gives `|phi(t)|<=min(1,4pi P^{-1/2}|t|^{-1})`. Its proved fractional-potential lemma yields

\[
H_{1/2}\le8\sqrt2\,P^{-1/4}.
\]

The square peel therefore gives

\[
\boxed{\|p_Q\|_\infty
\le8\sqrt2\,(|a\lambda|r_q^2\det G)^{-1/4}.}
\]

Hence

\[
|a\lambda|r_q^2\det G\ge L^4/65536
\quad\Longrightarrow\quad
\|p_Q\|_\infty\le128\sqrt2/L<181.020/L.
\]

If this gate also fails, the preceding resonance and pair estimates imply `|a lambda|>4031/8192`; together with `det G>=L^4/4096` this forces

\[
\boxed{r_q^2<512/4031=0.1270156289\ldots,\qquad
r_p^2>3519/4031=0.8729843711\ldots.}
\]

Thus the genuinely unpaid rank-one state is not merely anisotropic: its carrier direction is quantitatively aligned with the large original hub pivot.

## 5. Target-valid exact-resonance stress family

Let `m=16384`; take two normalized orthogonal Sylvester-Hadamard columns `u_1,u_2`, and put

\[
M=L\begin{pmatrix}u_1^T\\u_2^T\end{pmatrix},\quad
B=L\,\mathrm{diag}(\varepsilon,0),\quad
R={1\over\varepsilon L}e_1e_1^T,\quad D=0,
\qquad \varepsilon=1/128.
\]

Then `G=L^2I_2`, every arm leverage is `2/m`, and `kappa=1-lambda r^TBr=0`. The nonzero spectrum is exactly

\[
\boxed{L(\varepsilon+\varepsilon^{-1}),\quad +L,\quad -L},
\]

so this is a genuine exactly-three-nonzero-eigenvalue target matrix.

Every physical `2 x 2` principal block misses the `L/64` gate: the hub pair is singular; hub-1/light and light/light blocks are rank one; and a hub-2/light block has least singular value at most `L/sqrt(m)=L/128`.

This is NOT a QFORM counterexample. Apply the required fixed-source Theorem H after conditioning hub 1. The remaining hub-2/light augmented frame has leverage exactly `2/m`, rank-one light coefficient `L/epsilon`, and Gram determinant `L^2`. Hence

\[
\boxed{
\|p_Q\|_\infty
\le3\,2^{4/3}\varepsilon^{1/3}L^{-1}
={3\over2}L^{-1},
}
\]

with a continuous `C_0` density for every admissible product source. Thus neither a well-conditioned physical pair nor a nonzero physical diagonal twist is structurally necessary: the rank-one diffuse carrier itself can be the third smoothing resource.
