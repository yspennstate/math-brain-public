# Rank-two fractional potentials: verified refinements and provenance

**Status:** Complete arguments for the stated restricted theorems. The unrestricted three-eigenvalue density problem remains open. These estimates improve constants in previously available rank-two arguments; they are not a proof of the unrestricted conjecture. No priority or novelty claim is made.

**Source:** `proofnet24/QFORM-density/interactive/20260922T161801Z-rank-two-fusion/REPORT.md`, blob `00681629acaba8f2e04edda6c9f6b5c4f0fdafa4`, in `yspennstate/math-open-problems`. That report gives the valid constants 128 for arbitrary affine terms and $16\sqrt{30}$ for affine terms in the range. The present version keeps the same conditioning argument, sharpens the scalar kernel constant from 8 to 5, and uses the sharp diffuse Fourier estimate to sharpen the rank-one small-ball constant to 8. The resulting proved constants are $40\,2^{3/4}<68$ and $10\sqrt{30}$. The complete paper proofs are in `paper_work/rank_two.tex`; a self-contained derivation of the refinements follows.

Throughout, the original coordinates of $X$ are independent and have Lebesgue densities at most one. An arbitrary original-coordinate affine term is allowed unless a smaller class is stated explicitly. Orthogonal rotations below act on the spectral frame; they do not assert independence of rotated random coordinates.

## 1. Inputs from the Fourier and projection arguments

We use two independently proved analytic facts, with full proofs or precise primary references in the accompanying Fourier chapter.

1. If $U^TU=I_r$, each row has squared length at most $1/2$, and $\Lambda$ is invertible symmetric, then, even after adding arbitrary separable coordinate phases,

   \[
   |\phi(t)|\leq\min\{1,e^{r/2}\pi^{r/2}|\det\Lambda|^{-1/2}|t|^{-r/2}\}.
   \]

2. Every unit linear form in independent cap-one variables has density at most $\sqrt2$. More generally an $r$-dimensional orthogonal projection has density at most $2^{r/2}$, by Livshyts–Paouris–Pivovarov (2016).

These are used for diffuse frames and for unconditional linear projections only. No conditional projection-density bound is assumed.

## 2. Rank-one small balls with arbitrary affine terms

For a unit vector $u$, nonzero $\lambda$, and arbitrary $b,d$, let
\[
R=\lambda\langle u,X\rangle^2+b^TX+d.
\]
Then for every $w\in\mathbb R$ and $\rho>0$,
\[
\mathbb P(|R-w|<\rho)\leq\min\{1,8\sqrt{\rho/|\lambda|}\}.
\]

If some $u_i^2\geq1/2$, condition on the remaining original coordinates. A one-variable quadratic of leading coefficient $a$ has inverse image of an interval of length $2\rho$ of total length at most $2\sqrt{2\rho/|a|}$. Here $|a|\geq|\lambda|/2$, giving constant 4.

Otherwise the diffuse estimate gives $|\phi_R(t)|\leq\sqrt{e\pi}|\lambda t|^{-1/2}$. Gaussian smoothing yields, for every $v>0$,
\[
\begin{aligned}
\mathbb P(|R-w|<\rho)
&\leq\frac{e^v\rho}{2\sqrt{\pi v}}
\int_{\mathbb R}e^{-\rho^2t^2/(4v)}|\phi_R(t)|\,dt\\
&\leq\frac{e^v\sqrt e\,\Gamma(1/4)}{\sqrt2v^{1/4}}
\sqrt{\rho/|\lambda|}.
\end{aligned}
\]
Taking $v=1/4$ gives $e^{3/4}\Gamma(1/4)<8$. A purely elementary upper certificate is
\[
\Gamma(1/4)\leq4-\frac45+\frac29-\frac2{39}+\frac1{102}+e^{-1}.
\]
It follows by integrating the degree-four Taylor upper bound for $e^{-x}$ over $[0,1]$ against $x^{-3/4}$, and bounding the tail by $e^{-1}$. Using $e^{-1}<3/8$ and $e^{3/4}<17/8$ proves the strict bound 8.

## 3. The scalar kernel and its average

Define the even function
\[
\Psi(a)=\begin{cases}1+\log(1/|a|),&0<|a|\leq1,\\
|a|^{-1/4},&|a|\geq1,\\+\infty,&a=0.
\end{cases}
\]
For every density $f\leq K$,
\[
\int f(x)|a-x^2|^{-1/2}\,dx\leq5K\Psi(K^2a).
\tag{1}
\]

