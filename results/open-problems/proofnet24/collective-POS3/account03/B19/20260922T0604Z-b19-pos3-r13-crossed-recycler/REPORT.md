# POS3 account03/B19 — crossed two-channel recycling forces fresh vertices

**Run:** `20260922T0604Z-account03-B19-pos3-boundary-defect`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Target:** every finite nonchain poset of width at most three has an incomparable pair \(p,q\) with
\[
\frac13\le \Pr[p<q]\le \frac23
\]
under the uniform law on all linear extensions.  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14` unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

No induced/deletion law is replaced by a uniform law anywhere below.

## 1. Exact source state consumed

The assigned partner input is account04/B10 r14:

- `proofnet24/collective-POS3/account04/B10/20260922T051259Z-B10-POS3-r14/REPORT.md`
- Git blob `50bac494667235f3630991a512438eac42c30521`.

It proves that the surviving bridged blocker corridor contains a cover \(x\lessdot y\) and an incomparable point \(a\) with
\[
\Pr(x<a)>2/3,\qquad \Pr(y<a)<1/3,\qquad
\Pr(x<a<y)>1/3,
\]
and that a no-balanced candidate must export this heavy cover through at least two external relation-distinguisher channels.

I also apply account02/B10 r13:

- `proofnet24/collective-POS3/account02/B10/B10-20260922T024630Z-pos3-r13/REPORT.md`
- Git blob `e91498f0bb8e28f23aa1cada24e131c27182e0ff`.

Its one-distinguisher theorem says that an incomparable pair with at most one relation distinguisher is balanced. Equivalently, in a no-balanced poset every incomparable pair has at least two distinguishers.

A newer compatible account02/B10 handoff, `POS3-HANDOFF-account02-B10-20260922T0548Z.md` (brain blob `f3d03c80c2f81c92c98bcc7c1d7b3b860adbbb79`), strengthens a canonical second-blocker branch to a Hasse sandwich of mass \(>1/2\) and identifies simultaneous witness recycling as the unpaid global step.

The exact finite calibration also uses account03/B11's current middle-heavy-fibre output, brain blob `93f2313339cb2f0be56218aefe6800f4c3bbc2d7`, which preserves true insertion multiplicities and shows that blocker-free heavy fibres exist; hence the argument below deliberately avoids any fibrewise-uniform shortcut.

## 2. Relation notation

For incomparable \(p,q\), let
\[
D(p,q)=\{v\notin\{p,q\}:\operatorname{rel}(v,p)\ne\operatorname{rel}(v,q)\},
\]
where `rel` is one of \(v<p\), \(v\parallel p\), \(p<v\).

Consider the exact-two crossed configuration
\[
x\lessdot y,\qquad a\parallel x,y
\]
whose two external witnesses are exactly \(c,u\):
\[
\bigl(D(x,a)\setminus\{y\}\bigr)\cup
\bigl(D(y,a)\setminus\{x\}\bigr)=\{c,u\}.                 \tag{2.1}
\]
Assume, after the available order-dual/reversal symmetry, the crossed relations
\[
c\parallel x,\quad c<a,\quad c<y,                       \tag{2.2}
\]
\[
x<u,\quad a<u,\quad y\parallel u.                       \tag{2.3}
\]
In particular \(c<u\).

This is precisely the five-vertex crossed core that can carry the two-channel heavy-cover exit; the theorem below says it cannot recycle on a fixed local vertex set.

## 3. Crossed-recycler escalation theorem

### Theorem 3.1

Let \(P\) be a finite width-at-most-three poset with **no** balanced incomparable pair, and suppose (2.1)--(2.3) hold. Put
\[
C=\{x,y,a,c,u\},
\]
\[
L=(D(c,x)\setminus\{a\})\setminus C,\qquad
R=(D(y,u)\setminus\{a\})\setminus C.                    \tag{3.1}
\]

Then:

1. \(L\ne\varnothing\) and \(R\ne\varnothing\).
2. Every shared recycler \(r\in L\cap R\) satisfies
   \[
   r\parallel x,y,a,\qquad c<r<u.                       \tag{3.2}
   \]
3. The set \(L\cap R\) is a chain.
4. Either \(L\cup R\) contains at least two distinct vertices, or \(L=R=\{r\}\). In the latter case \(a\parallel r\), none of the five old core vertices distinguishes \(a\) from \(r\), and therefore
   \[
   |D(a,r)\setminus(C\cup\{r\})|\ge2.                   \tag{3.3}
   \]
   Thus the singleton-recycler case actually forces at least **three** vertices outside the old five-vertex core: \(r\) plus two new distinguishers of \((a,r)\).

Consequently an exact-two crossed heavy-edge state cannot form a closed two-channel loop on five or six vertices in a no-balanced POS3 candidate. It must either split to two distinct fresh side witnesses, or coalesce at a neutral bridge point and immediately branch again through at least two further vertices.

### Proof

Inside the five-vertex core, the incomparable pair \(c\parallel x\) has exactly one core distinguisher, namely \(a\). Indeed, \(y\) lies above both \(c,x\), while \(u\) lies above both \(c,x\). Since \(P\) has no balanced pair, the inherited one-distinguisher theorem implies that \(D(c,x)\) has at least two vertices. Hence there is a distinguisher outside the core, so \(L\ne\varnothing\).

Similarly, \(y\parallel u\). Inside the core, \(a\) is its only distinguisher: both \(c\) and \(x\) lie below \(y,u\). The same theorem gives \(R\ne\varnothing\). This proves item 1.

Now let \(r\in L\cap R\). Because \(r\notin C\) and (2.1) says that \(c,u\) are the **only** external distinguishers of the two heavy-cover endpoint pairs, \(r\) distinguishes neither \((x,a)\) nor \((y,a)\). Therefore
\[
\operatorname{rel}(r,x)=\operatorname{rel}(r,a)
=\operatorname{rel}(r,y).                                  \tag{3.4}
\]
There are only three common statuses.

If \(r\) is above all three \(x,a,y\), then \(c<a<r\), so \(r\) is above \(c\) as well as above \(x\). It cannot distinguish \(c\) from \(x\), contradiction.

If \(r\) is below all three, then \(r<a<u\), so \(r\) is below \(u\) as well as below \(y\). It cannot distinguish \(y\) from \(u\), contradiction.

Hence the common status in (3.4) is incomparability:
\[
r\parallel x,a,y.                                          \tag{3.5}
\]
Because \(r\) distinguishes \(c\) from \(x\) and is incomparable with \(x\), it must be comparable with \(c\). The alternative \(r<c\) would give \(r<c<a\), contradicting \(r\parallel a\); therefore \(c<r\). Likewise, because \(r\) distinguishes \(y\) from \(u\) and is incomparable with \(y\), it is comparable with \(u\). The alternative \(u<r\) would give \(a<u<r\), contradicting \(a\parallel r\); therefore \(r<u\). This proves (3.2).

If two shared recyclers \(r,s\in L\cap R\) were incomparable, then
\[
\{x,a,r,s\}
\]
would be a four-element antichain, because \(x\parallel a\) and every shared recycler is incomparable with both \(x,a\). Width at most three forbids this. Hence \(L\cap R\) is a chain, proving item 3.

If \(|L\cup R|\ge2\), item 4 is already in its first alternative. Otherwise nonemptiness gives \(L=R=\{r\}\), and (3.2) holds. Compare \(a\) and \(r\) against the old core:
- \(x\parallel a,r\);
- \(y\parallel a,r\);
- \(c<a,r\);
- \(a,r<u\).

Thus none of \(x,y,c,u\) distinguishes \(a\) from \(r\). Since \(a\parallel r\), if at most one vertex outside \(C\cup\{r\}\) distinguished them, the inherited one-distinguisher theorem (including the zero-distinguisher \(1/2\) case) would make \((a,r)\) balanced. This contradicts the no-balanced hypothesis. Therefore at least two such vertices exist, proving (3.3). `square`

## 4. Why this pays a real part of the global recycling obligation

The partner's r14 first missing step was to show that the two witness channels forced by a \(>E/3\) heavy cover cannot recycle forever.

Theorem 3.1 proves a strict local escalation for the exact-two crossed branch:

- the two channels cannot terminate at the crossed five-core;
- if they remain distinct, at least two outside vertices are already active;
- if they merge, the merger is forced into the one-dimensional neutral corridor \(c<r<u\), and the new pair \((a,r)\) has **zero old-core distinguishers**, so no-balance forces two further outside distinguishers;
- all possible shared mergers are linearly ordered by width three.

Thus “reuse both channels through one old vertex” is impossible. A continuation must consume fresh relation structure. What is **not** yet proved is the final global non-reuse theorem: vertices introduced at different generations might still be reused in a larger cycle, and one must show that such reuse causes span descent, a four-antichain, an autonomous/ordinal reduction, or an actual balanced pair.

This is the next exact obligation, not a claim that POS3 is solved.

## 5. Exact ideal-state census and sharpness calibration

I executed an independent exact-arithmetic enumerator over every distinct naturally-labelled transitive closure on \(n=2,\dots,6\), retaining width at most three and at least two linear extensions.

For each poset it enumerates all linear extensions exactly, finds strong cover flips
\[
x\lessdot y,\quad a\parallel x,y,\quad
3N(x<a)>2E,\quad 3N(y<a)<E,
\]
computes the external witness union (2.1), and tests all local incomparable pairs in the five-vertex core.

The exact output is:

```text
n  width<=3 nonchains  strong flips  exact-two flips  exact-two/no-local-balance
2  1                   0             0                0
3  6                   0             0                0
4  38                  0             0                0
5  313                 85            85               0
6  3338                2386          1042             26
```

All 26 six-point exact-two/no-local-balance configurations have exactly 26 linear extensions and, up to the stated orientation symmetries, have the crossed relations (2.2)--(2.3). In every one, the sole sixth vertex \(r\) is the shared recycler from Theorem 3.1:
\[
r\parallel x,y,a,\qquad c<r<u,
\]
and \((a,r)\) is exactly balanced with count \(13/26\).

A canonical example has covers
\[
0<4,\ 0<5,\ 1<2,\ 1<3,\ 1<5,\ 2<4,\ 3<4,
\]
with
\[
(x,y,a,c,u,r)=(0,5,2,1,4,3),
\]
and exact counts
\[
N(x<a)=19,\quad N(y<a)=7,\quad N(a<r)=13,\quad E=26.
\]

This finite census is **not** the proof of Theorem 3.1 and is not a universal POS3 proof. It is a regression/sharpness certificate: six vertices are enough to realize the singleton shared-recycler geometry, but then the newly created pair is forced to balance; a hypothetical no-balanced continuation must genuinely import further vertices exactly as Theorem 3.1 says.

Verifier:
- `verify_pos3_crossed_recycler.py`
- executed SHA-256 `83e85424786937667b8b85c1c1385181507aa8239d6ef0d443941b798dd2c1dd`
- output SHA-256 `c24b6686296b15e5a87108647d68c8c321e9de17fa682ee39b10298ce579f749`
- terminator `POS3_B19_CROSSED_RECYCLER_CENSUS_PASS`.

## 6. First remaining implication

**GLOBAL RECYCLER ACYCLICITY.** In a cardinality-minimal width-three no-balanced candidate, start from the partner's \(>E/3\) heavy bridge cover (or account02/B10's \(>E/2\) second-blocker sandwich), pass to its two required distinguisher channels, and apply Theorem 3.1 whenever the exact-two crossed pattern occurs. Prove that vertices created by successive split/merge steps cannot be reused in a directed cycle of relation-distinguisher states without forcing at least one of:

1. a balanced incomparable pair;
2. strict strong-majority span descent;
3. a four-antichain;
4. a proper autonomous nonchain / ordinal reduction; or
5. a non-crossed multi-distinguisher exit carrying the target-scale signed charge.

The new theorem removes the stationary local-loop case: every crossed recycling step either increases the active outside-vertex set by at least two or creates a neutral merger that itself forces two more external distinguishers.

## 7. Claim ledger

**Proved this run:** Theorem 3.1, conditional only on the exact crossed-core relations and the previously proved one-distinguisher theorem. The proof is arbitrary-size and uses the original poset relations only.

**Exact computation:** exhaustive \(n\le6\) ideal-state census above.

**Not proved:** global recycler acyclicity; boundary realization for every non-crossed exit; POS3 itself.

**No claim made:** novelty/priority, movement of the `n_bal=14` finite frontier, uniformity of any deletion-induced law, or verified brain use.
