# POS3 account03/B19 — same-ray packet exceptions force a new outward distinguisher export

**Run:** `20260922T070336Z-b19-pos3-r11-same-ray-export`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair \(p,q\) with
\[
\frac13\le \Pr[p<q]\le \frac23
\]
under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is for the original uniform law on the full poset. No deletion-induced law is treated as uniform.

## 1. Exact collective state consumed

The assigned other-account partner result is:

- account04/B10 r16,
  `proofnet24/collective-POS3/account04/B10/20260922T064124Z-B10-POS3-r16/REPORT.md`,
  Git blob `78e86dcdaef62417888ef6d8b66bf3b6d062f2c9`.

Its current heavy-cover state is
\[
x\lessdot y,\qquad a\parallel x,y,\qquad x\prec_*a\prec_*y,
\]
inside a hypothetical no-balanced width-three counterexample, after strict strong-majority span descent has been exhausted on the old two subintervals.

Using the canonical Hasse witness families
\[
F_1=\{s:x\lessdot s,\ s\parallel a,\ s\ne y\},
\]
\[
F_2=\{t:t\lessdot a,\ t\parallel x\},
\]
\[
F_3=\{u:a\lessdot u,\ u\parallel y\},
\]
\[
F_4=\{r:r\lessdot y,\ r\parallel a,\ r\ne x\},
\]
r16 proves lossless boundary-anchor recoding: every canonical left-ray mark is charged to an actual pair \((r,x)\), every right-ray mark to an actual pair \((y,r)\), and in its low-endpoint branch there are two distinct fully outward actual pairs, one from each failed-swap side, each carrying more than \(2E/33\) marked full extensions.

Its only same-ray local exception is exact:

- either the two selected blocker vertices are comparable, producing a nested outward channel;
- or they are incomparable, producing a width-saturating three-antichain gate.

Its first unpaid implication is `OUTWARD-STATE RECYCLING`.

I also use the already-consumed other-account one-distinguisher theorem:

- account02/B10: in a no-balanced width-three poset, every incomparable pair has at least two relation distinguishers; equivalently, an incomparable pair with at most one relation distinguisher is balanced.

The present run attacks exactly r16's same-ray exception, rather than reopening a generic recycling formulation.

## 2. Compact route and new statement

Suppose the two r16 packets land on the same **right** ray. Then the left-swap packet vertex must be some
\[
s\in F_1
\]
and the right-swap packet vertex some
\[
u\in F_3.
\]
Thus
\[
x\lessdot s,\qquad a\lessdot u,\qquad
s\parallel a,y,\qquad u\parallel y,
\]
and r16 gives
\[
y\prec_*s,\qquad y\prec_*u.
\]

There are only two cases.

1. **Nested:** \(s,u\) are comparable. Necessarily \(s<u\).
2. **Width-saturating:** \(s\parallel u\), so \(\{y,s,u\}\) is a three-antichain.

The theorem below shows that neither case can be a closed local recycler in a no-balanced poset. The nested case forces at least one new distinguisher outside the current five-vertex core; the width-saturating case forces at least two. Moreover, unless a permitted strict span descent has already occurred, every such required distinguisher lies beyond the current same-ray envelope, strictly before \(x\) or strictly after \(s\) in the strong-majority order.

The order-dual statement handles the same-left-ray case.

## 3. Same-ray outward-export theorem

Let
\[
C=\{x,y,a,s,u\}.
\]

### Theorem 3.1 — nested right-ray packets cannot close locally

Assume \(s\in F_1\), \(u\in F_3\), and \(s,u\) are comparable. Then:

1. necessarily \(s<u\);
2. for the incomparable pair \(a\parallel s\), the **only** relation distinguisher inside \(C\) is \(x\);
3. therefore, in a no-balanced poset, there exists
   \[
   z\notin C
   \]
   distinguishing \(a\) from \(s\);
4. for every such \(z\), at least one of the following holds:
   - \(z\prec_*x\);
   - \(s\prec_*z\);
   - there is a strict strong-majority incomparable subspan of one of the active intervals \((x,a)\) or \((a,s)\).

Hence, after excluding the already-authorized span-descent termination, the nested same-ray gate exports a genuinely external relation distinguisher strictly beyond the current strong-order envelope \([x,s]\).

#### Proof

