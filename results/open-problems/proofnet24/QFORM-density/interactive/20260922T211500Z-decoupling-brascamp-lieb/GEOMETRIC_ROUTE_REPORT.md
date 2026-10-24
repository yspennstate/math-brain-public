# Real-variable route: conditioning on coordinates, pivots and hubs

Frame: conditioning on ORIGINAL coordinates only (lossless Fubini), exact changes of variables along level curves, Schur complements, and one product-structure estimate for hyperbolas. No Fourier analysis. Independence is all that is used (identical distribution never helps or is needed). Every "PROVED" item has a complete proof below; constants are crude.

## Summary of results

| # | Statement | Status |
|---|---|---|
| L1.4 | **2D hyperbolic lemma.** $W$ with independent coordinates, densities $\le1$, $q=(w-w_0)^TB(w-w_0)+\kappa$, $\det B=-D<0$: $p_q(s)\le D^{-1/2}\big(5.2+\log_+\frac{32}{\Lambda|s-\kappa|}\big)$, $\Lambda=\|B^{-1}\|_{S_1}$. Log coefficient sharp. Fails for general 2D densities with bounded marginals. | PROVED |
| T2.1 | **n = 3**: all three $|\lambda|\ge1$, any signs, any linear terms, any laws (spread sets included): $\|p_Q\|_\infty\le20$. Covers $I-2ee^T$, the example with a degenerate block, $2I-J$ (all $2\times2$ blocks singular), zero diagonal. | PROVED |
| C2.2 | Any $n$: a principal $3\times3$ submatrix with all $|\lambda|\ge\gamma$ gives $\|p_Q\|\le20/\gamma$. | PROVED |
| T3.1 | **Pivot calculus.** If $A$ has a "certified pivot chain" (at most 3 pivots, each a diagonal entry $\ge c$ or a $2\times2$ principal minor $\ge c$ of the current Schur complement; at most 4 coordinates), then $\|p_Q\|\le135c^{-1}\sqrt{6.7+\log(1/c)}$, for every $n$, every other entry, every linear term. | PROVED |
| C3.1(b) | Direct sums: certified levels add. $2(X_1X_2+X_3X_4)$, $2(X_1X_2+X_3X_4+X_5X_6)$, $\lambda X_1^2+2X_2X_3$, diagonal + localized blocks: all bounded. | PROVED |
| T3.2 | **Every fixed dimension:** $\|p_Q\|\le250\,n(8+\log n)$ for all $n\times n$ $A$ with $\ge3$ eigenvalues $|\lambda|\ge1$ (so $\le4.5\cdot10^3$ for $n\le6$). | PROVED |
| P4.1 | Rank-3 forms: $\|p_Q\|\le20/\sigma_{\min}(R_S)^2$ for any invertible $3\times3$ row-submatrix; $\le60(n-2)$ always. | PROVED |
| P4.2 | Rank-3 forms with all leverages $\le1/50$ satisfy the hypothesis of Theorem D (matrix Chernoff). | PROVED given Theorem D |
| T5.1-5.2 | **Reduction/equivalence:** the conjecture is equivalent to its restriction to matrices with **no pivot** (all diagonal entries and all $2\times2$ principal minors $<c$; hence all entries $<\sqrt{2c}$), in three forms: bounded density for 3 large eigenvalues, $\sup_sE[|s-R|^{-1/2};|s-R|\le1]<\infty$ for 2, $\sup_sE\log_+\frac1{|s-R|}<\infty$ for 1. | PROVED |
| P5.3-5.5 | **Hubs** (a coordinate coupled to a spread linear form; invisible to $2\times2$ pivots, seen by off-diagonal blocks with rank one): hub small-ball lemma (zero hub diagonal); one hub + one rank-one direction bounded for ANY hub diagonal (explicit, $\le16.5$ at zero diagonal); two hubs bounded by $\frac12+8\sigma^{-2}$ whatever the rest of the matrix (zero hub block). | PROVED |
| 5.3 | Gluing lemma for the no-pivot regime (hubs + spread part) | OPEN, precisely stated |
| 7 | Numerics: Lemma 1.4 within factor 2 of adversarial sets; n = 3 extremal value $\approx2.55$ (uniform laws); hub examples $\le3.6$. | NUMERICAL |

## Four questions
(a) n = 3 with all $2\times2$ blocks indefinite or degenerate: **solved** (Theorem 2.1). The case is made uniform by two facts: the conditional $\log$ singularity sits at a critical value $\kappa(X_k)$ that is a one-dimensional quadratic in $X_k$ with leading coefficient $\det A/\det B=1/(A^{-1})_{kk}$, of modulus $\ge1$; and the conditional $\log$ profile itself is uniform over product laws (Lemma 1.4). For the example of question (a) one conditions on $(X_2,X_3)$, not on $X_3$.
(b) Small $n$: every fixed $n$ is proved, with $C_n=O(n\log n)$ (Theorem 3.2); $n\le6$ gives an explicit universal constant.
(c) Independent blocks: yes in the sublevel/mixture sense (direct-sum rule), e.g. $2(X_1X_2+X_3X_4)$ is certified. The pointwise form "density $\le C(1+\log_+1/|s-s_0|)$ with ONE centre $s_0$" is **false** in three variables: $Q=2X_1X_2+\varepsilon X_3$ ($X_1,X_2$ uniform on $[-\tfrac12,\tfrac12]$, $X_3$ uniform on $[-L-\tfrac12,-L]\cup[L,L+\tfrac12]$; eigenvalues $\pm1$ plus a linear term) has two log peaks of height $\approx\frac12\log\frac1\varepsilon$ at distance $\approx2\varepsilon L$, and no single $s_0$ serves both once $L\gg\varepsilon^{1/C-1}$. The true statement is a log profile around a RANDOM centre (Section 3.1), which is what composes.
(d) Gluing: Theorem 5.2 says precisely what the Fourier side must prove (the three no-pivot statements, uniform in linear terms). Section 5.2 isolates the one structure that neither pivots nor off-diagonal $e_3$ can see - hubs - with the example $Q=2X_h\langle w,X\rangle+\lambda\langle v,X\rangle^2$ (eigenvalues $\pm1,\lambda$, all off-diagonal blocks of rank $\le2$, no pivots), and proves it bounded by a third tool (projection density bounds applied to hub rows).

## 1. Tools (all PROVED)

Notation. $X=(X_1,\dots,X_n)$ has independent coordinates with densities $f_i\le 1$. $Q(x)=x^TAx+b^Tx+c$. For a random variable $Z$ put
$$\varphi_Z(u)=\sup_s P(|Z-s|\le u),\qquad \alpha_1(Z)=\sup_{u>0}\frac{\varphi_Z(u)}{\sqrt u},\qquad \alpha_2(Z)=\sup_{0<u\le 1}\frac{\varphi_Z(u)}{u(1+\log(1/u))},\qquad \alpha_3(Z)=\|p_Z\|_\infty .$$
For $P\subset[n]$ with $A_{PP}$ invertible, $A/A_{PP}=A_{P^cP^c}-A_{P^cP}A_{PP}^{-1}A_{PP^c}$ is the Schur complement.

**Lemma 1.1 (completing the square; conditioning on original coordinates).** If $A_{PP}$ is invertible then
$Q(x)=(x_P-m(x_{P^c}))^TA_{PP}(x_P-m(x_{P^c}))+\kappa(x_{P^c})$, where $m$ is affine and $\kappa$ is a quadratic polynomial in $x_{P^c}$ whose quadratic part has matrix $A/A_{PP}$. Given $X_{P^c}=y$, $Q$ is a quadratic in $X_P$ (product law, densities $\le1$) with matrix $A_{PP}$ and critical value $\kappa(y)$. If every conditional law has density $\le g(s,y)$ for a.e. $s$, then $p_Q(s)\le E\,g(s,X_{P^c})$ for a.e. $s$ (Fubini: $P(Q\in I)=E\int_I p_{Q|y}\le\int_I E g$). This loses nothing, in contrast with conditioning on eigen-coordinates (F2).

