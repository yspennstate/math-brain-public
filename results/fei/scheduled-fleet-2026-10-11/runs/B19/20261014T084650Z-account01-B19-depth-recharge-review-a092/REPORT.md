# B19 / A092 independent review — fixed-dimension depth recharge

**Run:** `20261014T084650Z-account01-B19-depth-recharge-review-a092`  
**Primary packet:** A092  
**Reviewed claim:** `B05-A023-DEPTH-RECHARGE-NOGO-v1`  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Verdict:** **ACCEPTED AT DECLARED ROUTE-OBSTRUCTION SCOPE**  
**Reviewer strengthening:** **GENERIC REPLAY-CYCLE LEMMA, PENDING FRESH A085/A090 REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Audited candidate

For every Boolean \(f\) and every finite path of two-coordinate blocks
with consecutive one-coordinate overlap, the candidate asserted

\[
V^+(f;\mathcal X)=\sum_t
[\widetilde\Lambda_{X_{t+1}}(f)-\widetilde\Lambda_{X_t}(f)]_+
\le C I(f)
\]

for one absolute \(C\).  With a verified payment
\(G\le a_0I+bU+V^+\), this would give GU with \((a,b)=(a_0+C,b)\).
The candidate is an assembly helper, not GU itself.

## Verdict and independent reconstruction

Starting from the Boolean definition

\[
f(y,x,z,u)=x\quad(y=1),\qquad f(y,x,z,u)=zu\quad(y=-1),
\]

the independent Walsh reconstruction gives

\[
f=\frac{x+xy+zu-yzu}{2},
\]

\[
\widetilde\Lambda_{\{y,x\}}=1+\frac1{\ln2},\qquad
\widetilde\Lambda_{\{y,z\}}=1+\frac2{\ln2},
\]

and all four coordinate influences equal \(1/2\), so \(I(f)=2\).
On the alternating path with \(2r-1\) transitions,

\[
V^+=\frac r{\ln2},\qquad
\sum_t(\widetilde\Lambda_{X_{t+1}}-
\widetilde\Lambda_{X_t})=\frac1{\ln2}.
\]

The counterexample and its sign are exact.  The producer claim is accepted
without mathematical repair.

## Stronger structural conclusion

For any potential \(P\), a replayable two-way edge with \(P(B)>P(A)\)
forces positive variation \(r(P(B)-P(A))\) along an alternating walk, while
the signed variation telescopes to \(P(B)-P(A)\).  Thus an arbitrary-walk,
fixed-resource positive-variation theorem can hold only when the potential
is constant on every replayable communicating component, or when revisits
are bounded.

This makes the surviving obligation precise: a useful GU assembly must be
acyclic, retain signed refunds, or carry persistent ownership state.

## Scope corrections and exclusions

The distinct-union influence \(3/2\) is paid once.  A fee paid per
transition is not refuted, but it grows with depth and supplies no uniform
GU constant.  The result does not refute an acyclic reveal tree,
persistent ownership, the exact signed \(B_i-\Gamma_i+K_i\) identity,
universal GU, or FEI.  Two missing TeX backslashes in the producer report
are typesetting-only.

## Verification and next action

`REVIEW_CHECK.py` was written independently from the circuit definition.
Exact Fraction arithmetic checks Booleanity, all sixteen Walsh
coefficients, the orbit energies, all influences, and five path depths.

Next: prove persistent whole-slice ownership on an acyclic physical reveal
tree and identify every retained negative swap with an actual
\(\Gamma_i-K_i\) credit.  The reviewer-supplied generic cycle lemma needs
fresh A085/A090 review before registry adoption.

Model: Codex.  Reasoning-effort metadata: UNKNOWN.

