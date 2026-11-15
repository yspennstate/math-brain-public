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

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T078 (read it, never
edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

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
VERDICT: PROVED sparse injection energy bound on the full cubic lattice, with sharp displacement power and sparsity threshold

The round 4 boundary-coloring estimate holds. LOG.md gives an independent partition-sum recheck, including its continuous-time coefficient and conditional magnetization implication. The initial literature check found the same previously known solution claim; no new resolution or correction was established. T078 remains unproved by this work.

The new result in [PROOF.md](PROOF.md) is spatial. Suppose m source labels on Z^3 satisfy the local counting bound L(1+r)^alpha, with 0<=alpha<1. Each label may distribute mass at most one within distance R. There are unit currents from the injection sites to infinity whose aggregate energy, counting each undirected edge once, is at most

    1000 L (1+R)^alpha m/(1-alpha).

The same estimate holds for the killed Dirichlet problem in every finite containing volume. Its proof derives the lattice Green bound explicitly, then uses a counting integral. It implies a linear capacity lower bound for sparse sets. The displacement exponent alpha is necessary: labels at floor(j^(1/alpha)) can send all mass to zero and require energy at least m^2/6. At alpha=1 a line segment has energy at least m log(m)/(16pi^2), ruling out a uniform linear estimate even with R=0. No novelty claim is made for these potential-theory arguments.

This verifies the unperforated three-dimensional special case of the spatial injection estimate identified in [RegularKernels.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularKernels.lean), and allows every alpha<1 in that case. The source uses alpha=1/100 and additionally handles removed sites under regularity hypotheses. Those hypotheses and the detour construction remain unverified. The full-lattice Green comparison cannot prove that extension: removing conductances can increase the required energy. No source error or improved temperature threshold is claimed.

Checks: a dyadic derivation independently verifies the displacement power and exponent threshold; two different Fourier integration regions verify the endpoint logarithm; the one-site test and the walk's initial holding time independently check the factor six. Edge summation and the Fourier symbol check the energy convention. All estimates and endpoint cases are written out in PROOF.md.

Commands: `rg --files` and `ls -la` inventoried prior work; `OMP_NUM_THREADS=1 nice -n 15 cat ...`, `sed ...`, and `wc -l -c ...` read and checked files. Web search/open performed the brief literature check; read-only GitHub connector fetch/search located the spatial dependencies. The immutable RegularKernels.lean content was fetched and matched to the inspected main-branch content. `apply_patch` wrote only this folder. The sandbox denied priority adjustments; no numerical script, heavy program, Lean build, git command, or subagent was run. No shared memory/checklist/mesh store was mutated because the task forbids writes outside this folder.

Access failures: the previously readable manuscript PDF and several guessed source paths failed; the actual source directory and theorem locations were subsequently found with the connector. These failures supply no evidence against the manuscript. The proof here is independent of the manuscript's correctness.

Next worker: audit `regular_component_envelope` in [RegularComponents.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/RegularComponents.lean) and `connected_envelope` in [FlowCongestion.lean](https://github.com/openai/math/blob/4eaee87548250b2682affda7d05d947c05554bae/lean/OAI/MathematicalPhysics/Heisenberg/FlowCongestion.lean). These are the calls in `regular_injection_energy` that replace the full lattice by the complement of removed sites. Establish a uniform current construction under their exact assumptions, or locate a failed assumption. The source's random regularity and return comparison would still require separate checks afterward.

Task: “take the NEXT checkable step on this problem, building on that work” — session start 2026-11-15 08:03 +04; exact user-message clock time unavailable.
