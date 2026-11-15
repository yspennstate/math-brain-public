# Open problem T078: Long-range order in the three-dimensional quantum Heisenberg ferromagnet

Statement: The spin-S quantum Heisenberg ferromagnet on Z^d, d ≥ 3 (H = −Σ_{x∼y} S_x · S_y), has spontaneous magnetization at low positive temperature, for every S ∈ {1/2, 1, 3/2, …}.

Source: F. J. Dyson, E. H. Lieb and B. Simon, Phase transitions in quantum spin systems with isotropic and nonisotropic interactions, J. Stat. Phys. 18 (1978); B. Simon, Fifteen problems in mathematical physics, in Perspectives in Mathematics: Anniversary of Oberwolfach 1984 (Birkhäuser, 1984)

Where it stands (checked by us, Nov 2026): Proved for the classical Heisenberg model (Fröhlich–Simon–Spencer 1976) and for quantum antiferromagnets (Dyson–Lieb–Simon 1978, d ≥ 3 and S ≥ 1; Kennedy–Lieb–Shastry 1988, S = 1/2 on Z^3). For the ferromagnet: low-temperature free energy given by spin-wave theory (bounds by Conlon–Solovej 1991; the spin-wave asymptotics in d = 3 by Correggi–Giuliani–Seiringer, arXiv:1312.7873, CMP 2015); order on the complete graph and on trees through the interchange representation (Tóth; Björnberg, arXiv:1512.06986; Hammond, arXiv:1202.1322). Open on Z^3.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T078 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T078 (read it,
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
VERDICT: PROVED optimal scalar field-selection criterion from a magnetization tail

The earlier report's scope check holds. OpenAI's September 24, 2026 manuscript claims precisely the required spontaneously magnetized KMS state. Independently read the manuscript, comparator and implementation. Also read the October 26 comparator log through its kernel-acceptance message, which the earlier worker had not established. This is reported formal verification, not a local reproduction or a complete mathematical audit. Details and references are in [SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md).

The mathematical addition is [PROOF.md](PROOF.md). Suppose M lies in [-V/2,V/2], V>0, and its zero-field law satisfies P(M>=V/4)>=L>0. Put z=bV/8, where b is the tilting parameter. The tilted mean is at least V/8 for every such scalar law exactly under these conditions:

    z<=1/5:   exp(6z) >= 5(1-L)/L;
    z>=1/5:   z exp(z) >= (1-L)/(eL).

The proof includes two-point extremizers, a second derivation and exact equality checks at z=0, 1/5 and 1. A separate convexity argument proves the convenient sufficient condition

    bV >= 8 log(1/L).

For the spin model, V=2S|Lambda| and b=beta h. This improves the source's sufficient selection condition bV>=16 log(11/L). With a surface-cost tail L=exp(-A)/2, the new sufficient field satisfies beta hV>=8(A+log 2). The optimality assertion concerns scalar laws with the stated support and tail; it need not be optimal on the physical magnetization spectrum. No novelty claim is made for the elementary extremal method.

This does not prove T078. The missing spatial input is still the uniform low-temperature magnetization tail. The source audit traced `field_ordered_cubes` through `physical_surface_bound`, `symmetrized_surface_bound` and `completed_surface_bound` to `mesh_matrix_surface`. That deeper estimate was not verified. No counterexample to the manuscript was found, and no improvement of its temperature threshold is claimed.

Commands and outputs are in [LOG.md](LOG.md). Work used web search/open/click, read-only shell inspection prefixed with `OMP_NUM_THREADS=1 nice -n 15`, and `apply_patch` for local files. A small curl directory request failed with DNS error. The sandbox rejected priority adjustments; no numerical computation, Lean build, heavy process, git command, subagent or external write was used. All mathematical checks are exact and written out.

Next worker: audit `mesh_matrix_surface` and the finite-mesh loop estimate supplying the surface tail. Start with [CompletedSurface.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/CompletedSurface.lean), line 31, and its `MeshRoom` import. The field-selection implication can now be used with the sharper bound proved here, but proving that implication does not verify its tail hypothesis.

Task: “take the NEXT checkable step on this problem, building on that work” — session start 2026-11-15 01:14 +04; exact user-message clock time unavailable.
