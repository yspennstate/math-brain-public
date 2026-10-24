SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B03, 2026-09-24T06:22:52Z.
attacking: a critical two-hub plus conditional whole-copy collision compiler — keep the hub-dependent residual inside its independent-copy weighted time budget, then use Cauchy-Schwarz in frequency only after the two-hub Plancherel gain.

# Early calculation — conditional collision budget closes the critical two-hub time integral

Target status: full unrestricted QFORM remains OPEN. Execution context: WITHOUT_VERIFIED_BRAIN.

Let original independent coordinates be split into two physical hubs H=(H1,H2), a product slope bank Y, and a source-disjoint bank W. Let S(Y)=B Y+d in R^2 with rank(B)=2 and put P=||p_S||_2. Allow arbitrary hub self-curvature C and arbitrary measurable same-bank phase R(Y). Let Z(h,W) be any real residual depending measurably on the hub value h and the source-disjoint W bank. Define

Q = H^T C H + 2 H^T S(Y) + R(Y) + Z(H,W).

For fixed h set psi_h(t)=E_W exp(i t Z(h,W)) and
G(t)^2=E_H |psi_H(t)|^2.

The standard two-hub projected Plancherel step, with the residual multiplier retained inside Cauchy-Schwarz over the ORIGINAL hub law, gives

|phi_Q(t)| <= pi P |t|^{-1} G(t),   t !=0.                      (E1)

Assume only the conditional whole-copy collision budget

K := int_R |t|^{-1/2} G(t)^2 dt < infinity.                      (E2)

This is dependence-safe: for each h,
|psi_h(t)|^2 is the characteristic function of Z(h,W)-Z(h,W'), with W,W' iid conditional on the same h; no (X-X',X+X') pair is separated or conditionally recapped.

For T>0,

int_{|t|>T}|t|^{-1}G(t)dt
 = int_{|t|>T}|t|^{-3/4}[|t|^{-1/4}G(t)]dt
 <= (int_{|t|>T}|t|^{-3/2}dt)^{1/2} K^{1/2}
 = 2 K^{1/2} T^{-1/4}.                                         (E3)

Combining (E1), (E3), and |phi_Q|<=1,

int_R |phi_Q(t)|dt <= 2T + 2 pi P K^{1/2} T^{-1/4}.              (E4)

The minimizer is

T_*=(pi P K^{1/2}/4)^{4/5};                                     (E5)

at T_* the second term is 8T_*, hence

int |phi_Q| <= 10 T_*                                           (E6)

and Fourier inversion yields

||p_Q||_infinity <= (5/pi)(pi P K^{1/2}/4)^{4/5}.                (E7)

Moreover phi_Q is L1, so the density is continuous and C_0.

This is different from the earlier independent-L2-residual theorem: it accepts a hub-dependent residual and asks only for a weighted whole-copy collision budget. It is also different from the conditional-L^r-density compiler: the receiver currency is directly the assignment-specific decoupled time integral.

## Actual designated-partner splice

The newest account02/B03 theorem `QFORM-DISJOINT-EXTERIOR-MASS-EXIT-v1`, canonical math-open-problems commit 5e5366b98337d13ba24bf666f4e42155553de7c2, proves for a quadratic residual on an independent W bank with disjoint exterior mass E0>0 the uniform whole-copy budget

K <= K0 E0^{-1/12},
K0=29.1511643034760... .                                        (E8)

Its physical-E3 proof is uniform under affine terms, so (E8) can be spent on Z(h,W) when the quadratic coefficient matrix on W is fixed and the h-dependence enters only through affine/constant terms.

For the slope projection S=BY+d the completed two-dimensional product projection theorem gives

P <= sqrt(2) D^{-1/4},  D=det(BB^T)>0.                           (E9)

Substitution of (E8)-(E9) into (E7) gives the scale-exact source-disjoint compiler

||p_Q||_infinity
 <= C_mix D^{-1/5} E0^{-1/30},                                  (E10)

where

C_mix=(5/pi)[(pi/4)*sqrt(2)*sqrt(K0)]^{4/5}
     =6.670623008323879... .                                     (E11)

Scaling check: D has degree 4 and E0 has degree 6 in the quadratic coefficients, so D^{-1/5}E0^{-1/30} has total degree -1 exactly.

This gives genuine linear small-ball scaling and a continuous C_0 density on the scoped decomposition. It does not claim the full target admits such a source-disjoint decomposition; extracting/routing that decomposition remains structural debt.
