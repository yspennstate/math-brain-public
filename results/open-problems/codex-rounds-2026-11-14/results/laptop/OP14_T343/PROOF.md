# Exact sphere slopes for orthogonal group interpolation

Write \(\sigma(t)=\max(t,0)\). Sections 1–6 use **Euclidean chord distance** on the sphere. Section 7 explicitly introduces geodesic distance and computes its exact Lipschitz constant, thereby also giving a sharp local lower bound for the chord constant.

**Main additional result:** the finite formula and closed forms in Section 7, together with the exact ball formula (14). The broad order-of-growth grouping obstruction is already recorded in the internal note `t343_grouping_interpolator_lip_is_n_over_k_not_sqrt_2026_10_31.md`; Sections 1–5 give a self-contained quantitative version with explicit constants, rather than a claim of a new obstruction.

The result concerns a particular construction. It does not give a lower bound for every network interpolating the same data.

## 1. The construction and the random-data theorem

Let \(x_1,\ldots,x_n\) be independent uniform points of \(S^{d-1}\). Fix a partition into nonempty groups \(G_1,\ldots,G_K\), with sizes \(s_j\le m\), and assign the common label \(\xi_j\in\{-1,1\}\) to group \(j\). The partition and signs are independent of the points. Define

\[
 X_j=(x_i^T)_{i\in G_j},\qquad
 w_j=X_j^T(X_jX_j^T)^{-1}{\bf1}_{s_j},\qquad
 F(x)=2\sum_{j=1}^K\xi_j\sigma(w_j^Tx-1/2).
\tag{1}
\]

Assume \(m\ge8\), \(d\ge m+1\), and at least \(2r\) groups have size exactly \(m\), where \(r=\lfloor m/8\rfloor\). Set

\[
 \Delta=2(K+1)9^m e^{-d/512}
       +2K(n+1)e^{-3d/(40m)}.
\tag{2}
\]

**Theorem.** With probability at least \(1-\Delta\), (1) is defined, interpolates every label, and

\[
 \operatorname{Lip}_{S^{d-1}}(F)\ge\sqrt{mr}\ge m/4.
\tag{3}
\]

In particular a sufficient condition for probability at least \(1-\delta\), for \(0<\delta<1\), is

\[
 d\ge512\bigl(m\log9+\log(4(K+1)/\delta)\bigr),\qquad
 d\ge\frac{40m}{3}\log\frac{4K(n+1)}{\delta}.
\tag{4}
\]

All logarithms are natural. Large constants in (4) are chosen for an elementary proof.

## 2. Two probability estimates

### 2.1 A Gram matrix estimate

If \(u_1,\ldots,u_q\) are independent uniform sphere points and \(U\) has these columns, then

\[
 \mathbb P\left\{\frac35 I_q\npreceq U^TU
                 \text{ or }U^TU\npreceq\frac53 I_q\right\}
 \le2\,9^q e^{-d/512}.
\tag{5}
\]

Here is a derivation. Let \(Z\) have independent \(N(0,1/d)\) entries. For each fixed unit \(a\in\mathbb R^q\), \(d\|Za\|^2\) is chi-squared with \(d\) degrees of freedom. Its moment generating function is \((1-2\lambda)^{-d/2}\). Chernoff's inequality gives, for \(0<t<1\), upper and lower tail bounds with exponents

\[
 -\frac d2(t-\log(1+t)),\qquad
 -\frac d2(-t-\log(1-t)).
\]

The inequalities \(t-\log(1+t)\ge t^2/4\) and \(-t-\log(1-t)\ge t^2/2\) follow by differentiation, starting at \(t=0\). Hence

\[
 \mathbb P\{|\|Za\|^2-1|>t\}\le2e^{-dt^2/8}.
\]

A maximal \(1/4\)-separated subset of the unit sphere in \(\mathbb R^q\) is a \(1/4\)-net of size at most \(9^q\): disjoint balls of radius \(1/8\) around its points fit inside a ball of radius \(9/8\). For a symmetric matrix \(A\), approximation of a maximizing unit vector by this net gives

