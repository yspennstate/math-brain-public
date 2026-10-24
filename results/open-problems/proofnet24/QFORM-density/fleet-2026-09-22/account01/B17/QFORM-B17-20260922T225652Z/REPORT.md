# QFORM B17 — exact k-fold collinear heavy-row branch

Run: `QFORM-B17-20260922T225652Z`

Status: `SUPPORTING_SHARP-BRANCH_THEOREM / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

The full conjecture is **not** proved here. This report gives an exact global extremal theorem for a source-valid family with an arbitrary finite number of macroscopic physical coordinates sharing the minority-sign spectral direction, and shows analytically how the known `3 sqrt(2)` obstruction is approached as the number of such coordinates grows.

## 1. Branch theorem

Fix an integer `k>=1`. Let `X_1,...,X_k` be independent real random variables with probability densities `0<=f_i<=1`. Let `G_1,G_2` be independent standard Gaussians, independent of the `X_i`, and put

\[
Y_k=\sqrt{\frac{12}{k}}\sum_{i=1}^k X_i,
\qquad
T_k=G_1^2+G_2^2-Y_k^2.
\]

Let `U_1,...,U_k` be iid `Unif[-1/2,1/2]`, and define

\[
B_k:=\frac12\,\mathbf E\exp\!\left[-\frac{6}{k}
      \left(\sum_{i=1}^kU_i\right)^2\right].
\]

Then `T_k` has a density and

\[
\boxed{\ \|p_{T_k}\|_\infty\le B_k.\ }
\]

The bound is sharp over all independent cap-one laws `f_i`: equality is attained at output `t=0` when all `X_i` are centered unit intervals.

Thus, after restoring the physical variance-`1/12` scale, the exact branch constant is

\[
\boxed{
C_k=12B_k
=6\,\mathbf E\exp\!\left[-\frac{6}{k}
      \left(\sum_{i=1}^kU_i\right)^2\right].
}
\]

This is a *global-output* statement: arbitrary translations and fragmentation of the cap-one heavy laws cannot produce a larger peak anywhere on the real line in this branch.

## 2. Proof by exact shell rearrangement and k-fold Riesz/BLL

Write

\[
E=G_1^2+G_2^2.
\]

Then `E` is exponential with density

\[
g_E(u)=\frac12e^{-u/2}\mathbf 1_{u\ge0}.
\]

Set

\[
a=\sqrt{12/k},\qquad Z=\sum_{i=1}^kX_i.
\]

Conditioning on `Z` gives, for every real `t`,

\[
p_{T_k}(t)=\int_{\mathbb R^k}
  \Big(\prod_{i=1}^kf_i(x_i)\Big)
  K_t(x_1+\cdots+x_k)\,dx,
\]

where

\[
K_t(z)=\frac12e^{-(t+a^2z^2)/2}
       \mathbf 1_{\{t+a^2z^2\ge0\}}.
\]

### Nonnegative output

For `t>=0`, `K_t=e^{-t/2}K_0`, and `K_0` is symmetric decreasing. The one-dimensional Brascamp--Lieb--Luttinger/Riesz rearrangement inequality gives

\[
p_{T_k}(t)
\le e^{-t/2}
\int\Big(\prod f_i^*(x_i)\Big)K_0\!\left(\sum x_i\right)dx.
\]

Each `f_i^*` is symmetric decreasing, has integral one and is bounded by one. Fix all factors except one. The inner convolution against the other symmetric-decreasing factors and `K_0` is again symmetric decreasing. The bathtub principle therefore replaces that `f_i^*` by `1_{[-1/2,1/2]}` without decreasing the integral. Iterating over all `i` gives

\[
p_{T_k}(t)\le e^{-t/2}B_k\le B_k.
\]

### Negative output: exact partner shell identity

Let `t=-r^2`, `r>0`. Then

\[
K_{-r^2}(z)
=\frac12e^{-(a^2z^2-r^2)/2}
 \mathbf 1_{\{|z|\ge r/a\}}.
\]

The exact symmetric-decreasing rearrangement is

\[
\boxed{
K_{-r^2}^*(u)=\frac12e^{-ar|u|-a^2u^2/2}.
}
\]

Indeed, if `z_0=r/a`, a superlevel shell consists of the two intervals
`z_0<=|z|<z_0+d`, whose total length is `2d`; moving that mass to the centered interval `[-d,d]` changes `(a^2z^2-r^2)/2` into `ar d+a^2d^2/2`.

This is the shell-rearrangement mechanism proved in the completed account02/B17 collinear theorem `20260922T194544Z-account02-B17-QFORM-r18`; here it is applied to the actual `k`-fold integral rather than merely cited.

BLL followed by the same coordinatewise bathtub replacement yields

\[
\begin{aligned}
p_{T_k}(-r^2)
&\le \frac12\mathbf E\exp\!\left[
-ar\left|\sum_{i=1}^kU_i\right|
-\frac{a^2}{2}\left(\sum_{i=1}^kU_i\right)^2
\right]\\
&\le \frac12\mathbf E\exp\!\left[
-\frac{a^2}{2}\left(\sum_{i=1}^kU_i\right)^2
\right]=B_k.
\end{aligned}
\]

Combining the two output signs proves the theorem. With centered interval laws and `t=0`, every rearrangement and bathtub step is an equality, so the branch constant is exact.

## 3. Source-valid finite matrices

For integers `m,k>=1`, take a physical-to-spectral frame `R_{m,k}` with

- `m` rows `e_1/sqrt(m)`,
- `m` rows `e_2/sqrt(m)`,
- `k` rows `e_3/sqrt(k)`.

Then

\[
R_{m,k}^TR_{m,k}=I_3.
\]

Hence, for

\[
A_{m,k}=R_{m,k}\operatorname{diag}(1,1,-1)R_{m,k}^T,
\]

every finite matrix has nonzero spectrum exactly `{1,1,-1}`. With centered unit-interval inputs in the two diffuse positive banks and arbitrary cap-one laws on the `k` heavy coordinates,

\[
Q_{m,k}
=
\left(m^{-1/2}\sum_{j=1}^mU_j^{(1)}\right)^2
+\left(m^{-1/2}\sum_{j=1}^mU_j^{(2)}\right)^2
-\left(k^{-1/2}\sum_{i=1}^kX_i\right)^2.
\]

For fixed `k`, as `m->infinity`,

\[
12Q_{m,k}\Rightarrow T_k.
\]

For centered interval heavy laws the limiting density is continuous at zero and has physical peak `C_k`. Therefore any universal density constant for the original conjecture must satisfy `C>=C_k`: if all finite members had density bounded by `C`, their fixed-interval concentration probabilities pass to the weak limit, and then shrinking the interval at zero gives `p(0)<=C`.

Thus `C_k` is a genuine target-level lower-bound sequence arising from exact finite original-coordinate product models.

## 4. Fourier representation and the Gaussian endpoint

Let

\[
W_i=\sqrt{12}\,U_i\sim\operatorname{Unif}[-\sqrt3,\sqrt3],
\qquad
S_k=k^{-1/2}\sum_{i=1}^kW_i.
\]

Then `C_k=6 E exp(-S_k^2/2)`. Since

\[
\phi_W(t)=\frac{\sin(\sqrt3t)}{\sqrt3t},
\]

Fourier inversion of `exp(-x^2/2)` gives the exact one-dimensional formula

\[
\boxed{
C_k=\frac6{\sqrt{2\pi}}
\int_{\mathbb R}e^{-t^2/2}
\left[
\frac{\sin(\sqrt3t/\sqrt k)}{\sqrt3t/\sqrt k}
\right]^kdt.
}
\]

For each fixed `t`, the bracketed power tends to `e^{-t^2/2}`. It is bounded in absolute value by one, so dominated convergence gives

\[
\boxed{C_k\longrightarrow 3\sqrt2.}
\]

Thus the known `3 sqrt(2)` lower obstruction is not only a completely diffuse three-bank effect: it is the endpoint of an exact hierarchy with **any finite number of macroscopic physical coordinates sharing one spectral direction**.

## 5. Quantitative approach to the barrier

For the standardized uniform characteristic function,

\[
\log\frac{\sin(\sqrt3z)}{\sqrt3z}
=-\frac{z^2}{2}-\frac{z^4}{20}-\frac{z^6}{105}+O(z^8).
\]

Hence

\[
k\log\phi_W(t/\sqrt k)
=-\frac{t^2}{2}-\frac{t^4}{20k}-\frac{t^6}{105k^2}
+O\!\left(\frac{t^8}{k^3}\right).
\]

Split the Fourier integral into `|t|<=delta sqrt(k)` and its Gaussian tail. On the first region the displayed analytic expansion is uniform; on the second the factor `e^{-t^2/2}` is exponentially small. Termwise integration therefore gives

\[
\boxed{
C_k=3\sqrt2\left[
1-\frac{3}{80k}-\frac{173}{17920k^2}+O(k^{-3})
\right].
}
\]

In particular, this exact branch approaches `3 sqrt(2)` from below for all sufficiently large `k`.

The first values are

| k | C_k |
|---:|---:|
| 1 | 3.980105675042009 |
| 2 | 4.151696859512994 |
| 3 | 4.184469829904556 |
| 4 | 4.200066166813146 |
| 5 | 4.209060935971992 |
| 10 | 4.226306396129321 |
| 20 | 4.234581516628117 |
| 50 | 4.239442207612535 |
| 100 | 4.241045586606818 |

The `k=2` value reduces exactly to the completed account02/B17 formula

\[
C_2=2\sqrt{3\pi}\,\operatorname{erf}(\sqrt3)-2+2e^{-3}.
\]

The numerical table is a check only; it is not used to infer monotonicity for every finite `k`.

## 6. Applying the latest account02/B17 fourth-mode result

The latest completed designated-partner result `account02/B17 20260922T204449Z-account02-B17-QFORM-r19` proves that

\[
G_1^2+G_2^2-G_3^2-\delta G_4^2
\]

has exact global peak

\[
\frac1{2\sqrt{2(1+\delta)}}
\qquad(\delta>0).
\]

Append to the source-valid family above an independent diffuse fourth bank with eigenvalue `-delta`. For every fixed `k`, subtracting the independent fourth-bank limit is a convolution, so

\[
\|p_{T_{k,\delta}}\|_\infty\le B_k.
\]

With centered interval heavy laws and then `k->infinity`, the exact partner theorem identifies the endpoint:

\[
12\,\|p_{T_{k,\delta}}\|_\infty
\longrightarrow
\boxed{\frac{3\sqrt2}{\sqrt{1+\delta}}}.
\]

Thus a fixed independent Gaussianized extra minority-sign spectral mode creates a strict asymptotic gap below the `3 sqrt(2)` barrier throughout this fragmentation hierarchy. Any witness above the barrier must use a genuinely coupled/non-Gaussian extra-mode mechanism rather than an independent diffuse spectral tail.

Partner source pins:

- account02/B17 r18 handoff proof source: `yspennstate/math-open-problems@97c8874b48c663a7ae131cb3899dbafdb5a31d1c`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T194544Z-account02-B17-QFORM-r18/REPORT.md`.
- account02/B17 r19 source: `yspennstate/math-open-problems@50913ed00c5943aaf2772473cbf17ddcb5bed090`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B17/20260922T204449Z-account02-B17-QFORM-r19/REPORT.md`.

## 7. What remains unpaid

This does **not** prove that `3 sqrt(2)` is the universal sharp constant and does not prove full QFORM. It excludes a broad exact witness architecture: any finite number of collinear macroscopic minority-sign physical rows, arbitrary cap-one fragmentation/translation of those laws, all output locations, and independent diffuse extra minority-sign modes at the Gaussian endpoint.

A larger witness, if it exists, must exploit something outside this architecture, such as non-collinear heavy rows interacting across signs, a coupled spectral tail sharing physical coordinates, finite/mesoscopic non-Gaussian overshoot, or a more complicated off-center geometry. Continuity for the full conjecture is separate and remains open.
