# account02/B17 — diffusive-boundary variance tax and global Gaussian barrier

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260924T054220Z-account02-B17-QFORM-auto11`  
Status: `NEW GLOBAL SHARP-WITNESS OBSTRUCTION / PARTNER RESULT APPLIED / FULL TARGET OPEN`.

The unrestricted quadratic-form bounded-density conjecture remains open. This report pays the first unpaid implication left by the latest account03/B17 symmetric-satellite witness: what happens at the exact diffusive remote-support boundary `eps R^2 -> tau`, where the remote fragments contribute a non-vanishing variance and the partner's `eps R^2 -> 0` sharp-tip theorem no longer applies.

The answer is rigid. In the same exact dense rank-three target family, arbitrary bankwise symmetric remote satellites with finite asymptotic variance taxes have globally convergent output densities. No hidden off-tip peak appears. The limiting density is a centered Gaussian quadratic-form density whose global maximum is at zero and is at most `3 sqrt(2)`. In the isotropic case the complete sharp profile is

\[
\boxed{
\|p_{Q_m}\|_\infty\longrightarrow
\frac{3\sqrt2}{1+12\tau}.}
\]

Thus the partner's condition `eps R^2 -> 0` is exactly the zero-variance-tax face of a larger global phase diagram. Reaching a nonzero constant fraction of the true diffusive scale costs a strict constant factor in the sharp peak.

## 1. Exact dense target matrix

Let
\[
n=\frac{(1,2,3)}{\sqrt{14}},\qquad
B_m=I_3-\left(2+\frac1m\right)nn^\top,
\]
and let `T_m` be the `3m x 3` synthesis matrix with `m` copies of `e_j/sqrt(m)` in bank `j`. Put
\[
A_m=T_mB_mT_m^\top.
\]
Since `T_m^T T_m=I_3`,
\[
\boxed{\operatorname{spec}_{\ne0}(A_m)=\{1,1,-(1+1/m)\}.}\tag{1.1}
\]
Every finite matrix is entrywise dense: the off-diagonal entries of `B_m` are nonzero and its diagonal entries are
\[
\frac{12m-1}{14m},\qquad
\frac{3m-2}{7m},\qquad
-\frac{4m+9}{14m}.
\]
Thus every `A_m` is an exact source-valid target matrix with three eigenvalues of modulus at least one. No independence after spectral rotation is used for the finite physical inputs.

Write
\[
B=\lim_m B_m=I_3-2nn^\top.
\]
Then `B^2=I_3` and `B` has signature `(2,1)`.

## 2. Bankwise symmetric satellite laws at the variance boundary

For each bank `j=1,2,3`, choose sequences
\[
L_{j,m}\to\infty,\qquad L_{j,m}=o(m),
\]
set
\[
\varepsilon_{j,m}=\frac{L_{j,m}}m,\qquad
\ell_{j,m}=1-\varepsilon_{j,m},
\]
and choose `R_{j,m}->infinity` so that
\[
\boxed{
\tau_{j,m}:=\varepsilon_{j,m}R_{j,m}^2\longrightarrow\tau_j\in[0,\infty).}
\tag{2.1}
\]
For all sufficiently large `m` define the physical one-coordinate density in bank `j` by
\[
\begin{aligned}
f_{j,m}(x)=&\;\mathbf 1_{[-\ell_{j,m}/2,\ell_{j,m}/2]}(x)\\
&+\mathbf 1_{[R_{j,m}-\varepsilon_{j,m}/4,\,R_{j,m}+\varepsilon_{j,m}/4]}(x)\\
&+\mathbf 1_{[-R_{j,m}-\varepsilon_{j,m}/4,\,-R_{j,m}+\varepsilon_{j,m}/4]}(x).
\end{aligned}\tag{2.2}
\]
The three intervals are eventually disjoint. Their total length is one, so `0<=f_{j,m}<=1` and `int f_{j,m}=1`. The law is exactly centered by symmetry.

Use independent copies of this law in the `m` physical coordinates of bank `j`, independently across all three banks. Define
\[
Y_{j,m}=m^{-1/2}\sum_{k=1}^mX_{j,m,k},\qquad
Y_m=(Y_{1,m},Y_{2,m},Y_{3,m}).
\]
Then the actual quadratic form is
\[
Q_m=X^TA_mX=Y_m^TB_mY_m.
\]
The three bank sums are genuinely independent because the physical coordinate banks are disjoint.

The support gap in bank `j` is asymptotic to `R_{j,m}`. When `tau_j>0`, (2.1) gives the exact diffusive boundary scale
\[
R_{j,m}\sim\sqrt{\frac{\tau_jm}{L_{j,m}}}.\tag{2.3}
\]
The expected number of satellite visits in bank `j` is `L_{j,m}->infinity`, while the all-main probability is
\[
\prod_{j=1}^3(1-\varepsilon_{j,m})^m
=\exp\left(-\sum_jL_{j,m}+o\left(\sum_jL_{j,m}\right)\right)\to0.
\tag{2.4}
\]
So the construction remains genuinely remote-fragment dominated at the sample level.

## 3. Latest account03/B17 result applied: exact moments and the triangular CLT

The latest compatible designated partner is account03/B17 run
`20260924T053018Z-account03-B17-QFORM-auto11`, corrected at
`math-open-problems@7a64594fceb49b99698431a4d57b6658b49ebc28`, theorem
`QFORM-SYMMETRIC-SATELLITE-NEAR-DIFFUSIVE-SHARP-WITNESS-v1`.
Its exact one-coordinate moment identities apply bank by bank here. For a law (2.2),
\[
\boxed{
\operatorname{Var}(X_{j,m})
=\frac{\ell_{j,m}^3}{12}
+\varepsilon_{j,m}R_{j,m}^2
+\frac{\varepsilon_{j,m}^3}{48}.}
\tag{3.1}
\]
Therefore
\[
\sigma_{j,m}^2\longrightarrow
v_j:=\frac1{12}+\tau_j.\tag{3.2}
\]
The same partner computation gives
\[
\boxed{
\mathbb E|X_{j,m}|^3
=\frac{\ell_{j,m}^4}{32}
+\varepsilon_{j,m}R_{j,m}^3
+\frac{\varepsilon_{j,m}^3R_{j,m}}{16}.}
\tag{3.3}
\]
Since `tau_{j,m}` is bounded and `m eps_{j,m}=L_{j,m}->infinity`,
\[
\frac{R_{j,m}^2}{m}
=\frac{\tau_{j,m}}{L_{j,m}}\to0.
\]
Consequently
\[
\frac{\varepsilon_{j,m}R_{j,m}^3}{\sqrt m}
=\tau_{j,m}\frac{R_{j,m}}{\sqrt m}\to0,
\]
and the other terms in (3.3), divided by `sqrt(m)`, also vanish. Hence the Lyapunov ratio tends to zero:
\[
\frac{\mathbb E|X_{j,m}|^3}
{\sqrt m\,\sigma_{j,m}^3}\to0.\tag{3.4}
\]
Thus, without any moment hypothesis on the owner problem itself but using the exact finite moments of this explicit witness family,
\[
\boxed{Y_{j,m}\Rightarrow N(0,v_j)}\tag{3.5}
\]
for each bank. Independence of the physical banks gives
\[
Y_m\Rightarrow G\sim N(0,V),\qquad
V=\operatorname{diag}(v_1,v_2,v_3).
\tag{3.6}
\]
Since `B_m->B`, the continuous-mapping theorem yields
\[
Q_m\Rightarrow Q_\infty:=G^TBG.\tag{3.7}
\]
The partner theorem treated the special zero-tax face `tau_j=0` by a direct local CLT and cone formula. The next section globalizes (3.7) for every finite tax vector.

## 4. Required pinned result applied: Theorem F gives a uniform L1 Fourier envelope

Use the completed Fresnel--Brascamp--Lieb Theorem F from
`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Diagonalize
\[
B_m=O_m\operatorname{diag}(1,1,-c_m)O_m^T,
\qquad c_m=1+1/m,
\]
and use the physical eigenframe `V_m=T_mO_m`. Its columns are orthonormal and every physical row has squared leverage exactly
\[
\|V_m(i,:)\|^2=\frac1m.
\]
Taking all physical coordinates as the Theorem-F set `I`, its Gram matrix is exactly `I_3`, the residual quadratic part is zero (hence diagonal), and for `m>=2` every normalized leverage is at most `1/2`. Therefore the actual finite physical characteristic function
\[
\Psi_m(t)=\mathbb E e^{itQ_m}
\]
satisfies
\[
\boxed{
|\Psi_m(t)|
\le
\min\left\{1,
(4\pi)^{3/2}c_m^{-1/2}|t|^{-3/2}
\right\}
\le
M(t):=\min\{1,(4\pi)^{3/2}|t|^{-3/2}\}.}
\tag{4.1}
\]
This is a real inequality on the source-valid witness family. Its majorant is integrable and has exact mass
\[
\int_{\mathbb R}M(t)\,dt=24\pi.\tag{4.2}
\]

