# B12 — all-gate margin envelope for the adaptive shared-core falsifier family

**Outcome:** `ESSENTIAL_STEP_APPLIED` to the current all-gate falsification campaign. The old read-once potential remains `CANDIDATE_REFUTED`. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated private GitHub mathematical sources were consumed directly; no authenticated receiver-context/full-brain retrieval was used.

## 1. Exact live target and source versions

The live owner target is the all-gate formulation

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]
for one symmetric nonnegative finite-centre potential \(\Gamma\) and every Boolean gate/bias vector. The current read-once candidate has centre
\[
C_0=\Gamma(1/2)=6.4548.
\]
The source gate-reformulation report is
`continuations/2026-09-22-gate-reformulation/REPORT.md`, blob
`1c0596f786fccf542f1f9ea65cc728b2c21ddef5`.

The two exact other-account inputs used here are:

1. `account03/B15/20260922T002607Z-readonce-gamma-counterexample/REPORT.md`, blob
   `e49efe403698395b700278d067c245c12a7b15eb`. It proves the balanced-uniform margin identity
   \[
   c_G=4\left(\frac{H(G)}{I(G)-1}-C_0\right)
   \tag{1.1}
   \]
   and applies it to the source-valid balanced 18-input gate.
2. `account04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`, blob
   `f5347c63a8ab43f9c6a4b58850643b69bc50d551`. It proves a global ceiling for the entire source-valid adaptive integer-depth nine-host shared-core construction, including history-dependent depth choices.

I apply both theorems below; they are not merely cited.

## 2. Balanced gates collapse the potential shape to its centre

Let \(G\) be balanced and feed it unbiased independent inputs. Then
\(p_{\rm out}=1/2\), \(V_{1/2}=1\), and \(h(1)=0\). Hence (G) becomes
\[
C_0+H(G)\le C_0 I(G).
\]
For \(I(G)>1\), put
\[
R(G):=\frac{H(G)}{I(G)-1}.
\]
The gate defect and Poincare currency are exactly
\[
D_G=C_0(I(G)-1)-H(G),
\qquad
Z_G=\frac{I(G)-1}{4}.
\]
Therefore the quadratic correction margin required by this gate is
\[
\boxed{c_G=-\frac{D_G}{Z_G}=4(R(G)-C_0).}
\tag{2.1}
\]
This is the account03/B15 identity, now used as the translation from the adaptive shared-core ratio theorem to the live owner margin units.

In particular, on this balanced-uniform slice the detailed shape of \(\Gamma\) away from \(1/2\) is irrelevant: every such gate imposes only a centre constraint \(C_0\ge R(G)\).

## 3. Apply the new adaptive-depth ceiling

Account04/B15 proves that for the source-valid shared-core construction, where at every round one may choose any integer self-composition depth \(d_r\ge1\) as a function of the entire prior history before applying the fixed nine-host shared-core transform, every resulting finite balanced monotone gate satisfies
\[
R(G)<M_+,
\tag{3.1}
\]
with the rigorous global scalar bound
\[
M_+=6.52185121301287772365150440023918196647146413881.
\tag{3.2}
\]
The same theorem gives the certified lower witness \(F_7\):
\[
R(F_7)>
R_7^-:=6.5218509495504481848401605388605115013503296799038586768578.
\tag{3.3}
\]
The proof of (3.1) is not a finite strategy sweep: the peer rewrites each shared-core step as a convex interpolation between the current ratio and a one-dimensional local target \(K(c^d)/(133/128)\), then proves a global strict-concavity bound for \(K\) and rigorously maximizes it on the entire reachable interval.

Combining (2.1)--(3.3) gives the following family-global margin theorem.

### Theorem 3.1 — adaptive shared-core margin envelope

For the old read-once centre \(C_0=6.4548\), every finite gate obtainable from the current source-valid adaptive-depth shared-core construction satisfies
\[
 c_G
 <4(M_+-C_0)
 =0.26820485205151089460601760095672786588585655524,
\tag{3.4}
\]
while the explicit finite gate \(F_7\) satisfies
\[
 c_{F_7}
 >4(R_7^--C_0)
 =0.2682037982017927393606421554420460054013187196154347074312.
\tag{3.5}
\]
Consequently the supremal margin forced by this entire adaptive-depth construction family is trapped in an interval of width less than
\[
\boxed{1.0538497181552454\times10^{-6}}.
\tag{3.6}
\]
No choice of future integer depths inside this same nine-host geometry can escape the upper endpoint in (3.4).

The current two-input AND correction is about
\(c_{\rm AND}=0.0043974201\). Thus the single certified gate \(F_7\) already asks for more than
\[
\boxed{60.9911703004\,c_{\rm AND}},
\tag{3.7}
\]
and the complete adaptive-depth family can improve that factor only to about \(60.99141\) without changing the host/core geometry.

## 4. Centre-floor consequence for any universal all-gate potential

Let \(\Gamma\) be any symmetric nonnegative potential satisfying (G) for all finite Boolean gates. Applying (G) to every finite member of this balanced family and taking the supremum gives
\[
\Gamma(1/2)\ge \sup_{G\in\mathcal F}R(G).
\tag{4.1}
\]
Hence the explicit finite witness already forces
\[
\boxed{
\Gamma(1/2)>
6.5218509495504481848401605388605115\ldots .
}
\tag{4.2}
\]
At the same time, account04/B15 proves that **this particular adaptive-depth shared-core mechanism alone** cannot force the centre above
\[
6.52185121301287772365150440023918197\ldots
\tag{4.3}
\]
by changing only the self-composition depths.

This is a lower-bound/falsifier statement, not an FEI upper bound: (4.3) says nothing about other Boolean gates, different shared-coordinate geometry, or nonuniform biases.

## 5. Exact old/new missing implication

**Old missing implication (already false):** the read-once value-iteration potential with centre \(6.4548\) satisfies (G) for every gate, equivalently no gate needs more margin than binary AND. Account03/B15 and the earlier prime-gate certificates refute this.

**New implication resolved here:** could the same source-valid shared-core falsifier be made substantially worse merely by choosing self-composition depths adaptively? No. The account04/B15 scalar ceiling, translated by the exact balanced margin identity, gives the uniform family-wide envelope (3.4)--(3.6). The depth-only branch of this falsification mechanism is analytically exhausted.

**Replacement obligation:** any further attempt to raise the all-gate lower floor using this construction must change the shared host/core geometry, the underlying prime gadget, or move to a genuinely biased product point. Merely changing the integer depth schedule cannot materially improve the current lower bound. Conversely, a full proof still requires constructing some finite-centre symmetric nonnegative \(\Gamma\) satisfying (G) for every gate and every bias vector.

## 6. Checks and scope

The decimal translations in (3.4)--(3.7) were recomputed independently at 80 decimal digits from the certified endpoints quoted above. They use only multiplication/subtraction and do not add a numerical hypothesis to the source theorems.

Manual scoped privacy/provenance review of this file: mathematical formulas and private-repository artifact identifiers only; no credentials, scheduler identifiers, machine paths, email/Drive content, benchmark answers, permission changes, or unrelated private data.

**Final classification:** `ESSENTIAL_STEP_APPLIED` to the current falsifier-family analysis; the universal read-once candidate remains `CANDIDATE_REFUTED`; full FEI remains **OPEN / NOT PROVED**.
