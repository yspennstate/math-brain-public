# T101 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received approximately 10:51 Asia/Tbilisi, 15 November 2026.

## 10:51–10:54 — orientation and literature

Read the four earlier folders' reports, logs, proofs and scripts. They remain
read-only. Read startup memory and compute state directly: status ok, mode
owner_away_open, CPU busy, free memory 44%. Every Python command uses
`nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1`, one thread,
bounded CPU/wall time and small memory. No git or subagents. The specific
folder-only order precludes the general shared brain/mesh/checklist writes;
all durable results and task records stay here.

Web-tool searches: `"Lorentz mirror" "2026" conjecture periodic orbits`
and `"Lorentz mirror" all orbits finite proof 2026`. Opened:

- Martin P. W. Zerner, *Infinite light rays and infinite clusters with
  infinitely many pivots*, arXiv:2610.12460,
  https://arxiv.org/abs/2610.12460. Abstract still calls finiteness on Z^2
  a conjecture; its infinite examples use other plane graphs.
- Gady Kozma and Vladas Sidoravicius, *Lower bound for the escape probability
  in the Lorentz Mirror Model on the lattice*, arXiv:1311.7437,
  https://arxiv.org/abs/1311.7437. The lower escape bound does not settle
  localization.
- Jian Gu and Qin Hao, *Boundary transmission and excursion geometry in
  the Lorentz mirror model: a numerical study*, arXiv:2609.14949,
  https://arxiv.org/abs/2609.14949. The abstract leaves localization unresolved.

No later solution found. Literature check ended within five minutes; it was
not exhaustive. Next first recheck the twelve-corner result, using its
independent cell-row audit and comparing every stored boundary/strip list.

## Preceding result holds

Command:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 recheck.py

Reran the independent cell-row construction against the prior coordinate-word
list: all 9,901 individual boundaries and oriented strips agree. Prefixes
129,988; local candidates 18,525; disconnected boundaries rejected 8,624.
Exact common-denominator and derivative identities pass. Rooted unit walks
visit 3,532,630 nodes and give 6,294,5560,51012,304800 at lengths 12–20.
Positive-gap versus signed-binomial counts agree through perimeter 80.
Four rational gap sums, five perimeter sums with tails below 10^-30, and
both small-density derivations pass. R12/p tends to 20635/16777216;
at p=1/2, R12=25440181/56687040000 and B12=1459458421/56687040000.
Elapsed 3.64 seconds; full RSS 91,373,568 bytes; nice 20. Saved recheck.json.
The nice warning is the inherited nice 20 issue recorded in earlier rounds;
actual priority remains at least 15. No mathematical discrepancy found.

## Choice before the new computation

Extend ONE piece: exactly sum all periodic orbits that repeat a vertex and
have at most eight turning visits in a period, over arbitrary positive
coordinate gaps. This includes transverse self-crossings at empty vertices
and, if compatible, visits to both sides of the same mirror. Turning visits
and distinct mirrors must be counted separately. This leaves the simple
polygon family and addresses a previously omitted type of orbit, while
remaining a small finite rank classification. It can be added disjointly
to B12. It is not the family with at most eight distinct mirrors.

Enumerate cyclic corner-coordinate words for 4,6,8 turns; require no repeated
undirected edge and consistent local state at every visited vertex. Record
repeated empty vertices c and repeated mirror vertices t. For length L and
k turning visits, a compatible circuit should have k-t distinct mirrors
and L-k-c distinct empty vertices, giving weight
(p/2)^(k-t) q^(L-k-c). Audit this carefully: the old polygon weight fails
at repeated vertices. Check against an independent rooted unit-step search
that carries local states, plus direct finite-environment tracing.

## Primary repeated-vertex classification

Command:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 repeated.py

Cyclic coordinate pairs: 4,36,1444 for k=4,6,8. Compatible rank circuits:
1,6,98 respectively, with k representations each. The simple subsets are
exactly the old 1,4,38. Thus there are 62 new non-simple rank circuits.
Five families (k turning visits, t double mirror vertices, c double empties):
(6,0,1):2; (8,0,1):40; (8,0,2):14; (8,0,3):4; (8,1,0):2.
Saved all corner lists and both strip weights in repeated_data.json.

With r=q^2, their respective translation-class generating functions are
2r^4/(1-r)^4;
r^6(20+40r+24r^2)/[(1-r)^6(1+r)^2];
6r^6/(1-r)^6;
4r^8/[(1-r)^6(1+r)^2];
2r^4/(1-r)^4.
Direct horizontal rooting agrees with r times the derivative at four rational
densities. Provisional total new probability at p=1/2 is 164/18225.
Elapsed 0.034 seconds, RSS 16,678,912 bytes, nice 20. These are provisional
until the independent walk, local-environment and symbolic checks below.

An important new case is a mirror visited twice: two diagonally placed
rectangles can be joined by the other mirror orientation at their common
corner. Counting this as eight independent mirrors would be wrong; there
are seven distinct mirrors and eight turning visits.

## Independent audits and completeness strengthening

Initial command:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit_repeated.py

PASS: independent local-state unit walks through length 16, 524,186 nodes,
all 62 new rank circuits and every rooted count; all 19,683 three-by-three
local environments, 36 successful configurations; 25 exact rational family
sums/perimeter tails below 10^-30, and positive gap versus signed counts
through perimeter 80. New linear coefficient 37/4096; combined with B12,
669595/16777216. At p=1/2 combined probability 1969564021/56687040000;
at p=1 it is 387/2048. Run 0.90 s, RSS 17,039,360 bytes, nice 20.
The finite-box probability is independently 2(p/2)^6 q+2(p/2)^7:
one crossing or one mirror visited twice, each with two rooted realizations.

