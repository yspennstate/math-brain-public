# Biased realizability audit

## 1. Exact interior characterization

Fix `n>=0` and an interior product law on `X_i in {0,1}` with
`P(X_i=1)=p_i in (0,1)`.  Put

\[
 \phi_i(x_i)=\frac{x_i-p_i}{\sqrt{p_i(1-p_i)}},\qquad
 \phi_S=\prod_{i\in S}\phi_i,
\]

and let `a_S` be real.  Define

\[
 g_a(x)=\sum_S a_S\phi_S(x),\qquad
 \kappa_i=\frac{1-2p_i}{\sqrt{p_i(1-p_i)}}.
\]

Since `phi_i^2=1+kappa_i phi_i`, the product rule is

\[
 \phi_S\phi_T=
 \sum_{R\subseteq S\cap T}
 \left(\prod_{i\in R}\kappa_i\right)
 \phi_{S\triangle T\cup R}.                                      \tag{1}
\]

Consequently `a` is the normalized product-Fourier coefficient vector of
an actual Boolean sign on every positive-mass input if and only if

\[
 \sum_{S,T}a_Sa_T
 \sum_{\substack{R\subseteq S\cap T\\S\triangle T\cup R=U}}
 \prod_{i\in R}\kappa_i
 =\mathbf1_{U=\varnothing}                                      \tag{2}
\]

for every `U subseteq [n]`.  Necessity follows by expanding `g_a^2=1`.
For sufficiency, (2) says the complete Fourier expansion of `g_a^2-1`
vanishes, hence `g_a(x)^2=1` on every atom; thus `g_a` is Boolean.  The
`U=empty` equation is Parseval, `sum_S a_S^2=1`; Parseval alone is not
sufficient.

Equivalently, put `u_S(x)=prod_{i in S}(x_i-p_i)` and write
`a_S=b_S sqrt(prod_{i in S}p_i(1-p_i))`.  Then

\[
 (x_i-p_i)^2=p_i(1-p_i)+(1-2p_i)(x_i-p_i),                       \tag{3}
\]

so (2) becomes a rational system whenever every `p_i` and `b_S` is
rational.  For an actual sign `g`,

\[
 b_S=\mathbb E_{X_{-S}}\Delta_Sg,
 \qquad
 \widehat g_p(S)^2=b_S^2\prod_{i\in S}p_i(1-p_i),                \tag{4}
\]

and the inverse formula is

\[
 g(x)=\sum_Sb_S\prod_{i\in S}(x_i-p_i).                          \tag{5}
\]

Equations (2), (4), and (5) provide an exact certificate: truth table,
normalization, signs, and inverse Booleanity are all retained.

## 2. Squared masses alone are insufficient

At `n=1`, `p=1/4`, consider the proposed normalized spectral law

\[
 a_\varnothing^2=a_{\{1\}}^2=\frac12.
\]

Here `kappa=2/sqrt(3)`.  For either possible relative sign, the nonconstant
coefficient of `g_a^2` is

\[
 2a_\varnothing a_{\{1\}}+\kappa a_{\{1\}}^2
 =\pm1+\frac1{\sqrt3}\ne0.
\]

Thus this nonnegative, normalized law is not the squared biased Fourier
law of any Boolean gate.  A realizability check must retain compatible
coefficient signs and all equations (2), not just masses and Parseval.

## 3. Exact finite-cube bias domain

A Boolean sign on `m` uniform bits has

\[
 P(g=1)=k/2^m
\]

for an integer `k`.  Conversely every dyadic `k/2^m` is realized by a
truth table with exactly `k` positive atoms.  Hence finite uniform Boolean
encoders realize exactly the dyadic probabilities.  Every finite vector of
dyadic biases can be realized simultaneously by using disjoint encoder
blocks.

Therefore the gate-potential equivalence in `biased.tex` is correctly
quantified on dyadic biases.  It already suffices for ordinary FEI because
the sufficiency direction applies the gate inequality at the uniform bias
`1/2`; the converse uses actual finite uniform child encoders.  An infimum
over finite encoders does not define the potential at a nondyadic bias.

For a fixed finite gate, the analytic Fourier quantities do have a closure.
From (4), each coefficient is continuous on the interior and extends under
coordinate contraction: coefficients containing a deterministic coordinate
vanish, and the others converge to the coefficient of the contracted gate.
Thus ordinary entropy, influence, corrected entropy, and deficit extend
continuously (with `0 log(1/0)=0`).  It follows that a gate inequality proved
on all interior dyadic biases extends to all real interior biases **only if**
every additional potential term has a specified continuous extension and
the constant is uniform.  This is a transfer hypothesis, not a consequence
of the dyadic infimum definition.

## 4. Boundary, reuse, and conditioning audit

- If `p_i` is zero or one, delete coordinate `i` and evaluate the gate on
  the unique positive-mass slice.  Off-support truth-table values and a
  normalized `phi_i` are not identifiable.  Forming `phi_i` first would
  divide by zero.
- Reusing the same physical child in two outer slots destroys the product
  law unless that child is deterministic.  For `G(y_1,y_2)=y_1y_2` and a
  balanced sign `h`, reuse gives `G(h,h)=1`, whereas disjoint fresh copies
  give the balanced parity `h_1h_2`.  The disjoint composition identities
  cannot be applied to the reused expression.
- Physical restriction is not spectral conditioning.  For a uniform
  dictator, conditioning the spectral set on containing its coordinate
  leaves the singleton spectral set, while physically fixing the input
  produces a constant child supported at the empty spectral set.

## 5. Weighted controls replayed at exact scope

The A042 controls remain compatible with this audit:

1. `alpha TC(Q)/I ~ (ln m+1)/8` refutes the event conditional-input-TC
   payment, not corrected FEI+ and not Boolean realizability.
2. The pivotal residual `~ (1/2)ln m-ln 2` refutes the coefficient-one
   proposal only; larger multipliers are not covered.
3. The fixed-`m`, `q->0`, then `m->infinity` every-coordinate obstruction
   concerns physical conditional-input mutual information.  It does not
   refute existential spectral-coordinate selection.

The weighted family is an actual Boolean threshold at every interior
parameter.  Its endpoint ratios are formed only after contracting
deterministic coordinates; raw `0/0` ratios are not endpoint theorems.

## Status

The characterization and domain audit are **AUTHOR_PROVED_PENDING_REVIEW**.
They resolve A045's requested normalization/scope audit but do not prove the
biased gate inequality, a weighted-threshold FEI+ theorem, or full FEI.
