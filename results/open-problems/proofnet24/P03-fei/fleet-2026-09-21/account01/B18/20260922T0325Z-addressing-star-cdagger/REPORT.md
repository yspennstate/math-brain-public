# B18 — the stable C-dagger candidate closes the entire common-data addressing family

**Classification:** `ESSENTIAL_STEP_APPLIED / SOURCE-CANDIDATE_ADDRESSING_CLOSED`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository controls and mathematical source files were retrieved directly; no authenticated cognitive-brain receiver/context entered the derivation.

## 0. Exact live candidate and conditional end-to-end chain

The all-gate formulation asks for one symmetric nonnegative potential `Gamma` such that, for every Boolean gate `G` of every finite arity and every interior product bias vector `p`,

\[
D_\Gamma(G;p):=
\sum_i \frac{\operatorname{It}_i(G;p)}{V_{p_i}}
\bigl(\Gamma(p_i)+h_2(V_{p_i})\bigr)
-\Gamma(p_{\rm out})-\widetilde H_G(p)\ge0,
\qquad V_u=4u(1-u).
\tag{0.1}
\]

The gate-reformulation continuation proves that (0.1), together with `Gamma(1/2)<=C`, implies `H(f)<=C I(f)` for every uniform-cube Boolean function. The composition-cocycle continuation reduces a fixed candidate to composition-prime gates.

