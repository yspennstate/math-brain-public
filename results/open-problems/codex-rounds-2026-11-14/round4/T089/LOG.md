# T089 work log

Task: "take the NEXT checkable step on this problem, building on that work."
Received 2026-11-15 approximately 04:46 Asia/Tbilisi (UTC+04).
The shell's timezone was subsequently checked against the UTC clock.

## Startup and bounded literature check

Read both predecessor folders' reports, logs, proofs and audit scripts.
Their files are read-only. Read the compute state: warn, CPU saturated,
owner_away_open. Only small standard-library single-process checks are planned.
No git, subagents, external publication or shared-state task commands.
The current folder-only restriction overrides older mesh/checklist/brain
mutation instructions. A startup brain recall was inadvertently invoked before
resolving that conflict; its output reported an in-memory index merge and a
failed detached refresh. No further brain commands will be run.

The web literature check lasted under five minutes. Queries included
`Bohigas Giannoni Schmit conjecture proved chaotic billiard GOE 2026` and
`site.arxiv.org 2026 "Bohigas" "proof" conjecture`.
Opened primary sources:

- Julien Moy, *Smooth spectral statistics of random perturbations of
  Schrödinger operators near Anosov energy levels*, arXiv:2610.09869,
  https://arxiv.org/abs/2610.09869 . Still v1, 7 October 2026; random
  perturbations and smoothed mesoscopic statistics, not the requested fixed
  billiard microscopic spacing law.
- R. B. do Carmo and T. Araújo Lima, *Effects of stickiness in quantum chaotic
  billiards with n-fold symmetry*, arXiv:2605.27693,
  https://arxiv.org/abs/2605.27693 . Numerical and experimental spectral
  statistics; not a proof of the stated limit.
- Alexander I. Bufetov, Pavel P. Nikitin, Yanqi Qiu, *On Number Rigidity for
  Pfaffian Point Processes*, arXiv:1810.09223,
  https://arxiv.org/html/1810.09223 . Opened Section 1.2 and equations (1.8)
  to verify the orthogonal sine kernel used by round 3.

No resolution found in this bounded search. No SOLVED_ELSEWHERE.md is warranted.

## Independent re-derivation of the round 3 claim

For n>=1, the alternating binomial sum through r equals
(-1)^r binom(n-1,r), by Pascal cancellation. Thus odd/even sums bracket
the zero-count indicator. Comparing the empirical upper sum with the target
lower sum, and conversely, gives exactly

    |V-E| <= b_(2m) + max(|U_a-U_b|, |L_a-L_b|).

In the GOE kernel, |S|<=1, |I|<=R+1/2 and |D|<=pi/2<2.
Each row of the 2k by 2k antisymmetric matrix has norm <=C_R sqrt(2k).
Taking the square root of Hadamard's determinant bound and integrating gives
b_k(s)<=(R C_R)^k(2k)^(k/2)/k!. Its even-order ratio is
2(R C_R)^2(1+1/m)^m/(2m+1). The earlier main bound holds.
An independent exact audit will check the binomial comparison and the order
390 claim without importing the earlier checker.

## Extension chosen before doing it

Sharpen only the GOE target remainder at R=2, preserving the preceding
target-only comparison. Use the signed sine-integral bound |I|<=1/2,
balance the two kernel row types by determinant-one diagonal congruence,
and retain their separate squared contributions in Hadamard's inequality.
This should reduce the required order substantially without high-dimensional
quadrature or an empirical count-tail assumption. No billiard spectral estimate
is proposed.

## Kernel refinement and preliminary arithmetic

Completed the remaining predecessor script/proof reads. A tiny exploratory
standard-library command, with the required environment and nice launcher,
verified inherited nice 20. Keeping only |I|<=1/2 and balanced uniform bounds
would give order 72 at R=2 (rational pi/4 upper bound 11/14).

A stronger estimate comes from projecting exp(i*pi*z*t) onto 1 and sqrt(3)*t
in L2([-1,1],dt/2): S(z)^2+3D(z)^2/pi^2<=1. A determinant-one diagonal
congruence with alpha^4=pi^2/3 makes one row type have squared norm <=k,
and the other <=k+(k-1)pi^2/12. Thus the candidate remainder is

    R^k [k(k+(k-1)pi^2/12)]^(k/4) / k!.

An exploratory exact squared-bound check, replacing pi^2/12 by 121/147,
found first even orders 14,26,58 for R=1/2,1,2 respectively, at threshold
10^-6. At R=2 the diagnostic float was 9.133162051048129e-7.
The proof, final rational enclosures and independent audits are next.

