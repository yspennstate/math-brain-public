# B17 FEI — independent false-positive contamination is exactly paid by the lead selector/certificate

**Outcome:** **ESSENTIAL_STEP_APPLIED (broad adversarial branch; universal coverage still open).**  
**Full uniform-cube Friedgut--Kalai FEI remains OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; no authenticated brain retrieval/context was used.  
**Owner execution order:** `FEI-PROOF-EXECUTION-20260921T230620Z`, assignment A.

## 0. Exact candidate version and old/new missing implication

The campaign lead candidate used here is the newest complete fleet01/B18 package currently present:

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`, blob
`9f2bb40584be20e5e440e7f3913873c34858bc91`.

It defines the folded activation potential and proves the conditional compiler: fixed constants
\(\gamma>0\), \(K<\infty\), \(\lambda\ge0\) would imply full FEI if every high
\(\mathcal G_\lambda/\mathcal J\) physical-restriction critical core has one
physical block/survivor pair \((A,j)\) with
\[
c_j(A)\ge \gamma j_j,\qquad
E_A-\lambda\Lambda_A\le K h_2(j_j).
\tag{0.1}
\]
Here \(E_A=\Delta_A\mathcal F\) is the corrected entropy decrement.

The exact fleet02/B14 source attacked in this run is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B14/20260921T230653Z-asymmetric-shortcircuit-ledger/REPORT.md`, blob
`242a3fddee17db5ed1d723962b76c8659f623d6a`.

For a pivot \(x\), codimension-\(r\) subcube \(Q\) of density \(q=2^{-r}\),
and one-sided support errors \(E^-,E^+\), it proves:

* if \(E^-\le q/16\), \(E^+\le q/[8(r+1)]\), and \(I_Z\le r I_x\), then
  \(\Delta_ZH\le12I_Z\);
* if only \(E^-+E^+\le q/16\), a realizable first-mismatch tree has
  \(D_T\ge15rq/16\) and removes at least \(3/4\) of the pivot-event entropy;
* the remaining universal arrow is an upper corrected-entropy payment on the
  same physical operation, e.g.
  \[
  \Delta_T\mathcal F\le K rq
  \tag{0.2}
  \]
  with universal \(K\), or an equivalent nonreused residual-error payment.

