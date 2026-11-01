# B01 / A004 — tensor-suspension amplification of the SMR lower bound

**Run:** `20261014T080727Z-fleet01-B01-tensor-suspension-a004`  
**Primary packet:** A004, constant and unit ledger  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B01-A004-TENSOR-SUSPENSION-LB-v1`  
**Status:** **PROVED ROUTE LOWER BOUND, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate and implication

For \(0<\eta\le1\), the sufficient signed-mismatch estimate is

\[
M(f)+(1+\eta)U(f)\le cI(f).
\tag{SMR}_{c,\eta}
\]

It would imply GU with \((a,b)=(c+2,1-\eta)\), hence FEI constant
\(2+2(c+2)/\eta\).  The bounded objective was to decide whether tensoring
or tensoring followed by one rare/fair suspension amplifies the strongest
exact activation witness.

## New result

Tensoring alone cannot amplify: \(U,I,G,B,M\), and therefore
\(L_{c,\eta}=M+(1+\eta)U-cI\), are exactly additive on disjoint products.

However, let \(q\) be mask 56242, \(F=A(q)\),
\(Q=F^{\otimes4}\), and \(W=A(Q)\).  Then

\[
c_W(\eta)=1.770873264041823\ldots
+1.451867015896827\ldots\eta.
\]

Exact rational-log interval certificates prove

\[
c_W(\eta)-c_F(\eta)
=0.037915828805916769\ldots
+0.11506096192931070\ldots\eta>0
\]

for every \(\eta\ge0\).  In particular,

\[
\boxed{c_W(1/4)=2.133840018016030\ldots>2.1338.}
\]

Thus the previously known necessary bound
\(c\ge2.0671589487\ldots\) at \(\eta=1/4\) strengthens to
\(c>2.1338\) within the same SMR route.

The all-\(t\) calculation also shows

\[
c_{A(F^{\otimes t})}(\eta)
=c_F(\eta)+\frac{2+2\eta-c_F(\eta)}{tI(F)}+o(t^{-1}).
\]

So this mechanism gives a finite improvement but no unbounded
amplification.

## Verification

- Exact 120-term rational atanh intervals certify both affine coefficient
  signs and \(c_W(1/4)>2.1338\).
- Direct truth-table reconstruction checks additivity of \(U,I,B,G,M\) on
  \(F^{\otimes2}\); maximum discrepancy is \(9.77\times10^{-15}\).
- Direct 11-variable reconstruction agrees with the recurrence threshold
  to \(1.16\times10^{-14}\).
- The exact proof is in `PROOF.md`; commands and complete outputs are saved.

## Before/after and next unpaid step

Before: the strongest source-checked \(\eta=1/4\) route lower bound was
\(c\ge2.0671589487\ldots\).  After: \(c>2.1338\).

This does not provide an admissible \((a,b)\), because it is a lower bound
on one sufficient proof route.  The next A004 action is to derive a uniform
upper bound for the full activation charge in (2) at some finite
\(c>2.1338401\), or find a genuinely iterated suspension whose normalized
threshold grows rather than returning to the seed threshold as in (5).

Fresh independent review should be assigned to A086 or A090.  Model:
Codex; reasoning effort metadata: UNKNOWN.

