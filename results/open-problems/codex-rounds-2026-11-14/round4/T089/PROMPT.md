# Open problem T089: The Bohigas–Giannoni–Schmit conjecture

Statement: For a classically chaotic quantum system, for example the Dirichlet Laplacian on a planar billiard Ω whose billiard flow is ergodic and hyperbolic (the Bunimovich stadium, the Sinai billiard), restricted to one symmetry class and with time-reversal symmetry, let x_j = |Ω|λ_j/4π be the eigenvalues unfolded by Weyl's law. As Λ → ∞, the x_j with λ_j in [Λ, 2Λ] have the local statistics of the Gaussian Orthogonal Ensemble; in particular the nearest-neighbour spacing distribution converges to the GOE (Gaudin) law.

Caveat: Arithmetic examples (hyperbolic surfaces from quaternion algebras) have Poisson-like statistics, so a theorem needs a genericity hypothesis, and there is no agreed form of one. Bohigas, Giannoni and Schmit (doi:10.1103/PhysRevLett.52.1) state the conjecture from numerics on the Sinai billiard.

Source: O. Bohigas, M.-J. Giannoni and C. Schmit, Characterization of chaotic quantum spectra and universality of level fluctuation laws, Phys. Rev. Lett. 52 (1984), 1–4

Where it stands (checked by us, Nov 2026): GOE statistics are not proved for any chaotic billiard or manifold. Support comes from periodic-orbit expansions of the spectral form factor (Berry 1985; Sieber–Richter 2001; Müller–Heusler–Braun–Haake–Altland 2004) and from numerics. Rigorous results concern eigenfunctions rather than eigenvalues: quantum ergodicity (Shnirelman 1974; Zelditch 1987; Colin de Verdière 1985) and arithmetic quantum unique ergodicity (Lindenstrauss 2006). Arithmetic exceptions: Poisson-like spacings for arithmetic surfaces (Bogomolny–Georgeot–Giannoni–Schmit, Phys. Rev. Lett. 69 (1992), 1477; Bolte–Steil–Steiner, Phys. Rev. Lett. 69 (1992), 2188) and the number variance on arithmetic hyperbolic surfaces (Luo–Sarnak, Comm. Math. Phys. 161 (1994)).

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T089 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T089 (read it,
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
VERDICT: PARTIAL finite-order GOE correlation certificate for the spacing reduction

The earlier result holds. A fresh proof and an independent exact checker
verified its spacing bound on 455 configurations, at three densities and
three secant lengths: 4095 full-supremum checks, including 330 bounds below
one. All 17 earlier sharpness examples also passed.

The new result is in [PROOF.md](PROOF.md). For the count C(t,s) in a uniformly
shifted interval, define

\[
a_k(s)=\frac1W\int_0^W\binom{C(t,s)}k\,dt,\qquad
b_k(s)=\mathbb E_{\rm GOE}\binom{Z_s}k.
\]

If epsilon_k bounds |a_k-b_k| on [0,R], then

\[
\sup_{s\leq R}|V(s)-E_{\rm GOE}(s)|
\leq\sum_{k=1}^{2m}\epsilon_k+
\frac{(R\max\{2,R+1/2\})^{2m}(4m)^m}{(2m)!}.
\]

The proof uses adjacent finite Bonferroni sums and the standard GOE
Pfaffian kernel. The remainder depends only on the target; no empirical
high-count-tail hypothesis is imposed. A certified finite-grid version adds
the mesh width and target-table errors. Combining it with the earlier
reduction yields an explicit spacing certificate. Convergence of each fixed
interval-count moment at rational thresholds is sufficient for the spacing
limit. No novelty is claimed for inclusion–exclusion or the kernel formula.

As an attempted break, two exact unit-density periodic spectra have identical
full two-point correlation measures but different spacing laws. On a circle
of length 4 their points are {0,1/3,4/3,2} and {0,1/3,1,7/3}. Their cyclic
CDFs differ by 1/4 at s=1, and their empty probabilities differ by 1/12 at
s=4/3. Repeating the periods preserves the discrepancy as the window grows.
Their third interval-count moment separates them. These are artificial
spectra, not billiard eigenvalues, and their common two-point law is not GOE.

Reproduce from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_previous.py > recheck_output.txt 2>&1
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_certificate.py > certificate_output.txt 2>&1
```

Both commands passed. The new audit checked 29148 moment identities by two
independent geometric integrations, 16380 Bonferroni brackets, 15123
target-remainder comparisons, and 1365 grid certificates. The two runs used
about 0.78 and 2.92 seconds, with measured peak RSS below 17 MB and inherited
nice 20. Scripts use one process, the standard library, and measured RSS/time
guards; OS hard memory limits were not imposed. The sandbox emits a nice
warning despite the verified inherited priority.

One auxiliary recurrence initially failed its independent factorial-formula
check: it had a factor of two too many. That error was corrected in the
proof and code, and the full audit passed afterward. The direct truncation
formula above was unchanged. The first traceback remains in
[certificate_first_output.txt](certificate_first_output.txt).

The under-five-minute literature check found no resolution of the stated
fixed-billiard problem. Opened primary references and the search scope are
in [LOG.md](LOG.md). The kernel input was checked in Alexander I. Bufetov,
Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity for Pfaffian Point
Processes*, [arXiv:1810.09223](https://arxiv.org/html/1810.09223), Section 1.2.

The remaining uncertainty is the spectral input: no chaotic billiard is
shown to have small moment errors, and no billiard spectrum was computed.
The conservative GOE remainder needs orders 32, 78 and 390 at R=1/2,1 and 2
to become at most 10^-6. Thus the certificate is explicit but currently
costly to apply. It proves neither BGS nor a new universality special case.

Next worker: at R=2, sharpen the target remainder b_{2m}(2), using the
explicit kernel (10), until a certified 10^-6 remainder is obtained at a
substantially lower order than 390. Preserve the target-only comparison
(9). This makes the finite-energy certificate more usable; an actual
symmetry-sector estimate for a_k-b_k is still the essential BGS obstacle.

Task: "take the NEXT checkable step on this problem, building on that work."
— received 2026-11-15 approximately 01:19 Asia/Tbilisi (UTC+04).