\[
 \|A\|_{\rm op}\le2\max_{a\text{ in the net}}|a^TAa|,
\]

because \(|x^TAx-a^TAa|\le2\|A\|_{\rm op}\|x-a\|\). Apply the chi-squared bound with \(t=1/8\) and take a union bound. Except on probability \(2\,9^q e^{-d/512}\),

\[
 \tfrac34 I\preceq Z^TZ\preceq\tfrac54 I.
\]

Normalize the columns of \(Z\). If \(D\) is the diagonal matrix of their norms, then \(U=ZD^{-1}\) has the required independent uniform columns, and \(\tfrac34 I\preceq D^2\preceq\tfrac54 I\). For every \(a\),

\[
 \tfrac34\|D^{-1}a\|^2\le\|Ua\|^2\le\tfrac54\|D^{-1}a\|^2.
\]

Bounding \(D^{-2}\) gives the constants \(3/5\) and \(5/3\) in (5).

### 2.2 A spherical tail estimate

For a uniform \(u\in S^{d-1}\), fixed unit \(v\), and \(a>0\),

\[
 \mathbb P\{|u^Tv|\ge a\}\le2e^{-da^2/2}.
\tag{6}
\]

Indeed, rotational invariance reduces to the first coordinate. Polar integration of a standard Gaussian gives

\[
 \mathbb E u_1^{2\ell}
 =\frac{1\cdot3\cdots(2\ell-1)}{d(d+2)\cdots(d+2\ell-2)}
 \le\frac{(2\ell-1)!!}{d^\ell},
 \qquad \mathbb E u_1^{2\ell+1}=0.
\]

For completeness, the identity follows from independence of Gaussian radius and direction: \(\mathbb E g_1^{2\ell}=(2\ell-1)!!\), while \(\mathbb E\|g\|^{2\ell}=d(d+2)\cdots(d+2\ell-2)\), obtained by differentiating \((1-2\lambda)^{-d/2}\). The exponential series consequently gives \(\mathbb E e^{\lambda u_1}\le e^{\lambda^2/(2d)}\). Chernoff's inequality, optimized at \(\lambda=da\), and the same bound for \(-u_1\), prove (6).

If a rotationally invariant random vector \(w\) has \(\|w\|^2\le5m/3\), its direction is uniform and independent of its radius. Thus for any independent random unit vector \(v\),

\[
 \mathbb P\{|w^Tv|\ge1/2,\ \|w\|^2\le5m/3\}
 \le2e^{-3d/(40m)}.
\tag{7}
\]

The same estimate holds if \(w\) is arbitrary and \(v\) is an independent uniform sphere point, by conditioning on \(w\). In either case substitute \(a=(1/2)/\sqrt{5m/3}\) in (6).

## 3. Interpolation and the witness point

Apply (5) to every group. Outside an event of probability at most \(2K9^m e^{-d/512}\), every group Gram matrix has eigenvalues in \([3/5,5/3]\). Denote this event of simultaneous success by \(E\). On \(E\),

\[
 w_j^Tx_i=1\ (i\in G_j),\qquad
 \frac35s_j\le\|w_j\|^2
 ={f1}_{s_j}^T(X_jX_j^T)^{-1}{\bf1}_{s_j}
 \le\frac53s_j\le\frac53m.
\tag{8}
\]

For \(i\notin G_j\), the point \(x_i\) is independent of \(w_j\). Applying (7) and a union bound over the at most \(Kn\) pairs shows that, except on probability \(2Kn e^{-3d/(40m)}\), no such pair has \(|w_j^Tx_i|\ge1/2\) together with the norm bound in (8). Combined with \(E\), this means only the point's own group contributes in (1). Its contribution is \(2\xi_j(1-1/2)=\xi_j\), proving interpolation.

Among the full groups, choose a set \(A\) of \(r\) groups of a common sign \(\xi\). Such a set exists by the pigeonhole principle; choose it from the partition and labels alone. The normals from distinct groups are independent and rotationally invariant, since the minimum-norm formula in (1) commutes with orthogonal transformations. They are nonzero almost surely; their directions are independent uniform sphere points, independent of their individual radii. Rank failures have probability zero because each group has at most \(m<d\) independent continuous sphere samples.

