# T064 work log

Task: “take the NEXT checkable step on this problem, building on
that work.” Session launch: 15 November 2026, 07:53:34 Asia/Tbilisi
(03:53:34 UTC), from this folder's run.pid creation time. The user-message
receipt time was not separately recorded. The first tool clock reading
is 03:54:12 UTC.

## Orientation and literature check (less than five minutes)

Read the three earlier REPORT.md and LOG.md files, both existing PROOF.md
files and scripts. The original folder has no proof or script. Some
combined reads were truncated; bounded follow-up reads recover those
parts below. Prior folders are read-only throughout.

Read startup memory index and compute state: `warn`, `owner_away_open`,
CPU saturated. Only small standard-library audits are planned. The
folder-only write instruction overrides shared brain, mesh and checklist
writes; no such writes, git operations or agents were used.

Web search queries:

- `random plane wave percolation Cardy SLE 6 conjecture 2025 2026 nodal`
- `random plane wave crossing probabilities pivotal saddles percolation 2026`
- `"random plane wave" "2026" percolation crossing`
- `"random plane wave" "2025" percolation Cardy`

Opened https://arxiv.org/abs/2010.11770,
https://arxiv.org/html/2010.11770v3,
https://arxiv.org/abs/2207.13448 and
https://arxiv.org/html/2207.13448. The publisher URL
https://link.springer.com/article/10.1007/s00440-025-01367-8 timed out.
No solution of the Cardy/SLE conjecture was located. The noncritical
phase transition without FKG is already covered by the first report;
it does not settle this problem. Search results about square-lattice
random-cluster interfaces do not concern random waves. The search is
bounded and cannot certify exhaustive absence of a solution.

Opened Lemma 2.9 and Appendix B.4 of arXiv:2010.11770v3 to check the
topological inputs of round 4. Opened DLMF section 10.17 for fixed-order
Bessel large-radius asymptotics. This subsequent reading checks proof
inputs rather than extending the novelty search.

Read commands used `cat` and `rg --files`; initial lightweight discovery
lacked the requested nice/thread prefix. Later shell commands use
`env OMP_NUM_THREADS=1 nice -n 15 ...`. macOS reports
`nice: setpriority: Operation not permitted`; the computational script
independently verifies inherited niceness 20.

## Re-check of round 4

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B ~/codex_op_1114r4/briefs/T064/check_local_threshold.py
```

Result: PASS, elapsed 0.180 s, peak RSS 13.17 MiB, actual niceness 20.
Conditional jet error 5.305e-10; interval integral error 5.107e-15;
24 interval and 644 pointwise comparisons passed. Total saddle density
0.045944074618; four-corner factor 1.000000000000. All eight edge
normal-form and four affine corner cases passed.

Independent algebraic derivation: in the Fourier–Bessel expansion,
the second-mode coefficients a2,b2 are independent standard normals.
Put U=(a2^2+b2^2)/2, so U has exponential density exp(-u). Conditional
on f=t and grad f=0, det Hess f=(t^2-U)/4. Hence

    E[(-det Hess f)_+] = integral_(t^2)^infinity
                            (u-t^2)exp(-u)du/4
                         = exp(-t^2)/4.

Multiplying by the gradient zero density 1/pi and phi(t) recovers
round 4's area density. The four boundary normal forms agree with the
strict-path argument of Lemma B.4. Their one-sided means and the four
corner quadrants recover the other terms. The earlier bound holds;
there is no reason here to revise its verdict.

## Chosen extension (recorded before derivation)

Derive an explicit determinant-weighted saddle field law, together with
a level comparison for that law. This is the conditional field actually
required by the preceding report's proposed pivotal Kac–Rice estimate.
An ordinary Gaussian field conditioned on its first jet is not enough:
the Hessian determinant changes its distribution.

Target: isolate the low Fourier modes, identify the size-biased radial
distribution of mode two, and couple different levels. If possible,
compute the total variation distance after removing the deterministic
radial mean. Check explicitly why this does not yet compare four-arm
events at their own levels. No unproved arm exponent will be assumed.

## Derivation and independent audit, by 07:59 Asia/Tbilisi

Created PROOF.md and check_saddle_palm.py. The law is

    F_t = t J0(r) + 2 sqrt(t^2+G) J2(r) cos(2 theta-Theta)
          + independent Gaussian modes n>=3,

with G of density g exp(-g), and uniform independent Theta. The
determinant at the distinguished saddle is -G/4. Subtracting t J0
leaves only the translation t^2 of a gamma radius variable as the
level dependence. On any nondegenerate centered annulus, the exact
total variation distance between these residual fields at levels
t,s is delta(|t^2-s^2|), where

    delta(a) = (1-exp(-a)) exp(-a/(exp(a)-1)) <= min(1,a/e).

Two independent derivations check the load-bearing constant: integrate
the density difference at its unique crossing c=a/(1-exp(-a)), or
use half the L1 derivative norm of g exp(-g), which is 1/e.
The exact expansion is delta(a)=a/e-a^3/(24e)+O(a^5).
Circular Fourier coefficients recover the radius, proving equality,
not merely an upper bound. Circular means prove that the uncentered
fields at distinct levels are mutually singular on the same annulus.

The same-variable coupling gives expected uniform difference outside
radius R at most

    |t-s| M0(R) + (sqrt(pi)/2)|t^2-s^2| M2(R),

where Mj(R)=sup_(r>=R)|Jj(r)|. These envelopes are O(R^(-1/2)).
The coefficient sqrt(pi)/2 is checked by the integral E G^(-1/2),
independently evaluated after the substitution g=v^2.

The proof also writes the exact interior threshold density as the
saddle height density times the Palm probability of global threshold
pivotality integrated over its location. This inserts the missing mark
without claiming an estimate on it.

Command:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B check_saddle_palm.py
```

