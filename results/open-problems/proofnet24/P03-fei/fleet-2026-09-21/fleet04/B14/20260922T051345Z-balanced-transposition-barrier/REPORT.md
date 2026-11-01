# B14 — exact balanced-transposition barrier for the source n=18 FEI prime gate

**Date:** 22 September 2026  
**Run:** `B14-20260922T051345Z-gate-restriction-r12`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / SOURCE-PRIME BALANCED-TRANSPOSITION BARRIER`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Later-owner precedence and current target

supersedes the older posterior-crossing-only wording and directs all FEI workers to the
equivalent all-gate inequality. I therefore keep the exact restriction identities and
counterexamples as invariants, but use them only to guide the current all-gate target.

The live candidate inherited from the current FEI chain is
\[
\Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p),
\qquad
C_*=\Gamma_*(1/2)=6.5218512.
\]
On a balanced gate at uniform input bias its defect is
\[
D_{\Gamma_*}(f;1/2,\ldots,1/2)
=
C_*[I(f)-1]-H(f).
\]
Thus the corresponding "danger" functional is
\[
F_{C_*}(f):=H(f)-C_*[I(f)-1],
\]
and the candidate is safe on the balanced-uniform slice exactly when \(F_{C_*}(f)\le0\).

No claim is made that this fixed candidate proves FEI.

## 1. Exact inherited mathematics consumed

### 1.1 Fleet01/B18 curvature-refunded restriction inequality

I read the exact completed source

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T1856Z-curvature-refunded-crossing/REPORT.md`

