SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B13, 2026-09-23T05:07:16Z.
attacking: the exact-zero-diagonal physical-pair chamber by combining pair-log half-Riesz smoothing with aggregate E2 extremality, then accounting exactly for the rank-two Schur correction.

# fleet01/B13 auto15b — exact bathtub reduction and pair-anchored E2 closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Extremal product laws  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED TARGET-RELEVANT SUPPORTING THEOREMS / FULL QFORM OPEN / CONTINUITY SEPARATE**

The full target remains open. The results below preserve arbitrary independent original-coordinate cap-one laws, arbitrary dimension, arbitrary extra spectrum, arbitrary affine terms induced by conditioning, and arbitrary translated/fragmented supports. No post-rotation independence, arbitrary-joint coarea bound, conditional projected-density cap, pointwise quadratic oscillatory decay, bounded-diameter localization, or fixed fragment count is used.

## 1. Sources actually consumed and applied

2. Designated partner `fleet02/B13` r23:
   `yspennstate/math-open-problems@892bfe36756e09cbaff3f05070f7a3e20fea0fd1`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B13/20260923T040105Z-fleet02-B13-extremal-r23/REPORT.md`.
   I apply its exact rank-one Schur `E2`-loss identity in Section 6 to the *actual pair-Schur correction*, producing a quantitative survive/tri-hub/transverse-star trichotomy.
3. `fleet03/B13` r23:
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B13/20260923T034405Z-fleet03-B13-qform-r23/REPORT.md`.
   Its `QFORM-E2-ENTROPIC-L3-v1` and `QFORM-E2-ENTROPY-OR-TRIHUB-v1` are used in Sections 4-5.
4. Pair-log theorem:
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
   Its physical-pair logarithmic envelope is optimized in Section 3.

The partner and E2 source theorems are supporting arguments and have not converted the full conjecture into a proved claim.

## 2. Exact extremal-product reduction for slab kernels

Let
\[
\mathcal F=\{f:\mathbb R\to[0,1]:\int_{\mathbb R}f=1\}.
\]
For every bounded measurable nonnegative kernel \(K:\mathbb R^n\to[0,\infty)\),
\[
\boxed{
\sup_{f_1,\dots,f_n\in\mathcal F}
\int_{\mathbb R^n}K(x)\prod_{j=1}^n f_j(x_j)\,dx
=
\sup_{\substack{E_1,\dots,E_n\subset\mathbb R\\ |E_j|=1}}
\int_{\prod_jE_j}K(x)\,dx .
}
\tag{2.1}
\]

This is an equality of suprema over arbitrary measurable unit-measure sets; no interval, centered set, diameter bound, fragment-count bound, or attainment assertion is present.

### Proof

First let \(g:\mathbb R\to[0,\infty)\) be bounded and measurable. For \(f\in\mathcal F\), layer cake gives
\[
\int fg
=\int_0^\infty\int_{\{g>t\}} f(x)\,dx\,dt
\le
\int_0^\infty \min\{1,|\{g>t\}|\}\,dt.
\tag{2.2}
\]
The right side is the decreasing-rearrangement quantity
\[
\int_0^1 g^*(s)\,ds
=
\sup_{|E|=1}\int_Eg.
\tag{2.3}
\]
The reverse inequality in
\[
\sup_{f\in\mathcal F}\int fg=\sup_{|E|=1}\int_Eg
\tag{2.4}
\]
is immediate because \(1_E\in\mathcal F\).

For fixed \(f_2,\ldots,f_n\), define
\[
g_1(x_1)=\int K(x_1,\ldots,x_n)\prod_{j=2}^nf_j(x_j)\,dx_2\cdots dx_n.
\]
It is bounded and nonnegative, so (2.4) replaces the first marginal by a unit-measure indicator without lowering the supremum. Suprema over independent choices commute. Iterate through all \(n\) coordinates to obtain (2.1). QED.

