VERDICT: PARTIAL a logarithmic-time escape lemma for unbiased independent middle-layer signs; convergence and eta_max remain open

The round-4 biased-sign catapult certificate holds on independent recheck.
The new result supplies its proposed first bootstrap for centered middle
weights: a small random residual grows to a fixed window, with explicit
control of every parameter and of a common middle-layer displacement.
This is an early instability theorem, not a completed catapult theorem.

Use the same dense three-layer tanh network

\[
 F_\theta(x)=\frac1m\sum_i a_i\tanh\left(
 \frac1{\sqrt m}\sum_jB_{ij}\tanh(c_jx)\right),
 \qquad L=\tfrac12F_\theta(1)^2.
\]

All m²+2m coordinates (a,B,c) are separately trained by simultaneous
Euclidean GD. The data law is the point mass at (1,0). Independently set

\[
 a_i\sim\mathrm{Unif}[7.99,8.01],\qquad
 c_j\sim\mathrm{Unif}[1.999,2.001],\qquad
 \sqrt mB_{ij}=S_{ij}U_{ij},
\]

where U_ij is uniform on [.999,1.001] and the independent signs are now
**unbiased**, P(S_ij=1)=P(S_ij=-1)=1/2. Thus only the middle-layer law
has changed from round 4. The output and input layers remain positive.

For every m>=200000, with probability at least

\[
 1-2m e^{-m/5000}-2e^{-m^2/400000}-143/m^2
 >1-4\cdot10^{-9},
\]

simultaneously for every constant eta in [.9m,1.1m], let tau be the
first time |F_t| reaches .02. Then

\[
 \begin{gathered}
 m^{-4}\leq|F_0|<.02,\qquad
 1\leq\tau\leq\min\{n:40^n\geq m^4/50\}=O(\log m),\\
 40|F_t|\leq|F_{t+1}|\leq69|F_t|,\quad
 F_tF_{t+1}<0\quad(t<\tau),\\
 .02\leq|F_\tau|<1.38,\qquad
 50/m<\lambda_t<63/m\quad(0\leq t\leq\tau).
 \end{gathered}
\]

The time bound is 13 at m=200000. Loss increases by a factor at least
1600 at each pre-exit step, and eta lambda_0>45>2. Lambda is the scalar
empirical NTK, not the loss Hessian.

Throughout these steps, a stays in [7.9,8.1], c in [1.97,2.03], and
every W_ij=sqrt(m)B_ij stays within .2 of its initial value. More precisely,

\[
 \max_{ij}\left|W_{ij,t}-W_{ij,0}
       +7.53\sum_{s<t}(\eta/m)F_s\right|<.0075.
\]

This controls the common component and the entrywise deviations without
tying weights. Only initial row concentration is needed; columns may be
arbitrarily imbalanced.

The proof is in [PROOF.md](PROOF.md). Its main estimate bounds the full
cross-gradient between 50/m and 63/m on a convex tube. A backwards
geometric sum controls total movement before exit; endpoint containment
is established before applying the gradient integral. A conditional
one-coordinate density estimate excludes residuals smaller than m^-4.
The initial upper residual bound follows from bounded differences over
all m² middle weights. Every probability step is derived in the proof.

Reproduce the three independent checks from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_signed.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_bootstrap.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_bootstrap.py
```

All passed. The first independently certifies the round-4 entrance and
tail, with 21 literal Euclidean trajectories and finite-difference error
below 2e-10. The second checks every new rational constant and 39
asymmetric trajectories, including imbalanced columns and row-event
boundaries. Its finite-difference error is below 8.6e-11. The third uses
binomial exponential enclosures, direct signed endpoint extrema and
literal-coordinate interval sums; it independently encloses the tube
cross-gradient in [51.7359979108704,61.95180738555273]. An exact
integer-power Chernoff calculation gives row-event failure below
1.695e-12 at width 200000.

The second audit also tests 24 near-balanced trajectories at 80- and
110-digit precision, with initial residuals as small as about 9.64e-31.
All escape; the longest takes 17 steps. Exit times agree between the
two precisions, and exit residuals agree within 1e-40. These small-width
tests audit the deterministic formulas; the large-width result follows
from the proof. No large dense matrix was allocated. Each script used
one thread, under 27 MB measured RAM, a 120-second CPU limit, and less
than one second of reported runtime. Actual nice value was 20.
Commands and outputs are in [LOG.md](LOG.md); results are in
`previous_recheck.json`, `bootstrap_verification.json`, and
`bootstrap_audit.json`.

What fails or remains uncertain:

- An exactly balanced initialization can have F_0=0 and stay fixed.
  A blanket deterministic escape statement is false. The probability
  theorem explicitly excludes this through the lower-residual event.
- The old one-step saturation argument cannot apply here. Every middle
  weight keeps its initial sign through tau, since its movement is less
  than .177287 and its initial magnitude is at least .999.
- The NTK stays large during the proved phase. Later curvature reduction,
  entry into a convergent region, convergence itself, and eta_max are
  unresolved. No numerical trajectory beyond escape is used as evidence
  for any of them.
- This centers only the middle layer and retains a single zero-label
  datum and mean output normalization. No centered-all-layers or general
  data theorem is proved. No mathematical certificate failed.

The literature update ended within five minutes and found no matching
solution. Opened primary sources included Aitor Lewkowycz, Yasaman Bahri,
Ethan Dyer, Jascha Sohl-Dickstein and Guy Gur-Ari,
[arXiv:2003.02218](https://arxiv.org/abs/2003.02218); Libin Zhu,
Chaoyue Liu, Adityanarayanan Radhakrishnan and Mikhail Belkin,
[arXiv:2205.11787](https://arxiv.org/abs/2205.11787); David Meltzer,
Min Chen and Junyu Liu,
[arXiv:2301.07737v2](https://arxiv.org/abs/2301.07737); Benjamin Gess
and Daniel Heydecker,
[arXiv:2603.10079v2](https://arxiv.org/abs/2603.10079); Quan Nguyen,
Robin Yadav, Param Mody and Mark Schmidt,
[arXiv:2610.23007](https://arxiv.org/abs/2610.23007); and Thomas Hofmann,
[arXiv:2607.04993](https://arxiv.org/abs/2607.04993).
Their checked scopes do not supply the requested theorem. This bounded
check is not an exhaustive absence or novelty claim.

Next worker: analyze the nonlinear continuation from the exit window
.02<=|F_tau|<1.38 using the common displacement estimate. The target
is a finite-step transition into a region with a smaller NTK and a
summable-residual tail, or a counterexample showing why such a transition
fails for part of this learning-rate interval. The wide range of possible
overshoots must be handled; a single symmetric trajectory does not do so.
Identifying eta_max remains a separate stability/divergence problem.

Task T227: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 08:48 Asia/Tbilisi.
