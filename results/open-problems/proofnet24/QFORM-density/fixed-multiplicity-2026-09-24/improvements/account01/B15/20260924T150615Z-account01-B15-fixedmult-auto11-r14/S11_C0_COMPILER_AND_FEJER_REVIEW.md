# account01/B15 improvement — exact regularity scope, Fejer review, and an s11 global C0 compiler

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`.

Pinned manuscript source: commit `7c0d6e60946b19423e6400a12d34b473cf0591e2`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`, SHA-256 `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`.

Status: **proved supporting regularity theorem plus independent B15 check of the Fejer constant patch.** This does not lower the currently complete multiplicity-nine density candidate to eight, and does not solve the unrestricted three-direction problem. It does not self-award release/validation status.

## 1. Exact regularity already contained in the pinned order-five branch

The pinned manuscript proves, from a physical crossing block with fifth crossing volume `Z_5>0`,

\[
 |\phi_Q(t)|\le \min\left\{1,\left(\frac{u}{|t|}\right)^{5/4}\right\},
 \qquad u=\pi e Z_5^{-1/10}.
\]

Since `5/4>1`, this is in `L^1`, so the Fourier inversion density is in `C_0(R)`. There is also a quantitative pointwise modulus that the manuscript does not state. For every `h`,

\[
\begin{aligned}
 |p(x+h)-p(x)|
 &\le \frac1{2\pi}\int |e^{-ith}-1|\,|\phi_Q(t)|\,dt\\
 &\le \frac{u^{5/4}}{\pi}\int_0^\infty
       \min(2,|h|t)t^{-5/4}\,dt\\
 &=\frac{16\,2^{3/4}}{3\pi}u^{5/4}|h|^{1/4}.
\end{aligned}
\]

Thus

\[
\boxed{[p_Q]_{C^{0,1/4}}
\le \frac{16\,2^{3/4}}{3\pi}(\pi e)^{5/4}Z_5^{-1/8}.}
\]

In the pinned no-pivot `s_17(A)>=1` branch, `Z_5>=4^{-5}\kappa^5`, so `u<=160\pi e` and

\[
\boxed{[p_Q]_{C^{0,1/4}}<2.372\times10^4.}
\]

This is deliberately a **no-pivot** regularity conclusion. The scalar and pair pivot branches of the pinned manuscript are measure-domination arguments and do not inherit this Fourier modulus automatically.

For comparison, the order-three envelope has exponent `3/4<1`, so it does not even give direct bounded-density inversion. Its role is different: multiplying by the Riesz weight `|t|^{-1/2}` creates the integrable tail exponent `5/4`. This verifies the manuscript's exact regularity scope.

## 2. Independent B15 check of the Fejer small-ball sharpening

A current improvement replaces the Gaussian smoothing constant `16` in manuscript Lemma `lem:quarter` by `4`. I independently checked the Fourier normalization and constant.

For `0<c<2\pi`, let

\[
 K_c(x)=\left(\frac{\sin(cx/2)}{cx/2}\right)^2,
 \qquad
 \widehat K_c(t)=\frac{2\pi}{c}\left(1-\frac{|t|}{c}\right)_+.
\]

On `|x|<=1`,

\[
 K_c(x)\ge m_c:=\left(\frac{\sin(c/2)}{c/2}\right)^2.
\]

Suppose

\[
 |\phi_R(t)|\le\left(\frac{4\pi e}{L|t|}\right)^{1/4}.
\]

Fourier inversion of the integrable Fejer kernel gives

\[
\begin{aligned}
 \Pr\{|R-a|\le\rho\}
 &\le \frac{\rho}{cm_c}
 \int_{|t|\le c/\rho}
 \left(1-\frac{\rho|t|}{c}\right)|\phi_R(t)|dt\\
 &\le \frac{32}{21}(4\pi e)^{1/4}c^{-1/4}m_c^{-1}
       (\rho/L)^{1/4}.
\end{aligned}
\]

The factor `32/21` is exact because

\[
2\int_0^1(1-u)u^{-1/4}du=\frac{32}{21}.
\]

At `c=6/5`, the alternating sine series gives

\[
\sin(3/5)\ge 3/5-(3/5)^3/6=141/250,
\qquad m_c\ge(47/50)^2.
\]

With the elementary upper bounds `pi<22/7`, `e<11/4`, the fourth power of the resulting coefficient is strictly below `4^4`. Therefore

