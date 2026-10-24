# B13 FEI Booleanity profile — exact rigidity of independent spectral samples

**Status:** PARTIAL / PROVED structured-class theorem + exact finite falsification search + OPEN universal stability target. Full uniform-cube Fourier entropy-influence (FEI) remains **OPEN / NOT PROVED**.

**Execution:** **WITHOUT_VERIFIED_BRAIN**. No genuine authenticated mathematical/cognitive brain retrieval or receiver-context use occurred in this run.

**Route:** APPROACHES 2/13/14. This run changes category from zeta-Palm coordinate elimination to the exact Boolean obstruction to the product-set spectral laws that would otherwise violate FEI. It does not re-run the settled read-once certificate or audit a previous sweep.

**No novelty claim:** the theorem below is a new-to-this-run deduction for the fleet. No publication-priority claim is made without a dedicated primary-literature comparison; the final characterization is naturally expressed in the classical language of bent Boolean functions.

## 1. Fresh frontier used

The owner handoff keeps full FEI open and emphasizes that scalar/quantization conditions are not sufficient: there are dyadic-square subset laws with unbounded entropy/mean-size ratio that pass a long list of scalar necessary tests but fail an exact Boolean sign/parity constraint. Thus a useful profile route must retain genuinely joint Boolean arithmetic rather than only marginals or hashes.

The preceding B13 run isolated exact projected phase/cross-correlation constraints and refuted two tempting shortcuts: every-coordinate zeta-Palm payment is false, and Boolean spectral samples need not be negatively associated. The present run therefore asks the most basic coding/point-process question left by APPROACHES 2/13/14:

> **Can the spectral sample of a Boolean function actually be an independent product-set process with small nonzero inclusion probabilities?**

For an arbitrary random subset the answer is trivially yes and `H(S)/E|S|` is then unbounded as the Bernoulli marginals tend to zero. The theorem below shows that Booleanity completely forbids this mechanism.

## 2. Exact statement attempted

Let `f:{-1,1}^n->{-1,1}` and let its spectral sample `S` satisfy

\[
\Pr[S=A]=\widehat f(A)^2,
\qquad A\subseteq[n].
\]

Assume the coordinate indicators `1_{i in S}` are mutually independent, with inclusion probabilities

\[
p_i=\Pr[i\in S]=\operatorname{Inf}_i(f).
\]

### Theorem 2.1 — product-spectrum rigidity

For every such Boolean `f`,

\[
\boxed{p_i\in\{0,1/2,1\}\quad\text{for every }i.}
\]

More precisely, there is a partition `[n]=Z\sqcup O\sqcup H` such that

* `p_i=0` on `Z`,
* `p_i=1` on `O`,
* `p_i=1/2` on `H`,
* `|H|` is even, and
* after deleting the irrelevant coordinates `Z`,
  \[
  f(x)=\chi_O(x)\,g(x_H),
  \]
  where `g` is a bent Boolean function on the even-dimensional cube `H`, equivalently every Walsh-Fourier coefficient of `g` has the same magnitude `2^{-|H|/2}`.

Conversely, every Boolean function of this form has an independent product spectral sample with exactly those marginals.

Consequently this whole structured class obeys the sharp class bound

\[
\boxed{H(f)=|H|\le 2I(f),}
\]

with equality when `O` is empty.

This is **not** full FEI; it exactly eliminates one high-entropy point-process obstruction.

## 3. Proof

Coordinates with `p_i=0` have no Fourier mass on sets containing `i`, hence `f` is independent of those coordinates. If `p_i=1`, every Fourier-support set contains `i`; multiplying `f` by the character `x_i` toggles `i` out of every Fourier-support set and leaves Booleanity intact. Thus, after deleting `p_i=0` coordinates and multiplying by the character on the `p_i=1` coordinates, it is enough to treat a Boolean function `g` on `m` coordinates for which

\[
0<p_i<1\quad (1\le i\le m).
\]

Independence then gives positive mass to every spectral atom, so every Fourier coefficient is nonzero.

Write the unnormalised Walsh coefficients

\[
W_A=2^m\widehat g(A)=\sum_{x\in\{-1,1\}^m}g(x)\chi_A(x)\in\mathbb Z.
\]

The product law gives

\[
\frac{W_A^2}{4^m}
=\prod_{i\in A}p_i\prod_{i\notin A}(1-p_i).
\tag{3.1}
\]

For every `i` and every `A` not containing `i`, division of (3.1) yields

\[
\frac{|W_{A\cup\{i\}}|}{|W_A|}
=\sqrt{\frac{p_i}{1-p_i}}.
\tag{3.2}
\]

The left side is a ratio of nonzero integers. Hence, in lowest terms,

\[
\sqrt{\frac{p_i}{1-p_i}}=\frac{a_i}{b_i},
\qquad a_i,b_i\in\mathbb Z_{>0},\quad \gcd(a_i,b_i)=1.
\]

Iterating (3.2),

\[
|W_A|
=d\prod_{i\in A}a_i\prod_{i\notin A}b_i,
\qquad
d=\frac{|W_\varnothing|}{\prod_i b_i}\in\mathbb Q_{>0}.
\tag{3.3}
\]

In fact `d` is an integer. To see this, define

\[
M_A=\prod_{i\in A}a_i\prod_{i\notin A}b_i.
\]

For any prime `ell`, and for every coordinate `i`, at least one of `a_i,b_i` is not divisible by `ell`. Choose `A` coordinatewise so that `M_A` always uses a factor not divisible by `ell`. Then `ell` does not divide this `M_A`. Therefore

\[
\gcd_{A\subseteq[m]}M_A=1.
\]

Since every `dM_A=|W_A|` is an integer, the denominator of `d` divides every `M_A`, hence divides `1`. Thus `d\in\mathbb Z_{>0}`.

