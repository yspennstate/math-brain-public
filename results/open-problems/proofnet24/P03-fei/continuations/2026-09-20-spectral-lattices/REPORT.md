# Lattice-valued Fourier components and unequal spectral weights

20 September 2026. Research continuation for Yitzchak Shmalo.

**Full FEI remains unproved in this work.** This report extends the preceding polynomial-support centroid argument from a single flat Boolean spectrum to arbitrarily many unequal Fourier magnitudes, under an explicit physical-value lattice condition on their projections. It proves a coefficient `4+2s`, a sharp constant-four integral case, a dependent-branch composition rule, and explicit obstructions to dropping the lattice hypothesis. Independent expert review, proof-assistant formalization and publication-priority clearance are not claimed.

## 1. Statement of the positive extension

For a Boolean sign function on the uniform cube, write

\[
f(x)=\sum_S\widehat f(S)\chi_S(x),\qquad
H(f)=\sum_S\widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\qquad
I(f)=\sum_S|S|\widehat f(S)^2.
\]

For each distinct positive magnitude `a` occurring among the Fourier coefficients, define its magnitude component

\[
A_a=\{S:|\widehat f(S)|=a\},\qquad
f_a(x)=\sum_{S\in A_a}\widehat f(S)\chi_S(x).
\tag{1}
\]

These functions are real-valued spectral projections; they need not themselves be Boolean or integer-valued. Their Fourier supports are disjoint and `f=sum_a f_a`.

**Theorem 1 (bounded lattice denominators).** Suppose that, for an integer `s>=0`, every component in (1) takes values in `2^{-s} Z` at every input. Then

\[
\boxed{H(f)\le(4+2s)\,\mathfrak I(f)\le(4+2s)J(f)\le(4+2s)I(f).}
\tag{2}
\]

Here `J=sum_i min(Inf_i,1-Inf_i)` and `Ifrak` is the minimum total influence over invertible affine input changes and multiplication by an output character. In particular:

- integer-valued magnitude components give constant **4**, with no bound on their number;
- half-integer-valued components give constant **6**;
- a grid with denominator `2^s` costs only `2s` beyond four.

There is no bound on dimension, number of coefficient magnitudes, algebraic degree, or number of distinct coefficient valuations. The value of `s`, however, is a real hypothesis and can grow without bound. Equation (2) is not unrestricted FEI.

The integer-component class contains the previously proved plateaued class but also functions with several different Fourier magnitudes. Constant four is optimal over the integer-component class in the limit, because it includes the standard addressing functions, whose ratios tend to four. No optimality of six or of `4+2s` for `s>0` is asserted.

## 2. Integer-valued flat packets and the centroid theorem

We first extend the earlier bottom-digit argument to integer-valued functions. For a real function `g` use the homogeneous entropy and Dirichlet energy

\[
\mathcal H(g)=\sum_S\widehat g(S)^2\log_2\frac1{\widehat g(S)^2},\qquad
\mathcal I(g)=\sum_S|S|\widehat g(S)^2.
\]

The squared norm is not assumed to be one. These are homogeneous spectral expressions, not the entropy of a normalized probability law unless the norm equals one.

**Lemma 2.1.** Let `h` be integer-valued, with Fourier coefficients equal to `0` or `+/-2^{-r}`, where `0<=r<=n`. If `A` is its Fourier support, then

\[
\deg_{\mathbb F_2}1_A\le n-r,
\qquad
\frac1{|A|}\sum_{S\in A}|S+b|\ge\frac r2
\quad\text{for every }b.
\tag{3}
\]

**Proof.** The integer Walsh transform `W_h(S)=2^n hhat(S)` has values `0,+/-2^{n-r}`. As an integer multilinear polynomial in the frequency bits,

\[
W_h(S)=\sum_x h(x)\prod_{i:x_i=1}(1-2S_i).
\]

Its coefficient at monomial `U` is divisible by `2^{|U|}`. Moreover every coefficient is divisible by `2^{n-r}`, since the coefficients are integer linear combinations of the values `W_h(S)`. Divide by `2^{n-r}` and reduce modulo two. Every monomial of degree greater than `n-r` vanishes. The resulting binary function is exactly `1_A`, since either sign reduces to one. Apply the preceding report's centroid theorem to this support polynomial. This proves (3). Unlike the Boolean `+/-1` case, no extra parity factor is available here; the threshold is `r/2`, not `(r+1)/2`. QED.

