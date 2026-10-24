# B17 FEI creative run — affine-character orbit normalization and exact rank rigidity of the Numaro seed

**Run:** `B17-20260921T141525Z-r29`  
**Status:** **PARTIAL. Full uniform-cube Fourier entropy–influence remains OPEN / NOT PROVED.**  
**Brain label:** **WITHOUT_VERIFIED_BRAIN.** No authenticated brain retrieval or receiver-side brain context was used.  
**Fresh scientific source:** `yspennstate/math-open-problems` master `7cec51d85a5188a99543d70217b08a34a2e43986` at the start of the derivation; master advanced through unrelated FEI work before delivery.  
**Active sprint:** `FEI-PROOF-NUMERICS-SPRINT-20260921T120803Z`; account04/B17 scope is adversarial non-read-once phase constructions.

## 1. Named obstruction and change of method

The two preceding B17 runs first showed that bounded local spectral marginals can miss arbitrarily large Boolean spectral KL, then bypassed that obstruction for balanced rare-selector substitution by an exact composition identity. This run changes mechanism again.

The coordinate directions appearing in total influence are not canonical inside the class of all Boolean functions: an invertible linear change of cube coordinates preserves uniform measure and Fourier entropy but changes which translations are called coordinate flips; multiplying by a Walsh character can also complement a directional disagreement. A possible way to sharpen any universal comparison is therefore to choose the cheapest affine/character representative before paying influence.

The question attacked here is whether the hard balanced 18-variable Numaro seed, which gives the current recovered lower bound through recursive composition, becomes substantially cheaper in influence after the strongest invertible-linear input normalization plus Walsh-character twisting. The answer is **no, exactly**. Along the way one gets an exact equivalent formulation of universal FEI in terms of a correlation-rank profile.

No novelty or publication-priority claim is made. The repository already contains character folding and a matroid threshold-basis argument in related FEI work; the contribution of this run is the exact orbit normalization, its correlation-rank formulation, and the source-admissible stress test on the current hard seed.

## 2. Exact affine-character normalization

Let `f:F_2^n -> {+1,-1}`. For a translation vector `v`, write

\[
c_f(v)=\mathbb E_x f(x)f(x+v),\qquad
q_f(v)=\Pr_x[f(x)\ne f(x+v)]=\frac{1-c_f(v)}2,
\]

and define

\[
j_f(v)=\min\{q_f(v),1-q_f(v)\}=\frac{1-|c_f(v)|}{2}.
\tag{2.1}
\]

Define

\[
J_{\rm aff}(f)
:=\min_{(v_1,\ldots,v_n)\text{ a basis of }\mathbb F_2^n}
\sum_{i=1}^n j_f(v_i).
\tag{2.2}
\]

### Theorem 2.1 — exact orbit minimum

For

\[
g(x)=\sigma(-1)^{a\cdot x}f(Lx+b),
\qquad L\in GL(n,2),\ a,b\in\mathbb F_2^n,\ \sigma\in\{\pm1\},
\tag{2.3}
\]

one has `H(g)=H(f)`, and

\[
\boxed{\min_{L,a,b,\sigma} I(g)=J_{\rm aff}(f).}
\tag{2.4}
\]

**Proof.** Fourier coefficients of `f(Lx+b)` are obtained from those of `f` by an invertible permutation of frequency labels and signs. Multiplication by `(-1)^{a\cdot x}` translates the frequency labels. Hence squared Fourier coefficients are permuted and `H(g)=H(f)`.

The `i`th coordinate flip of `g` maps under `L` to `v_i=Le_i`. Its disagreement probability is `q_f(v_i)` when `a_i=0` and `1-q_f(v_i)` when `a_i=1`. For a fixed `L`, the bits `a_i` can be chosen independently to make the `i`th influence exactly `j_f(v_i)`. The columns of an invertible `L` are exactly an arbitrary basis of `F_2^n`. Summing proves (2.4). ∎

### Corollary 2.2 — exact universal reformulation

For a fixed constant `C`, universal FEI

\[
H(f)\le C I(f)\quad\text{for every Boolean }f
\]

is equivalent to

\[
\boxed{H(f)\le C J_{\rm aff}(f)\quad\text{for every Boolean }f.}
\tag{2.5}
\]

Universal FEI applied to a minimizing orbit representative gives (2.5); conversely the standard coordinate basis gives `J_aff(f)<=I(f)`. Thus every universal proof is entitled to normalize to the cheapest affine/character representative first.

