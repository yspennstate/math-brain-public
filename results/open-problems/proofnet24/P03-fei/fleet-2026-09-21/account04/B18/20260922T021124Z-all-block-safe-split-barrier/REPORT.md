# B18 — shared-graft lower bound forces an all-block prime safe-split barrier

**Status:** `PROVED_ALL_BLOCK_MINIMAL_OBSTRUCTION / STRUCTURAL_INTEGRATION`.  
The old read-once-`Gamma` / AND-extremality programme remains **REFUTED**.  
Full uniform-cube Fourier entropy--influence remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated repository sources were read directly. No installed/native mathematical-brain retrieval or receiver-context was used.

## 1. Live target and exact dependencies

The later OWNER MESSAGE has superseded the older A/B route as the substantive target and asks all FEI workers to converge on the all-gate inequality. I therefore preserve the earlier mixed-curvature/zero-defect classification but do not combine it conditionally into a false closure.

This run uses four compatible source-exact ingredients.

1. **account04/B12 — Shannon child-slack and safe-split recursion.**  
   `proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T003525Z-shannon-margin-conservation/REPORT.md`, blob `7ca2a3c0943c44e80fe0312468964c9ad5eabb65`, and its safe-split successor `20260922T004033Z-prime-safe-split`.  
   For a fixed reference potential `Gamma`, a one-coordinate split satisfies
   \[
   D_G=(1-t)D_0+tD_1+R_i,\qquad
   P_G=(1-t)P_0+tP_1+Q_i,
   \]
   with \(Q_i\ge0\).  For
   \[
   S_c(G):=D_G+cP_G
   \]
   the exact recursion is
   \[
   S_c(G)=(1-t)S_c(G_0)+tS_c(G_1)+L_{i,c},
   \qquad L_{i,c}=R_i+cQ_i.
   \tag{1.1}
   \]
   B12 proved that a minimum-essential-arity violation is composition-prime and every first coordinate is bad.

2. **account02/B17 — exact composition cocycle.**  
   `proofnet24/P03-fei/fleet-2026-09-21/account02/B17/20260922T004442Z-gate-composition-cocycle/REPORT.md`.  
   Both \(D_\Gamma\) and \(P\), hence \(S_c\), decompose with the same nonnegative sensitivity weights. A minimum-arity violation therefore cannot be a nontrivial disjoint composition.

3. **account01/B18 / account03 continuation — source-valid shared-graft family.**  
   account01/B18 `20260922T0117Z-recursive-shared-graft` proves the exact Boolean recurrence. account03/B15 `20260922T012556Z-iterated-shared-graft` certifies a finite balanced monotone gate \(F_6\) with
   \[
   \frac{H(F_6)}{I(F_6)-1}
   >
   6.5218509495504481848401605388605.
   \tag{1.2}
   \]
   Relative to the historical read-once center \(C_0=6.4548\), this is the rigorous margin lower bound
   \[
   c_{F_6}>
   0.2682037982017927393606421554420.
   \tag{1.3}
   \]
   account03/B13/B18 subsequently prove that the fixed shared-graft recurrence has a finite increasing tail; that tail theorem is preserved and not re-certified here.

4. **account04/B13--B14 — explicit ten-input obstruction.**  
   The composition-prime \(G_{10}\) and its balanced-restriction-critical certificate remain valid. They show that the old AND/decomposable extremality already fails at small arity, but they do not identify the minimum gate for the much larger margin in (1.3). I keep that distinction explicit.

The older B18 zero-depth result also remains unchanged: the exact all-zero-depth class is the character-twisted one-point-defect class and satisfies \(H<4J\). No `sum d_i=O(J)` bridge is revived.

## 2. New block telescoping identity

Fix a product-bias instance \((G,p)\), a reference potential \(\Gamma\), and a nonempty set \(A\) of input coordinates. Reveal all coordinates in \(A\), obtaining restrictions \(G_z\) with the induced product probabilities on \(z\in\{0,1\}^A\). Define the **block residuals**
\[
R_A:=D_\Gamma(G;p)-\mathbb E_z D_\Gamma(G_z;p_{A^c}),
\tag{2.1}
\]
\[
Q_A:=P_G(p)-\mathbb E_z P_{G_z}(p_{A^c}).
\tag{2.2}
\]