By (3.7), `Psi_m(t)->Psi_infinity(t)` pointwise. The pointwise limit also obeys `|Psi_infinity|<=M`. Dominated convergence now gives
\[
\boxed{
\int_{\mathbb R}|\Psi_m(t)-\Psi_\infty(t)|\,dt\to0.}
\tag{4.3}
\]
Fourier inversion therefore gives continuous densities at every sufficiently large finite stage and the global uniform convergence
\[
\boxed{
\|p_m-p_\infty\|_\infty\to0.}
\tag{4.4}
\]
In particular,
\[
\boxed{
\|p_m\|_\infty\to\|p_\infty\|_\infty.}
\tag{4.5}
\]
This is strictly stronger than cone-tip convergence: it excludes a hidden positive- or negative-level spike. It also shows how a generic proof constant can be much weaker than the true witness behavior: Theorem F itself gives only the universal finite ceiling `12`, but its integrable envelope is strong enough to transport the exact Gaussian limiting profile.

## 5. Gaussian global-max lemma

Let `v_0=1/12`. Since every `v_j=v_0+tau_j>=v_0`, write
\[
G=V^{1/2}Z,\qquad Z\sim N(0,I_3),
\]
and set
\[
C=V^{1/2}BV^{1/2}.
\]
The matrix `B` is an orthogonal reflection, so `s_min(B)=1`. Hence
\[
s_{\min}(C)
\ge s_{\min}(V^{1/2})^2s_{\min}(B)
\ge v_0.
\tag{5.1}
\]
By Sylvester inertia, `C` has two positive and one negative eigenvalue. Write them as
\[
a,\quad b,\quad -c,
\qquad a,b,c\ge v_0.\tag{5.2}
\]
At this point an orthogonal rotation is legitimate because `Z` is an isotropic Gaussian limit; no such independence claim is made for any finite physical input. Thus
\[
Q_\infty\stackrel d= aZ_1^2+bZ_2^2-cZ_3^2.
\]

