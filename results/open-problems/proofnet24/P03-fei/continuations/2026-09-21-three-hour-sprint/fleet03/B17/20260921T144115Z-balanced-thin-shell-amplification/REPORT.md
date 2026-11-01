# B17 FEI new proof mechanism — balanced thin-shell tensor amplification

**Date:** 2026-09-21  
**Status of full FEI:** **OPEN / NOT PROVED**.  
**Run status:** `WITHOUT_VERIFIED_BRAIN` — no authenticated mathematical/cognitive-brain retrieval or receiver-context use occurred.  
**Role:** fleet03/B17, FEI new proof mechanisms.  
**Route:** New Route 18 — balanced thin-shell tensor amplification / within-level obstruction.

The mandated scientific entry was read in order from `TASKS_2026-09-21.md`, then `REPORT.md`, then `APPROACHES.md`. I also inspected the immediately preceding fleet03/B17 Han-deficit/local-credit result before continuing. This run deliberately changes mechanism: it uses exact Boolean tensor amplification to normalize any hypothetical counterexample into a balanced, high-influence, Fourier-diffuse, relatively thin-shell counterexample. It is not another local restriction charge, face-channel constant search, Han-deficit estimate, MUX calculation, or finite exhaustive FEI sweep.

No novelty or publication-priority claim is made here. The result is recorded as a reusable exact reduction and as guidance for the next universal attack.

## 1. Setup

For a Boolean function

\[
f:\{-1,1\}^n\to\{-1,1\},
\]

write

\[
p_f(A)=\widehat f(A)^2,
\qquad S_f\sim p_f,
\qquad K_f=|S_f|.
\]

Then

\[
H(f)=H(S_f),
\qquad I(f)=\mathbb E K_f.
\]

Let

\[
V_f:=\operatorname{Var}(K_f),
\qquad p_*(f):=\max_A p_f(A),
\]

and define the within-level spectral entropy

\[
H_{\rm sh}(f):=H(S_f\mid K_f)=H(f)-H(K_f). \tag{1.1}
\]

The subscript `sh` stands for shell: it measures the entropy of the Fourier location after the Fourier level has already been disclosed.

## 2. PROVED: exact balanced tensor amplification

Take `m` disjoint copies of the variables of `f`, denoted

\[
x^{(1)},\ldots,x^{(m)},
\]

and add one independent cube coordinate `z`. Define

\[
F_m(z,x^{(1)},\ldots,x^{(m)})
:=z\prod_{j=1}^m f(x^{(j)}). \tag{2.1}
\]

### Theorem 2.1 — exact spectral product law

For every Boolean `f` and every integer `m>=1`:

1. `F_m` is Boolean and balanced;
2. if `S_1,...,S_m` are independent copies of `S_f` on disjoint coordinate blocks, then the spectral sample of `F_m` is exactly

\[
S_{F_m}=\{z\}\cup S_1\cup\cdots\cup S_m; \tag{2.2}
\]

3. consequently

\[
\boxed{H(F_m)=mH(f)}, \tag{2.3}
\]

\[
\boxed{I(F_m)=1+mI(f)}, \tag{2.4}
\]

\[
\boxed{V_{F_m}=mV_f}, \tag{2.5}
\]

and

\[
\boxed{p_*(F_m)=p_*(f)^m}. \tag{2.6}
\]

#### Proof

The factor `z` makes `F_m` balanced because `E z=0`, independently of the bias of `f`.

Fourier expansion on disjoint blocks gives

\[
\prod_{j=1}^m f(x^{(j)})
=
\sum_{A_1,\ldots,A_m}
\left(\prod_{j=1}^m\widehat f(A_j)\right)
\chi_{A_1\sqcup\cdots\sqcup A_m}.
\]

Multiplication by `z` appends the new coordinate to every Fourier set. Therefore

\[
\widehat{F_m}(\{z\}\sqcup A_1\sqcup\cdots\sqcup A_m)^2
=
\prod_{j=1}^m p_f(A_j),
\]

with no other spectral atoms. This is exactly the product law (2.2). Shannon entropy adds under independent products, giving (2.3). Spectral sizes satisfy

\[
K_{F_m}=1+K_1+\cdots+K_m,
\]

which gives (2.4)-(2.5), and the largest atom of a product distribution is the product of the largest atoms, giving (2.6). □

### Balanced bases need no overhead

If `f` is already balanced, then

\[
G_m(x^{(1)},\ldots,x^{(m)})=\prod_{j=1}^m f(x^{(j)}) \tag{2.7}
\]

is itself balanced and satisfies the stronger exact identities

\[
H(G_m)=mH(f),\qquad I(G_m)=mI(f),\qquad
V_{G_m}=mV_f,\qquad p_*(G_m)=p_*(f)^m. \tag{2.8}
\]

Thus tensor amplification preserves the FEI ratio **exactly** for balanced bases.

## 3. PROVED: FEI is exactly equivalent to balanced FEI

### Corollary 3.1 — balanced reduction with the same constant

