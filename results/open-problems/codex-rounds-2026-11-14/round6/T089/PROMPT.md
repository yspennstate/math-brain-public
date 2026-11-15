# Open problem T089: The Bohigas–Giannoni–Schmit conjecture

Statement: For a classically chaotic quantum system, for example the Dirichlet Laplacian on a planar billiard Ω whose billiard flow is ergodic and hyperbolic (the Bunimovich stadium, the Sinai billiard), restricted to one symmetry class and with time-reversal symmetry, let x_j = |Ω|λ_j/4π be the eigenvalues unfolded by Weyl's law. As Λ → ∞, the x_j with λ_j in [Λ, 2Λ] have the local statistics of the Gaussian Orthogonal Ensemble; in particular the nearest-neighbour spacing distribution converges to the GOE (Gaudin) law.

Caveat: Arithmetic examples (hyperbolic surfaces from quaternion algebras) have Poisson-like statistics, so a theorem needs a genericity hypothesis, and there is no agreed form of one. Bohigas, Giannoni and Schmit (doi:10.1103/PhysRevLett.52.1) state the conjecture from numerics on the Sinai billiard.

Source: O. Bohigas, M.-J. Giannoni and C. Schmit, Characterization of chaotic quantum spectra and universality of level fluctuation laws, Phys. Rev. Lett. 52 (1984), 1–4

Where it stands (checked by us, Nov 2026): GOE statistics are not proved for any chaotic billiard or manifold. Support comes from periodic-orbit expansions of the spectral form factor (Berry 1985; Sieber–Richter 2001; Müller–Heusler–Braun–Haake–Altland 2004) and from numerics. Rigorous results concern eigenfunctions rather than eigenvalues: quantum ergodicity (Shnirelman 1974; Zelditch 1987; Colin de Verdière 1985) and arithmetic quantum unique ergodicity (Lindenstrauss 2006). Arithmetic exceptions: Poisson-like spacings for arithmetic surfaces (Bogomolny–Georgeot–Giannoni–Schmit, Phys. Rev. Lett. 69 (1992), 1477; Bolte–Steil–Steiner, Phys. Rev. Lett. 69 (1992), 2188) and the number variance on arithmetic hyperbolic surfaces (Luo–Sarnak, Comm. Math. Phys. 161 (1994)).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T089 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T089 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T089 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T089 (read it, never
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
VERDICT: PARTIAL GOE target remainder below 10^-6 at order 10 instead of 58

The round 4 bound and its order-58 constant hold. An independent audit
checked 150 exact evaluations by two formulas, 2,145 binomial identities,
and 16,245 target-only comparisons for 57 rational count laws, including
a rare count-64 cluster. The main claim was also re-derived analytically.

The new result is a Vandermonde bound for every GOE bulk factorial moment,
proved in [PROOF.md](PROOF.md). If Z_s counts the unit-intensity GOE bulk
points in (0,s] and b_k(s)=E binom(Z_s,k), it gives

\[
\sup_{0\leq s\leq2}b_{10}(s)
\leq\frac{517386}{10^{12}}<10^{-6},
\qquad
\sup_{0\leq s\leq2}b_{20}(s)<10^{-89}.
\]

Thus the predecessor's proposed order-20 target is proved. The preceding
target-only comparison now needs ten empirical moment errors:

\[
\sup_{s\leq2}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{j=1}^{10}\sup_{s\leq2}|a_j(s)-b_j(s)|
+\frac{517386}{10^{12}}.
\]

The grid version adds its target-table errors and grid mesh as before.
The first even orders for this new rational bound to reach 10^-6 are
6,8,10 at R=1/2,1,2. These are thresholds of the bound, not of the
actual GOE moments.

The proof applies Newton divided differences only to the smooth rows and
columns of the orthogonal sine Pfaffian. Their congruence extracts a full
Vandermonde factor. Fourier derivative bounds control the remaining rows;
monic Chebyshev polynomials bound the Vandermonde on an interval. The
discontinuous sine-integral block is left untouched. The kernel convention
was checked in Alexander I. Bufetov, Pavel P. Nikitin, Yanqi Qiu,
*On Number Rigidity for Pfaffian Point Processes*,
[arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.
No novelty is claimed for the standard interpolation or determinant tools.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_repulsion.py > repulsion_output.txt 2>&1
```

Both passed. The new audit compares 72 exact fourth-power evaluations
against an independently constructed entrywise envelope matrix. It checks
20 polynomial-kernel congruences, including reversed and tightly clustered
nodes, 440 recursive versus barycentric divided differences, 40 determinant
versus Pfaffian identities, and 72 exact Vandermonde matrix cases. The
polynomial models check algebra; they are not GOE samples. Exact constants
are in [repulsion_data.json](repulsion_data.json).

The runs took 0.563 and 0.329 seconds, with measured peak RSS below 18 MB,
one process, standard-library arithmetic, and inherited nice=20. The sandbox
prints a setpriority warning; each script independently verifies its actual
priority. Measured memory/time guards were used; no OS-enforced cap is claimed.

The crude estimate |Vandermonde|<=R^(k(k-1)/2) was too weak at order 20.
The Chebyshev bound supplies the missing interval factor. No mathematical
check of the final result failed. The discontinuous block, coincident-node
null set, smooth-block diagonal, normalization powers and k=1 endpoint
were checked separately; details and commands are in [LOG.md](LOG.md).

The under-five-minute literature check found no resolution of the fixed
chaotic-billiard microscopic spacing problem. The opened papers and their
scopes are recorded in the log. This is a bounded search result.

No billiard moment error was estimated, no billiard eigenvalues were
computed, and no certified GOE moment tables were produced. The BGS
conjecture remains unresolved. The new bound still loses information in
both Hadamard inequalities and the maximum bound on the Vandermonde.

Next worker: construct certified GOE target tables b_1,...,b_10 on a finite
grid in [0,2], using integration with rigorous error bounds, then insert
them into this ten-moment certificate. An alternative is to evaluate the
ordered Vandermonde integral rather than its maximum to sharpen (2).
Controlling empirical moment errors for a specified billiard symmetry
sector remains the central missing spectral input.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 08:09 Asia/Tbilisi (UTC+04).
