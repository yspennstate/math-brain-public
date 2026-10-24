# B18 — the explicit prime 10-input obstruction is balanced-restriction-critical

**Status:** `PROVED_EXPLICIT_RESTRICTION_CRITICAL_OBSTRUCTION` for the live gate programme. The old read-once-`Gamma` / AND-extremality candidate remains **REFUTED**. Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were consumed directly; no authenticated mathematical/cognitive brain retrieval or receiver-context use is claimed.

## 1. Live target and exact dependencies

The current owner control asks the FEI fleet to converge on the all-gate potential inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_p=4p(1-p).
\tag{G}
\]

The owner's numerical AND/decomposable-extremality conjecture is already refuted by later source-exact mathematics, so this run does not try to prove that stale candidate. The relevant newest compatible inputs are:

1. **account01/B18**, `20260922T002302Z-gate-refutation-balanced-excess`, commit `64935432d83bb0c759225a6149535980157f1a62`: for every finite `C`, full FEI(C) is equivalent to
   \[
   H(g)\le C\,[I(g)-1]
   \tag{1.1}
   \]
   for every balanced Boolean `g`; balanced disjoint composition makes `H/(I-1)` a literal convex combination of component ratios.
2. **account04/B12**, `20260922T004033Z-prime-safe-split`, commit `d96b3f494236cacf75f4ae0d4395f0f2dbb3008c`: the exact child-slack/Poincare recursion and prime safe-split theorem. A minimum-arity failure for a fixed corrected potential is composition-prime and has every first split locally bad. I keep this distinct from the balanced-restriction statement below: unbalanced children still matter to (G).
3. **account04/B13**, `20260922T0055Z-arity10-prime-falsifier`, commit `ab7372430937a437a4a577e4b0b198d2a1cfae9c`: the explicit balanced monotone ten-input gate `G_10`, reconstructed from the certified 18-variable source, with
   \[
   I(G_{10})=\frac{257}{128},\qquad
   \frac{H(G_{10})}{I(G_{10})-1}>6.4593722816378554,
   \tag{1.2}
   \]
   and a complete 1012-block cofactor certificate that `G_10` is composition-prime.
4. **account04/B14**, `20260922T005458Z-gate-balanced-small-arity`, commit `017829c263df9a9abce84d25c070d11db7af54ae`: exhaustive exact-rational certification that every balanced unate gate through arity six has amplified ratio below `6.4`, with arity-six maximum
   \[
   \frac{46}{5}-\frac95\log_2 3
   =6.347067498701918\ldots .
   \tag{1.3}
   \]

The older account01/B18 curvature-refunded physical-restriction theorem remains valid and preserved, but the later OWNER MESSAGE explicitly supersedes the older A/B route as the substantive target. I therefore do not combine it conditionally into a false unconditional closure.

## 2. New theorem: every proper balanced restriction of `G_10` falls below 6.35

A coordinate restriction of `G_10` is obtained by declaring each of its ten local coordinates free, fixed to `0`, or fixed to `1`. I exhaustively checked every **nonzero-dimensional proper restriction**, i.e.

\[
\sum_{r=1}^{9}\binom{10}{r}2^r
=3^{10}-1-2^{10}
=58,024
\tag{2.1}
\]

restrictions.

Exactly `9,514` of them are balanced. Their counts by remaining dimension are

\[
\begin{array}{c|rrrrrrr}
\text{dimension}&1&2&3&4&5&6&7\\ \hline
\text{balanced restrictions}&1028&2882&3112&1788&512&152&40.
\end{array}
\tag{2.2}
\]

In particular there are **no balanced one- or two-coordinate restrictions** of `G_10`: the balanced restriction set has no remaining dimension 9 or 8.

For every balanced proper restriction `R` with `I(R)>1`, the checker proves by exact rational logarithm intervals that

\[
\boxed{
\frac{H(R)}{I(R)-1}<6.35.
}
\tag{2.3}
\]

The exact maximum is

\[
\boxed{
\max_{R\text{ proper balanced}}
\frac{H(R)}{I(R)-1}
=
\frac{46}{5}-\frac95\log_2 3
=6.347067498701918\ldots .
}
\tag{2.4}
\]

There are 28 maximizing restrictions. A representative fixes local coordinates

\[
x_0=0,\qquad x_3=1,\qquad x_6=0,
\tag{2.5}
\]

leaving seven variables. Its exact influence is `13/8`. Its normalized squared spectral masses are

\[
32\times\frac1{256},\qquad
4\times\frac1{64},\qquad
4\times\frac1{16},\qquad
4\times\frac9{64}.
\tag{2.6}
\]

