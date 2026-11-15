VERDICT: PARTIAL the actual cube-capacity coefficient with a bounded error and a strict improvement of the previous trial constant

The preceding result holds under independent verification. The brief web
check found no later solution of the lattice critical-exponent problem.

The new result identifies the true leading lattice cube-capacity
coefficient, rather than another restricted trial-family coefficient.
For SRW Green covariance, define

    kappa = inf { (1/6) integral |grad F|^2 :
                  F compactly supported and Lipschitz,
                  F=1 on [-1,1]^3 }.

PROOF.md proves, for every integer R>=1,

    kappa R <= cap(B_R) <= kappa(R+1/2).

Consequently cap(B_R)=kappa R+O(1), with the error in [0,kappa/2].
The new ingredient is a reverse transfer by trilinear interpolation;
the predecessor's unit-cell averaging supplies the other direction.
No continuum-limit theorem or existence of a minimizer is assumed.

A variation supported in six face regions also proves

    2 pi/3 <= kappa <= C_1 < C_cube,
    C_1 = C_cube - 486 pi^2 C_cube^2/(24+16 pi)^4,

where C_cube is the exact constant from round 4. Thus its distance-profile
class is strictly suboptimal for the actual leading capacity coefficient.
The value of kappa is identified variationally, not evaluated in closed form.

For the same relative one-arm radius as before, the consequence is

    liminf_{t->0} t^2 log(1/t) L_rel(t)
      >= (log 2)^2/(8 kappa)
      >= (log 2)^2/(8 C_1) > (log 2)^2/(8 C_cube).

This uses the same existing density input from Stephen Muirhead,
[arXiv:2206.10724v2](https://arxiv.org/html/2206.10724v2), Theorems 1.2
and 1.10. Its excluded endpoint is not used.

AUDIT.md checks the interpolation by a separate Gram-matrix calculation,
the decrement by a fixed-amplitude trial function, and the crossover
coefficient by Gaussian tails instead of Holder. It checks support,
boundary cells, normalization, every integer radius, and finite cutoffs.

Commands: predecessor files were discovered with `rg --files` and read
with `OMP_NUM_THREADS=1 nice -n 15 cat <paths>`. Final file and consistency
checks are recorded in LOG.md. No numerical script, simulation, numerical
workload, or decimal evaluation was run. The sandbox denied priority
changes; work remained analytic with lightweight file reads. All authored
files are in this folder. No git, subagents, external writes or edits to
earlier folders were used.

What failed or remains uncertain: the logarithmic loss is unchanged. No
connection-specific score estimate or comparison to a conventional
correlation length was obtained. No lattice critical exponent, exponent
existence, critical nonpercolation, or agreement with cable exponents is
proved. The capacity interpolation may be standard; novelty of this
elementary argument or the explicit face variation is not established.
The L_rel coefficient is a lower bound, not proved optimal.

Next worker: the deterministic capacity coefficient is now identified,
so further capacity improvements cannot change the logarithmic order.
The substantive next target remains a connection-specific estimate for
-d/dh log p_R(h) of order sqrt(R), uniform over
h in [h_*,h_*+c/sqrt(R)], or a comparison with a specified conventional
correlation length. For capacity questions, (1) in PROOF.md gives a
uniform bounded error and section 6 gives an explicit admissible angular
variation; neither should be mistaken for an exponent calculation.

Task: “take the NEXT checkable step on this problem, building on that work”
— 15 November 2026, first retained local clock reading 08:14:56 +0400
(Asia/Tbilisi).