Let \(W\) be the \(r\)-by-\(d\) matrix with rows \(w_j^T\), \(j\in A\). Apply (5) to these directions. Except on an additional event of probability \(2\,9^r e^{-d/512}\), (8) and the direction estimate give

\[
 \frac9{25}m I_r\preceq WW^T\preceq\frac{25}9m I_r,
 \quad\hbox{and hence}\quad
 \frac m3 I_r\preceq WW^T\preceq3m I_r.
\tag{9}
\]

For example, writing \(WW^T=D U^TU D\), with the selected norms on the diagonal of \(D\), proves both inequalities directly from quadratic forms. Independence of the events in this argument is unnecessary: their failure probabilities are simply added.

Put \(t=3/4\) and

\[
 x_0=W^T(WW^T)^{-1}t{\bf1}_r.
\]

Then \(Wx_0=t{\bf1}_r\), and (9) gives

\[
 \|x_0\|^2=t^2{\bf1}_r^T(WW^T)^{-1}{\bf1}_r
 \le\frac{27r}{16m}\le\frac{27}{128}<1.
\tag{10}
\]

Choose a unit \(z\in\ker W\) by a fixed measurable rule depending only on \(W\), for example by projecting the coordinate vectors in order and normalizing the first nonzero projection. This is possible since \(d>r\). Set

\[
 x=x_0+\sqrt{1-\|x_0\|^2}\,z.
\tag{11}
\]

Since \(x_0\) belongs to the row span of \(W\), it is orthogonal to \(z\). Therefore \(\|x\|=1\) and \(w_j^Tx=3/4\) for every \(j\in A\). To apply probability estimates, define \(x\) to be a fixed unit vector on selected-group outcomes where (9)–(10) fail. This defines a unit vector everywhere, using only the selected groups.

Each unselected normal is independent of \(x\). Thus (7) and a union bound imply that, except on probability \(2(K-r)e^{-3d/(40m)}\), all unselected groups satisfy \(|w_j^Tx|<1/2\) on \(E\). No conditioning on the interpolation event is used. On the intersection of all the success events, precisely the groups in \(A\) are active at \(x\), with strict margins.

## 4. The tangential slope

In a neighborhood of this witness the ambient gradient is

\[
 g=2\xi W^T{\bf1}_r.
\]

By (9), \(\|g\|^2\ge(4/3)mr\). By the prescribed preactivations,

\[
 g^Tx=2\xi rt=\tfrac32\xi r.
\]

Consequently its tangent projection \(g_T=g-(g^Tx)x\) satisfies

\[
 \|g_T\|^2=\|g\|^2-(g^Tx)^2
 \ge\tfrac43mr-\tfrac94r^2
 \ge\left(\tfrac43-\tfrac9{32}\right)mr
 =\tfrac{101}{96}mr\ge mr.
\tag{12}
\]

For a unit tangent vector \(v=g_T/\|g_T\|\), the curve \(\gamma(h)=\cos(h)x+\sin(h)v\) lies on the sphere, has \(\gamma'(0)=v\), and satisfies \(\|\gamma(h)-x\|/|h|\to1\). Strict activation margins ensure that \((F\circ\gamma)'(0)=g^Tv=\|g_T\|\). The chord Lipschitz constant is therefore at least \(\|g_T\|\).

For \(m\ge8\), the number \(m/8\ge1\) satisfies \(\lfloor m/8\rfloor\ge m/16\). Hence \(\sqrt{mr}\ge m/4\). Adding the four failure bounds in Sections 3–4 and using \(r\le m\) yields (2). Each of the two terms in (2) is at most \(\delta/2\) under (4). This proves the theorem.

## 5. Independent binary labels and the width range

The theorem also applies conditionally on independent binary labels: group each sign separately into full groups of size \(m\), followed by at most one nonempty remainder group of each sign. The partition depends only on labels and thus remains independent of the points.

If the two label counts are \(n_+,n_-\), the number of full groups is

