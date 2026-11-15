# T227 working log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 11:26 Asia/Tbilisi; first recorded clock
2026-11-15 11:28:21 +04.

## Orientation and bounded literature update

Read startup memories, compute state, mesh protocol, and previous reports
and proofs. The current task's restriction to writes in this folder takes
precedence over the general mesh/checklist/brain write requirements. Those
external stores will not be changed. No git or subagents. Initial read-only
commands lacked the requested nice prefix; corrected before numerical work.
Compute state: status ok, owner_away_open. Computations will be scalar,
single-thread, nice >=15, CPU-limited, and under 1 GB.

Web search and primary-source opens completed within five minutes of the
start. Queries: “catapult phase deep nonlinear networks convergence proof
2026 learning rate”; “catapult neural networks Zhu Liu Radhakrishnan Belkin
2205.11787 convergence”. Opened:

- Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein,
  Guy Gur-Ari, *The large learning rate phase of deep learning: the catapult
  mechanism*, https://arxiv.org/abs/2003.02218 . Solvable models and empirical
  deep-network predictions, not the requested theorem.
- Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan, Mikhail Belkin,
  *Quadratic models for understanding catapult dynamics of neural networks*,
  https://arxiv.org/abs/2205.11787 . Neural quadratic models.
- David Meltzer, Min Chen, Junyu Liu, *Catapult Dynamics and Phase Transitions
  in Quadratic Nets*, https://arxiv.org/abs/2301.07737 . Quadratic and
  homogeneous two-layer models.
- Benjamin Gess, Daniel Heydecker, *Large Spikes in Stochastic Gradient
  Descent: A Large-Deviations View*, https://arxiv.org/abs/2603.10079 .
  Shallow networks, SGD and probabilistic spikes.
- Quan Nguyen, Robin Yadav, Param Mody, Mark Schmidt, *A Minimal ReLU
  Classifier on Non-Linearly Separable Data: Convergence and Implicit Bias
  at and beyond the Edge of Stability*, https://arxiv.org/abs/2610.23007 .
  Two-neuron ReLU classifier with logistic loss.

No matching solution found in this bounded update. No exhaustive absence
claim. No SOLVED_ELSEWHERE.md warranted.

## Earlier-result recheck

Direct differentiation independently gives, with W=sqrt(m)B,
u=tanh(c), v=tanh(Wu/m), q=1-v²,
A=v, D_ij=a_i q_i u_j, C_j=(1-u_j²)mean_i(a_i q_i W_ij),
the Euclidean gradients A/m, D/(m sqrt(m)), C/m. Thus the middle
cross-gradient term is the average over m² entries. The earlier tube and
backwards geometric-sum argument are consistent; a fresh computational
recheck will precede the extension.

## Recheck completed

Created fresh `recheck_escape.py`; no previous code imported or executed.
Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_escape.py
```

Exit 0, PASS. Exact rational bounds reproduce z0=.02527, tube
z=.21927, cross-gradient [51.20855358409636,62.36475941950364],
sum h|F| <=.022564102564102566, movements
[.005076923076923077,.17728615384615384,.017209258338461538],
common-shift error .007446153846153846, density derivative
7.66550189042784/m², failure bound 3.5766993532822474e-9 at
m=200000, and 13-step bound. A second calculation using signed endpoints
and 70-digit Decimal exponentials bounds the cross-gradient by
[51.91959188058138,61.812102848796805]. Twelve full Euclidean-coordinate
trajectories (circulants and imbalanced columns, widths 4 and 16, h=.9,
1,1.1) pass the escape and displacement checks. Finite-difference error
4.90e-11. RSS 14,499,840 bytes, nice 20, runtime .005 seconds.
Data: `escape_recheck.json`. The round-5 result holds.

## Chosen extension, before doing it

Prove global zero-loss convergence after escape, using only the trained
output layer. Set E_t=mean_i(a_i,t²), Q_t=mean_i(v_i,t²), and h=eta/m.
The proposed exact identity is

E_{t+1}-E_t = -h(2-h Q_t)F_t².

Since Q_t<=1, this would give sum_t F_t² <=E_0/[h(2-h)] for every
0<h<2, irrespective of how all the hidden weights evolve. It would
complete the loss-convergence part of the unbiased-sign theorem for the
entire exit window, without a finite-step entrance certificate. This
uses the single zero label in an essential way. It does not automatically
prove a later NTK drop, monotone loss, parameter convergence, or eta_max.
The choice is this convergence lemma and its application to the preceding
escape theorem; no search for a different architecture or initialization.

Planned audits: derive the identity by both coordinate expansion and the
eigenvalues of a rank-one output update; check exact rational examples,
independently evaluated full-network trajectories beyond escape, and
examples at h=2 and h>2 for fixed bounded features. Explicitly test whether
loss can rise again, so no unjustified monotonic tail claim slips in.

## Global convergence certificate

Created `verify_convergence.py`. Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_convergence.py
```

Exit 0, PASS. The identity holds in 360 exact rational cases, and all
360 are independently checked by orthogonal decomposition of the rank-one
output update. Tested h includes .001, .05, .9, 1, 1.1, 1.9, 1.999,
2 and 2.001. Mixed output signs and arbitrary bounded features are allowed.
For 0<h<2, E_{t+1}<=E_t-h(2-h)F_t². Telescoping proves convergence
for every finite initialization of the given tanh architecture and all
0<eta<2m, independent of the entire hidden trajectory.

