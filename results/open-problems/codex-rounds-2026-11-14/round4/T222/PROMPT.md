# Open problem T222: Steele's variance-limit conjecture for the planar Euclidean traveling salesman problem

Statement: Let X_1,...,X_n be independent uniform points in [0,1]^2 and let L_n be the length of the shortest closed Euclidean tour through them. Prove that Var(L_n) converges to a constant as n tends to infinity, and identify that constant if possible.

Caveat: The variance here is unscaled, for the total tour length in the fixed unit square. This is a fluctuation question, distinct from T156, which asks for the constant in the first-order law L_n/sqrt(n). It is not the mean-field traveling salesman model with independent edge costs, and it is not a variance statement about an approximation algorithm. A central limit theorem alone without variance control would not establish the assertion.

Source: S. Chatterjee, A general method for lower bounds on fluctuations of random variables, arXiv:1706.04290, Section 3, open problem (2)

Where it stands (checked by us, Nov 2026): The opened source explains that upper fluctuation bounds are well understood and recalls Rhee's lower bound of the correct order in dimension two. It still poses variance convergence explicitly. The inspected recent papers on finite-temperature mean-field optimization, one-dimensional bipartite tours and neural tour solvers do not establish this planar zero-temperature variance limit. No closing theorem was found in the recorded current-status searches. Open.

Earlier work: a previous worker spent one session on this problem. Its folder is ~/codex_op_1114/briefs/T222 (read it,
never edit it). Its REPORT.md is copied below. Read its REPORT.md, LOG.md, PROOF.md and scripts before you start.

Later work: a round 3 worker built on that session. Its folder is ~/codex_op_1114r3/briefs/T222 (read it,
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
VERDICT: PARTIAL a sharper asymptotic interaction-energy bound for the exact planar TSP

The variance-limit conjecture remains open. The earlier reduction checks
out. This session sharpens its asymptotic constant by more than a factor
of two, without a localization assumption for optimal tours.

With the earlier notation V_{n,j} for the order-j Hoeffding energies, put
E_n=sum_{j>=1}j V_{n,j}. The new result is

\[
 \limsup_{n\to\infty} E_n\le\kappa<\frac2\pi,
 \qquad
 \kappa=\min_{c\ge0}\left\{
 c^2+\frac4\pi e^{-\pi c^2}
 -2c\operatorname{erfc}(\sqrt\pi c)\right\}.
\]

The previous report gave 4/pi. The minimizer c_* is unique and satisfies

\[
 c_*=2c_*e^{-\pi c_*^2}+\operatorname{erfc}(\sqrt\pi c_*).
\]

Consequently the earlier reduction has the sharper errors

\[
 \limsup_n\sum_{j>m}V_{n,j}\le\frac\kappa{m+1},\qquad
 \limsup_n\bigl(\operatorname{Var}(L_n)-C_n(\rho)\bigr)
 \le\kappa(1-\rho).
\]

In particular limsup Var(L_n)<=kappa. These are bounds for the exact
optimal closed tour through uniform points in the fixed unit square.
Kappa is not a candidate value for the conjectured limiting variance.
No comparison with the best published variance upper bound is claimed.

The proof uses the insertion interval 0<=d<=2R, where R is the nearest
base-point distance. Conditional variance permits centering sqrt(n)d
at any constant c. The squared error is bounded by the larger of the
two endpoint errors. Since sqrt(n)R converges to a variable Z with
P(Z>z)=exp(-pi z^2), with a uniform Gaussian tail controlling moments,
the endpoint envelope has the expectation displayed above. This handles
the square's boundary explicitly. Taking c=1/sqrt(pi) proves the strict
bound kappa<2/pi by elementary integral inequalities; no decimal
approximation or numerical optimization is used.

PROOF.md supplies every step. It also proves that kappa is the exact
largest possible Var(Y) among scalar couplings satisfying 0<=Y<=2Z
with this marginal law of Z. The extremizer is
Y=2Z 1_{Z>c_*}. This is a limitation of the scalar-envelope argument,
not a realizable TSP insertion law asserted by the proof.

AUDIT.md independently checks the energy by replacement pairs, recomputes
the constant from exponential truncated moments, checks the derivatives
through threshold integrals, and tests boundary and singleton cases.
An oscillating product-space example shows why even the sharper bound
does not force variance convergence. No error in the earlier result or
the new bound was found. All checks are exact analytic calculations;
there is no simulation, generated dataset, or numerical script.

The bounded literature check found no closing theorem. The source actually
opened was Sourav Chatterjee, *A general method for lower bounds on
fluctuations of random variables*, arXiv:1706.04290, whose Section 3,
problem (2), states this conjecture:
https://arxiv.org/html/1706.04290v3.
This was a short update check, not an exhaustive review. No
SOLVED_ELSEWHERE.md was warranted.

Reproduce the artifact checks with:

```sh
env OMP_NUM_THREADS=1 nice -n 15 /bin/sh -c '
cat PROOF.md AUDIT.md
head -n 1 REPORT.md
wc -l LOG.md PROOF.md AUDIT.md REPORT.md
'
```

LOG.md records the reads, web queries, decisions and audit calculations.
The sandbox prints `nice: setpriority: Operation not permitted`; no
successful priority adjustment is claimed. Only short file reads were
run. All writes stay in this folder; no git or subagents were used.

What failed or remains uncertain: no fixed-order energy convergence,
fixed-noise covariance convergence, add-one stabilization, variance limit,
or limiting constant is proved. The scalar sharpness result shows that
another improvement needs information beyond the interval 0<=d<=2R
and the marginal nearest-distance limit. Novelty relative to the full
literature has not been established.

Next worker: return to V_{n,1}=n Var(E[L_n|X_1]), including the boundary,
or a fixed-noise covariance limit. Further geometry is needed; a local
insertion competitor does not prove that the optimal tour rearranges
locally. The sharper truncation errors are available once a geometric
limit is established.

Task: "take the NEXT checkable step on this problem, building on that work"
— T222, 2026-11-15 approximately 01:40 Asia/Tbilisi (recorded task time).
