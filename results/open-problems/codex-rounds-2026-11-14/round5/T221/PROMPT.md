# Open problem T221: Rokhlin entropy of Bernoulli shifts over arbitrary countable groups

Statement: For every countably infinite group G and every standard probability space (L,lambda), is h_Rok(G acting on (L^G,lambda^G))=H(L,lambda)? Here G acts by the Bernoulli shift, H is the Shannon entropy of the base, taken as infinity for a base without countable support, and h_Rok is the infimum of the Shannon entropies of countable generating partitions of this ergodic probability-preserving action.

Caveat: The conjecture, called RBS by Seward, includes infinite base entropy. The inequality h_Rok<=H is immediate from the coordinate partition; the opposite inequality is the issue. The equality is known for sofic groups. The existence of a non-sofic group does not itself prove either a positive or a negative answer. Isomorphism of Bernoulli shifts with unequal base entropies is a consequence-level question, not a second row here. T034 and T092 concern mixing and spectrum of a single transformation.

Source: B. Seward, Krieger's finite generator theorem for actions of countable groups II, arXiv:1501.03367v4 (2019), Introduction, statement RBS and Theorem 1.12

Where it stands (checked by us, Nov 2026): Seward proves the equality conditionally on positive Rokhlin entropy actions existing for every countably infinite group and establishes it for sofic groups. The inspected 2025-2026 entropy papers concern particular classes of actions or consequences of positive entropy, rather than a proof of RBS for all groups. The 2026 non-sofic-group announcement removes a possible shortcut through universal soficity but does not resolve RBS. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T221 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T221 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T221 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Your job for this session: take the NEXT checkable step on this problem, building on that work.
1. Five minutes at most: check whether anything after the earlier report changes the picture. If the problem was
   solved elsewhere, write SOLVED_ELSEWHERE.md (reference, arXiv id, what exactly is proved) and REPORT.md, then stop.
2. First re-check the earlier result: re-derive its main claim or re-run its computation an independent way, and
   write in LOG.md whether it holds. If it does not hold, that finding is your result.
3. Then choose ONE piece that extends it: the next step its report names, a wider special case, a sharper constant,
   more cases computed, the missing lemma. Write the choice and why in LOG.md first, then do it. A proof goes in
   PROOF.md with every step written out; a computation is a script in this folder with the command and output in LOG.md.
4. Try to break your own result: re-derive every load-bearing number a second way; look for the case you miss.
5. Finish with REPORT.md: first line exactly one of  VERDICT: PROVED <what> | VERDICT: PARTIAL <what> | VERDICT: COMPUTED
   <what> | VERDICT: NO PROGRESS <why> | VERDICT: EARLIER RESULT WRONG <what> . Then what is new beyond the earlier
   report, the commands, what failed, what you are unsure of, and what the next worker should do.