Iterating B12's one-coordinate identities in any order of the coordinates in \(A\) gives
\[
\boxed{
R_A=\sum_{v\in{\cal T}_A}w_vR_v,\qquad
Q_A=\sum_{v\in{\cal T}_A}w_vQ_v,
}
\tag{2.3}
\]
where \({\cal T}_A\) is the partial restriction tree that reveals exactly \(A\), \(w_v\) is the probability of reaching node \(v\), and \(R_v,Q_v\) are the one-step residuals there.

Because the left sides of (2.1)--(2.2) depend only on the final block restriction, (2.3) proves **order independence** of the aggregate block residuals. Since every one-step \(Q_v\ge0\),
\[
\boxed{Q_A\ge0.}
\tag{2.4}
\]

For the scalar-corrected potential \(\Gamma_c(u)=\Gamma(u)+c\,u(1-u)\), define
\[
L_{A,c}:=R_A+cQ_A.
\]
Then
\[
\boxed{
L_{A,c}
=S_c(G;p)-\mathbb E_z S_c(G_z;p_{A^c}).
}
\tag{2.5}
\]

This is the block version of B12's exact child-slack recursion. It uses no Fourier relaxation, no bounded-incidence assumption, and no sign discard.

## 3. New theorem: minimum violations are bad for every physical block

### Theorem 3.1 — all-block minimal-obstruction theorem

Fix \(c\in\mathbb R\) and a reference potential \(\Gamma\) for which the constant/unary base cases are valid. Suppose there exists an interior product-bias Boolean instance with
\[
S_c(G;p)<0.
\tag{3.1}
\]
Choose such an instance with the minimum number \(r\) of essential inputs, deleting inessential coordinates.

Then:

1. \(r\ge2\);
2. \(G\) is composition-prime;
3. every nonempty restriction \(G_z\) obtained by fixing any nonempty coordinate block has
   \[
   S_c(G_z)\ge0;
   \tag{3.2}
   \]
4. for **every nonempty physical block** \(A\subseteq[r]\),
   \[
   \boxed{L_{A,c}<0;}
   \tag{3.3}
   \]
5. for every nonempty \(A\), \(Q_A>0\), and hence the normalized block residual margin
   \[
   c_{R,A}:=-\frac{R_A}{Q_A}
   \tag{3.4}
   \]
   is defined and satisfies
   \[
   \boxed{c_{R,A}>c.}
   \tag{3.5}
   \]

#### Proof

If \(G\) were a nontrivial disjoint composition, the exact cocycle for \(S_c=D_\Gamma+cP\) would write its negative value as a nonnegative weighted sum of lower-essential-arity factor slacks. At least one factor would be negative, contradicting minimality. Thus \(G\) is composition-prime.

Fix any nonempty block \(A\). Every restriction \(G_z\) has at most \(r-|A|<r\) available input coordinates and therefore fewer than \(r\) essential inputs. By minimality,
\[
S_c(G_z)\ge0
\]
for every \(z\). Equation (2.5) now gives
\[
L_{A,c}
=S_c(G)-\mathbb E_zS_c(G_z)
\le S_c(G)<0,
\]
proving (3.3).

It remains only to justify strict positivity of \(Q_A\). Choose any \(i\in A\) and reveal \(i\) first. Since all \(r\) coordinates are essential and \(r\ge2\), B12's exact degeneracy classification gives \(Q_i>0\) at the root: an interior essential split has \(Q_i=0\) only for a unary literal/negation. All later terms in the telescoping sum (2.3) are nonnegative. Hence \(Q_A>0\). Dividing
\[
R_A+cQ_A=L_{A,c}<0
\]
by \(Q_A\) gives (3.5). \(\square\)

### What is new relative to B12

B12 proved the singleton case \(A=\{i\}\): a minimum violation has every first coordinate locally bad. The theorem above upgrades this to **every physical restriction block at once**, including adaptively chosen multi-coordinate blocks. Thus a failed scalar-lift candidate cannot in general be repaired merely by saying "choose a larger block instead of one coordinate."

This does not say that every block of the original explicit witness \(F_6\) is bad. The all-block gate is the minimum-essential-arity descendant supplied by Theorem 3.1, and it need not equal \(F_6\).

## 4. Quantitative application of the current shared-graft lower bound

Use the historical read-once reference potential \(\Gamma_{\rm RO}\) with
\[
\Gamma_{\rm RO}(1/2)=C_0=6.4548.
\]

