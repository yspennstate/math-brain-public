SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B02, 2026-09-24T01:10:09Z.

# Source-freshness addendum — newest account03/B02 r43 and sharpened grouped low-rank funnel

After `REPORT.md` was committed, a newer compatible designated-partner report appeared and was resolved before handoff publication:

- `account03/B02` r43, report creation commit `4df8b2f9e629830dcc85e1c254dd5ac551b2ff95`, source-pin/check refresh through `d298129b29fae57620ce14cf74fd516bda63ac98`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260924T010811Z-account03-B02-qform-r43/REPORT.md`;
- theorem `QFORM-GROUPED-TWOSTAR-LOWRANK-FUNNEL-L1-v1`.

This addendum supersedes the r42-only 'latest partner' wording in the earlier immutable report. The earlier mathematics remains valid; the current first unpaid implication is narrowed further below.

## 1. Partner r43 input

On the r39 physical partition `H,L,R`, let

`N=A[L,R]`,
`B_*=A[L union R,H]`,
`E_N=||N||_F^2`, `E_*=||B_*||_F^2`,

and

`S=sum_h ||c_h||^2 ||r_h||^2
          ||P_(c_h^perp) N P_(r_h^perp)||_F^2`.

The newest partner proves the exact grouped-energy inequality

`boxed: S <= (1/4) E_N E_*^2.`                                  (A.1)

For a matrix `M` with squared singular values `x1>=x2>=...`, total energy `E=sum xj`, and `T2=sum_(j>=3)xj`, define

`R1_theta(M): x2<theta E`,
`R2_theta(M): T2<theta E`,                                     (A.2)

for `0<theta<=1/2`. Outside both tubes,

`E3(M)>=theta^3 E^3`.                                           (A.3)

Partner r43 combines (A.1)-(A.3) with the older marginal-free third-volume receiver and shows that, unless `N` or `B_*` lies in one of the four tubes, the full law has Fourier `L1`.

## 2. Sharp-HY improvement of the partner's integrated constant

The same deterministic funnel can be spliced instead to this slot's reviewed sharp-Hausdorff--Young marginal-free theorem

`||p_Q||_infinity <= C3 E3(M)^(-1/6)`,
`int |phi_Q| <=2pi C3 E3(M)^(-1/6)`,
`C3=10.3450832321475... .`                                     (A.4)

This gives a strictly smaller integrated constant without changing any geometric hypothesis.

Put

`rho=(2 sqrt(S))^(1/3)`.                                        (A.5)

If `||N||_F>=rho` and `N` is outside both tubes, then by (A.3)-(A.4)

`||p_Q||_infinity
 <= C3 theta^(-1/2) E_N^(-1/2)
 <= C3 theta^(-1/2) rho^(-1)`.

If `||N||_F<rho`, (A.1) implies

`E_* >=2sqrt(S)/||N||_F >rho^2`,

and the same bound follows from `B_*` whenever `B_*` is outside both tubes. Since

`rho^(-1)=2^(-1/3)S^(-1/6)`,

we obtain the sharpened newest-partner corollary

`boxed:
 ||p_Q||_infinity
 <= 8.21089800270 theta^(-1/2) S^(-1/6),
`                                                                  (A.6)

`boxed:
 int_R |phi_Q(t)|dt
 <=2pi * 8.21089800270 theta^(-1/2) S^(-1/6),
`                                                                  (A.7)

unless `N` or `B_*` lies in `R1_theta` or `R2_theta`.

This is an equation-level use of the newest completed designated-partner theorem: (A.1) is its grouped two-star energy bridge, while (A.4) is this slot's sharper reviewed-HY receiver on the literal physical block selected by that bridge.

## 3. Actual V1 inequality

The r39 grouped two-star branch supplies

`S >= (4/3125)V1`.                                               (A.8)

With the partner's convenient `theta=1/4`, (A.6) becomes

`||p_Q||_infinity <=16.4217960054 S^(-1/6)`

and therefore

`boxed:
 ||p_Q||_infinity <=49.8370497026 V1^(-1/6).
`                                                                  (A.9)

On the target-scale branch `V1>1/4`,

`boxed: ||p_Q||_infinity <62.790748.`                            (A.10)

This improves the newest partner's corresponding `50.8250418687 V1^(-1/6)` and `<64.0355401123` constants while keeping exactly its physical hypotheses.

The D5 receiver remains complementary on either literal block:

`||p_Q||_infinity <=(5e/sqrt(2)) E5(M)^(-1/10)`                  (A.11)

whenever the selected `M` has positive fifth exterior volume. No implication from the grouped resource to a D5 lower bound is asserted.

## 4. Updated exact remainder

The earlier report's coarse condition `E3(B_*)<V1/64` is now superseded as the primary bookkeeping endpoint by the stronger r43 funnel. On the grouped two-star branch, after the sharpened Fourier exit, the only surviving geometry is one of the four literal original-coordinate tubes

`x2(N)<E_N/4`,
`T2(N)<E_N/4`,
`x2(B_*)<E_*/4`,
`T2(B_*)<E_*/4`.                                                 (A.12)

Thus the next B02 implication is

`QFORM-LOWRANK-PAIRBLOCK-STARBLOCK-COUPLED-PAYMENT-v1`:

combine the exact/near-rank-two block currencies with the completed grouped Schur/coherent-star receivers so that the nonzero tail is retained and a genuine third physical smoothing credit is supplied by the coupled block. A two-dimensional projected-density argument alone remains Fourier-critical at `|t|^-1`.

Full QFORM and target-wide universal unweighted Fourier L1 remain OPEN / not refuted.
