# B05 / A023: negative first-step credits delimit the data-prefix mechanism

Run ID: `20261011T222410Z-account01-B05-credit-boundary-a023`  
Primary packet: `A023` (Amortized rarity budget)  
Stable gap / obstruction: `B05_RARE_REFUNDS` / `O-B05`  
Attempt: `A023-CREDIT-BOUNDARY-3`  
Full FEI status: **OPEN**

## 1. Objective and prior value

The previous A023 run proved a positive family theorem for the activated
quadratic bent one-point defect.  Querying one coordinate from each quadratic
pair produces nonnegative single-use order-swap credits

\[
\Gamma_m=L_m-\frac12L_{m+1}\ge0
\]

which telescope the rare \(dk\) term and leave an \(O(d)\) terminal selector
packet.  The exact next question was whether this is a structural
one-point-defect phenomenon, or whether the equal bent spectrum is essential.

This run proves the boundary:

* there is an exact pairwise formula for the order-swap credit of every
  Boolean one-point defect;
* the summands and their total need not be nonnegative;
* for the genuine \(n\)-variable AND-type gate, every coordinate has negative
  credit for every \(n\ge3\), with a logarithmic wrong-way term
  \(-2n4^{-n}(1+o(1))\);
* for the unequal prime-gate tensor \(q_4\otimes q_5\), all nine physical
  coordinates have rigorously negative credit.

Thus the previous bent telescope does **not** extend under unchanged
hypotheses to arbitrary prime factors or arbitrary Boolean one-point defects.
Any universal A023 payment must permit signed intermediate credits and prove
global amortization, or impose a structural coordinate-selection condition.
This is a no-go theorem for that mechanism, not a counterexample to FEI.

## 2. General one-point-defect ledger

Use \(\{0,1\}^n\) only to place the exceptional point at the origin; the
Fourier characters and normalization are the standard uniform-cube ones.
Let

\[
b:\{0,1\}^n\to\{-1,1\},\qquad b(0)=1,
\]

and let

\[
b'=b-2\mathbf 1_{\{0\}}.
\]

With a fresh physical selector \(y\), define

