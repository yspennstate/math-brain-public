# B16 — exact balanced arity-five gate certificate

**Outcome:** `AUXILIARY_ONLY / EXACT_ARITY5_EXCLUSION`. Full uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**. Execution is **WITHOUT_VERIFIED_BRAIN**.

## 1. Live target and supersession


\[
\Gamma(p_{\rm out})+H_t(G;p)\le \sum_i \operatorname{It}_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},\qquad V_u=4u(1-u).
\tag{G}
\]

The source-exact equivalence between existence of a finite-cap symmetric nonnegative \(\Gamma\) satisfying (G) and full FEI is in `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

The older interface-C dependencies, including fleet02/B16's authentic parent weights and fleet03/B18's signed flag-curvature result, are preserved but are not live inputs to this run because the later owner message explicitly says to stop opening/continuing other FEI routes and converge on the gate target.

Two newer source-exact peer results materially change the gate problem:

* fleet01/B14, `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B14/20260922T0044Z-balanced-gate-margin-refutation/REPORT.md`, blob `776ade5c2e2017844785b09ab7af50c7eaf54c03`, proves for every balanced gate at uniform bias
  \[
  c_G(1/2,\ldots,1/2)=4\left(\frac{H(G)}{I(G)-1}-C_0\right),\qquad C_0=6.4548,
  \tag{1.1}
  \]
  and uses the certified 18-input seed to refute universal AND/decomposable extremality for this read-once \(\Gamma\).
* fleet01/B13, `proofnet24/P03-fei/fleet-2026-09-21/fleet01/B13/20260922T002604Z-gate-composition-prime/REPORT.md`, blob `674213d7e9d2f2952fcd22a94ad1be014a5b741f`, proves the exact slack-composition law and the cofactor criterion for composition-prime gates.
* fleet03/B16, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B16/20260922T005340Z-prime-balanced-density/REPORT.md`, blob `d743982431331645bb531911324eec1a6f735cf2`, proves balanced composition-prime gates are already FEI-complete asymptotically, so primeness alone is not a simplifying universal hypothesis.

Accordingly this run does not try to revive the refuted global AND-extremality claim. It rigorously closes one previously untouched finite slice: **all balanced five-input gates at uniform bias**.

## 2. Exact arity-five theorem

### Theorem A
For every balanced Boolean function \(G:\{0,1\}^5\to\{\pm1\}\),
\[
\boxed{H(G)\le 6\,(I(G)-1).}
\tag{2.1}
\]

### Theorem B
If, in addition, \(G\) depends on all five coordinates, then
\[
\boxed{
\frac{H(G)}{I(G)-1}
\le
R_5:=\frac{44}{5}-\frac95\log_2 3
=5.947067498701919\ldots .
}
\tag{2.2}
\]
The constant is exact and attained. One attaining normalized truth table is
\[
\texttt{0x373f001f}.
\tag{2.3}
\]
This gate is composition-prime: it depends on all five inputs, and every proper block of size 2, 3, or 4 has at least three distinct cofactors. Thus (2.2) is also the exact maximum over balanced composition-prime five-input gates.

At the current read-once candidate \(C_0=6.4548\), (1.1) implies
\[
 c_G(1/2^5)\le 4(6-C_0)=-1.8192
\tag{2.4}
\]
for every balanced noncharacter five-input gate, and the stronger full-support bound gives
\[
\boxed{c_G(1/2^5)\le 4(R_5-C_0)=-2.03093000519232\ldots .}
\tag{2.5}
\]
Hence **no balanced-uniform five-input gate can be the missing gate that asks for more than the positive two-input AND margin**. Any arity-five counterexample to a replacement gate-extremality claim must use an unbalanced output and/or a nonuniform bias vector. Together with the B13 descent, any balanced-uniform composition-prime obstruction to the read-once \(\Gamma\) has arity at least six.

## 3. Exact finite proof