### 5.1 The Gaussian density is globally maximized at zero

Let `U=aZ_1^2+bZ_2^2` and `W=cZ_3^2`. Their densities on `(0,infinity)` are independent. A standard direct convolution gives
\[
f_U(u)=\frac1{2\sqrt{ab}}
\exp\left[-\frac{a+b}{4ab}u\right]
I_0\left(\frac{|a-b|}{4ab}u\right),\tag{5.3}
\]
where `I_0` is the modified Bessel function. Since `I_1(x)<I_0(x)` for `x>0`,
\[
\frac d{du}\log f_U(u)
\le
-\frac{a+b-|a-b|}{4ab}
=-\frac1{2\max(a,b)}<0.\tag{5.4}
\]
So `f_U` is decreasing. Also
\[
f_W(u)=\frac{e^{-u/(2c)}}{\sqrt{2\pi cu}}
\tag{5.5}
\]
is decreasing.

For `s>=0`,
\[
p_\infty(s)=\int_0^\infty f_U(s+u)f_W(u)\,du
\le p_\infty(0).
\]
For `r>=0`,
\[
p_\infty(-r)=\int_0^\infty f_U(u)f_W(u+r)\,du
\le p_\infty(0).
\]
Therefore
\[
\boxed{\|p_\infty\|_\infty=p_\infty(0).}\tag{5.6}
\]

### 5.2 Exact cone integral and the `3 sqrt(2)` barrier

For standard Gaussian coordinates and eigenvalues `(a,b,-c)`, rescale the zero cone by
`u=sqrt(a) z_1`, `v=sqrt(b) z_2`, `w=sqrt(c) z_3`. Resolving `w=+/-sqrt(u^2+v^2)` gives
\[
\boxed{
p_\infty(0)=
\frac1{4\pi\sqrt{abc}}
\int_0^{2\pi}
\frac{d\theta}
{\sqrt{\cos^2\theta/a+\sin^2\theta/b+1/c}}.}
\tag{5.7}
\]
The integrand can be rewritten pointwise as
\[
\frac1{\sqrt{bc\cos^2\theta+ac\sin^2\theta+ab}}.
\]
Because `a,b,c>=v_0`,
\[
bc\cos^2\theta+ac\sin^2\theta+ab
\ge v_0^2(\cos^2\theta+\sin^2\theta)+v_0^2
=2v_0^2.
\tag{5.8}
\]
Hence
\[
\boxed{
\|p_\infty\|_\infty
=p_\infty(0)
\le\frac1{2\sqrt2\,v_0}
=3\sqrt2.}
\tag{5.9}
\]
Equality in (5.8) for almost every angle forces `a=b=c=v_0`. Then
`abc=|det C|=det V=v_1v_2v_3=v_0^3`; because every `v_j>=v_0`, equality forces `v_1=v_2=v_3=v_0`, i.e. every `tau_j=0`. Therefore any nonzero finite asymptotic variance tax in any bank produces a strict limiting gap below `3 sqrt(2)`.

