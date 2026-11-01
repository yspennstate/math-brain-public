# Supplement — the balanced two-flip sparse endpoint has safe-ray quotient zero

This directly attacks the balanced near-character escape left by `SAFE-RAY-COERCIVITY-v1` using the genuine sparse-defect family singled out in fleet01/B12 `20260922T081900Z-balanced-poincare-bellman` (commit `3a03960af4b07d1b38b418c3a0430360c272c0ac`).

## Theorem

Let `k>=3`. Start from the dictator `chi_1` on the uniform `k`-cube and flip its value at two vertices of opposite `chi_1` sign and Hamming distance two. The resulting Boolean function `f_k` is balanced. Then

\[
\boxed{H(f_k)<6\,[I(f_k)-1].}
\tag{1}
\]

Consequently the refuted all-gate candidate `Gamma^dagger` is nevertheless strictly safe on this entire obstruction family at the balanced point:

\[
D_{\Gamma^\dagger}(f_k;1/2^k)
> (6.521851214-6)[I(f_k)-1]>0,
\tag{2}
\]

so

\[
\tau(f_k;1/2^k)=0.
\tag{3}
\]

Thus the sparse family that refutes quadratic one-character leakage does **not** produce a blow-up of `SAFE-RAY-COERCIVITY-v1`.

## Exact spectrum

By cube symmetry take the flipped points

\[
x=(1,1,\ldots,1),\qquad y=(-1,-1,1,\ldots,1).
\]

Put

\[
q=2^{2-k}.
\]

Flipping a point `z` changes the Walsh coefficient at `S` by

\[
-2^{1-k}\chi_1(z)\chi_S(z).
\]

Hence the two changes add exactly when `S` contains an odd number of coordinates from `{1,2}`, and cancel otherwise. Therefore

\[
\widehat f_k(\{1\})=1-q,
\]

and every other set containing exactly one of `{1,2}` has coefficient `-q`; all remaining coefficients vanish. There are

\[
N=2^{k-1}-1
\]

of these non-dominant atoms. Thus the squared spectrum is

\[
(1-q)^2\quad\text{once},
\qquad q^2\quad\text{with multiplicity }N.
\tag{4}
\]

Since `2^{k-1}=2/q`, Parseval is immediate:

\[
(1-q)^2+Nq^2=1.
\]

The total Fourier level over all sets containing exactly one of `{1,2}` is `2^{k-2}k`. Removing the dominant singleton gives

\[
I(f_k)
=(1-q)^2+q^2(2^{k-2}k-1)
=1+(k-2)q.
\tag{5}
\]

Thus

\[
\delta:=I(f_k)-1=(k-2)q,
\tag{6}
\]

recovering the edge-count formula in the consumed peer report.

The entropy is also exact:

\[
\begin{aligned}
H(f_k)
={}&(1-q)^2\log_2\frac1{(1-q)^2}
 +(2q-q^2)\,2(k-2).
\end{aligned}
\tag{7}
\]

## Uniform bound

Use

\[
-\ln(1-q)\le \frac{q}{1-q}.
\]

The dominant-atom contribution in (7) is at most

\[
\frac{2q(1-q)}{\ln2}.
\]

Dividing (7) by `delta=(k-2)q` therefore gives

\[
\frac{H(f_k)}\delta
\le
4-2q+\frac{2(1-q)}{(k-2)\ln2}.
\tag{8}
\]

For `k=3`, direct substitution in (7) gives `H/delta=4`. For `k>=4`,

\[
\frac{H(f_k)}\delta
<4+\frac1{\ln2}<6.
\tag{9}
\]

This proves (1).

## Consequence for the current missing implication

The consumed fleet01/B12 theorem correctly shows that this family prevents a universal `O(delta^2)` best-character leakage estimate. But (1) shows that such quadratic leakage was never needed for the live safe-ray target: the exact all-gate defect is already positive on the family before any tilted-quartic repair is added.

Therefore a genuine balanced endpoint counterexample to `SAFE-RAY-COERCIVITY-v1` must have more complicated signed leakage geometry than the canonical two-flip sparse dictator defect. Full FEI remains open.
