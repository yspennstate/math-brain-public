# I0004 serious second attempt — 2026-10-12

This is a continuation of ATTEMPT.md, with its exact chain, positive-height C, pair scatter S, dispersion D, and published transience input unchanged. Two previously untried approaches are recorded in ATTEMPT.md Section 9. This file pursues the first. Overall verdict remains PARTIAL; the stronger results below do not classify arbitrary irrational angles.

## 1. Main result and notation

**Theorem.** Fix an even integer b_*≥2. Let

α=[0;a_1,b_1,A_1,b_2,A_2,b_3,A_3,…],

where a_1≥1 is an integer, every b_m is a positive even integer with 2≤b_m≤b_*, and A_m are positive integers. Suppose there exist c>0 and p>2/3 such that

A_m≥c m^p for all sufficiently large m.

Then the exact phase-zero simple random walk of ATTEMPT.md Section 1 is transient.

In particular the previously unresolved α=[0;1,2,33,2,34,2,35,2,…], A_m=m+32, is transient. The spikes need neither be monotone nor have an upper growth bound. The intervening digits need not all equal 2; any uniformly bounded sequence of positive even digits is allowed.

For p>1 it suffices to apply the result with exponent 1; hence the proof will take 2/3<p≤1. Write Q_m=q_{2m}, and B_m=S(Q_m)/Q_m², where S and C are as in ATTEMPT.md. Set

T=2b_*+1, E=8T+4, κ=1/(1,048,576 T²), d=κ/4.

These deliberately conservative constants depend only on the bound b_*.

## 2. Geometry of a full tower and uniformly bounded profile errors

Every Q_m is odd: q_0=1, q_2=b_1q_1+1 is odd, and q_{2m+2}=b_{m+1}q_{2m+1}+q_{2m}. This induction uses only evenness of the b_m, not parity of the A_m or of a_1.

Fix m, abbreviate q=Q_m, A=A_m, q^+=Q_{m+1}, and r=q_{2m−1}<q. The intermediate denominator is q'=Aq+r, while

q^+=(b_{m+1}A+1)q+b_{m+1}r.

