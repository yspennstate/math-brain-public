SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T03:08:17Z.
attacking: the first unpaid joint-star resource-to-Fourier implication from the preceding B02 run; convert the physical-row times aggregate residual E2 resource into a dependence-safe fractional Fourier potential without a pointwise decay claim.

# Early substantive checkpoint: one physical row + residual E2 gives a subcritical Riesz estimate

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. Execution context: WITHOUT_VERIFIED_BRAIN.

Let I,J be disjoint ORIGINAL-coordinate banks and M=A[I,J]. Select one row x in I and write M=[m;L], where m is that physical row and L is the remaining cross block. Put R=||m||_2 and Z2=e_2(L^T L). Assume R>0 and Z2>0. Decoupling in the I-bank gives

|phi_Q(t)|^2 <= E_D A_t(D) B_t(D),
A_t(D)=|psi_x(2t m.D)|,
B_t(D)=prod_{i in I\{x}} |psi_i(2t (LD)_i)|,

where D=X_J-X_J' has independent coordinate densities g_j<=1.

The product-marginal density theorem gives ||p_(m.D)||_infinity<=sqrt(2)/R. Plancherel and f_x<=1 therefore imply

E A_t^2 <= (pi sqrt(2))/(R |t|).

For B_t^2 use the k=2 volume-sampling Brascamp--Lieb estimate with q=2. Because every 2-volume row marginal alpha_i<=1, the sharp-HY exponent 2/alpha_i is always >=2, so there is NO residual leverage gate. The same determinant/entropy calculation as the reviewed q-dependent theorem gives

E B_t^2 <= (e^2/2) (pi/|t|)^2 Z2^(-1/2).

Cauchy--Schwarz followed by the original decoupling square root yields

|phi_Q(t)| <= min(1, K |t|^(-3/4)),
K=e^(1/2) pi^(3/4) 2^(-1/8) R^(-1/4) Z2^(-1/8).

Hence for every 0<alpha<3/4 the weighted Fourier integral is finite. Using
|x|^(-alpha)=[Gamma(alpha) cos(pi alpha/2)]^(-1) int_0^infinity t^(alpha-1) cos(tx) dt
(with standard exponential regularization),

H_alpha(Q):=sup_s E|Q-s|^(-alpha)
 <= C_alpha [R^2 Z2]^(-alpha/6),

C_alpha = [ (3/4)/(alpha(3/4-alpha) Gamma(alpha) cos(pi alpha/2)) ]
          * [e^(1/2) pi^(3/4) 2^(-1/8)]^(4alpha/3).

At alpha=1/2 this simplifies to

H_(1/2)(Q) <= 6 e^(1/3) 2^(5/12) [R^2 Z2]^(-1/12)
            <11.178 [R^2 Z2]^(-1/12).

This directly consumes the preceding B02 joint-star compiler. In its branch a^2 e_2(N^T N)>=Z3/8, the selected full row has R^2>=a^2 and the residual block L=[c,N] has e_2(L^T L)>=e_2(N^T N). Thus

H_(1/2)(Q) <= 6 e^(1/3) 2^(2/3) Z3^(-1/12) <13.293 Z3^(-1/12).

This pays one of the two compiler resources by a dependence-safe fractional potential, while retaining all other cross couplings and arbitrary same-bank quadratic phases. It is not yet an L-infinity density theorem by itself. The remaining branch is the two-stars times transverse-Frobenius resource, and the next step is to test whether the newest fleet03/B02 outside-linear theorem can close a genuine subbranch without fixed-minor extraction.
