# T127 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Received 15 November 2026, approximately 01:32 Asia/Tbilisi.

## Orientation and literature check

Read the earlier REPORT.md, LOG.md, PROOF.md, SOLVED_ELSEWHERE.md and
certificate.py in ~/codex_op_1114/briefs/T127, without
modifying that directory. No git commands or other agents are used. All
artifacts and coordination records for this session stay here; the task's
directory restriction rules out shared mesh, checklist and memory writes.

Read the compute governor: warn, owner_away_open, CPU saturation. Only tiny
standard-library calculations are planned. Requested nice -n 15 is denied
by the sandbox (setpriority: Operation not permitted). OMP_NUM_THREADS=1 is
set for every Python invocation; no parallel numerical libraries are used.

The initial brain recall returned the already known mt0-svg lead; it is a
hint, not evidence of a proof. No further brain commands are needed.

Web searches (within five minutes of starting):

- frog model 3-ary 4-ary tree mt0-svg recurrence transience solution
- frog model three four ary tree solved 2026
- "mt0-svg" "frog" paper
- "frog-model-tree" "23121586"

Opened https://github.com/mt0-svg/frog-model-tree . It still claims recurrence
for d=3 and transience for d=4 in exactly the one-sleeper simple-random-walk
model, with Lean declarations recurrent_three and transient_four. This is
the SAME lead as the earlier report, not a newly verified solution. Opening
the paper directory, STATEMENTS.md, FrogModel directory, raw Defs.lean and
https://zenodo.org/records/23121586 failed (Cache miss or inaccessible).
No accessible full proof or new arXiv identifier was obtained. Therefore the
step-1 stopping condition is not established here.

Also opened the primary sources:

- Christopher Hoffman, Tobias Johnson, Matthew Junge, Recurrence and
  transience for the frog model on trees, https://arxiv.org/abs/1404.6238 .
- Poly Mathews Jr, Improved critical drift estimates for the frog model
  on trees, https://arxiv.org/html/2309.14443v2 .

The first proves d=2 and d>=5; the latter still describes d=3,4 by simulation.
These facts do not disprove the inaccessible later claim.

## Independent recheck and chosen extension

Before extending the result, independently enumerate expected weighted
offspring from ordered directions, using the expected packet vector at
each target rather than the earlier closed-form matrix or mark enumeration.
Check the earlier exact slacks, root boundary, contraction factors and
expected-visit bounds. The new script will import no earlier code and will
read no earlier certificate data.

Chosen single extension: retain an empty child when BOTH frogs in a packet
step toward the root. Add type E (two frogs, one specified empty child).
The earlier D-to-D backward transition becomes D-to-E. Derive and check the
four-type matrix, then obtain exact rational transience certificates at
larger Bernoulli sleeper probabilities. This is the concrete next step named
in the earlier report, and changes only one piece of remembered information.
The original q=1 question is not presumed settled by this diluted case.

## Earlier result independently recovered (01:36)

Command:
```
OMP_NUM_THREADS=1 nice -n 15 python3 independent_audit.py > independent_audit_output.txt 2>&1
```
Exit 0. The script sums ordered directions and integrates the expected packet
vector at each distinct target analytically. It imports no earlier code and
reads no earlier data. Output:
```
d=3: slack=('1367/1640000', '1239/820000', '1777/1640000')
  rho=1638761/1640000; E[visits]<=1640000/1239; root_ratio=9459/13202
d=4: slack=('1481/850000', '3173/796875', '1383/850000')
  rho=273239/273700; E[visits]<=273700/461; root_ratio=27763/41055
PASS: earlier two exact certificates independently recovered.
peak_RSS_bytes = 14172160
```
The requested nice command printed its sandbox denial. The earlier result
holds: its arithmetic and boundary conditions check, and its deferred-sleeper
coupling remains valid. In particular a remembered child need only have no
remaining sleeping frog, not have been initially vacant.

Proceed with the previously chosen four-type extension. No further
literature searching is needed; the initial check took under five minutes.

## Four-type derivation and candidate search

Derived the matrix displayed in PROOF.md. Both two-frog types send two
backward frogs to E. For E, one child has no sleeper mark. Its F and D
numerators on forward moves are respectively
2d^2-(d-1)(2d-1)q and d+2d(d-1)q, with denominator (d+1)^2 t.

Command:
```
OMP_NUM_THREADS=1 nice -n 15 python3 four_type.py --search > search_output.txt 2>&1
```
Exit 0, about 0.478 seconds, peak RSS 16875520 bytes. Exploratory output:
```
exploratory d=3: q~0.419036865234375, t=2.04, v=[1.0220585894027152, 2.0, 0.9718385659118478, 1.9115485737957325]
exploratory d=4: q~0.67425537109375, t=2.54, v=[1.023060831169325, 2.0, 0.9711939867293676, 1.906149949395946]
```
These are candidate selection only, not certified optimal thresholds.
Choose q=419/1000 and q=337/500, and check all inequalities exactly.

First exact run stopped at the extra frog-slot count audit: the independent
check accidentally used Python integer division 2*d/(d+1), producing a
float. Changed it to Fraction(2*d,d+1). The three matrix derivations had
already agreed; the failed run wrote no certificate data. Command for both
runs: `OMP_NUM_THREADS=1 nice -n 15 python3 four_type.py > four_type_output.txt 2>&1`.

