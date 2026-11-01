# B16 FEI campaign-A adversary — recursive-majority terminal rows and exact critical descent

**Run:** `20260921T231428Z-fleet04-B16-fei-interfaceC-r14`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Status:** **PARTIAL / ESSENTIAL_STEP_APPLIED on one exact adversarial family. Full uniform-cube FEI remains OPEN / NOT PROVED.**

## 0. Why this run changed assignment

The invocation began from the older B16 interface-C prompt. Fresh common control then exposed the later owner execution reset
`FEI-PROOF-EXECUTION-20260921T230620Z`, which explicitly supersedes conflicting FEI duties and assigns
**fleet04/B16 to campaign A**:

> construct adversarial joint-derivative examples against A's proposed coverage/exception estimate, then attempt a source-valid repair.

I therefore did not continue the older interface-C source-to-flag calculation.

The exact other-account candidate consumed here is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260921T2205Z-folded-cooling-compiler/REPORT.md`,
blob `9f2bb40584be20e5e440e7f3913873c34858bc91`.

It defines
\[
\mathcal F(f)=H(f)-\mathcal C(f),\qquad
\mathcal C(f)=\sum_i\mathfrak j(j_i),
\]
and, for \(\lambda=0\), its critical object is the physical-restriction ratio \(\mathcal F/J\).
Its conditional compiler requires a physical crossing certificate on every nonconstant restriction-maximal core above
the fixed threshold.  The current paid branch is supplied by

`fleet04/B14/20260921T221102Z-recursive-certified-peeling/REPORT.md`,
blob `253268f70202891aa12c36d2ff4cf76519fa8241`:

a maximum-influence derivative support \(E_i\) is certifiable when it is within
\[
e\le \frac{2^{-r}}{16r}
\]
of a codimension-\(r\) coordinate subcube.  The residual class is the negation of this condition for every maximum row.

The quantitative derivative notation below matches
`fleet04/B13/20260921T2225Z-proxy-gauge-closure/REPORT.md`
(blob `1ec1555932e690e403f7d4320640040628697b96`):
\[
d_i=\sum_{k\ne i}\|D_k g_i\|_2^2,\qquad
\Delta_i=\frac{d_i}{j_i}-\frac12\log_2\frac1{j_i}.
\]

## 1. Exact adversary: recursive ternary majority is terminal for the current near-subcube policy

Let \(M_0(x)=x\), and recursively
\[
M_d=\operatorname{Maj}_3(M_{d-1}^{(1)},M_{d-1}^{(2)},M_{d-1}^{(3)})
\]
on three disjoint copies.  Every physical leaf has influence
\[
j_d=2^{-d},
\]
so
\[
J(M_d)=I(M_d)=3^d2^{-d}=\left(\frac32\right)^d.
\]
The standard balanced-majority Fourier decomposition
\[
\operatorname{Maj}_3(a,b,c)=\frac{a+b+c-abc}{2}
\]
gives
\[
H(M_d)=2+\frac32H(M_{d-1})
      =4\left[\left(\frac32\right)^d-1\right],
\]
hence
\[
\frac{H(M_d)}{J(M_d)}
=4\left[1-\left(\frac23\right)^d\right]\longrightarrow 4.
\]

Fix a leaf \(i\).  On the root-to-leaf path let \(B_\ell\) be the event that the two sibling subtree outputs at level
\(\ell\) disagree.  Those sibling regions are pairwise disjoint across levels, each output is balanced, and therefore
the \(B_\ell\) are independent with probability \(1/2\).  The exact sensitivity support is
\[
E_i=\bigcap_{\ell=1}^d B_\ell,
\qquad
\mu(E_i)=2^{-d}=j_d.
\]

### Theorem 1 — every coordinate-subcube certificate fails

For every codimension-\(r\) coordinate subcube \(Q\) in the sensitivity domain of \(i\),
\[
\boxed{\mu(E_i\triangle Q)>\frac{2^{-r}}{16r}.}
\]

If \(r\ne d\), density mismatch alone gives the result:
\[
\mu(E_i\triangle Q)\ge |2^{-d}-2^{-r}|,
\]
which is at least \(2^{-r}/2\) when \(r<d\), and at least \(2^{-r}\) when \(r>d\).

Now take \(r=d\).  A fixed coordinate can lie in only one of the disjoint sibling regions defining the \(B_\ell\).
For conditioning on \(Q\) to change the probability of \(B_\ell\) away from exactly \(1/2\), \(Q\) must fix at least
one coordinate in **each** of the two sibling blocks at that level.  Thus each affected level costs at least two of
the \(d\) fixed coordinates, and at most \(\lfloor d/2\rfloor\) levels can be affected.  Conditional independence of
the disjoint level regions then yields
\[
\Pr(E_i\mid Q)\le 2^{-\lceil d/2\rceil}.
\]
Since \(\mu(Q)=\mu(E_i)=2^{-d}\),
\[
\boxed{
\mu(E_i\triangle Q)
\ge
2^{1-d}\left(1-2^{-\lceil d/2\rceil}\right)
>
\frac{2^{-d}}{16d}.
}
\]
The last inequality has margin factor
\(32d(1-2^{-\lceil d/2\rceil})\ge16\).

Therefore **the root \(M_d\) is already a terminal node for the current B14 near-subcube peeling rule**, despite
\(H/J\to4\).  Terminality by itself is not a low-complexity conclusion.

## 2. Exact joint-derivative depth: the obvious exception bank is superlinear

For the same leaf \(i\), \(g_i=D_iM_d\) is the indicator of \(E_i\), up to the fixed monotone orientation.  Variables
from level \(\ell\)'s sibling region can change \(E_i\) only when all other \(B_m\) hold.  The disagreement event
\(B_\ell\) has total influence
\[
I(B_\ell)=2I(M_{\ell-1})=2\left(\frac32\right)^{\ell-1}.
\]
Using \(\|D_k1_E\|_2^2=\frac14\operatorname{Inf}_k(1_E)\) and the factor
\(2^{-(d-1)}\) from the other level events,
\[
\frac{d_i}{j_i}
=
\sum_{\ell=1}^d\left(\frac32\right)^{\ell-1}
=
2\left[\left(\frac32\right)^d-1\right].
\]
Consequently
\[
\boxed{
\Delta_i
=
2\left[\left(\frac32\right)^d-1\right]-\frac d2.
}
\]
All leaves are symmetric, so the fleet04/B13 defect bank satisfies
\[
\boxed{
\frac{\mathcal D(M_d)}{J(M_d)}
=
\Delta_i
\longrightarrow\infty,
\qquad
\mathcal D:=\sum_i j_i\Delta_i.
}
\]

This is an exact adversary to the tempting repair
“terminal separation can simply be paid by \(\mathcal D=O(J)\).”
It does **not** refute FEI and does not refute the peer stability theorem, which never asserted such a global bound.

## 3. Source-valid repair: exact ternary-majority factors cannot survive an \(\mathcal F/J\)-critical descent

The adversary has additional Boolean structure that a restriction-maximal proof is allowed to exploit.

### Theorem 2 — balanced ternary-majority critical descent

Let \(g:\{\pm1\}^m\to\{\pm1\}\) be any nonconstant balanced Boolean function, and let \(g_1,g_2,g_3\) be disjoint copies.
Set
\[
F=\operatorname{Maj}_3(g_1,g_2,g_3).
\]
Choose any input \(z\) with \(g(z)=-1\) and physically fix the entire third block to \(z\).  The resulting proper
restriction is
\[
R=\operatorname{AND}_2(g_1,g_2)
\]
in the \(\pm1\) convention.

Then every surviving coordinate has influence exactly one half of its influence in \(g\).  Hence all those influences
are at most \(1/2\), so folded and ordinary influence agree:
\[
J(F)=I(F)=\frac32I(g),\qquad
J(R)=I(R)=I(g).
\]
Because \(\widehat g(\varnothing)=0\), the single-copy and triple-product Fourier channels in
\[
F=\frac{g_1+g_2+g_3-g_1g_2g_3}{2}
\]
are disjoint.  Thus
\[
H(F)=2+\frac32H(g).
\]
Likewise
\[
R=\frac{-1+g_1+g_2+g_1g_2}{2}
\]
has four disjoint Fourier channels and
\[
H(R)=2+H(g).
\]

Now use the **actual additive coordinate correction** from the fleet01/B18 candidate.  Write
\[
A_g:=\sum_{i=1}^m\mathfrak j\!\left(\frac{\operatorname{Inf}_i(g)}2\right).
\]
Then
\[
\mathcal C(F)=3A_g,\qquad \mathcal C(R)=2A_g.
\]
Therefore, for the \(\lambda=0\) candidate \(\mathcal G_0=\mathcal F=H-\mathcal C\),
\[
\boxed{
\frac{\mathcal F(R)}{J(R)}
-
\frac{\mathcal F(F)}{J(F)}
=
\frac{2}{3I(g)}
>0.
}
\]

No special property of \(\mathfrak j\) is used beyond the candidate's coordinate-additive form; the correction cancels
exactly in the ratio difference.  Thus **no exact balanced three-copy ternary-majority composite can be a
physical-restriction maximizer of \(\mathcal F/J\)**.

For \(g=M_{d-1}\), the improvement is
\[
\boxed{
\frac{\mathcal F(R_d)}{J(R_d)}
-
\frac{\mathcal F(M_d)}{J(M_d)}
=
\left(\frac23\right)^d.
}
\]
So the same recursive-majority family that is maximally hostile to the current near-subcube terminal condition is
removed exactly by the critical-core quantifier of the \(\lambda=0\) fleet01/B18 compiler.

## 4. What this changes in the compact A proof chain

The surviving conditional chain can now be narrowed honestly.

1. Fleet01/B18 gives a complete conditional FEI compiler from a universal physical certificate on every
   \(\mathcal F/J\)-restriction-maximal core (take \(\lambda=0\)).
2. Fleet04/B14 pays and recursively removes every maximum row satisfying the sharp
   \(e\le2^{-r}/(16r)\) near-subcube condition.
3. The present Theorem 1 shows terminality alone is insufficient: recursive majority is terminal and has an
   unbounded normalized positive-depth defect bank.
4. The present Theorem 2 repairs that exact obstruction at the correct source level: recursive majority, and more
   generally every exact balanced three-copy ternary-majority factor, is excluded from the \(\mathcal F/J\)-critical
   residual by a proper physical restriction with a strictly larger ratio.

The **remaining universal implication** is now:

> prove that every nonconstant \(\mathcal F/J\)-restriction-maximal core above the compiler threshold either has a
> B14-certifiable near-subcube maximum row, or admits another source-valid critical descent/certificate.

This report does **not** prove that general dichotomy.  In particular it does not show that every terminal high-defect
core has an exact majority factor, nor that \(\mathcal D=O(J)\).

## 5. Verification

`check_b16_majority_terminal_descent.py` is standard-library only.  A clean `python -S` replay passed:

- 40 exact recursive-majority formula/depth/terminal-bound cases;
- direct truth-table checks for \(M_1,M_2\);
- 10 exhaustive codimension-grouped minimum subcube-distance checks (including all \(3^8-1\) nontrivial
  coordinate subcubes in the 8-coordinate sensitivity domain of a leaf of the 9-variable \(M_2\) case);
- all 8 balanced Boolean base functions in dimensions 1 and 2 for the exact majority-to-AND restriction identities;
- an additional arbitrary nonlinear additive coordinate correction, confirming the exact cancellation mechanism.

The checker SHA-256 is
`b1d1e821a308ec2cdd40a843303e7e1fbc45f308367afb915387c25049598b66`.

## 6. Status

**ESSENTIAL_STEP_APPLIED, structured branch only.**  
A genuine terminal/joint-derivative adversary was found, the naïve defect-bank repair was killed on it, and an exact
source-valid critical-descent repair was proved for the entire balanced self-similar ternary-majority obstruction.
The universal A coverage implication remains open; consequently full FEI remains **OPEN / NOT PROVED**.
