# POS3 account02/B11 r17 — an incomparability leaf cannot be a terminal ray state

**Run:** `20260922T065006Z-b11-pos3-r17-50176f59`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent status:** **OPEN / NOT PROVED**  
**Target:** every finite nonchain poset of width at most three has an incomparable pair \(p,q\) with
\[
\frac13\le \Pr[p<q]\le \frac23
\]
under the uniform law on all full linear extensions.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are for the original uniform law on full linear extensions of the stated poset. No deletion-induced law is silently replaced by a uniform law.

## 1. Fresh source state and conditional route

Fresh owner controls were resolved at `yspennstate/math-research-brain` commit
`77352e264285d13126b74509a70920fe48b9c4d1`, OWNER CONTROL revision
`2026-09-22.2`. The collective POS3 allocation remains active.

The latest complete campaign-lead result consumed is account04/B10 r15:

- `proofnet24/collective-POS3/account04/B10/20260922T061407Z-B10-POS3-r15/REPORT.md`
- science commit `0c95533fce3b4870b16ede500442a0209df3d9b6`
- blob `b0864fe6d45a6285e0226b3eec10a2272a8eeae1`.

It reduces the no-span-descent heavy-cover branch to `RAY-RETURN EXCLUSION`: an exact
active-defect packet is forced onto one of the two outer strong-majority rays, and
local interior absorption is impossible.

The latest complete named-partner result consumed is account03/B19 r13:

- `proofnet24/collective-POS3/account03/B19/20260922T0604Z-b19-pos3-r13-crossed-recycler/REPORT.md`
- science commit `ad387a28ee5b6fc514a29662ea5de50d784473f1`
- blob `6dc132cfb4ecfa6f50ffc0462dc1e0b06ea4c90b`.

It proves that an exact-two crossed heavy-edge state cannot close on a fixed
five- or six-vertex two-channel loop: its two channels either split to distinct
fresh witnesses or merge at a neutral recycler that itself forces at least two
further distinguishers.

The immediately preceding B11 leaf-splice result is source-bound by brain blob
`0c52dae4db6c14fed1f69e843ee37ca5e11ffc62`. The earlier B11 double-fan dual-corridor
result is source-bound by brain blob `4fe4f0f42bb8326c0aadd8a53e934ca481b04eda`
and science report blob `9b19bb38b080134c704f5d09bc53a77d3d4105d0`.

The conditional end-to-end route is therefore:

1. use the already-proved series/parallel reductions to work in a width-exactly-three,
   ordinally and parallel indecomposable minimal counterexample;
2. use the lead heavy-cover theorem and strong-majority span descent to reach the
   outward-ray recycling obligation;
3. **new here:** if such a strong-majority state ever lands at an endpoint which is
   an incomparability-graph leaf, it cannot terminate there: in the no-balanced,
   no-span-descent branch it is forced into an exact two-predecessor Hasse fan with
   a real channel of mass strictly between \(1/6\) and \(1/3\);
4. the prior B11 dual-corridor theorem reroutes that fan to a strict successor-chain
   corridor (unless it already gives span descent);
5. if the resulting corridor enters the partner's exact-two crossed configuration,
   account03/B19 r13 forces fresh vertices rather than a local recycler loop.

Thus incomparability leaves are removed as *terminal sinks* for the lead's ray packet.
The remaining global step is still ray-return/recycler acyclicity across successive
corridor and multi-distinguisher states.

## 2. Exact leaf capacities

Let \(x\) be an incomparability-graph leaf, with unique incomparable neighbour \(b\).
Put
\[
D=\operatorname{Pred}(x),\qquad U=\operatorname{Succ}(x),
\]
\[
L=P[D\cup\{b\}],\qquad R=P[U\cup\{b\}],
\]
and abbreviate
\[
d=e(D),\quad u=e(U),\quad \ell=e(L),\quad r=e(R).
\]

As proved in the preceding B11 run, the two orientations of the leaf pair factor
exactly:
\[
N_P(b<x)=\ell u,\qquad N_P(x<b)=dr,\qquad
E=e(P)=\ell u+dr.                                      \tag{2.1}
\]

