# Open problem T089: The Bohigas–Giannoni–Schmit conjecture

Statement: For a classically chaotic quantum system, for example the Dirichlet Laplacian on a planar billiard Ω whose billiard flow is ergodic and hyperbolic (the Bunimovich stadium, the Sinai billiard), restricted to one symmetry class and with time-reversal symmetry, let x_j = |Ω|λ_j/4π be the eigenvalues unfolded by Weyl's law. As Λ → ∞, the x_j with λ_j in [Λ, 2Λ] have the local statistics of the Gaussian Orthogonal Ensemble; in particular the nearest-neighbour spacing distribution converges to the GOE (Gaudin) law.

Caveat: Arithmetic examples (hyperbolic surfaces from quaternion algebras) have Poisson-like statistics, so a theorem needs a genericity hypothesis, and there is no agreed form of one. Bohigas, Giannoni and Schmit (doi:10.1103/PhysRevLett.52.1) state the conjecture from numerics on the Sinai billiard.

Source: O. Bohigas, M.-J. Giannoni and C. Schmit, Characterization of chaotic quantum spectra and universality of level fluctuation laws, Phys. Rev. Lett. 52 (1984), 1–4

Where it stands (checked by us, Nov 2026): GOE statistics are not proved for any chaotic billiard or manifold. Support comes from periodic-orbit expansions of the spectral form factor (Berry 1985; Sieber–Richter 2001; Müller–Heusler–Braun–Haake–Altland 2004) and from numerics. Rigorous results concern eigenfunctions rather than eigenvalues: quantum ergodicity (Shnirelman 1974; Zelditch 1987; Colin de Verdière 1985) and arithmetic quantum unique ergodicity (Lindenstrauss 2006). Arithmetic exceptions: Poisson-like spacings for arithmetic surfaces (Bogomolny–Georgeot–Giannoni–Schmit, Phys. Rev. Lett. 69 (1992), 1477; Bolte–Steil–Steiner, Phys. Rev. Lett. 69 (1992), 2188) and the number variance on arithmetic hyperbolic surfaces (Luo–Sarnak, Comm. Math. Phys. 161 (1994)).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T089 (read it,
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
VERDICT: PARTIAL quantitative empty-interval reduction for nearest-neighbour spacings

[PROOF.md](PROOF.md) proves a finite-window estimate and an asymptotic
equivalence for the nearest-neighbour part of T089. If N unfolded levels lie
in a window of length W, rho=N/W, and their cyclic empty-interval function
differs from the target integrated survival function by at most delta on
[0,S+h], then

\[
\sup_{0\leq s\leq S}|F_N^{\mathrm{int}}(s)-F(s)|
\leq \frac1N+
\frac{2\delta/h+\omega_F(h)+|\rho-1|}{\rho}.
\]

Here 0<h<=S and omega_F is the target CDF's modulus of continuity on the
relevant compact interval. The 1/N term removes the artificial cyclic gap.
Physical and cyclic empty probabilities differ by at most s/W. Both of these
edge constants are attained in the finite checks. A finite grid of mesh eta
adds at most eta to the empty-function error.

For a Lipschitz target, optimizing h gives an O(sqrt(delta)) bound. An explicit
family of exact finite spectra proves this exponent is optimal in the general
class: its CDF error is k/N and its empty-function error is (k/N)^2. This
sharpness example uses a uniform target, not GOE. No optimality claim specific
to GOE is made.

Weyl's law makes rho tend to one when the unfolding uses the symmetry sector's
own leading coefficient. Thus proving convergence of the microscopic
empty-interval function to the GOE integrated survival function is equivalent
to the spacing assertion. Full point-process convergence is not proved by
this reduction. The elementary identities are not claimed as new discoveries.

The exact audit is [check_reduction.py](check_reduction.py), with data in
[audit_data.json](audit_data.json) and captured output in
[audit_output.txt](audit_output.txt). Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_reduction.py > audit_output.txt 2>&1
```

Final run: exit status 0; 455 small configurations; independent geometric and
integrated-CDF checks; 17 exact sharpness cases; and 120 further theorem
checks using the full CDF supremum, including both signs of the density
error. Of the latter, 45 gave an internal-spacing bound below one. Runtime
was 2.628 seconds and peak RSS was 15,974,400 bytes, with inherited nice 20
and one process. All mathematical audit arithmetic uses rational numbers.

The sandbox rejected attempts to set OS memory limits and printed a warning
for `nice`; the process was independently verified to inherit nice 20. The
small audit instead used measured RSS/time guards. The initial launch failed
at the resource-limit call before any cases ran; no mathematical check failed.
The complete command history and relevant output are in [LOG.md](LOG.md).

The literature check found related random-family and mesoscopic advances,
recorded with opened primary references in
[SOLVED_ELSEWHERE.md](SOLVED_ELSEWHERE.md). It found no resolution of the
fixed-billiard microscopic problem within the ten-minute search limit.

What remains uncertain is the essential spectral estimate, not the finite
reduction: no chaotic billiard is shown here to satisfy the empty-interval
criterion. There is also no agreed genericity hypothesis. The next worker
should target equation (10) of PROOF.md for one explicitly specified symmetry
sector, or derive a certified finite-energy bound for that quantity. A smooth
variance estimate cannot simply be differentiated into the missing result.

Task: "push this problem forward by one checkable piece" — received
2026-11-14 approximately 20:54 Asia/Tbilisi (UTC+04).
