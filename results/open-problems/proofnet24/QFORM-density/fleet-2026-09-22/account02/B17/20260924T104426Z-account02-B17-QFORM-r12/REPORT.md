# account02/B17 — growing-direction uniform-convolution barrier

Run: `20260924T104426Z-account02-B17-QFORM-r12`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `SUPPORTING_SHARP-WITNESS_THEOREM / FULL QFORM OPEN`

## 1. First unpaid implication paid

The preceding B17 run ruled out a **fixed finite** tight frame of non-collinear root-`m` Poisson jump directions when an isotropic cap-one diffuse carrier Gaussianizes. The first unpaid sharp-witness mechanism was a number of macroscopic directions growing with dimension/scale.

This report pays that mechanism for a substantially larger, source-valid class. The number of possible macroscopic jump directions grows like the physical dimension and may become dense on the sphere; the jump amplitudes/laws need not be tight and need not possess any moments. The only structural feature retained is an exact independent unit-uniform convolution carrier in every physical coordinate.

The unrestricted QFORM conjecture is **not** proved here. No moment, bounded-support, log-concavity, diagonal-basis independence, or post-rotation independence assumption is added to the conjecture. The theorem below is a no-go theorem for a concrete adversarial witness architecture.

## 2. Rotated tetrahedral tight frame and exact target spectrum

Let

\[
t_1={1\over\sqrt3}(1,1,1),\quad
 t_2={1\over\sqrt3}(1,-1,-1),\quad
 t_3={1\over\sqrt3}(-1,1,-1),\quad
 t_4={1\over\sqrt3}(-1,-1,1).
\]

Then

\[
\sum_{a=1}^4 t_at_a^T={4\over3}I_3.
\tag{2.1}
\]

For each `K>=2`, choose **arbitrary** rotations `R_1,...,R_K in SO(3)` and form the `4K x 3` physical synthesis matrix `T_K` whose row indexed by `(k,a)` is

\[
r_{k,a}=\sqrt{{3\over4K}}\,R_kt_a.
\tag{2.2}
\]

By (2.1),

\[
T_K^TT_K=I_3,
\qquad
\|r_{k,a}\|^2={3\over4K}\le {1\over2}.
\tag{2.3}
\]

Let `B_K=B_K^T` be any real `3 x 3` matrix whose three eigenvalues satisfy

\[
|\lambda_j(B_K)|\ge1,\qquad j=1,2,3,
\tag{2.4}
\]

and set

\[
A_K=T_KB_KT_K^T.
\tag{2.5}
\]

Since `T_K` is an isometry on `R^3`, the nonzero spectrum is **exactly**

\[
\boxed{\operatorname{spec}_{\ne0}(A_K)=\operatorname{spec}(B_K).}
\tag{2.6}
\]

Thus every finite stage is an exact physical target instance. No spectral rotation is used to assert independence.

A convenient dense rank-three stress coefficient is the reflection

\[
n={1\over\sqrt{14}}(1,2,3)^T,
\qquad
B=I_3-2nn^T
={1\over7}
\begin{pmatrix}
6&-2&-3\\
-2&3&-6\\
-3&-6&-2
\end{pmatrix},
\tag{2.7}
\]

for which `B^2=I`, `det B=-1`, and

\[
\operatorname{spec}(B)=\{1,1,-1\}.
\tag{2.8}
\]

## 3. Arbitrarily rough additive physical noise while keeping the density cap

For every physical coordinate `i=(k,a)`, let

\[
U_i\sim\mathrm{Unif}[-1/2,1/2]
\]

independently. Let `J_i` be arbitrary independent real random variables, independent also of all the `U_i`; their laws may be discrete, singular, unbounded, non-identical, and may have no finite moments. Put

\[
X_i=U_i+J_i.
\tag{3.1}
\]

Then the `X_i` remain independent and each has a Lebesgue density

\[
f_i(x)=\int \mathbf 1_{[-1/2,1/2]}(x-y)\,d\nu_i(y)
      =\Pr\{J_i\in[x-1/2,x+1/2]\},
\tag{3.2}
\]

hence

\[
\boxed{0\le f_i\le1,\qquad \int f_i=1.}
\tag{3.3}
\]

This is a source-valid cap-one product law. The additive decomposition is a feature of this witness class, not an assumption on arbitrary QFORM inputs.

Writing

\[
S_K=T_K^TU,
\qquad
M_K=T_K^TJ,
\tag{3.4}
\]

we have the exact active-space decomposition

\[
T_K^TX=S_K+M_K,
\qquad
S_K\perp M_K.
\tag{3.5}
\]