If \(u<s\), then
\[
a<u<s,
\]
contradicting \(a\parallel s\). Hence \(s<u\).

Now compare \(a\) and \(s\) against the other three core vertices.

- \(x\parallel a\) but \(x<s\), so \(x\) distinguishes \(a,s\).
- \(y\parallel a\) and \(y\parallel s\), so \(y\) does not distinguish them.
- \(u\) is above both, because \(a<u\) and \(s<u\), so \(u\) does not distinguish them.

Thus
\[
D(a,s)\cap C=\{x\}.
\]
The one-distinguisher theorem now forces at least one additional \(z\notin C\) distinguishing \(a,s\).

Because \(a\parallel s\), a relation distinguisher \(z\) can only have one of four noncontradictory forms:

\[
\text{(N1)}\ z<a,\ z\parallel s;
\quad
\text{(N2)}\ z\parallel a,\ z<s;
\]
\[
\text{(N3)}\ a<z,\ z\parallel s;
\quad
\text{(N4)}\ z\parallel a,\ s<z.
\]

For (N1), \(x<z\) would imply \(x<z<a\), contradicting \(x\parallel a\), while \(z<x\) would imply \(z<x<s\), contradicting \(z\parallel s\). Hence \(z\parallel x\). Since \(z<a\), we have \(z\prec_*a\). If \(x\prec_*z\), then \((x,z)\) is a strict incomparable subspan of \((x,a)\); otherwise \(z\prec_*x\).

For (N2), the cover \(x\lessdot s\) rules out \(x<z<s\). Thus either \(z<x\), which gives \(z\prec_*x\), or \(z\parallel x\). In the latter case, if \(x\prec_*z\prec_*a\), then \((x,z)\) is a strict subspan of \((x,a)\); if \(a\prec_*z\prec_*s\), then \((a,z)\) is a strict subspan of \((a,s)\). With neither descent, one must have \(z\prec_*x\).

For (N3), \(a<z\) gives \(a\prec_*z\). If \(z\prec_*s\), then \((z,s)\) is a strict incomparable subspan of \((a,s)\). Otherwise \(s\prec_*z\).

For (N4), \(s<z\) directly gives \(s\prec_*z\).

This proves the stated trichotomy. \(\square\)

### Theorem 3.2 — width-saturating right-ray packets force two outward exports

Assume instead
\[
s\parallel u.
\]
Then:

1. \(\{y,s,u\}\) is a width-saturating three-antichain;
2. for the incomparable boundary pair \(y\parallel s\), **no** vertex of \(C\) distinguishes \(y\) from \(s\);
3. therefore a no-balanced poset contains at least two distinct vertices
   \[
   z_1,z_2\notin C
   \]
   distinguishing \(y,s\);
4. every such \(z\) satisfies at least one of:
   - \(z\prec_*x\);
   - \(s\prec_*z\);
   - a strict strong-majority incomparable subspan occurs inside one of
     \((x,a)\), \((a,y)\), or \((y,s)\).

Hence, after span-descent termination is excluded, the width-saturating same-ray gate exports **two** relation distinguishers beyond the current strong-order envelope.

#### Proof

The three-antichain statement is r16's same-ray alternative.

For the pair \(y,s\):

- \(x\) lies below both because \(x\lessdot y\) and \(x\lessdot s\);
- \(a\parallel y,s\);
- \(u\parallel y,s\) in the present case.

Thus
\[
D(y,s)\cap C=\varnothing.
\]
If there were at most one distinguisher outside \(C\), the one-distinguisher theorem would make \(y,s\) balanced. Therefore at least two distinct outside distinguishers exist.

For any one such \(z\), the possible relation types are

\[
\text{(S1)}\ z<y,\ z\parallel s;
\quad
\text{(S2)}\ z\parallel y,\ z<s;
\]
\[
\text{(S3)}\ y<z,\ z\parallel s;
\quad
\text{(S4)}\ z\parallel y,\ s<z.
\]

For (S1), the cover \(x\lessdot y\) rules out \(x<z<y\). Also \(z<x\) would imply \(z<x<s\), contradicting \(z\parallel s\). Hence \(z\parallel x\). Since \(z\prec_*y\), if \(x\prec_*z\), then relative to
\[
x\prec_*a\prec_*y
\]
either \(z\prec_*a\), making \((x,z)\) a strict subspan of \((x,a)\), or \(a\prec_*z\), in which case \(a<z\) is impossible because \(z<y\) and \(a\parallel y\); hence \(a\parallel z\) and \((a,z)\) is a strict subspan of \((a,y)\). Without descent, \(z\prec_*x\).

