VERDICT: PARTIAL loss growth followed by zero-loss convergence for unbiased middle-layer signs; eta_max and NTK reduction remain open

The round-5 escape lemma holds on independent recheck. The new result
proves convergence after its entire exit window, without any further
control of the hidden weights. The reason is an exact output-layer
identity that uses the zero label.

For the same dense three-layer tanh network
\[
 F_\theta(x)=\frac1m\sum_i a_i\tanh\left(
 \frac1{\sqrt m}\sum_j B_{ij}\tanh(c_jx)\right),
 \qquad L=\tfrac12F_\theta(1)^2,
\]
all \(m^2+2m\) coordinates are trained by simultaneous Euclidean GD.
For **every finite initialization**, every constant
\(0<\eta<2m\) gives
\[
 \sum_{t=0}^\infty F_t^2
 \leq\frac{m^{-1}\sum_i a_{i,0}^2}{h(2-h)},\qquad
 F_t\longrightarrow0,\qquad h=\eta/m.
\]
Indeed, with \(v_{i,t}=\tanh z_{i,t}\),
\(E_t=m^{-1}\sum_i a_{i,t}^2\) and
\(Q_t=m^{-1}\sum_i v_{i,t}^2\leq1\),
\[
 E_{t+1}-E_t=-h(2-hQ_t)F_t^2.
\]
This follows from the actual pre-update output weights and features;
hidden weights may change simultaneously. Telescoping proves square
summability and hence zero-loss convergence. It does not require a
saturated region or tied neurons.

Keep the round-5 independent initialization:
\(a_i\) uniform on [7.99,8.01], \(c_j\) uniform on [1.999,2.001],
and \(\sqrt m B_{ij}=S_{ij}U_{ij}\), where \(U_{ij}\) is uniform on
[.999,1.001] and each sign is independently unbiased. The data law remains
the point mass at (1,0). For every \(m\geq200000\), with probability
at least
\[
 1-2m e^{-m/5000}-2e^{-m^2/400000}-143/m^2>1-4\cdot10^{-9},
\]
simultaneously for every \(\eta\in[.9m,1.1m]\), the preceding escape
lemma and the new convergence result give:

- Initial effective step \(\eta\lambda_0>45>2\).
- Alternating residual growth by factors between 40 and 69 until the
  first exit \(.02\leq|F_\tau|<1.38\), in \(O(\log m)\) steps.
- Convergence of the subsequent loss to zero, with
  \(\sum_{t\geq0}L_t\leq71289/2200<32.405\).

The proof, including a self-contained reproduction of the escape and
probability estimates, is in [PROOF.md](PROOF.md). The new convergence
lemma is elementary; no claim that it is new to the literature is made.
It closes the loss-convergence gap in the preceding report.

Reproduce the checks from this folder:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_escape.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_convergence.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_convergence.py
```

All passed. The first independently rechecks the inherited constants,
probability estimate, and twelve literal-coordinate trajectories;
finite-difference error is below 4.90e-11. The second checks 360 exact
rational identities twice, by coordinate expansion and orthogonal
decomposition, and 57 full-network trajectories. Energy-identity and
telescoping errors are below 2.85e-14; finite-difference error is below
3.60e-11. The third obtains every gradient coordinate by independent
Decimal forward-mode automatic differentiation. Six 60-step trajectories
include a 1e-25 perturbation of exact balance, h=.9,1.1,1.99, and both
80- and 110-digit precision. Their residual sequences agree within
8.66e-55. All runs used one thread, nice 20, less than 16 MB measured RAM,
and less than four seconds. No large dense matrix was allocated.
Commands and outputs are recorded in [LOG.md](LOG.md); the three JSON
files contain the detailed checks.

What failed or remains uncertain:

- The same energy argument fails for nonzero labels: a native tanh state
  with zero output weights and label 1 has increasing output energy.
  This does not show nonconvergence for nonzero labels.
- Fixed bounded features equal to one give nondecay at h=2 and divergence
  above it. They show the general lemma's boundary is sharp, but are not
  divergence examples for the trained tanh network.
- Loss convergence does not prove a later NTK drop, a monotone or geometric
  tail, or convergence of every parameter. Only average-loss and
  best-iterate bounds of order 1/T follow from the sum bound. Some finite
  numerical runs had residuals above 1e-12 after 200 steps; numerical
  termination is not the convergence proof.
- The maximal learning rate is unidentified. The new unconditional
  guarantee extends to every step below 2m, so any supremum of convergent
  steps is at least 2m. Nothing here proves convergence at that endpoint,
  divergence above it, or that convergent steps form a single interval.
- The middle layer is centered, but the output and input layers are
  positive. General labels, nontrivial data, and conventional
  centered-all-layers initialization remain outside the result.

No mathematical certificate failed. The five-minute literature update
found no matching solution; opened primary sources and their exact
authors are listed in LOG.md. They include the original
[Lewkowycz et al. paper](https://arxiv.org/abs/2003.02218), the
[Zhu et al. quadratic-model paper](https://arxiv.org/abs/2205.11787), and
[Meltzer, Chen and Liu](https://arxiv.org/abs/2301.07737). This bounded
check is not an exhaustive absence claim.

Next worker: use the now-proved loss convergence to isolate the remaining
NTK question, or study stability at and above eta=2m for this same tanh
architecture. A proof of parameter convergence with sufficient derivative
control could connect residual convergence to a limiting NTK. Do not
reuse the fixed-feature boundary example as a divergence proof for trained
hidden layers. A finite-step saturated entrance is no longer needed to
prove zero-loss convergence below 2m, though it could still prove an NTK
drop and a geometric tail.

Task T227: “take the NEXT checkable step on this problem, building on that work.”
First recorded session clock: 2026-11-15 11:28 Asia/Tbilisi.
