# B18 — exact zero-selector-credit unequal-MUX frontier closed

**Classification:** `ESSENTIAL_STEP_APPLIED / ZERO_CREDIT_MUX_LINE_CLOSED / FULL_FEI_OPEN`.

Full uniform-cube Friedgut–Kalai Fourier entropy–influence remains **OPEN / NOT PROVED**. This report closes the first explicit missing scalar implication in the newest compatible unequal-data MUX interface. It does **not** prove the full unequal-MUX theorem, the arbitrary prime-gate inequality, or FEI.

Execution context: `WITHOUT_VERIFIED_BRAIN`. Mathematical dependencies were read directly from authenticated private repositories; no native brain receiver/context was used.

## 1. Exact live candidate and peer theorem applied

Use
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,\qquad a^\dagger=4(C^\dagger-C_0)=0.268204856,
\]
\[
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z),
\]
where \(\Gamma_0\) is the committed h96 read-once value-iteration candidate, pinned by Git blob
`1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.

The exact other-account result consumed and applied is

`account04/B18/20260922T045533Z-mux-joint-credit-collapse/REPORT.md`.

Its Theorem 5.1 proves that the selector Shannon credit of an interior one-bit MUX vanishes only on
\[
t=\frac12,\qquad q_0=\frac12\quad\text{or}\quad q_1=\frac12.
\]
Its Theorem 7.1 reduces either zero-credit line, after swapping data inputs if necessary, to
\[
Z(s):=C^\dagger-2+\frac12\Gamma^\dagger(s)
-\Gamma^\dagger\!\left(\frac14+\frac{s}{2}\right),
\qquad 0\le s\le1.
\tag{1.1}
\]
The peer report left the universal sign
\[
\boxed{Z(s)\ge0\quad(0\le s\le1)}
\tag{1.2}
\]
open. **(1.2) is the first essential missing inference attacked here.**

A second named dependency is the completed account02/B12 result
`account02/B12/20260922T045519Z-complementary-mux-fourstep/REPORT.md`.
Writing
\[
B:=\frac{C^\dagger}{2}+2=5.260925607,
\]
it proves
\[
\boxed{\Gamma^\dagger(s)\ge V_sB=4s(1-s)B}\qquad(0\le s\le1).
\tag{1.3}
\]
This theorem is used materially in the large-\(s\) branch below.

## 2. Source envelope from the pinned h96 candidate

For \(0<z\le1/2\), put
\[
x=\log_2(1/z),\qquad \Gamma_0(z)=zG(x),\qquad \alpha:=2(C_0-4)=4.9096.
\]
The committed h96 source output records
\[
\min_x[G(x)-\alpha x]=2.22922\ldots,\qquad
\max_x[G(x)-\alpha x]=8.62812\ldots.
\]
The source interpolates \(G\) linearly in \(x\), and its terminal tail has slope \(\alpha\). Hence the wobble is linear on each source segment and constant on the tail. With the deliberately weaker rounded bounds
\[
w_-=2.229,\qquad w_+=8.629,
\]
we have, for every \(0<z\le1/2\),
\[
\boxed{
L(z):=z(\alpha\log_2(1/z)+w_-)+a^\dagger z(1-z)
\le\Gamma^\dagger(z)
\le
U(z):=z(\alpha\log_2(1/z)+w_+)+a^\dagger z(1-z).
}
\tag{2.1}
\]
The source value
\[
\Gamma^\dagger(1/4)=4.5050884105
\]
gives
\[
\boxed{Z(0)=C^\dagger-2-\Gamma^\dagger(1/4)=0.0167628035>0.}
\tag{2.2}
\]

## 3. Local source-segment branch: \(0\le s\le1/50\)

Put
\[
u(s)=\frac14+\frac{s}{2},\qquad Q(s)=C^\dagger-2+\frac12L(s)-\Gamma^\dagger(u(s)).
\tag{3.1}
\]
Then \(Z(s)\ge Q(s)\). On this interval \(1/4\le u\le0.26\), so the source argument traverses only 21 fixed interpolation segments of the pinned h96 candidate. If such a segment has slope
\[
m_j=\frac{G_{j+1}-G_j}{x_{j+1}-x_j},
\]
then
\[
(\Gamma^\dagger)'(u)=G(x)-\frac{m_j}{\ln2}+a^\dagger(1-2u).
\tag{3.2}
\]
Also
\[
L'(s)=\alpha\left(\log_2\frac1s-\frac1{\ln2}\right)+w_-+a^\dagger(1-2s),
\tag{3.3}
\]
which decreases with \(s\). On each of the 21 source segments, taking (3.3) at the right endpoint, the larger source endpoint value of \(G\), and the adverse quadratic derivative gives a rigorous lower derivative bound. Across all segments,
\[
\boxed{Q'(s)>2.8826172255>0.}
\tag{3.4}
\]
The least lower bound occurs at the source wiggle immediately above \(u=1/4\) (source segment index 511), so that wiggle is explicitly retained rather than hidden behind a false global monotonicity assertion. Combining (3.4) with (2.2),
\[
\boxed{Z(s)>0\qquad(0\le s\le1/50).}
\tag{3.5}
\]

## 4. Source-tail envelope branch: \(1/50\le s\le1/10\)

By (2.1),
\[
Z(s)\ge L_1(s):=C^\dagger-2+\frac12L(s)-U(u(s)).
\tag{4.1}
\]
The derivative simplifies exactly:
\[
L_1'(s)=\frac12\left[
\alpha\log_2\frac{u(s)}s+(w_--w_+)+a^\dagger\left(\frac12-s\right)
\right].
\tag{4.2}
\]
For \(s\le1/10\), \(u(s)/s=1/(4s)+1/2\ge3\) and \(1/2-s\ge0.4\), so
\[
L_1'(s)\ge\frac12\left[4.9096\log_2 3-6.4+0.4(0.268204856)\right]>0.7444.
\tag{4.3}
\]
At the left endpoint,
\[
L_1(1/50)>0.0479544.
\tag{4.4}
\]
Hence
\[
\boxed{Z(s)>0\qquad(1/50\le s\le1/10).}
\tag{4.5}
\]

## 5. Complementary-MUX branch: \(1/10\le s\le1/2\)

Now apply account02/B12's theorem (1.3):
\[
Z(s)\ge L_2(s):=C^\dagger-2+2Bs(1-s)-U(u(s)).
\tag{5.1}
\]
Since
\[
U''(z)=-\frac{\alpha}{z\ln2}-2a^\dagger,
\]
we have
\[
L_2''(s)=-4B+\frac{\alpha}{4u(s)\ln2}+\frac{a^\dagger}{2}.
\tag{5.2}
\]
On \(s\in[1/10,1/2]\), \(u(s)\ge0.3\). Even the coarse bound \(\ln2>0.69\) gives
\[
\boxed{L_2''(s)<-14.9<0.}
\tag{5.3}
\]
so \(L_2\) is concave, and its minimum is at an endpoint. The conservative source envelope gives
\[
L_2(1/10)>0.26545,\qquad L_2(1/2)>0.31596.
\tag{5.4}
\]
Therefore
\[
\boxed{Z(s)>0\qquad(1/10\le s\le1/2).}
\tag{5.5}
\]

Combining (3.5), (4.5), and (5.5) proves (1.2) on \([0,1/2]\). For \(s'=1-s\), symmetry of \(\Gamma^\dagger\) gives
\[
\Gamma^\dagger(s)=\Gamma^\dagger(s'),
\]
and
\[
\Gamma^\dagger\!\left(\frac14+\frac{s}{2}\right)
=\Gamma^\dagger\!\left(1-\frac14-\frac{s}{2}\right)
=\Gamma^\dagger\!\left(\frac14+\frac{s'}{2}\right),
\]
so \(Z(s)=Z(1-s)\). Thus:

### Theorem 5.1 — exact zero-selector-credit MUX line

For the fixed source candidate \(\Gamma^\dagger\),
\[
\boxed{
C^\dagger-2+\frac12\Gamma^\dagger(s)
-\Gamma^\dagger\!\left(\frac14+\frac{s}{2}\right)>0
\qquad(0\le s\le1).
}
\tag{5.6}
\]
By account04/B18 Theorems 5.1 and 7.1, **both exact zero-selector-credit lines of the one-bit unequal-data MUX satisfy the live all-gate inequality.**

## 6. Old and new missing implications

**Old first missing implication (now proved):** establish (1.2), the scalar zero-credit frontier of the exact account04/B18 MUX collapse.

**New first missing implication:** extend positivity from the two zero-credit lines to the full three-dimensional unequal-data MUX cube. The correct next statement must retain the exact selector information credit from account04/B18 together with the account04/B12 data-pivot cross-deficit constraints. A natural next target is a quantitative collar: prove that sufficiently near either zero-credit line the positive selector credit dominates the possible scalar loss, then use the strictly positive selector-credit floor on compact subsets away from those lines. Only after full MUX closure should the campaign return to arbitrary composition-prime gates.

This is a genuine narrowing of the live candidate, not evidence that full FEI has converged.

## 7. Verification and provenance

- Pinned h96 candidate blob: `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`.
- Source output `cert_vi_h96k40.out` reports wobble min `2.22922`, max `8.62812`.
- Adjacent `check_zero_credit_line.py` loads and Git-hashes the existing NPZ and verifies only the new scalar inequalities. It does **not** regenerate the candidate or rerun the settled read-once proof.
- Adjacent `PRECHECK_OUTPUT.txt` records this invocation's robust numerical sign margins. It explicitly does not represent the repo-local checker as having been executed against a materialized NPZ in this connector environment.

**Final classification:** `ESSENTIAL_STEP_APPLIED`. **Full FEI remains OPEN / NOT PROVED.**