## 3. Correlation-rank formulation

For `0<=t<=1/2`, let

\[
E_t(f)=\{v\ne0:j_f(v)\le t\},\qquad
r_f(t)=\dim\operatorname{span}E_t(f).
\tag{3.1}
\]

The basis minimization is a minimum-weight-basis problem in the binary vector matroid. Greedy selection simultaneously contains `r_f(t)` vectors of cost at most `t` at every threshold. The layer-cake identity gives

\[
\boxed{J_{\rm aff}(f)=\int_0^{1/2}\bigl(n-r_f(t)\bigr)\,dt.}
\tag{3.2}
\]

Consequently full FEI is equivalently the correlation-rank statement

\[
H(f)\le C\int_0^{1/2}(n-r_f(t))\,dt.
\tag{3.3}
\]

This isolates a concrete universal Booleanity obligation: high spectral entropy must force enough linearly independent translation directions to have non-negligible folded disagreement.

## 4. Exact stress test on the recovered Numaro 18-variable seed

The current FEI handoff records Numaro's published July 2026 balanced monotone 18-variable seed as giving the recovered recursive lower bound `C>6.521845710923046575`. I used the already-recovered exact source representation and accepted it only after matching the published truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

The checker performs an exact integer Walsh transform, exact Walsh autocorrelation for all `2^18` translations, exact folded disagreement counts, and a binary-matroid greedy basis calculation. No floating point is used for the basis optimum.

The ordinary influence is

\[
I(f)=\frac{261}{128}.
\tag{4.1}
\]

The decisive rank profile is: at folded cost `1/256`, the cheap directions span rank `9`; even after admitting every direction of cost at most `9/256`, the span is still rank `9`; at cost `57/256`, the span jumps to rank `18`. An optimal basis therefore has nine directions of cost `1/256` and nine of cost `57/256`, so

\[
\boxed{J_{\rm aff}(f)=9\frac1{256}+9\frac{57}{256}=\frac{261}{128}=I(f).}
\tag{4.2}
\]

Hence **no invertible linear input change, output Walsh-character twist, translation, or global sign can lower the total influence of this seed at all**.

The spectral entropy computed from the exact Walsh integers is `6.776605309005978` bits in binary64 display arithmetic, so the balanced recursive-composition score with the affine-normalized denominator is still

\[
\frac{H(f)}{J_{\rm aff}(f)-1}=6.5218457109230465\ldots,
\tag{4.3}
\]

matching the recovered lower-bound calibration. This large normalization orbit therefore does not yield a stronger lower-bound seed and cannot explain away the hard example as a poor choice of coordinates.

## 5. Boundary checks

For a one-point defect on `n` bits, every nonzero translation has disagreement probability `2^{1-n}`. Hence `r_f(t)` jumps directly from `0` to `n`, and

\[
J_{\rm aff}(f)=n2^{1-n}=I(f).
\]

Affine normalization gives no discount on this rare-event family either.

If a quadratic Boolean phase has spectral law uniform on an affine subspace of dimension `r`, its autocorrelation has absolute value `1` on an `(n-r)`-dimensional translation subspace and is zero outside it. Therefore `j_f=0` on rank `n-r` and `j_f=1/2` on every direction required to complete a basis. Thus

\[
J_{\rm aff}(f)=\frac r2,\qquad H(f)=r=2J_{\rm aff}(f).
\tag{5.1}
\]

This is consistent with the preceding B17 code-phase family: affine normalization sees its global code structure, but that family itself has constant `2` and is not FEI-hard.

## 6. Failed route and residual obligation

The attempted mechanism was to improve the hard FEI ratio by searching the full affine-input/character-output orbit before composition. The Numaro seed is an exact obstruction: its orbit minimum equals its original influence. This eliminates an exponentially large transformation class at once rather than merely rechecking the original coordinates.

The surviving universal target is (3.3). A continuation must prove a genuinely Boolean correlation-rank inequality or go outside affine/character gauge changes, for example to nonlinear phase transformations whose entropy cost and influence gain can both be controlled. Arbitrary subset laws do not obey the needed constraint, so any proof must use Boolean phase/autocorrelation identities rather than marginal entropy alone.

**Full FEI remains OPEN.** This report proves the orbit identity and the exact source-admissible rank-rigidity calculation only; it does not claim a new universal constant or publication priority.