Output (exit 0; same shell priority warning as before):

```text
niceness=20; threads=1; CPU cap=60s
original determinant tilt: 7 levels; max moment error=3.205e-08
a, exact TV, half-L1 quadrature, independent max CDF gap:
1e-06 3.67879441171e-07 3.67879441146e-07 3.67879441171e-07
0.0001 3.67879441018e-05 3.67879440977e-05 3.67879441018e-05
0.01 0.00367877908347 0.00367877908307 0.00367877908347
0.1 0.0367726228295 0.0367726228254 0.0367726228295
1 0.353224356804 0.353224356763 0.353224356804
4 0.911088820855 0.911088820745 0.911088820855
16 0.999998086904 0.99999808678 0.999998086904
TV max quadrature error=1.233e-10
TV cubic coefficient checked against -0.015328310049
coupling inverse-radius moment=0.886226925453; four amplitude bounds passed
angular spectral / Fourier covariance error=1.110e-16
four circle-mean / latent-radius / saddle-eigenvalue audits passed
20 small-determinant / opposite-level coupling cases passed
PASS; elapsed=0.038s; peak RSS=13.34 MiB
```

This is constant-memory quadrature with small fixed Fourier sums,
not a large simulation. The script uses only the standard library,
verifies its inherited niceness and thread setting, and sets a
60-second CPU limit. The observed peak RSS is far below 1 GB.

Completed bounded reads of round 3's full log and round 4's script
tail to recover material hidden by initial combined-output truncation.
One attempted log patch failed exact-context matching and changed
nothing; it was reapplied against the actual last line.

## Attempts to break the extension

1. At t=0, ordinary Gaussian first-jet conditioning gives E U=1;
   determinant weighting gives E U=2. This detects omission of the
   Palm weight, a factor that would change the entire arm law.
2. The determinant computed directly from the Taylor coefficients
   agrees with the product of the two eigenvalues, -G/4, at four
   signed levels. The old density is recovered independently.
3. Tested a down to 1e-6 and up to 16, using density quadrature and a
   derivative-free maximization of the CDF difference. Both agree
   with the exact total variation formula. The a/e bound is sharp
   at first order, and the cubic coefficient is negative.
4. The circle restriction can recover U whenever J2(r)!=0. An
   isolated radius at a zero of J2 is excluded from that argument;
   every annulus of positive width contains admissible radii.
5. Tested nearly flat saddles G=1e-16 and opposite levels t=-s.
   The residual laws at opposite levels coincide exactly. The
   coupling bound uses E G^(-1/2), which is finite; a uniform lower
   bound on the determinant was never assumed.
6. Tried extending small residual total variation to F_t itself.
   It fails: the circle mean is deterministically t J0(r), so laws
   at distinct levels have total variation one on any such annulus.
7. Tried using the decaying coupling to remove level sprinkling in
   saddle arms. The event is about F_t-t=H_t-t(1-J0(r)), whose
   radial threshold tends to t at large radius. Its level change
   does not decay. The new comparison transfers this specified
   radial-level event to F0 with error delta(t^2), but does not
   compare that event to zero-level arms.

No numerical check failed. The unsuccessful extensions in items 6–7
are mathematical limitations, explicitly stated in PROOF.md. A later
worker still needs a macroscopic arm estimate or stability under the
radial level perturbation; the R^(-2) sufficient crossing window is
unchanged.

## Final artifact audit, 08:02 Asia/Tbilisi

Read back all of PROOF.md and REPORT.md and listed the folder. The
four deliverables are LOG.md, PROOF.md, REPORT.md and
check_saddle_palm.py. Checked that the verdict states the proved
conditional-field lemma, not the open percolation conjecture. The
report includes the exact commands, independent audit, failure of
uncentered TV comparison, unchanged level window and next missing
estimate. References name only papers actually opened this session;
the publisher timeout is explicitly recorded.

Re-derived the TV crossing equation v exp(-a)=v-a, its unique solution
c=a/(1-exp(-a)), and the positive density integral P(c)-P(c-a).
Checked normalization by both the polar Gaussian Jacobian and the
old conditional Hessian formula. The coupling denominator is at
least 2 sqrt(G), so the coefficient is E G^(-1/2)=sqrt(pi)/2,
not twice that value. The same annulus supports both total variation
lower bounds by selecting separate radii away from the respective
Bessel zeros. No further numerical run was needed after the passing
audit; the tested formulas were not changed.

Corrected an initial guessed receipt time: the exact command
`env OMP_NUM_THREADS=1 nice -n 15 stat -f '%N | created %SB | modified %Sm' -t '%Y-%m-%d %H:%M:%S %Z' run.pid PROMPT.md`
reports run.pid creation at 07:53:34 +04. The task footer now uses
that evidenced session-launch time and does not invent a receipt time.
Only this folder was written; preceding work and shared stores were
left untouched.

Task: “take the NEXT checkable step on this problem, building on that
work” — 15 November 2026, 07:53 Asia/Tbilisi (session launch).
