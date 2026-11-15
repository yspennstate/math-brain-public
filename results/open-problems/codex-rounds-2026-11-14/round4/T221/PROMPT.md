# Open problem T221: Rokhlin entropy of Bernoulli shifts over arbitrary countable groups

Statement: For every countably infinite group G and every standard probability space (L,lambda), is h_Rok(G acting on (L^G,lambda^G))=H(L,lambda)? Here G acts by the Bernoulli shift, H is the Shannon entropy of the base, taken as infinity for a base without countable support, and h_Rok is the infimum of the Shannon entropies of countable generating partitions of this ergodic probability-preserving action.

Caveat: The conjecture, called RBS by Seward, includes infinite base entropy. The inequality h_Rok<=H is immediate from the coordinate partition; the opposite inequality is the issue. The equality is known for sofic groups. The existence of a non-sofic group does not itself prove either a positive or a negative answer. Isomorphism of Bernoulli shifts with unequal base entropies is a consequence-level question, not a second row here. T034 and T092 concern mixing and spectrum of a single transformation.

Source: B. Seward, Krieger's finite generator theorem for actions of countable groups II, arXiv:1501.03367v4 (2019), Introduction, statement RBS and Theorem 1.12

Where it stands (checked by us, Nov 2026): Seward proves the equality conditionally on positive Rokhlin entropy actions existing for every countably infinite group and establishes it for sofic groups. The inspected 2025-2026 entropy papers concern particular classes of actions or consequences of positive entropy, rather than a proof of RBS for all groups. The 2026 non-sofic-group announcement removes a possible shortcut through universal soficity but does not resolve RBS. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T221 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T221 (read it,
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
VERDICT: PARTIAL an explicit finite-model defect bound for every hypothetical local entropy witness

RBS remains unresolved. The earlier finite-witness reduction holds under
independent re-derivation and a new computation. The extension proved here
is a quantitative necessary condition on a hypothetical strict witness.
No new group satisfying RBS and no counterexample is obtained.

For a finite base p, local encoder Y_g=f((X_gs)_{s in S}) with output
alphabet B, and finite decoding window D, set

\[
 a=H(Y_e),\qquad c=H(X_e\mid Y_D),\qquad
 \delta=H(p)-a-c.
\]

PROOF.md proves that, if delta>0, every finite permutation model of the
required coordinate pattern has a fraction eta of defective vertices
satisfying

\[
 \eta\geq\frac{\delta}{\log|B|+\delta}.
\]

The more precise bound separates encoder defects alpha from decoder
defects beta:

\[
 \delta\leq\alpha(\log|B|-a)+\beta(H(p)-c).
\]

The proof uses the finite identity
H(U_V)=H(Z_V)+H(U_V|Z_V), subadditivity, and the fact that every local
decoded name is a function of Z_V. It bounds bad-vertex conditional
entropy by H(p), which improves the elementary rank-alphabet bound for
nonuniform bases. Section 3 writes the result as an explicit sum of
normalized Hamming defects and fixed-point fractions of finitely many
words. This applies to the finitely presented cover from the earlier
report. The bound also holds with the earlier decoder-error gap Delta
in place of delta, by the elementary conditional-entropy error bound.

The conditional-entropy criterion is prior work for uniform bases:
Lewis Bowen and Michael Chapman,
[*Surjunctivity does not characterize cosoficity of invariant random
subgroups*, arXiv:2511.06586v1](https://arxiv.org/html/2511.06586v1),
Theorem 4.1 and Section 5. The contribution here is the explicit defect
estimate and its word formulation. Priority of that estimate has not
been established.

The bounded literature check found no resolution. The reopened statements
of Theorems 1.10 and 1.12 in Brandon Seward,
[*Krieger's finite generator theorem for actions of countable groups II*,
arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4), confirm the
earlier reduction, including infinite base entropy. Tim Austin,
[*Some Recent Developments in Structural Ergodic Theory*, ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564),
Question 3.1, still poses the possibility of identically zero Rokhlin
entropy. These checks do not prove the absence of later work.

Validation command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_defects.py
```

The successful run independently matched all 768 earlier CSV cases,
including 108 exact zero gaps and 660 exact positive gaps. It used
24,576 pointwise full-name reconstructions on a five-cycle, rather than
the earlier three-bit probability calculation, and an independently
expanded rational-product comparison for the entropy signs.

It also tested all 256 Boolean three-input encoders on the regular action
of S3 for two bases: 512 cases. Conditional entropy was computed both by
joint-minus-marginal entropy and by averaging posterior entropies; the
maximum discrepancy was 2.220446049250313e-16. The minimum information
slack was zero. Noncommuting generators check the multiplication order.

A deliberately inconsistent formal collision pattern exercises a positive
gap: delta=0.130812035941137 and the bound is 0.15876032857139014.
All 216 permutation assignments on three vertices and 13,824 on four
vertices satisfy the estimate. This pattern cannot occur in a group;
it is an arithmetic test, not an RBS witness. Its constants were also
derived as delta=(3/4)log 3-log 2 and bound=1-4log 2/(3log 3).

Full output is in audit_defects.json; commands, checks, and relevant
output are in LOG.md. The run took 0.602 seconds and 16,859,136 bytes
peak RSS. The wrapper's `nice: setpriority: Operation not permitted`
diagnostic reflects inherited nice priority 20, verified by the script.
No priority increase was attempted. No mathematical test failed.

The estimate was checked a second way using the repaired full name,
giving the same error-gap constant for uniform bases. Edge cases checked
include constant output, zero base probabilities, repeated name entries,
nonuniform bases, word order, and both equalities and inequalities in
the coordinate pattern. Sharpness is not established.

What failed to advance: no certified non-sofic candidate or genuine
positive-gap code was supplied. Non-soficity alone does not provide such
a code. The finite word pattern remains required input; the result does
not decide arbitrary presentation word problems.

Next: refine the bound for a fixed certified pattern by computing the
conditional entropy cost for each possible defective collision pattern,
instead of using the universal caps log|B| and H(p). This gives a concrete
way to reject proposed local codes or sharpen a candidate's obstruction.
An actual group pattern is essential; the inconsistent audit pattern
must not be used as a candidate.

Task: “take the NEXT checkable step on this problem, building on that work.”
— 2026-11-15 01:40 Asia/Tbilisi (session start recorded in LOG.md).