Exact constants for h in [.9,1.1]: E0<=8.01²=64.1601,
h(2-h)>=.99,
sum F_t² <=71289/1100,
sum L_t <=71289/2200=32.40409090909091.

Fifty-seven full Euclidean-coordinate trajectories passed the energy
identity and telescoping checks. Cases include the centered sign law,
balanced circulants, completely imbalanced columns, and ten deterministic
states spanning the old exit window .02 to 1.379. The latter test the
global statement; they are not claimed to be reachable stopping states.
Widths 4,16,32; h=.9,1,1.1. Maximum energy-identity error 2.14e-14;
telescoping error 2.85e-14; independent finite-difference error 3.60e-11.
Maximum trajectory length 200; largest terminal residual 8.75e-9.
Numerical termination is not used to prove convergence. No example of
renewed loss growth after an earlier decrease was found in this sample;
monotone loss is not inferred. RSS 15,843,328 bytes, nice 20,
runtime .193 seconds. Data: `convergence_verification.json`.

Fixed features v_i=1 give an exact boundary test: at h=2 the output
alternates without decay, and at h>2 it grows. This limits the general
bounded-feature argument; these are not counterexamples for the trained
tanh architecture and do not establish its maximal step.

## Written proof and arithmetic re-derivation

Wrote `PROOF.md`, including the output-energy identity, the independent
spectral derivation, finite-iterate existence, telescoping and convergence,
and a self-contained reproduction of the inherited escape/probability
argument. Combining them proves that all the old overshoots converge in
loss. All times and all h in the old interval share the same initial
event. The new deterministic convergence theorem needs no probability
event at all.

A separate Decimal stdin calculation, with the same environment/nice
prefix, re-derived the exact proof constants:
`7.20006²-.225²-.76268304²=51.2085535840963584`,
`7.857²+.225²+.76268304²=62.3647594195036416`,
`71289/2200=32.40409090909090909090909091`.
Read the remaining earlier logs in full; all earlier Python scripts have
also been read. Previous folders were never mutated.

The identity fails to have a sign for nonzero labels: it becomes
E^+-E=-2h(F-y)F+h²(F-y)²Q. At a=0 with nonzero features and nonzero
label the output energy increases. Thus the result uses the zero-label
law and is not a nonzero-label convergence theorem. No all-parameter
convergence, NTK reduction, or pointwise rate is implied by square
summability. The best-iterate and average-loss rates are the only rate
claims in the proof.

## Independent high-precision audit and attempts to break the result

Created `audit_convergence.py`, importing no other task code. It obtains
every Euclidean gradient coordinate by forward-mode automatic
differentiation of the literal network expression, with Decimal values.
Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_convergence.py
```

Exit 0, PASS. Six width-4 trajectories, each for 60 updates, start from a
balanced circulant perturbed in one B coordinate by 1e-25. They include
h=.9,1.1 and1.99, at both 80- and 110-digit precision. The energy
identity, nonincreasing output energy, telescoping, square-sum bound,
and escape all pass. The two precisions agree on exit times, and their
entire residual sequences differ by at most 8.66e-55 (.9), 3.63e-55
(1.1), and1.34e-55 (1.99). These finite computations test the identity;
the infinite-time theorem is the analytic telescoping argument.

A native tanh-network state with zero output weights and label 1 has
output-energy increase .76941961212420924836 at h=1, checked by the
same independent AD. This invalidates extending the nonincreasing-energy
identity to nonzero labels. It does not prove nonconvergence for such
labels. Fixed-feature boundary examples in the rational audit similarly
invalidate extending the general lemma through h=2, but do not identify
the trained tanh model's threshold.

RSS 15,024,128 bytes; nice 20; runtime 3.475 seconds. Data:
`convergence_audit.json`. No mathematical certificate failed.

Checks of possible missed cases:

- F=0 and Q=0 freeze the output update and satisfy the identity exactly.
- Output signs may change; the proof uses no positivity of a after time 0.
- Simultaneous hidden updates do not change the a-update's use of the old
  feature vector. Using the new feature vector here would be wrong.
- The lemma controls the square-sum, not the absolute sum, of residuals.
  Parameter limits and a geometric tail cannot be inferred from it.
- Initial rows or columns need not concentrate for global convergence.
  Their concentration is used only for the inherited early growth.
- Every finite hidden iterate exists by induction, even without a uniform
  parameter bound. The proof never assumes bounded hidden weights.
- A common probability event gives convergence for every fixed step in the
  interval; this does not supply a uniform-in-step convergence rate.
- The limit eta->2m makes the denominator of the general estimate vanish.
  It supplies no conclusion at that endpoint or above it.

## Final report and inspection

Wrote `REPORT.md` with the required PARTIAL verdict, the deterministic
convergence theorem, its high-probability growth-and-convergence corollary,
commands, failed extensions, remaining gaps, checked sources, and the next
task. Inspected all three scripts with ast.parse and all three saved JSON
summaries with a single-thread nice-prefixed standard-library stdin
program. Checked PASS, nice>=15, measured RSS<1 GB, runtime<20 minutes,
the exact rational sum constant, and the required verdict prefix.
Output: `Final artifact inspection PASS`.

Recorded text sizes before this final append: REPORT.md 5948 bytes,
PROOF.md 14142 bytes, LOG.md 10710 bytes. No additional numerical runs
were needed after the independent passing audit. All authored files stay
in this folder; no external files, prior work, git state, or shared stores
were changed.

Task T227: “take the NEXT checkable step on this problem, building on that work.”
First recorded session clock: 2026-11-15 11:28 Asia/Tbilisi.
