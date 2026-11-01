SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B06, 2026-09-24T06:51:58Z.
attacking: `QFORM-ADJUGATE-6465-TANGENTIAL-COLLAR-RECEIVER-v1`; test whether the partner's positive-normal 64/65 collar forces a quantitative normal floor, and derive a product-weighted three-frame curved-normal receiver before any fiber supremum.

# Early substantive calculation

Fresh designated-partner input: fleet03/B06 `QFORM-NORMAL-INNOVATION-COMPENSATED-CROSS-VOLUME-v1` at `3296465aa736673c06e0412a7a7c3191d3cc413d`. In its notation

\[
a^2\det(NN^T)=W(D+d\theta)^2+d^2H,\qquad \chi=H/(W\theta^2),
\]

and the unpaid branch is `0<chi<1/64`.

## A target-level family with chi -> 0 but fixed third-curvature layers

Let the tail bank have eight coordinates and choose the flat orthonormal Walsh rows
\[
w=8^{-1/2}(1,1,1,1,1,1,1,1),
\]
\[
v=8^{-1/2}(1,1,1,1,-1,-1,-1,-1),
\]
\[
u=8^{-1/2}(1,1,-1,-1,1,1,-1,-1).
\]
Thus every tail coordinate has two-frame leverage `1/4` and full three-frame leverage `3/8`.

For `0<epsilon<=1/32`, put
\[
E=\binom{w}{v},\qquad q=(1/4,1/4),\qquad z_h=qE+\epsilon u,
\]
and let `Z` have rows `(z_h,w,v)`. Then
\[
G=ZZ^T=\begin{pmatrix}
1/8+\epsilon^2&1/4&1/4\\
1/4&1&0\\
1/4&0&1
\end{pmatrix},
\]
so
\[
W=1,\quad \nu=\epsilon^2,\quad \det G=\epsilon^2,
\]
\[
e_1(G)=17/8+\epsilon^2,\qquad e_2(G)=9/8+2\epsilon^2,
\]
and
\[
\det(I+G)=17/4+4\epsilon^2.
\]
In particular `det G/det(I+G)<2^{-12}` for `epsilon<=1/32`.

Take
\[
B=\begin{pmatrix}-3&1&1\\1&1&-1\\1&-1&1\end{pmatrix},\qquad D:=\det B=-4,
\]
and add diagonal curvature `d=4` on the selected physical hub only. Then the actual literal three-hub block is
\[
F=B+\operatorname{diag}(4,0,0)
=\begin{pmatrix}1&1&1\\1&1&-1\\1&-1&1\end{pmatrix},
\]
with spectrum `{2,2,-1}`. Every physical `2x2` principal block of `F` is singular.

For the partner split,
\[
C=\begin{pmatrix}1&-1\\-1&1\end{pmatrix},\quad b=(1,1)^T,
\quad c=\operatorname{adj}(C)b=(2,2)^T,
\]
so `K=det C=0`, `theta=K+q c=1`, and the actual scalar pivot is `a=-3+4=1`. Hence
\[
H=\nu c^T\operatorname{adj}(I_2)c=8\epsilon^2,
\qquad \boxed{\chi=8\epsilon^2\to0}.
\]
At the same time the tangential resonance is exact:
\[
D+d\theta=-4+4=0.
\]
Therefore the partner identity gives
\[
\boxed{\det(NN^T)=128\epsilon^2},
\qquad \sigma_1(N)\sigma_2(N)=8\sqrt2\,\epsilon.
\]
Thus the current scalar-pivot/rank-two-cross receiver necessarily degenerates like `epsilon^{-1/4}` on this family.

Yet the complete mixed Pluecker layers stay uniformly large:
\[
P_0=4,\qquad P_1=17/2+4\epsilon^2,
\qquad P_2=9/2+8\epsilon^2,
\qquad P_3=4\epsilon^2,
\]
\[
P=17+16\epsilon^2.
\]
So neither large layer-0/1/2 currency, nor the diffuse two-frame gate, nor even the diffuse full-three-frame gate forces a positive lower bound on `chi`.

Define the full original-coordinate matrix
\[
A_\epsilon=[I_3,Z]^TB[I_3,Z]+\operatorname{diag}(4,0,0,0,\ldots,0).
\]
Its literal hub principal block is exactly `F`, so Cauchy interlacing implies that `A_epsilon` has at least two eigenvalues `>=2` and at least one eigenvalue `<=-1`. Hence it is an exact QFORM target for every `epsilon>0`.

Now apply the completed pinned `COUNTEREXAMPLE_SEARCH.md` Theorem A at `e5f71d79eff325201dd0274053d20268ce65b837`: conditioning on all tail coordinates leaves the literal three-hub quadratic part `F`, whose minimum absolute eigenvalue is one. Therefore, uniformly in every tail conditioning and all induced affine terms,
\[
\boxed{\|p_{X^TA_\epsilon X}\|_{\infty,\mathrm{ess}}\le 6\sqrt\pi.}
\]
Thus this is not a QFORM counterexample. It is a counterexample to the intermediate claim that the partner's `64/65` collar plus retained layer mass must force a quantitative normal floor or a usable physical pair.

The compiler must instead admit a localized three-hub exit, or genuinely spend the retained layer mass before paying the inverse normal coefficient.
