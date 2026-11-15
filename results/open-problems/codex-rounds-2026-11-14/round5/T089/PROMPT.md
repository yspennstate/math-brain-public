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
VERDICT: PARTIAL GOE target remainder below 10^-6 at order 58 instead of 390

The earlier target-only comparison and its order-390 bound hold. An independent
exact checker verified 6,561 binomial identities, 36,125 comparisons for
85 rational count laws, and the old remainder by both a direct factorial
formula and a recurrence. Rare large clusters were included.

The new result is proved in [PROOF.md](PROOF.md). If Z_s is the unit-intensity
GOE bulk interval count and b_k(s)=E binom(Z_s,k), then

\[
\sup_{s\leq R}b_k(s)\leq
\frac{R^k}{k!}\left[k\left(k+\frac{\pi^2}{12}(k-1)\right)\right]^{k/4}.
\]

The proof combines the orthogonal sine kernel, the elementary inequalities
|I|<=1/2 and S^2+3D^2/pi^2<=1, and Hadamard's determinant bound after a
determinant-one diagonal congruence. The kernel was checked in Alexander I.
Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point
Processes*, [arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.
No novelty is claimed for these general linear-algebra ingredients.

At R=2 this gives the exact rational certificate

\[
\sup_{s\leq2}b_{58}(s)\leq913317/10^{12}<10^{-6}.
\]

It replaces the earlier certificate's order 390 by 58 without an empirical
count-tail assumption. Thus

\[
\sup_{s\leq2}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{j=1}^{58}\sup_{s\leq2}|a_j(s)-b_j(s)|+913317/10^{12}.
\]

The proof also gives the corresponding grid and spacing certificates. The
first even orders for the rational upper-bound formula to reach 10^-6 are
14,26,58 at R=1/2,1,2. These are thresholds of the bound, not of the actual
GOE moments.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_round3.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_remainder.py > remainder_output.txt 2>&1
```

Both commands passed. The new audit checks 150 exact factorial/product
evaluations and 120 rational matrix cases, comparing determinants and
Pfaffians independently and checking the scale change and row bounds.
Its exact constants are in [remainder_data.json](remainder_data.json).
The runs took 0.631 and 0.068 seconds, with measured peak RSS below 16 MB,
one process, standard-library arithmetic and inherited nice 20. The sandbox
prints a nice warning; each script independently checks its actual priority.
Measured memory/time guards were used; no OS-enforced cap is claimed.

No mathematical check failed. A second Cauchy–Schwarz proof verified the
kernel inequality. Partial sine lobes, negative arguments, I's jump at zero,
the diagonal contribution and the determinant square-root exponent were
checked separately. Two log-append patches failed without changing files;
their replacements succeeded. Details and outputs are in [LOG.md](LOG.md).

The under-five-minute web check found no resolution of the fixed-billiard
microscopic spacing problem. Opened primary sources and their precise scopes
are recorded in the log. This is a bounded search result.

No chaotic billiard moment error was estimated, no billiard eigenvalues were
computed, and no certified GOE moment tables were produced. The central BGS
obstacle is unchanged. The bound is still conservative; it discards most
repulsion between nearby points.

Next worker: retain the target-only comparison and construct certified GOE
factorial-moment tables on a finite grid in [0,2], or reduce the remainder
order further by retaining the near-diagonal repulsion in the Pfaffian. The
concrete analytic target is b_20(2)<=10^-6; the present bound does not show
this. Any numerical integration needs a rigorous error bound, not a Monte
Carlo estimate. Estimating a_j-b_j for one symmetry sector remains essential.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 04:46 Asia/Tbilisi (UTC+04).