It suffices to prove $K=1$. For $a>0$, if $m_a(s)$ is the measure of the level set $|a-x^2|^{-1/2}>s$, then
\[
m_a(s)\leq\begin{cases}2\sqrt2/s,&s^{-2}\geq a,\\
4/(\sqrt a\,s^2),&s^{-2}<a.
\end{cases}
\]
Layer cake bounds the integral by $\int_0^\infty\min(1,m_a(s))\,ds$. For $0<a\leq1$, splitting at 1 and $a^{-1/2}$ gives $5+\sqrt2\log(1/a)\leq5\Psi(a)$. For $a\geq1$, split at $2a^{-1/4}$ to get $4a^{-1/4}$. If $a<0$, then $m_a(s)\leq2/s$, and $m_a(s)=0$ for $s\geq|a|^{-1/2}$. This gives $1+\log(1/|a|)$ for $|a|\leq1$; for $|a|\geq1$, the kernel is at most $|a|^{-1/2}\leq|a|^{-1/4}$. Rescaling proves (1).

If a real random variable $W$ satisfies
\[
\mathbb P(|W|<\rho)\leq L\sqrt\rho\qquad(\rho>0),
\]
then
\[
\mathbb E\Psi(W)\leq4\sqrt L.
\tag{2}
\]
Indeed, for $0<s<1$, the level probability is at most $Ls^{-2}$. For $s\geq1$, it is at most $Le^{(1-s)/2}\leq4L/s^2$, because $\sup_{s\geq1}s^2e^{(1-s)/2}=16e^{-3/2}<4$. Integrating $\min(1,4L/s^2)$ proves (2).

## 4. Arbitrary-affine rank-two half-power potential

Let $U^TU=I_2$, let $\Lambda$ be invertible symmetric, let $D=|\det\Lambda|$, and set
\[
R=(U^TX)^T\Lambda(U^TX)+b^TX+c.
\]
Then
\[
\boxed{\sup_w\mathbb E|R-w|^{-1/2}\leq40\,2^{3/4}D^{-1/4}<68D^{-1/4}.}
\tag{3}
\]

For diffuse frames, $|\phi_R(t)|\leq\min(1,K/|t|)$, where $K=e\pi D^{-1/2}$. The Gaussian representation of $|z|^{-1/2}$, followed by Gaussian Fourier inversion and Tonelli after taking absolute values, gives
\[
\mathbb E|R-w|^{-1/2}\leq(2\pi)^{-1/2}
\int_{\mathbb R}|t|^{-1/2}|\phi_R(t)|\,dt
\leq4\sqrt{2e}\,D^{-1/4}.
\]
The last integral splits at $|t|=K$; both pieces together equal $8\sqrt K$ before the factor $(2\pi)^{-1/2}$.

Otherwise choose an original coordinate of leverage $h>1/2$. Rotate the spectral frame so that
\[
Y_1=\sqrt h X_i+T,\qquad Y_2=Z,\qquad
\Lambda=\begin{pmatrix}\beta&\gamma\\\gamma&\delta\end{pmatrix},
\]
where $T,Z$ depend only on the remaining original coordinates and $Z$ is a unit linear form in those coordinates. Write $k=h^{-1/2}$, $d=b_i/\sqrt h$, and absorb the remaining affine terms into $L_0$. Then
\[
R=\beta Y_1^2+2\gamma Y_1Z+\delta Z^2+dY_1+L_0.
\]
Conditionally on the remaining original coordinates, $Y_1$ has density at most $k$.

For $\beta\ne0$, completing the square gives
\[
R=\beta\left(Y_1+\frac{\gamma Z}{\beta}+\frac d{2\beta}\right)^2+R_0,
\quad
R_0=\frac{\det\Lambda}{\beta}Z^2-\frac{\gamma d}{\beta}Z-\frac{d^2}{4\beta}+L_0.
\]
The remainder is a rank-one quadratic plus an arbitrary affine term in the remaining independent original coordinates. By (1), the conditional potential is at most
\[
5k|\beta|^{-1/2}\Psi(W),\qquad W=k^2(w-R_0)/\beta.
\]
The magnitude of the rank-one coefficient of $W$ is $\lambda_0=k^2D/\beta^2$. Section 2 and (2) give
\[
\mathbb E|R-w|^{-1/2}
\leq20\sqrt8\,k|\beta|^{-1/2}\lambda_0^{-1/4}
=20\sqrt8\sqrt k\,D^{-1/4}
\leq40\,2^{3/4}D^{-1/4}.
\]

For $\beta=0$, $D=\gamma^2>0$. The conditional polynomial is affine in $X_i$, with slope $\sqrt h(2\gamma Z+d)$. The elementary cap-$H$ bound
\[
\int f(x)|x-a|^{-1/2}\,dx\leq2\sqrt{2H}
\]
follows directly from layer cake. Apply it first to $X_i$, then to $Z$, whose density is at most $\sqrt2$. This yields
\[
4\,2^{3/4}h^{-1/4}D^{-1/4}\leq8D^{-1/4}.
\]
The single exceptional zero slope has probability zero. This finishes all cases of (3).

## 5. Affine terms in the quadratic range

If $b\in\operatorname{range}(U)$, then
\[
\boxed{\sup_w\mathbb E|R-w|^{-1/2}\leq10\sqrt{30}\,D^{-1/4}.}
\tag{4}
\]