For the slab kernel
\[
K(x)=1_{\{x^TAx\in J\}},
\tag{2.5}
\]
(2.1) is exactly the desired extremal-product reduction. The designated partner's no-attainment purification further supplies bounded-finite-union approximants when one wants a finite geometric witness; (2.1) itself needs no finite-fragment hypothesis.

## 3. A translation-uniform half-Riesz kernel from an indefinite physical pair

Let \(U,V\) be independent cap-one variables and let \(B\) be a fixed invertible indefinite \(2\times2\) symmetric matrix. Put
\[
D=|\det B|,\qquad \kappa=\sigma_{\min}(B)>0.
\]
The completed pair-log theorem gives, for every cutoff \(r>0\), every affine translation, and almost every output value,
\[
p_{\rm pair}(t)
\le
\frac{2\sqrt2}{r}
+
D^{-1/2}\log_+
\frac{2r^2}{\kappa|t-t_0|}.
\tag{3.1}
\]
For \(u=t-t_0\ne0\), choose
\[
r^2=\frac{\kappa|u|}{2}.
\tag{3.2}
\]
Then the logarithmic term vanishes exactly and
\[
\boxed{
p_{\rm pair}(t)\le4\kappa^{-1/2}|t-t_0|^{-1/2}.
}
\tag{3.3}
\]
The right side may be infinite at the single critical value; that causes no problem under the subsequent integrable averaging.

Now partition the original physical coordinates as \(K=\{i,j\}\) and \(K^c\), with \(B=A[K,K]\). Completing the pair square, without rotating the random vector, gives
\[
Q=
(X_K+m(Y))^TB(X_K+m(Y))+R(Y),\qquad Y=X_{K^c},
\tag{3.4}
\]
where
\[
S=A[K^c,K^c]-A[K^c,K]B^{-1}A[K,K^c]
\tag{3.5}
\]
is the pair Schur complement and \(R\) is its quadratic polynomial, including any affine term. Conditional on the ORIGINAL outside coordinates \(Y\), the two inputs in \(X_K\) remain independent cap-one variables, while \(m(Y)\) is merely a deterministic translation. Hence (3.3) gives
\[
\boxed{
p_Q(t)\le4\kappa^{-1/2}\,
\mathbb E|t-R|^{-1/2}.
}
\tag{3.6}
\]

## 4. \(L^3\) density implies a uniform half-Riesz bound

If \(R\) has probability density \(p\in L^3(\mathbb R)\), set \(M=\|p\|_3\). For every \(s\in\mathbb R\) and every \(\rho>0\),
\[
\int_{|x-s|\le\rho}|x-s|^{-1/2}p(x)\,dx
\le
M\left(\int_{|u|\le\rho}|u|^{-3/4}\,du\right)^{2/3}
=
4M\rho^{1/6},
\tag{4.1}
\]
while
\[
\int_{|x-s|>\rho}|x-s|^{-1/2}p(x)\,dx\le\rho^{-1/2}.
\tag{4.2}
\]
Optimizing at \(\rho=(3/(4M))^{3/2}\) gives
\[
\boxed{
\sup_s\mathbb E|R-s|^{-1/2}
\le
4(4/3)^{3/4}\|p_R\|_3^{3/4}.
}
\tag{4.3}
\]

This step uses only the unconditional \(L^3\) density of the Schur remainder. It does not invoke a conditional projection cap.

## 5. Pair + aggregate \(E_2\) gives \(L^\infty\), or a finite two-sided tri-hub

Choose disjoint original-coordinate banks \(I,J\subset K^c\) and put
\[
M=S[I,J].
\]
Let \(\mu\) be a probability law on the nonzero physical \(2\times2\) minors \(M[P,T]\), and suppose every row inclusion marginal of \(\mu\) is at most
\[
h\in[1/2,3/4).
\]
Define
\[
K_2(\mu)
=
\exp\!\left(
H(\mu)+\mathbb E_\mu\log\det(M[P,T])^2
\right).
\tag{5.1}
\]
The `fleet03/B13` entropic \(E_2\) theorem gives
\[
\|p_R\|_3
\le
A(h)K_2(\mu)^{-1/6},
\qquad
A(h)=
\left[
\frac{6\sqrt{e/(2h)}}{3-4h}
\right]^{2/3}.
\tag{5.2}
\]
Combining (3.6), (4.3), and (5.2) gives the new theorem

