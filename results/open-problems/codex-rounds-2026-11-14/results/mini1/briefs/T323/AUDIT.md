# Checks and boundary cases

## Independent derivation of the antipodal Jacobian

The proof differentiates the angular equation. The same Jacobian follows
by differentiating the Cartesian mean before tangent projection.
At a balanced antipodal configuration write
\(x_i=\sigma_i u\), \(v=Ju\), and perturb by
\(x_i'=\sigma_i\eta_i v\). Let
\(r=n^{-1}\sum_j\sigma_j\eta_j\) and
\(\bar\eta=n^{-1}\sum_j\eta_j\). The untransformed attention mean
\(M_i=\sum_jp_{ij}x_j\) vanishes at the base configuration. Its derivative is

\[
M_i'=rv+q\sigma_i(\eta_i-\bar\eta)u.
\]

Indeed, the derivative of the token values contributes \(rv\).
Differentiation of the logits gives
\(q\sigma_i\sigma_j(\eta_i-\eta_j)\); multiply by
\(x_j=\sigma_j u\) and sum with weight \(1/n\). The softmax row-average
term contributes zero because the base mean is zero. Since
\(Vu=au-\omega v\) and \(Vv=av+\omega u\), taking the angular tangent
\(\sigma_i v\) gives

\[
\dot\eta_i=a\sigma_i r-q\omega(\eta_i-\bar\eta).
\]

The derivative of the projection contributes zero because the base force
is zero. This reproduces (5) independently of differentiating (3).
For n=2, its separation eigenvalue a-B also agrees with the endpoint
expansion of the exact scalar equation.

## The equality case is not attracting

For \(\delta=\pi-\varepsilon\), direct series in (8), rather than the
Jacobian, give at \(B=a\)

\[
\dot\delta=-\frac{a(3+q^2)}{12}\varepsilon^3
             +O(\varepsilon^5).
\]

Thus \(\dot\varepsilon>0\) for sufficiently small positive
\(\varepsilon\). A zero linear eigenvalue at the threshold does not imply
an attracting antipodal pair. Independently, the strict bound H(delta)<q
proves global convergence to consensus for all initial separations below
pi at equality, without relying on a truncated expansion.

## Other cases that could invalidate the conclusion

- A balanced cluster split is essential. For odd n a configuration with
  unequal populations at opposite points has a nonzero mean, and with
  omega>0 is not a stationary state of this skew-key model. No odd-n
  extension is claimed.
- The common-rotation zero eigenvalue is retained. A single fixed
  orientation is not asymptotically stable in the full torus; the family
  is attracting, and the limiting phase depends on initialization.
- Decay of separation alone would allow continuing common rotation.
  The integrable phase equation in the proof establishes stationary limits
  for the antipodal basin and a rotating limit for consensus.
- The symmetric part of V is positive, but V is not symmetric. This does
  not give a counterexample when V is symmetric positive definite.
- Q and K are separate unrestricted real matrices. Their product Q^T K
  is skew, and the weights are directed. No conclusion is asserted for a
  symmetric positive semidefinite query–key product.
- Self-interaction is included in the denominators and vector fields.
  Removing it changes the problem and the threshold.
- The finite-n positive-measure basin is not inferred from the invariant
  two-cluster subspace alone: all n-1 transverse directions were checked,
  including the n-2 directions that split tokens within clusters.
- The n=2 separatrix is an unstable rotating pair, not an omitted third
  attracting state. Its basin has measure zero.
- At consensus, no individual point limit exists because omega>0. The
  theorem explicitly states convergence to a common rotating trajectory.
  The stationary antipodal basin separately rules out synchronization even
  in the weaker sense of pairwise distances tending to zero.

## Reproducible numerical checks

`audit.py` constructs the original Cartesian softmax vector field, including
projection. It compares 1,000 random two-token cases against the reduced
equations for both key choices. It finite-differences 32 full Jacobians
at n=2,4,6,10, covering B<a, B=a and B>a. Five original-system trajectories
are repeated at half step, and the two-token trajectories are separately
integrated using the reduced equations. The separatrix root is independently
computed from the original Cartesian angular velocities.

These are floating-point checks, not interval certificates. The decimal
root and basin probability are illustrative; the proof uses their exact
implicit definitions and does not depend on their displayed digits.
The data and captured stdout are in `audit_data.json` and `audit_output.txt`.

Final run: effective niceness 20, peak RSS 15,499,264 bytes, about 0.6 seconds.
The launch command's `nice -n 15` emits `setpriority: Operation not permitted`
in this environment. The program verifies its effective niceness is already
at least 15 before doing the checks; it was 20. CPU time and wall time are
both capped at 120 seconds. Only the standard library is used.
