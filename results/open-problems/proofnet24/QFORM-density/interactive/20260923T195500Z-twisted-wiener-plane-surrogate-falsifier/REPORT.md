# A dependent-light falsifier for projection-cap and Wiener surrogates

**Status:** Rigorous obstruction to an abstract intermediate lemma. The light law below is dependent and is **not known** to be an orthogonal projection of independent cap-one original inputs. It does not refute the QFORM conjecture or the proposed twisted Wiener bound under genuine product provenance.

## Targeted abstract implication

For a probability density $g(l,v,p)$ on $\mathbb R^3$ define
\[
 F_{\tau,g}(y,z)=\int_{\mathbb R^3}
 g(l,v,p)e^{i(yl+zv+\tau lp)}\,dl\,dv\,dp,\qquad
 J_\tau(g)=\int_{\mathbb R^2}|F_{\tau,g}(y,z)|\,dy\,dz.
\]
Even the following simultaneous hypotheses do **not** imply a bound for $J_1(g)$:

1. Every orthogonal $d$-dimensional projection of $g$ has density at most $2^{d/2}$ for $d=1,2,3$.
2. For every **affine** two-dimensional plane $\Pi$ in frequency space, $\int_\Pi|\widehat g|\,d\mathcal H^2\le K$ with $K$ independent of the example.
3. $\int_{\mathbb R^3}|\widehat g|\le K$ with the same uniformity.

We construct smooth probability densities $g^{\star}_k$ satisfying all three conditions for a fixed finite $K$ but $J_1(g^{\star}_k)\to\infty$. In particular, adding full-dimensional Wiener control and all rotated two-dimensional Wiener restrictions to all-plane density caps still fails to replace the true independent-product structure.

## Construction and twisted growth

Choose one nonnegative $C_c^\infty(\mathbb R)$ probability density $h$ with $h>0$ near the origin and $\|h\|_\infty\le1$. Let $A=\widehat h$; choose the support small enough or simply restrict to a small central interval on which $h(l)|A(l)|>0$. Write $B=k^4$ and, for integers $k\ge k_0$, define
\[
 g_k(l,v,p)=h(l)h(v)\,\frac1k\sum_{j=1}^k h(p-kl-jB). \tag{1}
\]
This is a probability density: it is the law of
\[
 L\sim h,\quad V\sim h,\quad
 P=kL+JB+U,
\]
where $J$ is uniform on $\{1,\ldots,k\}$ and $L,V,U,J$ are independent. The observed $(L,P)$ are dependent.

At $\tau>0$ fixed, integration over $P$ gives
\[
 F_{\tau,g_k}(y,z)
 =A(z)\,\frac1k\sum_{j=1}^k T_{k,\tau}(y+\tau jB),
 \quad
 T_{k,\tau}(s)=\int_{\mathbb R} h(l)A(\tau l)
             e^{i\tau k l^2+isl}\,dl. \tag{2}
\]
For each fixed $\tau>0$, stationary phase at $l=-s/(2\tau k)$ on a central interval where $h(l)A(\tau l)$ is nonzero shows
\[
 |T_{k,\tau}(s)|\ge c_\tau k^{-1/2}
 \quad\text{for }|s|\le c'_\tau k,\quad k\text{ large}. \tag{3}
\]
This is the standard one-dimensional stationary-phase expansion with a smooth fixed amplitude; the leading coefficient is bounded away from zero on the selected interval, and the uniform error is $O_\tau(k^{-1})$. Hence $\int|T_{k,\tau}|\ge c_\tau\sqrt{k}$. If $|s|\ge 2\tau k\sup|\operatorname{supp}h|+1$, repeated integration by parts (the phase derivative is $s+2\tau kl$) gives rapid decay away from this $O_\tau(k)$ band. Since the packet centers in (2) are separated by $\tau B\gg_\tau k$, the other packets have negligible total contribution on each central band. Thus
\[
 J_\tau(g_k)\ge c_\tau\sqrt{k} \qquad(\tau>0\text{ fixed}). \tag{4}
\]

## All rotated density caps

The joint $(L,P)$ density in (1) is at most $\|h\|_\infty^2/k$, since the $jB$ translates are disjoint. The full three-dimensional density is at most $\|h\|_\infty^3/k$.

Every scalar unit projection $aL+bP+cV$ has density bounded by an absolute constant $C_1$ independent of $k$:

- If $|c|\ge1/4$, condition on $(L,P,J,U)$ and use the density cap of the independent $cV$.
- If $|c|<1/4$ and $|a+kb|\ge1/4$, use the independent $(a+kb)L$ term instead.
- Otherwise $|a+kb|<1/4$ and $a^2+b^2+c^2=1$ imply $1/(2k)\le|b|\le 5/(4k)$ for all sufficiently large $k$. The supports of the $k$ conditional $J$ components are disjoint: adjacent centers differ by $|b|B\ge k^3/2$, while the within-component support diameter of $(a+kb)L+bU+cV$ is bounded independently of $k$. Within one component, its weight is $1/k$ and the independent $bU$ density cap is at most $2k\|h\|_\infty$. So the mixture cap is at most $2\|h\|_\infty$.

Every orthogonal two-dimensional projection of $(L,P,V)$ has density bounded by another absolute constant $C_2$. To see this, let $n=(n_{LP},n_v)$ be its unit normal. If $|n_v|\ge1/2$, condition on $V$: the linear projection of the $(L,P)$ plane into the target plane has determinant $|n_v|$, so the joint $(L,P)$ density cap pays at most a factor two. If $|n_v|<1/2$, put $e=n_{LP}/|n_{LP}|$ and choose target-plane basis $(e^\perp,0)$ and $(n_v e,-|n_{LP}|)$. In this basis the projected variables are
\[
 Z_1=\langle e^\perp,(L,P)\rangle,\qquad
 Z_2=n_v\langle e,(L,P)\rangle-|n_{LP}|V.
\]
Condition on $(L,P)$, use $V$'s independent density cap, and integrate along $\langle e,(L,P)\rangle$. The result is at most $\|h\|_\infty\,\|p_{Z_1}\|_\infty/|n_{LP}|\le(2/\sqrt3)\|h\|_\infty C_1$. Thus $C_2$ is uniform in orientation. Denote the uniform three-dimensional cap by $C_3$.

## Every affine two-plane has bounded Wiener norm after a logarithmic weighting

The full characteristic function factors as
\[
 \widehat g_k(\eta,z,\xi)
 =A(\eta+k\xi)A(z)A(\xi)D_k(B\xi),
 \qquad D_k(t)=\frac1k\sum_{j=1}^ke^{ijt}. \tag{5}
\]
Since $|D_k|\le1$ and $A$ is Schwartz,
\[
 \|\widehat g_k\|_{L^1(\mathbb R^3)}\le\|A\|_1^3. \tag{6}
\]
The normalized Dirichlet kernel obeys
\[
 \int_\mathbb R |A(\xi)D_k(B\xi)|\,d\xi
 \le C_h\frac{\log(k+1)}k,\qquad B=k^4. \tag{7}
\]
Indeed its average absolute value on one $2\pi$ period is $O(\log(k+1)/k)$; partition the line into periods of length $2\pi/B$, use the Schwartz envelope of $A$, and bound the first and last partial periods by $O(1/B)$. This proves (7) uniformly in the relative phase of the period grid.

We now verify the supremum over **all affine plane positions and orientations**. Change frequency coordinates from $(\eta,\xi,z)$ to $(a,\xi,z)=(\eta+k\xi,\xi,z)$. The linear map $T$ has determinant one. If an original affine plane has unit normal $n$, its transformed plane has unit normal $m=T^{-T}n/|T^{-T}n|$, and its surface measure transforms by
\[
 d\mathcal H^2_{\rm original}
 =M^{-1}d\mathcal H^2_{\rm transformed},
 \qquad M=|T^{-T}n|,
 \qquad M^{-1}=|T^Tm|\le k|m_a|+2. \tag{8}
\]
If $|m_a|<1/k$, the Jacobian is at most three. For every affine plane in $(a,\xi,z)$, the integral of the separable Schwartz product $|A(a)A(\xi)A(z)|$ is uniformly bounded: solve for a coordinate whose normal component has modulus at least $1/\sqrt3$, bound its $A$ factor by $\|A\|_\infty$, and integrate the other two $A$ factors. Since $|D_k|\le1$, this branch is $O_h(1)$.