Here is a conditional two-coordinate estimate used to prove (4). Suppose $Z$ has density at most $H$, and $S\mid Z$ has density at most $K$. For invertible symmetric $L$ and deterministic affine terms,
\[
\sup_w\mathbb E|(S,Z)L(S,Z)^T+\text{affine}-w|^{-1/2}
\leq10\sqrt{15}\sqrt{KH}\,|\det L|^{-1/4}.
\tag{5}
\]
Translate the deterministic affine term away. If $L_{11}=a\ne0$, condition on $Z$ and use (1). The remaining integrand has the form
\[
5K|a|^{-1/2}\Psi(A\pm\delta_0Z^2),\qquad
\delta_0=K^2|\det L|/a^2.
\]
The elementary sublevel length bound $|\{z:|z^2+A|<\rho\}|\leq4\sqrt\rho$ gives
\[
\|\Psi(A\pm\delta_0z^2)\|_{L^{2,\infty}(dz)}^2
\leq15\delta_0^{-1/2}.
\]
For levels below one the squared weak-norm estimate is at most $4\delta_0^{-1/2}$; for larger levels it is at most $64e^{-3/2}\delta_0^{-1/2}<15\delta_0^{-1/2}$. Integrating a weak-$L^2$ function against a cap-$H$ probability density gives at most $2\sqrt H$ times its weak norm. Substituting cancels $a$ and proves (5). If $a=0$, two applications of the affine negative-half estimate give the smaller constant $4\sqrt2\sqrt{KH}|\det L|^{-1/4}$.

To obtain (4), translate the original coordinates to remove $b\in\operatorname{range}(U)$. The diffuse case is already smaller. In the heavy case of Section 4, $Z$ has density at most $\sqrt2$, and $Y_1\mid Z$ has density at most $h^{-1/2}$. The latter statement follows by averaging the cap given all remaining original coordinates; it is not an assertion about arbitrary conditional projections. Formula (5) now gives
\[
10\sqrt{15}(2/h)^{1/4}D^{-1/4}\leq10\sqrt{30}D^{-1/4}.
\]

## 6. Two consequences recorded in the paper

**Exact rank-two concentration.** If $A=UMU^T$, $U^TU=I_2$, and $|\det M|\geq1$, then, with arbitrary original-coordinate affine terms and $0<a\leq1$,
\[
\sup_s\mathbb P(|Q_A-s|\leq a)
\leq32\sqrt2\,a(1+\log(1/a))\leq46a(1+\log(1/a)).
\]
The diffuse Fourier argument gives the smaller constant 28. In the heavy case, choose leverage $l>1/2$ and write $Q_A=ax_i^2+2Lx_i+T$. The discriminant $\Delta=L^2+a(s-T)$ has quadratic matrix $-l\det(M)r_1r_1^T$, with $r_1$ a unit vector in the remaining original coordinates. Section 2 gives $\mathbb P(|\Delta|<u)\leq8\sqrt2\sqrt u$. The conditional sublevel probability is at most $\min(1,4a_s/\sqrt{|\Delta|})$, including the case of zero quadratic coefficient. Layer cake therefore gives $\int_0^1\min(1,32\sqrt2a_s/\theta)\,d\theta$, proving the assertion. The full proof appears under `thm:rank-two-affine` in `structure.tex`.

**Exact rank-three Schur pivot.** Suppose an original-coordinate principal block has representation $A_{II}=VMV^T$, $V^TV=I_3$, with $M$ invertible. For $i\in I$, let $a=A_{ii}\ne0$ and $h=|V^Te_i|^2$. Then, even with arbitrary ambient blocks, couplings, and affine terms,
\[
\|p_Q\|_\infty\leq68(h|a||\det M|)^{-1/4}.
\]
Condition outside $I$, then complete the square in $X_i$. If $v=V^Te_i$ and $T$ is an orthonormal frame for $v^\perp$, the remaining Schur matrix is $WNW^T$, where $W=V_{-i}T$, $W^TW=I_2$, and $\det N=h\det M/a$. The scalar square-density kernel contributes $|a|^{-1/2}$, and (3) supplies the rest. For a full exact-rank-three matrix with all three eigenvalue moduli at least one, $|\det M|\geq\|M\|$ and $|a|\leq h\|M\|$, giving $\|p_Q\|_\infty\leq68/\sqrt{|a|}$. This is a pivot-dependent estimate, with no claim of uniformity as $a\to0$.

## 7. Verification and scope

The rank-one Gaussian normalization, the rational upper bound for its constant, and the discriminant improvement were independently checked during assembly. An independent second derivation also checked the kernel constant 5, the kernel-average bound, the cancellation giving the arbitrary-affine constant below 68, the zero-quadratic-coefficient case, and the conditional and range constants. Further mathematical and prior-art review remains appropriate; this record is an internal consistency check, not a claim of external validation. Constants are intentionally rounded upward in the paper where doing so improves readability. The difficult unrestricted rough-input endpoint, the small-leak uniformity problem, and the missing exhaustive quantitative structural reduction are unaffected by these constant improvements.
