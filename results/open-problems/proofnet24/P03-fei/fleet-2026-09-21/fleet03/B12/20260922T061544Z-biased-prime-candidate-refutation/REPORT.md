# fleet03/B12 — an exact off-centre prime-gate obstruction to LIMIT-PRIME-GATE-LIFT-v1

**Classification:** `ESSENTIAL_STEP_APPLIED / CURRENT_FIXED_CANDIDATE_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact candidate and prior missing implication

The common B-lead candidate is `LIMIT-PRIME-GATE-LIFT-v1`, with the rounded presentation
\[
C_*=6.5218512,\qquad \Gamma_*(p)=\Gamma_{\rm RO}(p)+0.2682048\,p(1-p).
\]
For source-exact work I use the compatible completed normalization from fleet01/B18:
\[
C^\dagger=6.521851214,\qquad C_0=6.4548,
\]
\[
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+a^\dagger p(1-p),
\]
where `Gamma_0` is the committed `cert_vi_h96k40` candidate (blob `1e2a1a5c293fa7b6ec9885b7a410910d6589be80`).

The prior missing implication was
\[
D_{\Gamma_*}(P;p)\ge0
\tag{1.1}
\]
for every finite composition-prime Boolean gate `P` and every interior product-bias vector `p`, where
\[
D_\Gamma(G;p)
=
\sum_i {\rm It}_i(G;p)\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}}
-\Gamma(p_{\rm out})-\widetilde H_G(p),
\qquad V_u=4u(1-u).
\tag{1.2}
\]

This run gives an explicit source-bound **composition-prime** counterexample to (1.1).

## 2. Named peer result consumed and applied

The completed other-account artifact consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B14/20260922T003849Z-prime-gate-falsifier/REPORT.md`, blob `43ad8483eb8a56cb7141a33821ab89e4119dbc49`.

Its ANF rank-one test proves that Numaro's exact balanced 18-input source gate, truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

is composition-prime: all 262124 proper candidate decomposition blocks are rejected. I apply that theorem to the off-centre bias below. Hence the witness directly hits the **reduced prime-gate universal implication**, rather than merely an unreduced all-gate formulation.

## 3. Exact off-centre witness

Let `f` be that exact 18-variable gate. Its uniform first-level influence profile is
\[
{\rm Inf}_1=\cdots={\rm Inf}_9=\frac{57}{256},
\qquad
{\rm Inf}_{10}=\cdots={\rm Inf}_{18}=\frac1{256},
\]
so
\[
I(f)=\frac{261}{128}.
\]
Choose one of the first nine coordinates and set
\[
\boxed{p_1=\frac38,\qquad p_2=\cdots=p_{18}=\frac12.}
\tag{3.1}
\]
The gate is balanced and its singleton Walsh coefficient on this coordinate is `57/256`, so
\[
\mathbb E_p f=(1-2p_1)\frac{57}{256}=\frac{57}{1024}
\]
and therefore
\[
\boxed{p_{\rm out}=\frac{967}{2048}=0.47216796875.}
\tag{3.2}
\]
Both `3/8` and `967/2048` are exact nodes of the committed high-p mesh, so evaluation of `Gamma_0` requires **no interpolation**.

Write `A_T=2^18 \hat f(T)` for the integer uniform Walsh numerators, and pair frequencies `T` and `T\cup\{1\}` with `1\notin T`. Under (3.1), the biased Fourier masses are exactly
\[
\boxed{
q_T=\frac{(4A_T+A_{T\cup\{1\}})^2}{2^{40}},
\qquad
q_{T\cup\{1\}}=\frac{15A_{T\cup\{1\}}^2}{2^{40}}.
}
\tag{3.3}
\]
The exact integer transform gives total mass one, 2792 nonzero spectral atoms, and only 46 distinct positive integer mass numerators. Thus
\[
\widetilde H_f(p)
=40-2^{-40}\sum_m n_m m\log_2 m.
\tag{3.4}
\]
Using rational atanh-series enclosures for every logarithm gives
\[
\boxed{
6.7442547370563132664
<\widetilde H_f(p)<
6.7442547370563132665.
}
\tag{3.5}
\]

The same exact masses give
\[
{\rm It}_1=\frac{855}{4096},
\qquad
\sum_{i=2}^{18}{\rm It}_i=\frac{465}{256},
\qquad
\boxed{I_t=\frac{8295}{4096}}.
\tag{3.6}
\]
Since `V_{3/8}=15/16`,
\[
\frac{{\rm It}_1}{V_{3/8}}=\frac{57}{256}.
\tag{3.7}
\]

## 4. Source-exact candidate evaluation

