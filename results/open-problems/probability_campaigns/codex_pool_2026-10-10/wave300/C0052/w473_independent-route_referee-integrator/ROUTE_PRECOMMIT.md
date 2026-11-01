# C0052 independent route, written before reading w471 or w472 artifacts

Time: 2026-10-10, approximately 09:15 Asia/Jerusalem.

Target: non-Gaussian critical 3D Ising spin-field scaling limit, with the precise formulation and current status still under verification. Prior local intake uses random-current intersection probabilities and a second-moment argument. This route uses the first Lee-Yang zero of the magnetization generating function.

For a finite ferromagnetic Ising box at zero field with free boundary, let M_L be total spin, V_L=Var(M_L), and i rho_L the closest zero of E exp(h M_L) in the upper imaginary half-plane. The Lee-Yang theorem puts all zeros on the imaginary axis. Factoring the even entire generating function into paired zeros gives V_L=2 sum_j rho_j^{-2} and -kappa_4(M_L)=12 sum_j rho_j^{-4}. Thus, with K_L=-kappa_4(M_L)/V_L^2 and z_L=rho_L sqrt(V_L),

    12/z_L^4 <= K_L <= 6/z_L^2.

Hence a uniform upper bound on z_L would force a nonzero normalized fourth cumulant. A Gaussian scaling limit with uniform fourth-moment integrability would require z_L to diverge. This route avoids an unproved current-intersection estimate but transfers the hard step to a uniform upper bound on the first normalized Lee-Yang zero at beta_c in 3D. No such bound is claimed here. I will derive the finite-volume identity and audit the exact match to the source's scaling-limit formulation.

The crucial boundary condition and field-observable match still need checking: a finite free-boundary total-spin limit is not automatically the infinite-volume smeared critical field. The first result is only a finite-volume conditional criterion.
