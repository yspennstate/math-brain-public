# Six-variable dense triangular-bank rotation: exact cone-tip witness above 4.063

Run: `20260923T144233Z-fleet01-B17-QFORM-auto11`  
Assignment: fleet01/B17, sharp constant and witnesses.  
Status: `SUPPORTING_EXACT_FINITE_WITNESS`; the unrestricted QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. Full-target continuity remains separate.  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. New exact finite witness

Let `U_{j,k}`, `j=1,2,3`, `k=1,2`, be six independent `Unif[-1/2,1/2]` variables and

\[
S_j={U_{j,1}+U_{j,2}\over\sqrt2},\qquad S=(S_1,S_2,S_3)^T.
\]
Each `S_j` has the exact triangular density

\[
h(s)=\sqrt2(1-\sqrt2|s|)_+.
\tag{1.1}
\]
The three banks remain independent because they use disjoint original coordinates.

Take

\[
n={1\over\sqrt3}(1,1,1)^T,
\qquad
B=I_3-2nn^T={1\over3}
\begin{pmatrix}
1&-2&-2\\
-2&1&-2\\
-2&-2&1
\end{pmatrix}.
\tag{1.2}
\]
Thus `spec(B)={1,1,-1}`. Define `Q=S^TBS`. If
`X=(U_{1,1},U_{1,2},U_{2,1},U_{2,2},U_{3,1},U_{3,2})`, then `Q=X^TAX` with

\[
A={1\over6}
\begin{pmatrix}
1&1&-2&-2&-2&-2\\
1&1&-2&-2&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&1&1&-2&-2\\
-2&-2&-2&-2&1&1\\
-2&-2&-2&-2&1&1
\end{pmatrix}.
\tag{1.3}
\]
The loading matrix has two copies of `e_j/sqrt(2)` in bank `j`, hence is Parseval. Therefore

\[
\boxed{\operatorname{spec}(A)=\{1,1,-1,0,0,0\}}.
\tag{1.4}
\]
Every entry of `A` is nonzero, so this is a genuinely dense physical-coordinate target instance, not a diagonal control.

The exact cone-tip density is

\[
\boxed{p_Q(0)=4.06307061680603726012548\ldots>4.063.}
\tag{1.5}
\]
Consequently this gives a finite six-variable source-valid lower witness strictly stronger than the previously pinned aligned six-uniform value

\[
2\pi-{7\over3}=3.949851973\ldots .
\tag{1.6}
\]
It still lies below the stronger asymptotic obstruction `3sqrt(2)=4.242640687...`; hence the best currently source-valid universal lower bound remains `C_univ>=3sqrt(2)`.

## 2. Exact coarea reduction

Write `q(y)=y^TBy=|y|^2-2(n\cdot y)^2`. A positive null-cone sheet on the unit sphere can be parameterized by

\[
\omega(\theta)={n+v(\theta)\over\sqrt2},\qquad
v(\theta)\perp n,\quad |v(\theta)|=1.
\]
Since the product density `rho(y)=prod_j h(y_j)` is coordinatewise even, the two cone sheets contribute equally. On a cone ray `y=r omega`, surface measure divided by `|grad q|` is `dr dtheta/(2sqrt(2))` per sheet. Thus

\[
p_Q(0)={1\over\sqrt2}\int_0^{2\pi}\int_0^\infty
\prod_{j=1}^3h(r\omega_j(\theta))\,dr\,d\theta.
\tag{2.1}
\]
With `c_j=sqrt(2)|omega_j|` and `M=max_j c_j`, (1.1) turns the radial integral into

\[
\int_0^{1/M}\prod_{j=1}^3(1-c_jr)\,dr.
\]
If `M=c_1`, elementary expansion gives

\[
J(c_1,c_2,c_3)
={1\over2c_1}-{c_2+c_3\over6c_1^2}+{c_2c_3\over12c_1^3}.
\tag{2.2}
\]
The prefactors in (2.1) and (1.1) cancel to

\[
p_Q(0)=2\int_0^{2\pi}J(\theta)\,d\theta.
\tag{2.3}
\]
No arbitrary-joint coarea inequality is used here: (2.1) is an exact calculation for this explicit independent-bank product density.

## 3. Symmetry and elementary closed form

Choose the phase so that

\[
\begin{aligned}
\omega_1(\theta)&={1\over\sqrt6}+{1\over\sqrt3}\cos\theta,\\
\omega_2(\theta)&={1\over\sqrt6}+{1\over\sqrt3}\cos(\theta-2\pi/3),\\
\omega_3(\theta)&={1\over\sqrt6}+{1\over\sqrt3}\cos(\theta+2\pi/3).
\end{aligned}
\tag{3.1}
\]
The integrand is invariant under the dihedral symmetries permuting the three coordinates, so

\[
p_Q(0)=12\int_0^{\pi/3}J(\theta)\,d\theta.
\tag{3.2}
\]
On `0<=theta<=pi/3`, `omega_1` is largest in absolute value, `omega_2>=0`, and `omega_3` changes sign only at `theta=pi/12`. Hence (2.2) has only two rational half-angle cells.

Put `t=tan(theta/2)` and `c=1+sqrt(2)`. The breakpoints are `t_0=tan(pi/24)` and `t_1=tan(pi/6)=1/sqrt(3)`. Including `dtheta=2dt/(1+t^2)`, the first-cell integrand is

\[
\begin{aligned}
R_+(t)=&-{7\sqrt3\over4(t-c)}-{9\sqrt6+17\sqrt3\over8(t-c)^2}
-{2\sqrt6+3\sqrt3\over4(t-c)^3}\\
&+{7\sqrt3\over4(t+c)}-{9\sqrt6+17\sqrt3\over8(t+c)^2}
+{2\sqrt6+3\sqrt3\over4(t+c)^3},
\end{aligned}
\tag{3.3}
\]
and the second-cell integrand is

