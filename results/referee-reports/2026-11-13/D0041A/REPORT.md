PARTIAL

The problem is the critically spiked **soft edge at beta = 1**. It concerns M. Y. Mo, *Rank 1 real Wishart spiked model*, Communications on Pure and Applied Mathematics 65 (2012), 1528–1638, [arXiv:1101.5144](https://arxiv.org/abs/1101.5144), **Theorem 2.4, PDF p.12**, with the definitions on pp.11–12 and the auxiliary derivation on pp.88–93. It is not a theorem of Mo for all even beta.

I did not find a printed verification of this formula against the Bloemendal–Virág PDE. This search does not establish that none exists. I have not completed that verification or independently evaluated Mo's finite-spike beta=1 contour formula numerically. The results below are a precise identification, proofs of several reductions and source inconsistencies, a complete known beta=2 verification as a control, exact beta=4 residual algebra, and numerical PDE evidence. The remaining determinant identity and analytic estimates are stated explicitly.

All page references below are **PDF pages of the retained text versions**, unless otherwise specified. Journal page numbers have not been inferred from arXiv pagination. Sources are retained only as text in `sources/`; code and numerical results are in `code/` and `data/`.

## 1. Statement and literature result

Virág's [*Operator limits of random matrices*](https://arxiv.org/abs/1804.06953) is dated May 25, 2014 and was posted to arXiv in 2018. Problem 3 on PDF p.12 says:

> Find a way to check that Mo’s formulas satisfy (10).

The preceding sentence explicitly specifies beta=1. Reference [34], p.27, identifies the Mo paper above. The beta=2 and beta=4 formulas discussed immediately before the problem are the already understood comparisons.

The equation, on PDF p.9, is

\[
\boxed{L_\beta F:=F_t+\frac{2}{\beta}F_{ww}+(t-w^2)F_w=0,
       \qquad (t,w)\in\mathbb R^2.}\tag{10}
\]

The boundary conditions are

\[
 F(t,w)\longrightarrow1\quad\text{as }t,w\longrightarrow+\infty
 \text{ together},\tag{BC+}
\]
\[
 F(t,w)\longrightarrow0\quad\text{as }w\longrightarrow-\infty,
 \quad t\text{ bounded above}.\tag{BC-}
\]

The second limit is uniform over every half-plane (t\leq t_0). The first means every sequence with both coordinates tending to positive infinity. These conditions, together with boundedness and classical solvability on the plane, are essential; merely checking a differential equation at finite points is insufficient.

[Bloemendal–Virág I](https://arxiv.org/abs/1011.1877), **Theorem 1.7(i)–(ii), pp.9–10**, characterizes the unique bounded solution as

\[
 F_\beta(t,w)=\mathbb P_{t,w}\{p_s\text{ never explodes to }-\infty\},
 \qquad dp_s=(s-p_s^2)\,ds+\frac2{\sqrt\beta}\,dB_s.
\]

Equivalently it is the CDF of the negative lowest eigenvalue of

\[
 \mathcal H_{\beta,w}=-\frac{d^2}{dx^2}+x+\frac2{\sqrt\beta}B'_x,
 \quad f'(0)=wf(0).
\]

The unspiked Tracy–Widom CDF is (F_\beta(t,+\infty)). At finite (w), this is a one-spike deformation. The spike variable (w) cannot be discarded.

The sentence following Problem 3 is about **Rumanov's hard-edge Painlevé III construction**, reference [42], arXiv:1212.5333. It is a separate equation. Virág's Question 9, PDF p.25, asks for a derivation of the bulk gap Painlevé equation from Brownian-carousel generator PDEs. Neither adjacent statement changes the target of Problem 3.

The literature search covered the requested authors and exact-title searches, followed by searches combining Mo's title/name, Bloemendal–Virág, PDE, verification, and publication years through 2026. The useful findings were:

| Primary source retained | Exact location read | Relevance to D0041 |
|---|---|---|
| [Bloemendal–Virág I](https://arxiv.org/abs/1011.1877) | Thm.1.1 p.7; Thm.1.7 pp.9–10, proof p.27; Thm.1.9 p.11, proof pp.29–30 | Soft-edge limit and PDE; direct Painlevé checks at beta=2,4. The paragraph on p.11 explicitly leaves reconciliation with Mo's beta=1 formula as a question. |
| [Bloemendal–Virág II](https://arxiv.org/abs/1109.3704) | Thms.1.5–1.6 pp.8–9; Section 6 pp.43–45 | Higher-rank diffusion/PDE, beta=2 Painlevé connection; no Mo beta=1 verification found. |
| [Mo](https://arxiv.org/abs/1101.5144) | Thm.1.2 p.5; Thm.2.4 pp.11–12; Prop.7.1 p.93 | The actual target. His p.5 already explains the interest in converting the two representations. |
| [Ramírez–Rider–Virág](https://arxiv.org/abs/math/0607331) | Thms.1.1–1.2 pp.3–4 | Stochastic Airy spectrum and diffusion, not the missing formula manipulation. |
| [Ramírez–Rider](https://arxiv.org/abs/0803.2043) | Thms.1–2 p.4 | Stochastic Bessel/hard-edge operator and diffusion. |
| [Rumanov, hard edge](https://arxiv.org/abs/1212.5333) | Eq.(2.2) p.5; Thm.1 pp.5–6, Thm.2 pp.6–7 | Painlevé III Lax constructions for beta=2,4; not soft-edge beta=1. |
| [Rumanov, classical integrability](https://arxiv.org/abs/1306.2117) | Section 3 pp.9–13; Section 4 pp.13–16 | Even-beta Lax construction; does not cover beta=1 by simply setting beta=1. |
| [Rumanov, beta=6](https://arxiv.org/abs/1408.3779) | Eq.(1.1) p.2 and the beta=6 auxiliary system | A different beta value and representation. |
| [Grava–Its–Kapaev–Mezzadri](https://arxiv.org/abs/1607.01351) | Thm.7.1 p.18; Prop.7.2 p.21; discussion pp.23–24 | Rigorous steps and remaining auxiliary issues for Rumanov's beta=6 representation. |
| [Yuqi Li](https://arxiv.org/abs/1812.00522) | Thms.1.2–1.3 pp.4–5 | Selects the bounded beta=6 solution; Thm.1.3 fixes its two constants. This is not a theorem about Mo or beta=1. |
| [Forrester, spiked Wishart](https://arxiv.org/abs/1101.2261) | Introduction pp.1–3; Prop.2.1 p.5; beta=4 discussion | General-beta finite-matrix construction and beta=4 formulas; distinguishes Mo and BV approaches. |
| [Forrester–Witte](https://arxiv.org/abs/1210.3381) | Soft-edge/Painlevé review | Context for classical beta=1,2,4 formulas, not an explicit resolution found here. |
| [Forrester, rank-one review](https://arxiv.org/abs/2201.00324) | **Remark 2.9 p.15**; Prop.2.11 pp.17–18; Prop.3.12 p.31 | Especially relevant: Remark 2.9 says Mo's expression had not been used for further analysis or numerical values. The review separates beta=2,4 verification, even-beta6 work, and hard-edge equations. |
| [Dumaz–Virág](https://arxiv.org/abs/1102.4818) | Thm.1 p.3 | Unspiked right-tail asymptotics; not a finite-spike Mo check. |
| [Wang](https://arxiv.org/abs/0711.2722) | Thm.1 pp.7–8 | Rank-one **quaternionic soft edge**, beta=4, including the critical GOE law. This must not be mislabeled a beta=1 spiked formula. |
| [Ramírez–Rider, spiking the hard edge](https://arxiv.org/abs/1506.04988) | Thm.3 pp.6–7; Thm.6 p.9 | Spiked hard-edge PDE and hard-to-soft transition. The requested Wang/hard-edge search led to distinguishing this work from Wang's soft-edge theorem. |
| [Liechty–Nguyen–Remenik](https://arxiv.org/abs/2009.07781), published 2022 | pp.10–11; Corollary 2 p.11 | Explicitly distinguishes their GOE deformation from beta=1 spiked TW. Their related one-spike BV PDE result has beta=4. |
| [Trogdon–Zhang](https://arxiv.org/abs/2304.04951), SIGMA 2024 | Section 2 pp.3–5, especially (2.3)–(2.4) | Numerical algorithms for BV, used as a method reference, not a formula verification. |
| [Forrester–Rahman–Shen](https://arxiv.org/abs/2611.10990), posted Nov.7, 2026 | Abstract and hard-edge review/results | Recent hard-edge expansions; no direct Mo soft-edge beta=1 check located. |

The 2022 review is evidence against mistaking earlier even-beta work for a resolution. It is not evidence that settles every publication through November 2026. No theorem/page supporting `RESOLVED_IN_LITERATURE` was found.

## 2. Mo's formula in the PDE variables

Use (t=\zeta) for Mo's edge threshold and retain his (w). To avoid confusion with his contour variable, call that variable (T). For the square-aspect limit,

\[
 t=(z-4)(N/4)^{2/3},\qquad
 w=(N/4)^{1/3}(1-\tau),\qquad \ell=1+\tau.
\]

These are the BV variables without an additional beta=1 rescaling. Indeed, in BV I Thm.1.1 set (p=N,n=M,\ell=1+\tau). For (M=N+1),

\[
 m_{M,N}=(M^{-1/2}+N^{-1/2})^{-2/3}\sim(N/4)^{1/3},
\]

and the centered spectral variable is asymptotic to Mo's (t). Taking (M=N+1) avoids an unnecessary issue with the rate of convergence of the aspect ratio. The bare condition (M/N\to1) alone does not justify replacing the moving edge by 4 at the (N^{-2/3}) scale.

Write (q(t)) for the positive Hastings–McLeod solution,

\[
 q''=tq+2q^3,\quad q(t)\sim\operatorname{Ai}(t)\ (t\to+\infty),
 \quad v(t)=\int_t^\infty q(s)^2\,ds,
\]
\[
 \mathcal F(t)=\exp\!\left[-\int_t^\infty(s-t)q(s)^2\,ds\right],
 \qquad E(t)=\exp\!\left[-\int_t^\infty q(s)\,ds\right].
\]

Thus (\mathcal F=TW_2), (\mathcal F'/\mathcal F=v), and (E'/E=q). Mo's limiting expression has the form

\[
 M(t,w)=C(w)\,\mathcal F(t)^{1/2}
 \operatorname{Im}\int_{\Xi_+}
 e^{-wT/2-\mathcal S(T)/2}\,I_0(T)^{1/2}
 D(t,T)^{1/2}\,dT,\tag{M}
\]
\[
 I_j(T)=\int_{-\infty}^{\infty}
 \frac{\operatorname{Ai}^{(j)}(u)}{(T-u)^{1/2}}\,du,
 \quad \psi=(T-t)^{1/2}.
\]

The branches, upper/lower boundary values and contour are part of the formula. Mo defines (\mathcal S) in (2.14), p.11; it depends only on (T), not on (t,w). It is retained verbatim in the source text. (D) is his three-by-three determinant. Using the body equations (7.22)–(7.23), pp.89–90, it is

\[
 D=\det\begin{pmatrix}
 1-R_-/2&-a_{21}&-a_{31}\\
 -P_{-,0}/2&1-a_{22}&-a_{32}\\
 -P_{-,1}/2&-a_{23}&1-a_{33}
 \end{pmatrix},
\]
\[
\begin{aligned}
 a_{21}&=TQ_0/2-\mathcal B_1Q_1-Q_2-\mathcal B_2\widetilde R_-,\\
 a_{31}&=Q_1/2+\mathcal B_1Q_0,\\
 a_{2j}&=Tu_{-,0,j-2}/2-\mathcal B_1u_{-,1,j-1}
             -u_{-,2,j-2}-\mathcal B_2\widetilde P_{-,j-2},\\
 a_{3j}&=u_{-,1,j-2}/2+\mathcal B_1u_{-,0,j-2},\quad j=2,3,\\
 \mathcal B_1&=-(I_1+1)/(2I_0),\\
 \mathcal B_2&=-\mathcal B_1/2-TI_0/4+\mathcal B_1I_1/2+I_2/2.
\end{aligned}\tag{D}
\]

Here (Q_j=q_{-,j}-q_{-,j}^{(\infty)}). The source's index conventions are reproduced, not silently reconciled. Proposition 7.1, p.93, relates these quantities to five vectors (V_j=(v_{j1},\ldots,v_{j4})^T), (j=0,\ldots,4), through

\[
 \partial_t V_j=UV_j+h_j,\qquad
 U=\begin{pmatrix}
 0&0&0&-\psi q\\
 0&0&q/\psi&-q/\psi\\
 0&-v/(q\psi)&q'/q+1/(2\psi^2)&0\\
 -q/\psi&0&1/(2\psi^2)&0
 \end{pmatrix},\tag{U, as printed}
\]

with (h_j=(0,0,0,\phi_j/\psi)^T) for (j=0,1,2), zero otherwise. The endpoint data are

\[
 V_j\sim(0,0,0,I_j)^T\ (t\to+\infty),\ j=0,1,2;
 \quad V_3\sim(0,0,-1,0)^T\ (t\to-\infty),
 \quad V_4\sim(0,0,-1,0)^T\ (t\to+\infty).
\]

The expressions include (Q_j=v_{j4}-v_{j3}-I_j), (R_-=v_{34}-v_{33}+1), (P_{-,0}=v_{32}), and Wronskians involving (v_{j3}) and (\phi_k/\psi). See the following source audit before using these equations as a numerical specification.

Direct substitution is difficult because (w)-derivatives become moments of a complex contour integral, (t)-derivatives act on a square-root determinant built from mixed-endpoint ODE solutions, and integration by parts in (T) requires compatible parameter derivatives and control of all branches/endpoints. Painlevé II for (q) alone supplies none of those missing (T)-identities.

### Source audit: three actual inconsistencies

These observations concern the retrieved arXiv version; the journal typography was not independently checked.

1. The definition before (2.15), p.11, has (\phi_1=q'+vq'), whereas body **(7.34), p.93**, gives (\phi_1=q'+vq). Both the extracted PDF text and the downloaded LaTeX text contain this difference.
2. Theorem 2.4, p.12, labels two different entries ( (\alpha_1,\beta_1)). Body (7.22) makes clear which position the third entry occupies. The introductory definition of (Q_j) also omits (j=0), although the matrix uses it.
3. There is a load-bearing sign inconsistency: **(7.32)–(7.33), p.92**, imply (W(q/\psi,\phi_1/\psi)=+v/\psi^2), with the stated convention (W(f,g)=fg'-gf'). But (7.34) and Painlevé II imply the negative sign. The proof follows below.

These issues prevent an unqualified implementation by copying pp.11–12. They do not establish a counterexample to the intended probabilistic formula. In particular, changing only one sign in (U) without auditing its definitions would be unjustified.

## 3. Proofs and reductions

### 3.1 Uniqueness from the diffusion characterization

Assume the path dichotomy of BV I Thm.1.7(i): a path either explodes in finite time to negative infinity or survives with (p_s\sim\sqrt{s}). Let (H) be a bounded classical solution of (10), (BC+), (BC-). Until explosion, Itô's formula gives

\[
 dH(s,p_s)=\frac2{\sqrt\beta}H_w(s,p_s)\,dB_s.
\]

Localize also on bounded spatial intervals to justify the stochastic integral. Since (H) is bounded, the resulting local martingale is a true martingale up to each stopping time under consideration. Stop at (\sigma_n=n\wedge\inf\{s\ge t:p_s=-n\}), and remove the upper spatial localization. There is no finite positive explosion for this diffusion. Therefore

\[
 H(t,w)=\mathbb E_{t,w}H(\sigma_n,p_{\sigma_n}).
\]

On a path exploding at finite time, (\sigma_n) tends to that time and its spatial coordinate tends to negative infinity, so (BC-) makes the integrand tend to zero. On a surviving path, (\sigma_n=n) eventually and (p_n\sim\sqrt n), so (BC+) makes it tend to one. Bounded convergence identifies (H) with the non-explosion probability. This proves uniqueness. Existence and smoothness are supplied by BV I Thm.1.7; the argument here does not purport to reprove the diffusion dichotomy.

### 3.2 Painlevé identities and the Wronskian sign

Set (p=q'). Differentiation gives

\[
 \frac d{dt}(p^2-tq^2-q^4)=-q^2.
\]

The Airy asymptotics make the expression vanish at positive infinity, whence

\[
 \boxed{v=p^2-tq^2-q^4.}\tag{H}
\]

Using the body definition (\phi_1=p+vq) and (v'=-q^2),

\[
 \phi_1'=tq+q^3+vp,
\]
\[
 W(q,\phi_1)=q(tq+q^3+vp)-p(p+vq)
            =tq^2+q^4-p^2=-v.
\]

Multiplying both arguments of a Wronskian by the same factor (1/\psi) multiplies it by (1/\psi^2), since the derivatives of that factor cancel. Consequently

\[
 \boxed{W(q/\psi,\phi_1/\psi)=-v/\psi^2,}\tag{W}
\]

which proves the sign inconsistency identified above. Since (q>0), (v>0) on the real axis, the two signs are genuinely distinct.

A further quadrature in Mo's coefficients can be eliminated exactly:

\[
 \int_t^\infty q\phi_1
 =\int_t^\infty(qq'+vq^2)=-q(t)^2/2+v(t)^2/2.
\]

Thus the body definition of (\phi_2) becomes

\[
 \boxed{\phi_2=tq-vp-\tfrac12(v^2+q^2)q.}\tag{P2}
\]

The integrations use (q,v\to0) at positive infinity; no asymptotic interchange is involved. These are exact identities, also checked symbolically in `code/symbolic_checks.py`.

### 3.3 The spike normalization must be tracked

Mo's statement writes “some constant (C)” for a fixed spike. One cannot assume that this is independent of (w) when differentiating in (w). Here is a finite-dimensional calculation of the surviving spike factor, using the convention that all the remaining kernel factors in (M) are independent of (w).

Let (k=N/2) and (a=M\tau/[2(1+\tau)]>0). A uniform unit vector has squared coordinates with Dirichlet parameters (1/2,\ldots,1/2). Its exponential average is

\[
 H_a(\lambda)=\frac{\Gamma(k)a^{1-k}}{2\pi i}
  \int_\Gamma e^{az}\prod_{j=1}^N(z-\lambda_j)^{-1/2}\,dz.
\]

To prove the formula, expand the exponential and use the Dirichlet moments
(\mathbb E\prod r_j^{m_j}=\prod(1/2)_{m_j}/(k)_{\sum m_j}).
The inverse Laplace integral of (\prod(z-\lambda_j)^{-1/2}) has exactly these coefficients after multiplication by (\Gamma(k)a^{1-k}). Equality first holds in a convergent expansion and then by analytic continuation to (a>0). This is also the rank-one contour mechanism underlying Mo's finite-(N) formula.

The Gaussian likelihood ratio relative to the identity covariance contributes ( (1+\tau)^{-M/2}H_a). Its scalar spike dependence outside the spectral integral is therefore

\[
 \tau^{1-N/2}(1+\tau)^{(N-M)/2-1}
\]

up to a factor independent of (\tau). At the contour edge (z=4), include also (e^{4a}). For (M=N+1), put (\epsilon=1-\tau=4^{1/3}wN^{-1/3}). The logarithmic ratio to (\tau=1) is

\[
 N\left\{\frac{2(1-\epsilon)}{2-\epsilon}-1
               -\frac12\log(1-\epsilon)\right\}+o(1)
 =N\epsilon^3/24+o(1)\longrightarrow w^3/6.
\]

The omitted terms have bounded coefficients times (\epsilon), and (N\epsilon^4\to0), so the remainder tends to zero for every fixed (w). If (z=4+(4/N)^{2/3}T), the extra exponent relative to (a_0=M/4) satisfies

\[
 (a-a_0)(z-4)\longrightarrow-wT/2.
\]

Thus the spike dependence in this convention is

\[
 \boxed{C(w)=c\,e^{w^3/6},\qquad e^{-wT/2}\text{ inside the transform}.}\tag{N}
\]

This calculation fixes the algebraic factor surviving Mo's critical scaling. It does not prove his contour asymptotics or a branch normalization. A different allocation of factors between (C) and the kernel must give the same total expression. The cubic coefficient was checked a second way by exact Taylor expansion in the symbolic script.

### 3.4 An exact contour-transform reduction

Use a full symmetric contour as in Mo's Proposition 6.14, p.84, rather than differentiating a moving endpoint of the upper half-contour. Locally choose its real crossing at (T_0>t), fixed as (t) varies in a small interval. Put

\[
 K(t,T)=\mathcal F(t)^{1/2}A(T)D(t,T)^{1/2},
 \qquad A(T)=e^{-\mathcal S(T)/2}I_0(T)^{1/2},
\]
\[
 J(t,w)=\int_\Gamma e^{-wT/2}K(t,T)\,dT,
 \qquad M(t,w)=c e^{w^3/6}J(t,w).
\]

The scalar relating this symmetric contour integral to the imaginary part is absorbed in (c).

**Proposition.** Suppose the contour and square roots are consistently defined, differentiation under the integral is valid through the indicated orders, and endpoint limits exist. Then

\[
 \frac{L_1M}{c e^{w^3/6}}
 =\int_\Gamma e^{-wT/2}\mathcal R(t,T)\,dT
       -[\mathcal B(t,T,w)]_{\partial\Gamma},\tag{R}
\]
\[
 \boxed{\mathcal R=K_t+(t-T)\left(2K_{TT}-\frac T2K\right),}\tag{K}
\]
\[
 \mathcal B=2\{e^{-wT/2}\partial_T[(t-T)K]
       -(\partial_T e^{-wT/2})(t-T)K\}+4e^{-wT/2}K.
\]

**Proof.** Conjugation by (e^{w^3/6}) gives

\[
 e^{-w^3/6}L_1(e^{w^3/6}J)
 =J_t+2J_{ww}+(t+w^2)J_w+(2w+tw^2/2)J.
\]

Differentiate the exponential to write the integrand as

\[
 e^{-wT/2}\{K_t+(T^2-tT)K/2+w^2(t-T)K/2+2wK\}.
\]

Use (w^2e^{-wT/2}=4\partial_T^2e^{-wT/2}) twice by parts and (2we^{-wT/2}=-4\partial_Te^{-wT/2}) once. The remaining kernel is

\[
 K_t+(T^2-tT)K/2+2\partial_T^2[(t-T)K]+4K_T.
\]

Expanding the second derivative cancels (4K_T), leaving (K); the endpoint terms are exactly the negative of (\mathcal B). This proves (R).

In particular, **(K)=0 plus vanishing endpoint terms is a sufficient local check of the PDE.** It is not proved here for Mo's determinant. If (C) were instead a genuinely (w)-independent constant, the corresponding kernel would be

\[
 K_t+2\partial_T^2(TK)+(T^2-tT)K/2.
\]

Confusing these two normalizations changes the proposed identity.

For an explicit finite algebraic target, assume temporarily (A,D\ne0), and set (a=A'/A). Since (\mathcal F'/\mathcal F=v), (K)=0 is equivalent to

\[
\boxed{\begin{aligned}
 P={}&DD_t+vD^2\\
 &+(t-T)\{[4(a'+a^2)-T]D^2+4aDD_T
                   +2DD_{TT}-D_T^2\}=0.
\end{aligned}}\tag{P}
\]

Indeed, (K_t/K=v/2+D_t/(2D)) and

\[
 K_{TT}/K=a'+a^2+aD_T/D+D_{TT}/(2D)-D_T^2/(4D^2).
\]

Substitution and multiplication by (2D^2) give (P). It is a polynomial in (D,D_t,D_T,D_{TT},a,a',v,t,T), so division by (D) can be removed. Branch/analytic continuation issues still need separate attention. This equivalence and the exact endpoint concomitant were verified symbolically.

What remains is substantive: establish (P) for the correctly reconciled Mo data, establish the needed (T)-parameter identities and contour estimates, and prove (BC+), (BC-) and boundedness directly from (M). I have not reduced these to a list of identities all of which are proved. The proposition is a proved **conditional reduction**, not a completion of D0041.

### 3.5 A complete beta=2 control verification

This is the known result of BV I Thm.1.9, not a beta=1 solution. Let (y=(f,g)^T) solve

\[
 y_w=\begin{pmatrix}q^2&-wq-p\\-wq+p&w^2-t-q^2\end{pmatrix}y,
 \qquad
 y_t=\begin{pmatrix}0&q\\q&-w\end{pmatrix}y,
 \qquad f(t,0)=g(t,0)=E(t).
\]

The compatibility condition is exactly Painlevé II. For (G_2=\mathcal Ff), direct differentiation gives

\[
 \mathcal F^{-1}(G_2)_t=vf+qg,
\]
\[
 \mathcal F^{-1}(G_2)_w=q^2f+(-wq-p)g,
\]
\[
 \mathcal F^{-1}(G_2)_{ww}
 =(q^4+w^2q^2-p^2)f+{-q+(wq+p)(t-w^2)\}g.
\]

Hence (L_2G_2=\mathcal F(v+q^4-p^2+tq^2)f=0) by (H).

For completeness, the boundary argument uses precisely BV I **Facts 5.1–5.2, pp.28–29**: (q>0); (\mathcal F) is a CDF; (f(t,w)\to1) as (t\to\infty) for fixed (w); (f(t,w)\to1) as (w\to\infty) for fixed (t); (f(t,w)\to0) as (w\to-\infty) for fixed (t); (f) is positive sufficiently far to the left for each fixed (w); and (g(t,w)=f(t,-w)e^{w^3/3-tw}). These are established Riemann–Hilbert asymptotic facts, not conclusions from a local polynomial calculation.

For fixed (w), both (f,g) are therefore positive at sufficiently negative (t). Their cooperative (t)-system prevents either component from first reaching zero: at a first zero its derivative is strictly positive, a contradiction. Thus (f_t=qg>0). Its limit at positive infinity implies (0<f\le1), so (G_2) is bounded. For (t\le t_0), (f(t,w)\le f(t_0,w)\to0) as (w\to-\infty), proving (BC-). For (t\ge t_0), (f(t,w)\ge f(t_0,w)\to1) as (w\to+\infty); combine this with (\mathcal F(t)\to1) to get (BC+). Uniqueness from Section 3.1 proves the claimed CDF identification. This is a complete verification given the explicitly cited classical asymptotic facts.

### 3.6 Exact beta=4 control algebra

Put (s=2^{2/3}t,z=2^{1/3}w), and evaluate (q,v,E,\mathcal F,f,g) at (s,z). Define

\[
 A_4=(E^{-1/2}+E^{1/2})/2,\quad
 B_4=(E^{-1/2}-E^{1/2})/2,\quad
 G_4=\mathcal F^{1/2}(A_4f+B_4g).
\]

Since (A_4'=-qB_4/2,B_4'=-qA_4/2), the same two linear matrices yield the exact coefficient identity

\[
 (2\partial_s+\partial_z^2+(s-z^2)\partial_z)G_4
 =\mathcal F^{1/2}(v+q^4-p^2+sq^2)(A_4f+B_4g)=0.
\]

The physical operator (L_4) is (2^{2/3}/2) times this operator. Every coefficient is a polynomial in (s,z,q,p,v,A_4,B_4). `symbolic_checks.py` expands both coefficients and verifies the identity exactly. Thus this is an algebraic proof, not sampled residual evidence. The full boundedness and boundary proof is the existing BV I Thm.1.9 proof, p.30; it is not being claimed as a new result here.

## 4. Computation: evidence and its limits

`code/compare_pde.py` solves the PDE independently of the Painlevé controls. With (\theta=\arctan w), (U(t,\theta)=F(t,\tan\theta)), the equation is

\[
 U_t+\frac2\beta\cos^4\theta\,U_{\theta\theta}
 +\left(t\cos^2\theta-\sin^2\theta
       -\frac4\beta\sin\theta\cos^3\theta\right)U_\theta=0.
\]

It is integrated backward from (t=T_*=12), also tested at 16. The negative endpoint is absorbing. At the positive endpoint the diffusion vanishes and the drift is -1; it is evolved using a one-sided derivative, not assigned the value 1. Initial data on (w<0) use the Gaussian asymptotic

\[
 \Phi\!\left((T_*-w^2)/\sqrt{(4/\beta)(-w)}\right),
\]

and equal 1 on (w\ge0), following Trogdon–Zhang (2.4). Centered generator differences are used where their off-diagonal rates are nonnegative, with upwind rates in the degenerate tails. Time stepping is implicit midpoint/Crank–Nicolson, preceded by four implicit Euler steps. This is a numerical truncation, without a rigorous error bound.

The controls solve the Hastings–McLeod boundary-value problem on [-14,10], integrate the (v,\log E,\log\mathcal F) equations, and solve the Lax equations. A second Painlevé solve on [-12,10] checks sensitivity. Positive-spike Lax evaluation uses a separated boundary-value solve; forward initial-value integration is unstable there. Its first failed evaluation and correction are recorded in `data/numerical_issues.txt`.

The grid has (t=-4,-3.5,\ldots,3) and (w=-3,-2,-1,0,1,2,3,+\infty): 120 points per beta. Comparisons use beta=2,4 at all 120 points and beta=1 only at its 15 **unspiked** points, where the known GOE formula is (\sqrt{\mathcal F E}).

| beta | Independent Painlevé control points | Max absolute discrepancy, 600 intervals | 1200 intervals | 2400 intervals |
|---:|---:|---:|---:|---:|
| 1 | 15, (w=+\infty) only | 1.211e-4 | 4.845e-5 | 1.925e-5 |
| 2 | 120 | 2.458e-4 | 9.959e-5 | 4.020e-5 |
| 4 | 120 | 5.007e-4 | 2.024e-4 | 8.284e-5 |

The time steps were respectively .004, .002 and .001. Increasing (T_*) from 12 to 16 at the finest grid changed sampled values by at most 1.36e-12. That small number is **not** a total error estimate: spatial differences are much larger. The two Painlevé solves differed by at most 2.69e-12 on the relevant compact interval; the Hamiltonian residual was at most 1.28e-12. Changing the positive-spike Lax boundary from 8 to 9, while changing its solver tolerance, changed 42 checked control values by at most 2.18e-13.

The numerical PDE/Lax comparison peaked at about 307 MB resident memory. Runs assert inherited nice=10 and cap BLAS/OpenMP at one thread. Results are in `data/pde_comparison.csv`, `data/numerics_summary.json`, and `data/control_refinement.json`.

An additional beta=1 finite-Wishart experiment is in `code/wishart_evidence.py` and `data/wishart_comparison.csv`. It uses the BV bidiagonal model with (M=N+1), spike (\ell=2-w(4/N)^{1/3}), 2500 coupled samples at each size and each (w=-2,0,2), and the same 15 thresholds. The sizes 256 and 1024 use full tridiagonal matrices. Size 262144 uses the leading 1280 rows; this truncation has not been rigorously bounded. The maximum absolute discrepancies over each sampled grid were 0.246, 0.179 and 0.0199 respectively. The first two sizes show substantial finite-size bias; the last has sampling error and an unbounded truncation error. The CSV reports discrepancies and binomial standard errors explicitly. This experiment compares matrices with the PDE, **not Mo's contour formula**.

The target finite-spike beta=1 PDE values have therefore been computed at 105 finite points, but the requested independent numerical evaluation of Mo's formula has **not** been achieved. There is no claimed Mo-versus-PDE numerical agreement. The beta=2,4 comparisons validate the solver and scaling conventions only.

## 5. What is established and what remains

Established here with proofs: the normalization calculation; the exact contour-transform residual and endpoint term; its determinant-polynomial reduction; the Painlevé Hamiltonian and quadrature identities; the source's Wronskian sign inconsistency; and the stated control algebra. The beta=2 boundary proof explicitly depends on cited classical asymptotic facts. The shared-matrix-limit argument also identifies Mo's intended distribution with the BV distribution, once the cited limit theorems and the intended formula are accepted. That indirect identification was already available when Virág posed his problem and is not counted as its solution.

Outstanding: reconcile the auxiliary formulas consistently with their integral definitions; prove (P) for that determinant or find a different direct check; justify contour deformations, differentiation, and endpoint terms; obtain boundedness and both boundary limits from the formula; and perform an independent, stable finite-spike beta=1 numerical evaluation. No resolving theorem in the searched literature was located, and no counterexample to the intended distribution is claimed.

Reproduction, from this directory at nice >=10:

```
python3 code/symbolic_checks.py
python3 code/compare_pde.py
python3 code/refine_controls.py
python3 code/wishart_evidence.py
```

Task: “Open problem D0041” — 13 November 2026, 10:08 Asia/Tbilisi (workspace prompt timestamp).