**Lemma 1.2 (one coordinate).** Let $g(x)=a(x-m)^2+\kappa$, $a\neq0$, and $X$ have density $f\le 1$.
(i) The density of $g(X)$ at $y$ is $\frac{f(m+r)+f(m-r)}{2\sqrt{|a||y-\kappa|}}\le |a|^{-1/2}|y-\kappa|^{-1/2}$ on the side $(y-\kappa)/a>0$, $r=\sqrt{(y-\kappa)/a}$, and $0$ on the other side.
(ii) $P(|g(X)-s|\le u)\le\min\{2\sqrt{2u/|a|},\ 4u/\sqrt{|a|\max(|s-\kappa|,u)}\}$. In particular $\alpha_1(g(X))\le 2\sqrt2\,|a|^{-1/2}$.
Proof. (i) is the change of variables $y=g(x)$ on each monotone half-line. (ii) Take $a>0$ and $w=(s-\kappa)/a$. The admissible $z=|x-m|\ge0$ satisfy $z^2\in[w-u/a,\,w+u/a]\cap[0,\infty)$, an interval of length $\le 2u/a$. Since $\sqrt\beta-\sqrt\alpha\le\sqrt{\beta-\alpha}$, the $z$-set has length $\le\sqrt{2u/a}$; if moreover $s-\kappa>u$ then $\sqrt{w+u/a}-\sqrt{w-u/a}\le 2u/\sqrt{a(s-\kappa)}$. The two signs of $x-m$ double these, and $f\le1$. $\square$

**Lemma 1.3 (two coordinates, definite; exact form of K3).** Let $W\in\mathbb R^2$ have ANY density $\rho\le K$, $q(w)=(w-w_0)^TB(w-w_0)+\kappa$, $B$ positive definite with eigen-pairs $(\mu_j,e_j)$, $D=\det B$. For $\delta=s-\kappa>0$,
$$p_q(s)=\frac1{2\sqrt D}\int_0^{2\pi}\rho\Big(w_0+\sqrt{\delta/\mu_1}\cos\theta\,e_1+\sqrt{\delta/\mu_2}\sin\theta\,e_2\Big)d\theta\ \le\ \frac{\pi K}{\sqrt D}.$$
Proof. The map $(\delta,\theta)\mapsto w$ has Jacobian $\frac{1}{2\sqrt{\mu_1\mu_2}}$. $\square$ Consequently $P(|q(W)-s|\le u)\le 2\pi Ku/\sqrt D$.

**Lemma 1.4 (two coordinates, indefinite, product structure) - the key new estimate.** Let $W=(W_1,W_2)$ have independent coordinates with densities $f_1,f_2\le1$, $q(w)=(w-w_0)^TB(w-w_0)+\kappa$ with eigenvalues $\mu_+>0>\mu_-$, $D=|\det B|$, $\Lambda=\mu_+^{-1}+|\mu_-|^{-1}\ (\ge 2D^{-1/2})$. Then for a.e. $s\ne\kappa$
$$p_q(s)\ \le\ D^{-1/2}\Big(5.2+\log_+\frac{32}{\Lambda|s-\kappa|}\Big)\ \le\ D^{-1/2}\Big(5.2+\log_+\frac{16\sqrt D}{|s-\kappa|}\Big),$$
and for all $s$, $u>0$: $P(|q(W)-s|\le u)\le \frac{2u}{\sqrt D}\big(6.2+\log_+\frac{16\sqrt D}{u}\big)$.

Proof. Translate so $w_0=0$ (translates of the $W_i$ still have independent coordinates with densities $\le1$). Let $e_\pm$ be unit eigenvectors, $\delta=s-\kappa>0$ (the case $\delta<0$ is symmetric, exchanging the roles of $e_\pm$). The two branches of $\{q=s\}$ are $w_\epsilon(t)=\epsilon\sqrt{\delta/\mu_+}\cosh t\,e_++\sqrt{\delta/|\mu_-|}\sinh t\,e_-$, $\epsilon=\pm1$, $t\in\mathbb R$, and $(\delta,t)\mapsto w_\epsilon$ is a diffeomorphism of $(0,\infty)\times\mathbb R$ onto $\{q>\kappa,\ \epsilon\langle w,e_+\rangle>0\}$ with Jacobian $\frac{\cosh^2t-\sinh^2t}{2\sqrt{\mu_+|\mu_-|}}=\frac1{2\sqrt D}$. Hence, for a.e. $\delta>0$,
$$p_q(\kappa+\delta)=\frac1{2\sqrt D}\sum_{\epsilon=\pm1}\int_{\mathbb R} f_1(w_{\epsilon,1}(t))f_2(w_{\epsilon,2}(t))\,dt .\tag{1.1}$$
($dt/2\sqrt D$ is the invariant measure $d\ell/|\nabla q|$ on the hyperbola.) Write $w_\epsilon(t)=u e^{t}+v e^{-t}$ with $u=(a+b)/2$, $v=(a-b)/2$, $a=\epsilon\sqrt{\delta/\mu_+}e_+$, $b=\sqrt{\delta/|\mu_-|}e_-$; since $a\perp b$, $|u|=|v|=\rho_0:=\tfrac12\sqrt{\delta\Lambda}$.
Tail $t\ge T$: pick a coordinate $i$ with $|u_i|\ge\rho_0/\sqrt2$. For $e^{2t}\ge2\sqrt2$ (i.e. $t\ge T_1=\tfrac34\log2$) we have $|v_i|e^{-t}\le\sqrt2|u_i|e^{-t}\le\tfrac12|u_i|e^{t}$, so $w_i'(t)=u_ie^t-v_ie^{-t}$ has constant sign, $|w_i'|\ge\tfrac12|u_i|e^t$, and $\tfrac12|u_i|e^t\le|w_i(t)|\le\tfrac32|u_i|e^t$; thus $|w_i'|\ge|w_i|/3$ and $w_i$ is monotone on $[T,\infty)$. Bounding $f_1f_2\le f_i$ and substituting $y=w_i(t)$,
$$\int_T^\infty f_1f_2\,dt\le 3\int_{|y|\ge m,\ \text{one side}}\frac{f_i(y)}{|y|}dy\le 3\log(1+1/m),\qquad m=\tfrac12|u_i|e^{T},$$
by the bathtub principle ($0\le f_i\le1$, $\int f_i\le1$, weight decreasing). Take $T=\max(T_1,\log(2/|u_i|))$, so $m\ge1$ and the tail is $\le3\log2$; the tail $t\le-T'$ is the same with $v$ in place of $u$. The middle part is $\le T+T'$ since $f_1f_2\le1$, and $T,T'\le 0.52+\tfrac12\log_+\frac{32}{\delta\Lambda}$. So each branch integral is $\le 1.04+6\log2+\log_+\frac{32}{\delta\Lambda}\le 5.2+\log_+\frac{32}{\delta\Lambda}$; two branches and the factor $1/(2\sqrt D)$ give the claim. For the sublevel bound integrate over $|s'-s|\le u$ and use that $\int_{-u}^{u}\log_+\frac{K}{|\tau-\tau_0|}d\tau\le 2u(1+\log_+\frac Ku)$ (the centred case is the worst, by rearrangement). $\square$

Remarks. (a) The coefficient of the logarithm is sharp: for $B=\mathrm{diag}(1,-1)$ and uniform $W$ the density is $\log(1/|\delta|)+O(1)$; the adversarial search of Section 7 gets within a factor $2$ of the bound. (b) The only product-structure input is $\rho(w)\le\min(f_1(w_1),f_2(w_2))$ with $\int f_i=1$: the far arms of the hyperbola are graphs over one coordinate axis and one marginal's unit mass cuts the $\int dt$ divergence off. For a general density on $\mathbb R^2$ with bounded marginals the far arms can be hugged by thin curved strips and (1.1) is unbounded; this is exactly the mechanism of (F1) in one dimension lower. (c) Case $B$ with $\det B=0$ is not covered; it is never needed below.

