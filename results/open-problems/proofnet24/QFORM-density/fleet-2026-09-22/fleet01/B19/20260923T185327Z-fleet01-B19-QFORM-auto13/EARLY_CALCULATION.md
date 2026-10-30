# Early calculation — common-plane small-s3 latent completion

Run: `20260923T185327Z-fleet01-B19-QFORM-auto13`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Status at this checkpoint: supporting derivation; full QFORM still open.

## Partner theorem applied first

Use fleet02/B19 r36, `QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1`, source
`yspennstate/math-open-problems@9157730c1b552b81f58b3cb6ef604b687962e548`.
For the actual physical common-plane predecessor with disjoint original banks `D1,D2,K`, old bicore `N=A[D1,K]`, self-edge `M=A[D1,D2]`, and `P2` the top-two left singular plane of `N`, it gives

\[
Z_{\rm phys}=e_3([M,N]^T[M,N])\ge (s_1(N)s_2(N))^2\|(I-P_2)M\|_F^2.
\]

At the live constants
\[
\Delta_*=0.0014419528160955833\ldots,\qquad
F=0.05671470919622164\ldots,
\]
so `||(I-P2)M||_F^2>=F/64` implies
\[
Z_{\rm phys}\ge \Delta_*^2F/64
 =1.842543860212322\times 10^{-9}.
\]
The marginal-free physical-E3 theorem of fleet03/B02 r35 therefore pays this branch with
\[
\|p_Q\|_\infty<301.317,
\]
and gives a continuous `C_0` density. Thus the state treated below is genuinely the in-plane common-plane survivor; no transverse coefficient is silently deleted.

## New deterministic lemma

Consider the normalized real symmetric `6 x 6` coefficient matrix
\[
K=\begin{pmatrix}
D_1&R&I_2\\
R^T&D_2&I_2\\
I_2&I_2&D_3
\end{pmatrix},
\qquad D_j=D_j^T,
\]
and put `eps=s_3(K)`, where singular values are decreasing.

### Claim
If `eps<1/4`, there is an invertible symmetric `2 x 2` matrix `S` such that, with
\[
K_S=\begin{pmatrix}
S&S&I_2\\
S&S&I_2\\
I_2&I_2&S^{-1}
\end{pmatrix}
=\begin{bmatrix}I_2\\ I_2\\ S^{-1}\end{bmatrix}
S
\begin{bmatrix}I_2&I_2&S^{-1}\end{bmatrix},
\]
we have
\[
\|S-R\|_{op}\le {28\over9}\,\varepsilon(1+\|R\|_{op}),
\]
and
\[
\boxed{\ \|K-K_S\|_{op}\le {73\over9}\,\varepsilon(1+\|R\|_{op}).\ }
\]
In particular the comparison matrix is an **exact symmetric rank-two latent square**.

### Proof
Because `K` is symmetric, truncate its spectral decomposition to the two eigenvalues of largest absolute value. This gives a symmetric matrix `L` of rank at most two with
\[
\|K-L\|_{op}=s_3(K)=\varepsilon.
\]
The block `L_{13}` is within `eps<1/4` of `I_2`, hence invertible, so `rank L=2`. Write
\[
A=L_{13},\qquad B=L_{23},\qquad H=L_{33}.
\]
A symmetric rank-two factorization `L=W\Lambda W^T` shows that invertibility of `L_{13}=W_1\Lambda W_3^T` forces `W_1,W_3,\Lambda` invertible; hence `H=W_3\Lambda W_3^T` is invertible. Put `S=H^{-1}`. The rank-two Schur complement about `H` vanishes identically, so
\[
L_{11}=ASA^T,\qquad L_{12}=ASB^T,\qquad L_{22}=BSB^T. \tag{1}
\]
Since every block of `L-K` has operator norm at most `eps`, writing `r=||R||op` gives
\[
\|A-I\|,\|B-I\|,\|L_{12}-R\|\le\varepsilon.
\]
Let `c=(1-eps)^{-1}<=4/3`. From `S=A^{-1}L_{12}B^{-T}`,
\[
\begin{aligned}
\|S-R\|
&\le c^2\varepsilon
 +\|(A^{-1}-I)RB^{-T}\|+\|R(B^{-T}-I)\|\\
&\le\varepsilon\{c^2+(c^2+c)r\}\\
&\le {28\over9}\varepsilon(1+r). \tag{2}
\end{aligned}
\]
As `eps<=1/4`, (2) yields
\[
\|S\|\le r+{7\over9}(1+r)\le {16\over9}(1+r). \tag{3}
\]
Using (1),
\[
\begin{aligned}
\|D_1-S\|
&\le\varepsilon+\|ASA^T-S\|\\
&\le\varepsilon+(2\varepsilon+\varepsilon^2)\|S\|\\
&\le5\varepsilon(1+r),
\end{aligned}
\]
and identically `||D2-S||<=5 eps(1+r)`. Finally `S^{-1}=H`, so
\[
\|D_3-S^{-1}\|\le\varepsilon.
\]
The only off-diagonal defect of `K-K_S` is the `(1,2)` block `R-S` and its transpose. Bounding a symmetric block matrix by the maximum row sum of its block operator norms gives
\[
\|K-K_S\|_{op}
\le 5\varepsilon(1+r)+{28\over9}\varepsilon(1+r)
={73\over9}\varepsilon(1+r).
\]
This proves the claim. No random variables were rotated, no input law was used, and no coefficient tail was dropped.

## Coupling the lemma to an actual physical E3 payment

The current fleet03/B20 r37 quarter-split theorem applies when each of the three two-dimensional physical frames has row leverage at most `1/64`. Let
\[
m_*^2={63\over64}\,0.000356312664981148\ldots
      =0.0003507452795908176\ldots .
\]
For its literal original-coordinate split cross block `M_phys`, the deterministic congruence and the two restricted frame Gramians give
\[
s_3(M_{phys})\ge {m_*^2\over4}s_3(K). \tag{4}
\]
The marginal-free physical-E3 theorem gives
\[
\|p_Q\|_\infty
\le C_{E3}s_3(M_{phys})^{-1},\qquad
C_{E3}=3\,2^{4/3}e^{1/3}=10.550168831164775\ldots . \tag{5}
\]
Therefore for any `eta>0`, every low-leverage common-plane state satisfies the exhaustive alternative
\[
s_3(K)\ge\eta
\quad\Longrightarrow\quad
\|p_Q\|_\infty\le {4C_{E3}\over m_*^2\eta},
\]
with continuous `C_0` density; while if `s_3(K)<min(eta,1/4)`, it is quantitatively near the exact latent rank-two family by the boxed lemma.

With `eta=1/512`, the paid constant is
\[
{4C_{E3}\over m_*^2\eta}=61,602,385.046\ldots<6.161\times10^7,
\]
and the unpaid state obeys
\[
\boxed{\ \|K-K_S\|_{op}<0.015843\,(1+\|R\|_{op}).\ }
\]
This is coefficient geometry only; it is **not** a license to treat the defect as a small random quadratic error under arbitrary unbounded cap-one laws.

## Exact next debt

At the exact latent endpoint, lifting the rank-two completion back to the original coefficient space gives a rank-two operator `L_2`. The target assumption still forces
\[
\|A-L_2\|_{op}\ge s_3(A)\ge1.
\]
Hence the third target spectral resource survives exactly, but an analytic product-preserving receiver for `latent rank-two square + retained unit spectral remainder` is still required. The other local residue is a physical frame row of leverage `>1/64`.
