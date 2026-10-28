# B14 — the n=18 all-gate falsifier is itself composition-prime

**Run:** `B14-20260922T003849Z-r11`  
**Status:** **ESSENTIAL_STEP_APPLIED / current read-once-Gamma extremality refuted more strongly.**  
**Full FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Latest owner target and source binding


\[
\Gamma(p_{\rm out})+H_t(G;p)\le
\sum_i {\rm It}_i(G;p)\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

with the two live jobs: prove decomposable/AND extremality for the current read-once potential, or falsify it by finding a gate and bias vector asking for a larger correction margin. The exact equivalence of (G) with full FEI is in `proofnet24/P03-fei/continuations/2026-09-22-gate-reformulation/REPORT.md`, section 1, blob `1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

Two newer source-exact peer results supersede the older numerical picture:

1. `proofnet24/P03-fei/fleet-2026-09-21/account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`, blob `e49efe403698395b700278d067c245c12a7b15eb`, applies Numaro's source-validated balanced 18-variable seed and proves, for the read-once candidate with `C0=Gamma(1/2)=6.4548`,
   \[
   c_G(1/2^{18})\ge
   0.2681828436921863026325758917943138734666491688421\ldots,
   \]
   versus the current two-input AND margin about `0.0043974201`. Thus the candidate is already decisively refuted.
2. `proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T002604Z-gate-composition-prime/REPORT.md`, blob `674213d7e9d2f2952fcd22a94ad1be014a5b741f`, proves the exact gate-slack composition law and the cofactor criterion for functional decomposition. It concludes that some composition-prime violating descendant exists at arity at most 18, but it does not identify whether the published 18-variable gate itself is prime.

This run closes that last structural ambiguity.

## 1. Exact ANF decomposition criterion

Write a Boolean gate as a bit-valued function
\(f:\{0,1\}^{A\sqcup B}\to\{0,1\}\) and expand it in algebraic normal form over \(\mathbb F_2\):

\[
f(x_A,x_B)=\bigoplus_{U\subseteq A,\,V\subseteq B}
c_{U,V}x_Ux_V.
\tag{1}
\]

For each nonempty \(U\subseteq A\), let
\[
r_U=(c_{U,V})_{V\subseteq B}\in\mathbb F_2^{2^{|B|}}.
\]

### Lemma (ANF rank-one criterion)

There exist Boolean functions \(g:\{0,1\}^A\to\{0,1\}\) and
\(H:\{0,1\}^{\{t\}\sqcup B}\to\{0,1\}\) with

\[
f(x_A,x_B)=H(g(x_A),x_B)
\tag{2}
\]

if and only if the span of the rows \(\{r_U:U\ne\varnothing\}\) has dimension at most one over \(\mathbb F_2\). Equivalently, all nonzero rows are identical.

### Proof

If (2) holds, every Boolean function of the one bit \(t\) can be written uniquely as
\[
H(t,x_B)=h_0(x_B)\oplus t\,h_1(x_B).
\]
Write
\[
g(x_A)=g_0\oplus\bigoplus_{U\ne\varnothing}g_Ux_U.
\]
Then for every nonempty \(U\), the entire ANF coefficient row is
\[
r_U=g_U\,\widehat h_1,
\]
so each row is either zero or the same vector \(\widehat h_1\). Hence the row span has dimension at most one.

Conversely, suppose all nonzero rows are identical to a vector \(r\). Let
\(h_0(x_B)\) be the \(U=\varnothing\) ANF row, let \(h_1(x_B)\) be the Boolean polynomial with ANF row \(r\), and put
\[
g(x_A)=\bigoplus_{U\ne\varnothing:\ r_U=r}x_U.
\]
Then (1) is exactly
\[
f(x_A,x_B)=h_0(x_B)\oplus g(x_A)h_1(x_B),
\]
which is (2) with \(H(t,x_B)=h_0(x_B)\oplus t h_1(x_B)\). If every nonempty row is zero, the function is independent of the whole block \(A\), the degenerate one-row case. QED.

This criterion is equivalent to the cofactor criterion in account01/B13, but is computationally much cheaper on a sparse ANF because it never forms the exponentially long cofactor rows.

## 2. Apply it to the source-bound n=18 seed

The exact truth table is reconstructed from the ten 512-bit slices already preserved in

`proofnet24/P03-fei/fleet-2026-09-21/account01/B15/20260921T130641Z-carry-congruence-n18-profile/n18_packet_carry_profile.py`, blob `ef314171fc38edf804d394319b1d34175165a52a`,

and accepted only after matching the source-bound complete truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

The exact Möbius transform over \(\mathbb F_2\) has only **193 nonzero ANF monomials**. Their union contains all 18 coordinates, so there is no dummy input.

I then tested every proper candidate block
\[
A\subset[18],\qquad 2\le |A|\le17.
\]
There are exactly
\[
2^{18}-1-18-1=262124
\]
such blocks. For each one, the nonempty-\(A\) ANF coefficient rows contain at least two distinct nonzero row signatures. By the lemma, no candidate block admits a representation (2).

Therefore

\[
\boxed{\text{Numaro's balanced 18-variable FEI record seed is composition-prime.}}
\tag{3}
\]

This is stronger than the previous descent statement: the published/source-bound counterexample to the read-once \(\Gamma\) does **not** obtain its large margin from any hidden disjoint functional composition. The obstruction already lives in a genuinely prime gate.

The exact per-size block counts checked were

`153, 816, 3060, 8568, 18564, 31824, 43758, 48620, 43758, 31824, 18564, 8568, 3060, 816, 153, 18`

for block sizes 2 through 17, with zero decomposable blocks at every size.

A deterministic rejection-witness stream, recording for each candidate block two unequal ANF rows and one column where they differ, had SHA-256

`b95b30e984d15880f552c5dc27b156e2856584220cdc38191780a1f4f16a71c8`.

The local standard-library checker exited 0 in 15.94 seconds. Its source SHA-256 was
`4d0da21ee5659c8bea96b0408a2c760f66b5a6847fa2aa0eefa76a3f804e0da1`; captured JSON-output SHA-256 was
`5d1e4267871cc1a5afde3eb82e08fc1e34c1ab16c15aec20c4af24fed4001b9b`.
A platform safety denial blocked upload of the checker source in this invocation; per control I did not retry it through encoding, renaming, another account, or another tool. The analytic criterion and the exact checked totals are preserved here, but the executable itself is therefore **not remotely delivered by this run**.

## 3. Exact consequence for the owner convergence target

For the current read-once value-iteration potential, account03/B15 already gives
\[
I(G)=\frac{261}{128},
\qquad
6.776605309005978082519790221891882314787235038
\le H(G)\le
6.776605309005978082519790221891882314787235039,
\]
and hence at uniform input bias
\[
\boxed{c_G\ge0.2681828436921863026325758917943138734666491688421\ldots .}
\tag{4}
\]
Combining (3) and (4):

\[
\boxed{
\text{A composition-prime 18-input gate asks for more than 60 times the current AND margin.}
}
\tag{5}
\]

Thus the proposed statement that the extremal gate for this particular read-once \(\Gamma\) is decomposable/AND is not merely false because some large composition contains a bad component; it is false on a source-bound **prime gate itself**.

This does **not** refute the gate reformulation, existence of some other finite-cap potential \(\Gamma\), or FEI. It only eliminates the current read-once fixed-point potential as the universal all-gate potential.

## 4. Source-to-next-arrow use


- B15 supplies a source-valid all-gate violation at cap 6.4548.
- B13 proves any future all-gate candidate need only be checked on composition-prime gates, because gate slack composes exactly.
- This run shows the record n=18 obstruction is already composition-prime, so structural decomposition cannot explain it away.

Therefore a replacement universal potential must satisfy (G) on this prime gate and must have
\[
\Gamma(1/2)\ge C_{\rm FEI}>6.521845710923046575
\]
or achieve an equivalent compensation through its shape while respecting the same cap constraint. The next authorized work on this single owner-selected target is to derive a necessary envelope/fixed-point operation for **prime gates** and test it first on this n=18 seed and its bias perturbations, rather than resume the superseded posterior-crossing route.

**Classification:** `ESSENTIAL_STEP_APPLIED`; the current decomposable/AND-extremality candidate is structurally refuted. **Full FEI remains OPEN / NOT PROVED.**