**Lemma 1.5 (Schur complements keep large eigenvalues).** Let $A$ be symmetric, $A_{PP}$ invertible, $p=|P|$. Then $\#\{\nu\in\mathrm{spec}(A/A_{PP}):|\nu|\ge1\}\ \ge\ \#\{\lambda\in\mathrm{spec}(A):|\lambda|\ge1\}-p$. If $A$ is invertible, $(A/A_{PP})^{-1}=(A^{-1})_{P^cP^c}$ and $\det A=\det A_{PP}\det(A/A_{PP})$; so if all $|\lambda(A)|\ge1$ then $\|(A/A_{PP})^{-1}\|\le\|A^{-1}\|\le1$ and all $|\nu(A/A_{PP})|\ge1$. In particular for $n=3$, $P=\{i,j\}$, $k$ the third index: the scalar $\sigma_k:=A/A_{PP}=\det A/\det A_{PP}=1/(A^{-1})_{kk}$ has $|\sigma_k|\ge1$.
Proof. For invertible $A$ the eigenvalues $\alpha_1\ge\dots\ge\alpha_n$ of $A^{-1}$ with $|\alpha|\le1$ form a block of consecutive indices $a..b$; Cauchy interlacing for the codimension-$p$ principal submatrix gives eigenvalues $\beta_j\in[\alpha_{j+p},\alpha_j]\subset[-1,1]$ for $a\le j\le b-p$. Invert. For singular $A$ apply this to $(A+\varepsilon I)/(1-\varepsilon)$ (invertible for all but finitely many $\varepsilon$, same count of eigenvalues of modulus $\ge1$) and let $\varepsilon\to0$; Schur complements are continuous and "$|\nu|\ge1-O(\varepsilon)$" passes to the limit. $\square$

**Lemma 1.6 (layer cake).** For any $Z$ with $\varphi_Z\le\varphi$:
$\sup_sE|Z-s|^{-1/2}\le\int_0^\infty\min(1,\varphi(v^{-2}))dv$; $\ \sup_sE\log_+\frac{M}{|Z-s|}\le\int_0^\infty\min(1,\varphi(Me^{-\tau}))d\tau$; $\ \sup_sE\max(|Z-s|,u)^{-1/2}\le\int_0^{u^{-1/2}}\min(1,\varphi(v^{-2}))dv$.
Consequences used below: $E\log_+\frac1{|Z-s|}\le2\log_+\alpha_1(Z)+2$; if $\varphi(u)\le Ku(1+\log_+\frac1u)$ with $K\ge1$ then $E|Z-s|^{-1/2}\le 8\sqrt{K(1+\log K)}$.

## 2. The case n = 3 (PROVED, constant 20)

**Theorem 2.1.** Let $A$ be a real symmetric $3\times3$ matrix all of whose eigenvalues satisfy $|\lambda|\ge1$ (any signs), $b\in\mathbb R^3$, $c\in\mathbb R$, and let $X_1,X_2,X_3$ be independent with densities $\le1$ (arbitrary laws: spread-out unions of intervals allowed; identical distribution not needed). Then $Q=X^TAX+b^TX+c$ has a density bounded by $20$.

Proof. Two routes, chosen by the diagonal of $A$.

*Route (i): some $|a_{ii}|\ge0.3$.* Condition on $X_{-i}=(X_j,X_k)$. By Lemma 1.1 with $P=\{i\}$, $Q=a_{ii}(X_i-m)^2+R(X_j,X_k)$, where $R$ is a quadratic in two independent coordinates whose quadratic part is the $2\times2$ Schur complement $S=A/a_{ii}$. By Lemma 1.5 both eigenvalues of $S$ have modulus $\ge1$, so $D_S=|\det S|\ge1$. By Lemma 1.2(i) and Lemma 1.1,
$$p_Q(s)\le |a_{ii}|^{-1/2}\,\sup_s E|s-R(X_j,X_k)|^{-1/2}.$$
If $S$ is definite, Lemma 1.3 gives $\varphi_R(u)\le 2\pi u/\sqrt{D_S}\le2\pi u$ and Lemma 1.6 gives $E|s-R|^{-1/2}\le2\sqrt{2\pi}\le5.02$. If $S$ is indefinite, Lemma 1.4 gives, for $u\le1$ and using $D_S\ge1$, $\varphi_R(u)\le\frac{2u}{\sqrt{D_S}}(6.2+\log16+\tfrac12\log D_S+\log\tfrac1u)\le 2u(9.34+\log\tfrac1u)$ (because $\frac{\log D}{2\sqrt D}\le e^{-1}$), and Lemma 1.6 gives $E|s-R|^{-1/2}\le\int_0^\infty\min\{1,2v^{-2}(9.34+2\log_+v)\}dv\le10.83$ (evaluated numerically, script n4_constants.py). Hence $p_Q\le 10.83/\sqrt{0.3}\le19.8$.

*Route (ii): all $|a_{ii}|<0.3$.* Then $\|A\|_F^2=\sum\lambda_j^2\ge3$ forces $\sum_{i<j}a_{ij}^2>(3-0.27)/2$, so some $a_{ij}^2>0.455$ and the principal block $B=A_{\{ij\}}$ has $D=|\det B|\ge a_{ij}^2-|a_{ii}a_{jj}|>0.365$. Condition on $X_k$ ($k$ the third index). Given $X_k=x$, $Q=q_x(X_i,X_j)$ with quadratic part $B$ and critical value $\kappa(x)$, a quadratic polynomial in $x$ with leading coefficient $\sigma_k=\det A/\det B$, $|\sigma_k|\ge1$ (Lemma 1.5).
If $B$ is definite, Lemma 1.3 gives $p_Q\le\pi/\sqrt D\le5.2$.
If $B$ is indefinite, Lemma 1.4 and Lemma 1.1 give
$$p_Q(s)\le D^{-1/2}\Big(5.2+\log_+(16\sqrt D)+E\log_+\frac1{|s-\kappa(X_k)|}\Big),$$
and by Lemma 1.2(ii) $\alpha_1(\kappa(X_k))\le2\sqrt2/\sqrt{|\sigma_k|}\le2\sqrt2$, so Lemma 1.6 gives $E\log_+\frac1{|s-\kappa|}\le2\log(2\sqrt2)+2$. Thus $p_Q\le D^{-1/2}(9.28+\log_+(16\sqrt D))$, a decreasing function of $D$, equal to $19.2$ at $D=0.365$. $\square$

Audit notes. (1) The averaging over the third coordinate is exactly what rescues the indefinite $2\times2$ block: the conditional density has a $\log$ singularity at $\kappa(X_k)$, and $\kappa(X_k)$ is a nondegenerate one-dimensional quadratic of $X_k$ ($|\sigma_k|\ge1$), whose small-ball probability $O(\sqrt u)$ makes $\log(1/|s-\kappa|)$ integrable, uniformly over all laws. (2) Nothing about the sets $E_i$ is used beyond $f_i\le1$, $\int f_i=1$; the linear terms are absorbed into $m$, $\kappa$, $R$. (3) Independence (not identical distribution) is all that is used, here and throughout this report. (4) Numerically the true supremum is far smaller: about $2.53$ for $I-2ee^T$ and $2.55$ for the example of question (a), both attained by uniform laws at $s\approx0$ (Section 7); the constant 20 is an artefact of crude bookkeeping.

**The hard examples, explicitly.**
- $A=I-2ee^T$, $e=(1,1,1)/\sqrt3$: $a_{ii}=1/3$, every $2\times2$ principal block is $\begin{pmatrix}1/3&-2/3\\-2/3&1/3\end{pmatrix}$ (indefinite). Route (i) with $i=1$: $S=\begin{pmatrix}-1&-2\\-2&-1\end{pmatrix}$, eigenvalues $1,-3$. Bound $10.83\sqrt3\le18.8$.
- The example $A=\begin{pmatrix}1/2&1/2&1/\sqrt2\\1/2&1/2&-1/\sqrt2\\1/\sqrt2&-1/\sqrt2&0\end{pmatrix}$, $Q=S^2/2+\sqrt2X_3D$ ($S=X_1+X_2$, $D=X_1-X_2$). The naive split conditions on $X_3$ and meets $E|D|^{-1}=\infty$. Route (i) conditions on $(X_2,X_3)$ instead: $a_{11}=1/2$, $Q=\tfrac12(X_1-m)^2+R(X_2,X_3)$ with $S=A/a_{11}=\begin{pmatrix}0&-\sqrt2\\-\sqrt2&-1\end{pmatrix}$ (eigenvalues $1,-2$). The square-root singularity in $X_1$ is integrated against the $u\log(1/u)$ small-ball law of the hyperbolic $R(X_2,X_3)$. Bound $10.83\sqrt2\le15.4$.
- $A=2I-J$ (eigenvalues $2,2,-1$): every $2\times2$ principal block $\begin{pmatrix}1&-1\\-1&1\end{pmatrix}$ is singular. Route (i): $Q=(X_1-X_2-X_3)^2-4X_2X_3$, $S=\begin{pmatrix}0&-2\\-2&0\end{pmatrix}$.
- Zero diagonal, e.g. $A=-(J-I)$ (eigenvalues $1,1,-2$), $Q=-2(X_1X_2+X_1X_3+X_2X_3)$: route (ii) with $B=\begin{pmatrix}0&-1\\-1&0\end{pmatrix}$, $Q=-2(X_1+X_3)(X_2+X_3)+2X_3^2$, $\kappa(X_3)=2X_3^2$.

