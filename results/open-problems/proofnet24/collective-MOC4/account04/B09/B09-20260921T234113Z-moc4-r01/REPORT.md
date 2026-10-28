# MOC4 r01 — exact obstruction to a spectrum-independent permutation-weight lift

**Campaign:** MOC4 (four-dimensional Marcus–de Oliveira determinant convex-hull conjecture)  
**Worker:** account04/B09  
**Outcome:** `CANDIDATE_REFUTED` — a stronger coefficientwise proof mechanism is false; **this is not a counterexample to MOC4**.  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`.

## Source-exact target

For complex normal \(4\times4\) matrices \(A,B\) with eigenvalues \(a_1,\dots,a_4\) and \(b_1,\dots,b_4\), prove

\[
\det(A+B)\in\operatorname{conv}\left\{\prod_{i=1}^4(a_i+b_{\sigma(i)}):\sigma\in S_4\right\}.
\]


The new collective root had no completed MOC4 peer report visible when this run began. Under the shared order's missing-peer rule, I attacked the common coefficient-representation candidate explicitly assigned to the MOC4 team (account01/B08) and the exact-unitary adversary direction assigned to account03/B08.

## Compact conditional route and first missing implication

After unitary diagonalization write

\[
A=\operatorname{diag}(a_1,\ldots,a_4),\qquad B=U\operatorname{diag}(b_1,\ldots,b_4)U^*.
\]

For \(S,T\subseteq[4]\) with \(|S|=|T|\), put

\[
p_{S,T}(U)=|\det U[S,T]|^2.
\]

Principal-minor expansion followed by Cauchy–Binet gives the exact polynomial identity

\[
D_U(a,b):=\det(A+B)
 =\sum_{S\subseteq[4]} a_{S^c}\sum_{|T|=|S|} b_T\,p_{S,T}(U),
\tag{1}
\]

where \(a_R=\prod_{i\in R}a_i\) and \(b_T=\prod_{j\in T}b_j\).

A tempting sufficient route is to find, for every fixed \(U\), a probability distribution \(\lambda_U\) on \(S_4\) satisfying

\[
p_{S,T}(U)=\Pr_{\sigma\sim\lambda_U}[\sigma(S)=T]
\quad\text{for all }S,T,\ |S|=|T|.
\tag{2}
\]

Then (1), coefficient by coefficient, would imply

\[
D_U(a,b)=\sum_{\sigma\in S_4}\lambda_U(\sigma)
\prod_i(a_i+b_{\sigma(i)}),
\]

which would prove MOC4 at once. The first essential question for this route is therefore whether the exterior-power squared-minor marginals admit one common classical permutation coupling. They do not.

## Exact no-go theorem

**Proposition.** There is a rational real orthogonal \(4\times4\) matrix \(U\) for which no probability distribution on \(S_4\) satisfies (2), even if (2) is required only for one-point and two-point subsets. Consequently there is no convex representation with weights depending only on \(U\) that agrees with \(D_U(a,b)\) for every choice of spectra \(a,b\).

Take

\[
U=\begin{pmatrix}
 492/625&-31/625&-48/125&12/25\\
 -9/25&12/25&-4/5&0\\
 -36/125&48/125&9/25&4/5\\
 -256/625&-492/625&-36/125&9/25
\end{pmatrix}.
\tag{3}
\]

It is exactly orthogonal; for example it is the product of the four rational Givens rotations

\[
G_{14}(3/5,-4/5)\,G_{34}(3/5,-4/5)\,
G_{23}(3/5,4/5)\,G_{12}(4/5,-3/5),
\]

with the convention that \(G_{ij}(c,s)\) has the \(2\times2\) block
\(\begin{psmallmatrix}c&-s\\s&c\end{psmallmatrix}\) on coordinates \(i,j\).

For any probability law on permutations define

\[
P_{ij}=\Pr[\sigma(i)=j],\qquad
Q_{S,T}=\Pr[\sigma(S)=T]\quad(|S|=|T|=2).
\]

Every such law obeys the linear inequality

\[
P_{1,2}+P_{2,4}-Q_{\{1,3\},\{2,3\}}
+Q_{\{1,4\},\{3,4\}}\ge 0.
\tag{4}
\]

This is pointwise on each permutation. Indeed, if
\(\sigma(\{1,3\})\ne\{2,3\}\), the sole negative indicator is absent. If
\(\sigma(\{1,3\})=\{2,3\}\), then either \(\sigma(1)=2\); or
\(\sigma(1)=3,\sigma(3)=2\). In the latter case the remaining images of
\(2,4\) are \(1,4\): either \(\sigma(2)=4\), or
\(\sigma(2)=1,\sigma(4)=4\), in which case
\(\sigma(\{1,4\})=\{3,4\}\). Thus the negative indicator is always paid by at least one positive indicator.

For the orthogonal matrix (3), the squared-minor data give

\[
P_{1,2}=|u_{1,2}|^2=\frac{961}{390625},\qquad
P_{2,4}=0,
\]

\[
Q_{\{1,3\},\{2,3\}}
=\left|\det U[\{1,3\},\{2,3\}]\right|^2
=\left(\frac{81}{625}\right)^2
=\frac{6561}{390625},
\]

while

\[
Q_{\{1,4\},\{3,4\}}
=\left|\det U[\{1,4\},\{3,4\}]\right|^2=0.
\]

Hence the left side of (4) equals

\[
\frac{961-6561}{390625}
=-\frac{224}{15625}<0,
\]

contradicting the existence of a common permutation coupling. This proves the proposition.

The final consequence follows by polynomial coefficient comparison: if

\[
D_U(a,b)=\sum_\sigma\lambda_U(\sigma)
\prod_i(a_i+b_{\sigma(i)})
\]

held for all \(a,b\) with one fixed probability vector \(\lambda_U\), then the coefficients of \(a_{S^c}b_T\) would force exactly (2).

## What this does and does not settle

This kills the strongest natural “one \(U\)-dependent Birkhoff lift for all spectra” strategy. It does **not** show that a particular determinant value lies outside the 24-point hull. MOC4 permits convex weights to depend on \(a,b\) (and, in a support-function proof, on the support direction). Negative or incompatible universal coefficient weights are therefore not a counterexample to the conjecture itself.

A full proof can instead target the exact support inequality

\[
\Re\!\left(e^{-i\theta}D_U(a,b)\right)
\le
\max_{\sigma\in S_4}
\Re\!\left(e^{-i\theta}\prod_i(a_i+b_{\sigma(i)})\right)
\quad\text{for every }\theta,
\tag{5}
\]

or find spectrum-dependent weights. The no-go result says that any such argument must use more than simultaneous classical realization of all \(\wedge^1 U\) and \(\wedge^2 U\) squared-minor marginals.

## Exact verification

`verify_no_universal_lift.py` uses only Python's standard-library `fractions.Fraction`. It verifies \(U^TU=I\), the two minors above, the exact violation \(-224/15625\), and inequality (4) pointwise on all 24 permutations. No numerical tolerance or optimization output is needed for the certificate.

## Handoff

**Candidate version:** `MOC4-U-LIFT-v1`.  
**Prior missing implication:** existence of one spectrum-independent probability law on \(S_4\) realizing the one- and two-subset squared-minor marginals of every \(U\in U(4)\).  
**New applied inference:** `CANDIDATE_REFUTED` by the exact rational orthogonal matrix (3) and inequality (4).  
**Remaining obligation:** prove the spectrum/support-direction dependent hull bound (5), or derive another exact mechanism retaining the common-unitary constraints.  
**Recommended recipients:** account03/B07 lead, account01/B08 coefficient-representation worker, account03/B08 exact-unitary adversary worker, and the account04 MOC4 peers.  
**Parent conjecture status:** OPEN; no counterexample or full proof claimed.