The needed centroid theorem is supplied with a proof in `2026-09-20-centroid-and-carries/REPORT.md`. Its mechanism is recalled to make the dependency explicit. For a binary support polynomial of degree `d`, the evaluation spaces on its support of degrees at most `u` and `v` are orthogonal over `F_2` when `u+v<n-d`. Their dimensions sum to at most the support size. Each dimension is at least the number of support points of Hamming weight at most its threshold, by the triangular monomial-inclusion evaluation matrix. A reversed pair of sorted distances with sum less than `n-d` would contradict the dimension bound. Summing the pair inequalities gives the centroid. Translations do not increase degree.

A useful consequence is that any nonzero **ternary** function `g` with flat nonzero Fourier magnitude satisfies

\[
\boxed{\mathcal H(g)\le4\mathcal I(g).}
\tag{4}
\]

Indeed its magnitude must be `2^{-k}`: Fourier inversion at a point where `g=+/-1` makes the reciprocal magnitude an integer, and Walsh rationality makes it a power of two. Apply (3) with `r=k`. The total spectral mass `p=E g^2` can be arbitrary; then `Hcal(g)=2kp` and `Ical(g)>=kp/2`. Character multiplication gives the corresponding centered-energy inequality. No affine physical-support hypothesis is used.

## 3. An exact arithmetic decomposition for every Boolean function

For a magnitude `a`, let

\[
\epsilon_a(S)=\begin{cases}\operatorname{sgn}\widehat f(S),&S\in A_a,\\0,&S\notin A_a,\end{cases}
\qquad
V_a(x)=\sum_S\epsilon_a(S)\chi_S(x).
\]

`V_a` is an integer-valued unnormalized Walsh transform. Define

\[
r_a=\min_{x:V_a(x)\ne0}\nu_2(V_a(x)),\qquad
b_a=a2^{r_a},\qquad p_a=|A_a|a^2=\mathbb E f_a^2.
\tag{5}
\]

Here `r_a` is a divisibility order, not a vector-space rank. It lies between zero and `n`. The function `h_a=2^{-r_a}V_a=f_a/b_a` is integer-valued, has some odd value, and has flat Fourier magnitude `2^{-r_a}`.

### 3.1 Boolean projections cannot have lattice spacing greater than one

For every nonempty magnitude component,

\[
\boxed{0<b_a\le1.}
\tag{6}
\]

Since `f_a` is a spectral projection of `f`, Parseval gives `E f f_a=E f_a^2=p_a`. Its values are multiples of `b_a`, so pointwise `f_a^2>=b_a|f_a|`. Hence

\[
p_a=\mathbb E f f_a\le\mathbb E|f_a|\le p_a/b_a.
\]

This proves (6). It is an exact use of Boolean boundedness; there is no replacement by approximate Booleanity.

### 3.2 The weighted centroid contribution and its unpaid remainder

Lemma 2.1 gives, for every character center,

\[
\mathcal I(\chi_b f_a)\ge\frac12p_a r_a.
\]

Summing disjoint spectral supports and then minimizing over characters gives the same lower bound for `J(f)`. Invertible affine transformations preserve `a,p_a,r_a,b_a`: the sign-mask Walsh values are merely permuted and multiplied by signs. Therefore

\[
\boxed{\mathfrak I(f)\ge\frac12\sum_a p_a r_a.}
\tag{7}
\]

Define the nonnegative arithmetic remainder

\[
\mathcal D(f)=\sum_a p_a\log_2(1/b_a).
\tag{8}
\]

Because `a=2^{-r_a}b_a`, there is an **exact** identity

\[
\boxed{H(f)=2\sum_a p_a r_a+2\mathcal D(f).}
\tag{9}
\]

Combining (7) and (9),

\[
\boxed{H(f)\le4\mathfrak I(f)+2\mathcal D(f).}
\tag{10}
\]

Equation (10) is universal but has an unpaid remainder. It is not a new universal FEI constant. In fact `0<=D<=H/2`; finiteness of a uniform `D/I` bound is equivalent up to constants to FEI, by (10) and this last inequality. Merely introducing `D` is not counted as progress toward its universal bound. The new positive step below is a proved, dimension-free payment on a larger class with unequal masses.

