# Independent audit: global operator-route boundaries

Date: 2026-10-02. Auditor: independent `antivoter_audit` agent.

**Verdict: PASS as a failed-route boundary checkpoint.** I read the entire
`continuation_20261002_operator_boundaries.md`, its exact obstruction
script and JSON, the spectral and radial search implementations, the
saved search summaries, and the relevant sections of the locally supplied
primary Rossman manuscript (`rossman_mobius.txt`/`.pdf`). I independently
rederived the inequalities and exact obstruction and reran fresh exact
arithmetic in a separate checker. The note correctly makes no unrestricted
Sidorenko claim. Two minor search-comment/wording qualifications are
recorded below; neither affects its mathematical conclusions. No author
file or Git state was modified.

## 1. Interpolation convention and global Perron bound

The stated convention
\[
 M(t)_{ij,kl}=(A_{ij}A_{kl})^t(A_{il}A_{kj})^{1-t}
\]
matches Rossman's Definition 4.1. For symmetric nonnegative \(A\),
the transfer is symmetric and entrywise nonnegative. Its diagonal is
\(A_{ij}^2\), so \(\operatorname{tr}M(t)=\|A\|_F^2\).
With \(S\) exchanging tensor factors, direct indexing gives
\(M(0)=(A\otimes A)S\) and
\(M(1)=\operatorname{vec}(A)\operatorname{vec}(A)^T\).
Consequently their spectral radii are \(\rho(A)^2\) and
\(\|A\|_F^2\). The first fact follows either from their tensor
eigenvectors or because \(S\) commutes with \(A\otimes A\) and
its eigenvalues have absolute values \(|\lambda_i(A)\lambda_j(A)|\).

For positive matrices \(B,C\) and positive Perron vectors \(x,y\),
rowwise Hölder applied to
\(v_i=x_i^{1-t}y_i^t\) gives
\[
 [B^{\circ(1-t)}\circ C^{\circ t}]v
 \le\rho(B)^{1-t}\rho(C)^t v.
\]
The positive-vector spectral-radius bound yields the claimed geometric
interpolation inequality. Applying it to the two endpoints gives
\[
 \rho(M(t))\le\rho(A)^{2(1-t)}\|A\|_F^{2t}
                 \le\|A\|_F^2=\operatorname{tr}M(t).
\]
For zero entries, approximate \(A\) by \(A+\varepsilon\mathbf1\)
at each fixed interior \(t\) and take the limit. Endpoints are defined
by their explicit matrices and satisfy the bound separately; no
continuity in \(t\) across zero-entry endpoints is required. The zero
matrix is trivial. This avoids a hidden \(0^0\) convention issue.

Thus excluding one Perron eigenvalue leaves a nonnegative total sum.
That conclusion supplies the total-sum endpoint, rather than the shorter
partial sums in Rossman's Section 6 weak-majorization proposal. This
distinction is correct. The full mathematical proof is self-contained;
I could not retrieve the linked Kingman publisher page through the web
tool, so this audit does not independently certify that bibliographic
attribution beyond the provided source record.

## 2. Ladder Hölder normalization

The bipartite ladder has \(2m\) vertices and \(3m\) edges. Its three
offset classes \(r-s\in\{-1,0,1\}\) are disjoint perfect matchings
for every \(m\ge3\). Let \(H_q\) be the product of \(W\) over
one offset matching. With independent uniform vertex labels,
\[
 t(BL_{2m},W)=\mathbb E[H_{-1}H_0H_1]
 \le\prod_q(\mathbb EH_q^3)^{1/3}
 =\left(\frac{\sum_{ij}W_{ij}^3}{n^2}\right)^m.
\]
Each matching uses disjoint random vertex pairs, which justifies the
last product factorization. Multiplying by \(n^{2m}\) gives
\(\operatorname{hom}(BL_{2m},W)\le(\sum W_{ij}^3)^m\).
Rossman's Lemma 1.5 identifies that homomorphism sum with
\(\operatorname{tr}(M_W^m)\), where
\((M_W)_{ij,kl}=\sqrt{W_{ij}W_{kl}}W_{il}W_{kj}\).
For even \(m\), every eigenvalue power is nonnegative, so
\(\rho(M_W)^m\le\operatorname{tr}(M_W^m)\). Taking even powers,
or already combining an even power with the bound, yields
\(\rho(M_W)\le\sum W_{ij}^3\). No \(n^2\) normalization factor
is missing. This is an upper bound, and does not provide Sidorenko's
required lower odd-moment bound.

For the interpolation connection, \(A=W^{\circ3/2}\) and \(t=1/3\)
give exactly \(M_W\), confirming the parameter orientation. The
independent checker also directly enumerates ladders for \(m=3,4,5,6\)
on \(W=\begin{pmatrix}1&4\\4&9\end{pmatrix}\) and verifies both the
trace identity and the Hölder normalization with exact integers.

## 3. Complete spectrum, inertia, and sector domination of the obstruction

For the specified nine-state matrix
\(B_*=\mathbf1\mathbf1^T-(3/20)I+(17/20)S\), every entry is
positive. It is symmetric and commutes with exchange. Its symmetric
sector has dimension six and antisymmetric sector dimension three.
The all-one vector has eigenvalue \(9-3/20+17/20=97/10\).
On its symmetric orthogonal complement the eigenvalue is \(7/10\),
with multiplicity five; on the entire antisymmetric sector it is
\(-1\), with multiplicity three. Thus its inertia is precisely six
positive and three negative eigenvalues.