Fix `C>=0`. The following statements are equivalent:

1. every Boolean function satisfies `H(f)<=C I(f)`;
2. every **balanced** Boolean function satisfies `H(f)<=C I(f)`.

#### Proof

Only `(2) => (1)` needs proof. Suppose instead that some Boolean `f` violates the desired constant. Put

\[
\delta:=H(f)-C I(f)>0.
\]

For (2.1),

\[
H(F_m)-C I(F_m)
=mH(f)-C(1+mI(f))
=m\delta-C. \tag{3.1}
\]

For every integer `m>C/delta`, the right side is positive. But `F_m` is balanced, contradicting (2). □

This is an exact reduction, not an asymptotic assumption: any strict unrestricted violation at a proposed constant produces a strict balanced violation at the same constant after finitely many tensor copies.

### Corollary 3.2 — high influence is sufficient

Fix any finite threshold `I_0`. If `H(g)<=C I(g)` is proved for every balanced Boolean `g` with `I(g)>=I_0`, then it already holds for **all** Boolean functions.

Indeed, a strict violating base `f` produces violating `F_m` by (3.1), while `I(F_m)=1+mI(f)` can simultaneously be made larger than `I_0`.

Thus a universal proof does not need a separate low-total-influence argument if it can establish the sharp inequality in the balanced high-influence regime.

## 4. PROVED: every obstruction can be made Fourier-diffuse and thin-shell

Assume `H(f)>0`. Then `p_*(f)<1`; otherwise the spectral law is a point mass and has zero entropy. Hence (2.6) gives

\[
p_*(F_m)\longrightarrow0. \tag{4.1}
\]

Moreover

\[
\frac{\operatorname{Var}(K_{F_m})}{I(F_m)^2}
=
\frac{mV_f}{(1+mI(f))^2}
\longrightarrow0. \tag{4.2}
\]

So Chebyshev gives, for every fixed `epsilon>0`,

\[
\Pr\left(
|K_{F_m}-I(F_m)|>\epsilon I(F_m)
\right)
\le
\frac{mV_f}{\epsilon^2(1+mI(f))^2}
\longrightarrow0. \tag{4.3}
\]

The amplified spectral sample therefore lies in a relative thin shell around its mean degree.

At the same time,

\[
\frac{H(F_m)}{I(F_m)}
=
\frac{mH(f)}{1+mI(f)}
\longrightarrow
\frac{H(f)}{I(f)}. \tag{4.4}
\]

Thus neither strong bias, a giant Fourier atom, nor broad **relative** level fluctuations are necessary features of a near-extremal FEI obstruction.

### Finite-threshold version

Fix `C`, a finite `I_0`, and `eta>0`. Suppose the FEI inequality with constant `C` is known for every balanced Boolean `g` satisfying

\[
I(g)\ge I_0,\qquad
p_*(g)\le\eta,\qquad
\frac{\operatorname{Var}(K_g)}{I(g)^2}\le\eta. \tag{4.5}
\]

Then it holds for every Boolean function.

If a strict violating `f` existed, `H(f)>0`, and the sequence `F_m` would eventually satisfy all three conditions in (4.5) while still violating by (3.1).

This is a useful normal form for the universal problem.

## 5. PROVED: the sharp FEI obstruction can be pushed almost entirely inside Fourier levels

Because `K_{F_m}` takes at most `mn+1` values,

\[
H(K_{F_m})\le\log_2(mn+1). \tag{5.1}
\]

Since `K_{F_m}` is a deterministic function of `S_{F_m}`,

\[
H_{\rm sh}(F_m)
=H(F_m)-H(K_{F_m})
=mH(f)-H(K_{F_m}). \tag{5.2}
\]

Combining (2.4), (5.1), and (5.2),

\[
\frac{H_{\rm sh}(F_m)}{I(F_m)}
\longrightarrow
\frac{H(f)}{I(f)}. \tag{5.3}
\]

This gives the main structural conclusion of the run.

### Theorem 5.1 — sharp-constant within-shell reduction

Let

\[
C_*:=\sup_{f:I(f)>0}\frac{H(f)}{I(f)}
\]

in the extended-real sense. Then `C_*` is also the supremal asymptotic value of

\[
\frac{H(S_g\mid |S_g|)}{I(g)} \tag{5.4}
\]

along sequences of balanced Boolean functions `g` satisfying

\[
I(g)\to\infty,\qquad
p_*(g)\to0,\qquad
\frac{\operatorname{Var}(|S_g|)}{I(g)^2}\to0. \tag{5.5}
\]

#### Proof

For every `g`, `H(S_g\mid |S_g|)<=H(g)`, so every limit superior in (5.4) is at most `C_*`.

Conversely, fix any Boolean `f` with positive entropy. The sequence `F_m` from Theorem 2.1 satisfies all three conditions in (5.5) by (2.4), (4.1), and (4.2), while (5.3) shows its within-shell ratio tends to `H(f)/I(f)`. Taking the supremum over base functions proves equality. Functions with zero spectral entropy contribute ratio zero and do not affect the supremum. □

