SOLUTION STATUS: PARTIAL

# HARD10-04 backfill — recovered local-response / locality iteration

Backfill archive time: 2026-09-15T16:29:00Z
Original research provenance: earlier HARD10-04 task response on 2026-09-15, prior to the verified 14:45Z and 15:26Z reports.
Recovery status: reconstructed from the accessible authored task response; this file preserves the mathematical content and original PARTIAL status. It is not represented as an independently verified proof.

## Exact target

For standard external site DLA on \(\mathbb Z^2\), started from \(A_1=\{0\}\), with attachment law given by simple-random-walk harmonic measure from infinity on the exterior vertex boundary, determine whether
\[
\frac{\log R_n}{\log n}
\]
converges almost surely to a deterministic exponent and identify that exponent, or rigorously refute existence/determinism.

This recovered iteration did **not** solve the full target. Its purpose was to sharpen the one-step capacity response and isolate how global geometry enters it.

## 1. Source notation

For a finite connected set \(A\subset\mathbb Z^2\), let
\[
\partial A=\{y\notin A:\exists z\in A,\ y\sim z\},
\qquad
\overline A=A\cup\partial A.
\]
For an accessible \(x\in\partial A\), set
\[
B=A\cup\{x\},
\qquad
K=\overline A,
\qquad
L=\overline B.
\]
Then
\[
S:=L\setminus K=\{x_1,\dots,x_k\},
\qquad 1\le k\le3,
\]
where the \(x_i\) are newly exposed neighbours of the added site \(x\).

Write
\[
p:=\omega(x,K),
\qquad
g_i:=G(x_i,K),
\qquad
w_i:=\omega(x_i,L),
\]
and let
\[
H_{ij}:=G(x_i,x_j,K).
\]
Losev–Smirnov's Lemma 5 proof supplies the exact identities
\[
\operatorname{Cap}(L)-\operatorname{Cap}(K)
=\sum_iw_ig_i,
\]
and, by first-entry decomposition,
\[
g_j=\sum_iw_iH_{ij}.
\]
The killed Green matrix is symmetric.

## 2. Exact finite-dimensional capacity response

### Proposition — recovered/proved in the original iteration

The vector identities
\[
\boxed{g=Hw}
\]
and
\[
\boxed{
\operatorname{Cap}(L)-\operatorname{Cap}(K)
=g^TH^{-1}g
}
\]
hold.

Moreover, the discrete normal derivative identity for simple random walk gives
\[
\boxed{
p=\frac14\mathbf1^Tg.}
\]
Therefore, if
\[
u:=\frac{g}{\mathbf1^Tg},
\qquad u_i\ge0,
\qquad\mathbf1^Tu=1,
\]
and
\[
\kappa_A(x)
:=
\frac{\operatorname{Cap}(L)-\operatorname{Cap}(K)}{p^2},
\]
then
\[
\boxed{
\kappa_A(x)=16u^TH^{-1}u.
}
\]

### Derivation

The first-entry equation is \(g=Hw\). Since \(H\) is a finite positive-definite Green matrix, it is invertible, so \(w=H^{-1}g\). Substitution into the exact capacity-increment identity gives
\[
\Delta\operatorname{Cap}=w^Tg=g^TH^{-1}g.
\]

For the flux identity, use the standard planar Green/harmonic-measure normal derivative at a killed site:
\[
\omega(x,K)=\frac14\sum_{y\sim x}G(y,K).
\]
The Green function vanishes on \(K\); the neighbours of \(x\) outside \(K\) are exactly \(x_1,\dots,x_k\). Hence
\[
p=\frac14\sum_i g_i.
\]
The displayed formula for \(\kappa_A(x)\) follows.

## 3. Return-kernel representation and explicit constants

Let \(Q\) be the first positive return kernel on \(S\) for simple random walk killed on \(K\):
\[
Q_{ij}
=
\mathbb P_{x_i}\{\text{first positive hit of }S\cup K\text{ is }x_j\}.
\]
Distinct neighbours of one square-lattice vertex are not nearest neighbours, so a return to \(S\) has positive length. The strong Markov property gives
\[
H=I+Q+Q^2+\cdots=(I-Q)^{-1}.
\]
Path reversal gives symmetry of \(Q\). A Schur-complement realization
\[
Q=B(I-P_U)^{-1}B^T
\]
shows \(Q\succeq0\). From each \(x_i\), a direct step to the newly occupied \(x\in K\) occurs with probability \(1/4\), hence
\[
\sum_jQ_{ij}\le\frac34.
\]
Thus
\[
0\preceq Q\preceq\frac34I,
\qquad
\frac14I\preceq H^{-1}=I-Q\preceq I.
\]
Consequently
\[
4\|u\|_2^2
\le
\kappa_A(x)
\le
16\|u\|_2^2.
\]
Since \(1/k\le\|u\|_2^2\le1\),
\[
\boxed{
\frac4k\le\kappa_A(x)\le16,
\qquad 1\le k\le3.
}
\]
In particular,
\[
\boxed{
\frac43\,p^2
\le
\Delta\operatorname{Cap}
\le
16p^2.
}
\]