If $|m_a|\ge1/k$, solve the affine plane equation for $a$ as a function of $(\xi,z)$. Its surface Jacobian is $1/|m_a|$, while $|A(a)|\le\|A\|_\infty$. Equations (7)--(8) bound this branch by
\[
 \frac{k|m_a|+2}{|m_a|}\,
 \|A\|_\infty\|A\|_1\,
 C_h\frac{\log(k+1)}k
 \le C'_h\log(k+1). \tag{9}
\]
No step depends on the affine offset. Thus
\[
 \sup_{\Pi\ {\rm affine\ 2\!-\!plane}}
 \int_\Pi|\widehat g_k|\,d\mathcal H^2
 \le C'_h\log(k+1). \tag{10}
\]

## Fixed normalization and final probability family

Choose one fixed dilation factor $D\ge1$ large enough that the law $\widetilde g_k(y)=D^{-3}g_k(y/D)$ has **all** its orthogonal $d$-projection density caps at most $2^{d/2}/2$ for $d=1,2,3$. This is possible uniformly in $k$ by the constants $C_1,C_2,C_3$ above, since a $d$-projection density scales by $D^{-d}$. Choose one fixed sufficiently broad isotropic Gaussian probability density $g_0$ whose corresponding projection caps are also at most $2^{d/2}/2$. Put
\[
 \alpha_k=\frac1{1+\log(k+1)},\qquad
 g_k^\star=\alpha_k\widetilde g_k+(1-\alpha_k)g_0. \tag{11}
\]
The projection-density caps of $g_k^\star$ are at most $2^{d/2}$ (in fact one half those values). Dilation changes the two-plane Fourier area by $D^{-2}$ and the three-dimensional Fourier volume by $D^{-3}$; (6), (10), and (11) give **uniform** full and every-affine-two-plane Wiener constants. The Gaussian has uniform finite constants on all affine planes.

Finally $F_{1,\widetilde g_k}(y,z)=F_{D^2,g_k}(Dy,Dz)$, so $J_1(\widetilde g_k)=D^{-2}J_{D^2}(g_k)\ge c_D\sqrt{k}$ by (4). The Gaussian has finite $J_1(g_0)$. The reverse triangle inequality in $L^1(\mathbb R^2)$ gives
\[
 J_1(g_k^\star)
 \ge\alpha_k J_1(\widetilde g_k)-(1-\alpha_k)J_1(g_0)
 \ge c_D\frac{\sqrt{k}}{1+\log(k+1)}-J_1(g_0)
 \longrightarrow\infty. \tag{12}
\]

## Scope

The shared categorical label $J$ in $P=kL+JB+U$ creates dependence between $L$ and $P$. No construction here realizes $g_k^\star$ as the orthogonal projection of independent cap-one coordinates in a three-frame with row leverage at most $1/2$. Therefore (12) defeats only the stated abstract surrogate. A genuine-product twisted Wiener bound remains a separate open step; proving it must use an invariant stronger than all the projection-density and Fourier-plane bounds above.


## Even two bounded-density 3D convolution banks do not suffice

The unweighted law $g_k$ in (1) already has $\|g_k\|_\infty\le C/k$. Let two independent light vectors have this same 3D density and put $\bar g_k=g_k*g_k$. Then $\bar g_k$ is the convolution of **two independent full-dimensional 3D densities**, each uniformly bounded, but the twisting problem persists. Explicitly, with independent copies,
\[
 \bar L=L_1+L_2,\quad \bar V=V_1+V_2,\quad
 \bar P=k\bar L+B(J_1+J_2)+(U_1+U_2).
\]
The label sum $M=J_1+J_2$ has nonnegative triangular weights $w_m$ with $\sum_mw_m=1$. The twisted $(\bar L,\bar V)$ density after integrating $\bar P$ has factor
\[
 a(l)e^{ikl^2}\sum_m w_m e^{imBl},
 \qquad a(l)=(h*h)(l)\widehat{h*h}(l),
\]
up to the separate $(h*h)(v)$ factor. For the same stationary-phase reason as (3), every $m$ contributes a Fourier packet of $L^1$ norm at least $c\sqrt{k}$. Their centers are $B$ apart, so their weighted sum has $L^1$ norm at least $c\sqrt{k}\sum_mw_m=c\sqrt{k}$. Therefore $J_1(\bar g_k)\ge c\sqrt{k}$. This convolution fact alone is not the product-projection representation required by the conjecture: the individual 3D banks themselves contain the dependent shared-label construction.