Combining (4.5) and (5.9) proves the anisotropic global barrier
\[
\boxed{
\limsup_{m\to\infty}\|p_{Q_m}\|_\infty\le3\sqrt2,}
\tag{5.10}
\]
with strict inequality in the limit whenever at least one `tau_j>0`.

## 6. Exact isotropic variance-tax profile

If all three banks use the same tax
\[
\tau_1=\tau_2=\tau_3=\tau,
\]
then
\[
V=vI_3,\qquad v=\frac1{12}+\tau,
\]
so `C=vB` has eigenvalues `(v,v,-v)`. Formula (5.7) is then explicit:
\[
\boxed{
\|p_\infty\|_\infty
=\frac1{2\sqrt2v}
=\frac{3\sqrt2}{1+12\tau}.}
\tag{6.1}
\]
By (4.5),
\[
\boxed{
\|p_{Q_m}\|_\infty
\longrightarrow
\frac{3\sqrt2}{1+12\tau}.}
\tag{6.2}
\]
The full limiting density is also explicit. For `s>=0`,
\[
p_\infty(s)
=\frac1{2\sqrt2v}e^{-s/(2v)},\tag{6.3}
\]
and for `r>=0`,
\[
p_\infty(-r)
=\frac1{2\sqrt2v}
 e^{r/(2v)}\operatorname{erfc}\!\left(\sqrt{r/v}\right).
\tag{6.4}
\]
Both sides are strictly below the tip away from zero.

This gives an exact quantitative answer at the partner's missing boundary. If `tau=0`, the sharp obstruction `3sqrt(2)` is recovered. If `tau>0`, the remote fragments impose the multiplicative loss
\[
\boxed{\frac1{1+12\tau}.}\tag{6.5}
\]

## 7. Diffusive-scale near-sharp witnesses

For any prescribed loss `eta in (0,1)`, choose
\[
\tau=\frac{\eta}{12(1-\eta)}.
\tag{7.1}
\]
Then the limiting peak is exactly
\[
\boxed{
\|p_{Q_m}\|_\infty\to(1-\eta)3\sqrt2.}
\tag{7.2}
\]
At the same time one may take any slowly diverging `L_m=o(m)` and
\[
R_m=\sqrt{\frac{\tau m}{L_m}},\tag{7.3}
\]
so the support gap is a nonzero constant multiple of the full diffusive boundary `sqrt(m/L_m)`, the expected number of remote coordinates is `3L_m->infinity`, and the all-main probability tends to zero exponentially in `L_m`.

For example, with `L_m=log log m` and `tau=1/1200`, the gap is asymptotic to
\[
\sqrt{\frac{m}{1200\log\log m}},
\]
while
\[
\|p_{Q_m}\|_\infty\to\frac{3\sqrt2}{1.01}
=4.20063434368\ldots .
\]
Thus almost-root-`m` fragmentation can remain arbitrarily near sharp, but any fixed nonzero variance tax prevents an overshoot of `3sqrt(2)`.

## 8. What this rules out and what remains unpaid

This is not a counterexample to QFORM and does not prove that `3sqrt(2)` is the universal sharp constant. It rules out a broad adversarial mechanism inside the exact dense three-bank witness architecture:

* symmetric remote fragmentation cannot create a hidden off-tip spike when each bank has a finite variance tax;
* anisotropic variance pumping across the three independent banks cannot raise the Gaussian-limit peak above `3sqrt(2)`;
* the sharp `3sqrt(2)` face is uniquely the zero-tax/minimum-variance face inside this phase diagram;
* central-cell localization is still invalid, since the all-main probability tends to zero and many remote coordinates occur with high probability.

The surviving B17 witness mechanisms are therefore outside this finite-tax Gaussian basin: genuinely non-Gaussian multiscale arrays that fail a triangular CLT while retaining cap one, several macroscopic non-collinear shared rows that do not collapse to three independent bank sums, or additional active spectrum whose contribution survives aggregation. A failure of the present Fourier-envelope/CLT mechanism in those regimes would be only a proof-mechanism failure. A finite peak above `3sqrt(2)` would refute the proposed sharp constant; a genuine counterexample to QFORM must defeat every finite universal bound.

Full QFORM: **OPEN / NOT PROVED / NOT DISPROVED**.  
Full-target continuity: **OPEN**.  
No Monte Carlo or heuristic histogram is used in this theorem.