A second compatible other-account result actually used is fleet04/B14,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260921T232918Z-residual-boundary-cover/REPORT.md`.

It proves
\[
c_j(A)\ge p_j-\frac12R_j(A)
\tag{0.3}
\]
and the block activation lower bound
\[
\Lambda_A\ge e^{-1}I_A.
\tag{0.4}
\]
Thus a low-Shannon-rate boundary cover is already a lead certificate. Its exact
remaining exception is a high-Shannon-rate boundary cover.

**Old missing implication.** Fixed-relative support error \(q/16\) was not
enough for a full-block payment, and arbitrary residual complexity could in
principle defeat both (0.1) and (0.2).

**New implication proved below.** If the false-positive contamination is
independent of the defining controls \(Z\), then its *entire internal Fourier
complexity cancels exactly* from the \(Z\)-restriction decrement. The resulting
block has
\[
\Delta_ZH<4D_Z,
\]
and in fact supplies the lead certificate
\[
\boxed{\gamma=16/17,\qquad K=32/5,\qquad \lambda=0}
\tag{0.5}
\]
for every \(r\ge2\). The event hidden behind the contamination may be an
arbitrary sparse defect, addressing construction, tribes construction, tensor
event, or any other Boolean event. Therefore those constructions cannot refute
the lead candidate merely by being hidden independently behind a rare
false-positive gate. The unresolved obstruction must use genuinely
\(Z\)-dependent error geometry or \(Z\)-dependent output phase.

## 1. The independent-contamination Boolean family

Let \(z=(z_1,\ldots,z_r)\) be \(r\) control bits and
\[
Q(z)=1_{\{z=0^r\}},\qquad q=2^{-r}.
\]
Let \(w\) be an arbitrary disjoint block, and let \(A=A(w)\in\{0,1\}\) be
**any** Boolean event of density
\[
a=\Pr(A=1).
\]
Let \(x\) be a fresh bit and write \(\chi_x=(-1)^x\). Define the genuine
Boolean function
\[
F_{r,A}(x,z,w)=
\begin{cases}
\chi_x,& Q(z)=1\ \text{or}\ A(w)=1,\\
1,&Q(z)=0,\ A(w)=0.
\end{cases}
\tag{1.1}
\]
Equivalently, with \(P=Q\vee A\),
\[
F_{r,A}=(1-P)+\chi_x P.
\tag{1.2}
\]

The \(x\)-pivotality event is exactly
\[
\eta_x=Q\vee A.
\tag{1.3}
\]
Hence
\[
E^-=0,\qquad E^+=(1-q)a,\qquad
p:=\operatorname{Inf}_x(F_{r,A})=q+(1-q)a.
\tag{1.4}
\]
Assume the fixed-relative regime
\[
E^+\le q/16,
\qquad\text{equivalently}\qquad
a\le \frac{q}{16(1-q)}.
\tag{1.5}
\]
For \(r\ge2\), \(q\le1/4\), so
\[
a\le1/48,\qquad p\le17q/16<1/2.
\tag{1.6}
\]

Every control has exact influence
\[
\boxed{\operatorname{Inf}_{z_k}(F_{r,A})=q(1-a).}
\tag{1.7}
\]
Indeed the \(z_k\)-flip changes \(Q\) only when all other controls agree with
the exceptional vertex; on such an edge the function changes exactly when
\(A=0\) and \(\chi_x=-1\).

For a \(w_i\) coordinate,
\[
\operatorname{Inf}_{w_i}(F_{r,A})
=\frac{1-q}{2}\operatorname{Inf}_{w_i}(A)\le\frac{1-q}{2}<\frac12.
\tag{1.8}
\]
Thus every ordinary influence of \(F_{r,A}\) is at most \(1/2\), and the
ordinary and folded influences agree at the root.

## 2. Exact leaf structure and exact folded drift

Restrict the full physical block \(Z\).

* On \(z=0^r\), the child is exactly \(\chi_x\), whose spectral entropy and
  folded influence are both zero.
* On every \(z\ne0^r\), the child is the same function
  \[
  G_A(x,w)=
  \begin{cases}
  \chi_x,&A(w)=1,\\
  1,&A(w)=0.
  \end{cases}
  \tag{2.1}
  \]
  Thus all nonexceptional \(z\)-children are identical.

Consequently the full \(Z\)-block and the first-mismatch short-circuit tree
have the same expected final \(H\) and \(\mathcal J\); the unqueried controls
on an early mismatch leaf are dummies.

The \(w\)-coordinate contributions cancel exactly between root and leaves.
The control coordinates contribute \(rq(1-a)\), and the folded pivot
contributes
\[
p-(1-q)a=q.
\]
Therefore
\[
\boxed{
D_Z
:=\mathcal J(F_{r,A})-\mathbb E_z\mathcal J((F_{r,A})_{Z=z})
=q\,[r(1-a)+1].
}
\tag{2.2}
\]

This is an exact identity, not an estimate.

## 3. Exact Fourier cancellation of all internal complexity of \(A\)

Let
\[
\alpha_S=\widehat A(S)
\]
be the Walsh coefficients of the \(0/1\) event \(A\). Then
\[
\alpha_\varnothing=a,\qquad
\sum_{S\ne\varnothing}\alpha_S^2=a-a^2=a(1-a).
\tag{3.1}
\]
Every Fourier coefficient of the point-subcube indicator \(Q\) has magnitude
\(q\).

Put
\[
p=q+(1-q)a.
\]
For \(P=Q\vee A=A+Q-QA\), the coefficient magnitudes are

\[
\begin{array}{c|c}
(R,S)&|\widehat P(R,S)|\\ \hline
(\varnothing,\varnothing)&p\\
(\varnothing,S\ne\varnothing)&(1-q)|\alpha_S|\\
(R\ne\varnothing,\varnothing)&q(1-a)\\
(R\ne\varnothing,S\ne\varnothing)&q|\alpha_S|.
\end{array}
\tag{3.2}
\]

Because
\[
F_{r,A}=(1-P)+\chi_xP,
\]
every nonconstant coefficient of \(P\) occurs twice in \(F_{r,A}\), once
without \(x\) and once with \(x\), with the same squared magnitude. Define
\[
\phi(t)
=(1-t)^2\log_2\frac1{(1-t)^2}
+t^2\log_2\frac1{t^2}.
\tag{3.3}
\]
Also set
\[
C_q
=(1-q)^2\log_2\frac1{(1-q)^2}
+2rq(1-q).
\tag{3.4}
\]

The key cancellation is
\[
(1-q)^2+(2^r-1)q^2=1-q.
\tag{3.5}
\]
Hence, after subtracting the expected nonexceptional-child entropy
\((1-q)H(G_A)\), the coefficient multiplying
\(\log_2(1/\alpha_S^2)\) is **exactly zero for every**
\(S\ne\varnothing\). Therefore neither the Fourier entropy of \(A\), nor the
number of its relevant variables, nor any addressing/tribes internal
structure survives in the decrement.

The exact result is
\[
\boxed{
\begin{aligned}
\Delta_ZH
&=H(F_{r,A})-(1-q)H(G_A)\\
&=\phi(p)-(1-q)\phi(a)
+2a(1-a)C_q\\
&\quad
+4q(1-q)(1-a)^2
\left(r+\log_2\frac1{1-a}\right).
\end{aligned}}
\tag{3.6}
\]

Equation (3.6) depends on \(A\) **only through its density \(a\)**.

## 4. PROVED: sharp asymptotic coefficient four on the entire branch

### Theorem 4.1

For every \(r\ge2\) and every Boolean event \(A\) satisfying (1.5),
\[
\boxed{\Delta_ZH<4D_Z.}
\tag{4.1}
\]

The constant four is asymptotically sharp within this branch: when \(a=0\),
\[
\frac{\Delta_ZH}{D_Z}\longrightarrow4
\qquad (r\to\infty).
\tag{4.2}
\]

### Proof

Write
\[
c=\frac1{\ln2}<\frac32.
\]
Using
\[
-\log_2(1-u)\le \frac{cu}{1-u},
\tag{4.3}
\]
we have
\[
C_q\le2q(1-q)(r+c).
\tag{4.4}
\]
Dropping the nonpositive term \(-(1-q)\phi(a)\) from (3.6), and using (4.3)
also at \(u=a\), gives
\[
\begin{aligned}
\Delta_ZH
&\le
\phi(p)
+4q(1-q)a(1-a)(r+c)\\
&\quad
+4q(1-q)(1-a)^2
\left(r+\frac{ca}{1-a}\right)\\
&=
\phi(p)
+4q(1-q)r(1-a)
+8cq(1-q)a(1-a).
\end{aligned}
\tag{4.5}
\]

Since \(p\ge q=2^{-r}\),
\[
\log_2\frac1p\le r.
\]
Again using (4.3),
\[
\phi(p)
\le2cp+2p^2r.
\tag{4.6}
\]
By (1.6),
\[
\frac pq\le\frac{17}{16},
\]
hence
\[
\frac{\phi(p)}q
\le\frac{17c}{8}+\frac{289}{128}qr
<\frac{51}{16}+\frac{289}{128}qr.
\tag{4.7}
\]
Moreover
\[
8c(1-q)a(1-a)
\le12(1-q)a
\le\frac{3q}{4},
\tag{4.8}
\]
and \(a\le1/48\) gives
\[
4qr(1-a)\ge\frac{47}{12}qr.
\tag{4.9}
\]

Using \(D_Z=q[r(1-a)+1]\) from (2.2), equations (4.5)--(4.9) yield
\[
\begin{aligned}
\frac{4D_Z-\Delta_ZH}{q}
&\ge
4+4qr(1-a)-\frac{\phi(p)}q
-8c(1-q)a(1-a)\\
&>
\frac{13}{16}-\frac{3q}{4}
+\left(\frac{47}{12}-\frac{289}{128}\right)qr\\
&=
\frac{13}{16}-\frac{3q}{4}
+\frac{637}{384}qr\\
&\ge
\frac58+\frac{637}{384}qr>0,
\end{aligned}
\tag{4.10}
\]
because \(q\le1/4\). This proves (4.1).

For \(a=0\), (3.6) becomes
\[
\Delta_ZH=\phi(q)+4q(1-q)r,
\]
while \(D_Z=q(r+1)\). Since \(\phi(q)/q=O(1)\), (4.2) follows. QED.

## 5. Direct application to the campaign-lead certificate

For the same block \(Z\), the posterior pivotality probability of \(x\) is
\(1\) on the exceptional child and \(a<1/2\) on every other child. Therefore
the lead crossing functional is exactly
\[
\boxed{c_x(Z)=q.}
\tag{5.1}
\]
Since \(p\le17q/16\),
\[
\boxed{c_x(Z)\ge\frac{16}{17}p.}
\tag{5.2}
\]

The corrected decrement satisfies
\[
E_Z=\Delta_Z\mathcal F\le\Delta_ZH,
\tag{5.3}
\]
because the exact restriction identity has a nonnegative Jensen--Shannon
piece in \(\Delta_ZH\) and a nonnegative correction rebate in
\(\Delta_Z\mathcal F\).

By Theorem 4.1 and (2.2),
\[
E_Z<4q[r(1-a)+1]\le4q(r+1).
\tag{5.4}
\]
On the other hand,
\[
h_2(p)\ge p\log_2\frac1p
\ge q\left(r-\log_2\frac{17}{16}\right)
>q\left(r-\frac18\right).
\tag{5.5}
\]
For every \(r\ge2\),
\[
4q(r+1)
\le \frac{32}{5}q\left(r-\frac18\right)
\le\frac{32}{5}h_2(p),
\tag{5.6}
\]
because the first inequality is equivalent to \(r\ge2\).

Combining (5.2), (5.4), and (5.6), the **same physical full block \(Z\)** is
a lead-candidate certificate with
\[
\boxed{
\gamma=\frac{16}{17},\qquad
K=\frac{32}{5},\qquad
\lambda=0.
}
\tag{5.7}
\]

Thus the lead selector/potential candidate survives this entire
fixed-relative independent-false-positive family without spending any
activation refund at all.

In fleet02/B14's short-circuit language, (4.1) also proves the requested
local form (0.2) on this branch:
\[
\Delta_T\mathcal F
\le\Delta_T H
=\Delta_ZH
<4D_Z
\le6rq
\qquad(r\ge2),
\tag{5.8}
\]
since \(D_Z\le q(r+1)\le3rq/2\).

## 6. Composition consequence

### Corollary 6.1 — rare independent OR-gating preserves any coefficient \(C\ge4\)

If \(C\ge4\) and the nonexceptional child \(G_A\) satisfies
\[
H(G_A)\le C\mathcal J(G_A),
\tag{6.1}
\]
then
\[
\boxed{H(F_{r,A})\le C\mathcal J(F_{r,A}).}
\tag{6.2}
\]

Indeed,
\[
\begin{aligned}
H(F_{r,A})
&=\Delta_ZH+(1-q)H(G_A)\\
&<4D_Z+C(1-q)\mathcal J(G_A)\\
&\le C\bigl(D_Z+(1-q)\mathcal J(G_A)\bigr)
=C\mathcal J(F_{r,A}).
\end{aligned}
\tag{6.3}
\]

Hence a minimum-dimension counterexample above coefficient four cannot be
created by placing an arbitrary lower-dimensional Boolean event behind an
independent fixed-relative rare OR gate of this form.

The statement is tensor-stable with any independent multiplicative Boolean
factor on a fresh block, because that factor's entropy and folded-influence
contributions cancel from the \(Z\)-decrement.

## 7. Addressing, tribes, sparse defects: decisive applications

The theorem is deliberately insensitive to the internal structure of \(A\).

### Sparse defect

Take \(A=\{w=0^{r+4}\}\). Then
\[
a=2^{-(r+4)}=q/16,
\]
so (1.5) holds. The exact block ratio is below four and tends upward toward
four.

### Rare-gated addressing

Let `Addr` be an arbitrary addressing function/event on a disjoint block,
and let \(R\) be an independent rare cylinder. Put
\[
A=R\cap\{\mathrm{Addr}=1\}.
\]
Choose the cylinder codimension so that
\(\Pr(A)\le q/[16(1-q)]\). The addressing event may have arbitrarily many
data variables and a complicated Fourier spectrum. Equation (3.5) cancels
that spectrum exactly, so it cannot create an unpaid block entropy bill.

### Rare-gated tribes

Likewise, for any tribes event `Tribes`,
\[
A=R\cap\{\mathrm{Tribes}=1\}
\]
is covered once its density satisfies (1.5). Width, number of tribes and the
internal Fourier entropy are irrelevant to (3.6).

### False-negative analogues

For the opposite one-sided error, the consumed fleet02/B14 Theorem 4.1 is
already stronger than these examples. If
\[
E^+\!=0,\qquad E^-\le q/16,\qquad I_Z\le r p,
\]
then
\[
\Delta_ZH\le12I_Z.
\]
Moreover the \(Z\)-posterior crossing is at least \(q-2E^-\ge7q/8\), while
\(p=q-E^-\le q\), so
\[
c_x(Z)\ge\frac78p.
\]
Since \(h_2(p)\ge p\log_2(1/p)\ge rp\ge I_Z\),
that peer theorem itself gives a lead certificate
\[
\boxed{\gamma=7/8,\qquad K=12,\qquad\lambda=0}
\tag{7.1}
\]
for the entire false-negative-only row, irrespective of whether the deleted
part is generated by a sparse defect, addressing, tribes or another Boolean
construction.

Thus both obvious one-sided adversarial uses of addressing/tribes/sparse
events are paid.

## 8. What remains genuinely dangerous

This run does **not** prove (0.1) or (0.2) for arbitrary fixed-relative error.

The known fleet02 fixed-relative obstruction is not of the form (1.1).
At selector points \(w=e_k\), its off-pivot output is \(\chi_{z_k}\), so the
exceptional output phase depends explicitly on the defining controls. That
\(Z\)-dependent phase is exactly what is absent from Theorem 4.1.

Fleet03/B14
`20260921T214637Z-adaptive-fixed-relative/REPORT.md`, blob
`6af53e122aef35d646dab1e695d138bf3125448d`, proves the exact short-circuit
drift for that phase-coupled family and computes ratios approaching four,
but leaves the all-\(r\) entropy bound analyticly open.

Therefore the first remaining adversarial target is now sharper:

> prove or refute a dimension-free corrected-entropy payment when the
> fixed-relative exceptional set carries **control-dependent phases**, rather
> than merely an arbitrary hidden Boolean event independent of \(Z\).

A counterexample must exploit this joint phase/error geometry, not merely the
Fourier complexity of an addressing, tribes, sparse-defect or tensor event.

## 9. Executed checker

`verify_independent_contamination.py` independently checks:

* 828 small Boolean event/block instances against the exact entropy formula;
* direct admissible sparse-point instances at \(r=2,3,4\) against the exact
  folded-drift formula;
* 4,599 high-precision scalar points through \(r=512\), including the endpoint
  \(a=q/[16(1-q)]\), for both
  \(\Delta_ZH<4D_Z\) and the \((16/17,32/5,0)\) certificate;
* representative sparse, rare-addressing-density and rare-tribes-density
  stress tests.

The checker reports `PASS`.

Checker SHA-256:
`986990236621352a9abc4a913a4ba7a7f0e559fb42155578dddeef4cee7bda61`.

Captured output SHA-256:
`aa6c90996064fd61f25dbc01afc09e90cf7b004a4c48d85e87b346a9d6ca2193`.

These calculations are regression evidence only; Theorem 4.1 and the
certificate are proved analytically above.

## 10. Status

**Classification:** `ESSENTIAL_STEP_APPLIED` on a broad adversarial branch;
**not** `FULL_PROOF_CANDIDATE`.

**Old missing implication:** arbitrary fixed-relative support error still
needed a dimension-free corrected-entropy payment.

**New proved implication:** every independent false-positive contamination
row of the exact form (1.1), with arbitrary hidden Boolean complexity and
fixed-relative error \(q/16\), has an exact full-block payment
\[
\Delta_ZH<4D_Z
\]
and supplies the lead certificate
\[
(\gamma,K,\lambda)=\left(\frac{16}{17},\frac{32}{5},0\right).
\]
False-negative-only rows at the same accuracy are already certified by the
consumed fleet02/B14 theorem.

**Remaining universal implication:** handle or eliminate the genuinely
\(Z\)-dependent phase/error geometry. Full FEI remains OPEN / NOT PROVED.