To strengthen completeness beyond small-perimeter coefficients, adapt the
independent walk search to stay within the four-by-four rank vertex grid,
starting upwards on every possible leftmost vertical root edge. There are
24 undirected grid edges, so a length-24 cap covers every circuit there.
The first exploratory heredoc stopped on a leftover assertion that the
root was (0,0); the variable-root search requires the actual root position.
This is an audit adaptation bug; it does not alter primary data or formulas.

## Complete independent classification and algebra audit

Corrected the variable-root assertion and reran the bounded search: 21,590
nodes, all 62 non-simple rank circuits, none missing or extra. Integrated
it into audit_repeated.py. It searches all local-state trajectories in the
four-by-four rank vertex box from each upgoing edge on its left boundary;
every rank circuit has such an edge. The 24-edge cap covers the whole grid.
This is independent of cyclic coordinate words and certifies completeness.
Both oriented strip lists are recomputed from unit edge counts and agree
for every circuit, including repeated vertices. The unbounded length-16
walk audit still agrees on all rooted coefficients (524,186 nodes).

Added exact polynomial expansions of every grouped F numerator and every
rooted derivative G, independent of the primary reduction code. All pass;
this strengthens the four-point rational checks to polynomial identities.

Reran the documented audit command. All checks pass, including all 19,683
finite environments, all counts through 80, and 25 exact probability/tail
checks. Runtime 0.97 seconds, RSS 18,530,304 bytes, nice 20.
The five closed contributions, in table order, are
p q/(8d^5);
p q^3(15+45r+49r^2+17r^3)/[32d^7(1+r)^3];
9p q^2/(64d^7);
p q^5(2+r)/[16d^7(1+r)^3];
p^2/(16d^5), where q=1-p, d=2-p, r=q^2.
The first and last sum to p/(16d^4). The repeated-mirror term is quadratic
at small p, and contributes 1/16 at p=1; treating it as eight distinct
mirrors would give incorrect powers at both endpoints.

Next write the full proof, including edge simplicity of any finite orbit,
rank completeness, local-state compatibility, distinct-vertex weights,
root multiplicities, grouped algebra and independent tail bounds.

## Analytic simplification and independent geometric interpretation

The two two-lobe families share the same underlying edge set: two diagonally
meeting rectangles. At the common vertex the empty state or the joining
mirror gives one circuit; the other mirror separates the rectangles.
Thus the central state's combined probability is q+p/2=d/2. There are six
other mirror vertices. A direct four-positive-gap sum, with two diagonal
placements and horizontal root multiplicity 2(a+b), gives p/(16d^4).
This re-derives the sum of (6,0,1) and (8,1,0) without rank enumeration.

Also, the one-crossing and three-crossing eight-turn contributions combine:
(15+45r+49r^2+17r^3)+2r(2+r)
=15+49r+51r^2+17r^3=(1+r)(15+34r+17r^2).
Consequently the full new contribution has the shorter positive expression

C(p)=p/(16d^4)+9p q^2/(64d^7)
     +p q^3(15+34q^2+17q^4)/[32d^7(1+q^2)^2].

The small-p coefficient is independently 1/256+9/8192+33/8192=37/4096.
The audit now checks the geometric rectangle sum, exact polynomial
factorization, and compact formula at all five rational densities.

## Proof and report written; adversarial review

PROOF.md now derives edge simplicity of every finite orbit using the
degree-two graph on undirected lattice edges, states the exact repeated-
vertex probability weight, gives the complete 10-row classification and
both exhaustive rules, proves rooting and arbitrary-gap sums, expands every
rational function and derivative, and proves the coefficient/tail checks.
REPORT.md gives the required PARTIAL verdict, exact scope, formula, limits,
commands, limitations and a concrete next step.

Adversarial checks addressed repeated corners, repeated mirror use, overlaps,
local-state conflicts, root orientation, rank fullness, canonicalization,
positive gaps, both density endpoints and the tail ratio. The independent
finite-environment histogram is {6:2,7:10,8:16,9:8}; it reproduces the orbit
weights after unused states sum out. In particular the shared mirror is
counted once, and the shared empty crossing is counted once.

A proof transcription omitted one of the two equal 4*6/2^17 summands in
the direct gap-singularity calculation. Comparing with the table caught
this; the seven-term displayed sum now agrees with the already correct
script value 37/4096. This was a document error, not a data or formula error.
Removed speculative clock labels on earlier log steps; the task receipt
and opening orientation time are retained approximately.

Reran the audit after the added geometric/compact-formula checks:
all checks pass, 1.075 s, full RSS 18,825,216 bytes, nice 20.
Next perform a read-only artifact audit against the saved exact data.

The first artifact-audit command failed because its Markdown parser confused
the length-8 rooted-count row with a classification row whose k is 8. Both
have six numeric fields. The proof tables and data were unchanged. Corrected
the checker to distinguish the two table headers before parsing rows.

## Final artifact audit passed

Command:

    nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 verify_artifacts.py

Output:

    PASS all 10 classification rows, five rooted rows, seven-term small-p sum,
    verdict, exact constants, 25 tail bounds, script syntax, document characters and resource limits.

REPORT.md records the checker command and its table-parser correction.
The final document read caught and removed a duplicated sentence fragment
introduced while adding that explanation. No numerical data changed.

Finished: exact repeated-vertex contribution with at most eight turning
visits, giving the strict new bound B12+C. All prior mathematical claims
rechecked successfully. Full periodicity remains unresolved. Every new
artifact is in this folder; no prior folder or external state was modified.

Task: “take the NEXT checkable step on this problem, building on that work” —
received approximately 10:51 Asia/Tbilisi, 15 November 2026.
