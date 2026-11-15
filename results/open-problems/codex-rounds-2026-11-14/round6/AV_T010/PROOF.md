# The conditional jitter-success lemma

The manuscript is OpenAI, *Pure-Point Spectrum for the Two-Dimensional Anderson Model at Every Positive Disorder*, September 23, 2026. The calculation below verifies the local numerator estimate `trans:jitter-success` on a regular zero-jitter datum. It does not establish that regular boundary data carry the required transmission weight.

Sources are [transmission.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/transmission.tex), especially `trans:rootless-fields` through `trans:jitter-success`, and [resonant.tex](https://raw.githubusercontent.com/openai/math/main/preprints/Pure-Point-Spectrum-for-the-Two-Dimensional-Anderson-Model-at-Every-Positive-Disorder-September-23-2026/build/sections/resonant.tex), especially `cell:sets`, `cell:profile-size`, `cell:interior-sampler`, `cell:jitter-widths`, and `cell:residual`. These are mutable main-branch sources opened November 15, 2026.

## 1. Assumptions and conclusion

Fix the clipped square

\[
 V=\{-L,\ldots,L\}^2\setminus\{(\pm L,\pm L)\},\qquad
 J=V\setminus\{0\},\qquad \epsilon=e^{-\nu L},\quad \nu>0.
\]

Let B be the exterior nearest-neighbor boundary, M the adjacency map from the projected boundary space P to J, and p the adjacency column from 0 to J. In particular, \(\|M\|\le\sqrt3\), its least singular value is at least 1, and M has nonzero rows only on the outer layer Z. Put \(Z^+=\{x\in J:\operatorname{dist}_1(x,Z)\le1\}\).

Fix the boundary matrix \(\widehat T\), source \(\widehat k\), and real common shift r. The boundary matrix is complex symmetric and passive, meaning \(-\operatorname{Im}\widehat T\ge0\). Define

\[
 A=\operatorname{Adj}_J+\operatorname{diag}(v-E),\quad
 H=\begin{pmatrix}A&M\\M^\top&\widehat T\end{pmatrix},\quad
 R=H^{-1},\quad \Gamma=R_{JJ},\quad
 z=R_{JP}\widehat k,\quad U=\Gamma p/\epsilon,\quad F=p^\top z/\epsilon.
\]

At zero jitters assume the inverses in

\[
 \|A^{-1}\|+\|\widehat T^{-1}\|
       +\|(\widehat T-M^\top A^{-1}M)^{-1}\|\le C L^q       \tag{1}
\]

exist, for fixed C,q independent of the exterior. These are the good-boundary and regular-r hypotheses, not conclusions here. Assume also the branch profile estimates, uniformly over all allowed jitters:

\[
 c e^{-\nu|x|_\infty}\le|\psi_x|\le C e^{-\nu|x|_\infty},
 \qquad \|-A^{-1}p-\psi\|\le C L^{q_0}\epsilon,
 \qquad \|A^{-1}\|\le C L^{q_0}.                         \tag{2}
\]

The exponents in (1)–(2) are fixed before the shell-depth parameter D2. This order matters. The source normalization is

\[
 k_*=(\widehat T-iI)^{-1}\widehat k,\qquad \rho=\|k_*\|^2.
\]

The independent jitter at x has half-width w=L^{-D3} if
\(L-|x|_\infty\le D2\log L+5\), and half-width \(\epsilon w\) otherwise. Choose D2 sufficiently large using the exponents in (1)–(2), then D3 sufficiently large using those exponents and D2.

**Conditional lemma.** For all sufficiently large L, uniformly in fixed boundary/r data satisfying (1),

\[
 \mathbb P_{\rm jitters}\{|F|\ge e^{-C_1(\log L)^2}\sqrt\rho\}
       \ge e^{-C_2(1+\log L)}.                            \tag{3}
\]

The constants are allowed to depend on the fixed branch parameters. No bound on \(\|\widehat T\|\) or \(\|\widehat k\|\) is assumed. If \(\rho=0\), (3) holds immediately with the non-strict threshold 0, so below assume \(\rho>0\).

## 2. Source size and an initial component

Write \(\mathcal B=\widehat T-M^\top A^{-1}M\), \(C_e=\widehat T-iI\), and \(\Delta=\mathcal B-C_e=iI-M^\top A^{-1}M\). Block inversion gives

\[
 R_{PP}=\mathcal B^{-1},\quad R_{JP}=-A^{-1}M\mathcal B^{-1},
 \quad \Gamma=A^{-1}+A^{-1}M\mathcal B^{-1}M^\top A^{-1}. \tag{4}
\]

Thus R and \(\Gamma\) have polynomial norm at zero jitters. Also
\(\Gamma^{-1}=A-M\widehat T^{-1}M^\top\) has polynomial norm.

Passivity gives \(\|C_e^{-1}\|\le1\): for any x,
\(\|C_e x\|\|x\|\ge|x^*C_e x|\ge-\operatorname{Im}(x^*C_e x)\ge\|x\|^2\).
Put \(b_0=\mathcal B^{-1}\widehat k\). Direct multiplication yields both identities

\[
 b_0=(I-\mathcal B^{-1}\Delta)k_*,\qquad
 k_*=(I+C_e^{-1}\Delta)b_0.
\]

All factors except the displayed vectors are polynomially bounded, so

\[
 L^{-q_1}\sqrt\rho\le\|b_0\|\le C L^{q_1}\sqrt\rho,
 \qquad \|z\|\le C L^{q_1}\sqrt\rho.                    \tag{5}
\]

Here and below increasing exponents absorbs fixed constants. The J rows of the source equation give \(Az=-Mb_0\). On Z, each row of A uses only coordinates of \(Z^+\), with bounded diagonal and degree at most four. The restricted operator norm is bounded by a constant depending only on h,E. Therefore

\[
 \|b_0\|\le\|Mb_0\|=\|(Az)_Z\|\le C\|z_{Z^+}\|.
\]

There are O(L) sites in \(Z^+\), so at least one fixed zero-jitter site \(j_0\in Z^+\) has

\[
 |z_{j_0}|\ge a_0\sqrt\rho,\qquad a_0\ge L^{-q_2}.       \tag{6}
\]

Use a deterministic tie rule to choose this site. In particular, it is chosen before exposing any jitters.

## 3. A terminal component uniform over the jitters

The trace of the profile on Z has norm at most \(C\sqrt L\epsilon\). By (2) and the support of M,

\[
 \|M^\top A^{-1}p/\epsilon\|\le C L^{q_3}.              \tag{7}
\]

Combining (4) and (7),

\[
 U=A^{-1}p/\epsilon+
        A^{-1}M\mathcal B^{-1}M^\top A^{-1}p/\epsilon.    \tag{8}
\]

The second term is polynomially bounded, with exponent fixed before D2. Equation (2) says that the first term is \(-\psi/\epsilon\) plus another such polynomial error. Let \(d=\lfloor D2\log L\rfloor\). At every site of max-radius \(L-d\),

\[
 |\psi_x|/\epsilon\ge c e^{\nu d}
       \ge c e^{-\nu} L^{\nu D2}.                        \tag{9}
\]

Choose D2 so that \(\nu D2\) strictly exceeds both error exponents in (8), with positive slack. For large L this gives \(|U_x|\ge2\) at zero jitters, and d<L-3.

This conclusion must remain true after conditioning on other jitters. Let \(R^{(0)}\) denote the zero-jitter inverse and let E be any permitted jitter diagonal on J. Then \(\|E\|\le w\), with no factor \(|J|\). Once \(w\|R^{(0)}\|\le1/2\), the identity

\[
 R^E=(I+R^{(0)}E)^{-1}R^{(0)}
\]

gives \(\|R^E\|\le2\|R^{(0)}\|\). Thus \(\|(\mathcal B^E)^{-1}\|=\|R^E_{PP}\|\) stays polynomial. Equations (2), (7) and (8) now apply uniformly to every permitted E, with the same exponents and possibly larger fixed constants. With D2 chosen with the stated slack, they imply

\[
 |U_x^E|\ge1\quad\hbox{whenever }|x|_\infty=L-d.        \tag{10}
\]

This proof does not multiply a small perturbation by the potentially exponential norm of U. That would give an unjustified stability assertion. It controls the reflected term in (8) separately and uses the uniform profile residual for the direct term.

## 4. From physical edges to large inverse entries

Choose a physical nearest-neighbor path from \(j_0\) to max-radius L-d by decreasing absolute coordinates that exceed L-d. It takes at most 2d+2 edges. If \(j_0\in Z\), first decrease its outermost coordinate; at a clipped corner the resulting site still lies in J and outside Z. Subsequent sites can all avoid Z. If \(j_0\notin Z\), start inward directly. The path stays away from the root for large L.

For each successive pair y,j, with \(j\notin Z\), put \(B_\Gamma=\Gamma^{-1}\). Since the nonlocal term \(M\widehat T^{-1}M^\top\) is supported on \(Z\times Z\),

\[
 (B_\Gamma)_{yj}=1,\qquad
 S_j:=\operatorname{supp}(B_\Gamma e_j)
       \subset\{j\}\cup\{\text{four physical neighbors of }j\}. \tag{11}
\]

All matrices in this paragraph are evaluated at zero jitters. Let n=|J|, \(K=\max(1,\|B_\Gamma\|)\),
\(S_y=\operatorname{supp}(B_\Gamma e_y)\), and \(\delta_0=(2nK^2)^{-1}\).
Make an undirected graph on \(S_y\cup S_j\), adding an edge between a in \(S_y\) and b in \(S_j\) whenever \(|\Gamma_{ab}|\ge\delta_0\). Complex symmetry makes this an undirected condition. The vertices y,j belong to the graph by (11).

Suppose they are disconnected. Let D be the diagonal indicator of y's component, extended by zero to the remaining coordinates of J. The inverse commutator identity is

\[
 [D,B_\Gamma]=-B_\Gamma[D,\Gamma]B_\Gamma.
\]

The y,j entry on the left has modulus 1. Any nonzero term on the right has its indices in \(S_y\times S_j\). If their D-values differ, the corresponding \(\Gamma\) entry has modulus below \(\delta_0\), since otherwise it is an edge joining the components. Therefore

\[
 1\le\delta_0\|(B_\Gamma)_{y,:}\|_1
                  \|(B_\Gamma)_{:,j}\|_1
       \le\delta_0 nK^2=1/2,
\]

a contradiction. The last inequality follows by Cauchy–Schwarz on each row/column and the definition of operator norm. This argument also checks that entries outside the graph contribute nothing.

Every edge of this graph meets \(S_j\), which has at most five vertices. A simple path therefore has at most ten edges: outside-cover vertices cannot be successive, so there are at most six of them in addition to the five cover vertices. All vertices in \(S_y\) lie in the physical star of y or in Z; all vertices in \(S_j\) lie in the physical star of j. Consequently all of them have depth at most d+1, within the prescribed jitter shell.

Replace each physical edge by such a simple inverse-entry path, concatenate, and remove loops. This gives distinct sites \(j_0,\ldots,j_s\), ending at depth d, with

\[
 s\le10(2d+2),\qquad
 |\Gamma_{j_a j_{a+1}}|\ge\delta_0\ge L^{-q_4}.           \tag{12}
\]

The choices depend only on zero-jitter data. Erasing loops removes edges without creating a new edge between formerly nonadjacent vertices, so the lower bound is preserved.

## 5. Stability before exposing the path variables

For every simultaneous permitted jitter E, inverse difference gives

\[
 \|R^E-R^{(0)}\|\le2\|R^{(0)}\|^2w,\qquad
 z^E-z^{(0)}=-\Gamma^E E_J z^{(0)}.                     \tag{13}
\]

The second formula follows by applying the full inverse identity to the fixed source column; it never uses a bound on \(\widehat k\). By (5) its right-hand side is bounded by \(C L^{q_5}w\sqrt\rho\). Increase D3 so that (13) is at most \(\delta_0/2\) in each required inverse entry and at most \(a_0\sqrt\rho/2\) in the initial component. Also arrange \(w\|\Gamma^E\|\le1/2\) for every E. Thus the following estimates hold simultaneously:

\[
 |z_{j_0}^E|\ge a\sqrt\rho,\quad a=a_0/2;\qquad
 |\Gamma^E_{j_a j_{a+1}}|\ge\delta,\quad\delta=\delta_0/2;
 \qquad w|\Gamma^E_{ii}|\le1/2.                         \tag{14}
\]

They hold in particular when any subset of jitters has been exposed and all others temporarily set to zero. The terminal estimate (10) also holds at every such state.

## 6. One fresh uniform: a quantitative estimate

For complex numbers A,b,c, let
\(f(t)=A-bt/(1+ct)\) on [-w,w], with \(w|c|\le1/2\). Its denominator has modulus between 1/2 and 3/2. For \(t\in[-w,-w/2]\) and \(u\in[w/2,w]\), exact subtraction gives

\[
 |f(t)-f(u)|
 =\frac{|b|\,|t-u|}{|1+ct|\,|1+cu|}
 \ge\frac49 w|b|.                                    \tag{15}
\]

If some value in the negative interval has modulus less than \(w|b|/9\), every value in the positive interval has modulus greater than \(w|b|/3\). If there is no such value, all values in the negative interval already have modulus at least \(w|b|/9\). Each of these intervals has uniform probability 1/4. Therefore

\[
 \mathbb P\{|f(t)|\ge w|b|/9\}\ge1/4.                 \tag{16}
\]

The conclusion also holds when b=0. Only the triangle inequality was used, so A,b,c may be complex and no alignment or real-sign assumption is hidden here.

## 7. Conditional exposure and the exact accumulated loss

Condition on every jitter outside the fixed path. The path uniforms remain independent, with the same half-width w. At step a<s, retain the exposed jitters, set future path jitters to zero, and vary only that at \(j_a\). Rank-one inversion gives

\[
 z^{\rm new}_{j_{a+1}}=z_{j_{a+1}}-
       \frac{\Gamma_{j_{a+1}j_a}z_{j_a}t}
                    {1+\Gamma_{j_a j_a}t}.             \tag{17}
\]

Apply (16) with \(b=\Gamma_{j_{a+1}j_a}z_{j_a}\). By (14), the conditional probability is at least 1/4 that

\[
 |z^{\rm new}_{j_{a+1}}|\ge (w\delta/9)|z_{j_a}|.       \tag{18}
\]

After the s transfers, expose the independent jitter at \(j_s\). Symmetry and the same rank-one formula give

\[
 F^{\rm new}=F-
       \frac{U_{j_s}z_{j_s}t}{1+\Gamma_{j_sj_s}t}.        \tag{19}
\]

Equation (10) and (16) give a conditional probability at least 1/4 of \(|F^{\rm new}|\ge(w/9)|z_{j_s}|\). Multiplying successive conditional probability bounds, rather than asserting independence of the success events, proves the explicit estimate

\[
 \boxed{\mathbb P\left\{|F|\ge
       a\frac w9\left(\frac{w\delta}{9}\right)^s\sqrt\rho\right\}
       \ge4^{-(s+1)}.}                                \tag{20}
\]

This includes s=0: then only the terminal update is needed. For s>0, later jitters can destroy earlier propagated components; (18) uses only the currently needed component, so no preservation of those earlier components is required. Every success event is measurable in the variables already exposed because all future path values in that intermediate calculation are fixed at zero. At the final step all variables have their actual values.

Since \(a\ge cL^{-q_2}\), \(\delta\ge cL^{-q_4}\), w=L^{-D3}, and \(s\le C(1+\log L)\), the negative logarithm of the threshold coefficient in (20) is at most

\[
 q_2\log L+O(1)+(s+1)(D3\log L+\log9)
                         +s(q_4\log L+O(1))
       \le C_1(\log L)^2
\]

for L sufficiently large. Also \((s+1)\log4\le C_2(1+\log L)\). This proves (3), uniformly after conditioning on all nonpath jitters, and hence after averaging them. It also gives \(\mathbb E_{\rm jitters}|F|^2\ge e^{-C(\log L)^2}\rho\) on each fixed regular datum.

## 8. Independent checks and limits

The update (17) can be derived without quoting the inverse formula. For this derivation let \(\widetilde z=R(0,\widehat k)\) be the full response, whose J part is z. The new equation is \((H+t e_j e_j^\top)\widetilde z^{\rm new}=(0,\widehat k)\). Multiplication by R gives \(\widetilde z^{\rm new}=\widetilde z-t R e_j z_j^{\rm new}\), so \(z_j^{\rm new}=z_j/(1+t\Gamma_{jj})\), which recovers (17). Multiplication by \(p^\top/\epsilon\) gives (19), using \(p^\top\Gamma e_j=\epsilon U_j\). Likewise, cross-multiplying the two affine fractions in (15) yields the numerator \(b(u-t)\), checking the cancellation directly.

The graph threshold was checked both by the displayed commutator and by bounding its sum termwise: the total crossing contribution is at most \(\delta_0\sum_a|B_{ya}|\sum_b|B_{bj}|\le\delta_0 nK^2\). The ten-edge bound follows equivalently from the fact that deleting the at most five cover vertices leaves isolated vertices along any simple path. The loss in (20) can be counted as s gains \(w\delta/9\) and one final gain w/9, or as s+1 fresh uniforms and s inverse-entry factors; both give the same powers.

Uniform invertibility excludes every intermediate pole. Large exterior norms never enter: source estimates use k*, and inverse estimates use (1). The shell covers the stars added by the inverse graph. The path is fixed before any path uniform is drawn. The terminal bound uses (2) uniformly, rather than continuity of the exponentially large field. Constants and the minimum L may depend on the fixed positive disorder and energy.

The unresolved inputs are (1), including the weighted good-boundary estimate and the regular-r probability, and the earlier construction of a profile satisfying (2). Formula (2)'s residual estimate follows from the stated uniform inverse bound and a shell residual of order L epsilon; the inverse-producing profile lemma is not independently proved here. Artificial absorption has been omitted from H, as in the source's rootless jitter argument. Restoring it and the calibrated root is a subsequent step, not part of this lemma. Neither the manuscript's complete transmission proposition nor the full T010 statement follows from this local result alone.