(blob `ef9f471c019a7d81e9864fd457a0e4bae9da890d`). In the median-centered gauge it proves,
for every physical block \(A\),
\[
\mathcal J(g)-\mathbb E_z\mathcal J(g_{A=z})=I_A+C_A
\tag{1.1}
\]
and for an \(\mathcal F/\mathcal J\)-critical core,
\[
B_A\ge
\rho I_A+
\sum_{j\notin A}\bigl(\rho+\mathfrak j'(p_j)\bigr)c_j(A).
\tag{1.2}
\]
The source-to-next-arrow use is structural and exact: **a viable induction/restriction
argument may not discard the nonmodular child/crossing credit.** The gate-reformulation
slack loses too much. In the truth-table perturbation calculation below I therefore
retain the entire signed positional term \(Q(x)-Q(y)\) instead of replacing it by an
unsigned or coordinatewise surrogate.

The known addressing obstruction to prescribed-coordinate payment is unchanged. Nothing
below asserts \(B_i\le K\operatorname{Inf}_i\) for every prescribed \(i\), and (1.1) is
preserved exactly.

### 1.2 Fresh source-prime biased-curvature result

I also consumed the fresh compatible result

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B16/20260922T045841Z-source-bias-log-curvature/REPORT.md`

(blob `06586519345fffaf8d2aa078b0659ada506f79eb`). For the exact balanced monotone
composition-prime \(n=18\) source gate it proves a unique negative zero-mode birth
direction. Biasing all nine core coordinates coherently gives
\[
D_{\Gamma}(u)
=
D_{\Gamma}(0)
-\frac{67383}{8192}u^2\log_2(1/u^2)+O_\Gamma(u^2),
\tag{1.3}
\]
so the requested gate margin rises away from the balanced point. At
\(u=2\cdot10^{-4}\), its leading decrement exceeds the certified central stable-candidate
defect by
\[
2.3822767131526423\times10^{-6}.
\tag{1.4}
\]
The remaining finite-candidate obligation is to control the \(O(u^2)\) remainder with
the authentic candidate bytes; those bytes are not present in the authorized repository.

### 1.3 Fresh B18 finite-pattern result

The newest compatible B18 result on the scientific branch,
commit `1827914d44a7eb9e110f4f914056cfd0c78aac4a`,
proves that any fixed finite balanced point-defect pattern diluted by dummy coordinates
has incremental entropy/influence slope \(4\). This rules out one asymptotic sparse
amplification mechanism but does not decide finite, source-specific one-pair mutations.
The theorem below closes exactly that finite one-pair neighborhood of the current
source gate.

## 2. General exact balanced-transposition identity

Let \(f:\{0,1\}^n\to\{\pm1\}\) be balanced, \(N=2^n\), and write its unnormalised Walsh
coefficients
\[
W_S=\sum_x f(x)\chi_S(x).
\]
Define the entropy atom
\[
e(w)=
\begin{cases}
\displaystyle {2w^2\over N^2}\log_2{N\over |w|},&w\ne0,\\[4pt]
0,&w=0.
\end{cases}
\tag{2.1}
\]
Then
\[
H(f)=\sum_S e(W_S),
\qquad
I(f)={1\over N^2}\sum_S |S|W_S^2.
\tag{2.2}
\]

Choose \(x,y\) with \(f(x)=+1\) and \(f(y)=-1\), and transpose their truth-table values:
\(f(x)\mapsto-1\), \(f(y)\mapsto+1\). Put \(d=x\oplus y\ne0\). The new Walsh coefficient is
\[
W'_S=W_S-2\chi_S(x)+2\chi_S(y)
=
\begin{cases}
W_S,&\chi_S(d)=+1,\\
W_S-4\chi_S(x),&\chi_S(d)=-1.
\end{cases}
\tag{2.3}
\]

For each frequency define
\[
m_S={e(W_S+4)+e(W_S-4)-2e(W_S)\over2},
\qquad
n_S={e(W_S-4)-e(W_S+4)\over2}.
\tag{2.4}
\]
Let their Walsh transforms on the physical cube be
\[
M(z)=\sum_Sm_S\chi_S(z),
\qquad
N_1(z)=\sum_Sn_S\chi_S(z),
\tag{2.5}
\]
and also
\[
L(z)=\sum_S|S|\chi_S(z),
\qquad
K(z)=\sum_S|S|W_S\chi_S(z).
\tag{2.6}
\]

### Theorem 2.1 — exact one-pair mutation decomposition

For every balanced transposition \((x,y)\), with \(d=x\oplus y\),
\[
\boxed{
\Delta H
=
{1\over2}\,[M(0)-M(d)+N_1(x)-N_1(y)]
}
\tag{2.7}
\]
and
\[
\boxed{
\Delta I
=
{1\over 2N^2}
\,[16(L(0)-L(d))-8(K(x)-K(y))].
}
\tag{2.8}
\]
Consequently, for every real constant \(C\),
\[
\boxed{
\Delta F_C=E_C(d)+Q_C(x)-Q_C(y),
}
\tag{2.9}
\]
where
\[
E_C(d)
=
{1\over2}[M(0)-M(d)]
-{8C\over N^2}[L(0)-L(d)],
\tag{2.10}
\]
\[
Q_C(z)
=
{1\over2}N_1(z)+{4C\over N^2}K(z).
\tag{2.11}
\]

### Proof

Equation (2.3) shows that only frequencies with \(\chi_S(d)=-1\) move. On such a
frequency, the entropy increment equals
\[
m_S+n_S\chi_S(x).
\]
Summing with the indicator
\((1-\chi_S(d))/2\) gives (2.7), because
\(\chi_S(x)\chi_S(d)=\chi_S(y)\).

For influence,
\[
(W_S-4\chi_S(x))^2-W_S^2
=
16-8W_S\chi_S(x)
\]
on the same odd frequencies. Multiplying by \(|S|/N^2\) and again inserting
\((1-\chi_S(d))/2\) gives (2.8). Subtracting \(C\Delta I\) from \(\Delta H\)
gives (2.9)--(2.11). QED.

This formula is deliberately signed. The term \(Q_C(x)-Q_C(y)\) is the
truth-table-mutation analogue of the nonmodular refund that cannot be thrown away in
the B18 restriction inequality.

## 3. Application to the exact source-valid n=18 prime gate

Use the published source gate with truth-table SHA-256
```
f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839
```
and exact
\[
I(f)={261\over128}.
\tag{3.1}
\]
The gate is balanced, so there are
\[
2^{17}\cdot2^{17}=17,179,869,184
\]
possible \(+/-\) truth-table transpositions.

Take the stable cap exactly as
\[
C_*={4076157\over625000}=6.5218512.
\tag{3.2}
\]
A rigorous fixed-point interval computation, described in Section 4, proves
\[
\boxed{
F_{C_*}(f)
<
-5.703494021798\times10^{-6}.
}
\tag{3.3}
\]

More strongly, simultaneously for every \(d\ne0\),
\[
\boxed{
E_{C_*}(d)
\le
-0.000817140727713073,
}
\tag{3.4}
\]
while
\[
\boxed{
\max_zQ_{C_*}(z)-\min_zQ_{C_*}(z)
\le
0.000552850562266978.
}
\tag{3.5}
\]
Hence Theorem 2.1 gives, for **every** balanced truth-table transposition,
\[
\boxed{
\Delta F_{C_*}
\le
-0.000264290165446095.
}
\tag{3.6}
\]
Combining with (3.3),
\[
\boxed{
F_{C_*}(f_{\rm transposed})
\le
-0.000269993659467893.
}
\tag{3.7}
\]

### Corollary 3.1 — finite one-pair balanced-mutation barrier

No single balance-preserving two-point truth-table mutation of the exact source
\(n=18\) prime gate can falsify the stable cap at the balanced-uniform point.
Every such mutation moves the gate **strictly farther inside** the safe half-space,
by at least \(2.64290165446095\times10^{-4}\) in \(F_{C_*}\).

The least-favourable displacement term in the certificate occurs at
\(d=1536\), a Hamming-distance-two difference vector, but even after paying the
entire worst possible signed positional range \(Q_{\max}-Q_{\min}\), the net change
is still strictly negative.

## 4. Rigorous certificate

`check_balanced_transposition.py` reconstructs the source gate from the exact ten
published 512-bit slices and first verifies the source truth-table SHA-256 above.

It then:

1. computes the complete integer Walsh transform;
2. verifies \(I=261/128\);
3. encloses every entropy atom \(e(w)\), \(e(w+4)\), and \(e(w-4)\) using rational
   `atanh` series for logarithms (50 terms, with an explicit positive tail bound);
4. rounds those intervals outward to scale \(10^{18}\);
5. interval-Walsh-transforms the \(m_S,n_S\) arrays;
6. evaluates exact integer transforms for \(L,K\);
7. obtains global upper bounds for \(\max_{d\ne0}E(d)\) and
   \(\max Q-\min Q\).

Thus the program does **not** enumerate the 17.18 billion transpositions. The exact
identity (2.9) reduces all of them to two cube transforms and two extrema.

Captured output:
```
PASS
truth_sha256 = f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839
source_I = 261/128
source_cap_slack_upper = -5703494021798 / 10^18
max_E_nonzero_upper = -817140727713073 / 10^18
argmax_E_nonzero = 1536 hamming_weight = 2
Q_range_upper = 552850562266978 / 10^18
transposition_change_upper = -264290165446095 / 10^18
all_transposed_cap_slack_upper = -269993659467893 / 10^18
balanced_transposition_barrier = True
```

Checker SHA-256:
`0493e08411882271946ebbdd77e937f170a58f60aa1fb82dabb1f6bb1de9fe66`.

Captured stdout SHA-256:
`0a5ae3be86d1efaa158c4d136c5112392444efce59e3652460394984a613d054`.

The checker is a rigorous finite certificate for this source gate and this local
mutation class; it is not an end-to-end FEI verifier.

## 5. Exact source-to-next-arrow consequence

The fresh source state now gives a sharp local dichotomy around the same prime gate:

* **gate mutation direction:** every single balanced \(+/-\) truth-table transposition
  is safely repelled by (3.6);
* **product-bias direction:** the coherent all-core bias direction is attractive for
  the requested margin at singular order, by (1.3).

Therefore the next decisive job should **not** spend another run searching one-pair
balanced mutations of this source. The sharper target is the finite biased remainder
from the B16 calculation:
\[
R_*(2\cdot10^{-4})
<
2.3822767131526423\times10^{-6}
\tag{5.1}
\]
would rigorously falsify the present fixed candidate \(\Gamma_*\) on an explicit
composition-prime gate and bias vector.

The authentic `cert_vi_h96k40_f4.npz` candidate bytes are not present in the current
authorized repository (`filename` code search returns no object, and direct path reads
fail). I did not substitute an older candidate or manufacture the two required
\(\Gamma_*\)-values. A candidate-independent analytic bound on the two near-half
potential increments is the alternative route.

Even if (5.1) is eventually proved, that falsifies this **candidate potential**, not
the FEI conjecture itself.

## 6. Preserved exclusions and status

* The prescribed-coordinate Shannon-erasure bound remains false.
* The addressing obstruction remains active.
* The exact centered block drift remains
  \[
  \mathcal J-\mathbb E\mathcal J_{\rm child}=I_A+C_A.
  \]
* No negative-information or signed child term was discarded.
* No benchmark gold, mock proof, paid/remote compute, workflow dispatch, email/Drive,
  unrelated private data, or notification change was used.
* Full uniform-cube FEI remains **OPEN / NOT PROVED**.
* Execution is `WITHOUT_VERIFIED_BRAIN`: Python was available, but `math_brain` was
  not importable and `lean`, `lake`, and `elan` were not available.

## 7. Handoff

`prior_missing_implication`:
prove or refute \(D_{\Gamma_*}(P;p)\ge0\) for every composition-prime gate and every
interior product bias.

`new_proved_inference`:
the exact source \(n=18\) prime gate has a rigorous all-pairs balanced-transposition
barrier at the live cap \(C_*=6.5218512\); every one-pair balanced truth-table mutation
decreases \(F_{C_*}\) by at least \(2.64290165446095\times10^{-4}\).

`replacement_obligation`:
certify the explicit finite coherent-bias remainder (5.1), or prove an alternative
candidate-independent near-half potential-increment bound.

`full_FEI`:
open / not proved.
