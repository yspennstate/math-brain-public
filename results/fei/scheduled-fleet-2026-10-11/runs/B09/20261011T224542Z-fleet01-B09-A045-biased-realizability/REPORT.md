# B09 / A045 — exact biased-Boolean realizability and finite-cube domain

**Run ID:** `20261011T224542Z-fleet01-B09-A045-biased-realizability`  
**Primary packet:** A045 (Biased realizability referee)  
**Attempt:** `A045-attempt-01-inverse-domain-audit`  
**Mathematical status:** `AUTHOR_PROVED_PENDING_REVIEW`  
**Full FEI:** **OPEN**

## 1. Frozen target and prior status

The source gate-potential proposition is quantified over dyadic biases, but
the surrounding biased Fourier formalism also permits arbitrary real product
biases.  A045 asks whether a proposed spectral law is actually the normalized
biased Fourier law of a Boolean gate, and requires deterministic inputs,
repeated physical variables, and physical-versus-spectral conditioning to be
handled explicitly.

**Prior status:** the dyadic gate-potential statement and the weighted controls
were source-proved, but A045 had no inverse-transform/Booleanity audit and no
exact statement of when dyadic results extend to all real biases.

**Bounded objective:** derive a necessary-and-sufficient Booleanity certificate
for one fixed interior product bias; determine the exact finite-uniform
realizability domain; give concrete failure witnesses for squared-mass-only,
repeated-variable, and conditioning substitutions.  The bounded checker covers
all 768 three-bit gate/bias pairs from three frozen rational bias vectors.

## 2. PROVED: complete inverse product-Fourier certificate

For independent `X_i in {0,1}` with `P(X_i=1)=p_i in (0,1)`, let

\[
 \phi_i=(X_i-p_i)/\sqrt{p_i(1-p_i)},\qquad
 \kappa_i=(1-2p_i)/\sqrt{p_i(1-p_i)}.
\]

For a real vector `(a_S)`, define `g_a=sum_S a_S phi_S`.  Then `g_a` is
a Boolean sign on every positive-mass atom if and only if, for every
`U subseteq [n]`,

\[
 \sum_{S,T}a_Sa_T
 \sum_{\substack{R\subseteq S\cap T\\S\triangle T\cup R=U}}
 \prod_{i\in R}\kappa_i=\mathbf1_{U=\varnothing}.       \tag{2.1}
\]

Indeed `phi_i^2=1+kappa_i phi_i`, so (2.1) is exactly the full Fourier
expansion of `g_a^2=1`.  Completeness of the product basis proves both
directions.  The empty equation is Parseval.  The nonempty equations are
additional sign-sensitive Booleanity constraints.

Writing

\[
 a_S=b_S\sqrt{\prod_{i\in S}p_i(1-p_i)}
\]

turns the certificate rational at rational biases because

\[
 (X_i-p_i)^2=p_i(1-p_i)+(1-2p_i)(X_i-p_i).             \tag{2.2}
\]

For an actual sign `g`, the exact forward and inverse formulas are

\[
 b_S=\mathbb E_{X_{-S}}\Delta_Sg,
 \quad \widehat g_p(S)^2=b_S^2\prod_{i\in S}p_i(1-p_i),             \tag{2.3}
\]

\[
 g(x)=\sum_Sb_S\prod_{i\in S}(x_i-p_i).                          \tag{2.4}
\]

These formulas retain the truth table, normalization, and coefficient signs.

### Exact nonrealizable law

At one bit and `p=1/4`, the masses

\[
 a_\varnothing^2=a_{\{1\}}^2=1/2
\]

are nonnegative and normalized.  But `kappa=2/sqrt(3)`, and the nonempty
coefficient in `g_a^2` is, for either relative sign,

\[
 2a_\varnothing a_{\{1\}}+\kappa a_{\{1\}}^2
 =\pm1+1/\sqrt3\ne0.
\]

Thus squared masses plus Parseval do not certify biased Boolean
realizability.  This is a finite obstruction to a helper representation, not
an FEI counterexample.

## 3. PROVED: exact dyadic domain; CONDITIONAL real-bias closure

A Boolean sign on `m` uniform bits has positive-output probability `k/2^m`.
Conversely, a truth table with exactly `k` positive atoms realizes `k/2^m`.
Therefore finite uniform Boolean encoders realize exactly the dyadic
probabilities.  Any finite vector of dyadic probabilities is jointly realized
using disjoint encoder blocks.

This validates the exact domain of the gate-potential proposition in the
source: its potential is defined on dyadic probabilities, and that is already
equivalent to uniform FEI.  No finite uniform Boolean gate has a nondyadic
output probability, so the encoder infimum does not itself define an
all-real-bias potential.

For a fixed finite gate, (2.3) proves continuity under product-bias limits.
When `p_i` tends to zero or one, coefficients containing `i` vanish; the other
coefficients converge to those of the gate contracted to the unique
positive-mass slice.  Ordinary spectral entropy, influence, corrected
entropy, and deficit therefore extend continuously, using `0 log(1/0)=0`.

Hence the precise transfer statement is conditional:

> A gate inequality holding uniformly on all interior dyadic bias vectors
> extends to all interior real bias vectors if every additional potential
> term has a specified continuous extension.  Deterministic endpoints are
> then handled by contraction.

The continuity hypothesis is essential; it is not supplied by the dyadic
infimum definition.

## 4. PROVED scope failures

1. **Deterministic inputs.** At `p_i in {0,1}`, contract the input before
   forming the basis.  Off-support truth-table values are irrelevant, and a
   normalized `phi_i` would divide by zero.
2. **Repeated physical variables.** Let `G(y_1,y_2)=y_1y_2` and let `h` be a
   balanced sign.  Reuse gives `G(h,h)=1`; disjoint fresh copies give balanced
   parity `h_1h_2`.  Thus a repeated child does not induce the product law
   required by disjoint composition, unless it is deterministic.
3. **Physical versus spectral conditioning.** A uniform dictator has spectral
   support `{i}`.  Conditioning the spectral set on containing `i` retains
   `{i}`, whereas physically fixing the input makes the child constant with
   spectral support `empty`.  These operations cannot be substituted.

## 5. Weighted obstruction replay

The source-bound A042 controls were checked at their exact scopes:

- `alpha TC(Q)/I=(ln m+1)/8+O((ln m)/m)` refutes the event
  conditional-input-TC payment, not corrected FEI+.
- The pivotal residual `(1/2)ln m-ln 2+O((ln m)/m)` refutes only the
  coefficient-one credit proposal.
- The fixed-`m` limit `q->0`, followed by `m->infinity`, refutes the proposed
  every-coordinate physical conditional-input-TC payment.  It does not refute
  existential spectral-coordinate selection.

The weighted threshold is an actual Boolean gate for every interior
parameter.  At deterministic endpoints the coordinate is contracted before
any ratio is formed; raw `0/0` is not assigned an endpoint value.

## 6. Exact validation

`CHECK.py` uses `fractions.Fraction`; no random sampling or floating point is
used.  For each of all 256 three-bit Boolean truth tables and each frozen bias
vector

\[
 (1/2,1/2,1/2),\quad(1/4,1/3,2/5),\quad(1/8,3/4,1/3),
\]

it independently computes (2.3), verifies mass normalization, reconstructs
all eight truth-table values through (2.4), and checks all eight coefficients
of `g^2=1` through the rational form (2.2).  It also verifies the repeated
variable and conditioning witnesses.

Command:

```text
python CHECK.py | tee CHECK.out
```

Actual output:

```text
Arithmetic: fractions.Fraction
Random seed: NONE
Dimension: 3
Boolean truth tables checked: 768
Assertions passed: 13060
Assertions failed: 0
Fake one-bit law: masses=(1/2,1/2), p=1/4, NOT REALIZABLE
Repeated-variable witness: G(h,h)=1 but G(h1,h2) is balanced
Physical/spectral conditioning supports: {empty} versus {{i}}
```

The all-dimensional result is the algebraic proof in Section 2; the finite
checker is an exact reproducer, not a finite-to-infinite proof.

## 7. Sources and immutable versions

- `assignments/B09.json`, blob
  `9c3ea2148589e4c23d8754d6f349e5564bfd58d9`.
- `EXECUTION_PROTOCOL.json`, blob
  `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- `source_material/reductions/paper/biased.tex`, open-problems commit
  `10bd8f25e7f93509b1ccb4daf9d8999fcb776f98`, blob
  `b620357b573b2906e8cb2df5966576c27ce3ffcd`; specifically the product basis,
  exact disjoint composition, weighted controls, and finite-cube gate
  potential proposition.
- A042 endpoint lower-bound correction, commit
  `6a287ff3c0bdf3956d7e981015789d16f4ca93b3`, report blob
  `144d7c0b8646bd01a119d932df2e14846ec24d91`.
- A042 weighted-control reconstruction, commit
  `6d5d784827c564687450f821edabd369465280c2`, report blob
  `5c5ad1e37e295cbd3de49ae10d58299266489294`.

No claim here depends on acceptance of the pending Maassen--Uffink theorem.

## 8. Packet delta and remaining gap

**New movement:** A045 now has a complete inverse/norm/Booleanity certificate,
an exact nonrealizable normalized law, a proof that the physical finite-cube
domain is exactly dyadic, and sharp boundary/reuse/conditioning rules.  The
source's dyadic gate-potential scope is validated; automatic all-real extension
is rejected unless a continuous potential extension is supplied.

**Artifact status:** both A045 deliverables are complete as author-side
artifacts.  Independent review by A091 or A090 remains required, so A045 is not
accepted in the campaign registry.

**First unsupported line toward full FEI:** no arity-uniform gate potential
`Gamma` satisfying the universal gate inequality has been constructed.  The
inverse certificate decides whether a candidate law is Boolean; it does not
provide the missing potential or influence payment.

**Next action:** use (2.1) as a realizability filter on proposed A041 weighted
replacement laws, or independently review the dyadic gate-potential
equivalence and its boundary contraction.  Consumers: A041, A043, A044, A091,
A090, and B20.

No full-FEI proof or counterfamily was obtained.