\[
\boxed{
\|p_Q\|_\infty
\le
C_{\rm pair}(h)\,
\kappa^{-1/2}K_2(\mu)^{-1/8},
}
\tag{5.3}
\]
where
\[
\boxed{
C_{\rm pair}(h)
=
16(4/3)^{3/4}
\left[
\frac{6\sqrt{e/(2h)}}{3-4h}
\right]^{1/2}.
}
\tag{5.4}
\]

This is `QFORM-PAIR-E2-ENTROPIC-LINF-v1`.

There is an exact original-matrix lift. Put
\[
K_{4,K}(\mu)=
\exp\!\left(
H(\mu)
+
\mathbb E_\mu
\log\det A[K\cup P,K\cup T]^2
\right).
\tag{5.5}
\]
The block determinant identity
\[
\det A[K\cup P,K\cup T]
=
\det(B)\det S[P,T]
\tag{5.6}
\]
gives
\[
K_{4,K}(\mu)=D^2K_2(\mu),
\tag{5.7}
\]
hence
\[
\boxed{
\|p_Q\|_\infty
\le
C_{\rm pair}(h)\,
\kappa^{-1/2}D^{1/4}K_{4,K}(\mu)^{-1/8}.
}
\tag{5.8}
\]

### Natural \(E_2\) law and the tri-hub alternative

Let
\[
E=E_2(M)=e_2(M^TM)
=\sum_{|P|=|T|=2}\det(M[P,T])^2>0
\tag{5.9}
\]
and let \(w_2(P,T)=\det(M[P,T])^2/E\).

Take
\[
h=0.51,\qquad L=\log4.
\tag{5.10}
\]
Apply `QFORM-E2-ENTROPY-OR-TRIHUB-v1` first to \(M\) and then to \(M^T\).

If either orientation admits a cap-feasible law with
\[
D(\mu\|w_2)\le\log4,
\tag{5.11}
\]
then
\[
K_2(\mu)=E e^{-D(\mu\|w_2)}\ge E/4,
\]
and (5.3) yields
\[
\boxed{
\|p_Q\|_\infty
\le
75.41281\,
\kappa^{-1/2}E^{-1/8}.
}
\tag{5.12}
\]

If neither orientation is paid, there are physical hub sets
\[
H\subset I,\quad C\subset J,\qquad |H|,|C|\le3,
\tag{5.13}
\]
such that less than \(E/4\) of the squared \(2\times2\)-minor mass avoids \(H\) on the row side and less than \(E/4\) avoids \(C\) on the column side. Therefore
\[
\boxed{
\sum_{\substack{P\cap H\ne\varnothing\\T\cap C\ne\varnothing}}
\det(M[P,T])^2
>
\frac{E}{2}.
}
\tag{5.14}
\]

Thus an indefinite physical pair followed by an aggregate order-two Schur bank is either paid in \(L^\infty\) or collapses to a finite two-sided tri-hub. This is `QFORM-PAIR-E2-LINF-OR-TRIHUB-v1`.

### Exact zero-diagonal pair: coefficient cancellation

If
\[
B=
\begin{pmatrix}
0&b\\ b&0
\end{pmatrix},
\qquad b\ne0,
\tag{5.15}
\]
then
\[
\kappa=|b|,\qquad D=b^2.
\tag{5.16}
\]
Define the anchored squared physical four-volume on the chosen cut
\[
V_{4,K}(I,J)
=
\sum_{|P|=|T|=2}
\det A[K\cup P,K\cup T]^2
=
b^4E.
\tag{5.17}
\]
The diffuse branch (5.12) becomes the particularly clean geometric bound
\[
\boxed{
\|p_Q\|_\infty
\le
75.41281\,V_{4,K}(I,J)^{-1/8}.
}
\tag{5.18}
\]
The small edge coefficient has disappeared into the anchored four-volume rather than being paid separately.