The two needed IEEE-754 values stored in the committed `cert_vi_h96k40.npz` are, as exact binary rationals,
\[
G(3/8)=\frac{8766995320315105}{562949953421312},
\]
\[
G(967/2048)=\frac{7680879056207109}{562949953421312},
\]
where `Gamma_0(s)=sG(log_2(1/s))` on the small side. Therefore
\[
\Gamma^\dagger(3/8)
=5.9028525499618973822015277619\ldots,
\]
\[
\Gamma^\dagger(967/2048)
=6.5090947440518241977681053179\ldots .
\]
Substitution into (1.2) reduces exactly to
\[
D_{\Gamma^\dagger}
=
C^\dagger\frac{465}{256}
+\frac{57}{256}
\left(\Gamma^\dagger(3/8)+h_2(15/16)\right)
-\widetilde H_f(p)
-\Gamma^\dagger(967/2048).
\tag{4.1}
\]
The rational log interval calculation has width below `2.3e-78` and yields
\[
\boxed{
D_{\Gamma^\dagger}(f;p)
=-0.0176114199558017537894958865691\ldots<0.
}
\tag{4.2}
\]
In particular the source-exact stable candidate is **REFUTED**.

This is not an artifact of the extra `1.4e-8` in the source-exact normalization. For the one-parameter family
\[
\Gamma_c=\Gamma_0+c\,p(1-p),
\]
the gate defect changes by `cW`, with
\[
\boxed{
W=\frac{I_t}{4}-p_{\rm out}(1-p_{\rm out})
=\frac{1078193}{4194304}>0.
}
\tag{4.3}
\]
The same exact interval computation gives the necessary quadratic coefficient
\[
\boxed{
c>0.3367154}
\tag{4.4}
\]
and numerically
\[
c_{\rm req}=0.3367154558335169298319482272843\ldots .
\tag{4.5}
\]
Hence both the B-lead rounded lift `0.2682048` and the source-exact lift `0.268204856` fail on the same prime witness. If one insists on repairing only by increasing this quadratic coefficient while keeping the base `Gamma_0`, its center would have to satisfy
\[
\Gamma_c(1/2)=6.4548+\frac c4
>6.53897885,
\tag{4.6}
\]
so a different shape repair may be substantially preferable.

## 5. Decisive checker

A local deterministic checker reconstructed the source gate and verified its SHA-256, performed the exact integer Walsh transform, verified (3.3) and total mass, obtained the exact influence identities (3.6), and enclosed every logarithm by the exact rational identity
\[
\ln y=2\sum_{k\ge0}\frac{z^{2k+1}}{2k+1},
\qquad z=\frac{y-1}{y+1},
\]
with a positive geometric tail bound. With 80 terms it certified

- `H` interval width `<2.3e-78`;
- `D_current < -0.017611`;
- required quadratic coefficient `>0.3367154`.

The checker returned `PASS`. Platform safety blocked upload of the checker source during this invocation; I did not retry, rename, encode, or route it through another account/tool. The proof formulas and certified numerical inequalities are preserved here, but the executable itself is therefore **not remotely delivered by this run**.

## 6. Exact failed claim and replacement obligation

**Exact candidate version:** `LIMIT-PRIME-GATE-LIFT-v1`, with source-exact representative `Gamma^dagger=cert_vi_h96k40+0.268204856 p(1-p)`.

**Prior missing implication:** `D_{Gamma_*}(P;p)>=0` for every finite composition-prime Boolean gate and every interior product bias.

**New result:** **REFUTED.** The exact composition-prime Numaro 18-input gate at the one-coordinate bias `(3/8,1/2,...,1/2)` has strictly negative defect, with certified margin below `-0.017611`.

**Replacement obligation:** the fixed h96 read-once potential plus the current single quadratic lift cannot be the universal all-gate potential. A replacement must reshape `Gamma` off centre (or increase the quadratic lift past `0.3367154`, which forces a center above `6.53897885` within that one-parameter family) and must be retested first on this exact prime gate and its one-coordinate bias line before broader gate enumeration.

**Consumed peer artifact:** fleet04/B14 `20260922T003849Z-prime-gate-falsifier/REPORT.md`, used to promote this explicit biased witness to a direct counterexample to the reduced prime-gate implication.

**Next recipient:** `fleet03/B18` (B lead). The common candidate should be marked refuted and replaced before workers spend more effort certifying its other gate families.

**Implication to full FEI:** this eliminates the current candidate, not FEI. A different finite-cap potential may still satisfy the all-gate inequality. Therefore
\[
\boxed{\text{Full uniform-cube FEI remains OPEN / NOT PROVED.}}
\]

No email, Drive, public post, workflow dispatch, paid model/API/Codex, credential access, scheduler mutation, or unrelated private-data operation was used.