\[
\boxed{\Pr\{|R-a|<\rho\}\le\min\{1,4(\rho/L)^{1/4}\}.}
\]

For `L>=1`, layer cake now gives

\[
\boxed{\sup_a\mathbb E\log_+\frac1{|R-a|}
\le 4+4\log4.}
\]

Substituting this into the already-audited pivot proof sharpens the scalar-pivot truncated half potential to

\[
 H(Q)\le 200+120\log4<367,
\]

and its full half potential to

\[
 \sup_a\mathbb E|Q-a|^{-1/2}
 \le201+120\log4.
\]

Applied to the complete current nine-direction replacement proof, the largest branch becomes

\[
10(201+120\log4)=2010+1200\log4
=3673.553233\ldots<3674.
\]

So, conditional only on the already-written nine-direction replacement dependency chain, the constant patch is mathematically sound:

\[
\boxed{s_9(A)\ge s\Longrightarrow\|p_Q\|_\infty<3674\,K^2/s.}
\]

This section checks the constant patch; it is not a new release-status declaration for the nine-direction theorem.

## 3. Generic deletion/submass compiler

The following lemma is independent of the details of the nine-direction proof.

### Lemma

Assume a fixed-multiplicity theorem `T_m(C)`:

> for all independent real coordinate probability densities bounded by `K`, all real symmetric `A` with `s_m(A)>=s>0`, and all affine terms, the output density exists and is bounded by `C K^2/s`.

Then, whenever `s_{m+2}(A)>=s`, replacing any one original-coordinate probability density by a subdensity `0<=h<=K` of total mass `q` produces an output submeasure with density bounded by

\[
\boxed{q\,C K^2/s.}
\]

#### Proof

It is enough to keep `K,s` explicit. Fix coordinate `j`. Let `B=A_{-j,-j}` be the principal deletion. Define threshold counts

\[
 p_s(M)=\#\{\lambda(M)\ge s\},\qquad
 n_s(M)=\#\{\lambda(M)\le-s\}.
\]

Cauchy interlacing gives

\[
 p_s(B)\ge p_s(A)-1,\qquad n_s(B)\ge n_s(A)-1.
\]

Since `s_{m+2}(A)>=s`, `p_s(A)+n_s(A)>=m+2`; hence

\[
 p_s(B)+n_s(B)\ge m.
\]

Thus `B` has at least `m` eigenvalues of modulus at least `s`.

If `q=0`, there is nothing to prove. For `q>0`, set `x_j=qz_j` and

\[
 g(z_j)=h(qz_j).
\]

Then `g` is a probability density, `g<=K`, and

\[
 h(x_j)dx_j=q\,g(z_j)dz_j.
\]

The transformed quadratic matrix is

\[
 A_q=D_qAD_q,
\]

where `D_q` is diagonal, equals `q` in coordinate `j`, and equals one elsewhere. Its principal deletion at `j` is exactly `B`. Interlacing from the principal block `B` to `A_q` therefore shows `s_m(A_q)>=s`. Apply `T_m(C)` to the normalized probability product law and multiply its output density by the prefactor `q`. This proves the lemma. No coordinate rotation and no conditional projection cap occur.

### Corollary: source-L1 to output-L-infinity Lipschitz estimate

Let `f=(f_i)` and `g=(g_i)` be two cap-`K` product probability inputs for the same `A`, with `s_{m+2}(A)>=s`. Replacing one coordinate at a time and writing

\[
 f_j-g_j=(f_j-g_j)_+-(g_j-f_j)_+,
\]

the two positive parts are cap-`K` subdensities of equal mass

\[
 q_j=\frac12\|f_j-g_j\|_1.
\]

The lemma bounds each corresponding output subdensity by `q_j C K^2/s`; summing the positive and negative pieces gives

\[
\boxed{
 \|p_f-p_g\|_\infty
 \le \frac{C K^2}{s}\sum_j\|f_j-g_j\|_1.
}
\]

This estimate is dimension-free and uses only literal original-coordinate product structure.

## 4. Smooth product inputs have a C0 output for any fixed rank at least three

This is an instancewise regularity fact; its constant is allowed to depend on the fixed matrix and the smoothed source.

Let every marginal be smooth with all derivatives in `L^1` (Gaussian mollifications of arbitrary `L^1` densities have this property), and suppose `rank(A)=r>=3`. Orthogonally diagonalize only the **deterministic integral**:

\[
 U^TAU=\operatorname{diag}(\Lambda,0),
\]

