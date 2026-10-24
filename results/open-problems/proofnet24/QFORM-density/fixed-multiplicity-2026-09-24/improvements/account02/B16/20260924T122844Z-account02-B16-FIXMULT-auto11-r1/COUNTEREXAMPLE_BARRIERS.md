# account02/B16 counterexample barriers for lowering the fixed-multiplicity threshold

Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Source manuscript: `yspennstate/math-open-problems@7c0d6e60946b19423e6400a12d34b473cf0591e2`  
Git blob: `183ccd294763214e6a707e8d4749ff9a8cf7006d`  
Advertised SHA-256: `9f3bdec0b88debe9a66076c7b4a5cc894fb14e69b89591a4107e785340f65e69`

Status: **proof-mechanism obstructions only; no counterexample to the 17-eigenvalue theorem and no lower-multiplicity theorem claimed.**

## 1. Seventeen unit spectral directions need not create a physical pivot

For integers `q>=1` and `m>=101`, let

\[
A_{q,m}=I_q\otimes \frac{J_m}{m},
\]

where `J_m` is the `m x m` all-ones matrix. Each block `J_m/m` has eigenvalues `1,0,...,0`. Hence `A_{q,m}` has exactly `q` nonzero singular values, all equal to one. In particular

\[
s_{17}(A_{17,m})=1.
\]

Nevertheless, every physical diagonal entry is `1/m<1/100`. A principal two-coordinate determinant is:

- `0` if the two coordinates are in the same block, because the corresponding `2x2` block is `(1/m)J_2`;
- `1/m^2<1/100` if they are in distinct blocks, because the off-diagonal entry is zero.

Thus `A_{17,m}` is in the manuscript's **no-pivot** class despite satisfying the full normalized 17-direction spectral hypothesis.

**Impact.** Any proof shortcut asserting that many large singular values force a scalar physical pivot or a large principal `2x2` determinant is false. The no-pivot Fourier/crossing-volume branch is structurally necessary.

## 2. The completion ranks `(3r,r)` are saturated by local no-pivot information

At `r=1`, take

\[
A_0=\begin{pmatrix}
-3&1&-3&-3\\
1&-3&-3&-3\\
-3&-3&10&9\\
-3&-3&9&9
\end{pmatrix},
\qquad S=\{1\},\quad T=\{2\},\quad L=\{3,4\}.
\]

Then `B=A_0[S,T]=[1]`. For the manuscript interpolation

\[
P=A_0[:,T]B^{-1}A_0[S,:],
\]

one computes

\[
A_0[L,L]-P[L,L]
=\begin{pmatrix}1&0\\0&0\end{pmatrix}.
\]

Hence the completion has `E=0`,

\[
D=\operatorname{diag}(0,0,1,0),\qquad R=A_0-D,
\]

and exact elimination gives

\[
\det A_0=144,
\quad \operatorname{rank}A_0=4,
\quad \operatorname{rank}R=3,
\quad \operatorname{rank}R[L,L]=1.
\]

So the manuscript bounds

\[
\operatorname{rank}R\le3r,
\qquad
\operatorname{rank}R[L,L]\le r
\]

are simultaneously attained.

Now scale by `alpha=1/20000`. The largest physical diagonal is `10 alpha=0.0005<1/100`. The largest absolute principal `2x2` determinant of `A_0` is `39`, so after scaling every such determinant is at most

\[
39\alpha^2=9.75\times10^{-8}<1/100.
\]

Thus the same rank saturation occurs strictly inside the manuscript's local no-pivot inequalities.

**Impact.** A `17 -> 16` or `17 -> 13` reduction cannot follow merely by replacing the completion bounds by smaller universal ranks on the basis of local no-pivot entry information. Direct sums supply the same algebraic rank saturation pattern for higher `r`.

The scaled witness is not a counterexample to a lower-multiplicity density theorem, because scaling also destroys the unit spectral hypothesis. It is only a counterexample to a proposed proof shortcut.

## 3. Endpoint obstruction in the present Fourier receiver

The audited regularized determinant bound converts order-`k` crossing volume into characteristic-function decay `|t|^{-k/4}`. Therefore:

\[
k=4\quad\Longrightarrow\quad |\phi(t)|\lesssim |t|^{-1},
\]

which is exactly the nonintegrable absolute-Fourier endpoint, whereas `k=5` gives exponent `5/4>1` and direct density inversion. The rank-saturation example above blocks a bookkeeping-only algebraic reduction, while this endpoint blocks simply replacing order five by order four in the same absolute-`L^1` Fourier argument.

## Next obligation

A genuine multiplicity reduction must introduce information absent from the current pipeline, for example one of:

1. a source-valid order-four endpoint receiver that does not require absolute `L^1` Fourier inversion; or
2. a quantitative bridge from the forced same-index bordered-minor information to additional **disjoint** crossing volume.

Any threshold reduction must preserve arbitrary independent rough coordinate densities, arbitrary affine terms, arbitrary signature and remaining spectrum, and must be supplied as a complete replacement proof with explicit constants and a closed dependency map. No such replacement proof is claimed here.
