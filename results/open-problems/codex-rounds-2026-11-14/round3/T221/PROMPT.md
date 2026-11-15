# Open problem T221: Rokhlin entropy of Bernoulli shifts over arbitrary countable groups

Statement: For every countably infinite group G and every standard probability space (L,lambda), is h_Rok(G acting on (L^G,lambda^G))=H(L,lambda)? Here G acts by the Bernoulli shift, H is the Shannon entropy of the base, taken as infinity for a base without countable support, and h_Rok is the infimum of the Shannon entropies of countable generating partitions of this ergodic probability-preserving action.

Caveat: The conjecture, called RBS by Seward, includes infinite base entropy. The inequality h_Rok<=H is immediate from the coordinate partition; the opposite inequality is the issue. The equality is known for sofic groups. The existence of a non-sofic group does not itself prove either a positive or a negative answer. Isomorphism of Bernoulli shifts with unequal base entropies is a consequence-level question, not a second row here. T034 and T092 concern mixing and spectrum of a single transformation.

Source: B. Seward, Krieger's finite generator theorem for actions of countable groups II, arXiv:1501.03367v4 (2019), Introduction, statement RBS and Theorem 1.12

Where it stands (checked by us, Nov 2026): Seward proves the equality conditionally on positive Rokhlin entropy actions existing for every countably infinite group and establishes it for sofic groups. The inspected 2025-2026 entropy papers concern particular classes of actions or consequences of positive entropy, rather than a proof of RBS for all groups. The 2026 non-sofic-group announcement removes a possible shortcut through universal soficity but does not resolve RBS. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T221 (read it,
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
VERDICT: PARTIAL finite witnesses and a reduction of RBS to finitely presented groups with finite uniform bases

The original problem remains open in this session. The result is a proved
reduction, with an explicit finite certificate for a hypothetical failure.
No claim of novelty is made for the local-witness principle.

For a finite base (p) on (k\geq2) symbols, PROOF.md proves

\[
h_G^{\rm Rok}(A^G,p^G)
=\inf_{S,D,B,f,d}\left[H(Y_e)+b(\varepsilon)
                         +\varepsilon\log(k-1)\right],
\]

where (Y_g=f((x_{gs})_{s\in S})), (S,D,B) are finite, and
(\varepsilon=\Pr[x_e\ne d((Y_t)_{t\in D})]). A strict value below (H(p))
is a finite witness: appending a rank correction yields a generating
partition, with a pointwise local inverse, below the base entropy.
Conversely, every entropy-lowering countable generator gives such a witness.

The witness depends on finitely many coordinate coincidences. Imposing
exactly those equalities on a free group gives a finitely presented cover
with the same witness statistics. Its quotient onto the subgroup generated
by the windows preserves the necessary inequalities between coordinates.
That subgroup must be infinite, by a direct finite-information argument.

Together with Theorems 1.10 and 1.12 of
[Brandon Seward, *Krieger's finite generator theorem for actions of countable
groups II*, arXiv:1501.03367v4](https://arxiv.org/abs/1501.03367v4),
this proves that full RBS, including infinite-entropy standard bases, is
equivalent to RBS for finitely presented infinite groups with finite uniform
bases. The dependence on these existing theorems is stated explicitly.
For rational bases, the finite entropy-gap test is an exact comparison of
integer products; formula (10) in PROOF.md gives the certificate.

The literature check took less than four minutes and found no resolution.
[Lewis Bowen and Michael Chapman, *Surjunctivity does not characterize
cosoficity of invariant random subgroups*, arXiv:2511.06586](https://arxiv.org/abs/2511.06586)
already provide a related, sharper conditional-entropy criterion in the IRS
setting, Theorem 4.1 and Section 5. That work is relevant prior art and does
not settle arbitrary-group RBS.
[Tim Austin, *Some Recent Developments in Structural Ergodic Theory*,
ICM 2026](https://epubs.siam.org/doi/10.1137/25M1805564)
still lists the existence of groups with identically zero Rokhlin entropy
as open. The opened paper page for
[Zongrui Hu, Leiye Xu, Shuhao Zhang, arXiv:2607.11549](https://arxiv.org/abs/2607.11549)
concerns an orbit-multiplicity consequence of positive entropy for amenable
groups, rather than universal RBS. This search is not a proof of absence
of later work.

Validation command:

```
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_local_codes.py
```

The successful run checked every binary two-input encoder and binary
two-output decoder on Z with windows S=D={0,1}, for input probabilities
1/2, 1/3, and 2/3. Results: 768 pairs, 6,144 pointwise reconstructions,
108 exact zero gaps, 660 exact positive gaps, and no negative gaps.
Each probability distribution was computed independently by direct
enumeration and by conditioning on the middle bit. Entropy-gap signs were
checked by integer arithmetic. These tests audit the construction in a
known case; they do not prove an unknown instance of RBS.

Data and full output are in local_code_audit.csv and local_code_audit.json.
The program used 16,515,072 bytes of peak RSS and finished in under a second.
The wrapper prints `nice: setpriority: Operation not permitted` because the
inherited process already has nice priority 20, confirmed and asserted by
the program. The first launch failed before enumeration because the Mac
rejected an RLIMIT_AS setting; this unsupported guard was removed. The
bounded run records and checks actual RSS and has a 60-second alarm.

The proof audit checked the multiplication order DS, the need to preserve
both equalities and inequalities in the finite word list, possible finite
subgroups, decoder errors 0 and 1, truncation of countable generators,
and the infinite-base case. It avoids entropy monotonicity under factors.
The detailed audit is in LOG.md.

What remains uncertain: priority relative to all existing formulations of
this reduction was not established. No counterexample was found, and no
new positive lower bound for a non-sofic group was proved. Arbitrary finite
presentation word problems prevent treating the reduction itself as an
unconditional enumeration algorithm for all groups.

Next: investigate a finitely presented candidate beyond the known sofic
cases, certify its required finite word-equality pattern, and use these
tests to seek a strict witness or a structural obstruction. The reduction
does not supply such a candidate. Increasing the small Z audit is only an
implementation check, since RBS for Z is already known.

Task: “push this problem forward by one checkable piece” — 2026-11-14 22:06 Asia/Tbilisi.
