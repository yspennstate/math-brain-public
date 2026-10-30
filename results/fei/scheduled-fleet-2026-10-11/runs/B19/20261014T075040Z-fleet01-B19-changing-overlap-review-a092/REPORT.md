# B19 / A092 independent review — changing-overlap swap obstruction

**Run:** `20261014T075040Z-fleet01-B19-changing-overlap-review-a092`  
**Primary packet:** A092  
**Reviewed claim:** `B05-A023-CHANGING-OVERLAP-SWAP-NOGO-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED ROUTE-OBSTRUCTION SCOPE**  
**Reviewer strengthening:** **ALL LOCAL BLOCK-INFLUENCE FEES REFUTED, PENDING FRESH REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Audited candidate and GU relevance

B05 refutes an absolute transition fee for the fixed-block logarithmic orbit
potential under the active swap ({y,x}\to{y,z}):

\[
\widetilde\Lambda_{\{y,z\}}(f)
\le\widetilde\Lambda_{\{y,x\}}(f)
+C(\operatorname{Inf}_x(f)+\operatorname{Inf}_z(f)).
\]

Such a fee would let the reviewed fixed-block ownership account follow a
changing rare-activation hierarchy.  This is an auxiliary route to the
signed-mismatch estimate and hence GU; it is not itself GU.

## Verdict

The Boolean multiplexer, orbit energies, majority coefficient, pivotal
budgets, and asymptotic constant all reconstruct correctly.  For

\[
f_m=x\quad(y=1),\qquad f_m=zM_m\quad(y=-1),
\]

one has exactly

\[
\widetilde\Lambda_{\{y,z\}}(f_m)
-\widetilde\Lambda_{\{y,x\}}(f_m)
=m q(a_m^2/2)-\frac12
=\frac1\pi\log_2m+O(1),
\]

while (operatorname{Inf}_x=operatorname{Inf}_z=1/2).  The B05 claim is
accepted without mathematical repair.

## Stronger adversarial finding

The shared selector also has

\[
\operatorname{Inf}_y(f_m)=\frac12.
\]

Therefore even the stronger rule

\[
\widetilde\Lambda_Y(f)
\le\widetilde\Lambda_X(f)
+C\sum_{v\in X\cup Y}\operatorname{Inf}_v(f)
\]

fails for every finite (C): the complete local block charge is (3C/2),
but the potential jump diverges.  Since B19 supplies this strengthening, it
requires an uninvolved A085/A090 review.

The counterfamily leaves total influence available:

\[
I(f_m)=\frac32+\frac12I(M_m)=\Theta(\sqrt m).
\]

Thus it kills local overlap fees, not whole-slice transport, a global
influence payment, signed KL cancellation, GU, or FEI.

## Independent verification

`REVIEW_CHECK.py` was written from the displayed Boolean function.  It does
not import or execute the producer checker.  Exact Fraction Walsh arithmetic
verified 45 orbit and influence identities across five direct families, and
the closed formula was evaluated through (m=10001).

One presentation correction is required: the producer report/proof dropped
several inline TeX delimiters and backslashes.  The mathematical formulas
are unambiguous and unaffected.

## Next action

The next viable target is a signed whole-slice ownership rule.  It should be
tested across two successive swaps to determine whether private-core
influence is charged once or recharged at each overlap change.
