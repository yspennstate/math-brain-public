# account03/B08 — two-deletion ridge rigidity for the `s_8` terminal chamber

Run: `20260924T131732Z-account03-B08-fixedmult-audit-r56`  
Current owner objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Pinned baseline manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`, `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/manuscript.tex`, blob `183ccd294763214e6a707e8d4749ff9a8cf7006d`.

Status: **new proved structural reduction below the validated nine-eigenvalue candidate; no eight-eigenvalue theorem claimed.**

This note starts from the independently reconstructed nine-eigenvalue candidate and the previous B08 `s_8` terminal theorem. It adds a multiple-physical-deletion version of the account04/B08 child-window receiver, and converts failure of every such receiver into three nested, quantitative original-coordinate stars. No rotated independence, moments, support assumptions, Gaussianity, or arbitrary-joint coarea statement is used.

Throughout the normalized discussion
\[
\eta=\frac1{100},\qquad \kappa=\frac1{80^2},\qquad
\tau=\frac1{64}.
\]

## 1. Multi-deletion child-window receiver

### Theorem — `QFORM-MULTI-PHYSICAL-DELETION-WINDOW-v1`

Let `I` be any set of original coordinates, let `J=I^c`, and write the quadratic polynomial as
\[
Q(X)=X_J^T C X_J+\text{terms involving at least one coordinate in }I,
\qquad C=A[J,J].
\]
Assume that `C` has at least three eigenvalues of modulus at least `m>0`. Let
\[
P_C(m/64)=\mathbf 1_{\{|C|\ge m/64\}}
\]
be the spectral projection onto the indicated absolute-eigenvalue window. If
\[
\max_{j\in J}(P_C(m/64))_{jj}\le\frac1{32},
\tag{1}
\]
then for every independent cap-one input law and arbitrary affine terms,
\[
\boxed{
\|p_Q\|_\infty
\le \frac{288\sqrt{3e}}{13m}<\frac{64}{m},
\qquad p_Q\in C_0(\mathbb R).
}
\tag{2}
\]

#### Proof

Condition on the **original** coordinates `X_I=x`. The remaining coordinates `X_J` stay independent and keep their density caps. The conditional polynomial is
\[
X_J^T C X_J+\ell_x^T X_J+c_x,
\]
where the vector `\ell_x` and scalar `c_x` may depend arbitrarily on the fixed value `x`. Thus the only induced perturbation of the child quadratic form is coordinate-separable affine data. The affine-uniform spectral-window theorem used in account04/B08's theorem `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` applies with the same matrix `C` and the same scale `m`, giving the bound in (2) for every fixed finite `x`.

Averaging the conditional densities preserves the essential-supremum bound. Each conditional density is continuous and vanishes at infinity and all are bounded by the common constant in (2); dominated convergence therefore proves continuity and vanishing at infinity for the mixture. This is exactly the account04/B08 argument, with one original coordinate replaced by an arbitrary finite set of original coordinates. No probabilistic change of coordinates is made. `QED`

This is an actual application and extension of account04/B08 r2, not a new unproved interface.

## 2. Singular multiplicity survives one and two physical deletions

For `I\subset[n]`, let `q=|I|`, let `C_I=A[I^c,I^c]`, and pad `C_I` by zeros back to an `n\times n` matrix. If `P_I` denotes the coordinate projection killing `I`, this padded matrix is `P_I A P_I`. Moreover
\[
A-P_IAP_I=(I-P_I)A+P_IA(I-P_I),
\]
so
\[
\operatorname{rank}(A-P_IAP_I)\le2q.
\tag{3}
\]
The manuscript's singular-value rank perturbation lemma therefore gives
\[
s_{j+2q}(A)\le s_j(C_I).
\tag{4}
\]
Consequently, under
\[
s_8(A)\ge1,
\tag{5}
\]
we have
\[
\boxed{
s_6(C_I)\ge1\quad(q=1),
\qquad
s_4(C_I)\ge1\quad(q=2).
}
\tag{6}
\]
In particular every one- or two-coordinate deletion child still has at least three unit-scale eigenvalues, so Theorem `QFORM-MULTI-PHYSICAL-DELETION-WINDOW-v1` applies at `m=1` to **every** such child whenever its `1/64` window is diffuse.

Thus an unpaid normalized `s_8` state must satisfy the simultaneous localization condition
\[
\boxed{
\forall I\subset[n],\ |I|\le2:\quad
\max_{j\notin I}
\left(\mathbf1_{\{|C_I|\ge1/64\}}\right)_{jj}>\frac1{32},
}
\tag{7}
\]
unless already
\[
\boxed{\|p_Q\|_\infty<64,\qquad p_Q\in C_0.}
\tag{8}
\]
For `I=\varnothing`, (7) is just the same affine-uniform ridge-window gate applied to the parent matrix itself.

This strengthens the previous B08 terminal statement, which imposed (7) only after one physical deletion.

## 3. Localized spectral leverage forces a physical star under the no-pivot hypothesis

The following elementary variance identity turns (7) into an actual coefficient statement.

### Lemma — `QFORM-WINDOW-LEVERAGE-TO-STAR-v1`

Let `C=C^T`, fix a physical coordinate `j`, put `a=C_{jj}`, and let
\[
P=\mathbf1_{\{|C|\ge\tau\}}.
\]
If `|a|<\eta<\tau` and `P_{jj}>q`, then
\[
\boxed{
\|C[j,-j]\|_2>(\tau-\eta)\sqrt q.
}
\tag{9}
\]

#### Proof

Let `\mu_j` be the spectral probability measure of `C` at the unit vector `e_j`. Its mean is
\[
\int \lambda\,d\mu_j(\lambda)=C_{jj}=a,
\]
and its mass on `|\lambda|\ge\tau` is exactly `P_{jj}`. Also
\[
\begin{aligned}
\|C[j,-j]\|_2^2
&=\|(C-aI)e_j\|_2^2\\
&=\int(\lambda-a)^2\,d\mu_j(\lambda).
\end{aligned}
\]
On `|\lambda|\ge\tau`, the reverse triangle inequality gives
`|\lambda-a|\ge\tau-|a|>\tau-\eta`. Hence
\[
\|C[j,-j]\|_2^2
>(\tau-\eta)^2P_{jj}
>q(\tau-\eta)^2.
\]
Taking square roots proves (9). `QED`

At the live constants
\[
q=\frac1{32},\qquad
\tau=\frac1{64},\qquad
\eta=\frac1{100},
\]
we have
\[
\tau-\eta=\frac9{1600},
\]
so every localized window coordinate in a no-`\eta`-pivot matrix satisfies
\[
\boxed{
\|C[j,-j]\|_2>
\frac{9}{6400\sqrt2}
=0.0009943689110435824\ldots .
}
\tag{10}
\]
The point of (9) is that a small physical diagonal cannot by itself account for the high-window leverage; a definite amount of the spectral mass must leave through the actual off-diagonal star.

## 4. A nested three-star certificate for every unpaid `s_8` no-pivot state

Assume now that `A` has no `\eta`-pivot, satisfies `s_8(A)\ge1`, and has not been paid by (8). Applying (7) successively gives distinct original coordinates `i_1,i_2,i_3` such that
\[
\left(\mathbf1_{\{|A|\ge1/64\}}\right)_{i_1i_1}>\frac1{32},
\]
\[
\left(\mathbf1_{\{|A[-i_1,-i_1]|\ge1/64\}}\right)_{i_2i_2}>\frac1{32},
\]
and
\[
\left(\mathbf1_{\{|A[-\{i_1,i_2\},-\{i_1,i_2\}]|\ge1/64\}}\right)_{i_3i_3}>\frac1{32}.
\]
Because every retained physical diagonal remains below `\eta`, Lemma (9) yields the nested original-coordinate star bounds
\[
\boxed{
\|A[i_1,[n]\setminus\{i_1\}]\|_2>c_*,
}
\tag{11}
\]
\[
\boxed{
\|A[i_2,[n]\setminus\{i_1,i_2\}]\|_2>c_*,
}
\tag{12}
\]
\[
\boxed{
\|A[i_3,[n]\setminus\{i_1,i_2,i_3\}]\|_2>c_*,
}
\tag{13}
\]
where
\[
c_*:=\frac9{6400\sqrt2}
=0.0009943689110435824\ldots .
\tag{14}
\]
These are not spectral-coordinate statements: every norm in (11)--(13) is an actual row norm over a specified set of original independent coordinates.

## 5. Compilation with the previous exact `s_8` terminal theorem

The prior B08 theorem `QFORM-S8-TERMINAL-R2-SATURATION-v1` showed that if the existing order-three crossing-volume gate fails, then the only possible bad sampled ratio is `r=2`, and the corresponding completion has
\[
\|E\|_F\le\frac3{80},\qquad
\operatorname{rank}R\le6,
\qquad
\operatorname{rank}R_{L,L}\le2,
\]
\[
s_2(D)\ge\frac{77}{80},
\qquad
s_3(D)\le\frac{519}{1400},
\qquad
s_6(R)\ge\frac{1657}{2800}.
\tag{15}
\]
It also proved simultaneous saturation of all three rank-two support pieces and the determinant chain among pairwise-disjoint physical two-banks `S,H,T`.

Together with the present note, the normalized `s_8` problem is now reduced as follows.

* Any `\eta`-pivot is paid by the same scalar/pair arguments already used in the nine-eigenvalue reconstruction; the scalar child still has at least seven unit-scale eigenvalues, more than the five needed by the half-potential compiler.
* In the no-pivot case, if `V_3(A)\ge\kappa^3`, the reviewed marginal-free third-compound receiver gives
  \[
  \|p_Q\|_\infty
  \le160\,6^{4/3}<1744.436,
  \qquad p_Q\in C_0.
  \tag{16}
  \]
* If a parent, one-deletion child, or two-deletion child has a diffuse `1/64` window, (8) gives `<64` and `C_0`.
* Therefore every still-unpaid `s_8` state lies in the exact rank-two-saturation terminal chamber (15), satisfies the localization condition (7) simultaneously through two deletions, and carries the nested physical stars (11)--(13).

This is strictly stronger than the earlier `s_8` endpoint. It converts the abstract repeated child-localization alternative into three explicit, scale-separated original-coordinate coefficient witnesses while retaining the sharp nonsymmetric interpolation information.

## 6. Scaling

If instead `s_8(A)\ge s>0`, apply the normalized statements to `A/s`. The multi-deletion diffuse-window payment becomes
\[
\|p_Q\|_\infty<64K^2/s
\]
after the standard input/output scaling, and each nested star bound becomes
\[
\boxed{
\|A[i_r,\text{its remaining coordinates}]\|_2
>c_*s,\qquad r=1,2,3.
}
\tag{17}
\]
No assumption on moments, support, signs, log-concavity, or diagonalizability in the product coordinates is introduced.

## 7. Remaining implication

This does **not** prove the eight-eigenvalue density theorem. The remaining endpoint is now:

> consume the simultaneous `r=2` interpolation saturation (15), the pair-bank determinant chain from the previous B08 run, and the nested physical star chain (11)--(13), without rotating the input law or deleting the complementary spectrum.

A natural next receiver should use the three star witnesses together with the two saturated interpolation-defect channels. The current proof does not assert that the three stars are linearly independent; treating their row norms as a third compound would be invalid.

Full three-eigenvalue QFORM and global continuity remain open.