where `Lambda` is nonsingular `r x r`. Write `U^Tx=(y,z)` and the transformed affine term as `(alpha,beta)`. If `F(x)` is the original smooth product density, define

\[
 a_t(y)=\int e^{it\beta\cdot z}F(U(y,z))dz.
\]

For every multi-index `gamma`, differentiation in `y` acts only on `F`, so

\[
 \sup_t\|\partial_y^\gamma a_t\|_1<\infty.
\]

Taking sufficiently many derivatives therefore gives a uniform bound

\[
 \sup_t\|\widehat a_t\|_1<\infty.
\]

Fourier inversion of `a_t`, followed by the standard Fresnel integral in the `r` active quadratic coordinates, yields for `|t|>=1`

\[
 |\phi_Q(t)|
 \le C_{A,F}|t|^{-r/2}.
\]

The constant is instance-dependent, which is harmless here. Since `r>=3`, this tail is integrable. Hence

\[
\boxed{p_Q\in C_0(\mathbb R)}
\]

for every such smooth product input. Rotated coordinates are never declared independent; rotation is used only to evaluate a deterministic oscillatory integral with a smooth joint amplitude.

## 5. New global rough-input regularity theorem at multiplicity eleven

Apply the compiler with the complete current nine-direction candidate. Using the conservative reviewed constant `C=5338` already suffices. With the independently checked Fejer patch above, use `C=3674`.

### Theorem (s11 global C0 compiler)

Assume the complete nine-direction theorem in the current proof stack. If

\[
 s_{11}(A)\ge s>0
\]

and the coordinates are independent with arbitrary probability densities `0<=f_i<=K`, then the law of

\[
 Q=X^TAX+b^TX+c
\]

has a canonical continuous density vanishing at infinity and

\[
\boxed{\|p_Q\|_\infty<3674\,K^2/s.}
\]

Moreover, for any two such product inputs `f,g` for the same matrix,

\[
\boxed{
 \|p_f-p_g\|_\infty
 <\frac{3674K^2}{s}\sum_i\|f_i-g_i\|_1.
}
\]

#### Proof

The height bound itself follows already from `s_11>=s_9>=s`. For continuity, mollify each original marginal by a Gaussian kernel:

\[
 f_{i,\varepsilon}=f_i*\gamma_\varepsilon.
\]

Convolution preserves probability mass and the cap `K`, and

\[
 \|f_{i,\varepsilon}-f_i\|_1\to0.
\]

The smooth-input lemma gives a density `p_\varepsilon in C_0`. Because `s_11(A)>=s`, the deletion/submass compiler with `m=9` gives

\[
 \|p_\varepsilon-p\|_\infty
 \le \frac{3674K^2}{s}
       \sum_i\|f_{i,\varepsilon}-f_i\|_1\to0.
\]

Thus the smooth output densities converge uniformly. Their uniform limit is a `C_0` representative of the rough output density, and the height bound passes with no further loss. The two-source estimate was proved in Section 3.

### Why the `+2` is real for this compiler

This argument cannot mechanically replace `m+2` by `m+1`. Consider

\[
 A=\begin{pmatrix}0&1\\1&0\end{pmatrix}\oplus I_8.
\]

It has ten eigenvalues of modulus one. Deleting either coordinate of the hyperbolic `2x2` block leaves only the eight unit eigenvalues from `I_8`; both the positive and negative threshold counts can be lost at once. Thus `s_{10}(A)>=1` does **not** guarantee a nine-direction principal deletion for every source coordinate. This is only a sharpness example for the deletion compiler, not a counterexample to continuity or bounded density at multiplicity ten.

## 6. Current multiplicity frontier

- pinned 17-direction manuscript: PASS in the accompanying B15 end-to-end audit;
- current complete nine-direction replacement: lowest complete theorem I support from the present proof stack; independent full review artifacts exist, while repository release status remains owner/release-gate controlled;
- new result here: global rough-input `C_0` and dimension-free source stability at multiplicity eleven, downstream of the nine-direction height theorem;
- multiplicity eight: still GAP at the overlap/masked-collar analytic receiver;
- unrestricted multiplicity three: OPEN.

The important separation is now explicit: the central height theorem is the harder statement. Once a height theorem is available at multiplicity `m`, two spare threshold directions automatically compile it into global `C_0` regularity and an `L^1(source)->L^infinity(output)` Lipschitz bound, without any rotated-independence or pointwise rough-quadratic Fourier shortcut.