Define the two insertion capacities
\[
A=\frac{\ell}{d},\qquad B=\frac r u.                   \tag{2.2}
\]
Then
\[
\Pr_P(b<x)=\frac{A}{A+B},\qquad
\Pr_P(x<b)=\frac{B}{A+B}.                              \tag{2.3}
\]

Here \(A,B\ge1\). For example, \(b\) is a maximal element of \(L\): if
\(z\in D\) is comparable with \(b\), then necessarily \(z<b\), since
\(b<z<x\) would contradict \(b\parallel x\). Hence every extension of \(D\)
gives an extension of \(L\) ending in \(b\), so \(\ell\ge d\). The proof
that \(B\ge1\) is dual.

For completeness, the deletion marginal can also be written exactly. If \(Q=P-x\),
the unique extensions of \(Q\) that admit two positions for \(x\) are those with
all of \(D\) before \(b\) and all of \(U\) after \(b\). There are exactly \(du\)
of these, so
\[
e(Q)=\ell u+dr-du=du(A+B-1).                            \tag{2.4}
\]
Thus the induced law on \(L(Q)\) is a one-bit \(1/2\)-multiplicity tilt, not the
uniform law. This identity is used only as a consistency check below; the proof
of the new structural theorem stays in the original full-extension law.

## 3. Delayed predecessors form at most a double Hasse fan

Assume the strong-majority orientation
\[
\Pr_P(b<x)>2/3.                                         \tag{3.1}
\]
By (2.3),
\[
A>2B.                                                   \tag{3.2}
\]

Define the delayed predecessor set
\[
I=D\setminus\operatorname{Pred}(b).
\]
Because \(b<z<x\) is impossible, every \(z\in D\) is either below \(b\) or
incomparable with \(b\). Hence
\[
I=\{z\in D:z\parallel b\}.                              \tag{3.3}
\]

### Lemma 3.1 — upset and width

\(I\) is an upset of \(D\), and \(\operatorname{width}(I)\le2\).

**Proof.** If \(i\in I\) and \(i<z\in D\), then \(z<b\) would imply
\(i<b\), while \(b<z\) would imply \(b<z<x\). Both are impossible, so
\(z\parallel b\), hence \(z\in I\). If \(I\) contained a three-antichain,
adjoining \(b\), which is incomparable with every member of \(I\), would
give a four-antichain in \(P\). `square`

Let
\[
T=\max I.
\]
Then \(|T|\le2\). Moreover every \(t\in T\) is a Hasse predecessor of \(x\):
if \(t<z<x\), then the upset property gives \(z\in I\), contradicting maximality
of \(t\).

### Lemma 3.2 — exact reverse-union mass

Let
\[
V=\bigcup_{t\in T}\{L_{\rm ext}: b<_{L_{\rm ext}}t\}
\]
as an event in the full uniform extension space \(L(P)\). Then
\[
|V|=(\ell-d)u                                           \tag{3.4}
\]
and therefore
\[
\Pr_P(V)=\frac{A-1}{A+B}.                               \tag{3.5}
\]

**Proof.** The event \(b<t<x\) lies entirely in the branch \(b<x\).
Conditioned on that branch, a full extension is exactly an extension of \(L\),
then \(x\), then an extension of \(U\).

Because \(b\) is maximal in \(L\), the extensions of \(L\) ending in \(b\)
are in bijection with \(L(D)\), so exactly \(d\) of the \(\ell\) extensions
end in \(b\). If \(b\) is not last, every element after it belongs to \(I\);
moving upward in the finite upset \(I\) reaches some \(t\in T\), which is
also after \(b\). Conversely \(b<t\) plainly means that \(b\) is not last.
Thus the union over \(T\) is exactly the set of the \(\ell-d\) non-last
extensions of \(L\), each with \(u\) choices on \(U\). This proves (3.4),
and (3.5) follows from \(E=du(A+B)\). `square`

