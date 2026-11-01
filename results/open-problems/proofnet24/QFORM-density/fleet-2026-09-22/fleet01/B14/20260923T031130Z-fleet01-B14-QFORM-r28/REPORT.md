SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B14, 2026-09-23T03:11:30Z.
attacking: mass-proportional fractional small-ball localization for the physical-pair logarithmic envelope; identify the exact thin-fiber normalization threshold and apply fleet02/B14 r24 to a target-valid inequality.

# fleet01/B14 r28 — mass-proportional logarithmic localization and a target-valid pair-log conditioning-order barrier

Programme: QFORM-DENSITY-3EIG-20260922. Status: NEW SUPPORTING LOCALIZATION THEOREM + TARGET-VALID PROOF-MECHANISM BARRIER. FULL QFORM REMAINS OPEN. Continuity is separate.

## Source pins actually used

2. Completed physical-pair logarithmic envelope: `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`, `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`.
3. Assigned partner fleet02/B14 r24, current report on master: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B14/20260923T025915Z-fleet02-B14-QFORM-r24/REPORT.md`; its key exact theorem is the overlap-power compiler and its exact fragmented overlap family
   `E_N=union_{j=1}^N [4^j,4^j+1/N]`,
   with
   `I_gamma(N)=int m_N(u)^gamma du = 2/(gamma+1)[(1-1/N)N^(1-gamma)+1/N]`.

No arbitrary-joint coarea, post-rotation independence, bounded-diameter localization, fixed-fragment-count assumption, moment bound, or pointwise quadratic Fourier decay is used.

## 1. New zero-tax localization theorem for logarithmic kernels

Let `(S,eta)` be a parameter space and let `nu_u` be finite positive measures on R with mass

`w(u)=nu_u(R)`, `0<=w(u)<=1`, `int w(u) deta(u)=1`.

Assume that for some `0<alpha<=1` and `K>0`, every slice has the **unnormalized mass-proportional** small-ball estimate

`nu_u{ |R-t|<rho } <= w(u) min(1,K rho^alpha)`                     (1)

for every `t in R`, `rho>0`, and almost every `u`.

Define

`Psi(z)=z` for `0<=z<=1`, and `Psi(z)=1+log z` for `z>=1`.

### Theorem 1 (mass-proportional fractional log localization)

For every `A>0`, uniformly in `t`,

`int_S int_R log_+( A/|R-t| ) dnu_u(R) deta(u)
 <= alpha^(-1) Psi(K A^alpha)`.                               (2)

Thus arbitrary fragmentation of the parameter law costs exactly zero provided the local small-ball certificate retains one full slice-mass power before normalization.

### Proof

For one slice, layer cake gives

`int log_+(A/|R-t|) dnu_u(R)
 = int_0^infty nu_u{|R-t|<A e^(-s)} ds`.

By (1), this is at most

`w(u) int_0^infty min(1, K A^alpha e^(-alpha s)) ds`.

If `z=K A^alpha<=1`, the integral is `z/alpha`. If `z>=1`, split at `s_0=alpha^(-1) log z`; the integral is `(1+log z)/alpha`. Hence the slice is at most

`w(u) alpha^(-1) Psi(KA^alpha)`.

Integrating and using `int w=1` proves (2). QED.

This is the exact logarithmic analogue of fleet02/B14's overlap-power theorem: the dangerous normalized-fiber factor never appears because the small-ball estimate is carried by the finite slice measure itself.

## 2. Actual application to the physical-pair logarithmic envelope

Let `B` be an invertible indefinite physical 2-by-2 block and put

`D=|det B|`, `kappa=sigma_min(B)`.

The source-pinned pair theorem says that after completing the pair, for every gradient cutoff `r>0`, the pair contribution against a scalar critical-value variable `R` is bounded by

`2 sqrt(2)/r + D^(-1/2) log_+( 2r^2/(kappa |t-R|) )`.          (3)

Suppose now that an arbitrary localization/disintegration produces finite critical-value measures `nu_u` satisfying (1). Integrating (3) against `nu_u`, then in `u`, and applying Theorem 1 with `A=2r^2/kappa` gives the **same constant as in the undisintegrated probability theorem**:

`||p_Q||_infinity
 <= 2 sqrt(2)/r
  + D^(-1/2) alpha^(-1)
    Psi( K (2r^2/kappa)^alpha )`.                              (4)

There is no support-radius, fragment-count, fragment-separation, translation, tail, or moment parameter in (4).

For a square remainder `R=a(Y-g(u))^2+h(u)` where, before normalization, each slice is `w(u)` times a cap-one probability law in the independent scalar `Y`, one has

`nu_u{|R-t|<rho} <= w(u) 2 sqrt(2/|a|) sqrt(rho)`.             (5)

Hence `alpha=1/2`, `K=2 sqrt(2/|a|)`, and (4) becomes

`||p_Q||_infinity
 <= 2 sqrt(2)/r
  + 2 D^(-1/2) Psi( 4r/sqrt(|a| kappa) )`.                    (6)

In the linear branch `32D<=|a|kappa`, optimizing in `r` yields

`||p_Q||_infinity <= 8*2^(1/4) (D |a| kappa)^(-1/4)`.         (7)

The point is not the numerical front constant but the exact localization interface: (6) survives arbitrary outside translations/fragments because the finite slice keeps its full mass `w(u)` until after the logarithmic singularity is integrated.

## 3. Partner r24 gives the sharp failure threshold for normalized thin fibers

Fleet02/B14 r24 proves that one full overlap power is sharp. For its legal separated set

`E_N=union_{j=1}^N [4^j,4^j+1/N]`

and iid `X,X'` uniform on `E_N`, define