For arbitrary measurable \(E_\ell\subset\mathbb R\) of measure one, the exact extremal-product reduction gives the corresponding slab-volume inequality
\[
\boxed{
\left|
\left\{
x\in\prod_\ell E_\ell:
x^TAx\in J_0
\right\}
\right|
\le
75.41281\,V_{4,K}(I,J)^{-1/8}|J_0|
}
\tag{5.19}
\]
throughout this diffuse zero-diagonal-pair branch. No interval assumption is present.

Define the global anchored four-volume
\[
\Omega_{4,K}(A)
=
\sum_{\substack{|P|=|T|=2\\
P,T\subset K^c,\;P\cap T=\varnothing}}
\det A[K\cup P,K\cup T]^2.
\tag{5.20}
\]
A random red/blue coloring of \(K^c\) places a fixed ordered disjoint pair \(P,T\) into opposite banks with probability \(1/16\). Hence some disjoint cut satisfies
\[
V_{4,K}(I,J)\ge\Omega_{4,K}(A)/16.
\tag{5.21}
\]
Applying the previous dichotomy to that cut gives:

\[
\boxed{
\text{either }\;
\|p_Q\|_\infty
\le
106.64982\,\Omega_{4,K}(A)^{-1/8},
\quad
\text{or the selected Schur }E_2\text{ mass is two-sided tri-hub.}
}
\tag{5.22}
\]

This is a genuine reduction from the previous pair-anchored **five-volume** obstruction to an anchored **four-volume** obstruction in the diffuse \(E_2\) chamber.

## 6. Applying the designated fleet02/B13 Schur-loss identity to the actual pair correction

This section is the required direct use of the designated partner.

Let \(N=A[I,J]\) be a pre-Schur physical cross block and let
\[
S=N-A[I,K]B^{-1}A[K,J]
\tag{6.1}
\]
be the actual pair-Schur cross block. The correction has rank at most two, so choose any rank-two factorization
\[
N=S+x_1y_1^T+x_2y_2^T,
\qquad
S_1=S+x_2y_2^T.
\tag{6.2}
\]
The designated partner's exact rank-one identity applied first to
\(N=S_1+x_1y_1^T\) and then to \(S_1=S+x_2y_2^T\) gives
\[
D_1^2
:=
\|\wedge^2N-\wedge^2S_1\|_F^2
=
\|x_1\|^2\|y_1\|^2
\|P_{x_1^\perp}S_1P_{y_1^\perp}\|_F^2,
\tag{6.3}
\]
\[
D_2^2
:=
\|\wedge^2S_1-\wedge^2S\|_F^2
=
\|x_2\|^2\|y_2\|^2
\|P_{x_2^\perp}SP_{y_2^\perp}\|_F^2.
\tag{6.4}
\]
Triangle inequality in the exterior Hilbert space gives
\[
\sqrt{E_2(N)}
\le
\sqrt{E_2(S)}+D_1+D_2.
\tag{6.5}
\]

Put \(E_0=E_2(N)\). If
\[
E_2(S)<E_0/4,
\tag{6.6}
\]
then (6.5) forces \(D_1+D_2>\sqrt{E_0}/2\), so
\[
\boxed{
\max\{D_1^2,D_2^2\}>E_0/16.
}
\tag{6.7}
\]
Thus pair Schur descent cannot destroy more than three quarters of the aggregate pair-volume without creating a quantitatively large exact transverse-star currency.