This matches the full-rank \(n=3\) Rossman inertia. For actual
interpolated transfers that inertia is conditional on the relevant
Hadamard power having rank three; it is not claimed at the rank-one
endpoint \(t=1\). The counterexample's wording correctly uses the
full-rank comparison.

In the conventional normalized symmetric unordered-pair basis, the
all-one vector has coordinates one on diagonal pairs and \(\sqrt2\)
on off-diagonal pairs. Thus the full symmetric block is
\(uu^T+(7/10)I\). Its principal block indexed by the three off-diagonal
pairs is
\[
 \begin{pmatrix}27/10&2&2\\2&27/10&2\\2&2&27/10\end{pmatrix},
\]
whereas the normalized antisymmetric block is \(-I_3\). The former
therefore entrywise dominates the absolute value of the latter,
including the diagonal. This is the stated domination, rather than a
comparison of unmatched block dimensions.

Exact eigenvalue arithmetic now gives
\[
 \operatorname{tr}B_*=51/5,\quad
 \operatorname{tr}B_*-\rho(B_*)=1/2,\quad
 \lambda_2+\lambda_{\min}=-3/10,
\]
and
\[
 \operatorname{tr}(B_*^5)-\rho(B_*)^5
 =5(7/10)^5-3=-43193/20000<0.
\]
Therefore the listed generic structural properties, even jointly, do
not imply the desired fifth-moment inequality.

## 4. This matrix is outside the actual product family

Any actual \(M(t)\) recovers \(A_{ij}^2\) on its diagonal.
The obstruction would therefore require
\(A_{01}^2=17/20\) and
\(A_{00}^2=A_{11}^2=17/10\). Nonnegativity of \(A\) then forces
\[
 M(t)_{01,10}
 =(17/20)^t(17/10)^{1-t}\le17/10.
\]
The actual entry is \(37/20\), which exceeds that upper bound.
This excludes every interpolation parameter \(t\in[0,1]\), not just
the ladder value \(1/3\). It is therefore no counterexample to
Rossman's product-family conjecture or to Sidorenko. The missing
product constraints are an essential scope boundary.

## 5. Searches: verified implementation and minor qualifications

The saved spectral searches evaluate actual symmetric transfers and
have the stated 100, 100, and 120 starts. Their best objectives are
\(8.22\times10^{-14}\), \(-4.44\times10^{-16}\), and
\(6.35\times10^{-15}\), respectively, so no reliable negative value
was found. The normalized host matrices are numerically close to
rank one, with nonleading Frobenius singular-value fractions of about
\(4.29\times10^{-7}\), \(1.03\times10^{-8}\), and
\(9.32\times10^{-8}\). These observations support the description of
the saved numerical output, without giving a certificate.

One comment in `continuation_20261002_spectral_obstruction_search.py`
reverses the pseudo-positive inequality. For \(p<q\), Rossman's
nonincreasing pseudo-norm requires
\(\log S_p/p-\log S_q/q\ge0\), rather than \(\le0\).
The implemented objective is precisely that difference and is minimized
to look for negative values, so the code searches the correct direction.
Only its explanatory comment is incorrect.

The radial search checks the gradient once before its multi-start loop,
at one random point per program invocation. It does not repeat that
finite-difference check before every individual optimization start.
Thus the proof note's phrase "before each run" should be read as a
script invocation, or clarified accordingly. This is a reporting detail,
not a claimed mathematical certificate. Radial smoothing would give the
lower bound on the regular-host class by setting \(\tau=0\); it does
not supply an arbitrary-host reduction by itself. The note correctly
does not assert an unrestricted solution or interpret a radial failure
as a Sidorenko counterexample.

I independently compared the actual search gradients with centered
finite differences at fresh nonsingular four-state points: shortest and
longer majorization objectives, the pseudo-norm objective, and the radial
objective all agree with maximum absolute errors below
\(5.5\times10^{-11}\). This supports the numerical implementations;
it proves no global spectral inequality.

## 6. Remaining spectral step and independent artifacts

Rossman's primary transfer identity reduces ML10 to
\(\operatorname{tr}(M_W^5)\). His Rayleigh-vector argument gives
\(\rho(M_W)\ge n^2(\operatorname{mean}W)^3\): use the vector
\(\sqrt{W_{ij}}\), its C4 quotient, and the C4 Sidorenko bound.
Thus \(\operatorname{tr}(M_W^5)\ge\rho(M_W)^5\) would indeed be a
sufficient full step. The present bound \(\rho(M_W)\le\operatorname{tr}M_W\)
does not establish it, and the exact generic matrix demonstrates why
the listed structural assumptions alone are insufficient. The note
preserves this unresolved gap correctly.

New separate artifacts are `operator_boundaries_ant_independent_check.py`
and `operator_boundaries_ant_independent_checks.json`. Exact arithmetic
constructs a full rational eigenbasis of rank nine, verifies every
eigenvalue directly, computes the fifth power independently, checks both
sector blocks and the incompatible exchange entry, and verifies the
ladder normalization by direct enumeration. Numerical gradient checks
are explicitly separated from exact arithmetic in the report. The
original obstruction script/JSON were inspected but not overwritten.

This is a valid method-obstruction checkpoint and a valid elementary
global upper bound. It is neither a new solution of unrestricted ML10
nor a counterexample to the actual Rossman or Sidorenko conjectures.