No tightness or convergence assumption on `M_K` will be used.

## 4. Uniform local CLT for the rotated tetrahedral carrier

Define the single-block random vector

\[
W=\sqrt{{3\over4}}\sum_{a=1}^4 t_aU_a.
\tag{4.1}
\]

Then `EW=0` and, by (2.1),

\[
\operatorname{Cov}(W)={1\over12}I_3.
\tag{4.2}
\]

The carrier is

\[
S_K={1\over\sqrt K}\sum_{k=1}^KR_kW_k,
\tag{4.3}
\]

where `W_k` are independent copies of `W`.

With `sinc x=sin(x)/x`, its one-block characteristic function is

\[
\phi_W(\eta)
 =\prod_{a=1}^4
 \operatorname{sinc}\!\left({\sqrt3\over4}t_a\cdot\eta\right).
\tag{4.4}
\]

Near zero,

\[
\log\phi_W(\eta)=-{|\eta|^2\over24}+O(|\eta|^4),
\tag{4.5}
\]

uniformly in direction. Therefore for every fixed `xi`, uniformly over all choices of rotations,

\[
\widehat g_K(\xi)
=\prod_{k=1}^K\phi_W(R_k^T\xi/\sqrt K)
\longrightarrow e^{-|\xi|^2/24}.
\tag{4.6}
\]

The crucial global Fourier tail is also uniform in the rotations. For every unit vector `u`,

\[
\sum_{a=1}^4(t_a\cdot u)^2={4\over3}.
\tag{4.7}
\]

Hence at least two of the four numbers `|t_a dot u|` are at least `1/3`: otherwise one contributes at most `1` and the other three contribute strictly less than `3(1/3)^2`, contradicting (4.7). Using `|sinc x|<=min(1,1/|x|)` gives

\[
\boxed{|\phi_W(\eta)|\le\min\{1,48|\eta|^{-2}\}.}
\tag{4.8}
\]

There are constants `delta,c>0` such that

\[
|\phi_W(\eta)|\le e^{-c|\eta|^2},\qquad |\eta|\le\delta.
\tag{4.9}
\]

For every fixed `R>delta`, continuity and nondegeneracy give

\[
\rho_{\delta,R}:=\sup_{\delta\le|\eta|\le R}|\phi_W(\eta)|<1.
\tag{4.10}
\]

Thus Fourier space splits into three uniform zones:

- for `|xi|<=delta sqrt(K)`, `|hat g_K(xi)|<=e^{-c|xi|^2}`;
- for `delta sqrt(K)<=|xi|<=R sqrt(K)`, `|hat g_K(xi)|<=rho_{delta,R}^K`;
- for `|xi|>=R sqrt(K)`, (4.8) gives

\[
|\widehat g_K(\xi)|
\le\left({48K\over|\xi|^2}\right)^K.
\tag{4.11}
\]

For any fixed `R>sqrt(48)`, the last zone has integral

\[
4\pi(48K)^K{(R\sqrt K)^{3-2K}\over2K-3}
={4\pi K^{3/2}\over2K-3}\,48^K R^{3-2K}\to0.
\tag{4.12}
\]

The medium zone is `O(K^{3/2}rho^K)`, and the low zone is handled by dominated convergence. Consequently

\[
\|\widehat g_K-e^{-|\xi|^2/24}\|_{L^1(\mathbb R^3)}\to0,
\tag{4.13}
\]

uniformly over all rotation choices. Fourier inversion yields uniform convergence of the densities to

\[
\gamma(x)=\left({6\over\pi}\right)^{3/2}e^{-6|x|^2}.
\tag{4.14}
\]

Finally, `E|S_K|^2=tr(I_3/12)=1/4` for every `K`. Uniform convergence on bounded balls plus the common Chebyshev tail and the Gaussian tail imply the stronger total-variation statement

\[
\boxed{\varepsilon_K:=\sup_{R_1,\ldots,R_K}\|g_K-\gamma\|_1\longrightarrow0.}
\tag{4.15}
\]

This is the only local-limit input needed below.

## 5. Pinned Fresnel theorem gives a shift-uniform finite-stage anti-spike envelope

Fix `K`, a deterministic active shift `z in R^3`, and write

\[
Q_{K,z}=(S_K+z)^TB_K(S_K+z).
\tag{5.1}
\]

Diagonalize only the coefficient matrix,

\[
B_K=O\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)O^T.
\]

The corresponding **physical** eigenframe is `V_K=T_KO`. By (2.3),

