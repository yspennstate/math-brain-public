# B01 / A004 — iterated tensor-suspension limit

**Run:** `20261014T090500Z-fleet01-B01-iterated-suspension-a004`  
**Primary packet:** A004, constant and unit ledger  
**Stable gap:** `GU-ASYMMETRY-MISMATCH`  
**Claim:** `B01-A004-ITERATED-SUSPENSION-LIMIT-v1`  
**Status:** **PROVED ROUTE LOWER BOUND AND FINITE-LIMIT THEOREM, PENDING INDEPENDENT REVIEW**  
**Universal GU / full FEI:** **OPEN**

## Exact candidate and GU implication

For \(0<\eta\le1\), the sufficient signed-mismatch estimate is

\[
M(f)+(1+\eta)U(f)\le cI(f). \tag{SMR}_{c,\eta}
\]

It implies GU with \((a,b)=(c+2,1-\eta)\), and hence FEI constant
\(2+2(c+2)/\eta\).  The bounded objective was to determine whether genuine
iteration of tensor-suspension makes the necessary threshold unbounded.

## Result

Let \(F_0=A(q)\), with \(q\) the mask-56242 activation witness, and define

\[
F_{k+1}=A(F_k^{\otimes4}).
\]

The exact activation recurrence compresses this exponentially growing
tower to \(U,I,M\), its mean, and finitely many weighted singleton types.
At \(\eta=1/4\), an outward rational-log certificate proves

\[
\boxed{c_{F_4}(1/4)>2.18},
\]

improving the preceding necessary bound \(c>2.1338\).  The exact residual
at \(c=2.18\) lies in

\[
[0.18867195539361673287,0.18867195539361673288].
\]

The tower nevertheless cannot amplify without bound.  Its mean satisfies

\[
m_{k+1}=\frac{1+m_k^4}{2}
\]

and converges to \(\rho=0.543689012692\ldots\).  Singleton mass and its
logarithmic moment remain uniformly bounded because old mass contracts by
at most \((5/8)^6\).  Therefore the node corrections in

\[
I_{k+1}=2I_k+d_k^I,quad U_{k+1}=2U_k+d_k^U,quad
M_{k+1}=2M_k+d_k^M
\]

are uniformly bounded.  Dividing by \(2^k\) gives convergent series and

\[
c_{F_k}(\eta)\to\alpha_\infty+\beta_\infty\eta<\infty.
\]

Numerically,

\[
\alpha_\infty\approx1.808574256827,qquad
\beta_\infty\approx1.539070793542,
\]

so \(c_\infty(1/4)\approx2.193341955212\).  These last decimals are
numerical; finite convergence and the \(2.18\) lower bound are proved.

## Scope and next move

This is a stronger necessary constant for one sufficient route, not an
admissible GU pair.  It proves that iterated fourfold tensor-suspension has
a finite ceiling and cannot refute every finite \(c\).

This is the third substantive lower-bound attempt within the same gap
(reused cone wedge, one suspension, iterated tower).  The mechanism is now
retired.  The next A004 action is to upper-bound the complete node correction
\(\Theta\) in the signed recurrence, retaining all singleton-logarithmic
credit, or to replace SMR by a smaller aggregate estimate.

Fresh independent review should be assigned to A086 or A090.  Model:
Codex; reasoning-effort metadata: UNKNOWN.

