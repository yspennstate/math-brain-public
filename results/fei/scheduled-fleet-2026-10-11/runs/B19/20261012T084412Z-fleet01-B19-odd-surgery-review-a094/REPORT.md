# B19 / A094 independent review — B05 odd-surgery payment

## Verdict

**ACCEPTED AT THE DECLARED ONE-NODE SCOPE.**  I independently reconstructed
`B05_ODD_SURGERY_PAYMENT_v1`, `B05_ODD_M_SPARSE_PAYMENT_v1`, and their
odd-parity refund dependency.  No mathematical repair was needed, so reviewer
independence is preserved.

For every bent Boolean `g` on even `k>=10`, every `h` obtained by flipping
three distinct truth-table values, and every fresh `d`-bit one-address
selector,

\[
U(F)-(1-p)U(g)-pU(h)<327I_{\rm ctl}(F),\qquad p=2^{-d}.
\]

For odd `m` satisfying `m*2^(-k/2)<=1/32`, the general bound

\[
J\le\left(1+\frac{99m}{2\ln2}+4\log_2m\right)I_{\rm ctl}
\]

is also accepted.  Its constant grows with `m` and is not universal over
the surgery count.

## Independent reconstruction

The review independently established:

1. the complete selector Walsh spectrum and upper-mass formula;
2. the physical identity `I_ctl=2pdm*2^-k`;
3. the exact `J = scalar Phi + p(1-p)K + (1-2p)I_ctl`
   decomposition;
4. the odd-parity lower bound `|e_T|>=2*2^-k` and
   `K<=8m*2^-k*log2(m)`;
5. every Hessian constant, both Taylor remainders, and the final strict
   inequality `326.415903212827...<327`.

The full reconstruction is in `REVIEW_PROOF.tex`.

## Independent computation

`CHECK.py` imports no author code.  It passed:

- all 560 triple edit sets of a four-bit bent core;
- 53,760 exact Walsh-coefficient comparisons at selector depths 1 and 2;
- 1,120 exact physical control-influence comparisons;
- 40 independent 90-digit reconstructions of both entropy identities;
- exact rational certification of every Taylor-box and remainder constant;
- exact rational series enclosures for `ln(2)` and `ln(3)`.

The largest identity error was `1.26e-88`.  The exact triple half-Hessian
remainder was `51617/40=1290.425`, and the independently bounded
`Phi_uu/p` coefficient was `5.528809876...<6`.

## Scope correction and remaining gap

The accepted statement is a retained-child payment, not by itself an FEI
theorem for the terminal child `h`.  It is not restriction-closed and does
not control a hierarchy in which coherent cores change across nodes.  It
therefore does not supersede the explicit universal gap.

The next unpaid term is the `O(m)` scalar payment.  A universal argument must
replace the pointwise `m^2` Taylor charge by an averaged or single-use credit
of order `sum_T e_T^2=4m*2^-k`, while surviving even-`m` zero-atom erasure
and shared-variable descendants.

One harmless source typo was found: equation (16) contains `1.1,quad`
instead of `1.1,\quad`.  This has no mathematical effect and does not make
the reviewer a proof contributor.

## Literature boundary

O'Donnell–Tan applies to disjoint-variable composition; O'Donnell–Wright–
Zhou covers proper read-once/decision-tree classes; Potapov covers plateaued
and partially bent Boolean functions.  None supplies the reviewed
shared-core upper-set payment or widens it to arbitrary changing-core
hierarchies.  No novelty claim is made; details and URLs are in `SOURCES.md`.

## Status

The two reviewed B05 claims are independently accepted at their exact
scope.  Full FEI remains **OPEN**.