\[
 \lfloor n_+/m\rfloor+\lfloor n_-/m\rfloor
 \ge\lfloor n/m\rfloor-1.
\]

Thus \(n\ge m(2\lfloor m/8\rfloor+1)\) guarantees the required \(2r\) full groups for every labeling. The resulting width satisfies \(n/m\le K<n/m+2\). For a probability bound uniform over label outcomes, replace \(K\) in (2) or (4) by \(\lceil n/m\rceil+2\).

Along sequences with \(m\to\infty\), \(n/m\to\infty\), this construction's sphere Lipschitz constant is at least \(m/4\), whereas \(\sqrt{n/K}\le\sqrt m\). Therefore its ratio to the desired scale diverges at least as \(\sqrt m/4\), with probability tending to one whenever (2) tends to zero. These parameter sequences are compatible with \(n\) polynomial in \(d\), for example \(n=m^2\), \(d=m^3\). This prevents the desired bound from being obtained by a sharper analysis of this **fixed construction** in this regime. Different group choices depending on the points, different biases, and different interpolants are not covered.

## 6. An exactly computable orthogonal case

There is a second derivation without probability estimates. Let the samples be orthonormal, with \(n=Km\), \(d\ge n\), equal group sizes \(m\ge2\), and arbitrary group signs. Then \(w_j=\sum_{i\in G_j}x_i\), so \(u_j=w_j/\sqrt m\) are orthonormal. Formula (1) becomes

\[
 F(x)=2\sqrt m\sum_{j=1}^K\xi_j\sigma(u_j^Tx-1/(2\sqrt m)).
\tag{13}
\]

Its exact Lipschitz constant on the closed unit ball is

\[
 \operatorname{Lip}_{B_2^d}(F)
 =2\sqrt{m\min(K,4m-1)}.
\tag{14}
\]

To see the upper bound, if \(a\) groups are strictly active at a point of the ball, Bessel's inequality gives

\[
 1\ge\sum_{j\text{ active}}(u_j^Tx)^2>a/(4m),
\]

so the integer \(a\le\min(K,4m-1)\). The gradient there has squared norm \(4ma\). On any line segment in the ball, (13) is piecewise affine. On each open piece its directional derivative is bounded by this gradient bound; units that are identically at a kink along the segment contribute zero. Integrating along the segment proves the upper bound even at nondifferentiable endpoints.

For the reverse inequality take \(a=\min(K,4m-1)\) and choose \(c>1/(2\sqrt m)\) with \(ac^2<1\), possible since \(a<4m\). At \(x=c\sum_{j=1}^a u_j\), precisely those groups are active, and the point is in the interior of the ball. A sufficiently short line in the gradient direction attains the slope \(2\sqrt{ma}\), proving equality.

If \(K\ge2m\), choose \(m\) groups of a common sign. Since \(d\ge Km>K\), choose a unit \(z\) orthogonal to all \(u_j\). For \(0<\varepsilon<1/2\) set

\[
 x_\varepsilon=\frac{1/2+\varepsilon}{\sqrt m}
                 \sum_{j\text{ selected}}u_j
       +\sqrt{1-(1/2+\varepsilon)^2}\,z.
\]

This is a unit vector with just the selected groups active. Its gradient has squared norm \(4m^2\) and squared radial component \(m^2(1+2\varepsilon)^2\). Letting \(\varepsilon\downarrow0\), the tangential argument used in Section 4 gives

\[
 \sqrt3\,m\le\operatorname{Lip}_{S^{d-1}}(F)
 \le\operatorname{Lip}_{B_2^d}(F)\le4m.
\tag{15}
\]

In contrast, on all of \(\mathbb R^d\), every group can be active simultaneously, and the exact constant is \(2\sqrt{mK}\). Thus ball, sphere, and whole-space constants must not be interchanged.

## 7. Exact geodesic constant for every sign count

Consider (13), with \(m\ge2\), \(K\ge1\), and \(d>K\). These assumptions hold for the orthogonal samples in Section 6. Let \(K_+\) and \(K_-\) be the numbers of positive and negative signs, with \(K_++K_-=K\). Define geodesic distance by \(d_g(x,y)=\arccos(x^Ty)\) on the unit sphere, and let \(L_g\) be the Lipschitz constant for that distance.