**Corollary 2.2 (3x3 core in any dimension).** If $A$ ($n\times n$, any $n$) has a principal $3\times3$ submatrix $A_{SS}$ with all eigenvalues of modulus $\ge\gamma>0$, then $\|p_Q\|_\infty\le20/\gamma$ for all linear terms and all laws. Proof: condition on $X_{S^c}$ (Lemma 1.1); the conditional form in $X_S$ has matrix $A_{SS}$ and some linear terms; apply Theorem 2.1 to $A_{SS}/\gamma$ and rescale. $\square$

## 3. A pivot calculus: localized structure in any dimension (PROVED)

The n = 3 proof is one instance of a mechanism that works in every dimension and never uses the eigenvalue hypothesis except to guarantee that a pivot exists.

### 3.1 Profiles around random centres
Say $Q$ has a **profile of type 1 (resp. 2, 3) with constant $K$ around the random centre $\xi$** if for a.e. $y$
$$p_Q(y)\le K\,E|y-\xi|^{-1/2},\qquad(\text{resp. } p_Q(y)\le K\,E\big[1+\log_+\tfrac1{|y-\xi|}\big],\qquad p_Q\le K).$$
Pivots produce profiles (Lemmas 1.1-1.4):
- **(P1) 1x1 pivot.** If $a_{ii}\ne0$: type 1 with $K=|a_{ii}|^{-1/2}$ around $\xi=R_i(X_{-i})$, a quadratic polynomial of $X_{-i}$ with matrix $A/a_{ii}$.
- **(P2) indefinite 2x2 pivot.** If $B=A_{\{ij\}}$ is indefinite, $D=|\det B|>0$: type 2 with $K=D^{-1/2}(5.2+\log_+16\sqrt D)$ around $\xi=\kappa_B(X_{-ij})$ (matrix $A/B$).
- **(P3) definite 2x2 pivot.** If $B$ is definite: type 3 with $K=\pi/\sqrt D$. No centre needed.

Composition with the centre uses only the centre's small-ball function $\varphi_\xi$ (Lemma 1.6, plus $\int_{-u}^u|y+d|^{-1/2}dy\le4\sqrt2\,u/\sqrt{\max(|d|,u)}$):
- **(C1)** type 1 ($K$) around $\xi$ with $\alpha_2(\xi)\le K'$ ($K'\ge1$) $\Rightarrow$ $\|p_Q\|_\infty\le 8K\sqrt{K'(1+\log K')}$.
- **(C2)** type 1 ($K$) around $\xi$ with $\alpha_1(\xi)\le K'$ $\Rightarrow$ $\alpha_2(Q)\le4\sqrt2\,K\max(K',1)$.
- **(C3)** type 2 ($K$) around $\xi$ with $\alpha_1(\xi)\le K'$ $\Rightarrow$ $\|p_Q\|_\infty\le K(3+2\log_+K')$.
- **(C4)** type 2 ($K$), any centre $\Rightarrow\alpha_2(Q)\le4K$. **(C5)** type 1 ($K$), any centre $\Rightarrow\alpha_1(Q)\le4K$. **(C6)** type 3 ($K$) $\Rightarrow\alpha_2(Q)\le2K$, $\alpha_1(Q)\le\max(2K,1)$.

Independent sums. If $Q=Q_1(X_{G_1})+Q_2(X_{G_2})$ with disjoint coordinate groups and $Q_1$ has a type-$a$ profile around $\xi_1$ (a function of $X_{G_1}$), then $Q$ has the same profile around $\xi_1+Q_2$, and $\varphi_{\xi_1+Q_2}\le\varphi_{Q_2}$ (condition on $\xi_1$). So (C1)-(C3) apply with $Q_2$ in place of the centre.

### 3.2 Certified pivot chains (universal constants)
Fix $c\in(0,1]$. A symmetric matrix $M$ is **$c$-certified of level $k$** if:
- level 1: $M$ has $|m_{ii}|\ge c$, or a $2\times2$ principal block with $|\det|\ge c$;
- level 2: $M$ has a $2\times2$ principal block with $|\det|\ge c$, or $|m_{ii}|\ge c$ with $M/m_{ii}$ certified of level 1;
- level 3: $M$ has a definite $2\times2$ principal block with $\det\ge c$; or an indefinite one, $B$, with $|\det B|\ge c$ and $M/B$ certified of level 1; or $|m_{ii}|\ge c$ with $M/m_{ii}$ certified of level 2.

By the quotient property of Schur complements a certificate involves at most **four** coordinates and depends only on the principal submatrix on them.

**Theorem 3.1.** If $A$ is $c$-certified of level $k$, then for every linear term, every $n$ and all independent laws with densities $\le1$: $\alpha_1(Q)\le K_1:=50c^{-1/2}$ ($k=1$), $\alpha_2(Q)\le K_2:=283c^{-1}$ ($k=2$), $\|p_Q\|_\infty\le K_3:=135c^{-1}\sqrt{6.7+\log(1/c)}$ ($k=3$). No other entry of $A$ and no eigenvalue of $A$ enters.

Proof. Induction on $k$ with (P1)-(P3), (C1)-(C6) and the sublevel form of Lemma 1.4. Level 1: 1x1 pivot, $\alpha_1\le2\sqrt2c^{-1/2}$ (Lemma 1.2); definite 2x2, $\alpha_1\le\sqrt{2\pi}D^{-1/4}$; indefinite 2x2, $\sup_u\frac{2\sqrt u}{\sqrt D}(6.2+\log_+\frac{16\sqrt D}u)=49.6D^{-1/4}$ (the maximum is at $u=16\sqrt D$). Level 2: a 2x2 block gives $\alpha_2\le2(6.2+\log16+\tfrac12\log_+D)/\sqrt D\le19c^{-1/2}$; a 1x1 pivot followed by level 1 gives $\alpha_2\le4\sqrt2c^{-1/2}K_1$ by (C2). Level 3: definite gives $\pi c^{-1/2}$; indefinite followed by level 1 gives $8.4c^{-1/2}(3+2\log K_1)$ by (C3); 1x1 followed by level 2 gives $8c^{-1/2}\sqrt{K_2(1+\log K_2)}$ by (C1), which dominates. $\square$

Corollaries. (a) The proof of Theorem 2.1 exhibits, for every $3\times3$ matrix with all $|\lambda|\ge1$, a level-3 certificate with $c=0.3$; so Theorem 3.1 contains Theorem 2.1 and Corollary 2.2 up to the value of the constant. (b) **Direct sums.** If $A$ is block diagonal and block $a$ is $c$-certified of level $k_a$, with $\sum k_a\ge3$, then $A$ is $c$-certified of level 3 (pivots taken inside different blocks do not interact, because Schur complements preserve the block structure). This is the general form of question (c): $Q=2(X_1X_2+X_3X_4)$ is certified (indefinite pivot $\{1,2\}$, then the level-1 pivot $\{3,4\}$ of the Schur complement $A_{\{34\}}$), as is $2(X_1X_2+X_3X_4+X_5X_6)$, any $\lambda_1X_1^2+2X_2X_3$, any three diagonal entries $\ge c$, and any mixture of a diagonal part with localized blocks. (c) Certificates survive arbitrary additional coupling to other coordinates as long as the four-coordinate principal submatrix still has the pivots.

### 3.3 Every fixed dimension
**Theorem 3.2.** For every $n$ and every $n\times n$ symmetric $A$ with at least three eigenvalues of modulus $\ge1$: $\|p_Q\|_\infty\le C_n:=250\,n\,(8+\log n)$, for all linear terms and all laws.

