# T227 work log

Task: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 05:10 Asia/Tbilisi (01:10 UTC).

## 1. Orientation and literature check

Read the startup memory index and compute state. The governor reports warn,
owner_away_open, CPU saturation; only small, single-thread scalar programs
are planned. All writes stay in this folder. The task-specific prohibition
on outside writes precludes shared mesh/checklist/brain updates. No git or
subagents. The earlier and round-3 folders are read-only sources.

Read both REPORT.md, LOG.md, PROOF.md and their scripts. Re-derived the dense
gradient: with W=sqrt(m)B, u=tanh(c), v=tanh(Wu/m), q=1-v^2,
the scaled derivatives are A_i=v_i, D_ij=a_i q_i u_j,
C_j=(1-u_j^2) sum_i a_i q_i W_ij/m. Actual derivatives are
(A/m,D/(m sqrt(m)),C/m). Thus m times the cross-gradient is the sum
of the A and C averages and the D average over all m^2 entries, as claimed.

Literature check began at approximately 05:10 and ended before 05:15,
within the five-minute cap. Queries included catapult phase deep nonlinear
networks rigorous convergence 2025 2026 learning rate; catapult mechanism
finite width nonlinear networks theorem Zhu Liu Radhakrishnan Belkin;
catapult deep proof 2026 neural networks; and catapult nonlinear convergence
2025 theorem finite width. No matching solution was identified. This is a
bounded update check, not an exhaustive absence claim.

Opened primary sources:

- Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein, Guy Gur-Ari,
  *The large learning rate phase of deep learning: the catapult mechanism*,
  [arXiv:2003.02218](https://arxiv.org/abs/2003.02218).
- Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan, Mikhail Belkin,
  *Quadratic models for understanding catapult dynamics of neural networks*,
  [ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf):
  neural quadratic models; this does not supply the requested theorem for
  the original deep nonlinear network.
- David Meltzer, Min Chen, Junyu Liu, *Catapult Dynamics and Phase Transitions
  in Quadratic Nets*, [arXiv:2301.07737v2](https://arxiv.org/abs/2301.07737):
  quadratic models and two-layer homogeneous networks.
- Benjamin Gess, Daniel Heydecker, *Large Spikes in Stochastic Gradient
  Descent: A Large-Deviations View*,
  [arXiv:2603.10079v2](https://arxiv.org/abs/2603.10079): shallow networks
  and stochastic gradient descent.
- Quan Nguyen, Robin Yadav, Param Mody, Mark Schmidt, *A Minimal ReLU
  Classifier on Non-Linearly Separable Data: Convergence and Implicit Bias
  at and beyond the Edge of Stability*,
  [arXiv:2610.23007](https://arxiv.org/abs/2610.23007): minimal shallow
  classifier, not the requested deep wide architecture.
- Thomas Hofmann, *The Map Behind the Flow: Finite-Step Gradient Descent
  as a Dynamical System*, [arXiv:2607.04993](https://arxiv.org/abs/2607.04993):
  solvable reductions. No matching product-initialization theorem was found.

## 2. Independent recheck

The dense formulas above agree with direct differentiation. The entrance,
cross-gradient and segment-containment arguments will now be checked by a
new rational arithmetic script, without importing or running previous code.

Created `recheck_dense.py`. First run of the command below exited before any
calculation: this macOS environment rejected an address-space rlimit with
`ValueError: current limit exceeds maximum limit`. Removed that optional
guard; the script retains a 60-second CPU limit and checks measured RSS.
It allocates only small scalar lists. This was an environment guard failure,
not a failed mathematical certificate.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_dense.py
```

Exit 0, PASS. Independent degree-90 exponential enclosures confirm:
`a1 in (6.2057725,6.579595044)`,
`W1 in (-24.077804521158427,-19.17912740489895)`,
`c1>1.0732194798371582`, `37.65368770803901<m*lambda0<38.67861402583242`,
`L0<6.496210125`, `L1>19.219999998078`.
Tail cross error: `1.0000173312e-10`. Every tail margin passed.
There were 60 independently implemented trajectories in literal Euclidean
`(a,B,c)` coordinates; finite-difference error `5.360876187410213e-10`,
maximum residual ratio `0.10000000004629837`. Runtime 0.0291 s,
RSS 14,483,456 bytes, process nice 20. Saved `recheck_dense.json`.
**The earlier result holds.** No prior script was imported or executed.

## 3. Chosen extension, before its calculation

Keep the dense architecture, one zero-label datum, and all coordinates
separately trained. Replace its narrowly positive dense weights by
`sqrt(m)*B_ij = S_ij U_ij`, independently over all entries,
where `P(S_ij=+1)=3/4`, `P(S_ij=-1)=1/4`,
and `U_ij` is uniform on `[.999,1.001]`, independent of all signs.
Retain independent `a_i` uniform on `[7.99,8.01]` and `c_j` uniform
on `[1.999,2.001]`.

This addresses the previous report's entrance question for genuinely
independent signs in the dense layer. It does not center the law or
introduce signs in the other two layers. Each dense coordinate has a
two-interval continuous distribution, and there is no tying or common
hidden sign variable.

Proposed good event: every row and every column average of S lies in
`[.45,.55]`. Hoeffding plus a union bound should give failure at most
`4m exp(-m/800)`. On this event, signed averages of W lie in
`[.449,.551]` and absolute averages are at most 1.001. The latter
bound controls the errors from unequal first-layer activations and
unequal second-layer derivatives. In particular, a signed column sum
cannot be bounded by discarding its signs.

Try to certify the same step interval `[.9m,1.1m]`, entrance into
`|a|<=18, -30<=W<=-15, c>=.8`, and then use a full-space
cross-gradient integral as before. The only substantive extension is
the high-probability entrance under this mixed-sign product law.
Next: calculate all margins exactly; test deliberately asymmetric
sign matrices on the event boundaries and failures outside it.

## 4. Mixed-sign certificate and first audit

Created `verify_signs.py`, with exact rational arithmetic for every
entrance, kernel, loss and tail margin. Exponential enclosures use a
degree-80 positive series and a geometric remainder bound. Ran:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_signs.py
```

Exit 0, PASS. Exact bounds, shown here as decimal summaries:

```text
initial z: [0.43277215,0.53125285]
initial |C_j| upper: 0.27008554318049927
a1: [5.900303941,6.818818041]
W1: [-28.648607298330237,-16.19444100934115]
c1 lower: 0.8400745478908345
m*lambda0: [34.51908229113352,41.82528126589167]
L0 upper: 7.60839337845
L1 lower: 16.8199996636
tail cross-gradient error: 2.01167696e-08 < 1e-6
contraction upper: 0.1000011 < 1/8
total h*|F| after entrance: 8.674285714285714
tail |a| upper: 15.574285714285715 < 18
tail W: [-29.000003122742857,-15.999996877257143] inside [-30,-15]
tail c lower: 0.8399063177142857 > .8
```

The controlling estimate for the signed column is
`|mean_i k_i W_ij| <= k_mid*abs(mean_i W_ij) + k_rad*mean_i abs(W_ij)`.
It retains the signs of W in the leading term, and bounds only the
variation of `k_i=a_i sech^2(z_i)` in absolute value. Directly replacing
the whole signed sum by an absolute sum gives an inadequate entrance
bound for c; this centered decomposition is the missing entrance lemma.

108 trajectories passed at widths 40, 80, 160. These small networks test
the deterministic theorem conditional on the good event; they do not
estimate its large-width probability. Sign patterns: circulants with
negative fractions .225, .25, .275, and a four-block pattern with both
row and column averages at opposite event boundaries. Amplitudes were
independent random values or two opposing asymmetric corner choices.
Steps: .9, 1, 1.1 times width. Maximum residual ratio
`0.10000000217917783`. Finite-difference gradient error in actual B
coordinates `9.679807511098204e-10`; disagreement between literal
Euclidean updates and auxiliary W updates `1.7763568394002505e-15`.

Probability bound at m=20000: `4m exp(-m/800)=1.1110355091971217e-6`.
The weaker stated bound `2e-6` is also checked by rational arithmetic
(`e^25>4e10`). Runtime 6.9271 seconds, RSS 29,704,192 bytes,
nice 20. Saved `signed_verification.json` with exact fractions and
all trajectory records. The sandbox's setpriority warning does not
raise the inherited nice value.

## 5. Written proof and independent audit

Wrote `PROOF.md`, including a proof of concentration by bounding the
second derivative of the log moment generating function by 1. The proof
handles the entire simultaneous update segment in the actual Euclidean
metric, proves its containment before applying the cross-gradient bound,
and includes zero residuals and sign changes of the output weights.

Created `audit_signs.py`. It uses a second exponential construction:
`(1+x/n)^n <= exp(x) <= (1-x/n)^(-n)` for `n=2^30`, with
outward rational rounding after each of 30 squarings. These inequalities
follow from `log(1+t)<=t<=-log(1-t)`. No Taylor approximation or
verification-script import is used. It bounds signed column sums by
assigning opposite endpoint values to positive and negative entries,
instead of the proof's midpoint decomposition. It then explicitly sums
the original-coordinate gradient intervals at square widths 4 and 100.

Command:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_signs.py
```

Exit 0, PASS. Independent bounds over the entire event (decimal summaries):

```text
u: [0.963956860836054,0.9640981630963681]
z: [0.4327777335356803,0.531249849081661]
v: [0.40764008450202516,0.48633590220290646]
C: [0.18190376776549302,0.26971417789463237]
a1: [5.9059992853031815,6.815068376798144]
W1: [-28.593597883143048,-16.236200370485495]
c1: [0.8432462566504728,1.4677782371105996]
m*lambda0: [34.777358679644294,41.77240174317795]
```

Literal metric audits use width 4 with one negative per row/column,
and width 100 with 23, 25, or 27 negatives per row/column. Tail
cross-gradient interval, independently computed with products of arbitrary
signed hidden gradients:
`[0.9999999598832308,1.0000000001167697]`.
The wider lower interval compared with the main proof uses
`v in [-1,-1+epsilon]` rather than `|v|>sqrt(1-epsilon)` and still
proves the stated `delta=1e-6` bound.
Summed movements in actual `(a,sqrt(m)B,c)` coordinates:
`[8.674285714285714,3.1227428571428573e-6,9.368228571428571e-5]`.
Every invariance, contraction, loss and kernel margin passed independently.

The probability was also checked a second way: for m=20000, exactly sum
the integer binomial weights `binom(m,k)*3^k`, divided by `4^m`,
over `k<14500` or `k>15500`, then multiply by `2m` for rows and
columns. The exact-rational union bound is approximately
`1.4851236667566674e-11`, smaller than the theorem's conservative
Hoeffding bound. This sharper number is an audit at this width, not a
claim of that same bound at every width. Saved `signed_audit.json`.

Runtime of the expanded audit: 2.5491 seconds, RSS 27,639,808 bytes,
nice 20. An initial version used rounded negative counts at width 100;
the extreme rounded values fell outside the event and were skipped.
Changed this to ceiling/floor so both feasible extreme counts, 23 and 27,
are included. All four literal metric audits passed.

## 6. Attempts to break the conclusion

- Row concentration alone does not imply the stated entrance: take every
  row to have negatives in the same first quarter of columns and positives
  elsewhere, with `a=8,c=2,|W|=1`. Every row average is .5, but at
  `h=1.1` the minimum c after the first update is
  `0.21923952921109935`, below .84 and .8. The signed-column condition
  is doing necessary work for this certificate. This does not assert
  divergence or failure of catapult convergence for that matrix.
- A fully balanced signed matrix with `a=8,c=2,|W|=1` and half positive
  and half negative entries in each row has `z=F=0` exactly and is fixed
  by GD. Thus a blanket deterministic loss-spike assertion for arbitrary
  signs is false. This support example does not rule out a centered-law
  high-probability theorem.
- Adversarial asymmetry: the four-block tests have rows and columns at
  both sign-event boundaries, and opposing choices of parameter corners.
  The shared first-layer estimate survived these tests. No equality of
  neuron parameters is used in the proof.
- Tail signs, boundary points, and metric: interval audits include
  arbitrary output signs, `c=.8`, and `W=-30,-15`; the product terms
  can have either sign. Euclidean finite differences and literal updates
  check the normalization independently of the auxiliary recurrence.
- No matrix at the theorem's minimum width was allocated. General-width
  concentration and the deterministic proof give the theorem; small-width
  experiments only audit its formulas.
- The law is biased in the middle layer and positive in the other layers.
  No centered-initialization theorem, eta_max, divergence theorem, or
  result near `2/lambda0` follows. No mathematical certificate failed.

Added a rational enclosure of the row-only counterexample's c1 to the
second audit, so its failure is not inferred from a floating-point value.

The final counterexample enclosure is
`c1 in [0.21923951475951794,0.21923954366267906]`, by exact rational
arithmetic; it is below .22 throughout. The final audit rerun passed in
2.5201 seconds with RSS 27,262,976 bytes.

## 7. Report and final inspection

Wrote `REPORT.md` with the required PARTIAL verdict, the theorem and law,
reproduction commands, failures and limits, and the next missing lemma.
The result is one extension: a high-probability entrance certificate for
independently signed dense middle-layer weights. It does not solve the
original eta_max problem.

Final read-only inspection used the same single-thread/nice prefix with
`python3 -B -` and a standard-library stdin script. It parsed all three
Python files with `ast.parse`, loaded every saved JSON result, checked
PASS, nice>=15, RSS<1GB, and checked REPORT.md's required first line.
Output: `Final artifact inspection PASS`. Script sizes: 4791, 7927,
7845 bytes. REPORT.md 6481 bytes; PROOF.md 11782 bytes before this log
append. No additional numerical runs were needed after the passing audits.
All authored files are in this folder; earlier folders were never edited.

Finished 2026-11-15 05:25 Asia/Tbilisi (01:25 UTC).

Task T227: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 05:10 Asia/Tbilisi.
