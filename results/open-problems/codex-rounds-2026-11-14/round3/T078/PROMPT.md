# Open problem T078: Long-range order in the three-dimensional quantum Heisenberg ferromagnet

Statement: The spin-S quantum Heisenberg ferromagnet on Z^d, d ≥ 3 (H = −Σ_{x∼y} S_x · S_y), has spontaneous magnetization at low positive temperature, for every S ∈ {1/2, 1, 3/2, …}.

Source: F. J. Dyson, E. H. Lieb and B. Simon, Phase transitions in quantum spin systems with isotropic and nonisotropic interactions, J. Stat. Phys. 18 (1978); B. Simon, Fifteen problems in mathematical physics, in Perspectives in Mathematics: Anniversary of Oberwolfach 1984 (Birkhäuser, 1984)

Where it stands (checked by us, Nov 2026): Proved for the classical Heisenberg model (Fröhlich–Simon–Spencer 1976) and for quantum antiferromagnets (Dyson–Lieb–Simon 1978, d ≥ 3 and S ≥ 1; Kennedy–Lieb–Shastry 1988, S = 1/2 on Z^3). For the ferromagnet: low-temperature free energy given by spin-wave theory (bounds by Conlon–Solovej 1991; the spin-wave asymptotics in d = 3 by Correggi–Giuliani–Seiringer, arXiv:1312.7873, CMP 2015); order on the complete graph and on trees through the interchange representation (Tóth; Björnberg, arXiv:1512.06986; Hammond, arXiv:1202.1322). Open on Z^3.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T078 (read it,
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
VERDICT: PARTIAL matching solution preprint located; correctness not independently audited

The literature search located OpenAI's September 24, 2026 preprint addressing exactly T078. The statement, normalization, coverage, identifier status, and verification limits are recorded in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). The manuscript was opened at its [readable PDF copy](https://mathcommunity.github.io/oai-math-revised/papers/Spontaneous-magnetization-in-the-quantum-Heisenberg-ferromagnet-September-24-2026/paper.pdf).

The prescribed ten-minute literature stage was sufficient to find this result. Stopped at step 1 as instructed. No original theorem, numerical computation, PROOF.md, or data file is claimed.

Checks: compared the manuscript's theorem against the released formal statement and implementation; checked the Hamiltonian sign, edge counting, spin range, fixed positive temperature, zero-field equilibrium condition, and the conversion ℓ/8 = S/4. The paper explicitly separates its state-existence conclusion from a finite-volume two-point criterion. These checks establish relevance, not proof validity.

Commands and web queries are in [LOG.md](LOG.md). Writes used `apply_patch`. No git, subagents, accounts, posts, email, or writes outside this folder. No numerical program was run. Attempts to apply `nice -n 15` to shell reads were denied by the sandbox; the restriction and failed source-access routes are logged.

Uncertainty: the full analytical proof and Lean dependency chain were not audited or compiled; no peer-review status or arXiv identifier was established. Next worker: review this preprint and its formalization before treating the brief's open-status assertion as settled or investing in a new proof. In particular, distinguish the requested magnetized KMS state from any separately desired finite-volume correlation statement.

Task: “push this problem forward by one checkable piece” — session start 2026-11-14 20:52 +04; user-message clock time unavailable.