For (S2), the cover \(x\lessdot s\) rules out \(x<z<s\). If \(z<x\), then \(z<y\), contradicting \(z\parallel y\); hence either \(z\parallel x\) or the case is impossible. If \(x\prec_*z\), then according to the location of \(z\) in
\[
x\prec_*a\prec_*y\prec_*s,
\]
one gets respectively a strict subspan \((x,z)\subset(x,a)\), \((z,y)\subset(a,y)\), or \((y,z)\subset(y,s)\). Therefore without descent \(z\prec_*x\).

For (S3), \(y<z\) gives \(y\prec_*z\). If \(z\prec_*s\), then \((z,s)\) is a strict subspan of \((y,s)\); otherwise \(s\prec_*z\).

For (S4), \(s<z\) gives \(s\prec_*z\).

Thus every compulsory outside distinguisher either produces an accepted strict descent or lies beyond the current envelope. \(\square\)

### Corollary 3.3 — same-ray local recycling is eliminated

In the r16 low-endpoint branch, if the two \(>2E/33\) boundary packets choose the same ray, then the process cannot close using only the old heavy-edge core and the two packet vertices.

On the right:

- nested packets force at least one external distinguisher of \((a,s)\);
- width-saturating packets force at least two external distinguishers of \((y,s)\).

The dual statement holds on the left.

After strict span descent is excluded, the required vertices occur strictly outside the current same-ray strong-order envelope. Therefore the remaining `OUTWARD-STATE RECYCLING` problem is narrower: a genuine cycle must reuse a vertex that was exposed in an **earlier, larger envelope** or must alternate between opposite outer rays. A same-ray state cannot recycle entirely inside its own present envelope.

This is the new applied structural step.

## 4. Why exact counting is still needed: local balance closure is false

A tempting stronger shortcut would say that either same-ray exception already forces one of the obvious local pairs to be balanced. That is false.

I constructed two exact width-three counterexamples to this stronger **local** claim. They are not counterexamples to POS3; each has balanced pairs elsewhere.

The verifier enumerates every linear extension of the listed posets exactly.

### 4.1 Nested same-ray witness

Take the eight-element poset with Hasse covers
\[
(0,5),(0,7),(1,2),(1,4),(2,5),(3,4),(3,6),(4,7),(5,6)
\]
and state
\[
(x,y,a,s,u)=(1,2,0,4,7).
\]

It has
\[
E=128
\]
linear extensions and satisfies the right nested geometry:
\[
x\lessdot y,\quad x\lessdot s,\quad a\lessdot u,\quad s<u,
\]
with
\[
a\parallel x,y,s,\qquad y\parallel s,u.
\]

The exact key counts are
\[
N(x<a)=89,\qquad N(y<a)=42,
\]
\[
N(y<s)=90,\qquad N(y<u)=120,\qquad N(a<s)=105.
\]

Since
\[
128/3=42\tfrac23,\qquad 2\cdot128/3=85\tfrac13,
\]
all five key pairs are unbalanced in the same directions as the hypothetical no-balanced branch:
\[
\Pr(x<a)>2/3,\quad \Pr(y<a)<1/3,
\]
\[
\Pr(y<s)>2/3,\quad \Pr(y<u)>2/3,\quad \Pr(a<s)>2/3.
\]

For the new nested pair,
\[
D(a,s)=\{1,3,5,6\},
\]
so the unique core distinguisher is indeed \(x=1\), while the exterior structure supplies three more.

Balanced pairs exist elsewhere, for example the exact verifier finds
\[
(0,3):57/128,\quad (1,3):82/128,\quad (4,5):83/128,\quad (6,7):55/128,
\]
all in the target interval after choosing the minority orientation as appropriate.

Thus the nested same-ray core itself does **not** force a local balanced key pair; the external-export theorem is the correct mechanism.

### 4.2 Width-saturating witness and sharp distinguisher count

Take the seven-element poset with Hasse covers
\[
(0,2),(0,3),(0,4),(1,4),(1,5),(2,5),(5,6)
\]
and state
\[
(x,y,a,s,u)=(0,2,1,3,4).
\]

