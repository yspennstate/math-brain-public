# Independent audit of the full-polymer mixing upper bound

Auditor: the independent kernels/nonreversibility review agent.
Audited source files:

- ../tv/07_stronger_sector_certificate.tex
- ../tv/08_count_lyapunov_smoothing.tex
- ../tv/09_full_polymer_tv_upper.tex

Scope: all displayed formulas and logical steps in these three files were
checked analytically. The already established harmonic decomposition,
stationary lift Dirichlet identity, count lumpability, and stationary
Gaussian/geometric estimates are the inputs. The preceding hitting-time
calculations were separately audited in audit_tv_hitting_times.md.

**Result: PASS. No remaining mathematical obstruction was found.**
The conclusion is an arbitrary-start upper bound of order
sqrt(n) (log n)^2, for fixed b > 0 and beta = b/n. This does not establish
worst-case full-polymer cutoff.

## 1. Stronger sector certificate

The rising-factorial neighboring ratios are correct. Inserting them into
the radial generator combines the deletion and killing terms exactly
into the displayed positive last term. The first-term estimate for
k <= A uses ell <= k, A <= n/4, and denominator at most 3A; the
last-term estimate for k >= A uses A >= 2. Hence the lower bound
ell sqrt(beta)/6 holds on the entire sector, including both endpoints.
The independent lower bound from the killing rate is also valid.

## 2. Count smoothing

The detailed-balance formula for QV/V is exact for exponent 3/4. The
factorization of its constant-coefficient part is exact and controls
three quarters of (sqrt(lambda)-sqrt(mu))^2.

The first coefficient error has the stated concavity bound for k >= 2
and the direct bound at k=1. For k <= 2A it is O_b(1/A); for k > 2A
its ratio to W is O_b(1/A). The second error is O_b(1/A) uniformly,
including the vanishing birth rate at k=n. Consequently the square-drift
bound holds at both boundaries as well as in the interior.

The comparison log V <= C_b (1+A W) is valid in all three regions.
In the uppermost tail the sum of -log(1-j/n) is O(n), which is indeed
at most C k^2/n for k > n/2. In the central region the zero of the
count drift differs from A by O_b(1), so changing the centering only
changes the additive constant.

Jensen's inequality for x log x gives the claimed evolution inequality
for y=E V. Applying it to log y and using the stated polynomial bound on
the initial log moment yields a uniform bounded V moment after
C_b A log n. Finally q(k) <= C_b/V(k), the mode estimate, and the
sum of sqrt(p(k)) give M(t)=sum q(k)^2/p(k) <= C_b A. This is a valid
polynomial density bound, without asserting complete count L2 mixing.

## 3. Positivity and harmonic dimension

The projection onto a complete degree sector acts separately on each
layer: the full sector is the direct sum of the corresponding
irreducible copies over layers. On a layer the orthogonal projector
commutes with the permutation action, so its diagonal is constant.
Its trace gives diagonal d_ell/N_k.

Positive semidefiniteness bounds every matrix entry in absolute value
by d_ell/N_k. Nonnegativity of F therefore gives the quadratic estimate
norm(P_ell F)^2 <= d_ell sum_k p(k) average(F|k)^2.
There is no assumption that P_ell itself preserves positivity.
Summing dimensions telescopes to binomial(n,d). Absent degrees
only reduce the left hand side.

## 4. Compression and Nash integration

The evolving density is that of the actual reversible polymer chain.
Its norm derivative is exactly minus twice its polymer energy, and
the stationary lift identifies that energy with the cut energy at
the same instant. This argument does not require the lifted density
to evolve under the cut generator, and does not require the lifted
subspace to be invariant under the individual degree projectors.
Thus the argument avoids the usual false semigroup-intertwining step.

The count projection strongly lumps, so the fixed bound M_* applies
to the lifted density at every time after t_0. Positivity also gives
R <= 2^n M_*. When R > 16 M_* n^2, the selected integer
d=floor(log(R/M_*)/(2 log n)) lies within the valid degree range for
large n and satisfies M_* binomial(n,d) <= R/4.

The resulting differential inequality for s=log(R/M_*) is valid:
s' <= -g s/(2 log n). Its explicit integration from s <= n log 2
to s <= log(16 n^2) takes at most 2 g^{-1}(log n)^2.
The full norm is nonincreasing, so the threshold remains satisfied.
The final gap estimate then gives the stated additional
C_b A (log n + log(1/epsilon)) time, uniformly in the initial polymer
state. Since A=sqrt(bn), the final claimed order follows.

## Claim boundary

The result supplies a proved full-polymer arbitrary-start upper bound
and retains a logarithmic gap from the endpoint lower bound. The text
correctly leaves full-polymer worst-case cutoff unresolved. All constants
are allowed to depend on fixed b; no uniformity in varying b is claimed.