Parseval for Boolean `g` gives

\[
\sum_AW_A^2=4^m.
\]

Using (3.3),

\[
\boxed{d^2\prod_{i=1}^m(a_i^2+b_i^2)=4^m.}
\tag{3.4}
\]

Every positive integer factor `a_i^2+b_i^2` in (3.4) therefore has no odd prime divisor, so it is a power of two. Because `a_i,b_i` are positive and coprime, they cannot have opposite parity: that would make `a_i^2+b_i^2` an odd integer greater than one. They cannot both be even. Hence both are odd, so

\[
a_i^2+b_i^2\equiv2\pmod4.
\]

The only power of two congruent to `2 mod 4` is `2`. Thus

\[
a_i^2+b_i^2=2,
\qquad a_i=b_i=1.
\]

Equation (3.2) now gives `p_i/(1-p_i)=1`, hence `p_i=1/2` for every non-deterministic coordinate.

Therefore the active spectral law is uniform on all `2^m` subsets. In particular

\[
|\widehat g(A)|=2^{-m/2}
\quad\text{for every }A,
\]

so

\[
|W_A|=2^{m/2}.
\]

Because `W_A` is an integer, `m` must be even. This is exactly the flat-Walsh (bent-function) condition. Reattaching the deterministic-one coordinates multiplies by `chi_O`; reattaching the deterministic-zero coordinates only adds irrelevant variables. The converse follows immediately from a flat Walsh spectrum and character translation. QED.

Finally, under the classified product law,

\[
H(S)=|H|,
\qquad
I(f)=\sum_i p_i=|O|+\frac{|H|}{2},
\]

which proves `H(f)<=2I(f)` for this class.

## 4. Decisive exact counterexample search

A separate exact-arithmetic enumeration was run over all Boolean truth tables modulo global sign through `n=4`. For each function it computed the integer Walsh transform, tested the full product identity exactly using rational arithmetic, extracted exact marginals, and rejected the theorem if any product-spectrum example had a marginal outside `{0,1/2,1}`.

Results:

| n | product-spectrum functions modulo global sign | distinct marginal patterns | count by number of 1/2 marginals | violations |
|---:|---:|---:|---|---:|
| 1 | 2 | 2 | `{0: 2}` | 0 |
| 2 | 8 | 5 | `{0: 4, 2: 4}` | 0 |
| 3 | 32 | 14 | `{0: 8, 2: 24}` | 0 |
| 4 | 560 | 41 | `{0: 16, 2: 96, 4: 448}` | 0 |

The even number of half-marginals visible in the enumeration is explained by the integrality step in the proof (`|H|` must be even), rather than being merely an observed pattern.

The enumeration is a falsification check only; the theorem itself is the all-dimensional argument above.

## 5. What this says about the full FEI mechanism

For a general spectral sample with marginals `p_i`, write the total correlation

\[
\mathrm{TC}(S)=D\left(P_S\middle\|\prod_i\mathrm{Bern}(p_i)\right)
=\sum_i h_2(p_i)-H(S).
\]

Thus full FEI would follow from a dimension-free Booleanity inequality of the form

\[
\mathrm{TC}(S)
\ge
\sum_i\bigl[h_2(p_i)-C p_i\bigr]_+
\tag{5.1}
\]

for some universal `C`: subtracting (5.1) from the marginal entropy bound gives `H(S)<=C sum_i p_i=C I(f)`.

The product-spectrum theorem proves the exact zero-total-correlation endpoint of this program: when `TC(S)=0`, Booleanity forces every active marginal to be `1/2`, so no tiny-marginal entropy explosion is possible. It does **not** provide the quantitative stability needed when `TC(S)>0`.

As a finite stress test, exhaustive `n<=4` enumeration found that (5.1) holds for all Boolean functions already at approximately

\[
C_{\le4}=3.75925424014,
\]

with the binding `n=4` example having marginal vector

\[
(1/8,1/8,3/8,3/8),
\]

spectral entropy `2.848681565885773`, total influence `1`, and total correlation

\[
0.14731532636334999.
\]

This finite constant is **not** a universal FEI constant and is not a novelty claim; it only identifies a concrete quantitative direction for the next attack. The current known larger-dimensional lower obstructions mean any eventual universal argument must accommodate substantially harder families.

## 6. Dead routes and classifications

**PROVED:** exact classification of independent/product Boolean spectral samples as character shifts of bent spectra with irrelevant variables; class constant `2`.

**REFUTED previously and retained:** unrestricted Boolean spectral samples are not necessarily negatively associated, so standard determinantal/negative-dependence entropy theorems cannot be imported wholesale.

**REFUTED by the fresh fleet handoff and retained:** scalar/quantization necessary conditions, even many simultaneous ones, do not characterize Boolean spectra; a joint sign/parity condition is indispensable.

**OPEN:** a quantitative stability theorem converting small total correlation or near-product structure into closeness of the marginals to `{0,1/2,1}` strongly enough to pay the entropy excess in (5.1).

**OPEN:** full FEI.

## 7. Next attack

The next B13 attack should prove or kill a **product-rigidity stability lemma**. A concrete target is to bound

\[
\sum_i [h_2(p_i)-C p_i]_+
\]

by the total correlation plus a signed/autocorrelation defect that is forced to vanish for genuine Boolean spectra. The proof above suggests using approximate rank-one relations among the integer Walsh magnitudes, while the newest dyadic-relaxation counterexample says that magnitude quantization alone is insufficient; the missing ingredient must couple those approximate ratios to the exact convolution equations from `f^2=1`. A decisive next computation is to optimize (5.1) on the known hard FEI families and on projected Numaro/composition descendants, then inspect the coordinates where the total-correlation payment is tight.