Proof. Run the decision tree of Theorem 3.1 on the actual Schur complements, choosing pivots by size. At level $k$ the current matrix $M$ (size $m\le n$) has at least $k$ eigenvalues of modulus $\ge1$ (Lemma 1.5, applied to the composite pivot set), hence $\|M\|_F\ge1$; then either $\max_i|m_{ii}|\ge1/(2m)$, or $\sum_i m_{ii}^2<1/(4m)$ and some $|m_{ij}|^2\ge3/(4m(m-1))$, whence $|\det M_{\{ij\}}|\ge m_{ij}^2-|m_{ii}m_{jj}|\ge1/(2m^2)$. Redo the bookkeeping of Theorem 3.1 with threshold $1/(2n)$ for 1x1 pivots and $1/(2n^2)$ for 2x2 pivots: $\alpha_1\le59\sqrt n$, $\alpha_2\le472n$, $\|p_Q\|\le\max\{246n\sqrt{7.2+\log n},\,11.7n(11.2+\log n),\,4.5n\}$. $\square$

Remarks. (1) The recursion depth is at most 3 whatever $n$ is, which is why the constant is polynomial. (2) The loss is exactly delocalization: the pivots can be as small as $1/n$ (diagonal) or $1/n^2$ (2x2 minors) only when the mass of $A$ is spread over $\gtrsim n$ rows, which is the regime where the Fourier argument works. (3) For rank-3 forms Section 4 improves $n\log n$ to $60(n-2)$.

## 4. Rank-3 forms and the thin-shell question

Here $A=R\Lambda R^T$ with $R\in\mathbb R^{n\times3}$ orthonormal columns $r_1,r_2,r_3$, $\Lambda=\mathrm{diag}(\lambda_k)$, $|\lambda_k|\ge1$; $r^{(i)}\in\mathbb R^3$ is the $i$-th row of $R$ and $\ell_i=|r^{(i)}|^2$ its leverage ($\sum_i\ell_i=3$). Linear terms are arbitrary (they need not lie in the range of $R$).

**Proposition 4.1 (PROVED).** (a) If $R_S$ ($S$ a 3-set of rows) is invertible, then $\|p_Q\|_\infty\le20/\sigma_{\min}(R_S)^2$. (b) Consequently every rank-3 form satisfies $\|p_Q\|_\infty\le60(n-2)$.
Proof. (a) $A_{SS}=R_S\Lambda R_S^T$; by Ostrowski's theorem its eigenvalues are $\theta_k\lambda_k$ with $\theta_k\in[\sigma_{\min}(R_S)^2,\sigma_{\max}(R_S)^2]$, so all have modulus $\ge\sigma_{\min}(R_S)^2$; apply Corollary 2.2. (b) Take $S$ maximizing $|\det R_S|$. By Cramer's rule every entry of $RR_S^{-1}$ is a ratio of two $3\times3$ minors of $R$, hence of modulus $\le1$, and its rows in $S$ form $I_3$; so $\|R_S^{-1}\|=\|RR_S^{-1}\|\le\|RR_S^{-1}\|_F\le\sqrt{3(n-2)}$ (the first equality because $R$ is an isometry). $\square$

**Proposition 4.2 (PROVED, given Theorem D of RESULTS.md).** If all leverages satisfy $\ell_i\le1/50$, a uniformly random partition $I\cup J$ satisfies, with probability $\ge0.87$, $\lambda_{\min}(R_I^TR_I),\lambda_{\min}(R_J^TR_J)\ge1/4$. For such a partition $e_3(A_{IJ}^TA_{IJ})=\det(\Lambda)^2\det(R_I^TR_I)\det(R_J^TR_J)\ge4^{-6}$, and the volume-sampling marginal of $i\in I$ equals $r^{(i)T}(R_I^TR_I)^{-1}r^{(i)}\le4\ell_i\le1/2$. So Theorem D gives $\|p_Q\|_\infty\le6\sqrt e\cdot4\le40$.
Proof. Matrix Chernoff (Tropp) for $\sum_{i\in I}r^{(i)}r^{(i)T}$, summands $\preceq\ell_i\le\varepsilon$, mean $I_3/2$: $P(\lambda_{\min}\le\tfrac14)\le3\big(e^{-1/2}(1/2)^{-1/2}\big)^{1/(2\varepsilon)}=3e^{-0.0767/\varepsilon}$; union over $I$ and $J$. The nonzero eigenvalues of $A_{IJ}^TA_{IJ}=R_J\Lambda R_I^TR_I\Lambda R_J^T$ are those of $(\Lambda R_I^TR_I\Lambda)(R_J^TR_J)$. For $G=A_{IJ}A_{IJ}^T=UU^T$, $U=R_I(\Lambda R_J^TR_J\Lambda)^{1/2}$ of rank 3, $\det G_{SS}=\det(U_S)^2$, so the marginal of $i$ is the leverage of row $i$ of $U$, which does not depend on the right factor. $\square$

So for rank-3 forms the only case not covered by Fourier is **some coordinate of leverage $\ge1/50$**. Two different things can happen there.
- *Positive semidefinite $\Lambda$*: $a_{ii}=r^{(i)T}\Lambda r^{(i)}\ge\ell_i\ge1/50$ is a 1x1 pivot. Then $Q$ has a type-1 profile around $R_i(X_{-i})$ whose matrix $A/a_{ii}$ is PSD of rank 2 with both eigenvalues $\ge1$ (Lemma 1.5); what is needed is the small-ball law $\alpha_2(R_i)\lesssim1$ for a rank-2 PSD form **with arbitrary linear terms** (possibly outside its range). If $A/a_{ii}$ has a heavy coordinate we pivot again (Theorem 3.1); otherwise all its rank-2 leverages are small and a random partition makes both $2\times2$ Gram blocks well conditioned (same Chernoff argument), which is the rank-2 version of the hypothesis of Theorem D. So **for PSD rank-3 forms, including $|PX|^2$, the conjecture follows from the Fourier bound of Theorem D in the three versions $e_1,e_2,e_3$ (decay $|t|^{-1/2},|t|^{-1},|t|^{-3/2}$, uniform over linear terms) under small leverages.** Without linear terms outside the range the rank-2 step is elementary (2D projections have density $\le2$, K3); with them it is not: $R=q(Y)+\beta Z$ with $Z$ orthogonal to $Y$ leads to the mixed norm of (F2).
- *Indefinite $\Lambda$*: a heavy coordinate need not be a pivot. Example: $r_{1,2}=(e_1\pm w)/\sqrt2$, $\lambda=\pm1$, gives $A=e_1w^T+we_1^T$ with $\ell_1=1$, $a_{11}=0$ and all $2\times2$ minors $-w_j^2$ small: a **hub**. Section 5.3 treats hubs.

**The spherical-means question (exact reformulation).** For $Y=R^TX\in\mathbb R^3$ with density $\rho_Y$ and $y_0\in\mathbb R^3$, the coarea formula gives
$$p_{|Y-y_0|^2}(r^2)=2\pi r\,M_{y_0}(r),\qquad M_{y_0}(r)=\text{mean of }\rho_Y\text{ over the sphere }\{|y-y_0|=r\}.$$
So "spherical means of $\rho_{PX}$ are $\le C/r$ uniformly in the centre" is *equivalent* to the conjecture for $Q=|PX-y_0|^2$. Status: true with $C\le60(n-2)/(2\pi)$ always (Prop. 4.1(b)); with $C$ universal if $R$ has a $3\times3$ minor with $\sigma_{\min}$ bounded below or, more generally, a certified pivot chain; with $C\le40/(2\pi)$ if all leverages are $\le1/50$ (Prop. 4.2); open in the mixed regime described above. The product structure is essential: $\rho_Y\le2^{3/2}$ alone allows $M(r)\sim$ const at large $r$ (thin shells, F1). For a product measure the mechanism that forbids shells is the one in Lemma 1.4: far from the centre a level set is almost flat, and a coordinate marginal with unit mass cannot follow it.

## 5. Gluing with the Fourier regime

### 5.1 Reduction to matrices with no local structure (PROVED)
Say $M$ has **no $c$-pivot** if every $|m_{ii}|<c$ and every $2\times2$ principal minor has modulus $<c$. Then every $|m_{ij}|<\sqrt{2c}$, and $\|\mathrm{diag}(M)\|<c$, so the large eigenvalues live in the off-diagonal part.

