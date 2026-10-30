SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B13, 2026-09-23T06:03:26Z.
attacking: dependence-safe gluing of the completed partner L^{3/2} physical-pair theorem to its L^3 Schur-E2 theorem, without assuming pair/residual independence.

# Early substantive checkpoint

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Execution: WITHOUT_VERIFIED_BRAIN.

The designated partner fleet03/B13 completed the following live branch. A selected physical pair has conditional polynomial

  P_y(u,v)=d u^2+2a uv+e v^2+2 l(y)^T(u,v)+c(y),   a != 0,

and the associated Schur critical quadratic R(y) has, in the paid E2 branch,

  ||p_R||_3 < 12.257 |a|^(1/3) Z^(-1/6).

The partner proved a uniform conditional L^{3/2} bound for P_y but left the general pair/residual gluing open because l(y) depends on the same residual coordinates y.

There is a dependence-safe closure in the robust hyperbolic subbranch

  |d| < |a|/2,    |e| < |a|/2.                                    (C1)

Then B=[[d,a],[a,e]] is invertible indefinite and D=|det B|>=3a^2/4. Complete the physical pair square exactly:

  m(y)=B^{-1} l(y),
  P_y(u,v)=(z^T B z)+R(y),    z=(u,v)+m(y),

where all y-only terms are absorbed into the same Schur critical value R(y). Conditional on y, z_1,z_2 remain independent translates of the original cap-one marginals.

The completed orientation-uniform hyperbolic envelope gives, for every y,

  k_y(s) <= G_B(s):=D^(-1/2)[5.2+log_+(16 sqrt(D)/|s|)].          (C2)

Crucially, G_B is the SAME centered envelope for every y; it is translation-uniform in the inputs. Hence no independence between the pair and R is needed:

  p_Q(t)=E_y k_y(t-R(y))
        <=E_y G_B(t-R(y))
        =(G_B*p_R)(t).                                            (C3)

The partner's explicit envelope integration gives

  ||G_B||_(3/2) < 2.654 |a|^(-1/3).                              (C4)

Therefore Hölder in the single output variable and the paid Schur-E2 estimate imply

  ||p_Q||_infinity
     < 2.654*12.257 Z^(-1/6)
     < 32.531 Z^(-1/6).                                          (C5)

This closes the previously unpaid dependence gluing whenever the controlling pair is robustly hyperbolic in the original coordinates. No conditional density cap, rotated independence, moment, support bound, or small-matrix perturbation is used.

The remaining branch is now necessarily strong-diagonal: |d|>=|a|/2 or |e|>=|a|/2. A square kernel has only the common envelope |d|^{-1/2}s_+^{-1/2}; combining it with an L^3 residual by Hölder gives the scale ||p_R||_3^(3/4), and that exponent cannot be improved from only probability normalization plus an L^3 norm. Indeed p_L=L^{-1}1_[0,L] has ||p_L||_3=L^(-2/3)=M and

  integral_0^L u^(-1/2)p_L(L-u)du=2L^(-1/2)=2M^(3/4).            (C6)

Thus the strong-diagonal survivor genuinely needs the existing scalar-Schur / tri-hub / transverse-star structure; generic L^{3/2}-L^3 norm gluing is not the remaining issue.

I will now write the full proof, transfer it to arbitrary cap-one product laws through the already completed finite-mixture/no-attainment reduction, and intersect it with the pinned D5 obstruction from the required Fourier package.
