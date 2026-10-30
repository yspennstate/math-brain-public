SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B12, 2026-09-23T03:53:18Z.
attacking: replace the previous exact shielding condition for arbitrary-magnitude added spectrum by a rank-plus-unshielded-norm decomposition, so small dense tails and approximately shielded large eigenvalue changes can be controlled simultaneously in original coordinates.

# Early substantive checkpoint — leaky shielding reduction

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN.

Let an original-coordinate cross block of the final quadratic matrix be

M = M0 + L + E,

and let P be an orthogonal projection on the row bank with max_i P_ii <= 1/2. The preceding fleet02/B12 theorem required exact shielding (I-P)L=0. The new observation is that exact shielding is unnecessary: split

L_sh = P L,     L_leak = (I-P)L.

Then

M = M0 + L_sh + E',      E' = L_leak + E,

with (I-P)L_sh=0, rank(L_sh)<=rank(PL), and

||E'||op <= ||(I-P)L||op + ||E||op.

Thus an arbitrary-magnitude added spectral component is paid by rank only in its protected row component and by operator norm only in its unprotected cross-cut component. If

r >= rank(PL),
eta = ||(I-P)L||op,
delta >= ||E||op,
rho = eta + delta,

a1=(s_{r+1}(M0)-rho)_+,
a2=(s_{r+2}(M0)-rho)_+,
B^2=sum_{k>=r+3}(s_k(M0)-rho)_+^2,
epsilon0=||(I-P)M0||op,

then the previous rank-reserve minimax argument applied to L_sh and E' gives

s1(M)>=a1,  s2(M)>=a2,  T2(M)>=B^2,

while

||(I-P)M||op <= epsilon0 + rho.

Hence, if a2,B>0 and epsilon0+rho <= B/15, the completed collective-tail theorem gives

||p_Q||infinity <= (9 sqrt(3)e/2) (a1 a2 B)^(-1/3),

with arbitrary self blocks, outside couplings and affine terms of the final matrix. No claim that X^T E X is small is used.

The required e5f D' theorem also applies directly: the leakage gate implies

alpha_i <= (1+sqrt(3)/15)^2/2 = 0.6221367205... < 2/3,

so e5f D' with h=2/3 gives the source-valid fallback

||p_Q||infinity <= 9 sqrt(3e) (a1 a2 B)^(-1/3).

For a spectral cloud S=sum_a tau_a v_a v_a^T across a cut I|J,

L=S[I,J]=sum_a tau_a (v_a)_I (v_a)_J^T,

and therefore

eta <= sum_a |tau_a| ||(I-P)(v_a)_I||_2 ||(v_a)_J||_2.

This is the intended hybrid interface: very large |tau_a| are allowed when their unshielded physical footprint correspondingly shrinks, while the shielded footprint can be arbitrarily large with no norm charge.