It has
\[
E=62
\]
linear extensions and satisfies
\[
x\lessdot y,\quad x\lessdot s,\quad a\lessdot u,\quad s\parallel u,
\]
with the same required incomparabilities.

The exact key counts are
\[
N(x<a)=42,\quad N(y<a)=18,\quad N(y<s)=45,
\]
\[
N(y<u)=51,\quad N(a<s)=52.
\]

Because
\[
62/3=20\tfrac23,\qquad 2\cdot62/3=41\tfrac13,
\]
again all five local key pairs are outside the balanced interval.

Most importantly,
\[
D(y,s)=\{5,6\}.
\]
Thus the core contributes zero distinguishers and **exactly two** external distinguishers occur. This shows that the "at least two outside distinguishers" conclusion of Theorem 3.2 is sharp at the level of relation-distinguisher count.

The whole poset still has balanced pairs elsewhere, e.g.
\[
(3,4):36/62,\qquad (3,5):34/62,\qquad (4,5):28/62.
\]

So this is a counterexample only to the stronger local-closure shortcut, not to POS3.

## 5. Exact verifier

Artifact:
`verify_pos3_same_ray_export.py`

The verifier:

- rebuilds both posets from their Hasse covers;
- checks width at most three;
- verifies the required cover and incomparability geometry;
- enumerates all full linear extensions exactly;
- verifies the five strong-orientation counts;
- verifies that none of those five local key pairs is balanced;
- computes the relation-distinguisher sets;
- verifies the exact two-distinguisher sharpness in the saturated witness;
- confirms balanced pairs elsewhere, preventing any accidental POS3-counterexample claim.

Executed SHA-256:
`83a21560cc4d556a32106e2d4ba9ac04f4c69891637ca0f584fd8e56fdd65131`

Captured output SHA-256:
`6e3d7b5d3810e2f521d2e374e962c95a74f919efe3c8436baf7ea3f3701f8bf0`

Terminator:
`POS3_B19_SAME_RAY_EXPORT_CERTIFICATE_PASS`.

## 6. First remaining implication

The r16 `OUTWARD-STATE RECYCLING` obligation is now reduced further.

The **same-ray present-envelope closure** is paid by Theorems 3.1-3.2. The surviving first global implication is:

> **CROSS-ENVELOPE REUSE EXCLUSION.** In a cardinality-minimal no-balanced width-three poset, follow the r16 two-packet boundary recoding. Whenever both packets choose one ray, apply Theorems 3.1-3.2 to export beyond the current envelope unless span descent occurs. Prove that a compulsory exported distinguisher cannot be a vertex from an earlier, strictly larger envelope in such a way that the process alternates left/right and forms a finite reuse cycle. Any such attempted reuse must force one of: a balanced pair, strict span descent, a four-antichain, a proper autonomous/ordinal reduction, or a non-crossed multi-distinguisher exit carrying the exact packet charge.

The key point is that the unresolved cycle can no longer be purely same-ray and local. It must cross an earlier envelope boundary or alternate rays. That is a strictly narrower global obstruction than r16.

## 7. Claim ledger

**Consumed/applied**
- account04/B10 r16 boundary-anchor recoding, two \(>2E/33\) outward packets, and same-ray nested/three-antichain dichotomy;
- account02/B10 one-distinguisher theorem.

**Proved this run**
- nested same-right-ray packet pair has exactly one core distinguisher for \((a,s)\), so no-balance forces an external distinguisher;
- width-saturating same-right-ray packet pair has zero core distinguishers for \((y,s)\), so no-balance forces at least two external distinguishers;
- each compulsory distinguisher either lies beyond the current same-ray strong-order envelope or yields an accepted strict span descent;
- order-dual same-left-ray statements;
- same-ray local recycling inside the current envelope is therefore excluded.

**Exact computation**
- one \(n=8\), \(E=128\) nested witness refuting the stronger local-balance shortcut;
- one \(n=7\), \(E=62\) width-saturating witness with exactly two external distinguishers, showing sharpness of Theorem 3.2's distinguisher count.

**Not proved**
- cross-envelope reuse exclusion;
- arbitrary global recycling termination;
- POS3.

No novelty/priority claim is made. No finite nonviolation is treated as a proof. No induced law is treated as uniform.
