# B17 — all five-input gates at the uniform bias are paid by the certified read-once lift

**Classification:** `ESSENTIAL_STEP_APPLIED / ARITY5_UNIFORM_ALL_GATES_CLOSED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Version/change summary

This run binds to the current fixed all-gate candidate `LIMIT-PRIME-GATE-LIFT-v1` from

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0222Z-shared-graft-tail/REPORT.md`

(observed report blob `7ea2c548afc0a5fc62f972f9c64df0578f7e0838`).  That candidate fixes

\[
C_*=6.5218512,\qquad
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p)
\]

and leaves the universal composition-prime/all-bias gate inequality open.

The exact peer result used rather than repeated is fleet04/B12,
commit `e9d8c67867cce3d8eca74e2064c1c644fafb54e2`,
`fleet04/B12/20260922T041709Z-arity5-unate-tube/REPORT.md`.
It proves the balanced **unate** five-input uniform-center sector harmless.  The other
compatible adversarial result consumed is fleet03/B17,
`fleet03/B17/20260922T040248Z-asymmetric-dyadic-spine/REPORT.md`
(observed blob `6f1f5b6054a4bc8e7ee750fc952735114f3ce129`), which closes one genuinely
asymmetric five-input dyadic slice.  This run attacks the remaining central slice
in a different direction: remove both the balance and unateness restrictions.

The new theorem proves the current candidate on **every** five-input Boolean gate
at the uniform input-bias vector.  In fact it proves the stronger bound for the
smaller already-certified read-once lift `c=0.01`, hence

\[
\boxed{c_G(1/2,\ldots,1/2)\le 0.01}
\]

whenever the Poincare denominator defining \(c_G\) is positive.  Therefore the
stable lift `0.2682048` has substantial reserve on this whole slice.

This is an exact finite slice of the universal missing implication, not a proof of
the all-bias or all-arity statement.

## 1. Compact conditional end-to-end argument

For a symmetric nonnegative potential \(\Gamma\), define

\[
D_\Gamma(G;p)=
\sum_i\frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p).
\tag{1.1}
\]

The all-gate reformulation proves:

1. if \(D_\Gamma(G;p)\ge0\) for every Boolean gate, every arity and every
   interior product bias, with \(\Gamma(1/2)\le C\), then \(H(f)\le CI(f)\)
   for every uniform-cube Boolean \(f\);
2. fleet02/B17's exact composition cocycle reduces the fixed scalar-lift
   candidate to composition-prime gates;
3. the current stable candidate is `LIMIT-PRIME-GATE-LIFT-v1` above.

Thus the still-unproved implication is

\[
D_{\Gamma_*}(P;p)\ge0
\quad\text{for every finite composition-prime Boolean }P
\text{ and every interior bias }p.
\tag{1.2}
\]

The present run proves (1.2) for arity five at
\(p=(1/2,\ldots,1/2)\), and actually without assuming composition-primality.

## 2. Use the certified read-once potential, not the rough stable cap

The proved read-once certificate
`continuations/2026-09-21-readonce-certificate/REPORT.md`
certifies

\[
\Gamma_{.01}(u):=\Gamma_{\rm RO}(u)+0.01\,u(1-u),
\qquad
\Gamma_{.01}(1/2)=C_{\rm cert}=6.4573,
\tag{2.1}
\]

for all binary AND/OR/NOT read-once formulas.  Therefore every such formula \(F\)
with output measure \(q\) satisfies

\[
\Gamma_{.01}(q)\le C_{\rm cert} I(F)-H(F).
\tag{2.2}
\]

For a five-input gate at the uniform input vector,

\[
D_{\Gamma_{.01}}(G;1/2^5)
=C_{\rm cert}I(G)-H(G)-\Gamma_{.01}(p_{\rm out}).
\tag{2.3}
\]

Consequently, if for each possible output cardinality
\(m=32p_{\rm out}\) one can exhibit a read-once comparator \(F_m\) with the
same measure and prove

\[
C_{\rm cert}I(G)-H(G)
\ge C_{\rm cert}I(F_m)-H(F_m)
\tag{2.4}
\]

