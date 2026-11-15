VERDICT: PARTIAL no finite margin-stationary representation of the earlier Gaussian conical scores, almost surely; GD benign overfitting remains unresolved

The earlier result holds. An independent derivation verifies its exact
path-norm formula, including extra hyperplanes and cancellations.
New recheck.py recovers the explicit intrinsic norms
386.3134673380746 and 49.221478356835924 through attaining rational
baseline allocations and independent 70-digit gradient-jump sums.
The separate exact certificate 144>81 and the displayed-realization
descent also pass. No verified resolution of the full problem was found
in the bounded literature check; opened primary references and scope
are in [LITERATURE.md](LITERATURE.md).

The new result answers the previous report's next question generically:
the obstruction belongs to the score, regardless of its finite
representation. Consider the earlier bias-free score

\[
 f_h(x)=v^Tx+\sum_i A_iH_{T_i,h_i}(x),\qquad
 0<h_i\le\Delta_i/3.
\]

If any A_i is nonzero and its center slope T_i is nonzero, **no finite
two-layer ReLU representation of this score satisfies generalized KKT
stationarity** for minimum half-squared parameter norm under unit-margin
constraints, with both layers trainable. This includes arbitrary extra
neuron directions, split coefficients, and independent ReLU derivatives
in [0,1] at zero. Every nonzero scalar multiple is excluded too.

The proof derives a necessary angular-bisector condition. An endpoint
neuron's stationarity fixes its signed active-sample vector. Evaluating
that vector at the center excludes any center neuron on the same
orientation. Both edges must therefore use the opposite orientation
from the center. The edge coefficients have the same sign, forcing

\[
 u_-^Tu_0=u_+^Tu_0.
\]

For the earlier slope-symmetric normals q(T_i-h_i), q(T_i),
q(T_i+h_i), this equality implies 4 T_i h_i=0. This contradicts
T_i!=0. For the sample-mean Gaussian construction, the slopes are
nonzero and at least one residual is nonzero almost surely, by
absolute continuity and a nonzero-polynomial argument. Hence the
exclusion holds almost surely for every finite n>=1,d>=2, including
n>=d. Full proofs are in [PROOF.md](PROOF.md).

The exception is real. Section 5 supplies an exact zero-centered tent
with an arbitrary linear baseline and a balanced three-neuron KKT
representation. All margins are one; its objective and positive
multiplier sum are both exactly 10. Its center derivative is 13/48.
Thus removing the nonzero-slope hypothesis for arbitrary baselines
would be false. This example does not use the sample-mean baseline
and does not contradict the almost-sure statement.

Run from this folder:

```sh
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck.py
env OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 MKL_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit.py
```

Both final runs exited 0 in under one second, at actual niceness 20
and peak RSS below 17 MB. The recheck verifies 294 exact score
identities, twelve gradient jumps, and fifteen descent derivatives.
The new audit enumerates all 27 orientation supports; checks 432 exact
activation-cell identities, 1,296 zero-derivative identities, 35
high-precision geometric cases and 28 independent angle calculations;
and verifies twelve exact KKT exception certificates. Their 36 margins
and 36 stationarity vectors pass. Commands and outputs are recorded in
[LOG.md](LOG.md), with details in [AUDIT.md](AUDIT.md) and both JSON
result files.

What failed: the first run stopped before mathematics because macOS
rejected the attempted RLIMIT_AS guard. Removing that unsupported
guard allowed the small measured runs to complete. The attempted
unqualified exclusion at zero center is false, as the exact KKT example
shows. No mathematical assertion failed in either final run.

What remains uncertain: GD selection and convergence; approximate
stationarity as cone widths shrink; and risk of other localized or
minimum-norm interpolants. This is an exact finite-width stationarity
obstruction for the earlier scores, not an impossibility theorem for
benign overfitting. It gives no uniform separation from stationary
scores and no theorem about a GD trajectory.

Next worker: replace slope-symmetric tents with tents whose endpoint
normals are angularly symmetric about the center. Lemma 1 identifies
the necessary geometry, and Section 5 proves it can support KKT
stationarity for one isolated tent. Determine whether common margin
multipliers can support many such tents while their population
disagreement vanishes. This tests whether the selection obstruction
persists after removing the construction's coordinate-dependent
asymmetry. A separate dynamical argument remains necessary for T265.

Task: “take the NEXT checkable step on this problem, building on that work” — 15 November 2026, approximately 09:02 Asia/Tbilisi.