\[
V_K^TV_K=I_3,
\qquad
\|\operatorname{row}_iV_K\|^2={3\over4K}\le{1\over2},
\tag{5.2}
\]

and the residual physical quadratic block is zero.

Conditioning on the additive noises `J` makes `z=T_K^TJ` deterministic and leaves the original `U_i` independent unit-interval variables. Expanding `(S_K+z)^TB_K(S_K+z)` adds only a physical linear term. The completed pinned Fresnel--Brascamp--Lieb Theorem F at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

explicitly permits such a linear term. Applying it to this actual physical frame gives, for every shift `z`,

\[
|\Phi_{K,z}(t)|
\le (4\pi)^{3/2}|t|^{-3/2}
|\lambda_1\lambda_2\lambda_3|^{-1/2}
\le (4\pi)^{3/2}|t|^{-3/2}.
\tag{5.3}
\]

Together with `|Phi|<=1`,

\[
\boxed{|\Phi_{K,z}(t)|\le M_F(t):=
\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.}
\tag{5.4}
\]

The exact majorant mass is

\[
\int_\mathbb R M_F(t)dt=24\pi.
\tag{5.5}
\]

This is a real finite-stage obstruction, not a law-uniform stationary-phase claim: it uses the completed low-leverage physical-frame theorem exactly in its proved scope.

## 6. Uniform-in-shift comparison with the Gaussian quadratic form

Let `G~N(0,I_3/12)` and

\[
Q^G_{K,z}=(G+z)^TB_K(G+z).
\tag{6.1}
\]

Let `h_{K,z}` and `h^G_{K,z}` denote the output densities. From (4.15), for every `t,z,B_K`,

\[
|\Phi_{K,z}(t)-\Phi^G_{K,z}(t)|
\le\|g_K-\gamma\|_1\le\varepsilon_K.
\tag{6.2}
\]

The Gaussian characteristic function supplies a second shift-uniform integrable envelope. With `v=1/12`, diagonalizing `B_K` only inside the Gaussian comparator gives

\[
|\Phi^G_{K,z}(t)|
\le\prod_{j=1}^3(1+4v^2\lambda_j^2t^2)^{-1/4}
\le(1+t^2/36)^{-3/4}
\le 6^{3/2}|t|^{-3/2}.
\tag{6.3}
\]

The noncentral exponential factor has modulus at most one. Hence with

\[
C_*=(4\pi)^{3/2}+6^{3/2},
\tag{6.4}
\]

we have the pointwise **uniform-in-shift** difference bound

\[
|\Phi_{K,z}(t)-\Phi^G_{K,z}(t)|
\le\min\{\varepsilon_K,C_*|t|^{-3/2}\}.
\tag{6.5}
\]

Integrating explicitly at the crossover `t_0=(C_*/epsilon_K)^{2/3}` gives

\[
\int_\mathbb R
\min\{\varepsilon_K,C_*|t|^{-3/2}\}\,dt
=6C_*^{2/3}\varepsilon_K^{1/3}.
\tag{6.6}
\]

Fourier inversion therefore yields the quantitative bridge

\[
\boxed{
\sup_z\|h_{K,z}-h^G_{K,z}\|_\infty
\le {3\over\pi}C_*^{2/3}\varepsilon_K^{1/3}
=:\delta_K\longrightarrow0.
}
\tag{6.7}
\]

Numerically `(3/pi) C_*^(2/3)=14.5121633802...`; no rate for `epsilon_K` is needed.

## 7. Latest account03/B17 comparator closes the sharp barrier

The latest compatible designated partner theorem is account03/B17

`QFORM-GAUSSIAN-FULLTARGET-COMPARATOR-v1`,
`math-open-problems@ea855178c7771925095c4517c830888c9a8938ea`.

It proves that for every Gaussian `H~N(mu,Sigma)` with `Sigma>=vI` and every symmetric coefficient matrix having at least three eigenvalues of magnitude at least `s`,

\[
\|p_{H^TAH}\|_\infty\le{1\over2\sqrt2\,vs}.
\tag{7.1}
\]

Apply this with dimension three, `Sigma=I_3/12`, `s=1`, and arbitrary mean `z`. Uniformly in `z` and in every `B_K` satisfying (2.4),

\[
\boxed{\|h^G_{K,z}\|_\infty\le3\sqrt2.}
\tag{7.2}
\]

Combining (6.7) and (7.2),

\[
\boxed{
\sup_z\|h_{K,z}\|_\infty
\le3\sqrt2+\delta_K,
\qquad \delta_K\to0.
}
\tag{7.3}
\]