From \(A>2B\) and \(B\ge1\),
\[
3(A-1)-(A+B)=2A-B-3>3(B-1)\ge0,
\]
so
\[
\Pr_P(V)>1/3.                                           \tag{3.6}
\]

## 4. Leaf-terminal exclusion theorem

### Theorem 4.1

Suppose \(P\) has width at most three and no balanced incomparable pair.
Let \(x\) be an incomparability-graph leaf with unique incomparable neighbour
\(b\), and suppose
\[
b\prec_* x
\]
(that is, \(\Pr_P(b<x)>2/3\)). Assume also that the pair \((b,x)\) admits no
strict strong-majority span descent.

Then \(T=\max(\operatorname{Pred}(x)\setminus\operatorname{Pred}(b))\) has
**exactly two** elements \(t_1,t_2\). Both are Hasse predecessors of \(x\),
both are incomparable with \(b\), and
\[
\Pr_P(b<t_i)<1/3\qquad(i=1,2),                          \tag{4.1}
\]
while
\[
\frac13<
\Pr_P\bigl((b<t_1)\cup(b<t_2)\bigr)
<\frac23.                                               \tag{4.2}
\]
Consequently at least one actual Hasse channel satisfies
\[
\frac16<\Pr_P(b<t_i)<\frac13.                           \tag{4.3}
\]

The order-dual statement holds when \(x\prec_*b\), producing an exact
double-successor Hasse fan.

**Proof.** By Lemmas 3.1-3.2, \(|T|\le2\), each \(t\in T\) is a Hasse
predecessor of \(x\), and their union event has probability \(>1/3\).

For any \(t\in T\), the pair \(b,t\) is incomparable and \(t<x\). If
\(\Pr(b<t)\in[1/3,2/3]\), it is balanced, forbidden by hypothesis. If
\(\Pr(b<t)>2/3\), then
\[
b\prec_*t\prec_*x,
\]
and the incomparable pair \((b,t)\) is a strict strong-majority span descent,
also forbidden. Hence every \(t\in T\) satisfies (4.1).

A singleton \(T\) would make its sole event equal to \(V\), contradicting
(3.6). Hence \(|T|=2\). Since each channel has probability \(<1/3\), their
union has probability \(<2/3\), proving (4.2). Finally
\[
\Pr(b<t_1)+\Pr(b<t_2)\ge \Pr(V)>1/3,
\]
so one channel exceeds \(1/6\), proving (4.3). `square`

### Interpretation

The leaf is therefore not a new terminal geometry. In the exact no-balanced,
no-span-descent branch it is forced into the successor-free double-predecessor
fan previously treated by B11. The older double-fan theorem then reroutes the
state to strict span descent or, after clean dual-fork propagation, to a strict
successor-nested pair with chain successor difference. In the present branch
span descent is already excluded, so only the corridor exit remains.

This replaces the preceding run's broad unpaid phrase “dominant-side balance
transfer” by a substantially narrower structural obligation: no arbitrary
mixture theorem is needed merely to leave the leaf state.

## 5. Application of the named partner and current lead

This theorem pays a concrete part of the lead r15 `RAY-RETURN EXCLUSION`.

A lead outward packet that reaches a strong-majority pair whose endpoint is an
incomparability leaf cannot be absorbed there. It must either have already
created a balanced pair / strict span descent, or it exports through the exact
double Hasse fan of Theorem 4.1 and hence into the previously proved dual
successor-chain corridor.

Now apply account03/B19 r13 to the first exact-two crossed state on such a
continuation. Its crossed-recycler theorem forces fresh relation structure:
the two channels cannot close on the old five-vertex core, and a singleton
shared recycler itself forces at least two further outside distinguishers.
Thus the combined route excludes the specific return mechanism

`outer ray -> incomparability leaf -> fixed local double-fan/crossed loop`.

What remains genuinely open is reuse across *multiple generations* of
corridor/recycler states or a non-crossed multi-distinguisher exit. That is
strictly narrower than allowing a leaf to be an unanalysed terminal sink.