The latest complete fixed center consumed here is account04/B18,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B18/20260922T031308Z-global-shared-core-invariant/REPORT.md`, report blob `630d799d165e6d18c67c59cec7421758230e9ee4`.

It fixes

\[
\boxed{C^\dagger=6.521851214}
\tag{0.2}
\]

and closes the known shared-core obstruction class at that center. To make the candidate itself source-exact, let `Gamma_0` be the committed read-once h96 value-iteration candidate `cert_vi_h96k40`, normalized by

\[
C_0=\Gamma_0(1/2)=6.4548,
\]

and put

\[
\boxed{
a^\dagger=4(C^\dagger-C_0)=0.268204856,
\qquad
\Gamma^\dagger(z)=\Gamma_0(z)+a^\dagger z(1-z).
}
\tag{0.3}
\]

Then `Gamma^dagger(1/2)=C^dagger`. The smallest honest conditional chain is:

1. prove `D_{Gamma^dagger}(P;p)>=0` for every composition-prime gate `P` and every interior product bias;
2. use the exact nonnegative composition cocycle to obtain the same statement for every Boolean gate;
3. apply the all-gate equivalence to obtain full FEI with constant `C^dagger`.

Step 1 remains open in general. This run directly proves it for the infinite common-data MUX/addressing class.

## 1. Exact other-worker theorem consumed and applied

The named peer result used substantively is account01/B17,

`proofnet24/P03-fei/fleet-2026-09-21/account01/B17/20260922T003221Z-gate-addressing-collapse/MUX_STAR_REDUCTION.md`, blob `2ccf5f8435982101a3d8ebfd2f05b49c2b144b4d`.

For **any** symmetric potential `Psi`, it proves the exact identity for the one-address-bit multiplexer with address bias `p` and both data bits at the same bias `q`:

\[
\boxed{
D^{\Psi}_{\rm MUX}(p,q)
=V_q\left[
D^{\Psi}_{\rm AND}(p,1/2)
+\Psi(p/2)-p\Psi(1/2)
\right].
}
\tag{1.1}
\]

For a common-data `k`-address construction the corresponding exact sum is

\[
\boxed{
D^{\Psi}_{\rm Addr_k}
=V_q\sum_{i=1}^k
\left[
D^{\Psi}_{\rm AND}(p_i,1/2)
+\Psi(p_i/2)-p_i\Psi(1/2)
\right].
}
\tag{1.2}
\]

Thus the actual missing mathematics on this whole obstruction family is the one-dimensional star inequality

\[
\Psi(p/2)\ge p\Psi(1/2),\qquad 0\le p\le1/2,
\tag{1.3}
\]

plus the already-certified AND inequality. The B17 source left (1.3) uncertified for the then-current finer candidate. The next section proves (1.3) for the present `Gamma^dagger`.

## 2. Source facts for the h96 candidate

On the small side `0<s<=1/2`, write

\[
s=2^{-x},\qquad
\Gamma_0(s)=sG(x),\qquad x=\log_2(1/s).
\tag{2.1}
\]

The source generator `continuations/2026-09-21-readonce-certificate/code/fei_cert_vi.py` defines `G` by piecewise-linear interpolation through the stored h96 nodes. The committed output

`continuations/2026-09-21-readonce-certificate/data/cert_vi_h96k40.out`, blob `2a93045da2554b31668312dfd1c4a026ba10851c`,

records

\[
G(x)-2(C_0-4)x\ge 2.22922\ldots
\]

at its global minimum, the dyadic value at `x=2` has wobble `8.000000`, and the smallest consecutive node increment is `-5.458e-02`. We deliberately weaken these by large buffers and use only

\[
\boxed{G(x)-4.9096x>2.22}
\tag{2.2}
\]

throughout the interpolated grid/tail,

\[
\boxed{G(2)>17.8,}
\tag{2.3}
\]

and

\[
\boxed{G_{j+1}-G_j>-0.056.}
\tag{2.4}
\]

The first and third inequalities extend from nodes to each linear segment in the only way used below: (2.2) is linear-minus-linear on every segment, hence its segment minimum is at an endpoint; (2.4) gives the endpoint loss over a counted number of grid steps. The buffers are orders of magnitude larger than the displayed floating-point rounding scale. This is a theorem about the **committed source-defined candidate array and its recorded diagnostics**; it is not presented as a new independent interval verification of the value-iteration computation.

On the relevant interval near `s=1/4`, the h96 grid is uniform in `s` with mesh `1/2048`.

## 3. New theorem: star positivity for Gamma-dagger

### Theorem 3.1

For every `0<=p<=1/2`,

\[
\boxed{
\Gamma^\dagger(p/2)\ge p\,C^\dagger.
}
\tag{3.1}
\]

For `p>0` the conservative bounds below are strict.

### Proof

The endpoint `p=0` follows by continuity. Take `0<p<=1/2`, set

\[
s=p/2,
\qquad
x=\log_2(1/s)=\log_2(2/p)\ge2.
\]

From (0.3) and (2.1),

\[
\begin{aligned}
\Gamma^\dagger(p/2)-pC^\dagger
&=sG(x)+a^\dagger s(1-s)-2sC^\dagger\\
&=s\left[G(x)-2C_0+a^\dagger(1/2-s)\right].
\end{aligned}
\tag{3.2}
\]

The cancellation in the second line is exact because `2C^dagger=2C_0+a^dagger/2`.

Define

\[
x_0:=
\frac{2C_0-a^\dagger/4-2.22}{4.9096}
=2.16362815422845\ldots,
\tag{3.3}
\]

so

\[
s_0=2^{-x_0}=0.22319426240335\ldots .
\tag{3.4}
\]

**Farther from the center: `x>=x_0`.** Since `s<=1/4`,

\[
a^\dagger(1/2-s)\ge a^\dagger/4.
\]

Using (2.2),

\[
G(x)-2C_0+a^\dagger(1/2-s)
>
4.9096x+2.22-2C_0+a^\dagger/4
\ge0
\tag{3.5}
\]

by the definition of `x_0`.

**Near the center: `2<=x<=x_0`.** Here `s` ranges from `1/4` down only to `s_0`. The number of h96 mesh increments crossed is at most

\[
\left\lceil2048(1/4-s_0)\right\rceil=55.
\tag{3.6}
\]

By (2.3)-(2.4), including linear interpolation inside the final cell,

\[
G(x)>17.8-55(0.056)=14.72.
\tag{3.7}
\]

Therefore

\[
\begin{aligned}
G(x)-2C_0+a^\dagger(1/2-s)
&\ge 14.72-12.9096+a^\dagger/4\\
&=\boxed{1.877451214}>0.
\end{aligned}
\tag{3.8}
\]

Equations (3.5) and (3.8) cover every `x>=2`, proving (3.1). QED.

The point of the two-regime proof is that it does **not** assume `G` is monotone. In fact the source output explicitly reports that `G` is not increasing everywhere. The near-center argument pays for every possible local downward node step using the measured worst-step bound.

## 4. Apply the star theorem to MUX and addressing

The read-once certificate proves the AND gate inequality after adding the quadratic margin `0.01 p(1-p)` to the base candidate. In the normalized AND slack, increasing the quadratic coefficient by `delta c>=0` increases the slack by the nonnegative quantity `delta c(1-p)(1-q)`. Since

\[
a^\dagger=0.268204856>0.01,
\]

we have

\[
D^{\Gamma^\dagger}_{\rm AND}(p,q)\ge0
\quad\text{for all interior }p,q.
\tag{4.1}
\]

Now substitute `Psi=Gamma^dagger` into the exact B17 identities (1.1)-(1.2). By (3.1) and (4.1), every term in brackets is nonnegative. Hence

\[
\boxed{
D^{\Gamma^\dagger}_{\rm MUX}(p,q)\ge0
\quad (0<p,q<1),
}
\tag{4.2}
\]

for the equal-data-bias one-bit MUX, and, for every finite `k`, arbitrary address biases `p_1,...,p_k` and common data bias `q`,

\[
\boxed{
D^{\Gamma^\dagger}_{\rm Addr_k}(p_1,\ldots,p_k;q)\ge0.
}
\tag{4.3}
\]

Boundary biases follow by continuity. Thus the stable universal candidate has now been proved on the full common-data addressing family in every dimension. This is exactly the source-valid addressing obstruction requested by the current execution order; it is not a finite-arity extrapolation.

## 5. Adversarial construction attempt around the explicit prime gate

Before adding the theorem above, I applied the current sparse-defect obstruction rather than ignoring it. The exact account01/B15 source reconstructs the balanced composition-prime ten-input gate with truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`

