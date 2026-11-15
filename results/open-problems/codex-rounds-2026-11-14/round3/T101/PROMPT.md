# Open problem T101: Closed orbits in the Lorentz mirror model

Statement: At each vertex of Z^2 place, independently, a two-sided mirror along one of the two diagonals, each with probability p/2, or no mirror, with probability 1 − p. A light ray moving along the edges is reflected by mirrors and passes straight through empty vertices. Prove that for every p ∈ (0, 1) every orbit is periodic almost surely.

Caveat: For p = 1 the statement follows from critical bond percolation on Z^2. In three dimensions the opposite is expected at small p: infinite orbits with positive probability.

Source: T. W. Ruijgrok and E. G. D. Cohen, Deterministic lattice gas models, Phys. Lett. A 133 (1988); G. Grimmett, Percolation, 2nd ed. (Springer, 1999)

Where it stands (checked by us, Nov 2026): For p = 1 every orbit is closed, through critical bond percolation. Kozma and Sidoravicius showed that the probability that the ray reaches distance n is at least 1/(2n+1) at every mirror density (arXiv:1311.7437). arXiv:2610.12460 (2026) states that finiteness of all orbits on Z^2 is still a conjecture and builds infinite rays on other decorated planar graphs; arXiv:2609.14949 is a numerical study. Open for 0 < p < 1.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T101 (read it,
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
VERDICT: PARTIAL exact probability of vertex-simple periodic orbits with at most six mirrors

For a fixed directed lattice edge, the probability that its orbit is vertex-simple, periodic, and contains at most six mirrors is

\[
 B(p)=\frac{p}{8(2-p)^3}+\frac{p(1-p)^2}{4(2-p)^5}
 =\frac{p(6-8p+3p^2)}{8(2-p)^5}.
\]

The two terms count all rectangles and all L-shaped orthogonal hexagons, respectively, over arbitrary positive side lengths. Thus the probability of a periodic orbit is at least B(p). In particular its liminf after division by p, as p decreases to zero, is at least 3/128. At p=1/2 the bound is 11/486. The full almost-sure periodicity conjecture remains unresolved.

`PROOF.md` gives the shape classification, exact probability of each prescribed boundary, disjointness of rooted-orbit events, translation counts, series evaluations, and a second derivation by perimeter. No novelty claim is made for this elementary restricted-family bound.

Verification command, run from this folder:

```sh
nice -n 15 env OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 python3 audit.py --max-length 14 --output audit_data.json
```

The independent walk enumeration gives four-turn counts 2, 6, 12, 20, 30, 42 at perimeters 4 through 14, and six-turn counts 0, 0, 16, 80, 240, 560. These agree with m(m-1) and 16 binom(m,4), where the perimeter is 2m. An independent reflection-table tracer exhausts all 19,683 environments in a three-by-three box and agrees with the geometric calculation at three rational densities. Five exact rational series checks bound the omitted tails below 10^-25. The final run used about 17.5 MB and 0.065 seconds, one thread, inherited nice 20. The `nice` warning is explained in `LOG.md`. Exact tail bounds are stored alongside decimal approximations, which can underflow to zero.

The bounded literature search found no solution or substantial advance for the stated square-lattice model. Opened sources include Gady Kozma and Vladas Sidoravicius, [arXiv:1311.7437](https://arxiv.org/abs/1311.7437); Martin P. W. Zerner, [arXiv:2610.12460](https://arxiv.org/html/2610.12460v1); and Jian Gu and Qin Hao, [arXiv:2609.14949](https://arxiv.org/html/2609.14949v1). Zerner's introduction explicitly retains the conjecture. Additional opened leads concerned a hierarchical model, loop weight 2, or the Manhattan lattice; references and search details are in `LOG.md`. This was a short search, not an exhaustive literature review.

What failed or remains uncertain: the search did not yield a proof of localization. No attempted mathematical claim failed its audit, but the initial decimal-only representation of tiny tail bounds was insufficient and was corrected. The formula omits simple orbits with eight or more mirrors and every orbit that repeats a vertex. The enumeration already finds 40 eight-turn simple polygons of perimeter 10; each has positive probability for 0<p<1, so B(p) is strictly smaller than the full periodicity probability. The result supplies no estimate forcing the probability of an infinite orbit to vanish.

Next work: derive and sum the eight-corner family, using the independent counts 40, 372, 1764 at perimeters 10, 12, 14 as audit targets. Such an extension would improve this explicit lower bound, but a solution of T101 still needs control of unrestricted orbit geometry. Do not identify vertex-simple polygons with all mirror trajectories.

Task: “push this problem forward by one checkable piece” — received approximately 21:58 Asia/Tbilisi, 14 November 2026.