## 6. Source-valid adversary to a stronger shortcut

The theorem does **not** say that one of the two fan channels is itself balanced.
An exact six-point width-three example, with both the comparability and
incomparability graphs connected, has covers
\[
0<4,\quad1<4,\quad1<5,\quad2<3,\quad2<5,\quad3<4.
\]
Take \(x=4,b=5\). There are \(E=37\) full linear extensions and
\[
N(5<4)=25>2E/3.
\]
Here
\[
T=\{0,3\},\qquad
N(5<0)=7,\qquad N(5<3)=10,
\]
so both fan channels are \(<1/3\), while their union has
\[
13/37>1/3.
\]
The poset is not a POS3 counterexample: for example several other pairs are
balanced (the verifier records exact witnesses). Hence this is a source-valid
refutation only of the stronger *local fan-channel balance* shortcut. It shows
why the corridor/recycler continuation is genuinely needed.

## 7. Exact regression

I executed an independent exact-arithmetic enumerator over all distinct
naturally-labelled transitive closures on \(2\le n\le6\).

Results:

```text
natural_posets 5230
width_le3 3701
leaf_states 3192
strong_b_before_x 760
no_strict_span_descent 760
balanced_T_channel 685
hard_local_leaf_states 75
hard_local_biconnected 75
POS3_LEAF_DOUBLE_FAN_CAPACITY_V1_PASS
```

For every leaf state the checker verifies the splice factorization, capacity
identity, upset/Hasse claims and exact reverse-union count. In all 75 finite
states where the leaf orientation is strong and neither span descent nor a
balanced maximal delayed-predecessor channel occurs, the state is exactly a
double fan and one channel has probability \(>1/6\). All 75 happen also to be
bi-connected in the two complementary graphs. This is regression evidence
for the symbolic proof, not arbitrary-size closure.

Verifier:
- `verify_leaf_double_fan_capacity_v1.py`
- executed SHA-256 `b1c5e8b94ab3e0b81f0cc9e6e1cccfc7cc939b6b0aa66514e096e69347bf7b2b`

Captured output:
- `verify_leaf_double_fan_capacity_v1.out`
- SHA-256 `cf9ff1a88187929431b238b6b2e2579f74581695c511d4dd112bacf3ef6ed80d`

## 8. First remaining implication

The first essential unpaid implication is now:

> **GLOBAL NON-REUSE AFTER LEAF EXPORT.** Starting from the lead r15 outward
> defect packet, after every incomparability-leaf landing is converted by
> Theorem 4.1 into a double Hasse fan and then into the prior dual chain
> corridor, prove that successive corridor / exact-two crossed / non-crossed
> multi-distinguisher states cannot reuse previously exposed vertices in a
> directed cycle without forcing a balanced incomparable pair, strict
> strong-majority span descent, a four-antichain, or a proper
> autonomous/ordinal/parallel reduction.

The partner r13 theorem already excludes the smallest exact-two crossed local
closure; the missing part is the arbitrary-generation non-reuse argument.

## 9. Claim ledger and provenance

**Proved this run**
- exact insertion-capacity representation (2.2)-(2.3);
- exact maximal delayed-predecessor reverse-union formula (3.4)-(3.5);
- leaf-terminal exclusion Theorem 4.1 and its order dual;
- reduction of the previous leaf-specific balance-transfer obstruction to the
  already existing double-fan/corridor mechanism.

**Applied**
- account04/B10 r15 outer-ray localization / ray-return obligation;
- account03/B19 r13 crossed-recycler fresh-vertex theorem;
- prior B11 double-fan dual-corridor theorem.

**Refuted only as a stronger shortcut**
- “one fan channel must already be balanced,” by the exact six-point example.

**Not proved**
- global recycler/ray acyclicity;
- POS3;
- any movement of the inherited finite frontier.

No benchmark material, sealed answers, credentials, scheduler identifiers,
machine paths, raw private transcripts, email/Drive data, paid API/model/Codex
calls, remote workflow, permission change, or public posting is used or claimed.