for **every** five-bit Boolean \(G\) of that cardinality, then (2.2)--(2.4)
give \(D_{\Gamma_{.01}}(G;1/2^5)\ge0\).

This is the first essential inference attacked below.

Because a scalar lift changes gate defect by

\[
c\,M_G,\qquad
M_G=\frac{I(G)}4-p_{\rm out}(1-p_{\rm out})\ge0,
\tag{2.5}
\]

the theorem for \(c=0.01\) automatically implies the fixed stable candidate
with \(c=0.2682048\).

## 3. New theorem: read-once extremizers of \(C_{\rm cert}I-H\) at every five-cube volume

### Theorem 3.1

Let \(G:\{0,1\}^5\to\{-1,1\}\), and let
\(m=|\{x:G(x)=-1\}|\).  For every \(m\in\{0,\dots,32\}\) there is a
binary AND/OR read-once gate \(F_m\), with dummy inputs allowed, having the same
output cardinality and satisfying

\[
\boxed{
C_{\rm cert}I(G)-H(G)
\ge
C_{\rm cert}I(F_m)-H(F_m)
},
\qquad C_{\rm cert}=6.4573.
\tag{3.1}
\]

For \(m>16\), take the output complement of the \(32-m\) comparator.
Constants \(m=0,32\) are immediate.

For \(1\le m\le16\), one choice of comparator is:

| \(m\) | comparator \(F_m\) | cube boundary \(B_m=16I(F_m)\) |
|---:|---|---:|
|1|`x1&(x2&(x3&(x4&x5)))`|5|
|2|`x1&(x2&(x3&x4))`|8|
|3|`x1&(x2&(x3&(x4|x5)))`|11|
|4|`x1&(x2&x3)`|12|
|5|`x1&(((x2&x3)|x4)&x5)`|15|
|6|`x1&(x2&(x3|x4))`|16|
|7|`x1&((x2&x3)|(x4&x5))`|19|
|8|`x1&x2`|16|
|9|`(x1|x2)&(x3&(x4|x5))`|21|
|10|`x1&(x2|(x3&x4))`|20|
|11|`x1&(x2|(x3&(x4|x5)))`|21|
|12|`x1&(x2|x3)`|20|
|13|`x1&(x2|(x3|(x4&x5)))`|21|
|14|`(x1&x2)|(x3&x4)`|24|
|15|`(x1|(x2&x3))&(x4|x5)`|25|
|16|`x1`|16|

The checker independently regenerates all canonical read-once gates through
five leaves and verifies that the selected comparator is indeed objective-minimal
within that read-once family at its volume.

### Corollary 3.2 — exact arity-five central gate inequality

Every five-input Boolean gate satisfies

\[
\boxed{
D_{\Gamma_{.01}}(G;1/2,\ldots,1/2)\ge0.
}
\tag{3.2}
\]

Equivalently, whenever \(M_G>0\),

\[
\boxed{
c_G(1/2,\ldots,1/2)\le0.01.
}
\tag{3.3}
\]

Since \(0.01<0.2682048\),

\[
\boxed{
D_{\Gamma_*}(G;1/2,\ldots,1/2)\ge0
}
\tag{3.4}
\]

for the stable `LIMIT-PRIME-GATE-LIFT-v1` candidate, for **all** five-input gates,
prime or decomposable, balanced or unbalanced, unate or non-unate.

## 4. Why the finite certificate covers all \(2^{32}\) truth tables

Let \(A=\{x:G(x)=-1\}\), \(|A|=m\), and let \(B=|\partial A|\) be its
undirected edge boundary in \(Q_5\).  Then

\[
I(G)=\frac B{16}.
\tag{4.1}
\]

Also the empty Fourier mass is \((1-2m/32)^2=1-V\), where

\[
V=4\frac m{32}\left(1-\frac m{32}\right).
\]

The remaining spectral mass \(V\) lies on at most \(31\) atoms, so

\[
\boxed{
H(G)\le h_2(V)+V\log_2 31.
}
\tag{4.2}
\]