Consequently 2Aq<q^+≤T A q. Also δ=α−p_{2m}/q obeys |δ|<1/(q q'), by the convergent estimate proved in ATTEMPT.md Section 3. Let J=⌊q^+/q⌋. Then 2A≤J≤TA.

For each complete block 0≤j<J define H_j=C(jq) and

e_{j,t}=∑_{u=1}^t(ε_{jq+u}−ε_u), 1≤t≤q.

The identity

C(jq+t)=C(t)+H_j+e_{j,t}                                          (2.1)

is exact by subtracting the cumulative sums. We now prove the important bound

|e_{j,t}|≤E for every such j,t.                                  (2.2)

For every y≤Jq≤q^+, |yδ|<q^+/(q q')<T/q. For a fixed residue u modulo q, both signs ε_u and ε_{jq+u} are values of the square wave at the rational grid point {up_{2m}/q}, displaced along the same direction by amounts of absolute value less than T/q. If the signs differ, the segment between their lifted arguments crosses a discontinuity in ℤ or 1/2+ℤ. Thus the rational grid point has circular distance at most T/q from 0 or from 1/2. Since p_{2m} is coprime to q, the q residues give precisely the equally spaced q-point grid.

A circular interval of radius T/q contains at most 2T+1 grid points: if its length 2T/q≥1, this follows from q≤2T; otherwise lift the interval to the line and use spacing 1/q, so at most floor(2T)+1 points lie in it. This statement also handles an interval crossing 0 by a different lift. The union of the two neighborhoods therefore contains at most 4T+2 residues. Each altered letter contributes a difference of absolute value at most 2 to any partial sum, proving |e_{j,t}|≤2(4T+2)=E. Multiples of q are included in this count. The phase-zero discontinuity is not discarded, and no generic-phase argument is used.

## 3. Variance accumulated by block offsets

Assume A≥32 and put K=⌊A/8⌋. Then K≥4 and K≥A/16. ATTEMPT.md's exact odd-denominator block lemma applies to the first K blocks, independently of the next intervening digit. If s=sign(δ), it gives H_j=js for 0≤j<K.

Let V_H be the variance of the J equally weighted values H_0,…,H_{J−1}. Pair scatter and restriction to the first K entries give

V_H=(1/J²)∑_{0≤u<v<J}(H_v−H_u)²

≥(K/J)²(K²−1)/12

≥(K/J)² K²/16≥κ A².                                            (3.1)

The last step uses J≤TA and K≥A/16: (K/J)²K²/16≥A²/(16⁴·16·T²)=κA². The factor 16⁴·16 is 1,048,576. The first K offsets have a true linear trend even though no trend is asserted for the rest of the tower.

Choose j uniformly on {0,…,J−1} and t independently uniformly on {1,…,q}. Put Y=C(t)+H_j, Z=e_{j,t}, and X=Y+Z=C(jq+t). Independence implies

Var(Y)=B_m+V_H.                                                  (3.2)

The variables Y and Z are not assumed independent. From |Z|≤E we have Var(Z)≤E[Z²]≤E².

For every A>0 and real u,v, expansion gives the exact identity

A(u+v)²−(A−1)u²+A(A−1)v²=(u+Av)²≥0.                            (3.3)

Apply it to the centered variables u=Y−E[Y] and v=Z−E[Z], then average and divide by A. For A≥1 this proves

Var(X)≥(1−1/A)Var(Y)−(A−1)Var(Z)

≥(1−1/A)(B_m+V_H)−E² A.                                        (3.4)

This argument retains the correlations between the error and the old profile; the loss is controlled rather than set to zero.

## 4. An almost lossless variance transfer

Let λ=Jq/q^+. Since q^+<(J+1)q and J≥2A,

λ≥J/(J+1)≥1−1/(2A), and λ²≥1−1/A.

Monotonicity of S, applied to the complete J-block prefix, yields

B_{m+1}=S(q^+)/(q^+)²≥λ² Var(X).

Combining (3.4) with 0<λ²≤1 and its lower bound gives

B_{m+1}≥(1−1/A)²(B_m+V_H)−E² A

≥(1−2/A)B_m+(κ/2)A²−E² A, for A≥32.                           (4.1)

In the last line (1−1/A)²≥1−2/A and ≥1/2, B_m,V_H≥0, and (3.1) is used. The sign of the negative error term was handled using λ²≤1, not by incorrectly replacing it by a lower bound. Neither B(N) nor B_m is asserted monotone.

Whenever A≥4E²/κ, the final two terms in (4.1) are at least d A². Thus, for all sufficiently large m under the theorem's growth hypothesis,

B_{m+1}≥(1−2/A_m)B_m+d A_m².                                  (4.2)

The threshold can be enormous because the constants are conservative, but it is finite and independent of m. No finite experiment is used to claim that (4.2) already holds with these constants at small m.

## 5. A fully proved accumulation bound

Take 2/3<p≤1 and choose c>0 with A_m≥c m^p eventually. Put k=2/c and h=d c². Choose an integer M large enough that (4.2), this growth bound, and 1−k/m^p≥0 all hold for m≥M. Since B_m≥0, (4.2) implies

B_{m+1}≥(1−k/m^p)B_m+h m^(2p), m≥M.                           (5.1)

Let a=h/(k+12)>0. We claim, for every integer m≥M,

B_m≥a(m−M)^(3p).                                                (5.2)

At m=M the right side is zero, so this follows from nonnegativity. For the induction step put t=m−M, so 0≤t≤m. The integral formula for a real power gives

(t+1)^(3p)−t^(3p)=∫_t^(t+1) 3p x^(3p−1) dx

≤3p(m+1)^(3p−1)≤12 m^(3p−1)≤12 m^(2p).

Here 3p≤3, m+1≤2m, 3p−1≤2, and 3p−1≤2p because p≤1. Also k t^(3p)/m^p≤k m^(2p). These inequalities show

(t+1)^(3p)≤(1−k/m^p)t^(3p)+(k+12)m^(2p).

The nonnegative coefficient in (5.1) allows substitution of the induction hypothesis, and h=a(k+12) proves (5.2) at m+1. This proves the claim without assuming any regularity or monotonicity of A_m.

For m≥2M, (m−M)≥m/2, hence

B_m≥a 2^(−3p)m^(3p).                                           (5.3)

Thus linearly growing spikes (p=1) accumulate at least a constant times m³ variance. This is precisely the accumulation missing from the first attempt.

## 6. Uniform summation across every scale, including very large spikes

It remains to avoid a divergent tail cost and avoid assuming A_m has an upper bound. Fix a sufficiently large m and abbreviate q=Q_m, A=A_m, B=B_m and K=⌊A/8⌋, L=Kq. The stable-block estimate (5.3) of ATTEMPT.md uses only the exact first K blocks, so it remains valid:

D(n)≥(n/16)√(1+B+(n/q)²), q≤n≤L.                               (6.1)

For n between L and q^+≤TAq, the exact K-block variance formula gives

S(n)≥S(L)=L²[B+(K²−1)/12]≥L²(B+K²/16).

Since L/q^+≥1/(16T) and K≥A/16,

D(n)²=n²+S(n)

≥n²[1+B/(256T²)+A²/(1,048,576T²)]

≥n²(1+B+A²)/(1,048,576T²).                                     (6.2)

Therefore the tail interval has reciprocal-dispersion sum at most

1024T [1+log(16T)]/√(1+B+A²).                                  (6.3)

To check this, use (6.2) and ∑_{n=L}^{q^+}1/n≤1+log(q^+/L)≤1+log(16T). This gives an O(1/√(1+B)) tail cost, rather than the earlier O(1/A) cost.

Set H=√(1+B)≥1. On the stable interval (6.1) gives D(n)≥(n/16)max{H,n/q}. Up to n≤Hq, the reciprocal sum is at most 16(1+log H)/H. Beyond Hq it is bounded by 16∑q/n²≤32/H: for real Hq≥1, with N=⌊Hq⌋, the integral bound gives ∑_{n>Hq}1/n²≤1/N≤2/(Hq). Restriction to n≤L only decreases either bound. Thus for a constant C_T depending only on T,

∑_{n=Q_m}^{Q_{m+1}−1}1/D(n)≤C_T log(2+H)/H.                    (6.4)

This bound is independent of any upper bound on A_m. In deriving it, we used the linear trend of the stable offsets to sum the long range n/q>H and retained old variance in the tail.

The function g(H)=log(2+H)/H is decreasing for H>0. Indeed its derivative has numerator H/(2+H)−log(2+H)<0: log z≥1−1/z for z>0, obtained by minimizing log z−1+1/z at z=1, and for z=2+H one has H/(2+H)=1−2/z<1−1/z. By (5.3), H≥c' m^(3p/2) eventually, for some c'>0. Consequently the right side of (6.4) is at most C(1+log m)/m^(3p/2).

This series converges because r=3p/2>1. For a direct domination, let η=(r−1)/2>0. For m≥1, log m=∫_1^m dx/x≤∫_1^m x^(η−1)dx≤m^η/η, so the summands are bounded by a constant times m^(−(r+1)/2), whose exponent exceeds one. The intervals [Q_m,Q_{m+1}) cover all sufficiently large integers. We conclude ∑_n1/D(n)<∞. ATTEMPT.md Section 2, with the already verified hypotheses of Brémont Corollary 3.7(3), now proves the main theorem. ∎

## 7. What could fail, and the checks required

* A uniformly bounded number of changed letters does not by itself imply bounded total block sums over many blocks. We use the exact offset H_j for each block and bound only the within-block profile error e_{j,t}.
* No independence between old profile and error is assumed. The scaled-square identity (3.3) controls their covariance. It is the key algebraic step selected for an additional Lean check.
* The partial final block can dilute variance. Its loss is tracked explicitly by λ²≥1−1/A. Dropping it without this factor would be invalid.
* The first K offsets have a linear trend; later offsets need not. Restricting pair scatter proves (3.1) even when later offsets reverse direction.
* In the scalar induction the coefficient must be nonnegative. M is chosen to enforce that, in addition to the finite threshold for absorbing the bounded-profile error.
* The old tail estimate alone costs 1/A and is insufficient for A_m=m+32. Section 6 strengthens the tail using the full inherited B_m; all scales remain covered.
* This proof is for exact phase zero and odd even-index denominators ensured by bounded even intervening digits. It does not transfer automatically to other phases, odd intervening digits, or unbounded intervening digits.
* The constants imply only an eventual asymptotic lower bound. Small finite examples cannot certify the m^(3p) statement, but can falsify the finite comparison on which it rests. Exact tests in followup_checks.py passed for the first three towers of the linear-gap family (through 1,022,701 heights), a variable-even-separator family, and a nonmonotone-spike family. They checked all complete-block profile errors in those towers, offset variance, the covariance-sensitive scaled inequality, normalization loss, transfer recursion and selected all-scale inequalities using exact integer and rational arithmetic. See followup_checks.json. Additional exhaustive algebra tests covered 18,496 scaled-square cases and 81,200 integer cubic-barrier cases. The run took 1.87 seconds and well under 1 GB of memory. The recurrence's large eventual threshold is justified analytically, not tested numerically.
* Running `lake env lean ~/brain_workers/TRIO_1011/op/I0004/VarianceLoss.lean` from ~/lean_verify exited 0 after 120.79 seconds with no diagnostics. The scaled-square identity, its inequality, and the cubic increment are kernel checked, with no sorry or native_decide. The finite averaging argument, calculus estimates, continued-fraction geometry and full probability theorem are written proofs, not claimed as formalized. See lean_followup_check.txt.

## 8. Remaining gap after the second attempt

The full source question still permits every irrational α. The theorem above handles bounded even intervening digits and spike lower growth with exponent strictly above 2/3. It supplies no classification for arbitrary parity patterns or arbitrary intervening-digit growth, and does not settle the boundary family A_m=ceil(m^(2/3))+32 with intervening digit 2. At that exponent this argument produces at best a dispersion upper cost of order log m/m, which is not summable; failure of this upper bound to be summable is not evidence of recurrence. The old recurrence sufficient criterion also does not classify this boundary family: its summands are O(log m/m^(5/3)), a convergent series. The precise continuing mathematical gap is a sharp accumulation estimate or different recurrence/transience criterion that evaluates those remaining arithmetic regimes.

No source-wide SOLVED verdict and no novelty claim are made. The previous remaining example A_m=m+32 is now resolved by a complete written special-case proof.