## 4. Integral projections form a signed physical partition

The following three conditions are equivalent:

1. Every magnitude component `f_a` is integer-valued.
2. Every `b_a` equals one.
3. At each physical input exactly one magnitude component equals `f(x)` and all others are zero.

For `1 => 2`, write the dyadic amplitude as `a=q2^{-k}` with `q` odd. Since `h_a` has an odd value, integrality implies `r_a>=k`. Thus `b_a=q2^{r_a-k}` is a positive integer. Equation (6) forces `b_a=1`. For `2 => 1` use `f_a=b_a h_a`.

For `1 => 3`, at each input the integer vector `(f_a(x))_a` sums to `+/-1`, so its squared norm is at least one. Orthogonality gives

\[
\mathbb E\sum_a f_a(x)^2=\sum_a p_a=1.
\]

Thus the pointwise squared norm equals one everywhere, proving condition 3. The converse is immediate.

These facts explain why the integral case can have many different Fourier weights without an interference penalty. Each component is a ternary flat packet, their spectra are disjoint, and their physical supports partition the cube. Equations (8)--(10) prove constant four. The standard addressing function on `k` address bits and `2^k` data bits is plateaued, hence lies in this class, and has `H/I=4k/(k+2) -> 4`.

This is not a representation theorem for arbitrary Boolean functions. Section 7 gives a small exact obstruction even when all Fourier magnitudes are powers of two.

## 5. Proof of the coefficient `4+2s`

Assume all magnitude components take values in `2^{-s} Z`. Since `h_a` has an odd value and `b_a` is dyadic, the lattice assumption implies `b_a` is a positive multiple of `2^{-s}`. Together with (6),

\[
2^{-s}\le b_a\le1,\qquad \mathcal D(f)\le s.
\tag{11}
\]

Thus (10) alone gives `H<=4I+2s`. The key point is to turn this additive error into `2s I`, including the regime `I<1`.

### 5.1 Two elementary inequalities

For a Boolean function with smaller sign-class density `delta`, edge isoperimetry gives

\[
I(f)\ge2\delta\log_2(1/\delta).
\tag{12}
\]

A short induction uses two slice densities `a<=b`, within-slice bounds and at least `b-a` crossing disagreement. Setting `t=a/(a+b)`, the remaining inequality is `h_2(t)>=2t` on `[0,1/2]`, which follows from concavity. This proves the needed normalization of (12).

For distinct Fourier labels `S,T`, Boolean boundedness gives

\[
|\widehat f(S)|+|\widehat f(T)|\le1.
\tag{13}
\]

Choose signs to make the two expectations positive and bound their sum by `E|+/-chi_S +/-chi_T|=1`. Thus a Fourier coefficient with magnitude greater than one half is unique at that magnitude.

We also need the scalar inequality, valid for `0<=delta<=1/4` and `p=(1-2delta)^2`,

\[
\boxed{-p\log_2p+2(1-p)\le4\delta\log_2(1/\delta).}
\tag{14}
\]

For a proof put `t=2delta`. Multiplying the right-minus-left difference by `ln(2)/2` gives

\[
G(t)=-t\ln t-t(1-t)\ln2+(1-t)^2\ln(1-t).
\]

It vanishes at `0` and `1/2`. On `(0,1/2)`,