Rules (the author's standing laws):
- Work only inside this folder. Read anything, but never edit files elsewhere, never use git, never push, post, email or
  create accounts. Nothing you write leaves this folder except when the coordinating agent copies it.
- Compute: every program you run stays under 1 GB of RAM, one thread (set OMP_NUM_THREADS=1), runs under `nice -n 15`,
  and finishes within 20 minutes per run. No GPU, no MLX, no torch. This Mac is shared; never fill it.
- Literature: use the web search tool. Cite only papers you actually opened, with the authors exactly as on the paper or
  its arXiv page. Never invent a reference, a number or a step.
- Save as you go: append to LOG.md after every step (what you did, the command, the output that matters). The account's
  weekly allowance runs out within hours and the session may stop at any moment; LOG.md is what survives.
- Write plainly, like a working mathematician: no hype, no talk about yourself or the process inside PROOF.md.



----- earlier REPORT.md -----
VERDICT: PARTIAL a collision-table refinement of the finite-model defect bound, with a sharp cap for the three-input AND encoder

RBS remains unresolved. The earlier defect bound survives an independent
chain-rule derivation. The bounded literature check found no resolution.

The new result replaces the universal bad-root entropy cap
log|B|+H(p) by an exact finite table for the specified local rule. A
partition of a prefix-closed word window is realizable at a root of finite
permutations exactly when each generator prescribes a well-defined
injective partial map on its classes. Such a map completes to a
permutation on the same classes. PROOF.md proves both directions,
including inverse letters.

For a hypothetical strict witness, write

\[
 C_0=H(Y_e)+H(X_e\mid Y_D),\qquad \delta=H(p)-C_0>0.
\]

If M_bad is the maximum table cost among realizable types with the
wrong coordinate pattern, every finite permutation model satisfies

\[
 \eta\geq\frac{\delta}{M_{\rm bad}-C_0}.
\]

Here eta is the fraction of roots with the wrong pattern. The one-point
model proves M_bad>=H(p)>C0, so the denominator is positive. This is at
least as strong as the earlier delta/(log|B|+delta) bound. The table also
gives finite linear constraints for weights on individual word defects.
Those weights were not optimized numerically.

For a genuine certified example, take F2=<a,b>, S=D=(1,a,b), and the
three-input AND encoder on Bernoulli(p) bits. The seven words
1,a,b,aa,ab,ba,bb are distinct in F2. The exact maximum local cost is

\[
 M=h(p)+p\max\{h(p),h(p^2)\}.
\]

The proof derives the upper bound directly by conditioning on the root
bit. Two- and three-point permutation models attain its two branches.
For the fair base this improves the cap from 2 log2 to (3/2)log2:
1.3862943611198906 to 1.0397207708399179. The cap is sharp at a single
root; sharpness of the resulting defect estimate is not established.

This example has no positive gap. Its target deltas are exactly negative
for p=1/3,1/2,2/3, with numerical values -0.1155117709606206,
-0.2746765991340926, and -0.43181739761778837. Therefore it illustrates
the improved cap and does not instantiate a nontrivial positive-gap
defect bound. No new group satisfying RBS or counterexample is obtained.

Validation command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 collision_costs.py
```

The final run succeeded in 0.273 seconds with 17,924,096 bytes peak RSS.
It enumerated all 877 partitions of the seven-word window: 103 are
realizable and 774 are rejected. Every realizable type was completed to
explicit permutations on at most seven points. A separate enumeration
checked all 576 pairs of four-point permutations at all 2,304 roots.
The five bases 0,1/3,1/2,2/3,1 gave 515 completed-model/base checks.

Every cap comparison uses exact rational entropy-product signs.
Conditional entropies were computed by both joint-minus-marginal entropy
and posterior averaging; the largest difference was
3.3306690738754696e-16. The genuine target cost was additionally derived
by conditioning on the two independent child outputs, agreeing exactly
by entropy-product comparison. The script checks the earlier separate
encoder/decoder defect inequality on all completed models. Full data are
in collision_table.json and collision_summary.json; LOG.md records the
commands, output, independent derivations and edge cases.

The nice wrapper prints `setpriority: Operation not permitted` because
the inherited priority is already 20, which the script reads and checks.
The run used one process, no workers, a 180-second alarm and an RSS check
below 1 GiB. No mathematical test failed. A patch with mismatched context
was corrected without changing the mathematical result. No predecessor
artifact or external state was edited; no git or subagents were used.

The opened literature was Brandon Seward,
[*Krieger's finite generator theorem for actions of countable groups II*,
arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4);
Lewis Bowen and Michael Chapman,
[*Surjunctivity does not characterize cosoficity of invariant random
subgroups*, arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1);
and Tim Austin,
[*Some Recent Developments in Structural Ergodic Theory*, ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564).
The conditional-entropy criterion is existing work. Priority of the
collision-table refinement and completion lemma was not established.
Austin's Question 3.1 still asks about identically zero Rokhlin entropy;
the search is not proof that no later resolution exists.

What did not advance: no genuine strict witness or new non-sofic group
pattern was supplied. Single-root completion does not give a finite
action of G or a model good at most roots. Bell-number growth limits
larger direct tables, and global compatibility of rooted types remains
unaddressed.

Next: add stationarity constraints to the existing 103-type table before
enlarging the window. For each partition sigma of three positions, the
frequency of sigma on (1,a,b) must equal its frequency on (a,aa,ab), and
also on (b,ba,bb), because each generator permutes the roots. These are
explicit linear constraints on the type frequencies. Combine them with
the table entropy inequality and prescribed word-defect tolerances in a
finite linear program. For an RBS application a certified genuine
positive-gap candidate is still essential; the AND example has none.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 2026-11-15 05:02 Asia/Tbilisi.
