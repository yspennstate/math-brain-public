VERDICT: PARTIAL volume-uniform first-step resonance bounds for Bernoulli-diluted Ising chains

The earlier exact-barrier result survives an independent audit. The new result
is the specific denominator estimate proposed in its report: geometric block
tails do compensate for the number of adjacent block-eigenstate pairs, for
the first barrier flip. The estimate holds simultaneously over all local
eigenstates and all outer frozen-spin assignments, uniformly in chain length.
It does not prove stability after the barriers acquire transverse fields.

Assume iid Bernoulli active indicators with probability p<1, and independent
iid longitudinal fields with density bounded by rho. Keep the earlier
Hamiltonian H_0 with exact zero transverse fields at frozen sites. At a
specified frozen site f, let m be the total length of its two adjacent active
blocks. Every denominator induced by X_f is

\[
 2h_f+c,
\]

where c is independent of h_f. There are at most 4*4^m distinct candidates:
four outer-control assignments and 4^m pairs of adjacent block states.
Spectator energies cancel. Thus, conditional on all randomness except h_f,
the probability that any such denominator has magnitude below delta is at
most min(1,4 rho delta 4^m).

Writing t=4 rho delta, averaging the two geometric run lengths gives

\[
 \mathbb P(\text{any first-flip resonance at }f\mid\xi_f=0)
 \le F_p(t)=(1-p)^2\sum_{k\ge0}(k+1)p^k\min(1,t4^k).
\]

For p<1/4, this is bounded by t[(1-p)/(1-4p)]^2. At p=1/4 it is
O(t log^2(1/t)); for p>1/4 it is O_p(t^alpha log(1/t)), where
alpha=log(1/p)/log4. In particular it tends to zero for every fixed p<1.
The value 1/4 is a threshold of the uncapped counting estimate, not a claimed
physical transition. [PROOF.md](PROOF.md) gives the exact capped sum, a separate
fractional-power bound, the finite-boundary argument, and all proof steps.

Reproduce both audits from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 audit_earlier.py > earlier_audit_stdout.txt 2> earlier_audit_stderr.txt
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 nice -n 15 python3 verify_denominators.py > denominator_stdout.txt 2> denominator_stderr.txt
```

The earlier audit passed 62 matrix cases and 612 exact support-probability
checks; its largest normalized residual was 1.51e-15. The new audit passed
135 conditional matrix cases, 240 interval-union integrations, 108 exact
capped-sum comparisons, 126 exact finite-volume checks, and a seven-site
spectator test with 64 energy-cancellation checks. The largest spectral
residual was 2.49e-14. An exact rational empty-block example saturates the
outer-control factor four. Exact p=1/4 and both sides of powers of four were
checked. Matrix checks are floating-point checks, not certified intervals.

The final runs used at most 36,175,872 bytes RSS and each finished in under
one second. All numerical thread limits were one; actual nice value was 20.
macOS denied the redundant nice adjustment, producing the only stderr line
in either accepted run. Data and output: [earlier_audit.json](earlier_audit.json),
[denominator_verification.json](denominator_verification.json),
[earlier stdout](earlier_audit_stdout.txt), [new stdout](denominator_stdout.txt),
and their corresponding stderr files.

One added spectator test initially failed because its fixture interchanged
outer-control and active bit positions. Correcting that indexing made the
full suite pass; no theorem was changed. The failed traceback is retained in
[spectator_initial_stderr.txt](spectator_initial_stderr.txt), with the diagnosis
in [LOG.md](LOG.md). The uncapped first-moment approach also fails for
p>=1/4; capping before averaging is essential there.

The bounded literature check found no newer unconditional solution. John Z.
Imbrie's theorem still assumes limited level attraction; Francois Huveneers'
survey discusses the unresolved high-probability extension.
[John Z. Imbrie, *On Many-Body Localization for Quantum Spin Chains*,
arXiv:1403.7837](https://arxiv.org/abs/1403.7837);
[Francois Huveneers, *Many-body localization: an introduction for
mathematicians*, arXiv:2609.39462, Section 4.5](https://arxiv.org/html/2609.39462v1).
Both sources were opened. An unindexed result could have been missed; no
novelty claim is made for this elementary lemma.

The missing step is control after the first rotation. Neighboring flips share
blocks and fields; the new denominators need not remain affine in an unused
independent field. The next worker should construct a first rotation on cells
with no first-step resonance, bound its operator norm and spatial tails, and
identify explicitly the two-barrier denominators created at second order.
The bound here cannot be substituted for Imbrie's LLA assumption.

Task: “take the NEXT checkable step on this problem, building on that work.”
15 November 2026, approximately 01:28 Asia/Tbilisi.