For integers \(0\le p\le K_+\), \(0\le q\le K_-\), with \(1\le r=p+q\le4m-1\), put \(P=\max(p,q)\), \(Q=\min(p,q)\), and

\[
 H_m(p,q)=4mr-
    \left[\max\{0,P-\sqrt{Q(4m-P)}\}\right]^2.
\tag{16}
\]

**Exact formula.**

\[
 L_g^2=\max_{\substack{0\le p\le K_+,\ 0\le q\le K_-\\
                      1\le p+q\le4m-1}} H_m(p,q).
\tag{17}
\]

This is a finite maximization over at most \((K_++1)(K_-+1)\) pairs, with no continuous optimization remaining. For the chord constant \(L_c\),

\[
 L_g\le L_c\le
 \min\left\{\frac\pi2 L_g,\ 2\sqrt{m\min(K,4m-1)}\right\}.
\tag{18}
\]

### 7.1 Minimizing the radial component

At a point with precisely \(p\) positive and \(q\) negative active groups, write their coordinates as \(t_i=u_i^Tx>a\), where \(a=1/(2\sqrt m)\). The gradient has squared norm \(4mr\), and its radial component is

\[
 2\sqrt m\left(\sum_{i\text{ positive}}t_i
                    -\sum_{i\text{ negative}}t_i\right).
\]

The squared tangent norm is therefore \(4mr\) minus the square of this radial component. The active coordinates must satisfy \(\sum t_i^2\le1\). Conversely, any strictly active coordinates of squared norm less than one are realized on the sphere by setting every inactive coordinate to zero and filling the remaining norm in a direction orthogonal to all \(u_j\). The assumption \(d>K\) supplies that direction.

Swap the sign classes if necessary, so \(P\ge Q\). Work first with the closure \(t_i\ge a\), \(\sum t_i^2\le1\). If \(Q=0\), the minimum absolute signed sum is \(Pa\), obtained by setting every active coordinate to \(a\). Assume henceforth \(Q>0\). Let \(U\) be the sum of the \(P\) coordinates and \(V\) the sum of the \(Q\) coordinates. Cauchy–Schwarz gives

\[
 U\ge Pa,\quad V\ge Qa,\quad
 \frac{U^2}{P}+\frac{V^2}{Q}\le1.
\tag{19}
\]

These conditions are also sufficient: assign all coordinates within each sign class their class average. They are at least \(a\), and their total squared norm is the last expression in (19).

If \(Pa\le\sqrt{Q(1-Pa^2)}\), set the \(P\) coordinates to \(a\) and the \(Q\) coordinates to \(Pa/Q\). Their signed sum is zero, and their squared norm is

\[
 Pa^2+P^2a^2/Q\le1.
\]

The last inequality is precisely the displayed condition squared and rearranged. Thus the minimum absolute signed sum is zero in this case.

Otherwise, for every feasible \(U,V\), (19) implies

\[
 U-V\ge U-\sqrt{Q(1-U^2/P)}
       \ge Pa-\sqrt{Q(1-Pa^2)}>0.
\tag{20}
\]

The second inequality holds because the function of \(U\) preceding it is increasing: its derivative is \(1+\sqrt Q\,U/(P\sqrt{1-U^2/P})>0\) in the interior, and continuity treats the endpoint. Equality is realized by taking the \(P\) coordinates equal to \(a\), and the \(Q\) coordinates equal to \(\sqrt{(1-Pa^2)/Q}\). This latter value exceeds \(a\), because \(ra^2<1\).

In both cases, including \(Q=0\), the minimum absolute signed sum is

\[
 M=\max\{0,Pa-\sqrt{Q(1-Pa^2)}\}.
\tag{21}
\]