### Corollary 5.2 — a shell-only theorem would prove full FEI

Fix `C`. It is enough to prove

\[
H(S_g\mid |S_g|)\le C I(g) \tag{5.6}
\]

for the balanced, high-influence, Fourier-diffuse, relatively thin-shell regime in (5.5), uniformly along every such sequence.

Indeed, if some base had gap `delta=H(f)-C I(f)>0`, then

\[
H_{\rm sh}(F_m)-C I(F_m)
=m\delta-C-H(K_{F_m}), \tag{5.7}
\]

and the right side tends to `+infinity` because `H(K_{F_m})=O(log m)`. So sufficiently large `m` would violate (5.6).

This identifies a different universal bottleneck from the previous B17 local-credit route: after exact Boolean normalization, the hard entropy may be assumed to be **within a narrow Hamming shell**, not in uncertainty about the Fourier degree.

## 6. Exact admissible Boolean stress tests

A targeted exact Walsh checker was run on boundary functions. It uses `Fraction` arithmetic for the Walsh law, influences, spectral-size moments, product-law equality and largest atoms. Decimal entropy displays are evaluated only after the exact law comparison.

### 6.1 Two-bit one-point defect

The base spectrum is exactly uniform on all four subsets:

\[
H=2,\quad I=1,\quad \operatorname{Var}K=\frac12,\quad p_*=\frac14.
\]

For `m=2` with the balancing bit, the exact amplified law matches the product prediction and gives

\[
H=4,\quad I=3,\quad \operatorname{Var}K=1,\quad p_*=\frac1{16}.
\]

No biased-family pathology breaks the construction.

### 6.2 Three-bit majority

For balanced majority on three bits,

\[
H=2,\quad I=\frac32,\quad \operatorname{Var}K=\frac34,\quad p_*=\frac14.
\]

The two-copy product **without** a balancing bit is again balanced and has exactly

\[
H=4,\quad I=3,\quad \operatorname{Var}K=\frac32,\quad p_*=\frac1{16},
\]

so its FEI ratio is preserved exactly, as (2.8) claims.

### 6.3 Character boundary

A nonconstant character has a one-atom Fourier law, hence `H=0`, `Var K=0`, and `p_*=1`. Tensor amplification leaves spectral entropy zero. This is precisely the exceptional zero-entropy case excluded from the diffuse conclusion (4.1), and it cannot obstruct FEI.

### 6.4 Constant boundary

A constant has `H=I=0`. FEI is trivial and no ratio is formed. The checker keeps this degenerate case separate.

All exact structural checks passed. These examples are targeted stress tests of the proved identities, not evidence for full FEI by finite enumeration.

## 7. Dead routes and what the reduction rules out

This theorem does **not** prove FEI. It does, however, kill several possible universal narratives:

* a hypothetical counterexample cannot be dismissed merely because it is biased — a balanced one follows by finite amplification;
* proving the target only for bounded total influence is not enough to isolate the difficulty — every strict counterexample amplifies to arbitrarily large influence;
* a proof cannot rely on every hard example having a dominant Fourier coefficient — the maximum atom can be driven to zero exponentially while retaining the ratio;
* a proof that controls only the entropy of the Fourier **level** cannot close the conjecture — any obstruction can be amplified until level entropy is `o(I)` while essentially the original FEI ratio survives.

The last point is the decisive method change. The remaining universal content can be pushed into the geometry and signs **inside Hamming shells**.

## 8. Next attack: Boolean shell rigidity from the exact convolution equations

For a Boolean `f`, its Fourier amplitudes `a_A=hat f(A)` obey the exact autocorrelation/convolution constraints coming from `f^2=1`:

\[
\sum_A a_A a_{A\triangle T}=0
\quad\text{for every nonempty }T, \tag{8.1}
\]

with `sum_A a_A^2=1` for `T=emptyset`.

The amplification theorem says it is enough to understand high-entropy solutions whose squared mass is concentrated in a narrow Hamming annulus. That suggests a new target not covered by the previous restriction/face-channel machinery:

> **Shell-rigidity target (OPEN):** derive a dimension-free upper bound on the within-shell entropy `H(S||S|)` from `E|S|` for real Walsh amplitude vectors satisfying all Boolean convolution equations (8.1), at least when the degree law is relatively concentrated.

A particularly concrete first subproblem is the exact-level case: classify or entropy-bound Boolean Laplacian eigenfunctions whose Fourier support lies on one Hamming level. Such functions correspond to constant-sensitivity/equitable cube colorings, so arbitrary constant-weight subset laws are inadmissible. The goal is to exploit (8.1) or the resulting constant-sensitivity geometry to prove `H(f)=O(k)` when the spectrum lies on level `k`, then extend stably to an `o(k)`-width shell.

This is the next attack. It is structurally different from another small-dimensional sweep: it asks for a theorem on Boolean shell rigidity. Full FEI remains **OPEN** until that or another universal step is proved.