This handles every sufficiently large boundary analytically.

For the remaining low-boundary tables, split \(Q_5\) into two \(Q_4\) layers
\(A_0,A_1\).  If \(b(A)\) denotes the \(Q_4\) boundary,

\[
B=b(A_0)+b(A_1)+|A_0\triangle A_1|.
\tag{4.3}
\]

The raw five-cube Walsh coefficients are exactly

\[
W_0(S)+W_1(S),\qquad W_0(S)-W_1(S),
\tag{4.4}
\]

where each \(W_b(S)\) is an integer four-cube Walsh sum.  Hence every spectral
mass is \(t^2/1024\), and its entropy contribution is

\[
\frac{t^2}{1024}\left(10-2\log_2|t|\right).
\tag{4.5}
\]

The checker enumerates all low-boundary layer pairs and uses rational interval
bounds for every logarithm.  It covers **3,425,314** low-boundary tables for
\(1\le m\le16\); all higher-boundary tables are discharged by (4.2), and
\(m>16\) follows by output complementation.

The smallest certified **strict** low-boundary objective gap is

\[
\boxed{0.004906502214}
\]

at \(m=7\) or \(m=9\).  Exact equality cases are never decided by overlapping
floating intervals: the checker recognizes them symbolically by identical
boundary and identical multisets of absolute integer Walsh coefficients.

The checker output is `PASS`.

## 5. Exact arithmetic and verification

No floating-point logarithm is used for a sign decision.  For integer \(n\ge1\),
the checker encloses

\[
\ln n
=
2\sum_{r=0}^{N-1}\frac{y^{2r+1}}{2r+1}+R_N,
\qquad
y=\frac{n-1}{n+1},
\]

with

\[
0\le R_N\le
\frac{2y^{2N+1}}{(2N+1)(1-y^2)},
\tag{5.1}
\]

using exact `Fraction` arithmetic with \(N=320\), and independently encloses
\(\ln2\).  Entropy atoms are rounded outward to an integer grid of
\(10^{-12}\).  The strict gaps are many orders larger than that outward
rounding.  Equality spectra are treated exactly as described above.

Checker SHA-256:

`9f8a92231544fb87e2a7bf80db2b5cdad8d969e35bda81a0a28f71091d2a0f5e`

Captured output SHA-256:

`df48be96df14c77e12d7334b78dc3746b25cc00376edc0855cccd19eab31b7ec`

## 6. What changed and what remains missing

**Old missing implication.** Prove or refute `LIMIT-PRIME-GATE-LIFT-v1` for
every composition-prime gate, every arity and every interior product bias.

**New proved inference.** The candidate is now proved for every arity-five gate
on the complete central input-bias slice \(p_1=\cdots=p_5=1/2\).  More strongly,
the already-certified smaller read-once lift \(c=0.01\) pays this entire slice,
so every positive-denominator central arity-five margin obeys \(c_G\le0.01\).
This strictly extends the prior balanced-unate and balanced-center exclusions:
output balance and unateness are both removed.

**Other peer slice retained.** fleet03/B17 independently closes the asymmetric
dyadic slice \((1/2,1/2,1/2,1/2,1/4)\) at output mass \(1/8\); this run did not
repeat it.

**Replacement obligation.** The unresolved adversarial frontier is now genuinely
off-center: a composition-prime five-input gate at a nonuniform bias vector
outside the already-certified dyadic spine, or a proof that all such biased
instances reduce to decomposable/read-once comparators.  A repetition of the
uniform center is no longer useful.

**Implication to full FEI.** Direct but partial.  One full arity-five bias slice
of the universal gate inequality is closed rigorously.  The all-bias/all-arity
quantifier remains open.

**Classification:** `ESSENTIAL_STEP_APPLIED`.

Scoped privacy review: this report and its checker contain only FEI mathematics,
source-bound repository paths/hashes and sanitized verification metadata.  No
credentials, scheduler IDs, machine paths, unrelated private material,
email/Drive action, public-posting action, paid/remote compute, workflows or
permission changes are included.