If instead
\[
E_2(S)\ge E_0/4,
\tag{6.8}
\]
Section 5 applied to the *actual* Schur block yields either its finite tri-hub survivor or
\[
\boxed{
\|p_Q\|_\infty
\le
89.68145\,
\kappa^{-1/2}E_0^{-1/8}.
}
\tag{6.9}
\]
Indeed (5.12) and \(E_2(S)\ge E_0/4\) add the factor \(4^{1/8}\).

This proves the new trichotomy `QFORM-PAIR-SCHUR-E2-SURVIVE-OR-TRIHUB-OR-STAR-v1`:

1. **paid:** (6.9);
2. **finite survivor:** more than half of the actual surviving Schur \(E_2\) mass is jointly incident to at most three row and three column hubs;
3. **exact loss certificate:** one of the two rank-one correction components has transverse-star currency \(>E_0/16\).

For the exact null pair (5.15), there is a physical factorization with
\[
A[I,K]B^{-1}A[K,J]
=
b^{-1}
\left(
c_1u_2^T+c_2u_1^T
\right),
\tag{6.10}
\]
where \(c_a=A[I,k_a]\) and \(u_a=A[k_a,J]^T\). Thus the star alternative is itself expressed entirely in original-coordinate coupling banks.

The paid branch of (6.9) becomes
\[
\boxed{
\|p_Q\|_\infty
\le
89.68145\,(b^4E_0)^{-1/8}
}
\tag{6.11}
\]
for the zero-diagonal pair.

## 7. Consequence for an extremal counterexample sequence

Suppose the full conjecture fails. By (2.1), its slab ratios can be realized in the supremum by arbitrary unit-measure product indicators, and by the designated partner's purification they can be approximated by bounded finite unions of intervals with no fixed fragment-count or diameter restriction.

In the exact zero-diagonal physical-pair chamber, every nonzero edge \(b=A_{ij}\) now has the following obstruction pattern:

* if an anchored pair-Schur \(E_2\) cut is diffuse, the output density is paid by (5.18);
* if a pre-Schur \(E_2\) bank survives at least one quarter, then either it is paid by (6.11) or the surviving mass is supported on a finite two-sided tri-hub;
* if it loses more than three quarters under the pair Schur correction, the exact designated-partner identity forces a transverse-star currency at least \(E_0/16\).

Therefore a diverging counterexample sequence cannot merely make all scalar diagonals vanish and all pair five-volumes small. It must simultaneously drive the pair-anchored **four-volume** into the tri-hub chamber for every useful null pair, or route its pre-Schur pair-volume into one of the explicit transverse-star certificates above.

The sharpened first unpaid implication is

`QFORM-NULLPAIR-E2-TRIHUB-STAR-CLOSURE-v1`:

> In the no/near-scalar-pivot class, turn the finite two-sided tri-hub or one of the exact transverse-star currencies from Section 6 into an already-paid grouped bank / bi-hub / three-bank density mechanism, uniformly over arbitrary translated product indicators; or construct a genuine counterexample inside that intersection class.

Arbitrary additional spectral directions remain retained throughout Sections 3-6; the missing step is structural exhaustion, not a rank-exactly-three restriction.

## 8. Deterministic checks and status

A seeded deterministic check verified:

* the bordered pair determinant identity (5.6) on 500 random symmetric systems, maximum absolute floating error `6.306066779870889e-14`;
* the designated partner rank-one exterior identity on 500 random rectangular systems, maximum absolute floating error `1.1368683772161603e-12`;
* the two-step exterior triangle inequality used in (6.5), maximum observed violation `0`;
* constants
  `C_pair(0.51)=63.41436110402684`,
  diffuse `log 4` constant `75.41280941826052`,
  quarter-survival constant `89.68144952253964`,
  and global zero-diagonal anchored-four-volume diffuse constant `106.64981785596152`.

These numerical checks are diagnostic only. The statements above have analytic proofs at their stated scopes.

**Full QFORM remains OPEN / NOT PROVED.** The separate continuous-density conclusion remains OPEN. The new statements require independent mathematical review before any full-proof assembly may rely on them as reviewed facts.
