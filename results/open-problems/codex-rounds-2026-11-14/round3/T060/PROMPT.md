# Open problem T060: The Haldane conjecture for integer-spin chains

Statement: The spin-1 antiferromagnetic Heisenberg chain H = Σ_x S_x·S_{x+1} has a unique infinite-volume ground state, a spectral gap above it, and exponentially decaying correlations; more generally antiferromagnetic Heisenberg chains are gapped for integer spin and gapless for half-integer spin.

Source: F. D. M. Haldane, Nonlinear field theory of large-spin Heisenberg antiferromagnets, Phys. Lett. A 93 (1983); F. D. M. Haldane, Continuum dynamics of the 1-D Heisenberg antiferromagnet, Phys. Rev. Lett. 50 (1983)

Where it stands (checked by us, Nov 2026): The AKLT chain, a different spin-1 Hamiltonian, is gapped (Affleck–Kennedy–Lieb–Tasaki 1987); half-integer chains cannot have a unique gapped ground state (Lieb–Schultz–Mattis 1961; Affleck–Lieb 1986); a loop-model reformulation (Aizenman–Nachtergaele 1994). Open for the spin-1 Heisenberg chain.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T060 (read it,
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
VERDICT: PARTIAL literature update: the spin-1 periodic gap is proved elsewhere

The literature search found substantial advances and triggered step 1's stop rule. No new proof or numerical experiment was undertaken.

[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md) records the opened papers, exact authors, identifiers, and theorem scope. OpenAI's September 2026 manuscript proves the periodic spin-1 gap. Subsequent primary papers are [Hal Tasaki, arXiv:2610.34330v2](https://arxiv.org/abs/2610.34330v2) and [Sirui Lu, arXiv:2611.11049v1](https://arxiv.org/abs/2611.11049v1).

The essential limitation is explicit in Tasaki's theorem: uniqueness is among translation-invariant algebraic ground states. Unrestricted infinite-volume uniqueness is outside that result. The general claim for every integer spin is not established by the sources checked here.

Verification compared primary abstracts with the full theorem statements and supplement, checked Hamiltonian normalization and boundary conditions, and distinguished analytic formalization from finite numerical hypotheses. Certificates were not recomputed; their numerical values are cited results, not independently certified outputs of this session.

Web search commands were `spin 1 Heisenberg chain Haldane conjecture rigorous proof 2025 2026 spectral gap` and `Haldane conjecture Heisenberg chain mathematical proof spectral gap recent advances`. Full text URLs and fetch outcomes are in [LOG.md](LOG.md). Direct original-PDF fetching initially failed; a readable PDF mirror subsequently succeeded. Shell work was limited to directory inspection and small read-only orientation scripts. `nice -n 15` printed a sandbox priority error; no numerical workload was launched.

Next worker: update the problem status, review the finite-certificate verifiers under the allowed resource limits, and investigate the remaining exclusion of nontranslation-invariant infinite-volume ground states. Do not spend a new session treating the periodic spin-1 gap as untouched.

Task: “push this problem forward by one checkable piece” — November 14, 2026, 20:48:39 Asia/Tbilisi (session start).