**Theorem 5.1.** Fix $c\in(0,1]$. Suppose that for $k=1,2,3$ there are constants $H_k$ such that
> (Hyp$_k$) for every symmetric $M$ with at least $k$ eigenvalues of modulus $\ge1$ and **no $c$-pivot**, every $R=Y^TMY+\beta^TY+\gamma$ ($Y$ independent coordinates, densities $\le1$, any $\beta,\gamma$) has $\alpha_k(R)\le H_k$ ($\alpha_3=$ sup of the density).

Then the conjecture holds, with $C$ depending only on $c,H_1,H_2,H_3$.

Proof. Decision tree of depth $\le3$. At level $k$ the current Schur complement $M_k$ has $\ge k$ eigenvalues of modulus $\ge1$ (Lemma 1.5). If $M_k$ has a $c$-pivot, apply (P1)/(P2)/(P3): a 1x1 pivot lowers the level by one; a definite 2x2 pivot ends the tree; an indefinite 2x2 pivot ends it at levels 1, 2 and lowers level 3 to level 1. If not, Hyp$_k$ ends the tree. Every composition is one of (C1)-(C6), which only need the small-ball function of the centre. $\square$

**Theorem 5.2 (equivalence, PROVED).** Replace Hyp$_1$, Hyp$_2$ by the integrability forms
Hyp$'_1$: $\sup_sE\log_+\frac1{|s-R|}\le H_1$ (for $\ge1$ large eigenvalue, no $c$-pivot) and Hyp$'_2$: $\sup_sE\big[|s-R|^{-1/2};|s-R|\le1\big]\le H_2$ ($\ge2$ large eigenvalues, no $c$-pivot). Then (Hyp$'_1$, Hyp$'_2$, Hyp$_3$) imply the conjecture, and **the conjecture implies all three**. So the conjecture is equivalent, with polynomially related constants, to its no-pivot restriction in these three forms.
Proof. Sufficiency: the same decision tree; the only new composition is "1x1 pivot followed by level 1" into Hyp$'_2$ form, where Lemma 1.2(ii) gives $\int_1^\infty\varphi_Q(v^{-2})dv\le\frac{4}{\sqrt{|a|}}(1+\tfrac12E\log_+\frac1{|s-R|})$. Necessity: Hyp$_3$ is a special case. For Hyp$'_2$ add a new independent coordinate $X_0$ uniform on $[-\tfrac12,\tfrac12]$: $R\pm4X_0^2$ has $\ge3$ eigenvalues of modulus $\ge1$ and $p_{R\pm4X_0^2}(s)=\tfrac12E[|s-R|^{-1/2};0<\pm(s-R)\le1]$. For Hyp$'_1$ add two: $R+4(X_0^2-X_0'^2)$, and use $p_{4(U^2-V^2)}(z)\ge\frac14\log_+\frac1{|z|}$ for $|z|\le\frac12$ (uniform $U,V$). $\square$

So **the conjecture is equivalent to its restriction to matrices with no $c$-pivot** (entrywise small, $\max|m_{ij}|<\sqrt{2c}$), in the three forms above, for any fixed small $c$ (constants degrade polynomially in $1/c$). Everything living on $\le4$ coordinates (principal blocks, diagonal parts, direct sums of small blocks, the $n=3$ structures) is absorbed by the pivot calculus. What the Fourier side has to supply is exactly Hyp$_1$-Hyp$_3$ with uniformity over linear terms. Theorem D (spread 3-volume of an off-diagonal block) is a sufficient condition for Hyp$_3$; the same argument with $e_1,e_2$ in place of $e_3$ should give Hyp$_1$, Hyp$_2$ under spread 1- and 2-volume. For rank-3 PSD forms, Proposition 4.2 shows that "no pivot" forces small leverages and hence the spread condition, so there the gluing is complete modulo the $e_1,e_2$ versions.

### 5.2 Hubs: the structure both methods miss
A **hub** is a coordinate $h$ with (nearly) zero diagonal whose row $w=A_{h,-h}$ has norm $\gtrsim1$ but small entries: $Q\ni 2X_h\langle w,X_{-h}\rangle$. A hub carries two eigenvalues $\pm|w|$, has no pivot (all $2\times2$ minors $-w_j^2$ are tiny), and is seen by an off-diagonal block only with **rank one** (column $w_I$ if $h\in J$). So a hub "costs" two large eigenvalues but contributes one to $e_k$. Consequences:
- one hub alone ($Q=2X_hL$, $L=\langle w,X_{-h}\rangle$, rank 2): $e_2(A_{IJ}^TA_{IJ})=0$ for every partition, yet Hyp$_2$ must hold for it;
- one hub plus one delocalized rank-one direction ($Q=2X_hL+\lambda V^2$, $V=\langle v,X_{-h}\rangle$, $v\perp w$, eigenvalues $\pm1,\lambda$): every off-diagonal block has rank $\le2$, so $e_3=0$ for all partitions, and there is no pivot. Neither the pivot calculus nor the $e_3$-Fourier theorem applies. This is the sharpest example I know of an input that falls between the two methods.

Both are handled by a third, elementary tool: the density bound $\le2^{k/2}$ for $k$-dimensional projections (K5) applied to the hub rows.

**Proposition 5.3 (hub lemma, PROVED).** If $a_{hh}=0$ and $|w|>0$ then $\alpha_2(Q)\le2+4\sqrt2/|w|$ (any other entries, any linear terms).
Proof. Given $X_{-h}$, $Q$ is affine in $X_h$ with slope $L'=2\langle w,X_{-h}\rangle+b_h$, so $P(|Q-s|\le u\mid X_{-h})\le\min(1,2u/|L'|)$. The density of $L'$ is $\le\sqrt2/|w|$ (Ball, one-dimensional case of K5). Split $|L'|\le2u$, $2u<|L'|\le1$, $|L'|>1$. $\square$

**Proposition 5.4 (one hub + rank one, any hub diagonal, PROVED).** Let $w,v\in\mathbb R^{n-1}$ be orthonormal, $L=\langle w,X_{-h}\rangle$, $V=\langle v,X_{-h}\rangle$, $a,\beta\in\mathbb R$, and
$$Q=aX_h^2+2(L+\beta)X_h+F(L,V),\qquad F(\ell,v)=\lambda(v-v_c(\ell))^2+F_c(\ell),\quad F_c(\ell)=\sigma_F\ell^2+\text{affine},$$
with $\lambda\ne0$ and $D_H:=|1-a\sigma_F|>0$. Then $\|p_Q\|_\infty\le1+4|\lambda|^{-1/2}\Psi(D_H)$, where $\Psi(D)=2\sqrt{2\pi}D^{-1/4}$ if $a\sigma_F>1$ and $\Psi(D)=8\sqrt{K(1+\log K)}$, $K=\max\{1,2D^{-1/2}(6.2+\log_+16\sqrt D)\}$, if $a\sigma_F<1$. For $a=0$ (zero hub diagonal) and $|\lambda|\ge1$ the direct computation gives $\frac12+16|\lambda|^{-1/2}\le16.5$. (Here $1-a\sigma_F=-\det M_{\rm core}/\lambda$, $M_{\rm core}$ the matrix of the form on $\mathrm{span}(e_h,w,v)$.)
Proof. Given $X_{-h}$, $Q=g(X_h)$ with $g(x)=ax^2+2tx+F(\ell,v)$, $t=\ell+\beta$, whose density at $s$ is $\sum_{g(x)=s}f_h(x)/(2|ax+t|)$. So $p_Q(s)=\iint\rho_{LV}\sum_{g(x)=s}\frac{f_h(x)}{2|ax+t|}\,d\ell\,dv$, $\rho_{LV}\le2$ (K5). Roots with $|ax+t|\ge1$ contribute $\le\int\!\!\int\rho_{LV}=1$. For the others change variables $v\mapsto x$ at fixed $\ell$ (on each monotone branch $|dv/dx|=2|ax+t|/|\partial_vF|$): their contribution is
$$\int\!\!\int f_h(x)\,\mathbf 1\{|ax+\ell+\beta|<1\}\sum_{v:\,F(\ell,v)=s-ax^2-2(\ell+\beta)x}\frac{\rho_{LV}(\ell,v)}{|\partial_vF|}\,d\ell\,dx\ \le\ \int\!\!\int f_h(x)\mathbf 1\{\cdot\}\frac{2\,d\ell\,dx}{\sqrt{|\lambda||H(\ell,x)|}},$$
$H=s-ax^2-2(\ell+\beta)x-F_c(\ell)$, since $|\partial_vF|=2\sqrt{|\lambda||H|}$ at both solutions. Put $\ell=r-ax-\beta$, $|r|<1$: $H$ becomes a quadratic $\tilde H(r,x)$ with quadratic part $\begin{pmatrix}-\sigma_F&a\sigma_F-1\\a\sigma_F-1&a-a^2\sigma_F\end{pmatrix}$, determinant $a\sigma_F-1$. So the contribution is $\le4|\lambda|^{-1/2}E|\tilde H(U,X_h)|^{-1/2}$ with $U$ uniform on $(-1,1)$ independent of $X_h$ (densities $\frac12,\le1$), and Lemma 1.3/1.4 with Lemma 1.6 bound this by $\Psi(D_H)$. For $a=0$ one can instead integrate $f_h$ first: $\int f_h\big(\frac{s-F}{2t}\big)dv\le4|t|^{1/2}|\lambda|^{-1/2}$ and $\int_{|t|<1}\frac{dt}{2|t|}\cdot2\cdot4|t|^{1/2}|\lambda|^{-1/2}=16|\lambda|^{-1/2}$. $\square$
The mechanism is the same as in Theorem 2.1: the $1/|ax+t|$ singularity of the hub coordinate is exchanged, by one change of variables, for a square-root singularity of a nondegenerate two-variable quadratic in $(r,X_h)$, which Lemma 1.4 integrates uniformly.

