VERDICT: PARTIAL a high-probability catapult interval with independent mixed signs in the dense middle layer; eta_max remains open

The earlier dense-network certificate holds on independent recheck.
The new result replaces its narrowly positive middle-layer initialization
by a product law with independent signs: each dense weight is negative
with probability 1/4. No signs are shared, and no parameters are tied.

For every width m>=20000, use the same dense three-layer tanh architecture

\[
 F_\theta(x)=\frac1m\sum_i a_i\tanh\left(
 \frac1{\sqrt m}\sum_jB_{ij}\tanh(c_jx)\right),\qquad
 L=\tfrac12F_\theta(1)^2.
\]

The data law is the point mass at (1,0). All m²+2m coordinates
are separately trained by ordinary simultaneous Euclidean GD in (a,B,c).
Independently initialize

\[
\begin{split}
 a_i&\sim\mathrm{Unif}[7.99,8.01],\qquad
 c_j\sim\mathrm{Unif}[1.999,2.001],\\
 \sqrt m B_{ij}&=S_{ij}U_{ij},\qquad
 U_{ij}\sim\mathrm{Unif}[.999,1.001],\\
 \Pr(S_{ij}=1)&=3/4,\qquad \Pr(S_{ij}=-1)=1/4.
\end{split}
\]

With probability at least `1-4m exp(-m/800)>0.999998`, simultaneously
for every constant learning rate

\[
 \boxed{.9m\leq\eta\leq1.1m},
\]

the loss satisfies `L0<8`, `L1>16`, and
`L_t <= 64^{-(t-1)} L1 -> 0` for t>=1. Every parameter converges.
The scalar empirical NTK satisfies

\[
 \frac{34}m<\lambda_0<\frac{43}m,\qquad
 \frac{1-10^{-6}}m<\lambda_t<\frac{1+10^{-6}}m\quad(t\geq1).
\]

Thus `eta*lambda0>30.6>2`, and the kernel drops after the spike.
These are NTK bounds, not loss-Hessian bounds.

The new entrance lemma uses the event that every row and column average
of S lies in [.45,.55]. On this event, the first update puts every scaled
dense weight in (-29,-16), every first-layer weight above .84, and every
output weight in (5.8,6.9). The crucial column estimate retains the signed
average of W=sqrt(m)B in the constant part of `a_i sech²(z_i)` and
bounds only its variation in absolute value. This permits independent
negative dense weights without losing control of the shared first-layer
derivative. Concentration proves the event probability. The saturated-tail
argument then applies in the full parameter space. All steps are in
[PROOF.md](PROOF.md).

Reproduce the independent earlier-result check and both new audits with:

```sh
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B recheck_dense.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B verify_signs.py
OMP_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 nice -n 15 python3 -B audit_signs.py
```

All passed. The recheck verifies the prior rational constants and 60
trajectories in literal Euclidean coordinates. The new verification
checks rational bounds and 108 asymmetric signed-network trajectories,
including event-boundary row/column patterns. Finite-difference gradient
error was below 9.7e-10; Euclidean-update disagreement was below 1.8e-15.
The second audit uses binomial-limit exponential brackets instead of Taylor
series, signed endpoint extrema instead of the midpoint decomposition,
and explicit original-coordinate gradient sums. Its independent full-event
entrance bounds are stronger than those stated in the proof.

The probability was independently checked by exact integer binomial sums
at m=20000: the row-and-column union bound is approximately 1.486e-11.
The theorem uses the simpler conservative bound valid at every m>=20000.
No large dense network was allocated: the general-width proof supplies
the theorem; the small networks audit its formulas.

Each script uses one thread and the Python standard library, less than
30 MB peak RAM, and a CPU limit of at most 120 seconds. Each completed in
under eight seconds. The inherited nice value was 20. A first attempt to
set an address-space limit was rejected by macOS before calculation;
the optional guard was removed, and measured memory remained small.
Commands and outputs are in [LOG.md](LOG.md); data are in
`recheck_dense.json`, `signed_verification.json`, and `signed_audit.json`.

Attempts to break the result exposed a real limit of the entrance lemma:
row concentration alone is insufficient. If every row has its negative
quarter in the same columns, the first-layer minimum after one step is
about .219, outside the certified region. A rational enclosure confirms
this failure. It is a counterexample to dropping the column condition,
not a divergence claim. An exactly balanced signed support point has
zero residual and never spikes; this does not rule out a centered-law
high-probability result. No mathematical certificate failed.

The literature update stayed within five minutes. Opened primary sources
included Aitor Lewkowycz, Yasaman Bahri, Ethan Dyer, Jascha Sohl-Dickstein
and Guy Gur-Ari, [arXiv:2003.02218](https://arxiv.org/abs/2003.02218);
Libin Zhu, Chaoyue Liu, Adityanarayanan Radhakrishnan and Mikhail Belkin,
[ICLR 2024](https://proceedings.iclr.cc/paper_files/paper/2024/file/949b3011c50300a2b4e60377466f52a8-Paper-Conference.pdf);
David Meltzer, Min Chen and Junyu Liu,
[arXiv:2301.07737](https://arxiv.org/abs/2301.07737);
Benjamin Gess and Daniel Heydecker,
[arXiv:2603.10079](https://arxiv.org/abs/2603.10079);
Quan Nguyen, Robin Yadav, Param Mody and Mark Schmidt,
[arXiv:2610.23007](https://arxiv.org/abs/2610.23007); and Thomas Hofmann,
[arXiv:2607.04993](https://arxiv.org/abs/2607.04993).
No matching solution of the requested deep finite-width problem was found
in this bounded check. No exhaustive absence or novelty claim is made.

What remains unresolved: eta_max, divergence, onset near 2/lambda0,
centered initialization, signs in the other layers, and nontrivial data.
The law here has E[sqrt(m)B_ij]=1/2; it is not a centered initialization.
The upper endpoint 1.1m is a certificate endpoint, not a stability boundary.
No unverified numerical conjecture is needed for the stated result.

Next worker: seek a multi-step entrance lemma for unbiased independent
middle-layer signs. A concrete first target is a bootstrap controlling
the mean component of W and its row/column fluctuations until the residual
reaches a fixed entrance window. The centered-law initial residual is
small, so the present first-step argument does not supply this bootstrap.
Identifying eta_max still requires a separate stability/divergence analysis.

Task T227: “take the NEXT checkable step on this problem, building on that work.”
Session start: 2026-11-15 05:10 Asia/Tbilisi.
