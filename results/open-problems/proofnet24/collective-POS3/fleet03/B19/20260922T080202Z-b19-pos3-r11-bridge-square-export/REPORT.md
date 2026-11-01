# POS3 fleet03/B19 — the first cross-envelope 4-cycle cannot close: bridge-square export

**Run:** `20260922T080202Z-b19-pos3-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has an incomparable pair \(x,y\) with
\[
\frac13\le \Pr[x<y]\le \frac23
\]
under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Inherited finite frontier:** `n_bal=14`, unchanged.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

Every probability below is under the original uniform law on all full linear extensions of the original poset. No deletion-induced law is used as though it were uniform.

## 1. Fresh collective state consumed and mechanism change

The named partner result actually consumed is fleet04/B10 r18:

- `proofnet24/collective-POS3/fleet04/B10/20260922T081352Z-B10-POS3-r18/REPORT.md`,
  Git blob `456e0674fdcecd6e419a0920786c05e3d35a5bfd`.

It proves that every surviving four-channel outward export recreates a heavy Hasse bridge, and that an opposite-ray two-step switch is exactly one of:

1. strict strong-majority span descent;
2. strict envelope expansion;
3. exact backtrack through the heavy bridge.

Its first unpaid implication is `POS3-CROSS-ENVELOPE-BACKTRACK-EXIT-v1`: exclude global recycling made from envelope expansions and non-exact/multi-distinguisher backtracks.

I also consume fleet02/B10's exact full-law four-channel transposition theorem:

- `proofnet24/collective-POS3/fleet02/B10/20260922T075033Z-b10-pos3-r11/REPORT.md`,
  Git blob `c82c5309ce2cf74a1c103149b879249eaa1ffce9`.

For every strong incomparable pair \(a\prec_* b\), its outgoing position-swap defect has size \(>E/3\), every defect has a Hasse witness in at most four width-three channels, and therefore one actual incomparable-pair channel carries \(>E/12\) marked full extensions.

After several runs on local recycler cases, this run changes mechanism as required: instead of another one-ray/local-distinguisher case split, it studies the **bridge-transition graph** and attacks its first possible genuine reuse cycle.

## 2. Bridge-transition graph

Assume hypothetically that the poset has no balanced pair. Then the strong-majority relation \(\prec_*\) is a strict total order (fleet01/B10).

A **heavy bridge triple** is a triple
\[
(a,q,c)
\]
with
\[
a\lessdot c,\qquad q\parallel a,c,\qquad a\prec_*q\prec_*c.
\]

Define the undirected bridge-transition graph \(\mathcal G\) as follows.

- Its vertices are ordered strong incomparable pairs \((u,v)\) with \(u\prec_*v\).
- Every heavy bridge triple \((a,q,c)\) contributes the edge
\[
(a,q)\ --\ (q,c).
\]

Traversing this edge in either direction is exactly the heavy-bridge backtrack/switch state isolated by fleet04/B10 r18.

Orient each edge canonically
\[
(a,q)\longrightarrow(q,c).
\]
If \(\rho\) is strong-order rank, then
\[
\rho(a)<\rho(q)<\rho(c),
\]
so along an oriented edge both coordinates shift strictly to the right. In particular this canonical orientation is acyclic.

### Lemma 2.1 — no triangle

The underlying graph \(\mathcal G\) has no triangle.

**Proof.**
If a vertex \((a,b)\) has two outgoing neighbors, they are \((b,c_1)\) and \((b,c_2)\) with \(c_1\ne c_2\). Such two neighbors cannot themselves be adjacent, because adjacency requires the second coordinate of one ordered pair to equal the first coordinate of the other. The dual statement holds for two incoming neighbors.

An acyclic orientation of a triangle has a source or sink incident to two edges whose other endpoints are adjacent. The preceding coordinate observation excludes that. \(\square\)

Thus the first possible nontrivial closed reuse in the bridge-transition graph has length four.

## 3. Exact characterization of a four-cycle

### Lemma 3.1 — every bridge-transition four-cycle is a \(K_{2,2}\) cover square around one middle vertex

Every simple four-cycle in \(\mathcal G\) has, after relabelling, vertices
\[
(\ell_1,q),\quad(\ell_2,q),\quad(q,r_1),\quad(q,r_2)
\]
and its four edges are the four heavy bridge triples
\[
(\ell_i,q,r_j),\qquad i,j\in\{1,2\}.
\]

Consequently
\[
\ell_i\lessdot r_j\quad\text{for all }i,j,
\]
\[
q\parallel \ell_1,\ell_2,r_1,r_2,
\]
and
\[
\ell_i\prec_*q\prec_*r_j.
\]

**Proof.**
Because the canonical orientation is acyclic, a four-cycle cannot be a directed cycle. A source-to-sink orientation with two directed paths of length two is also impossible: if
\[
(a,b)\to(b,c_1),\qquad (a,b)\to(b,c_2),
\]
then a common next vertex would have to begin simultaneously with \(c_1\) and \(c_2\), forcing \(c_1=c_2\).

A three-edge directed path plus a closing edge is impossible for the same coordinate-shift reason: after
\[
(a,b)\to(b,c)\to(c,d)\to(d,e)
\]
neither endpoint pair can be adjacent to the other unless a strict strong-order rank repeats.

Hence the only acyclic orientation of the four-cycle compatible with the ordered-pair overlap rule has two sources and two sinks alternating. The two sources must share their second coordinate \(q\), and the two sinks must share first coordinate \(q\). Writing them as above gives exactly the claimed four heavy bridge triples. \(\square\)

Distinct lower covers of either \(r_j\) are incomparable, so
\[
\ell_1\parallel\ell_2.
\]
Dually,
\[
r_1\parallel r_2.
\]

The core therefore consists of a three-antichain
\(\{\ell_1,\ell_2,q\}\), another three-antichain
\(\{q,r_1,r_2\}\), and the complete \(K_{2,2}\) family of cover relations from the two lower vertices to the two upper vertices.

## 4. New bridge-square export theorem

The tempting statement “a four-cycle already contains a balanced sibling pair” is false; Section 5 gives an exact counterexample. What is true is the stronger-for-induction export statement below.

### Theorem 4.1 — a span-descent-exhausted bridge square exports \(>E/12\) beyond its entire strong-order hull

Let \(P\) have width at most three and suppose there is no balanced pair. Let
\[
\ell_1,\ell_2,q,r_1,r_2
\]
form a bridge-transition four-cycle as in Lemma 3.1. Assume all strict strong-majority span descents inside the four bridge endpoint intervals have already been accepted as terminating exits.

Rename the lower siblings so that
\[
\ell_1\prec_*\ell_2.
\]

Then one of the following occurs:

1. a balanced pair exists;
2. an already-authorized strict span descent occurs;
3. there is a vertex \(z\) outside the five-vertex core and an incomparable pair involving \(z\) that carries \(>E/12\) full-extension marks in its minority orientation, with \(z\) lying **strictly outside the entire strong-order hull**
\[
[\min_*\{\ell_1,\ell_2\},\max_*\{r_1,r_2\}]_*.
\]

In particular a bridge-transition four-cycle cannot be a closed local recycler in a no-balanced, span-descent-exhausted candidate.

#### Proof

Apply fleet02/B10's exact four-channel transposition theorem to the strong sibling pair
\[
\ell_1\parallel\ell_2,\qquad \ell_1\prec_*\ell_2.
\]

Its outgoing swap defect has size \(>E/3\). Every defect has a Hasse witness in
\[
U=\{z:\ell_1\lessdot z,\ z\parallel\ell_2\},
\]
or
\[
D=\{z:z\lessdot\ell_2,\ z\parallel\ell_1\},
\]
and width at most three gives
\[
|U|\le2,\qquad |D|\le2.
\]
Therefore one concrete channel carries \(>E/12\) marked full extensions.

No vertex of the five-vertex square core belongs to \(U\cup D\). The middle vertex \(q\) is incomparable with both siblings. Each \(r_j\) is above **both** lower siblings, so it is not incomparable with \(\ell_2\) and cannot lie in \(U\). There is likewise no core member of \(D\). Thus the selected Hasse witness \(z\) is external.

Now localize \(z\) in the strong order.

**Case \(z\in D\).**
We have
\[
z\lessdot\ell_2,\qquad z\parallel\ell_1.
\]
Hence \(z\prec_*\ell_2\). If
\[
\ell_1\prec_* z\prec_*\ell_2,
\]
then \((\ell_1,z)\) is a strict strong-majority incomparable subspan of the sibling interval, an accepted descent. In the surviving branch,
\[
z\prec_*\ell_1.
\]
Every mark assigned to this channel has distinguished order
\[
\ell_1<z<\ell_2,
\]
so it lies in the minority orientation of the actual incomparable pair \((z,\ell_1)\). This minority event has probability \(>1/12\), and \(z\) lies strictly to the left of the whole square hull.

**Case \(z\in U\).**
We have
\[
\ell_1\lessdot z,\qquad z\parallel\ell_2.
\]
First \(z\parallel r_1,r_2\). Indeed, \(z<r_j\) would put
\[
\ell_1<z<r_j
\]
between the cover endpoints \(\ell_1\lessdot r_j\), while \(r_j<z\) would imply
\[
\ell_2<r_j<z,
\]
contradicting \(z\parallel\ell_2\).

Since \(\{q,r_1,r_2\}\) is a three-antichain and width is at most three, \(z\) must be comparable with \(q\). The alternative \(z<q\) would imply
\[
\ell_1<z<q,
\]
contradicting \(q\parallel\ell_1\). Hence
\[
q<z,
\]
so \(q\prec_*z\).

For either \(j\), if
\[
z\prec_*r_j,
\]
then \(z\parallel r_j\) and
\[
q\prec_*z\prec_*r_j,
\]
giving a strict strong-majority incomparable subspan of the bridge interval \((q,r_j)\). In the surviving no-descent branch this is impossible for both upper endpoints, so
\[
r_1\prec_*z,\qquad r_2\prec_*z.
\]

Every mark assigned to the \(U\)-channel has
\[
\ell_1<z<\ell_2.
\]
Because
\[
\ell_2\prec_*q\prec_*z,
\]
the marked event \(z<\ell_2\) is the minority orientation of the actual incomparable pair \((z,\ell_2)\). It has probability \(>1/12\), and \(z\) lies strictly to the right of the entire square hull.

This proves the theorem. \(\square\)

### Corollary 4.2 — the shortest nontrivial cross-envelope reuse motif is paid

Fleet04/B10 r18 left a global reuse problem after same-ray motion and two-step switch normalization. In the bridge-transition graph, immediate traversal of one edge backward is the exact-backtrack case. The first genuinely different closed reuse motif is a simple four-cycle. Lemma 3.1 identifies it exactly, and Theorem 4.1 shows it cannot absorb charge locally: after span descent is excluded, it exports a fresh \(>E/12\) minority packet beyond the whole five-vertex strong-order hull.

Thus a surviving global recycler must use a longer bridge-transition cycle / a return through an earlier larger hull, not a closed four-state bridge square.

## 5. Exact targeted counterexample to the stronger local-balance shortcut

The theorem above must be an **export** theorem. A four-cycle does not by itself force either sibling pair to be balanced.

Take the nine-element poset with Hasse covers
\[
(0,1),(1,3),(1,4),(2,5),(2,7),(3,5),(3,7),(4,6),(5,6),(6,8).
\]

Use the square
\[
(\ell_1,\ell_2,q,r_1,r_2)=(2,3,4,5,7).
\]

It has exactly
\[
E=64
\]
linear extensions and width at most three. The four bridge counts are
\[
N(2<4)=52,\qquad N(3<4)=44,
\]
\[
N(4<5)=44,\qquad N(4<7)=52,
\]
all strictly greater than \(2E/3=42\tfrac23\). Thus all four bridge triples are genuinely strong.

But the sibling pairs are both unbalanced:
\[
N(2<3)=46,\qquad N(5<7)=46,
\]
so each has probability
\[
46/64=23/32>2/3.
\]

The balanced pairs occur one layer outside the square:
\[
N(1<2)=36,\qquad N(6<7)=28,
\]
i.e.
\[
\Pr(1<2)=9/16,\qquad \Pr(6<7)=7/16.
\]

Even more sharply, the lower sibling transposition defect is
\[
(M,N,|D_M|,|D_N|)=(46,18,28,0),
\]
with the **single** Hasse defect channel
\[
D(2,3)=\{1\}.
\]
All 28 defect extensions have
\[
2<1<3,
\]
and their exported pair \((1,2)\) is balanced.

Dually, the upper sibling defect is again
\[
(46,18,28,0),
\]
with the single Hasse channel
\[
U(5,7)=\{6\},
\]
and all 28 marks have
\[
5<6<7.
\]
The exported pair \((6,7)\) is balanced.

So the exact witness falsifies the tempting stronger claim

> “a \(K_{2,2}\) heavy-bridge square forces a balanced pair inside its five-vertex core,”

while simultaneously exhibiting exactly the outward mechanism proved in Theorem 4.1.

The deterministic verifier terminates with
`POS3_B19_BRIDGE_SQUARE_EXPORT_WITNESS_PASS`.

Executed-byte SHA-256:

- `verify_pos3_bridge_square_export.py`:
  `ef44bea31dc4e7313c70b42b7749be3b5a36ffa7d1c87ee7ad278fc299222ac3`;
- `verifier_output.txt`:
  `df821fd92d55d145dfb07c8d1529eae2efbc04a7ab84720b46bf09fab2e1ef1e`.

This finite witness is a falsification/regression certificate for the stronger local shortcut. It is not a counterexample to POS3.

## 6. First remaining global implication

The first unpaid statement is now narrower:

> **`POS3-BRIDGE-GRAPH-LONG-REUSE-EXIT-v1`.**  
> In a no-balanced width-three candidate after strict span descent is exhausted, prove that the bridge-transition graph cannot support a longer nonbacktracking reuse cycle by repeatedly exporting \(>E/12\) packets into vertices exposed by an earlier, larger strong-order hull. Equivalently, at the first return to a previously exposed hull, convert the repeated full-law defect marks into either a balanced pair, a strict span descent, a proper autonomous/ordinal reduction, or a monotone global charge/potential increase.

The new theorem removes the shortest genuinely nontrivial closed bridge-reuse motif. The remaining obstruction is therefore not a four-state local square; it requires longer-history vertex reuse.

A useful next attack for the named partner `fleet04/B10` is to choose a shortest nonbacktracking cycle in the bridge-transition graph, use Theorem 4.1 to exclude length four, and combine r18's heavy-bridge cell identities with the \(>E/12\) exported packet on the first repeated hull boundary. Any proof that only tracks the local five-vertex core is now known to be insufficient because of the exact nine-point witness above.

## 7. Status and integrity

- fleet04/B10 r18 heavy-bridge / switch normal form: **CONSUMED/APPLIED**;
- fleet02/B10 full-law four-channel transposition theorem: **CONSUMED/APPLIED**;
- bridge-transition graph formulation: **NEW**;
- triangle exclusion: **PROVED**;
- exact characterization of every bridge-transition four-cycle: **PROVED**;
- four-cycle outward export \(>E/12\) beyond the full square hull, modulo accepted span descent/balance: **PROVED**;
- stronger “core sibling balance” shortcut: **REFUTED** by exact nine-element witness;
- longer cross-envelope reuse: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- inherited finite frontier `n_bal=14`: **UNCHANGED**;
- run classification: **`ESSENTIAL_STEP_APPLIED`**.

No benchmark material, credentials, scheduler identifiers, machine paths, raw private transcripts, email/Drive material, paid model/API/Codex execution, remote workflow, permission change, or public posting was used.