Therefore

\[
H=\frac{23}{4}-\frac98\log_2 3,
\qquad
I-1=\frac58,
\tag{2.7}
\]

which gives (2.4). Every restriction with a different normalized spectral histogram is interval-separated strictly below this value; the same normalized histogram accounts for all 28 ties. Thus (2.4) is a finite certificate, not a floating-point maximization claim.

### Proof / verification boundary

The checker reconstructs the exact certified 18-variable source and verifies its truth-table SHA-256

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`,

then reconstructs `G_10`, rechecks balance, `I=257/128`, and all 1012 composition-prime blocks. For each of the 58,024 nonzero-dimensional proper restrictions it computes the integer Walsh transform. Entropy bounds use a 40-term exact-rational `atanh` enclosure for every logarithm. The executed standard-library checker exits `0`; no finite-dimensional extrapolation is used beyond this exact restriction lattice.

## 3. Consequence: a concrete balanced-restriction-critical prime obstruction

Combining (1.2) and (2.4), for every constant

\[
\frac{46}{5}-\frac95\log_2 3
<C<
\frac{H(G_{10})}{I(G_{10})-1},
\tag{3.1}
\]

the balanced composition-prime gate `G_10` violates the balanced-excess inequality (1.1), while **every proper balanced coordinate restriction satisfies it**.

In particular this holds simultaneously for the owner's current certificate scales `C=6.4559` and `C=6.4573`:

\[
\boxed{
R\text{ proper and balanced}
\Longrightarrow
H(R)<6.35[I(R)-1]
< C[I(R)-1],
}
\tag{3.2}
\]

but

\[
\boxed{
H(G_{10})>6.45937[I(G_{10})-1]>C[I(G_{10})-1].
}
\tag{3.3}
\]

So the small explicit prime falsifier is not merely a descendant of the 18-variable source: within its complete coordinate-restriction lattice, the balanced-excess obstruction is **born at the ten-input root**. This gives a concrete restriction-critical witness for the FEI-equivalent balanced formulation.

This does **not** prove that arity ten is globally minimal. The account04/B14 theorem excludes balanced-uniform unate witnesses through arity six, but non-unate gates at arities five and six, arbitrary gates at arities seven through nine, and nonuniform bias vectors remain outside this finite certificate.

## 4. Relation to the safe-split and rigidity machinery

The result sharpens the interface to B12 without overclaiming it. B12's exact gate recursion is

\[
S_c(G)=(1-t)S_c(G_0)+tS_c(G_1)+L_{i,c}(G).
\tag{4.1}
\]

The present theorem says that if one works only in the FEI-equivalent **balanced-excess** slice, no proper balanced child of this explicit root carries the obstruction. Therefore a successful gate proof cannot hope to descend this witness through a chain of balanced restrictions while preserving the offending ratio.

However, most one-coordinate children of `G_10` are unbalanced. Equation (4.1) depends on their actual gate slacks and on the local residual `L_{i,c}`. I do **not** infer from (2.4) that every first split of this particular `G_10` is bad in B12's stronger potential sense. B12's minimal-obstruction theorem proves existence of an all-coordinate-bad prime gate for a failed fixed potential, but does not identify that abstract minimal gate with `G_10`.

Likewise the exact zero-depth mixed-curvature classification remains preserved: all-zero-depth systems are character-twisted one-point defects and obey the previously proved `H<4J`. Nothing here promotes that branch, the curvature-refund branch, or any refuted `sum d_i=O(J)` bridge into a universal FEI closure.

## 5. Exact remaining arrow

The current AND/decomposable extremality conjecture is already source-exactly false. The smallest useful next implication on this explicit root is now:

> evaluate the B12 corrected residuals `L_{i,c}` for all ten first splits of `G_10` against a source-exact successor potential, retaining the unbalanced child slacks; either obtain a genuinely safe split or certify this concrete gate itself as all-coordinate bad for that potential.

At the global level, the owner-requested falsification job is done; the universal problem is to construct a different finite-cap `Gamma` satisfying (G), or prove the corresponding prime safe-split envelope uniformly. Full FEI remains **OPEN / NOT PROVED**.

## 6. Reproduction

Artifact checker: `CHECKER.py` (standard library only).

Executed command: `python -S CHECKER.py`.

Checker SHA-256: `0b94190ba5b14a114aed02d06eca3a02f25cb8459133ae45c975c1c0ea988e6f`.

Output SHA-256: `923ca3707217a12d0e2d1868dddcb246775c1637feeb196b4b23ee31bd350827`.

No novelty or publication-priority claim is made.