**Proposition 5.5 (two hubs, PROVED).** Let $H=\{h_1,h_2\}$ with $A_{HH}=0$ and let the $2\times(n-2)$ matrix $A_{H,H^c}$ have singular values $\ge\sigma>0$. Then $\|p_Q\|_\infty\le\frac12+8\sigma^{-2}$, **whatever** $A_{H^cH^c}$ and the linear terms are.
Proof. Given $X_{H^c}$, $Q=c_1X_{h_1}+c_2X_{h_2}+\text{const}$ with $(c_1,c_2)=2(L_1,L_2)+b_H$, $(L_1,L_2)=A_{H,H^c}X_{H^c}$; the conditional density is $\le1/\max(|c_1|,|c_2|)$ (convolution of $c_1X_{h_1}$, density $\le1/|c_1|$, with $c_2X_{h_2}$). By K5 and a linear change of variables $(L_1,L_2)$ has density $\le2/(\sigma_1\sigma_2)$. Hence $p_Q\le E\frac{1}{2|L-\ell_0|_\infty}\le\frac{2}{\sigma_1\sigma_2}\int_{|z|_\infty\le1}\frac{dz}{2|z|_\infty}+\frac12=\frac{8}{\sigma_1\sigma_2}+\frac12$. $\square$

Remarks. (1) Two hubs already give a bounded density although their off-diagonal blocks have rank 2 ($e_3=0$): the four eigenvalues $\pm|w_1|,\pm|w_2|$ are all used. (2) Props 5.3 and 5.5 need the hub diagonal (resp. $A_{HH}$) to vanish exactly; Prop. 5.4 does not. With $0<|a_{hh}|<c$ the small-ball function of a hub genuinely acquires a term of order $\sqrt{|a_{hh}|u}/|w|$ (on the event $L'\approx0$, of probability $\sim|a_{hh}|/|w|$, $Q$ is a one-dimensional quadratic with coefficient $a_{hh}$), so the sublevel statement of Prop. 5.3 is FALSE for small nonzero diagonal. Prop. 5.4 shows how the density bound survives anyway: one must not pass through sublevel bounds, but change variables so that the centre of the square-root singularity is integrated by a two-variable hyperbolic estimate. The same device should handle Prop. 5.5 with small $A_{HH}\ne0$, but the remainder $R(X_{H^c})$ is then not a function of a fixed low-dimensional projection and I have no proof (Section 8).

### 5.3 What the gluing lemma must say
Combining Theorem 5.1 with Section 5.2, a complete proof needs, in the no-pivot regime, a statement of the following shape (OPEN):
> **Gluing lemma (conjectural).** Let $M$ have no $c$-pivot and $\ge k$ eigenvalues of modulus $\ge1$. Let $H$ be the set of hubs (rows of norm $\ge\eta$; there are at most $\|M\|_F^2/\eta^2$ of them, but $\|M\|_F$ is not bounded, so one should take hubs relative to the large eigenspace). Then the $k$ large directions split as $2|H'|+k'$, where $H'\subseteq H$ are hubs whose rows are well conditioned (Props 5.3-5.5 handle them after conditioning on $X_{H^c}$), and $k'$ directions are carried by $M_{H^cH^c}$ with spread $k'$-volume in some off-diagonal block (Fourier on $X_{H^c}$, conditionally on $X_H$, uniformly in the linear terms that conditioning creates); the two contributions compose by (C1)-(C3).

The analytic ingredients for each branch are proved above; the missing pieces are (i) Fourier bounds uniform over the linear terms produced by conditioning on the hub coordinates, (ii) hubs with nonzero diagonal, or pairs of hubs with a nonzero hub block, coupled to a general remainder (the pure hub + rank-one case is Prop. 5.4), and (iii) the linear-algebra statement that every no-pivot matrix decomposes this way with universal constants.

## 6. Which tool handles which example

| Example | Structure | Tool | Bound |
|---|---|---|---|
| $\mathrm{diag}(\lambda_1,\lambda_2,\lambda_3,\dots)$ | separable | K1, or three 1x1 pivots | $\pi$ |
| $I-2ee^T$ ($n=3$) | all 2x2 blocks indefinite | 1x1 pivot $a_{11}=\frac13$, then indefinite 2x2 Schur complement | 18.8 |
| the $3\times3$ example | block $\{1,2\}$ singular | 1x1 pivot $a_{11}=\frac12$ (condition on $X_2,X_3$) | 15.4 |
| $2I-J$ ($n=3$) | all 2x2 blocks singular | 1x1 pivot, Schur complement $\begin{pmatrix}0&-2\\-2&0\end{pmatrix}$ | 10.9 |
| $-(J-I)$ ($n=3$) | zero diagonal | indefinite 2x2 pivot ($D=1$), $\kappa(X_3)=2X_3^2$ | 12.1 |
| $2(X_1X_2+X_3X_4)$ | two independent hyperbolic blocks | indefinite pivot $\{1,2\}$ then level-1 pivot $\{3,4\}$ | $K_3(1)\approx91$ |
| $\lambda X_1^2+2X_2X_3$ | diagonal + hyperbolic block | 1x1 pivot then 2x2 | $K_3$ |
| $2X_h\langle w,X\rangle+\lambda\langle v,X\rangle^2$, $w\perp v$ spread | hub + rank one; no pivot, $e_3\equiv0$ | Prop. 5.4 (2D projection bound) | 16.5 |
| $2X_{h_1}L_1+2X_{h_2}L_2+R$ | two hubs, anything else | Prop. 5.5 | $\frac12+8\sigma^{-2}$ |
| $X^TMX$, $M$ a normalized conference matrix | no pivot, spread | Fourier (Theorem D) | - |
| $|PX|^2$, $P$ rank 3, all leverages $\le\frac1{50}$ | no pivot, spread | Fourier via Prop. 4.2 | 40 |
| $|PX|^2$, one leverage $\ge\frac1{50}$, rest spread | PSD pivot + rank-2 spread | pivot + Fourier $e_2$ (needed) | open until Fourier $e_2$ |
| $aX_h^2+2X_hL+F(L,V)$, $a$ small $\ne0$ | hub with small diagonal + rank one | Prop. 5.4 (general $a$) | explicit |
| hub with small nonzero diagonal + a general remainder | no pivot | none of the above | OPEN |

## 7. Numerics (NUMERICAL; scripts in this folder, all run BelowNormal, each under 10 minutes)

All estimators below are exact conditional formulas averaged by Monte Carlo, not histograms, so they do not suffer from bin-width artefacts.

1. **The hyperbolic change of variables (n1_hyperbolic_check.py).** Formula (1.1) against a 4-million-sample Monte Carlo window estimate, for a rotated $B$ with eigenvalues $(2,-0.5)$ and a spread $W_2$: $\delta=0.3$: 0.1115 (MC) vs 0.1132 (formula); $\delta=-0.8$: 0 vs 0; $\delta=2.5$: 0.1769 vs 0.1783. (MC window $\pm0.01$ and sampling noise explain the $1\%$ gap.)
2. **Adversarial test of Lemma 1.4 (n2_hyperbolic_adversarial.py).** 30 random $B$ (rotation uniform, $|\mu_\pm|\in[e^{-3},e^3]$), random $\delta\in\pm[e^{-9},e^2]$; for each, sets $E_1,E_2$ of measure $\le1$ built greedily (unions of $5\cdot10^{-4}$ bins along the level curve, 10 Lagrangian weightings) to maximize the right side of (1.1). Worst ratio (adversarial density)/(proven bound) $=0.507$; the adversarial $t$-integral grows like $2\log\frac1{\Lambda|\delta|}+O(1)$, i.e. the coefficient of the logarithm in Lemma 1.4 is attained.
3. **n = 3 (n3_threedim_check.py).** Route-(i) estimator $p_Q(s)=E\big[\frac{f_1(m+r)+f_1(m-r)}{2\sqrt{|a|\,|s-R|}}\big]$, 40 configurations per matrix (uniform laws and random unions of 2-12 intervals spread over up to $\pm300$, random linear terms), coarse-to-fine scan in $s$: worst $\sup_sp_Q$ = **2.53** for $I-2ee^T$, **2.55** for the example of question (a); both attained by uniform laws with $b=0$ at $s\approx0$. Spread laws only lowered the density. (The run for $2I-J$ hit the time limit and is not reported.) Proven bound: 20.
4. **Constants (n4_constants.py).** $\int_0^\infty\min\{1,2v^{-2}(9.34+2\log_+v)\}dv=10.82$; route (i) $19.76$; route (ii) $19.12$ at $D=0.365$; $E\log_+\frac1{|X^2+h|}$ for uniform $X$ maximized over $h$: 3.39 (bound used: 4.08).
5. **Hubs (n5_hubs_check.py), 60 leaf coordinates, orthonormal random $w,v,u$, uniform laws.** $Q=2(L+\beta)X_h+\lambda V^2$: $\max_s p_Q\approx3.53$ ($\lambda=\pm1,\beta=0$), $2.68$ ($\beta=0.3$), $2.05$ ($\lambda=4$), against the proven $16.5$ and $8.5$. Two hubs with an arbitrary remainder $R=3U^2-2LV+0.7L$: $1.24$ against the proven $8.5$. (A run with spread leaf laws scanned the wrong range of $s$ and is not informative.)

6. **Hub + rank one with nonzero hub diagonal (n6_hub_diag_check.py; 19 of 20 configurations finished before the time limit on a loaded machine).** $Q=aX_h^2+2(L+\beta)X_h+\mu L^2+V^2$, $a\in\{0,0.01,0.1,0.5,-0.3\}$, $\mu\in\{0,0.5\}$, $\beta\in\{0,0.2\}$: $\max_sp_Q$ between $2.70$ and $3.63$, flat in $a$, as Prop. 5.4 predicts.

Consistency with COUNTEREXAMPLE_SEARCH.md: the worst value seen anywhere is still $\approx3\sqrt2$ (Gaussian limit of $(1,1,-1)$ with uniform inputs); at $n=3$ the extremal value is about $2.55$.

## 8. Gaps, audit, and what would change the picture

**Open (the complement is now narrow and explicit).**
1. *The no-pivot regime* (Theorem 5.2). Everything else reduces to it. Needed from the Fourier side: bounded density (3 large eigenvalues), $\sup_sE[|s-R|^{-1/2};|s-R|\le1]$ (2), $\sup_sE\log_+\frac1{|s-R|}$ (1), for matrices whose diagonal entries and $2\times2$ principal minors are all $<c$, **uniformly in the linear terms** (conditioning on pivot coordinates creates arbitrary linear terms, including directions outside the range of the matrix).
2. *Structure lemma (linear algebra).* Show that a no-pivot matrix with $k$ large eigenvalues is "hubs + spread part" in the sense of Section 5.3, with universal constants. The hypothesis of Theorem D (spread 3-volume of one off-diagonal block) fails for one hub + one delocalized rank-one direction (Section 5.2); that case is proved by Prop. 5.4, but only in its pure form (the rest of the form a function of the two projections $L,V$).
3. *Hubs with small nonzero diagonal.* Prop. 5.4 (hub + rank one) holds for any hub diagonal; Props 5.3 and 5.5 need the hub diagonal, resp. the hub-hub block, to vanish exactly. With $0<|a_{hh}|<c$ the small-ball function acquires a genuine $\sqrt{|a_{hh}|u}$ term (Remark 2 after Prop. 5.5), so a general composition must track the random centre $-L'^2/(4a_{hh})$ of that square-root singularity, as the change of variables in Prop. 5.4 does; for a remainder that depends on more than a fixed two-dimensional projection I have no proof.
4. *PSD rank 3 with one heavy coordinate*: reduces (Section 4) to the $e_2$-version of the Fourier bound for a rank-2 PSD form with linear terms outside its range; the elementary argument (2D projections have density $\le2$) does not cover those linear terms because of the mixed-norm problem (F2).
5. *Constants.* Proven: 20 at $n=3$ (true value $\approx2.55$), $K_3(c)$ in Theorem 3.1, $O(n\log n)$ in Theorem 3.2. No attempt at the sharp constant (the numerics still point to $3\sqrt2$ as the supremum over all $n$).

**Interpretation of Theorem D used here.** In Prop. 4.2 I took "volume-sampling marginal of $i\in I$" to mean $P(i\in S)$ under $P(S)\propto\det(G_{SS})$, $G=A_{IJ}A_{IJ}^T$, $|S|=3$, and "$\le1/2$" to be required on $I$ only. If the condition is read differently (both sides, or another normalization) Prop. 4.2 needs the corresponding one-line change; the matrix-Chernoff input is symmetric in $I,J$.

**Audit (each load-bearing step checked a second way).**
- Lemma 1.4: the Jacobian $1/(2\sqrt D)$ checked symbolically ($\cosh^2-\sinh^2$) and numerically against a 4-million-sample Monte Carlo (agreement to 1%); the bound checked against greedy adversarial sets (worst ratio 0.51); the log coefficient matched by the adversary, so the lemma is sharp in form. Strongest case against it: a set pattern that lets BOTH factors stay near 1 along a long arc. Impossible: on each tail one coordinate is monotone with $|w_i'|\ge|w_i|/3$, and that coordinate's unit mass caps the arc's $dt$-measure; the adversary confirms.
- Theorem 2.1: every constant recomputed by quadrature (n4_constants.py); the four hard matrices checked by an unbinned estimator with spread laws (max 2.55 vs 20). The Schur-complement facts ($|\sigma_k|\ge1$, $|\mathrm{eig}(A/a_{ii})|\ge1$) are the standard block-inverse identity plus $\|(A^{-1})_{PP}\|\le\|A^{-1}\|$.
- Lemma 1.5 for singular $A$: perturbation $(A+\varepsilon I)/(1-\varepsilon)$ keeps the count of eigenvalues of modulus $\ge1$, and the condition $|\nu|\ge1-O(\varepsilon)$ is closed.
- Theorem 5.2 necessity: the density of $4(U^2-V^2)$ for uniform $U,V$ is $\frac14p(z/4)$ with $p(z)=2\log\frac{\sqrt{1/4-|z|}+1/2}{\sqrt{|z|}}\ge\log\frac1{4|z|}$ for $|z|\le\frac18$.
- What would falsify the programme: a no-pivot matrix with three large eigenvalues and an unbounded density. The candidates I cannot rule out are hubs with a nonzero diagonal (or two hubs with a nonzero hub block) coupled to a remainder that is not a function of a fixed low-dimensional projection; every pure case I could reduce is bounded (Props 5.4, 5.5), and the numerics for hub + rank one give $\le3.7$ for every hub diagonal tried.
- Prop. 5.4: the change of variables $v\mapsto x$ was checked by rederiving it as the coarea identity $p_Q(s)=\iint f_h(x)\sum_{v}\rho_{LV}/|\partial_vF|\,d\ell\,dx$ (integrating the delta function in $v$), and the determinant $a\sigma_F-1$ was recomputed twice by expanding $ax^2-2rx-\sigma_F(r-ax)^2$.
