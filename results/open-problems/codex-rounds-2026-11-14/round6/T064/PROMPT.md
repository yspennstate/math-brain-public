# Open problem T064: Percolation description of the nodal lines of random waves (Bogomolny–Schmit)

Statement: The nodal set of the random plane wave (the centred Gaussian field on R^2 with covariance J_0(|x − y|)), and conjecturally of high-energy eigenfunctions of chaotic billiards, has the large-scale behaviour of critical percolation: crossing probabilities of nodal domains converge to Cardy's formula and nodal lines to SLE(6).

Caveat: The predicted number of nodal domains per unit area, (3√3 − 5)/π times a normalisation, is off by a few percent in numerics (Nastasescu 2011; Beliaev–Kereta 2013), so the conjecture is the scaling-limit statement, not that constant.

Source: E. Bogomolny and C. Schmit, Percolation model for nodal domains of chaotic wave functions, Phys. Rev. Lett. 88 (2002); M. V. Berry, Regular and irregular semiclassical wavefunctions, J. Phys. A 10 (1977)

Where it stands (checked by us, Nov 2026): The number of nodal domains grows like a constant times the area (Nazarov–Sodin 2009, 2016). Russo–Seymour–Welsh bounds and sharp thresholds hold for positively correlated planar Gaussian fields with fast decay (Beffara–Gayet 2017; Rivera–Vanneuville 2019; Muirhead–Vanneuville 2020). The random plane wave correlates slowly and changes sign, so none of this applies; open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T064 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T064 (read it, never
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
VERDICT: PROVED explicit determinant-weighted saddle law and exact residual-field level comparison

The round-4 crossing-stability bound holds. Its script passed again,
and an independent Fourier–Bessel derivation recovers its saddle
height intensity phi(t) exp(-t^2)/(4 pi). No solution of the Cardy/SLE(6)
conjecture was found in the five-minute literature check.

New beyond round 4: the full conditional field required by the
proposed pivotal Kac–Rice estimate is explicit. Under the normalized
saddle determinant weighting at height t,

    F_t(r,theta) = t J0(r)
        + 2 sqrt(t^2+G) J2(r) cos(2 theta-Theta)
        + independent Gaussian Fourier modes n>=3,

where G has Gamma(2,1) distribution and Theta is independent uniform.
In particular det Hess F_t(0)=-G/4. Ordinary first-jet Gaussian
conditioning would give the wrong second-mode law.

Put H_t=F_t-t J0. On every centered annulus of positive width,

    TV(Law(H_t), Law(H_s)) = delta(|t^2-s^2|),
    delta(a) = (1-exp(-a)) exp(-a/(exp(a)-1)) <= min(1,a/e),
    delta(0)=0.

Thus comparison with zero has exact error t^2/e+O(t^6). A shared-mode
coupling also has expected uniform field difference outside radius R
bounded by

    |t-s| M0(R) + (sqrt(pi)/2)|t^2-s^2| M2(R),

where Mj(R)=sup_(r>=R)|Jj(r)|=O(R^(-1/2)), j=0,2. PROOF.md proves
these statements and gives the interior threshold density with the
global pivotality mark retained. These are derived identities; no
literature priority is claimed.

Commands:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T064/check_local_threshold.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_saddle_palm.py
```

Both passed. The new audit used 13.34 MiB peak RSS and 0.038 seconds,
with actual niceness 20. Independent density quadrature and maximized
CDF differences checked the total variation formula; spectral-angle
integration checked the Fourier normalization; direct tilted moments,
circle statistics and near-degenerate saddles checked the other
constants. Full output is in LOG.md. The proof does not depend on
numerical quadrature.

What failed and remains unresolved: uncentered Palm laws at distinct
levels have total variation one, even on a distant annulus, because
their circle means reveal the conditioned height. More importantly,
saddle arms concern F_t-t=H_t-t(1-J0(r)); subtracting t J0 leaves a
radial threshold asymptotic to t. The residual-law comparison does
not remove that threshold. There is no new arm decay estimate, RSW
bound, enlargement of the o(R^(-2)) sufficient level window, or
conformal limit. Literature novelty was not established, and the
bounded search cannot certify absence of a later solution.

Sources actually opened: Stephen Muirhead, Alejandro Rivera and Hugo
Vanneuville, with an appendix by Laurin Köhler-Schindler,
*The phase transition for planar Gaussian percolation models without FKG*,
[arXiv:2010.11770v3](https://arxiv.org/abs/2010.11770v3), for threshold
genericity and measurability; Dmitry Beliaev, *Gaussian fields and
percolation*, [arXiv:2207.13448](https://arxiv.org/abs/2207.13448),
for the Fourier–Bessel representation. Bessel formulas were checked
in DLMF Sections 10.2, 10.17 and 10.23, linked in PROOF.md.

Next worker: use (2) of PROOF.md as the exact sampling or analytic law
for determinant-weighted four-arm probabilities. For a measurable
annular arm event, its probability under H_t differs from that under
F_0 by at most delta(t^2), even when the chosen event depends on t.
The remaining comparison is between zero arms and arms at the radial
level t(1-J0(r)); quantify that stability or obtain direct large-radius
arm decay under F_0. Boundary pivotal estimates remain separate.

Only this folder was changed; no git or external writes. The shell's
nice warning is documented; the scripts verified inherited niceness.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 07:53 Asia/Tbilisi (session launch; the
message receipt time was not separately recorded).