`U=X-X'`, `V=X+X'`, `m_N(u)=|E_N intersect (E_N-u)|`.

Then

`p_U(u)=m_N(u)`,
`||p_(V|U=u)||_infinity = 1/(2m_N(u))`,                       (8)

and

`int m_N(u)^gamma du
 = 2/(gamma+1)[(1-1/N)N^(1-gamma)+1/N]`.                    (9)

In particular, differentiating (9) at `gamma=1` gives the exact overlap entropy

`int m_N(u) log(1/m_N(u)) du
 = 1/2 + (1-1/N) log N`.                                     (10)

So even a merely logarithmic dependence on the **normalized** fiber cap can accumulate a `log N` loss. Positive cap powers are worse: a local factor `m(u)^(-beta)` leaves the unnormalized mass power `m^(1-beta)`, and (9) grows like `N^beta` for every fixed `0<beta<1`.

## 4. Target-valid pair-log conditioning-order barrier

The preceding distinction is not cosmetic. Consider the exact target form on four original coordinates

`Q_N = 2 X_1 X_2 + (X_3+X_4)^2/2`,                            (11)

with matrix

`A = [[0,1,0,0],[1,0,0,0],[0,0,1/2,1/2],[0,0,1/2,1/2]]`.

Its eigenvalues are `{1,-1,1,0}`; hence it has three eigenvalues of absolute value one. Let `X_3,X_4` be iid uniform on `E_N`; `X_1,X_2` are arbitrary independent cap-one inputs.

### Safe proof order: original-coordinate conditioning

Condition on `X_3=x_3`. The indefinite pair `(X_1,X_2)` has

`D=kappa=1`.

The remainder is

`R=(x_3+X_4)^2/2`.

Since `X_4` still has density cap one, uniformly in the arbitrary translation `x_3`,

`P(|R-t|<rho | X_3=x_3) <= 4 sqrt(rho)`.                     (12)

Applying the completed pair-log smoothing theorem with fractional coefficient `H=4` gives

`||p_(Q_N | X_3=x_3)||_infinity <= 4 sqrt(2H)=8 sqrt(2)`.    (13)

Averaging over `X_3` preserves the same constant:

`boxed: ||p_(Q_N)||_infinity <= 8 sqrt(2)`                    (14)

for every `N`, despite arbitrarily distant fragments and no moment control.

### Unsafe proof order: conjugate-fiber normalization first

Instead condition on

`U=X_3-X_4`, `V=X_3+X_4`.

By (8), conditional on `U=u`, `V` has normalized density cap `1/(2m_N(u))`. For the remainder `R=V^2/2`, the best direct square small-ball estimate is

`P(|R-t|<rho | U=u) <= (2/m_N(u)) sqrt(rho)`.                (15)

The pair-log half-order compiler therefore gives the normalized conditional certificate

`||p_(Q_N | U=u)||_infinity <= 8 m_N(u)^(-1/2)`.             (16)

Multiplying by the actual slice mass `p_U(u)=m_N(u)` and averaging gives the proof bound

`8 int m_N(u)^(1/2) du
 = (32/3)[(1-1/N) sqrt(N)+1/N]`,                              (17)

which diverges like `(32/3) sqrt(N)`.

Thus the *same target-valid family* has the uniform direct bound (14), but the proof order

`condition on conjugate difference -> normalize thin sum fiber -> pay pair-log reciprocal square-root -> average`

loses order `sqrt(N)`. This does not refute the pair-log theorem and does not refute QFORM. It proves that pair-log must be applied before this thin-fiber normalization, or else one must retain a full unnormalized overlap power as in Theorem 1.

This is an actual application of fleet02/B14 r24: its exact overlap formula (9) turns the conditional pair-log inequality (16) into the explicit divergent certificate (17), while its exponent-one compiler certifies the zero-tax positive inequality (4) whenever the local small-ball estimate is mass-proportional.

## 5. Consequence for the full programme

For translation/localization purposes, the surviving rule is now exact:

* arbitrary shifts and remote fragments are harmless if localization is performed on whole original-coordinate factors or on finite slices whose small-ball certificate carries one full slice-mass power;
* normalizing a thin conjugate fiber before paying any positive reciprocal curvature exponent can destroy uniformity, even inside an exact three-large-eigenvalue target matrix;
* pair-log smoothing is therefore compatible with arbitrary-law localization only in an **unnormalized mass-proportional** compiler, or when one conditions on original coordinates so the active cap-one law is retained.

The unresolved full-target implication is structural: from `s_3(A)>=1`, expose a useful pair/ridge/bank/cross certificate while preserving the original product or unnormalized overlap mass through the reciprocal-curvature step. The theorem above removes support/tail/translation bookkeeping from that implication, but it does not itself force the needed matrix certificate.

Claim IDs proposed: `QFORM-MASS-PROPORTIONAL-FRACTIONAL-LOG-LOCALIZATION-v1`; `QFORM-PAIRLOG-THIN-FIBER-NORMALIZATION-BARRIER-v1`.

FULL QFORM remains OPEN. No unrestricted continuity claim is made.