## Exact certificates obtained

The corrected exact run exited 0 in 0.012 seconds, peak RSS 16662528 bytes.
The candidate vectors have now been hardcoded as fractions; a normal run
uses no floating point for any certificate calculation. The optional
--search mode is retained solely to reproduce candidate selection.

Output of the successful certificate run:
```
d=3; q=419/1000; t=51/25; v=('1022057/1000000', '2', '971841/1000000', '382311/200000'); c=382311/400000
  v-Mv = ('210439/13600000000', '1656539/54400000000', '101517/6800000000', '2349271/81600000000')
  root_margin = 517970983/2040000000
  root_replacement_margins = ('32127/2000000', '17689/200000', '0')
  rho = 155980538729/155982888000 ; E[visits] <= 155982888000/2349271
  q_improvement = 9/1000
  q=1 slacks = ('-355089247/1700000000', '-625405173/1700000000', '-118359161/850000000', '-5003068201/20400000000')
d=4; q=337/500; t=127/50; v=('511527/500000', '2', '971203/1000000', '1906179/1000000'); c=1906179/2000000
  v-Mv = ('2275273/31750000000', '22341133/158750000000', '2160033/31750000000', '21335453/158750000000')
  root_margin = 369665863/1270000000
  root_replacement_margins = ('36227/2000000', '93821/1000000', '0')
  rho = 32479689227/32481964500 ; E[visits] <= 32481964500/2275273
  q_improvement = 7/500
  q=1 slacks = ('-3182568687/31750000000', '-28791566587/158750000000', '-2386472937/31750000000', '-21589095337/158750000000')
PASS: three independent matrices, exact slacks, root, and q=1 failures.
```

All weighted entries agree for q=0, q=endpoint and q=1 under three
derivations: formula, ordered-direction enumeration with integrated marks,
and explicit enumeration of Bernoulli bits on distinct fresh targets.
The E row's double-backward transition and empty-child marks were included.
Weighted total slot counts were also checked independently of packet types.
Wrote PROOF.md with the full coupling, all matrix entries, the reflecting
root and the finite-expectation argument. Saved four_type_data.json.

## Independent final audit and attempts to break the result

Command:
```
OMP_NUM_THREADS=1 nice -n 15 python3 audit_saved.py > audit_saved_output.txt 2>&1
```
Exit 0. This script imports neither comparison script, constructs no mean
matrix, and samples full configurations of marks on ALL children before
enumerating walks. It sums scalar packet weights at height two, height one,
and the root. Thus it independently recomputes every saved slack, every
height-one expected weight, the root margin, both contraction factors,
both expectation bounds and the q=1 failures. It also checks transcription
of all load-bearing fractions into PROOF.md.

Output:
```
d=3: complete child-mark enumeration recovered every slack and boundary.
  worst_row=E; epsilon=2349271/155982888000; bound*epsilon=1
  q=1 failed in all four rows; proof fractions match saved data.
d=4: complete child-mark enumeration recovered every slack and boundary.
  worst_row=F; epsilon=2275273/32481964500; bound*epsilon=1
  q=1 failed in all four rows; proof fractions match saved data.
peak_RSS_bytes = 15925248
PASS: saved-data scalar audit.
```

Reviewed the coupling against the following cases:

1. Two frogs choose the same child: one mark, producing D or D+F.
2. Two frogs choose distinct children: distinct independent marks.
3. Two frogs choose the parent: E remembers the actual child just left.
4. An E packet returns to its remembered child: mark zero, including when
   both frogs choose it.
5. Packets contain auxiliary slots: empty-child validity is required only
   for packets with actual frogs. Auxiliary-only descendants stay auxiliary.
6. Several packets first reach the same actual site: the packet supplying
   the actual sleeper is chosen from actual arrivals before any new mark.
7. Both frogs return from height one: replace E by two root packets; the
   boundary equality 2c=v_E is allowed because the interior slack is strict.
8. The root reflects through d neighbors, not d+1; its scalar enumeration
   checks this separately.
9. Reducing q delays activation, so a same-time monotonicity statement is
   unnecessary. Total path visits of activated frogs are monotone, which
   is sufficient for the stated smaller-q expectation bounds.
10. The q=1 slacks are all negative for both displayed vectors. This only
    breaks these certificates; it does not prove an obstruction for all
    vectors, nor recurrence of the original model.

The final hardcoded-certificate run also exited 0 and is saved in
four_type_output.txt. Only --search uses floating point; it is not called
by the exact certificate path. Every mathematical run took under one second
and measured less than 20 MB RSS. The sandbox denied nice priority changes
on each run; the requested invocation is preserved in all output files.

Limits: no proof at q=1, no optimized threshold, no claim of novelty relative
to published Bernoulli bounds. The reported outside complete solution remains
unverified here. The expectation bounds here are larger than the earlier
ones because the new endpoint certificates are close to loss of contraction.

Wrote REPORT.md. All earlier files remain untouched. No git, publication,
account creation or external messaging occurred.

Final artifact inspection at approximately 01:40 Asia/Tbilisi confirmed the
required REPORT.md verdict line and the proof, three scripts, saved exact
data, three verification outputs and exploratory search output are present.
The time labels above are approximate stage labels except for explicitly
reported tool-clock readings. The task is complete for this chosen extension.
