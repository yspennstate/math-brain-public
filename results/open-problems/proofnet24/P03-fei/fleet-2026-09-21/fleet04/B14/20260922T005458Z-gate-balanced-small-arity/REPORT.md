# B14 gate target: balanced-unate small-arity exclusion for the old read-once potential

**Date:** 2026-09-22  
**Account / slot:** fleet04 / B14  
**Run:** `B14-20260922T005458Z-gate-extremal-r11`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full FEI status:** OPEN / NOT PROVED

## 1. Why this run changed target


The scientific gate report fixes the old read-once candidate at

\[
C_0=\Gamma(1/2)=6.4548,
\]

with gate margin

\[
c_G(p)=-\frac{D_G(p)}{I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\]

The previous arity-two floor is approximately `0.0043974201`. A newer peer result (`fleet04/B12/20260922T004033Z-prime-safe-split`) has already shown that this *particular* fixed potential is globally false: the certified balanced 18-variable monotone seed has margin at least `0.2681828436921863...`. The useful question for this run was therefore: **how early can that failure appear, and does the owner's untouched arity-five search already contain it?**

## 2. Exact balanced-uniform reduction

Let a Boolean gate `G` have all input biases `p_i=1/2` and be balanced, so `p_out=1/2`. Then `V_{p_i}=1`, `h(V_{p_i})=0`, and every input sees the same potential value `C_0`. Hence the gate defect and Poincare denominator collapse to

\[
D_G=C_0 I(G)-H(G)-C_0=C_0(I(G)-1)-H(G),
\]
\[
P_G=\frac{I(G)}4-\frac14=\frac{I(G)-1}{4}.
\]

Therefore, whenever `I(G)>1`,

\[
\boxed{\quad c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right).\quad}
\]

This identity is independent of the values of `Gamma` away from `1/2`. It turns the balanced uniform arity-five search into a finite search for large amplified ratio `H/(I-1)`.

For the certified 18-variable seed, the published/recovered interval

\[
\frac{H}{I-1}\ge 6.5218457109230465756581439729\ldots
\]

immediately gives

\[
c_{18}\ge4(6.5218457109230465\ldots-6.4548)
=0.2681828436921863\ldots,
\]

exactly matching the newer prime-safe-split obstruction. Thus the global "AND is extremal for this fixed potential" route is already false; only a bounded-arity or structural version can survive.

## 3. New exhaustive monotone calculation through arity six

I exhaustively generated **every monotone Boolean function** on five and six variables by the exact recursion

\[
\mathcal M_n=\{(f_0,f_1):f_0,f_1\in\mathcal M_{n-1},\ f_0\le f_1\text{ pointwise}\}.
\]

This gives the complete counts

- `M(5)=7581`, of which `621` are balanced;
- `M(6)=7828354`, of which `492288` are balanced.

For each balanced gate the checker computes the integer Walsh transform, exact influence numerator, and a rigorous upward bound on spectral entropy. The entropy table is not floating-point evidence: for each possible nonzero Walsh magnitude `w`, a companion script bounds `log_2(N^2/w^2)` from above using a 40-term exact-rational `atanh` series, rounds the resulting single-atom entropy contribution upward to units of `10^-15`, and the C++ checker verifies by integer arithmetic that

\[
\boxed{\frac{H(G)}{I(G)-1}<6.4}
\qquad\text{for every balanced monotone }G\text{ on }n=5,6,\ I(G)>1.}
\]

There were **zero** violations of this rational upper certificate.

The numerical maxima are much lower than the certificate threshold:

### Five inputs

The maximum is

\[
\frac{H}{I-1}=6,
\qquad H=3,\quad I=\frac32,
\]

attained by 60 truth tables in the enumeration (before quotienting by input symmetries).

### Six inputs

The maximum is

\[
\frac{H}{I-1}
=\frac{46}{5}-\frac95\log_2 3
=6.347067498701918873\ldots,
\]

attained by 180 truth tables in the enumeration. One representative is

`0xfff0faf0ffc00000`.

Its nonzero Walsh magnitudes have histogram

- `|W|=4`, multiplicity 32;
- `|W|=8`, multiplicity 4;
- `|W|=16`, multiplicity 4;
- `|W|=24`, multiplicity 4.

Thus

\[
I=\frac{13}{8},
\qquad
H=\frac{23}{4}-\frac98\log_2 3,
\]

which gives the displayed ratio exactly. The next distinct numerical ratio is `6.278945252708618110...`, leaving a wide gap.

## 4. Consequence for the owner's arity-five falsifier search

Uniform input negations, input permutations, and output negation preserve `H`, `I`, balance, and therefore `c_G`. Every unate Boolean function is an NPN transform of a monotone one. Consequently the exhaustive result proves:

\[
\boxed{\text{No balanced unate gate of arity }\le6\text{ can falsify the old candidate at uniform bias.}}
\]

Indeed the rigorous `6.4` bound gives

\[
c_G<4(6.4-6.4548)=-0.2192,
\]

far below both zero and the positive arity-two floor `0.0043974201`.

So the untouched arity-five search is now sharply narrowed:

1. any **uniform balanced** arity-five counterexample must be **non-unate**;
2. an arity-five unate counterexample, if one exists, must exploit **nonuniform biases**;
3. the known monotone obstruction at arity 18 cannot be a small-arity uniform monotone phenomenon: the first such monotone failure, if any, has arity at least 7.

This is a genuine elimination, not a proof of the all-gate inequality. I did **not** scan all 616,126 five-input NPN classes or the full nonuniform bias cube in this run.

## 5. Exact source-to-next-arrow use

**Source object:** the current gate reformulation `D_G>=0` plus the peer prime-safe-split theorem showing the old `Gamma` already fails globally.

**New output object:** a rigorous structural exclusion for balanced-uniform unate gates through arity six.

**Next arrow:** perform the owner's arity-five falsifier search only on the remaining non-unate NPN classes and/or nonuniform biases. If no arity-five witness exists, the next bounded-arity target is arity six non-unate; if a witness exists, report its exact truth table and bias vector and stop trying to prove decomposable extremality for this fixed potential.

## 6. Artifacts

- `fei_b14_monotone_gate_scan.cpp`: complete monotone recursion, exact Walsh/influence calculation, and integer verification of the `6.4` bound.
- `derive_entropy_upper_tables.py`: exact-rational derivation of the upward entropy atom tables.
- `fei_b14_monotone_gate_scan.out`: deterministic checker output.
- `entropy_tables.out`: generated tables.

Local SHA-256 values at execution:

- checker source: `19c96593f7cf58fb8d6043628778353afabe3416ede07786bb471b082dd1bf41`
- entropy-bound generator: `2061cfcdf86c107af8aadf39950551607ebf1702a70846e99024100002d56e6e`
- generated entropy tables: `a65ff63769aa7d7fd54cd1a4cc48b0411c4774b2c7aecd02e628479ef98007e5`
- checker stdout: `27b0cc9a8f780fe358d1bffb01671c51034be2c4664701a1b43041af15c59722`

No paid or remote compute was used. Full FEI remains open.