and proves it is a strict local maximum of `H/(I-1)` under all 262144 balanced two-point swaps. I reconstructed that same gate from the source constants; the hashes and exact balance matched, with

\[
H=6.509836127588151\ldots,
\quad
I=2.0078125,
\quad
H/(I-1)=6.459372281637855\ldots .
\]

As a genuinely different nonlocal stress test, five balance-preserving simulated-annealing runs of 30000 swaps each never exceeded the source gate. Independent random balanced `k`-swap perturbations, 20000 samples for each tested `k`, gave best observed ratios approximately

\[
6.39461\ (k=2),\quad
6.32084\ (k=3),\quad
6.24301\ (k=4),\quad
5.96137\ (k=8),\quad
5.47493\ (k=16).
\]

These computations are **exploratory only**. They neither prove local/global extremality beyond the exact B15 one-swap theorem nor support a universal FEI conclusion. Their role is only to record that the required sparse-defect/nonlocal falsification attempt was actually executed and did not produce a counterexample before the analytic addressing theorem was derived.

## 6. Exact old/new missing implication

**Old first essential implication:** prove the fixed `Gamma^dagger` gate inequality for every composition-prime Boolean gate at every interior product bias, or find a genuine prime/bias counterexample.

**New proved implication:** the same fixed candidate satisfies the gate inequality for every equal-data-bias one-bit MUX and, by the exact star decomposition, every common-data addressing gate in arbitrary dimension and arbitrary address biases. Together with the already completed shared-core closure and explicit G10 corridor, this removes another infinite obstruction family without altering the candidate.

**New first missing implication:** control genuinely prime gates not reducible to the closed shared-core/composition/addressing mechanisms. The nearest concrete extension is the unequal-data MUX (`q_0 != q_1`), where the star identity acquires real data-asymmetry terms; beyond that remain general biased composition-prime gates. Nothing here proves a classification saying all prime gates have one of the closed forms.

Therefore the target-level status is unchanged:

\[
\boxed{\text{Full Friedgut--Kalai FEI remains OPEN / NOT PROVED.}}
\]

## 7. Scope and provenance

The mathematical inputs are source-bound repository artifacts, not remembered paraphrases. No email, Drive, public posting, permission changes, paid/remote compute, workflows, credentials, machine paths, scheduler identifiers, benchmark material, or unrelated private data are used or stored. The conservative arithmetic in Section 3 is reproducible from the displayed source-output premises and is intentionally much looser than their recorded values. No publication-priority claim is made.
