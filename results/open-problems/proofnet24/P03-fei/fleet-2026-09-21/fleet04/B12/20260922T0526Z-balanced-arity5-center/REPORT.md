# fleet04/B12 — the entire balanced arity-five center satisfies H <= 6(I-1)

**Run:** `B12-20260922T051428Z-r44`  
**Classification:** `ESSENTIAL_STEP_APPLIED / BALANCED_ARITY5_CENTER_CLOSED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Full uniform-cube Fourier entropy-influence remains **OPEN / NOT PROVED**.

## 1. Exact live target and peer result consumed

The live owner control asks every FEI worker to converge on the source-exact all-gate formulation

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for every Boolean gate and every interior product bias. At uniform input biases and a balanced output this reduces exactly to

\[
H(G)\le C\,[I(G)-1],\qquad C=\Gamma(1/2).
\tag{1.1}
\]

The previous B12 report proved only that the essential **unate** balanced five-input center satisfies
\(H/(I-1)\le 5.9470674987\ldots\). The present run changes mechanism and closes the entire balanced five-input center, including every non-unate gate.

The named newest compatible other-account result consumed is

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B13/20260922T045511Z-joint-credit-critical-core/REPORT.md`.

For an unbiased physical pivot with actual Boolean children \(f_0,f_1\) and disagreement probability \(\delta\), it proves the exact joint-information lower bound

\[
\mathcal C_j=H(B\mid S)+I(S;J)
\ge
h_2\!\left(\frac{1-2\sqrt{\delta(1-\delta)}}2\right).
\tag{1.2}
\]

Its concrete local-gluing consequence used here is that when both children are balanced and \(\Gamma(1/2)=C\ge13/2\), every pivot with \(\delta\ge1/4\) has strictly positive local cocycle remainder. Combined with the theorem below, any minimum-essential-arity **balanced-center** counterexample for such a candidate must have arity at least six, and every dangerous balanced-child central pivot must lie in the remaining \(\delta<1/4\) sector (or else leave the balanced-child hypothesis). Thus the five-input center and the large-disagreement balanced-child local sector are simultaneously removed from the current falsifier frontier.

The old read-once/AND-extremality claim is already source-validly falsified elsewhere in the current archive, so this run does not repeat that dead route. It addresses the owner's arity-five falsification frontier directly.

## 2. New theorem

### Theorem 2.1 — complete balanced arity-five center

For every Boolean function
\[
f:\{0,1\}^5\to\{-1,+1\}
\]
that is balanced under the uniform law,

\[
\boxed{H(f)\le 6\,[I(f)-1].}
\tag{2.1}
\]

The constant 6 is attained in the finite certificate. Consequently, for every all-gate potential with
\(\Gamma(1/2)=C\ge6\), inequality (G) holds at the uniform balanced center for every gate of essential arity at most five. In particular, there is **no balanced-center arity-five falsifier** for the current \(C\approx6.5218512\) candidate. Any five-input falsifier must use nonuniform input biases and/or unbalanced output measure.

This is a finite theorem at the uniform balanced center, not full FEI and not an off-center theorem.

## 3. Proof: split by distance to the signed dictators

Let
\[
d_*:=\min_{1\le i\le5,\ \sigma\in\{\pm1\}}
\bigl|\{x:f(x)\ne\sigma\chi_i(x)\}\bigr|.
\]

Because both \(f\) and every signed dictator are balanced, every such Hamming distance is even; after choosing the sign, \(d_*\le16\). Hence
\[
d_*\in\{0,2,4,6,8,10,12,14,16\}.
\]

We treat \(d_*\le10\) by an exact defect-sphere certificate and \(d_*\ge12\) by a larger integer spectral relaxation.

### 3.1 Near a dictator: 22,720,080 exact balanced defect realizations

If \(d_*=0\), then \(f\) is a dictator, so \(H=0\) and \(I=1\).

Suppose \(d_*=d\in\{2,4,6,8,10\}\). Cube symmetries and output sign map a closest signed dictator to a fixed \(\chi_1\), preserving squared Fourier masses, \(H\), \(I\), and balance. Relative to this fixed dictator, balance forces exactly \(d/2\) flipped points in its positive half and exactly \(d/2\) flipped points in its negative half. Thus it suffices to enumerate

\[
\binom{16}{d/2}^2
\]

defect sets for each \(d\). The exact counts are

\[
256,
\quad14{,}400,
\quad313{,}600,
\quad3{,}312{,}400,
\quad19{,}079{,}424,
\]

for \(d=2,4,6,8,10\), respectively, totaling

\[
\boxed{22{,}720{,}080}
\]

balanced defect realizations.

For each realization the checker computes the Walsh transform exactly over integers. A balanced five-bit Fourier coefficient is a multiple of \(1/8\), so write
\[
\widehat f(S)=m_S/8,
\qquad p_S=\widehat f(S)^2=m_S^2/64.
\]
It then bounds every entropy term from above using exact rational lower bounds on \(\log_2 m\), obtained from the positive atanh expansion with an explicit geometric tail. The final comparison
\[
H(f)\le6[I(f)-1]
\]
is performed as an integer inequality after multiplying by a common scale \(10^{12}\); no floating-point logarithm is used to certify the sign.

The exhaustive certificate returns:

| distance \(d\) | realizations | minimum certified integer slack | diagnostic maximum ratio ceiling |
|---:|---:|---:|---:|
| 2 | 256 | 35120782361600 | 4.536634068267 |
| 4 | 14,400 | 18117300051904 | 5.433834373378 |
| 6 | 313,600 | 20096404744320 | 5.497589881392 |
| 8 | 3,312,400 | 0 | 6.000000000000 |
| 10 | 19,079,424 | 2117300051712 | 5.947067498707 |

The ratio column is only a readable diagnostic from the rigorous entropy ceilings; the theorem is certified by the exact integer slack comparison. Distance eight attains equality.

### 3.2 Far from every dictator: an integer spectral relaxation gives 11/2

Assume now \(d_*\ge12\). For each singleton coordinate,
\[
\min_\sigma d(f,\sigma\chi_i)
=16\bigl(1-|\widehat f(\{i\})|\bigr),
\]
so
\[
|\widehat f(\{i\})|\le\frac14.
\tag{3.1}
\]

For every nonempty character \(\chi_S\), both \(f\) and \(\chi_S\) are balanced. Their Hamming distance is therefore even, hence their dot product is divisible by four. Thus every nonempty Fourier coefficient has the exact quantization
\[
\widehat f(S)=m_S/8,
\qquad m_S\in\mathbb Z.
\tag{3.2}
\]
Balance gives \(m_\varnothing=0\), and Parseval gives
\[
\sum_{S\ne\varnothing}m_S^2=64.
\tag{3.3}
\]
From (3.1), the five singleton squares satisfy
\[
m_{\{i\}}^2\in\{0,1,4\}.
\tag{3.4}
\]
For all higher-degree atoms we deliberately forget Boolean convolution constraints and allow any square
\[
m_S^2\in\{0,1,4,9,16,25,36,49,64\}.
\]
This enlarges the admissible class, so any upper bound for the relaxation is valid for the actual Boolean spectra.

Using (3.3),
\[
I(f)-1
=\frac1{64}\sum_{S\ne\varnothing}(|S|-1)m_S^2,
\tag{3.5}
\]
while the entropy contribution of one atom with \(u=m_S^2>0\) is
\[
\frac{u}{64}\log_2\frac{64}{u}.
\tag{3.6}
\]

A dynamic program over the five degree-one atoms, ten degree-two atoms, ten degree-three atoms, five degree-four atoms and one degree-five atom retains, for each pair

\[
\left(\sum m_S^2,\ \sum(|S|-1)m_S^2\right),
\]

the largest rigorous entropy ceiling. It has 6,983 live terminal states and 199 states with Parseval weight exactly 64. Every such state with positive influence excess satisfies the exact integer comparison corresponding to

\[
\boxed{H\le\frac{11}{2}(I-1).}
\tag{3.7}
\]

The diagnostic maximum ratio ceiling is exactly 5.5. Since this calculation is over a strict relaxation of Booleanity, (3.7) proves the entire \(d_*\ge12\) branch.

Together with the defect-sphere branch and the dictator endpoint, this proves Theorem 2.1. \(\square\)

## 4. Implication for the all-gate programme

At uniform input biases with balanced output, (G) is exactly (1.1). Therefore Theorem 2.1 removes **every** balanced five-input gate, not merely NPN-unate representatives, as a possible central obstruction whenever \(C\ge6\). This strictly strengthens the preceding B12 result, which removed only the unate sector.

The remaining arity-five falsifier search is now genuinely off-center: one must find a gate together with a nonuniform bias vector (or unbalanced output measure) for which the full potential margin is negative / requires a larger quadratic lift. A center-only NPN search cannot produce the requested arity-five falsifier.

Combining this with the fleet02/B13 joint-credit theorem gives a second structural narrowing for any minimum-arity balanced central counterexample at cap at least \(13/2\): it has arity at least six, and a physical pivot with two balanced children cannot be dangerous when its child disagreement is at least \(1/4\). The remaining local-gluing obstruction is therefore in the small-disagreement and/or unbalanced-child sector.

## 5. Verification artifact

Checker:

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0526Z-balanced-arity5-center/check_balanced_arity5_center.py`

Recorded output:

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B12/20260922T0526Z-balanced-arity5-center/check_balanced_arity5_center.out`

Executed source SHA-256:

`a017a96ed9d8e97a19697bad63b89d9db6851a9f38cc7bd86297f6a42e239ac5`

Output SHA-256:

`fbf619dd9e46977ec7171d8ed30ca3f96dc48dd1907d6d4eeeec57cdfa08c93a`

`py_compile` passed and the checker returned `PASS` with all 22,720,080 near-dictator realizations plus the complete far-spectrum relaxation certified.

The finite certificate is self-checked here and should still receive an independent worker replay before being treated as independently verified.

## 6. Preserved exclusions and status

Nothing here uses an ambient-dimension row cost, an ordinary second-derivative-depth payment, or the false implication \(\sum_k d_k=O(J)\). The fleet04/B18 mixed-curvature integrability identity remains intact and untouched. This run does not revive any refuted erasure, raw-depth, or blind-arity-induction shortcut.

Full FEI remains **OPEN / NOT PROVED**. The next decisive arity-five target is the off-center product-bias sector for the current source-exact \(\Gamma\), not another balanced-center classification.

No benchmark gold, email/Drive, paid or remote compute, workflow dispatch, unrelated private data, scheduler mutation, permission change, or notification enabling was used.