\[
G''(t)=-1/t+2\ln2+2\ln(1-t)+3,
\qquad G'''(t)=1/t^2-2/(1-t)>0.
\]

Hence `G''` increases from negative infinity to one and has one zero. Also `G'(0+)=+infinity` and `G'(1/2)=2 ln2-3/2<0`. Therefore `G'` changes sign exactly once, from positive to negative: before the zero of `G''` it decreases, and afterwards it increases but remains negative at its final endpoint. Thus `G` first increases and then decreases between its zero endpoints, so `G>=0`. This proves (14).

### 5.2 Moderate bias

If `|E f|<=1/2`, then `delta` lies in `[1/4,1/2]`. The concave function `2delta log_2(1/delta)` is at least one on this interval, since both endpoint values equal one. Consequently `I>=1`. Equation (10) and (11) give

\[
H(f)\le4I(f)+2s\le(4+2s)I(f).
\]

### 5.3 Large bias

Suppose `m=|E f|>1/2`. By (13), the magnitude component of the empty Fourier label is the single constant `+/-m`. Put `p=m^2` and `delta=(1-m)/2<1/4`. The other components have total mass `1-p`, and their energies sum to `I(f)`. Applying the packet bound to them gives

\[
H(f)\le4I(f)-p\log_2p+2s(1-p).
\]

For `s>=1`, nonnegativity of `-p log_2 p` and (14) imply

\[
-p\log_2p+2s(1-p)
\le s[-p\log_2p+2(1-p)]
\le4s\delta\log_2(1/\delta)
\le2sI(f).
\]

This proves (2) with `I`. For `s=0`, the integral case was already proved directly. The lattice condition is preserved by invertible affine input changes and output characters, so apply the same result after each change and take the minimum. This proves Theorem 1 in full.

The large-bias argument requires the lattice condition only on the nonconstant magnitude components, not on the isolated constant. It does not assert that an arbitrary selected Fourier coefficient can be discarded without checking the other components.

### 5.4 Independent cores and surjective affine mixing

The inherited affine-minimum identities are

\[
\mathfrak I(\prod_t f_t)=\sum_t\mathfrak I(f_t),\qquad
\mathfrak I(f\circ L)=\mathfrak I(f)
\]

for disjoint logical inputs in the product and a jointly surjective affine input map `L` in the lift. Entropy has the same additivity/invariance. Therefore independent factors with lattice exponents `s_t<=s`, followed by any jointly surjective affine mixing and output character, satisfy the single constant `4+2s`. There is no factor-count penalty, even when the merged magnitude components acquire finer denominators.

For completeness the minimum-basis identity is `Ifrak(f)=integral_0^{1/2}(n-dim span{v:j_f(v)<=t}) dt`. Product autocorrelations multiply, so a product direction's folded cost is at least each factor cost; embedded single-factor directions preserve the cost. Thus the cheap-direction spans form a direct sum, proving tensorization. A surjective lift replaces the span by its inverse image and adds only the kernel dimension. These are the preceding affine-variance report's proofs, not newly claimed results. Joint surjectivity and logical independence must not be dropped.

## 6. Nonaffine flat cells and dependent branches

### 6.1 Flat-cell tagging without an affine-cell assumption

Let `A_l` partition a physical data cube, and let `g_l` be a ternary function supported on `A_l` with absolute value one there. Suppose every `g_l` has flat nonzero Fourier magnitude. For distinct tag characters `chi_{b_l}(z)`, set

\[
F(x,z)=\sum_l g_l(x)\chi_{b_l}(z).
\tag{15}
\]

The function is Boolean. The summands are integer-valued flat packets on disjoint joint Fourier supports, because their tag labels are distinct. Merging summands with the same magnitude preserves integrality. Theorem 1 with `s=0` gives

\[
\boxed{H(F)\le4\mathfrak I(F).}
\tag{16}
\]

The cells need not be affine; their signed indicator spectra must be flat. Tags in (15) are actual coordinates of the function being proved. Appending tags to an arbitrary unknown function and then fixing them is not an inverse transfer theorem.

Here is an explicit unequal-magnitude, nonaffine-cell example. On four data bits take the bent quadratic phases

    h1=(-1)^(x1*x2+x3*x4),   h2=(-1)^(x1*x3+x2*x4).

With two more sign variables `T,S`, set `h=(h1+T h2)/2`, `h'=(h1-T h2)/2`, and

    g1=h(1+S)/2,   g2=h(1-S)/2,   g3=h'.

Their supports partition the six-variable data cube. The graph defining the support of `h` has quadratic, nonaffine equation, and the three cells are nonaffine. Their flat magnitudes are `1/16,1/16,1/8`. Use three distinct single-bit tags in (15). The resulting nine-variable Boolean function has 128 coefficients of magnitude `1/16` and 32 of magnitude `1/8`, so `H=7`. The exact checker gives `I=15/4` and `Ifrak=13/4`. These finite values illustrate the general theorem, not a claim of separation from every alternative earlier representation.

### 6.2 Shared-variable branch replacement

Suppose integer-valued flat selectors `g_l(x)` form a signed physical partition and have disjoint Fourier supports. Let `h_l(y)` be arbitrary Boolean branches on the **same** residual variables `y`. Set `F=sum_l g_l(x)h_l(y)` and `p_l=E g_l^2`. Then

\[
\boxed{H(F)=\sum_l\mathcal H(g_l)+\sum_l p_lH(h_l),}
\]
\[
\boxed{I(F)=\sum_l\mathcal I(g_l)+\sum_l p_lI(h_l).}
\tag{17}
\]

The joint Fourier supports are disjoint in the selector frequency, and coefficients multiply within each block. Direct expansion proves both identities; no independence between different branches is used. If every branch satisfies `H(h_l)<=C J(h_l)`, equations (4) and (17), followed by character normalization of selector and branch coordinates, give

\[
\boxed{H(F)\le\max\{4,C\}J(F).}
\tag{18}
\]

The selector variables and residual variables must be disjoint. The different branches may reuse the entire residual variable set. Arbitrary affine mixing between selector and branch coordinates is not asserted to preserve (18); the stronger affine conclusion (16) applies when all the resulting packets are flat and integral. Spectral disjointness is essential and is not replaced by ordinary orthogonality of the selectors alone.

## 7. Obstructions to a universal closure

### 7.1 Powers of two do not force integral magnitude components

On five binary variables define

\[
f_*(x_1,x_2,x_3,y_1,y_2)
=1-2\mathbf1_{\{y_1=x_1x_2,\ y_2=x_1x_3\}}.
\tag{19}
\]

Its negative density is `1/4`. The Fourier expansion of the graph indicator gives one coefficient `1/2` at the empty label and twelve coefficients of magnitude `1/4`, all other coefficients being zero. To see the twelve, each nonzero tag combination is a nonzero quadratic `x1(v1*x2+v2*x3)` on three bits, whose Walsh spectrum has four coefficients of magnitude `1/2`. Multiplication by the graph-indicator scale gives magnitude `1/4` for the Boolean function.

The two magnitude components are

    f_(1/2)=1/2,
    f_(1/4)=f_*-1/2,  taking values 1/2 and -3/2.

They are not integer-valued, but are half-integer-valued. Thus (19) refutes the tempting implication from power-of-two amplitudes to integral components. It is covered by the new constant-six theorem, not a counterexample to FEI. Exact values are

\[
H(f_*)=7/2,\qquad I(f_*)=15/8,\qquad H/I=28/15.
\]

The physical influences are `3/8,1/4,1/4,1/2,1/2`, giving the stated total. The signed-mask divisibility orders are zero for the `1/2` band and one for the `1/4` band, and both have mesh `1/2`.

All power-of-two spectra in dimensions at most four did have integral components in the exhaustive checks. The five-variable example shows why those complete small-dimensional checks did not justify a universal theorem.

### 7.2 No fixed lattice denominator covers all power-of-two spectra

For `t` independent copies, `f_*^{tensor t}` still has only power-of-two Fourier magnitudes. Its smallest-magnitude component is

\[
(f_*-1/2)^{\otimes t},
\]

whose values have exact dyadic denominator `2^t`: every value is an odd integer times `2^{-t}`. All other components also lie on that grid, by product expansion. Hence the smallest common lattice exponent is exactly `t`. Yet

\[
H(f_*^{\otimes t})=7t/2,\qquad I(f_*^{\otimes t})=15t/8.
\]

The ratio remains `28/15`. This disproves a fixed-denominator representation claim, not FEI. The independent-core closure in Section 5.4 keeps coefficient six on this family without using the growing merged denominator.

### 7.3 The exact remaining universal obligation

The universal remainder `D(f)` in (8) is not bounded by this report by any constant multiple of `I`. Bounded denominators pay it on the stated class, but a general Boolean function may have arbitrarily fine lattices without an available independent-core decomposition. The positive classes here are additional stopping certificates, not a universal representation.

The original erasure target remains a finite universal bound on `sum_i H(S_i | S_-i)/I(f)`. A uniform arithmetic-remainder bound would also imply FEI through (10), but reformulating that obligation is not a proof. The previous carry obstruction is not removed: no linear degree bound for higher Walsh digits is assumed. No result here revives absolute-overlap selection, raw shared-control decrement subadditivity, a fixed-coefficient affine-drift estimate, or the false pointwise erasure converse.

## 8. Actual verification and exploratory records

Run `python verify_spectral_packets.py` with Python 3.10+ and NumPy. Its mathematical assertions use integer Walsh transforms and rational inequalities. Entropy comparisons use outward rational logarithm intervals from a 48-term atanh series after range reduction; no floating-point tolerance certifies a sign.

Executed checks:

- Every one of 65,812 Boolean functions in dimensions 1--4, with 147,348 nonempty magnitude components. Checks include the lattice gap, mask-degree bound, all-center centroid consequence via the minimum-centered energy, exact reconstruction, grid exponent and theorem inequality. There are 23 cached distinct entropy-bound certificates. Of these functions, 29,076 have integral components, including 26,880 with more than one Fourier magnitude. The half-integer class has no additional examples in those dimensions.
- All 6,651 ternary truth tables in dimensions 1--3 were examined; 536 nonzero flat functions satisfy the homogeneous centroid/entropy statements.
- The actual five-variable counterexample; actual tensor-power truth tables on 5, 10 and 15 variables; the nine-variable nonaffine-cell construction.
- Sixteen invertible affine/character images of the five- and nine-variable examples, including exact greedy minimum-basis influence checks.
- Twenty-four branch pairs sharing the same three residual variables, verifying the exact spectral mixture and energy identities in dimension six.
- A 257-point rational check of the biased-head scalar inequality, with exact endpoint equalities.

These finite families overlap and are not exhaustive unrestricted Boolean coverage at dimensions five through fifteen. The checker was copied into a separate directory and rerun. Its output was byte-identical. This is reproducibility, not an independent audit or a proof-assistant formalization.

The exploratory folder preserves the initial level-degree enumeration, the test of integral components in small dimensions, and the direct five-variable witness computation. Their floating-point entropy displays are exploratory only; the final checker verifies the relevant statements exactly. A failed hypothesis is not silently used as a lemma.

## 9. Sources and provenance

Actually consumed repository sources, on `yspennstate/math-open-problems`, branch `master`:

- Current FEI entrypoint, blob `74f4ab003c44ef18e19e0d91adacd93aeb27ab20`, including the centroid update and remaining mass-weighted gap. Its earlier later sections were not all independently re-audited.
- `continuations/2026-09-20-centroid-and-carries/REPORT.md`, blob `87923382aa41f3fd4cf355750679846d8e45e35d`: the support-pairing proof, bottom-digit argument, plateaued result and higher-digit obstruction. The uniform-spectrum conclusion is retained with its stronger finite-k coefficient; this report does not relabel it as new.
- `continuations/2026-09-19-affine-variance/REPORT.md`, blob `2fa7fb2f510b10ceedc53fd560b87defa904c6dc`, Sections 3.1--3.4: minimum-basis formula, exact tensorization and surjective lifting, with their stated hypotheses. Those identities are reused, not claimed new.
- The mounted previous centroid/Booleanity ZIP was extracted for local computational context. No earlier checker was replayed as part of this continuation; only the new checker was executed and replayed.

Primary literature checked on 20 September 2026: Gonzalez--MacManus--Pereyra, *Further evidence towards the Fourier Entropy-Influence conjecture*, arXiv:2606.00246v2, revised 9 June 2026; O'Donnell--Tan, *A composition theorem for the Fourier Entropy-Influence conjecture*, arXiv:1304.1347; Cao--Hu, *Two Boolean functions with five-valued Walsh spectra and high nonlinearity*, arXiv:1406.4567. Their abstract pages establish context and the existence of earlier composition and multi-valued-spectrum literature. They are not used as uninspected proof premises for the new theorems. In particular, the O'Donnell--Tan composition statement assumes disjoint inner inputs, whereas Section 6.2 has a different, explicitly spectrally separated selector hypothesis. No claim of superiority or independent novelty follows from that distinction.

The mathematical additions to this project are the integer-flat-packet extension, the projection lattice-gap argument, the exact arithmetic decomposition, its complete bounded-denominator payment including large bias, the corresponding unequal-weight classes and nonaffine/shared-branch constructions, and the explicit failures of automatic/fixed-denominator closure. Publication priority remains unverified. Full FEI remains unproved. No schedule, ownership, visibility or native atlas metric is changed by this report.