## Independent round 3 audit passed

Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B recheck_round3.py > recheck_output.txt 2>&1
```

The checker uses a fresh implementation and does not import predecessor code.
It checks finite alternating sums, both target-only comparisons for rational
count laws including a rare cluster of size 40, and the old R=2 threshold by
two exact formulas. The complete output is in recheck_output.txt.

```text
binomial_identities=6561; rational_count_laws=85;
target_only_comparisons=36125; sharper_than_sum=34408;
old_formula_vs_recurrence=220; old_R2_first_even_order=390;
previous_result_holds=true; elapsed_seconds=0.631;
nice=20; peak_rss_bytes_macos=13811712.
```

## Sharper remainder proved and exact audit passed

Wrote PROOF.md and check_remainder.py. Command (exit 0):

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B check_remainder.py > remainder_output.txt 2>&1
```

The rational certificate uses pi^2/12 < 121/147, established by the positive
integral 22/7-pi = integral_0^1 x^4(1-x)^4/(1+x^2) dx. Polynomial division
and integration are also checked exactly in the script. The squared target
bound is computed two ways (factorial formula, sequential product) at 150
radius/order pairs. Exact square-root enclosures:

| R | First even order for this bound <=10^-6 | Rational upper bound |
|---|---|---|
| 1/2 | 14 | 538396/10^12 |
| 1 | 26 | 272206/10^12 |
| 2 | 58 | 913317/10^12 |

At R=2 order 56 the bound is between 3608289/10^12 and 3608290/10^12.
Every earlier positive even order was checked, not just the preceding one.
No claim is made that the actual moment needs order 58.

The independent matrix audit checked 120 exact rational antisymmetric
matrices satisfying the scaled entry constraints, for k=1,2,3,4.
It compared determinants from Gaussian elimination with Pfaffians from a
recursive matching expansion, checked both row types and Hadamard's bound,
and verified determinant-one congruence separately. These abstract matrices
are not GOE samples. No high-dimensional GOE integral was evaluated.

Final output: all exact remainder and matrix checks passed; elapsed 0.068 s,
peak RSS 15,695,872 bytes, inherited nice 20. Full output and the exact
squared fraction are in remainder_output.txt and remainder_data.json.
Scripts use one process and the standard library, 128 MiB measured RSS and
120-second elapsed guards. No OS-enforced memory cap is claimed. The launcher
prints a nice warning, but each script independently requires inherited
nice>=15, and measured nice was 20.

## Attempted breaks and second derivations

- Re-derived the projection inequality without complex Hilbert-space notation:
  S is the average of cos(pi*z*t) on [-1,1], and -D/pi is the average of
  t*sin(pi*z*t). Cauchy gives S^2<=average cos^2 and
  3D^2/pi^2<=average sin^2, since average t^2=1/3. Adding gives one.
- Checked the sine integral lobe argument for partial as well as full lobes,
  both signs of z, the discontinuity of I at zero and its assigned value
  I(0)=0. Bounding the integral by its absolute integral would lose the result.
- Re-derived the determinant exponent: k rows of each type give determinant
  bound [k(k+(k-1)pi^2/12)]^(k/2), so the correlation bound has exponent k/4.
  Squaring the moment bound gives exponent k/2, integral for every even k.
  The exact matrix audit checks these exponents independently of the kernel.
- The diagonal contribution is one in each row. I(0)=D(0)=0 gives k-1,
  not k, in the first-row correction. At k=1 the moment bound is exactly R.
- The target-only comparison was checked for 85 rational count laws,
  including order above the law's support and a rare count-40 cluster.
  It does not assume any empirical tail bound.
- Restricted the grid corollary explicitly to nested interval counts;
  arbitrary unrelated count laws indexed by s need not be monotone.
- The old order 390, the new order 58 and all displayed bounds are exact
  rational comparisons, not conclusions from floating-point approximations.

No mathematical check failed. Two intermediate attempts to append this log
with apply_patch missed their context and changed no file; corrected patches
succeeded. The first clock annotation mistook local time for UTC;
date and the UTC tool established 04:46 Asia/Tbilisi as the start time.

## Final artifact audit

Created REPORT.md with the partial verdict and the next analytic target.
Reopened the primary kernel source's equation (1.1), confirming explicitly
that correlations are Pf[K(x_i,x_j)J], so the block signs in PROOF.md agree
with the cited convention.

A separate read-only inline standard-library check, launched with
`env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 MKL_NUM_THREADS=1 nice -n 15 python3 -B -`,
loaded remainder_data.json and recomputed its saved squared fraction directly
as 2^116*[58*(58+57*121/147)]^29/(58!)^2. It checked the two rational
enclosure endpoints, the threshold, all audit counts a second way, the eight
deliverables for nonzero size, and the exact report verdict. Exit status 0:

```text
Final artifact, independent count and exact squared-constant checks passed.
nice= 20
```

The eight deliverables are REPORT.md, PROOF.md, LOG.md, recheck_round3.py,
check_remainder.py, recheck_output.txt, remainder_output.txt and
remainder_data.json. No predecessor file was executed or edited.