Now condition on the entire rough-noise vector `J`. Given `J`, the active shift is simply `z=M_K=T_K^TJ`; no property of its conditional value is needed. Averaging the conditional densities cannot increase the uniform bound, so for the original source-valid product law

\[
\boxed{
\|p_{X^TA_KX}\|_\infty
\le3\sqrt2+\delta_K.
}
\tag{7.4}
\]

The error `delta_K` is independent of **all** additive-noise laws and of the rotation sequence. Therefore

\[
\boxed{
\limsup_{K\to\infty}
\sup_{\substack{R_1,\dots,R_K\\
B_K:\ |\lambda_j(B_K)|\ge1\\
\nu_{k,a}\ \mathrm{arbitrary}}}
\|p_{X^TA_KX}\|_\infty
\le3\sqrt2.
}
\tag{7.5}
\]

This is the main new obstruction.

## 8. Explicit growing-direction non-Lindeberg stress

Choose the rotations `R_k` so that the countable set

\[
\{R_kt_a:k\ge1,\ 1\le a\le4\}
\]

is dense on `S^2`. Thus the number of possible macroscopic directions in stage `K` is `4K` and grows without bound.

Fix `c,lambda>0`. For every coordinate `(k,a)` at stage `K`, choose independently

\[
J_{k,a}^{(K)}=
\begin{cases}
0,&1-\lambda/(4K),\\
+D_K,&\lambda/(8K),\\
-D_K,&\lambda/(8K),
\end{cases}
\qquad
D_K=c\sqrt{{4K\over3}}.
\tag{8.1}
\]

Then each original input `X=U+J` has the explicit cap-one density

\[
\begin{aligned}
f_K(x)={}&\left(1-{\lambda\over4K}\right)
\mathbf1_{[-1/2,1/2]}(x)\\
&+{\lambda\over8K}
\mathbf1_{[D_K-1/2,D_K+1/2]}(x)
+{\lambda\over8K}
\mathbf1_{[-D_K-1/2,-D_K+1/2]}(x),
\end{aligned}
\tag{8.2}
\]

for all sufficiently large `K`, with the three intervals disjoint. The density integrates to one and is everywhere at most one.

A rare jump contributes exactly

\[
r_{k,a}(\pm D_K)=\pm cR_kt_a
\tag{8.3}
\]

in active space. The expected number of such jumps among the `4K` coordinates is exactly `lambda`. For every fixed `0<eta<c`, the active-space Lindeberg tail satisfies

\[
\sum_{k,a}
\mathbb E\left[
\|r_{k,a}X_{k,a}\|^2
\mathbf1_{\{\|r_{k,a}X_{k,a}\|>\eta\}}
\right]
\longrightarrow\lambda c^2>0.
\tag{8.4}
\]

So this family is genuinely non-Lindeberg and retains root-dimension macroscopic jumps in a number of possible non-collinear directions tending to infinity. Nevertheless (7.4) gives

\[
\boxed{
\limsup_{K\to\infty}\|p_{X^TA_KX}\|_\infty\le3\sqrt2.
}
\tag{8.5}
\]

For the reflection (2.7), every finite matrix has exact nonzero spectrum `{1,1,-1}`.

## 9. What this rules out, and what remains unpaid

This theorem shows that merely increasing the number of surviving macroscopic jump directions—even to a dense set of directions—and allowing arbitrary rough, non-tight, momentless additive noise does **not** create a peak above `3 sqrt(2)` when every physical source retains an independent unit-uniform convolution carrier and the active rank-three geometry is a vanishing-leverage tight frame.

The mechanism is stronger than convergence of the jump field: the proof never asks `M_K` to converge, be tight, or have moments. The conditional bound is uniform in its realized shift.

The surviving sharp-witness frontier is therefore more specific:

1. rough cap-one sources with no common independent unit-uniform convolution factor / a genuinely non-Gaussian diffuse carrier;
2. dependence between the diffuse carrier and the macroscopic component created before aggregation, so conditioning cannot reduce the latter to a pure location shift;
3. additional active spectrum or residual quadratic structure outside the exact rank-three low-leverage Theorem-F receiver;
4. high-dimensional mechanisms that deplete the `I/12` Gaussian core rather than merely translate it.

Failure of the present argument in those classes would be a **proof-mechanism failure**, not a counterexample to QFORM. A finite example above `3 sqrt(2)` refutes the proposed sharp constant only; a genuine counterexample to QFORM must defeat every finite universal density bound.

The unrestricted QFORM conjecture and unrestricted continuity remain open.
