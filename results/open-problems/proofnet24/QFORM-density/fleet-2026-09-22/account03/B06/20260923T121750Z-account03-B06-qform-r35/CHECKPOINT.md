SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T12:17:50Z.
attacking: the shared-bank-square survivor by composing the curved one-sided half-Riesz kernel with a conditionally capped translated square, then testing it on an actual coupled near-coloop family.

# Early substantive checkpoint

The first useful implication is a dependence-safe square transducer at the half-Riesz level. Let F be a sigma-field, let R and Psi be F-measurable, and suppose Z|F has a conditional density capped by L almost surely. For a!=0,

Q=R+a(Z+Psi)^2

has, for a.e. t,

p_Q(t) <= L/sqrt(|a|) E[ 1_{a(t-R)>0} |t-R|^(-1/2) ].

This follows by conditioning on F: translation by Psi does not change the conditional cap, and the two roots of a z^2=t-R give the usual one-sided square kernel. Unlike the completed density-to-square theorem, this only asks for a one-sided half-Riesz estimate of R, so R itself may have an unbounded density.

Applied to the existing scalar/dependent-pair base R=delta Y^2+2k UY, Y=gamma X+H, with X independent of (H,U), this immediately extends the current B06/account02-B16 kernels from an independent smoothing square to an arbitrarily base-dependent translation of a fresh capped scalar:

Q=delta Y^2+2k UY+beta[Z+Psi(X,H,U)]^2.

The already-proved half-Riesz calculations give the same constants: for delta beta>=0, all t,

||p_Q||inf <= 8 L_Z sqrt(L_X L_U/|beta gamma k|),

with 4 instead of 8 at delta=0; for delta beta<0, on the two-sheet side t beta<0,

p_Q(t) <= 4 sqrt(2) L_Z sqrt(L_X L_U/|beta gamma k|).

Concrete coupled target family: keep the orthonormal near-coloop spectral coordinates (Y,U,V) from the previous run, but replace the smoothing square by (V+theta Y+zeta U)^2. With r=(theta,zeta), rho=||r||, the 3x3 spectral matrix is B_delta+Delta_r, where

Delta_r=[[theta^2,theta*zeta,theta],[theta*zeta,zeta^2,zeta],[theta,zeta,0]].

Delta_r has eigenvalues 0 and (rho^2 +/- rho sqrt(rho^2+4))/2, hence

epsilon(rho)=||Delta_r||op=(rho^2+rho sqrt(rho^2+4))/2.

For rho<1/sqrt(2), epsilon<1. Since the uncoupled B_delta has all three eigenvalue moduli >=1 in both the delta>=0 family and the delta=-eta<=0 family, Weyl gives every eigenvalue modulus of B_delta+Delta_r at least 1-epsilon. Therefore scaling the whole quadratic form by (1-epsilon)^(-1) restores the exact target hypothesis without weakening the density bound.

This is a genuine shared/coupled smoothing square: the square contains both Y and U, while the fresh scalar V remains a disjoint original-source reserve. It is not covered by a density-to-square argument when the base 2UY has its logarithmic rank-two singularity.

Remaining work this run: write the complete theorem/proof, close the positive- and negative-pivot coupled target families with explicit constants, apply a completed account04 theorem at an actual equation, refresh corrections/control, and publish the source-pinned handoff/memory snapshot.