\[
s(y,x)=\frac{b(x)+b'(x)}2+
       y\frac{b(x)-b'(x)}2.
\]

Put \(\delta=2^{-n}\), and, in bits, define

\[
\phi(t)=t\log_2\frac1t,
\qquad
\Psi(a,e)=\phi(a^2)+\phi(e)-\phi(a^2+e).
\]

Since the point flip subtracts \(2\delta\) from every Fourier coefficient,
the selector midpoint and half-difference at frequency \(S\) are

\[
a_S=\widehat b(S)-\delta,
\qquad v_S=\delta.
\]

Consequently its conditional-label packet is exactly

\[
\boxed{
L_n(b)=\sum_{S\subseteq[n]}
\Psi\bigl(\widehat b(S)-\delta,\delta^2\bigr).
}\tag{1}
\]

## 3. PROVED: exact pairwise order-swap formula

Query physical coordinate \(i\) before the selector.  On the branch
\(x_i=1\), the origin is excluded and \(b=b'\), so the remaining selector
packet is zero.  On the branch \(x_i=0\), write \(b_0\) for the restricted
background.  The raw order-swap credit is therefore

\[
\Gamma_i(b)=L_n(b)-\frac12L_{n-1}(b_0).
\tag{2}
\]

For every \(T\subseteq[n]\setminus\{i\}\), Fourier restriction gives

\[
\widehat {b_0}(T)=\widehat b(T)+\widehat b(T\cup\{i\}).
\]

Set

\[
x_T=\widehat b(T)-\delta,
\qquad
y_T=\widehat b(T\cup\{i\})-\delta.
\]

The midpoint and selector half-difference in the surviving child are then
\(x_T+y_T\) and \(2\delta\).  Substitution in (1) proves

\[
\boxed{
\Gamma_i(b)=
\sum_{T\not\ni i}G_\delta(x_T,y_T),
}\tag{3}
\]

where

\[
\boxed{
G_\delta(x,y)=
\Psi(x,\delta^2)+\Psi(y,\delta^2)
-\frac12\Psi(x+y,4\delta^2).
}\tag{4}
\]

Equations (3)--(4) have no approximation.  They expose the missing condition
in the bent proof: coherent Fourier merging can make \(G_\delta\), and even
its complete sum, negative.  The bent support/sign counts create a positive
aggregate; positivity is not a consequence of entropy concavity alone.

## 4. PROVED: an unbounded prime-gate no-go family

Let

\[
q_n(x)=
\begin{cases}
1,&x=0,\\
-1,&x\ne0.
\end{cases}
\]

Up to input/output sign conventions this is the genuine \(n\)-input
AND/OR gate.  Its one-point flip is the constant \(-1\) function.  Its
Fourier coefficients are

\[
\widehat q_n(\varnothing)=-1+2\delta,
\qquad
\widehat q_n(S)=2\delta\quad(S\ne\varnothing).
\]

All coordinates are symmetric.  Define

\[
F(x)=\Psi(1-x,x^2).
\]

Equation (1) gives

\[
L_n(q_n)=F(\delta)+2\delta-2\delta^2.
\tag{5}
\]

The surviving restriction is \(q_{n-1}\), with exceptional mass
\(2\delta\).  Hence every coordinate has the exact credit

\[
\boxed{
\Gamma_n=
F(\delta)-\frac12F(2\delta)+2\delta^2.
}\tag{6}
\]

### Negativity for every \(n\ge3\)

Write

\[
F(x)=2x^2\log_2\frac{1-x}{x}+R(x),
\]

where

\[
R(x)=\bigl((1-x)^2+x^2\bigr)
\log_2\left(1+\frac{x^2}{(1-x)^2}\right).
\]

For \(0<x\le1/8\),

\[
0\le R(x)
\le \frac{x^2}{\ln2}
\left(1+\frac{x^2}{(1-x)^2}\right).
\tag{7}
\]

Dropping the nonpositive term \(-R(2x)/2\) in (6), using
\(x=2^{-n}\), and noting that

\[
\frac{1-x}{(1-2x)^2}\le\frac{14}{9}
\qquad(0<x\le1/8),
\]

gives

\[
\frac{\Gamma_n}{x^2}
\le
2\left[-n+3+\log_2\frac{14}{9}\right]
+\frac{50}{49\ln2}.
\tag{8}
\]

The right side is negative for \(n\ge5\).  Exact rational log intervals
certify

\[
\Gamma_3<-0.0048,
\qquad
\Gamma_4<-0.0112.
\]

Therefore

\[
\boxed{
\Gamma_i(q_n)<0
\quad\text{for every }n\ge3
\text{ and every physical coordinate }i.
}\tag{9}
\]

The logarithmic scale is explicit.  From

\[
F(x)=x^2\bigl(2\log_2(1/x)+\log_2 e\bigr)+O(x^3)
\]

we obtain

\[
L_n(q_n)
=2\delta+
\delta^2\bigl(2n+\log_2 e-2\bigr)+O(\delta^3),
\tag{10}
\]

and

\[
\boxed{
\Gamma_n=
\delta^2\bigl(-2n+6-\log_2 e\bigr)+O(\delta^3).
}\tag{11}
\]

Thus pushing the selector below any data coordinate increases the expected
remaining selector packet by \((2+o(1))n\delta^2\).  The rare logarithm is
not erased; it appears as a negative order-swap credit.

If this core is activated on an independent control event of probability
\(p\), all quantities in (5)--(11) are multiplied by \(p\).  Rare
restriction therefore preserves the sign and leaves a wrong-way term
\(-(2+o(1))pn\delta^2\).

## 5. PROVED: unequal prime tensor with no good first coordinate

The failure is not confined to a single large gate.  Let

\[
b=q_4\otimes q_5
\]

on disjoint variables and flip only its global origin.  This is an exact
tensor of two unequal genuine prime Boolean gates before the one-point
surgery.

For \(q_r\), put \(D_r=2^{-r}\).  Its Fourier coefficient is
\(-1+2D_r\) at the empty set and \(2D_r\) elsewhere.  Therefore the
four coefficient classes of \(q_a\otimes q_b\), with their multiplicities,
are

\[
\begin{array}{c|c}
\text{coefficient}&\text{multiplicity}\\ \hline
(-1+2D_a)(-1+2D_b)&1\\
2D_a(-1+2D_b)&2^a-1\\
(-1+2D_a)2D_b&2^b-1\\
4D_aD_b&(2^a-1)(2^b-1).
\end{array}
\tag{12}
\]

Substituting these rational values into (1), and using (2), gives two
coordinate classes.  Rigorous rational logarithm intervals certify

\[
\boxed{
\begin{aligned}
\Gamma_{q_4\text{-coordinate}}
&<-0.00022,\\
\Gamma_{q_5\text{-coordinate}}
&<-0.00026.
\end{aligned}
}\tag{13}
\]

By symmetry, all four coordinates in the first factor and all five in the
second have the corresponding sign.  Hence this unequal near-tensor has no
physical coordinate with a nonnegative first-step credit.

## 6. Exact no-go scope

The following statement is refuted:

> For every genuine Boolean one-point-defect selector pair, there exists a
> physical data coordinate whose first data/selector order-swap credit is
> nonnegative.

It is already refuted by every \(q_n\), \(n\ge3\), and independently by
the unequal \(q_4\otimes q_5\) factor test.

The following stronger-looking conclusions are **not** justified:

* no signed multi-step telescope exists;
* no stopping tree can amortize the complete packet;
* every coordinate remains negative after conditioning;
* the full entropy decrement is negative or violates an influence bound;
* FEI fails for AND, tensors, or one-point defects.

The no-go concerns the particular nonnegative, nodewise, single-use
order-swap currency used in the preceding bent proof.

## 7. Mandatory falsifiers

* **Sparse one-point defects:** equations (1)--(4) are derived for an arbitrary
  genuine Boolean one-point flip.
* **Rare restrictions:** independent activation multiplies every packet and
  credit by the same reach probability and preserves the negative sign.
* **Near tensors:** \(q_4\otimes q_5\) has unequal disjoint prime factors and
  negative credit in all coordinates.
* **Actual prime Boolean gates:** \(q_n\) is an AND/OR gate up to signs and
  relabeling.
* **Addressing:** direct checks for address width \(r=2,3\) find positive
  address-coordinate credits but negative data-coordinate credits.  Thus
  addressing rejects an all-coordinate positivity claim but does not reject
  an existentially selected coordinate.
* **Bent controls:** the prior quadratic bent credits remain nonnegative for
  \(k=2,4,6,8,10\), confirming that the new negative examples delimit rather
  than contradict the preceding theorem.
* **Shared-variable interference:** formula (3) retains the coherent
  \(x_T+y_T\) merge, the precise source of the sign failure.
* **Parity erasure and phase:** no parity lower bound is invoked, and no
  selector phase/JS packet is discarded.  The claim is solely about the
  conditional-label component \(L\).

## 8. Verification

`credit_boundary_checker.py` uses exact `fractions.Fraction` arithmetic and
a rigorously remainder-bounded atanh series for every logarithm in the finite
certificates.  It reports:

* 20 rigorous negative interval assertions: \(q_n\), \(3\le n\le20\),
  plus the two \(q_4\otimes q_5\) coordinate classes;
* 1,050,144 exact Walsh restriction identities over every Boolean truth table
  with \(b(0)=1\) in dimensions \(2,3,4\);
* 3,760 negative coordinate credits in that exhaustive finite enumeration;
* bent controls through \(k=10\);
* addressing controls through \(r=3\).

Command:

\[
\texttt{python3 credit\_boundary\_checker.py}
\]

No randomness or seed is used.  The exhaustive floating evaluations locate
sign patterns; the displayed AND and unequal-tensor signs are certified by
the rational intervals and the all-\(n\) AND theorem is analytic.

## 9. Primary-literature overlap check

González--MacManus--Pereyra, *Further evidence towards the
Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, explicitly frames
FEI induction through a well-chosen splitting variable and stopping binary
trees, and gives examples where a wrong splitting variable fails a stronger
surrogate inequality.  Wan--Wright--Wu, arXiv:1312.3003, and
O'Donnell--Tan, arXiv:1304.1347, supply the established decision-tree and
composition context.

The present result is compatible with those sources: it concerns the sign of
one exact selector/data order-swap component, not their full entropy split.
No external-literature novelty claim is made.  The campaign delta is the
source-pinned formula (3), the all-\(n\) AND sign theorem, and the exact
unequal-factor witness.

## 10. Status and next action

Claim `B05-A023-ORDER-SWAP-CREDIT-BOUNDARY-v1` is
**ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW**.

This is substantive progress on A023 because it precisely identifies the
unpaid hypothesis in the positive bent transport and prevents an invalid
universalization.  A023 remains **OPEN / PARTIAL_PROGRESS**: a universal
signed amortization, if true, is still missing.

The next attempt should retain the signed credits and test a two-level
potential

\[
\Gamma_i(b)+
\frac12\mathbf E\bigl[\Gamma_j(b_{x_i})\mid
\text{defect survives}\bigr],
\]

with a stopping rule allowed to choose the second coordinate from the
restricted spectrum.  The first target is the \(q_n\) family: determine
whether the accumulated negative \(n\delta^2\) term is exactly paid by the
terminal \(2\delta\) packet or by an influence decrement without reusing
either quantity.  Only after that should the potential be tested on
addressing and the bent family.

Independent review is requested from A087 or A094.  The reviewer should
reconstruct (3), the bound (8), the \(n=3,4\) interval certificate, and both
coordinate classes in (13).

## 11. Immutable inputs

* Positive bent prefix: open-problems commit
  `6cb946b93c2506310f15deda852cc40cd4cd2181`, report blob
  `c0353372b1e896045504067fb77724f588397527`.
* Accepted local no-go: open-problems commit
  `80cc2e5027efa56d79c4ecdf7d4949759ef2068b`.
* B05 contract blob:
  `05447e6d999437bb82a266b427bd76a4b37266b6`.
* Campaign status blob:
  `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.
* Obstruction registry blob:
  `dd482025647aed25166b46cc217a7ed77dcaa767`.

No protected evaluation material, held request, scheduler state, email,
public release, merge, or live-store mutation was accessed.

## 12. Execution metadata

The runtime exposed Codex based on GPT-5.  No separate model selector,
reasoning-effort selector, continuous-hour guarantee, billing identity, or
remaining allowance meter was exposed.  Natural derivation, computation,
persistence, review, and ingestion are recorded separately.