This made the source's two-sided \(\asymp p^2\) estimate explicit in the square-lattice normalization, subject to the stated Green-function normalization.

## 4. Exact boundary-size increment

The original iteration also observed a simple combinatorial identity. When an accessible site \(x\) is attached, \(x\) leaves the outer vertex boundary and the \(k\) new sites in \(S=L\setminus K\) enter it. No other old boundary site ceases to be a boundary site merely because \(x\) was added. Hence
\[
\boxed{
|\partial B|-|\partial A|=k-1.
}
\]
For an accessible DLA attachment, \(1\le k\le3\), so the outer vertex-boundary cardinality is nondecreasing along the process.

This identity by itself does not control harmonic measure, because many boundary sites may carry extremely small or zero harmonic measure.

## 5. Locality of the return kernel

Suppose two closed cluster environments \(K,K'\) agree inside \(B(x,L)\), have the same active attachment site \(x\), and therefore the same local new-neighbour set \(S\). Let \(Q_K,Q_{K'}\) be their first-return kernels on \(S\).

Couple the two killed walks using the same simple-random-walk trajectory. Their first-return/killing outcomes can differ only if the walk exits \(B(x,L)\) before hitting the common local absorbing set. Since \(x\in K\cap K'\), this event is contained in
\[
\{\tau_{\partial B(x,L)}<T_x\}.
\]
For planar simple random walk started one lattice step from \(x\), the potential-kernel gambler's-ruin estimate gives
\[
\mathbb P\{\tau_{\partial B(x,L)}<T_x\}
\le\frac{C}{\log L}.
\]
Therefore
\[
\boxed{
\max_{i,j}|Q_K(i,j)-Q_{K'}(i,j)|
\le\frac{C}{\log L},
}
\]
and because \(k\le3\),
\[
\boxed{
\|Q_K-Q_{K'}\|_{2\to2}
\le\frac{C}{\log L}.
}
\]

Since
\[
\kappa_K(x)=16u_K^T(I-Q_K)u_K,
\]
one obtains
\[
|\kappa_K(x)-\kappa_{K'}(x)|
\le
32\|u_K-u_{K'}\|_2+rac{C}{\log L}.
\]
Thus the return-kernel part of the one-step response is logarithmically local; the principal potentially nonlocal variable is the normalized incoming-flux split \(u\).

## 6. Capacity-martingale strengthening recovered in the same iteration

For DLA let
\[
C_n=\operatorname{Cap}(\overline A_n),
\quad
\Delta_{n+1}=C_{n+1}-C_n,
\quad
a_n=\mathbb E[\Delta_{n+1}\mid\mathcal F_n].
\]
With \(\xi_{n+1}=\Delta_{n+1}-a_n\) and \(M_n=\sum_{k<n}\xi_{k+1}\), the original iteration strengthened the earlier Freedman estimate by proving finite total quadratic variation.

From \(\Delta\lesssim p^2\),
\[
\mathbb E[\Delta_{n+1}^2\mid\mathcal F_n]
\lesssim
S_5(n)
\le
(p_n^*)^2S_3(n)
\lesssim
(p_n^*)^2a_n.
\]
Beurling and capacity-radius comparison give
\[
(p_n^*)^2\lesssim e^{-(\pi/2)C_n}.
\]
Setting \(Z_n=e^{-(\pi/2)C_n}\), boundedness of one-step capacity increments yields
\[
\mathbb E[Z_n-Z_{n+1}\mid\mathcal F_n]
\gtrsim Z_na_n.
\]
Conditional telescoping from any finite stopping time \(T\) therefore gives
\[
\boxed{
\mathbb E\!\left[
\sum_{n=T}^\infty\Delta_{n+1}^2
\middle|\mathcal F_T
\right]
\lesssim
R_T^{-1}.
}
\]
Consequently \(M_n\) converges a.s. and in \(L^2\), with conditional tail variance \(O(R_T^{-1})\), and
\[
\boxed{
\log R_n
=
\frac\pi2\sum_{k<n}a_k+O(1)
\qquad\text{a.s.}
}
\]

This strengthening was later independently incorporated into the verified Rényi/intermittency backfill and subsequent reports, so it is repeated here only to preserve the original recovered iteration's provenance.

## 7. Status / checks / gaps

### PROVED in the recovered iteration, subject to source-normalization verification

- finite-dimensional response formula \(\kappa_A(x)=16u^TH^{-1}u\);
- return-kernel form \(H^{-1}=I-Q\);
- explicit bound \((4/3)p^2\le\Delta\operatorname{Cap}\le16p^2\);
- exact boundary-size increment \(|\partial B|-|\partial A|=k-1\);
- logarithmic locality of \(Q\) under remote modifications;
- finite future quadratic energy and convergence of the capacity martingale.

### OPEN / not established

- locality or self-averaging of the normalized flux split \(u\);
- convergence of the weighted response amplitude;
- convergence/determinism/value of the planar DLA radial exponent.

### Recovery and verification caveat

This is a backfill of genuine earlier authored mathematical work from the accessible task transcript. It preserves the original PARTIAL status. No independent referee or formal verification was available in that earlier run, and this archive does not upgrade self-review to independent verification.
