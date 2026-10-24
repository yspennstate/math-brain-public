# Additional full-scope exploration and limits

20 September 2026. This file separates the proved reports from exploratory candidates. Nothing here supplies the missing universal FEI estimate.

## 1. Direct restriction and endpoint searches

The conversation workspace contains `probe.py` and `endpoint_probe.py` with actual output JSON files. They sampled random truth tables, rare sets, threshold examples and polynomial phases. Their Fourier entropies and noninteger endpoint powers use floating point. They are exploratory searches, not certificates or upper bounds over all functions.

The initial finite endpoint search did not find an every-coordinate ratio above four. The analytical construction in `ENDPOINT_QUANTIFIERS.md` nevertheless disproves every fixed coefficient for that stronger quantifier. This is why the sample maxima are not used in either proof report. The existential endpoint selector remains unresolved.

## 2. A dyadic support observation with a proof

Let \(W(S)=2^n\widehat f(S)\) for a non-affine Boolean sign function. Let \(r\) be the minimum 2-adic valuation among the nonzero integers \(W(S)\). Then \(1\le r<n\). Define

\[
R(S)=(W(S)/2^r)\bmod2.
\]

**Observation.** \(R\) is a nonzero polynomial over \(\mathbb F_2\) of degree at most \(r-1\).

Indeed, as an integer-valued multilinear polynomial in the bits of \(S\),

\[
W(S)=\sum_x f(x)\prod_{i:x_i=1}(1-2S_i).
\]

The coefficient at monomial \(T\) is \((-2)^{|T|}\sum_{x:x_T=1}f(x)\). If \(|T|<n\), the inner sum is even, so that coefficient is divisible by \(2^{|T|+1}\). For \(|T|=n\), it is divisible by \(2^n\). Also every integer multilinear coefficient is a signed sum of function values, so global divisibility of \(W\) by \(2^r\) implies divisibility of every coefficient by \(2^r\). After division and reduction modulo two, every monomial of degree at least \(r\) vanishes, proving the observation. If \(r=n\), Parseval would allow just one nonzero Walsh coefficient and \(f\) would be affine, the excluded case.

The standard minimum-weight induction for a nonzero degree-\(d\) binary polynomial gives at least \(2^{n-d}\) nonzero values. Hence the lowest-valuation layer contains at least \(2^{n-r+1}\) frequencies. The observation is a possible input to a multiscale argument, not a spectral-entropy bound. Its independent publication novelty has not been checked.

## 3. An unproved centroid candidate and what its finite tests mean

I considered the statement

\[
\sum_{x:P(x)=1}|x|\ \ge\ \frac{n-d}{2}\,|\{x:P(x)=1\}|
\tag{C}
\]

for every nonzero binary polynomial of degree at most \(d\). **No all-dimensional proof or counterexample to (C) was obtained. It is not a lemma available for use.**

The accompanying C++20 program `centroid_probe.cpp` enumerates all coefficient vectors in three Reed–Muller families by a Gray-code traversal. It uses exact bit masks and popcounts. Its actual output is:

```
5 2 cases 65536 max_violation 0 witness 0
6 2 cases 4194304 max_violation 0 witness 0
5 3 cases 67108864 max_violation 0 witness 0
```

The sum is 71,368,704 parameter cases across overlapping families, not that many distinct unrestricted Boolean functions. The degree-two five-variable family is contained in the degree-three five-variable family. A zero maximum includes the zero polynomial, checked directly, and equality examples. These data are finite checks only. Separate seeded polynomial samples through dimension eight also found no counterexample; they do not establish (C).

Even proving (C) would not finish the attempted FEI route. Applied just to the lowest-valuation layer, it would yield

\[
I(f)\ge(n-r+1)2^{r-n}.
\]

That conclusion is already available without (C): the smaller physical sign class has density at least \(2^{r-1-n}\), because its cardinality is a positive multiple of \(2^{r-1}\). Cube edge isoperimetry \(I\ge2\delta\log_2(1/\delta)\), minimized over \(\delta\in[2^{r-1-n},1/2]\), gives the same bound. Thus this first-layer inference is not counted as a new universal advance.

An actual full-scope improvement along this route would need a quantitative statement about higher amplitude digits or weighted layers that survives the carry terms and charges entropy, not merely minimum denominator. No such statement was proved. The affine-symmetric theorem and endpoint obstruction do not depend on (C), on these exploratory searches, or on the dyadic observation.

## 4. Current continuation obligation

The new proved stopping class handles surjective affine images of independent symmetric factors. Allowing arbitrary dependent logical forms would already encode every Boolean function by repeated input bits; REPORT.md proves this explicitly. The new endpoint obstruction rules out paying a prescribed coordinate uniformly, not choosing one appropriately. The full problem still requires either the correctly quantified universal erasure estimate, a paid existential selector, or another complete influence-controlled decomposition. None is assumed from finite searches or a small set of cases.
