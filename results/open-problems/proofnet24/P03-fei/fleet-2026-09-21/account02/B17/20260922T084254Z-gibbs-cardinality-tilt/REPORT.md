# account02/B17 — exact B-Gibbs refutation and cardinality-tilt replacement

**Run:** `20260922T084254Z-b17-gibbs-cardinality-tilt`  
**Classification:** `CANDIDATE_REFUTED / REPLACEMENT_EXECUTED / FULL_FEI_OPEN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository context was read, but no native brain receiver-context was used.

MODEL SELF-REPORT: GPT-5.6 Sol  
REQUESTED REASONING: maximum actually supported  
CONFIGURED / KNOWN REASONING LEVEL: UNKNOWN / NOT_EXPOSED  
PROVIDER REASONING USAGE: NOT_EXPOSED


## 0. Last-three comparison and exact change

The last three substantive account02/B17 reports are:

1. `20260922T044637Z-radius2-dust-compensation`: closed the symmetric-difference-four neighborhood of the published shared-core support, then proved slope four for a signed two-point Fourier-dust family.
2. `20260922T061440Z-mesoscopic-defect-codimension`: refuted the stronger idea that vanishing physical defect density alone forces slope four and replaced it by an exponential-codimension safety theorem.
3. `20260922T071234Z-and-slack-rigidity`: consumed the actual 18-input biased prime witness, refuted the fixed candidate `Gamma^dagger`, proved that a bounded center-preserving correction cannot be free on every AND constraint, and proposed same-center slack-budgeted transport.

**FULL-PROBLEM CHANGE:** none. No finite universal FEI constant is proved here.

**MECHANISM CHANGE:** yes. The previous mechanism tried to preserve the center and move existing signed AND slack through a correction `psi(1/2)=0`. This run attacks the Campaign-B lead's newest *exact normalized Gibbs residual* and then abandons center preservation. The replacement is an exact **cardinality-price tilt**: increase the quadratic coefficient by a finite amount, which shifts every Gibbs price uniformly and pays only the spectral cardinality excess. I instantiate a new finite-center candidate at coefficient `c_1=0.34` rather than merely announcing that a larger quadratic coefficient could be tried.

## 1. Campaign-B lead candidate and exact incompatibility

The newest complete Campaign-B lead report is account03/B18

`20260922T075546Z-gibbs-price-bellman/REPORT.md`.

It defines, for a nonconstant Boolean gate `G` at interior product bias `p`, output variance `v=V_q`, nonempty normalized biased squared-spectrum law `w^+`, coordinate prices

\[
a_i=\frac{\Gamma^\dagger(p_i)+h_2(V_{p_i})}{V_{p_i}},
\qquad
x_i=2^{-a_i},
\]

and output price `a_q` and weight `x_q` analogously. With

\[
A_0=\prod_i(1+x_i)-1,
\qquad
\nu_x^+(S)=\frac{\prod_{i\in S}x_i}{A_0},
\]

its exact normalized residual is

\[
R_B(G;p)=D_{\rm KL,2}(w^+\|\nu_x^+)-\log_2(A_0/x_q),
\tag{1.1}
\]

and the lead proves the identity

\[
D_{\Gamma^\dagger}(G;p)=v R_B(G;p).
\tag{1.2}
\]

The report then proves a Gibbs price-Bellman lower envelope and explicitly leaves the low-price Boolean-shape region open.

There is an exact compatibility failure that must be propagated: the earlier completed account03/B12 report

`20260922T061544Z-biased-prime-candidate-refutation/REPORT.md`

already gives an actual composition-prime 18-input Boolean gate with

\[
p_1=3/8,\quad p_2=\cdots=p_{18}=1/2,\quad q=967/2048
\]

and

\[
D_{\Gamma^\dagger}=-0.0176114199558017537894958865691\ldots<0.
\tag{1.3}
\]

Thus the lead's `Gamma^dagger` is not a live universal candidate. Applying the lead's own exact normalization rather than reverting to an older defect gives

\[
v=4q(1-q)=\frac{1045327}{1048576}
\]

and therefore

\[
\boxed{R_B=-0.01766615833282291549110894366555\ldots<0.}
\tag{1.4}
\]

So `B-GIBBS-KL-v1 : R_B\ge0` is decisively refuted on an **actual Boolean common source and a composition-prime gate**. This refutes that stronger fixed-potential bridge, not FEI.

For diagnostic scale only, inserting the certified witness values into the lead's scalar Bellman expression gives

\[
a_1\approx6.65615212435,\qquad a_q\approx6.55970663525,
\]
\[
A_0\approx0.21393695566,\qquad
m=\mathbb E_{w^+}\sum_{i\in S}a_i\approx13.2768763011.
\]

The scalar safe threshold is about `17.32650`, while the optimized scalar Bellman envelope is about `-2.22594` bits. The actual Boolean shape/relative-entropy term recovers about `2.20827` bits but still misses by (1.4). These decimals are diagnostics, not a certificate; the refutation itself is the exact source-bound defect plus (1.2).

## 2. Named other-account result consumed and applied

I also consume account04/B17

`20260922T081319Z-birth-entropy-cancellation-axis/REPORT.md`.

That report proves an exact Boolean one-axis Fourier transport theorem for essential composition-prime five-input gates. Its key cancellation is that newborn spectral entropy `beta h_2(r^2)` is paid by the pivot's physical `d h_2(r^2)` term, with surplus `(d-beta)h_2(r^2)`, while the old-support relative-entropy credit is retained. It proves

\[
D_{\Gamma^\dagger}(P;p)>0
\quad\text{whenever exactly one bias moves and}\quad
|p_k-1/2|\le2.59\times10^{-5},
\tag{2.1}
\]

for every essential composition-prime five-input gate.

I use this theorem below rather than repeating that search: the replacement potential is a **positive quadratic lift**, and the exact monotonicity theorem in Section 3 shows every source safe under `Gamma^dagger` stays safe. Hence the entire five-input axis tube (2.1), including its signed birth cancellation and retained KL credit, transfers automatically to the new candidate.

## 3. Exact cardinality-tilt theorem

Let `Gamma` be any symmetric potential and define, for real `delta`,

\[
\Gamma_\delta(p)=\Gamma(p)+\delta p(1-p)
                 =\Gamma(p)+\frac\delta4 V_p.
\tag{3.1}
\]

For a nonconstant Boolean gate, write

\[
I_p=\sum_i \operatorname{It}_i(G;p),\qquad
v=V_q,
\qquad
\mu=\mathbb E_{w^+}|S|=I_p/v.
\tag{3.2}
\]

### Theorem 3.1 — uniform quadratic lift is exactly a Gibbs cardinality tilt

For every Boolean gate of every arity and every interior product bias,

\[
\boxed{a_i^{(\delta)}=a_i+\delta/4,\qquad
       a_q^{(\delta)}=a_q+\delta/4.}
\tag{3.3}
\]

Consequently, with `s=2^{-delta/4}`,

\[
x_i^{(\delta)}=s x_i,\qquad x_q^{(\delta)}=s x_q,
\tag{3.4}
\]

so the Gibbs reference is tilted by the exact cardinality factor `s^{|S|}`. At the all-gate defect and normalized-residual levels,

\[
\boxed{
D_{\Gamma_\delta}(G;p)
=D_\Gamma(G;p)+\frac\delta4(I_p-v),
}
\tag{3.5}
\]

\[
\boxed{
R_{B,\delta}(G;p)
=R_B(G;p)+\frac\delta4(\mu-1).
}
\tag{3.6}
\]

**Proof.** Equation (3.3) follows immediately after dividing the added term `delta V_p/4` by `V_p` in each input price and at the output. Equation (3.4) is exponentiation. In the all-gate inequality the added input payment is

\[
\sum_i \frac{\operatorname{It}_i}{V_{p_i}}\frac\delta4V_{p_i}
=\frac\delta4 I_p,
\]

whereas the added output cost is `delta V_q/4=delta v/4`; subtracting proves (3.5). Dividing by `v>0` and using (3.2) proves (3.6). No sign, coordinate price, spectral reconstruction term, or negative KL credit is discarded. `QED`.

Since Poincare gives `I_p\ge v`, every `delta>=0` makes the defect monotone nondecreasing for **every actual Boolean gate**. In particular all already-proved safe gates and bias regions remain safe.

A useful exact reformulation is

\[
K_\Gamma(G;p)
=\frac{[-R_B(G;p)]_+}{\mu-1}
=\frac{[-D_\Gamma(G;p)]_+}{I_p-v}
\tag{3.7}
\]

when `mu>1`. If the supremum of (3.7) over actual Boolean prime gates and interior biases is finite, then adding `4K p(1-p)` proves the all-gate inequality and increases the center by exactly `K`. Thus the replacement target is a **Boolean shape deficit per unit Poincare excess**, not an unnormalized entropy remainder.

## 4. Execute the replacement: `c_1=0.34`

Write the previous candidate as

\[
\Gamma^\dagger=\Gamma_0+0.268204856\,p(1-p).
\]

The completed B12 witness has

\[
I_p=8295/4096,
\qquad
I_p-v=\frac{1078193}{1048576},
\qquad
M=\frac{I_p-v}{4}=\frac{1078193}{4194304}.
\tag{4.1}
\]

Its required quadratic margin relative to `Gamma_0` is therefore

\[
\boxed{c_{\rm wit}=0.33671545583351692983194822728428\ldots.}
\tag{4.2}
\]

Equivalently its required center increment over `C^dagger` in the pure cardinality direction is

\[
K_{\rm wit}=0.01712764995837923245798705682107\ldots.
\tag{4.3}
\]

I now instantiate

\[
\boxed{\Gamma^{(1)}(p)=\Gamma_0(p)+0.34\,p(1-p),}
\tag{4.4}
\]

whose center is

\[
\boxed{C_1=\Gamma^{(1)}(1/2)=6.5398.}
\tag{4.5}
\]

This is not claimed universal. It is a concrete replacement candidate with finite dimension-independent center.

For the actual 18-input prime witness, `delta=0.071795144` relative to `Gamma^dagger`, and (3.5) gives

\[
\boxed{D_{\Gamma^{(1)}}
=0.0008443290063125803169494259309\ldots>0,}
\tag{4.6}
\]

or normalized

\[
R_B^{(1)}=0.00084695328076594234954761643478\ldots>0.
\tag{4.7}
\]

In the owner's comparable margin units, (4.2) is the key number: the witness asks for `0.3367154558...`, below the executed coefficient `0.34` by `0.00328454416648...`.

By monotonicity (3.5), account04/B17's entire certified five-input one-axis tube (2.1) also remains safe under `Gamma^(1)` without rerunning its finite classification.

## 5. Actual Boolean adversarial sanity checks: majority and composition

These checks are deliberately on genuine Boolean sources.

### 5.1 Recursive ternary majority

For depth-`d` recursive ternary majority, an earlier complete B17 proof gives

\[
I_d=(3/2)^d,\qquad H_d=4(I_d-1).
\]

At uniform bias the new residual is therefore exactly

\[
R_B^{(1)}=C_1(I_d-1)-H_d=(C_1-4)(I_d-1)>0.
\tag{5.1}
\]

So recursive majority is not an adversary to the executed candidate at the balanced point.

### 5.2 Ordinary odd majority

I recomputed the actual uniform spectra for odd majority through `n=17`. The excess ratios `H/(I-1)` were

`n=3: 4.000000`, `5: 3.800429`, `7: 3.681674`, `9: 3.600531`, `11: 3.540497`, `13: 3.493716`, `15: 3.455906`, `17: 3.424507`.

Thus every tested majority is far below even the refuted `C^dagger`, and hence below `C_1`. This is a finite falsification check, not a theorem for all odd `n`.

### 5.3 Tensors and balanced self-composition

For a balanced Boolean tensor product on disjoint coordinates,

\[
H(f\otimes g)=H(f)+H(g),\qquad I(f\otimes g)=I(f)+I(g).
\tag{5.2}
\]

Hence ordinary tensor powers of a fixed balanced source with `H/I<C_1` cannot create a large-`m` negative residual; the leading slope is `m(C_1 I-H)`.

More sharply, for balanced self-composition `F=f(f^{(1)},\ldots,f^{(n)})` on disjoint blocks,

\[
I(F)=I(f)^2,
\qquad
H(F)=(1+I(f))H(f),
\]

so

\[
\frac{H(F)}{I(F)-1}=\frac{H(f)}{I(f)-1}.
\tag{5.3}
\]

The source-bound 18-input seed has

\[
\frac{H}{I-1}=6.5218457109230465756581\ldots,
\]

so every balanced self-composition stays below the new center `6.5398`; already at the seed the new balanced-center defect is about `0.01865562849`. Thus the known recursive/tensor amplifiers do not refute the replacement at the balanced point. The genuinely dangerous phenomenon remains **biased prime-gate shape**, exactly as the B12 witness demonstrates.

## 6. Remaining universal implication

The fixed candidate `Gamma^dagger` and its universal normalized residual are retired by (1.4). The executed replacement is

\[
\Gamma^{(1)}=\Gamma_0+0.34p(1-p),\qquad C_1=6.5398.
\]

The exact remaining implication is

\[
\boxed{
R_B^{(1)}(P;p)
=D_{\rm KL,2}(w^+\|\nu_{x^{(1)}}^+)
-\log_2(A_0^{(1)}/x_q^{(1)})\ge0
}
\tag{6.1}
\]

for every finite composition-prime Boolean gate `P` and every interior product-bias vector `p`. Equivalently, no actual Boolean prime/bias source may have required margin `c_P(p)>0.34`.

This is not closure. A new prime Boolean gate with margin above `0.34` would refute only this finite-center candidate and would prescribe the next cardinality lift; it would not refute FEI. The next Campaign-B adversarial search should therefore maximize the comparable quantity `c_P=-D_{Gamma_0}/M` (or equivalently (3.7)), while retaining the full signed Boolean spectrum and relative-entropy credits, instead of optimizing raw `D`, raw entropy, or arbitrary-row relaxations.

## 7. Operational / verification scope

The scientific claims above use exact algebra plus source-bound certified witness values. The only new numerical enumerations are the odd-majority checks through `n=17`; they are explicitly finite diagnostics. The scalar Bellman optimizer values in Section 1 are descriptive diagnostics and are not used in any theorem.

A fresh scheduler inspection was limited to account02. All twenty managed B01--B20 tasks were exposed as enabled with hourly recurrences; B12--B18 remain on FEI and task notification/email flags are off. No scheduler mutation was made and no account-local deficit requires a B20 repair report.

Scoped privacy/source review: this report contains no credentials, scheduler identifiers, machine paths, raw transcripts, benchmark gold, unrelated private data, email/Drive content, permission changes, or public-posting action. Historical and peer artifacts are referenced read-only. The denied canonical login write was not bypassed.
