# Open problem T200: Exact intersection exponents of three-dimensional Brownian motion

Statement: Determine the three-dimensional Brownian intersection exponents xi_3(k,lambda), for integers k >= 1 and real lambda > 0. In the standard definition, k independent Brownian paths start at 0 and another starts at (1,0,0); Z_n is the conditional probability that the latter path avoids the first k until all have reached the sphere of radius exp(n), given the first k paths. Then xi_3(k,lambda) = -lim n^(-1) log E[Z_n^lambda]. In particular, determine xi_3(1,1).

Caveat: This is a question about exact values, not existence or analyticity of the exponents. The special value xi_3(1,2)=1 is known. T103 concerns loop-erased random walk and its growth exponent; Brownian intersection exponents describe avoidance of independent un-erased paths and a whole moment family.

Source: Y. Gao, X. Li, Y. Li, R. Liu and X. Liu, A boundary Harnack principle and its application to analyticity of 3D Brownian intersection exponents, arXiv:2411.14921 (2024), Section 1.1

Where it stands (checked by us, Nov 2026): Gao and collaborators prove real analyticity in lambda for every positive integer k (Theorem 1.1); this does not identify the values. Liu (arXiv:2609.18643) proves the explicit bound xi_3(1,1)<0.9999. Shi, Liu, Li, Li and Deng (arXiv:2609.25968) give numerical estimates for several packet sizes and continuous moments, explicitly describing them as numerical. No general exact expression is known. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T200 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T200 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 4 worker built on that session. Its folder is ~/codex_op_1114r4/briefs/T200 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 5 worker built on the latest of these. Its folder is ~/codex_op_1114r5/briefs/T200 (read it, never
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
VERDICT: PARTIAL radial exit estimates and xi_3(1,1) < 0.9971

The exact-value problem remains unresolved. The completed extension is

\[
\xi_3(1,1)\leq1-\frac{2}{627\log3}
=0.997096525592896850419093332804\ldots<0.9971.
\]

The decimal evaluates the upper bound, not the exponent. Round 4's bound
was 0.9980977236643117... . Its energy identity, minimizing argument,
conditional capacity estimate and numerical certificate were independently
checked first; no defect was found. The new gap below one is 29/19 times
the preceding gap, an increase of about 52.6%.

The new piece is the radial exit estimate suggested by round 4. The time
for three-dimensional Brownian motion to go from radius r to radius 2r,
divided by r squared, has exactly the same law as the exit time of a
one-dimensional Brownian motion from (-1,1), started at zero. Both Laplace
transforms are sech(sqrt(2q)). Reflection and a certified rational Gaussian
tail bound give

\[
\mathbb P(\sigma_{2r}-\sigma_r<r^2/7\mid\mathcal F_{\sigma_r})
<16311/1000000.
\]

This permits a longer occupation time than round 4's r squared/18.
Retaining its optimal deterministic time weight and factor-three layers,
the resulting conditional capacity estimate is

\[
\mathbb E\left[e^{-17\operatorname{cap}(K(r))/r}
\mid\mathcal F_{\sigma_r}\right]<13623/100000.
\]

For the sum T_N of normalized layer capacities, this yields

\[
\mathbb P(T_N<N/19)
\leq(333313941/1000000000)^N.
\]

The exceptional-tail exponent is 1.000052956527928... > 1.
Despite the small margin, the required comparison is the exact integer
inequality 999941823 < 1000000000. The earlier hitting estimate and
xi_3(1,2)=1 then prove the bound above. The full argument, including the
radial identity, Gaussian estimate, weighted energy and exponent comparison,
is in [PROOF.md](PROOF.md).

Reproduce from this folder:

```
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py baseline
OMP_NUM_THREADS=1 nice -n 15 python3 -B audit.py radial
```

The first prints `ROUND 4 RESULT VERIFIED independently`; the second prints
`ALL RADIAL-EXIT CERTIFICATE CHECKS PASSED`. All load-bearing scalar
inequalities use exact fractions. The Gaussian tail is certified twice,
by a rational Mills bound and an integrated Taylor series. A radial heat
equation expansion independently checks the exit law at four times.
Rational logarithm bounds, Decimal arithmetic and libm agree on the gap.
The baseline directly integrates the time potential using a substitution
different from round 4's; its error decreases from 5.40e-9 to 3.32e-10 on
doubling the mesh. These quadratures are diagnostics, not proofs.

Both audits complete in under one second, use one thread and have measured
peak RSS below 16 MiB. They check inherited nice 20 and a 60-second CPU
limit. The shell's nice warning reflects its unsuccessful attempt to add
15 to an already lower-priority process; the scripts verify actual priority
before computing. The exploratory command `OMP_NUM_THREADS=1 nice -n 15
python3 -B explore.py` is optional and supplies no proof certificate.
Commands and output are recorded in [LOG.md](LOG.md).

What failed: the simpler third Gaussian Mills convergent with the old
energy rounding does not support the chosen threshold; the fifth does.
The first full radial audit passed its exact comparisons but failed a
redundant Decimal check because a rational log interval was narrower than
the 60-digit context. Increasing the context to 80 digits fixed it without
changing proof constants. An initial edit patch was rejected atomically
and was reapplied with the correct context.

The audit checked the radial function at the origin, generator and scaling,
finite stopping times, transform uniqueness, reflection factors, Mills-bound
sign, endpoint singularities, occupation support, conditional iteration,
inward returns, initial hits, zero capacity, the last layer, noninteger
thresholds and interpolation in log-radius. No unresolved mathematical
defect was found. The full capacity argument is not optimized.

The web literature check ended within five minutes and found no later exact
evaluation. Sources actually opened and queries are listed in LOG.md.
In particular, Qiyuan Shi, Runsheng Liu, Xinyi Li, Ming Li and Youjin Deng,
*Intersection Exponents of Simple Random Walks in Two and Three Dimensions*,
[arXiv:2609.25968v1](https://arxiv.org/html/2609.25968v1), still describe their
three-dimensional results as numerical. This search does not establish
absence, priority or a best known bound. Neither the exit-time identity nor
the Gaussian rational approximation is claimed to be new. No exact exponent
or general moment formula was obtained.

The next worker should audit Sections 1–2 of PROOF.md first, especially
the generator normalization and the Gaussian tail factor. A concrete next
extension is to vary the segment radius a and layer spacing b instead of
fixing them at 2 and 3. For a segment from radius 1 to a>1, the same radial
calculation gives transform a sinh(sqrt(2q))/sinh(a sqrt(2q)); for b>a,
the Green minimum is 1/(1+a)-b/(b squared+a). A certified radial exit bound
for this two-geometry-parameter family could be carried through the same
moment argument. The present calculation makes no claim about its optimum.

Task: “take the NEXT checkable step on this problem, building on that work.”
T200, 15 November 2026, session began about 08:35 Asia/Tbilisi (UTC+04).