\[
\begin{aligned}
R_-(t)=&{\sqrt3\over12(t-c)}+{9\sqrt3+5\sqrt6-4\sqrt2-8\over8(t-c)^2}
+{2\sqrt6+3\sqrt3\over4(t-c)^3}\\
&-{\sqrt3\over12(t+c)}+{9\sqrt3+5\sqrt6+4\sqrt2+8\over8(t+c)^2}
-{2\sqrt6+3\sqrt3\over4(t+c)^3}.
\end{aligned}
\tag{3.4}
\]
Thus

\[
p_Q(0)=12\left(\int_0^{t_0}R_+(t)dt+\int_{t_0}^{t_1}R_-(t)dt\right).
\tag{3.5}
\]
Both have elementary rational/logarithmic antiderivatives. Let

\[
A_+=9\sqrt6+17\sqrt3,\qquad D=2\sqrt6+3\sqrt3.
\]
One may take

\[
F_+(t)={7\sqrt3\over4}\log{t+c\over c-t}
+{A_+\over8}\left({1\over t-c}+{1\over t+c}\right)
+{D\over8}\left({1\over(t-c)^2}-{1\over(t+c)^2}\right),
\tag{3.6}
\]
and, with

\[
C_-=9\sqrt3+5\sqrt6-4\sqrt2-8,\qquad
C_+=9\sqrt3+5\sqrt6+4\sqrt2+8,
\]

\[
F_-(t)={\sqrt3\over12}\log{c-t\over c+t}
-{C_-\over8(t-c)}-{C_+\over8(t+c)}
-{D\over8(t-c)^2}+{D\over8(t+c)^2}.
\tag{3.7}
\]
Direct differentiation gives `F_+'=R_+` and `F_-'=R_-`. Therefore

\[
\boxed{
p_Q(0)=12\{F_+(t_0)-F_+(0)+F_-(t_1)-F_-(t_0)\}.
}
\tag{3.8}
\]
Directed interval evaluation of this exact endpoint expression gives

\[
4.063070616806037260125484422593499956752965346063914292086712935024256
< p_Q(0)
<4.063070616806037260125484422593499956752965346063914292086712935024278.
\tag{3.9}
\]
The accompanying checker verifies the matrix spectrum, differentiates both antiderivatives symbolically, and reproduces (3.9) with interval arithmetic.

## 4. What the witness constrains

The older six-uniform control uses the aligned core `diag(1,1,-1)` and has cone-tip value `2pi-7/3`. The present construction keeps exactly the same six independent cap-one physical variables and exactly the same nonzero spectrum but rotates the minority-sign eigendirection to `(1,1,1)/sqrt(3)`. The finite cone tip increases by

\[
4.063070616806\ldots-(2\pi-7/3)=0.113218643837\ldots .
\]
Thus already at six variables, signature orientation relative to the product-bank geometry materially changes the density. A sharp proof depending only on the nonzero eigenvalues, bank sizes, or row leverages misses this finite effect.

This finite stress still stays below the diffuse `3sqrt(2)` obstruction. It supports, but does not prove, the hypothesis that Gaussianized diffuse banks are more dangerous than small fixed-bank rotations.

## 5. Designated partner result applied to an actual inequality

The latest completed fleet02/B17 theorem is source-pinned at
`yspennstate/math-open-problems@9cd98044087dd0e8bafe8ee2900cf1686552c802`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B17/20260923T142532Z-fleet02-B17-QFORM-auto11/REPORT.md`.
It proves, for arbitrary unit vectors `a,b`, centered unit-interval banks `S_a,T_b`, and every independent heavy law with density `f<=1`,

\[
\|p_{X_f^2+S_a^2-T_b^2}\|_\infty
\le K_*={\pi\over2}(\sqrt2+2^{1/4})
=4.089443637123813\ldots<3\sqrt2.
\tag{5.1}
\]
Apply it concretely to `a=(1,1)/sqrt(2)` and `b=(1,1,1)/sqrt(3)`. Then for arbitrary independent cap-one `X_f` and independent centered unit intervals `U_1,U_2,V_1,V_2,V_3`,

\[
\boxed{
\left\|p_{\,X_f^2+((U_1+U_2)/\sqrt2)^2-((V_1+V_2+V_3)/\sqrt3)^2}\right\|_\infty
\le4.089443637123813\ldots<3\sqrt2.
}
\tag{5.2}
\]
The physical matrix in (5.2) has exact nonzero spectrum `{1,1,-1}`. Thus the partner result genuinely closes an unequal finite-bank architecture adjacent to the present six-variable stress: the present dense three-bank rotation reaches `4.06307...`, while the whole one-heavy/two-unequal-bank class remains below `4.08945`.

## 6. Scope and correction compatibility

This report does **not** assert that zero is the global mode of the new six-variable rotated form; one exact value `p_Q(0)>4.063` is enough for a lower witness. It does not improve the stronger universal lower obstruction `3sqrt(2)`, and it does not prove the unrestricted sharp constant is `3sqrt(2)`.

The proof stays in original independent physical coordinates until the three disjoint banks are aggregated, and thereafter uses their exact independent triangular densities. It uses no law-uniform pointwise oscillatory decay, no independence after a general spectral rotation, no arbitrary-joint coarea bound, no conditional-density positive-moment gate, no bounded-fragment reduction, and no uniformly conditioned physical minor/cross-cut claim. The full QFORM conjecture and full-target continuity remain open.
