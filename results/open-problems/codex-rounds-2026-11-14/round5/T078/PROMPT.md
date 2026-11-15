# Open problem T078: Long-range order in the three-dimensional quantum Heisenberg ferromagnet

Statement: The spin-S quantum Heisenberg ferromagnet on Z^d, d ≥ 3 (H = −Σ_{x∼y} S_x · S_y), has spontaneous magnetization at low positive temperature, for every S ∈ {1/2, 1, 3/2, …}.

Source: F. J. Dyson, E. H. Lieb and B. Simon, Phase transitions in quantum spin systems with isotropic and nonisotropic interactions, J. Stat. Phys. 18 (1978); B. Simon, Fifteen problems in mathematical physics, in Perspectives in Mathematics: Anniversary of Oberwolfach 1984 (Birkhäuser, 1984)

Where it stands (checked by us, Nov 2026): Proved for the classical Heisenberg model (Fröhlich–Simon–Spencer 1976) and for quantum antiferromagnets (Dyson–Lieb–Simon 1978, d ≥ 3 and S ≥ 1; Kennedy–Lieb–Shastry 1988, S = 1/2 on Z^3). For the ferromagnet: low-temperature free energy given by spin-wave theory (bounds by Conlon–Solovej 1991; the spin-wave asymptotics in d = 3 by Correggi–Giuliani–Seiringer, arXiv:1312.7873, CMP 2015); order on the complete graph and on trees through the interchange representation (Tóth; Björnberg, arXiv:1512.06986; Hammond, arXiv:1202.1322). Open on Z^3.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T078 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T078 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T078 (read it,
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
VERDICT: PROVED smaller boundary-coloring cost for finite transposition meshes

The round 3 scalar field-selection criterion holds. An independent derivation is recorded in [LOG.md](LOG.md). The initial literature check found the same September 24, 2026 solution claim by OpenAI and its known companion claims, with no newly established resolution or correction. The manuscript was opened; its full proof remains unaudited here. T078 is not proved by this work.

The new result is a boundary-cost estimate in [PROOF.md](PROOF.md). In a finite exchange mesh, let D be a set of slots, let r_j be the independent base activation probabilities, and let X contain exactly the transpositions crossing between D and its complement. Weight each picture by 2 to the number of cycles and color the cycles independently and fairly. Then

    P(all cycles visiting D are up)
      >= 2^(-|D|) product_(j in X) (1+r_j)^(-1).

The proof counts one directed exit per active crossing transposition and uses the exact conditional activation bound 2r/(1+r). It does not assume independent marks after loop weighting. An algebraic partition-weight argument checks the conditional factor a second way. Two-slot examples and all endpoint cases are checked exactly; the estimate is not asserted to be optimal.

For repeated spatial sweeps at rate delta/2 and fixed time t, the boundary factor becomes

    exp[-|D| log 2 - t J_cross/2].

A separate Poisson insertion argument re-derives the coefficient 1/2. The inspected source instead uses exp[-|D| log 2 - 2 log(2) t J_K], where J_K>=J_cross also counts edges with both endpoints in D. This sharpens the boundary cost in the next dependency named by round 3, rather than repeating the field-selection improvement.

If the boundary-pinned law makes every slot's avoidance probability at most p<1/2, the corresponding zero-field magnetization tail at one quarter of the slot count is at least 1-2p times the proved boundary factor. That spatial hypothesis remains unproved here. The audit traced `mesh_matrix_surface` to `mesh_surface_tail` in MeshSurface.lean, whose inputs are `mean_boundary_cycles` in BoundaryMesh.lean and `Bootstrap.mesh_pin_bound`. The result improves the former input; it does not verify the latter, the physical-spin projection, or the infinite-volume state construction. No source error or improved temperature threshold is claimed.

Commands: read prior files using `cat`, inventory using `rg --files` and `find`, and inspect local artifact sizes using `wc`. Shell reads after the initial inventory used `OMP_NUM_THREADS=1 nice -n 15`; priority adjustments were denied by the sandbox. No numerical script or Lean build was run. All mathematical verification is written out exactly. Web search/open/click supplied the literature and Lean sources linked in PROOF.md. Local edits used `apply_patch`. The initial brain recall was interrupted after an unexpected ONNX import; its internal logging was not inspected. No git or subagents were used; all explicit file edits stayed in this folder.

Access failures: guessed MeshSurfaceTail.lean returned 404, while MeshSurface.lean opened successfully; GitHub directory/API listings failed. They do not indicate missing mathematical dependencies. These failures and the priority restriction are recorded in LOG.md.

Next worker: audit `mesh_pin_bound` in [MeshPin.lean](https://raw.githubusercontent.com/openai/math/main/lean/OAI/MathematicalPhysics/Heisenberg/MeshPin.lean), especially `periodic_return_estimate` (line 45), `regularity_of_pin_induction` (line 46), and the uniform parameter choice (lines 47–49). The single-slot avoidance bound is sufficient for the tail proved here. Establish it uniformly in volume, or locate a failed hypothesis; another scalar tilt or boundary-cost estimate will not supply that spatial input.

Task: “take the NEXT checkable step on this problem, building on that work” — session start 2026-11-15 04:40 +04; exact user-message clock time unavailable.
