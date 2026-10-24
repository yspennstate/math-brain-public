# B05 / A023 — odd-surgery retained-credit payment

## Result

**AUTHOR-PROVED, PENDING A087/A094 REVIEW.**  Let `g` be a bent Boolean
function on even `k` variables, let `h` be obtained by flipping any three
distinct truth-table values, and let a fresh `d`-bit selector activate `h`
at one address and otherwise return `g`.  For every even `k >= 10` and every
`d >= 1`, with `p=2^-d`,

\[
U(F)-(1-p)U(g)-pU(h)<327 I_{\rm ctl}(F).
\]

The constant is independent of dimension, selector depth, activation
probability, edit locations, and bent phases.  This is the first genuinely
higher-order coherent-surgery class beyond the one- and two-edit cases.

More generally, for every odd `m` satisfying
`m 2^(-k/2) <= 1/32`, the same physical first-revelation ledger proves

\[
J\le\left(1+\frac{99m}{2\ln2}+4\log_2m\right)I_{\rm ctl}.
\]

This exposes, rather than removes, the remaining parameter dependence: the
present scalar payment is `O(m)`.

## Exact mechanism

For the difference spectrum
`e_T=-2*2^-k sum_j g(x_j) chi_T(x_j)`, odd `m` forces the signed sum to be a
nonzero odd integer.  Hence every atom obeys
`2 delta <= |e_T| <= 2m delta`.  The upper cone then satisfies
`D_T/e_T^2 <= m^2 2^(k-|T|)`, yielding the retained rare-log credit

\[
K=\mathcal U(e)-\sum_T e_T^2(k-|T|)
 \le 8m\delta\log_2m.
\]

Combining this with the exact shared-selector identity and a uniform
three-variable Taylor estimate for the coherent scalar term gives the
stated bounds.  The full derivation is in `ODD_SURGERY_PAYMENT.tex`; the
single-use stopping ledger is in `RARITY_CREDIT_LEDGER.json`.

## Verification

`CHECK.py` performed:

- four direct full-truth-table Walsh reconstructions of the exact selector
  identity and the `Phi+K` decomposition (largest errors below `2e-12`);
- 36 deterministic triple-surgery checks over `k=10,12,14`, selector depths
  `d=1,2,4,8`, and three geometrically different edit sets;
- 12 deterministic general odd-`m` checks for `m=1,3,5,7` in the proved
  sparse regime.

The largest observed triple ratio was `3.684624267`, while the analytic
uniform constant is `326.415903213 < 327`.  These finite checks corroborate
the algebra; they are not the proof.

## Scope and class extension

Previous retained-credit results covered a one-point bent surgery and the
two-point algebraic refund/payment.  The new class covers arbitrary triples
uniformly in `k,d` and derives a general odd-surgery pattern.  Odd parity is
essential to the proof because it prevents zero difference-spectrum atoms.
Even edit counts require a separate treatment of erasures.

The stopping rule is physical, nonadaptive, and finite: spend the selector's
rarity credit exactly once when its fresh control block is first revealed;
no descendant receives it again.  This is a complete one-node payment for an
unbounded family, not a restriction-closed class and not a payment for an
arbitrary changing hierarchy.

## Remaining gap

Full FEI remains **OPEN**.  The result does not control arbitrary terminal
cores or a hierarchy whose coherent edit set changes from node to node.
The next unpaid step is to replace the `O(m)` term in the general odd-`m`
bound by a constant, or to amortize it across disjoint physical pivotal
events without reusing rarity credit.  An additional live issue is parity:
even surgery counts can create zero atoms and defeat the lower bound used in
the logarithmic refund.

## Sources and provenance

- Owner control revision `2026-10-12.1`, commit
  `40210272c19f43fed84f6a67653f9a04b0e11e28`.
- B05 contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Obstruction registry blob `e111933338dff1d7798c5e59b43700bbf30f7b96`.
- Neighboring two-surgery physical payment: canonical commit
  `ebafad5c0cbed83fd935c2d1ab7e490afc24992a`, proof blob
  `5f7e0b34afbb1795a03100a3ceddb8986d1b94fa`.
- Independent review of the algebraic two-surgery refund: canonical commit
  `85a6d0d5bad197f7d430421702be5ec75c48d75f`, report blob
  `65a9538bf284f032c661c91b6dce3ee1f8fd1b48`.

No literature novelty claim is made.  The proof is self-contained from the
displayed Walsh identities.