The equality may lie on an activation boundary or on the boundary of the coordinate ball. This does not change the supremum over strictly active sphere points. To verify this, choose \(b\) strictly between \(a\) and \(1/\sqrt r\). The vector of \(r\) coordinates all equal to \(b\) is strictly feasible with squared norm less than one. Convex combinations of this vector with any minimizing vector in (21) are strictly active, have norm less than one, and tend to the minimizing vector. Complete them to sphere points in the orthogonal complement as above. At these points all inactive coordinates are zero. Thus the supremum of squared tangent norms on this activation pattern is exactly

\[
 4mr-4mM^2=H_m(p,q),
\]

which proves the claimed expression for each feasible pair. Every such pair is available by selecting the requisite numbers of the two signs; no pattern with \(r\ge4m\) is available by the strict Bessel bound in Section 6.

### 7.2 From local slopes to the two distances

Let \(L_*\) be the square root of the maximum in (17). Tangential differentiation along unit-speed sphere curves at strictly active points, and the approximating points just constructed, gives \(L_g\ge L_*\) and \(L_c\ge L_*\).

Conversely join two sphere points by a shortest unit-speed great-circle arc. Each preactivation along the arc is of the form \(A\cos s+B\sin s-a\). Since \(a>0\), it cannot vanish identically on an interval; it has finitely many zeros along this arc. Between these zeros the function is differentiable along the arc and its derivative has absolute value at most the corresponding tangent-gradient norm, hence at most \(L_*\). Integrating on the finitely many pieces gives \(|F(x)-F(y)|\le L_*d_g(x,y)\). This proves (17), including antipodal endpoints, where any shortest great circle can be used.

For \(0\le\theta\le\pi\), the chord length is \(2\sin(\theta/2)\), and \(\theta\le(\pi/2)\,2\sin(\theta/2)\). This follows from concavity of sine on \([0,\pi/2]\), which gives \(\sin t\ge2t/\pi\). Hence \(L_c\le(\pi/2)L_g\). Restricting the ball bound (14) to the sphere gives the other upper bound in (18).

### 7.3 Two closed forms

If all \(K\) signs agree, every available pair has one coordinate zero. Then \(H_m(p,0)=4mp-p^2\). This quadratic increases up to \(p=2m\) and decreases afterwards. With \(s=\min(K,2m)\),

\[
 L_g^2=4ms-s^2.
\tag{22}
\]

In particular \(L_g=2m\) for all \(K\ge2m\).

If there are at least \(2m\) groups of one sign and \(2m-1\) of the other, then

\[
 L_g^2=4m(4m-1)
       -\left(2m-\sqrt{2m(2m-1)}\right)^2.
\tag{23}
\]

Indeed, any pattern with \(r\le4m-2\) has \(H_m(p,q)\le4m(4m-2)\). For \(r=4m-1\), the smallest possible larger class is \(P=2m\), with \(Q=2m-1\), which is available under the hypothesis. With \(r\) fixed, the expression

\[
 P-\sqrt{(r-P)(4m-P)}
\]

increases as \(P\) increases: \(P\) increases while both nonnegative factors in the square root decrease. Its nonnegative part therefore has its smallest value at the most balanced available pattern. At \(P=2m,Q=2m-1\), the difference is positive and less than one, because

\[
 2m-\sqrt{2m(2m-1)}
 =\frac{2m}{2m+\sqrt{2m(2m-1)}}<1.
\]

Consequently this pattern gives \(H_m>4m(4m-1)-1>4m(4m-2)\), proving global optimality and (23). Its geodesic constant divided by \(4m\) tends to one as \(m\to\infty\), whereas (22) gives \(2m\) with all signs equal. The exact formula quantifies the effect of sign counts on worst sphere slopes; it does not claim either closed form is the exact chord constant.

## Scope and source

The construction (1) is the grouping construction in Appendix C of Sébastien Bubeck, Yuanzhi Li, Dheeraj Nagaraj, *A Law of Robustness for Two-Layers Neural Networks*, [COLT 2021](https://proceedings.mlr.press/v134/bubeck21a/bubeck21a.pdf), [arXiv:2009.14444](https://arxiv.org/abs/2009.14444). The probability estimates and the obstruction proved here are self-contained. No novelty claim is made. The full achievability conjecture and the behavior of gradient descent remain unresolved by this result.