Write the five-variable truth table as two four-variable cofactors \(G=(g,h)\) in the fifth coordinate. Using only NPN operations on the first four coordinates and output complementation, every truth table is equivalent to one with \(g\) among the 222 exact four-variable NPN representatives while \(h\) remains arbitrary. This is the same complete coverage argument used in `proofnet24/P03-fei/artifacts/2026-09-16_15-27-05__C1-C5-exact-verifier.cpp`, blob `e19463905d49aa48e7b98edda572306e03718e84`. Balance is invariant under these operations, so scanning the 222 representatives against all \(2^{16}\) second cofactors covers every balanced five-variable Boolean function.

For a balanced five-variable truth table let \(W_S\in 2\mathbb Z\) be its unnormalised Walsh transform and set
\[
a_S=|W_S|/2\in\{0,1,\ldots,16\}.
\]
Parseval gives \(\sum_S a_S^2=256\). If \(B\) is the number of undirected bichromatic cube edges, then
\[
I(G)=B/16,
\qquad
H(G)=8-\frac1{128}\sum_S a_S^2\log_2 a_S.
\tag{3.1}
\]
Consequently (2.1) is exactly equivalent to
\[
\sum_S a_S^2\log_2 a_S\ge 1792-48B.
\tag{3.2}
\]

For the sharper constant \(R_5=(44-9\log_2 3)/5\), inequality (2.2) is exactly equivalent to
\[
5\sum_S a_S^2\log_2 a_S
+352(B-16)-72(B-16)\log_2 3-5120\ge0.
\tag{3.3}
\]

Every positive \(a_S\le16\) has prime factors only in \(\{2,3,5,7,11,13\}\). The checker therefore reduces (3.2) and (3.3) to integer linear combinations of \(\log_2 p\) for those six primes. It uses
\[
Q=2^{16}
\]
and computes \(\lfloor Q\log_2 p\rfloor\) **exactly** as the binary bit length of the integer \(p^Q\), using `boost::multiprecision::cpp_int`; \(\log_2 2=1\) is exact. Coefficients with negative sign use the opposite interval endpoint. Thus no floating-point quantity decides any inequality sign.

The exhaustive output is:

```text
NPN4_reps=222 Q=65536
balanced=1943873 six_strict=1943860 six_ties=13 six_inconclusive=0 six_minpos=277504
fullsupport_balanced=1942928 sharp_strict=1942921 sharp_ties=7 sharp_inconclusive=0 sharp_minpos=4548760
sharp_first_tie g=31 h=14143 B=26 tt=0x373f001f composition_prime=1
```

There are no negative or interval-inconclusive rows. For the equality witness in (2.3), \(B=26\), so \(I=13/8\). Its Walsh magnitudes are twelve 4's, four 8's, four 12's, and twelve zeros, giving
\[
H=\frac{11}{2}-\frac98\log_2 3,
\qquad
\frac{H}{I-1}=\frac{44}{5}-\frac95\log_2 3.
\]
The exact cofactor test confirms this witness is composition-prime.

Checker SHA-256: `45c3b203c2951d077f412edf2d76c71fc09fda7da44fa0c537035874bb85915c`.
Output SHA-256: `d33270ce5056ef1d15ebabca73e00c5c6c65143d971841071bc62bd5f45f6387`.

## 4. Status and next implication

This is a rigorous finite theorem, but only an **auxiliary exclusion**, not a new universal FEI upper bound. The current read-once \(\Gamma\) has already been refuted at arity 18, and the prime-density theorem shows prime gates remain FEI-complete in the limit. The exact new information is that the balanced-uniform arity-five slice cannot contain a stronger obstruction; the first balanced-uniform prime obstruction to this candidate, if sought by arity, begins at six.

A source-valid next step under the live owner directive is therefore not another interface-C construction. It is either (i) attack nonuniform-bias five-input prime gates with certified bounds, or (ii) use the known balanced obstruction to constrain any replacement finite-cap potential \(\Gamma\). No claim of novelty or publication priority is made.