For a balanced gate at uniform bias,
\[
c_G
=4\left(\frac{H(G)}{I(G)-1}-C_0\right).
\tag{4.1}
\]
The source-valid finite gate \(F_6\) from account03/B15 therefore satisfies (1.3).

Consequently, for **every**
\[
c<
c_\star:=
0.2682037982017927393606421554420,
\tag{4.2}
\]
we have
\[
S_c(F_6)<0.
\tag{4.3}
\]
Apply Theorem 3.1. There exists a finite composition-prime Boolean gate \(P_c\), at an interior product-bias vector, such that every nonempty physical block \(A\) obeys
\[
\boxed{c_{R,A}(P_c)>c.}
\tag{4.4}
\]

In particular, at the exact decimal threshold
\[
\boxed{c=0.2682037982,}
\tag{4.5}
\]
there exists one prime gate for which **no coordinate and no larger physical block is a safe first reveal** for the read-once potential lifted by \(c\,p(1-p)\).

Equivalently, if
\[
A_r^{\rm block}
:=
\sup_{\substack{G\ {\rm composition\!-
prime}\\
                 G\ {\rm has}\ r\ {\rm essential\ inputs}\\
                 p\in(0,1)^r}}
\ \min_{\varnothing\ne A\subseteq[r]} c_{R,A}(G,p),
\tag{4.6}
\]
then
\[
\boxed{
\sup_{r\ge2}A_r^{\rm block}\ge c_\star.
}
\tag{4.7}
\]

The tiny arithmetic checker accompanying this report reproduces
\[
4(6.5218509495504481848401605388605-6.4548)
=
0.2682037982017927393606421554420
\]
exactly as decimal arithmetic and verifies that the convenient threshold (4.5) lies strictly below it.

## 5. Relation to the depth-two refund and why there is no contradiction

account01/B13's exact block-currency theorem shows a useful two-step refund on the **specific** 18-bit Numaro obstruction in the balanced zero-reference ledger: a high-priced auxiliary coordinate is cheaply repaired by pairing it with its source pivot.

Theorem 3.1 does not contradict that result.

- The B13 calculation is for a particular explicit gate and a particular zero-reference entropy/currency ledger.
- The present theorem is for a **minimum violation of the corrected read-once potential** \(S_c=D_{\Gamma_{\rm RO}}+cP\).
- The minimum gate produced here is not identified with the 18-bit seed, \(G_{10}\), or \(F_6\).
- The block residual in (2.1)--(2.5) retains the actual child slacks of the same potential; no zero-reference quantity is substituted for it.

What the theorem does establish is a hard structural boundary: **below the certified scalar margin \(c_\star\), no universal restriction induction based on finding one safe physical block can close the old read-once potential.** Some genuinely different potential/envelope or a non-safe-block compensating mechanism is required.

## 6. Status and exact remaining arrow

**PROVED**
- order-independent block telescoping for \(R_A,Q_A\);
- \(Q_A\ge0\);
- all-block minimal-obstruction theorem;
- quantitative all-block barrier at every \(c<c_\star\), in particular \(c=0.2682037982\).

**PRESERVED**
- explicit ten-input composition-prime / balanced-restriction-critical obstruction;
- exact zero-depth one-point-defect classification;
- shared-graft finite lower bound and tail theorem;
- all previously refuted bridges (`sum d_i=O(J)`, fixed-relative near-subcube payment, prescribed-coordinate payment, AND/decomposable extremality).

**OPEN / UNPAID**
- a finite-cap symmetric nonnegative potential satisfying the all-gate inequality for every composition-prime gate and every product bias;
- equivalently, a universal finite upper bound for balanced \(H/(I-1)\);
- any mechanism that pays the all-block-bad minimum obstruction without simply increasing the same scalar quadratic lift again.

Thus full FEI remains **OPEN / NOT PROVED**.

The smallest honest next implication is now sharper: build an all-prime/all-bias potential whose compensation is not reducible to "there exists a safe physical restriction block" for the old read-once base, or exhibit another source-valid gate forcing that new envelope upward.

## 7. Reproduction boundary

`CHECKER.py` performs only the exact decimal arithmetic needed to transfer the certified account03/B15 `F6` endpoint into the margin units used in this report. The mathematical block theorem is analytic and depends only on the cited exact B12/B17 identities.

No novelty or publication-priority claim is made. No benchmark gold, email/Drive data, paid/remote computation, scheduler secrets, or unrelated private data enter this artifact.
