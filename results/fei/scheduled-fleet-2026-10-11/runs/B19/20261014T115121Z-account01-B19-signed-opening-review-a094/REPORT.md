# B19 / A094 — adversarial review of signed-opening history transfer

**Reviewed claim:** `B05-A023-SIGNED-OPENING-HISTORY-TRANSFER-v1`  
**Producer:** account01/B05, canonical commit `d232abb332afaa7932be590f77fa158255d5d12e`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **INDEPENDENTLY ACCEPTED AT CLARIFIED SCOPE**  
**Universal GU / full FEI:** **OPEN**

## Audited candidate

For (c_*=29/2+4/\ln2), every Boolean core (f), every core-coordinate
block (X), every (0<\eta\le1), and a fresh fair activation (F=A(f)),
open (X\cup\{z\}) at the selector root and pass (X) to the core child.
The claim is

\[
\Delta_zL_{c_*,\eta}(F)+2(R-O)
\le\Phi(f)-\Theta_X(f)\le0.
\]

If the core already has a complete inherited-(X) SOLD tree, prepending
this node gives the conditional endpoint

\[
G(F)\le\left(\frac{33}{2}+\frac4{\ln2}\right)I(F)<22.270781I(F).
\]

## Verdict and reconstruction

The one-node theorem is correct.  I reconstructed the proof from the
definitions rather than the producer's status label:

1. (q) is increasing, singleton mass is dominated by the matching
   influence or orbit energy, hence (Phi(f)\le\Theta_X(f)).
2. With inherited block empty, opening (X\cup\{z\}), and querying (z),
   the direct definitions give
   (R-O=\Phi(F)-\Theta_X(f)/2).  The entire positive opened orbit packet
   cancels before any upper bound.
3. Substitution into the independently reviewed half-packet invariant
   proves the signed node drift is nonpositive with no dimension, depth,
   block-size, bias, or overlap loss.
4. The complete-tree implication is a valid conditional telescope.
   Constant leaves have zero (L) and zero orbit potential.

No material repair was needed, so this review remains independent.

## Required scope clarification

“Arbitrary history block” must be read as an arbitrary block **opened at
this outer selector root and inherited by the core child**.  The theorem
does not pay arbitrary already-inherited history at an internal selector:
the audited node starts with inherited block empty.  It also does not prove
that the core admits a complete SOLD tree.

For stopped trees, terminal (L) and terminal (Theta) reserves remain.
Dropping them would be a circular leaf assumption.  Biased/nonfresh
selectors and later data-query nodes are outside the claim.  Accordingly,
this result is not A023 closure and does not establish a universal GU pair.

## Independent finite audit

`INDEPENDENT_CHECK.py`, written independently from the definitions, uses
exact rational Walsh coefficients.  It exhausts every Boolean core through
three variables and tests seeded cores through six variables, every block
in the exhaustive range and 20 declared blocks for larger cores, at four
values of (eta).

The run passed all direct (R-O) identities, all
(Phi\le\Theta_X) checks, and all signed node inequalities.  These finite
checks are regression evidence; the proof is analytic in `REVIEW_PROOF.md`.

## Remaining unpaid line

Prove that every Boolean core and inherited block (X) admit a complete
adapted physical restriction tree satisfying SOLD, or replace that
existence claim by a universal aggregate argument retaining all terminal
reserves.  The smallest next adversarial case is a two-level overlapping
history such as ({x,y}\to{y,z}), where the second node starts with
nonempty inherited history.

Model: Codex. Reasoning-effort metadata: UNKNOWN.
