SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B02, 2026-09-24T01:08:11Z.
attacking: the r39/r42 grouped two-star residue; convert fixed grouped transverse mass into an integrated-Fourier exit unless the interbank block or the total star block is quantitatively near rank one/two.

# account03/B02 r43 — grouped two-star low-rank funnel

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Integrated Fourier estimate  
Status: **NEW SUPPORTING FOURIER COMPILER / GROUPED TWO-STAR GENERIC BRANCH PAID / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The exact owner target is unchanged: independent ORIGINAL real coordinates with one-dimensional probability densities bounded by one, arbitrary real symmetric `A`, and at least three eigenvalues of modulus at least one. No Gaussianity, log-concavity, moment, bounded/connected support, iid hypothesis, post-rotation independence, conditional-density cap, scalar pointwise quadratic van-der-Corput estimate, or deletion of a small quadratic tail is used.


## 1. Source-pinned inputs actually used

### 1.1 Marginal-free physical third-volume crossing

The completed theorem used below is `QFORM-Z3-CROSSING-MARGINAL-FREE-v1`, with current source

- `yspennstate/math-open-problems@master`, report `proofnet24/QFORM-density/fleet-2026-09-22/account02/B03/20260923T184716Z-account02-B03-QFORM-auto11/REPORT.md`;
- supporting projected-crossing proof `yspennstate/math-open-problems@829192412f2a2d84e72b4bed91115fc5fab68401`, path `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`;
- prior B02 compiler `yspennstate/math-open-problems@c8536549aca3308f1773992e46a6abe4a1dc9922`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T170106Z-account03-B02-qform-r35/REPORT.md`.

For every literal original-coordinate cross block `M=A[I,J]` with

`Z_3=e_3(MM^T)>0`,

the full ambient law has a continuous `C_0` density and

`||p_Q||_infinity <= C_3 Z_3^(-1/6)`,

`int_R |phi_Q(t)| dt <= 2 pi C_3 Z_3^(-1/6)`,

where

`C_3=3*2^(4/3)*e^(1/3)=10.550168831164775...`.                    (1.1)

All same-bank quadratic terms, affine terms, signs, outside couplings, and additional spectrum are retained.

### 1.2 Immediate grouped two-star source

From r39/r40, for one actual original-coordinate partition `H,L,R`, put

`N=A[L,R]`,
`c_h=A[L,h]`, `r_h=A[h,R]`,

`T_h=||c_h||^2 ||r_h||^2
      ||P_(c_h^perp) N P_(r_h^perp)||_F^2`,

`S=sum_(h in H) T_h`.                                               (1.2)

On the grouped two-star alternative produced from the overlap-one third-compound mass `V_1`,

`S >= (4/3125)V_1`.                                                (1.3)

In particular, on the target-scale branch `V_1>1/4`,

`S>1/3125`.                                                        (1.4)

The source is `yspennstate/math-open-problems@f2d4617424eb9e168515ea3fd7043d31571fb253`, path `proofnet24/QFORM-density/fleet-2026-09-22/account03/B02/20260923T210023Z-account03-B02-qform-r39/REPORT.md`.

### 1.3 Designated partner account04/B02

The partner result applied at an actual new inequality in Section 5 is

- `QFORM-ZERO-DIAGONAL-TRIPLE-CONTINUITY-v1`;
- `yspennstate/math-open-problems@0b11995430ce407a8852ac3bc5651491f2ee64f7`;
- `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260922T193108Z-account04-B02-QFORM-r2/REPORT.md`.

On its exact overlap, a nonsingular physical zero-diagonal principal triple `H_0` gives

`L:=int_R |phi_Q(t)|^2 dt
   <= 6 pi 2^(2/3) |det H_0|^(-1/3)`.                              (1.5)

I also use account04/B02's strong-cut inequality from
`yspennstate/math-open-problems@674f13a108a33176aafffe8f9b6d44ec3a89f03a`, path `proofnet24/QFORM-density/fleet-2026-09-22/account04/B02/20260923T151038Z-account04-B02-QFORM-r1/REPORT.md`, only as a compatibility/application check in Section 6.

## 2. A uniform pointwise tail for the physical `Z_3` crossing theorem

The source theorem (1.1) was previously recorded mainly through its integrated consequence. Its branch proof actually yields one uniform tail constant.

### Lemma 2.1 — `QFORM-Z3-CROSSING-UNIFORM-TAIL-v1`

For every literal original-coordinate cross block `M` with `Z_3=e_3(MM^T)>0`,

`boxed:
 |phi_Q(t)|
 <= min{1, 4 sqrt(e) pi^(3/2) Z_3^(-1/4)|t|^(-3/2)}.
`                                                                       (2.1)

#### Proof

The account02/B03 proof is exhaustive.

1. If all third-volume row marginals are at most `1/2`, its source Theorem D gives coefficient

`K_0=(2pi)^(3/2)e^(3/4) Z_3^(-1/4)`.

Since `2^(3/2)e^(3/4) < 4e^(1/2)`, this is below (2.1).

2. If a physical row is heavy, the exact identity in that proof is

`J=S_0^2 Z_2 > Z_3/2`,                                              (2.2)

where `S_0` is the hub crossing norm and `Z_2` the projected two-volume.

On the one-hub diffuse subcase, the grouped projected-crossing theorem has coefficient

`2^(7/4)pi^(3/2)e^(1/2) S_0^(-1/2)Z_2^(-1/4)`.

By (2.2) this is strictly below

`2^(7/4)2^(1/4)pi^(3/2)e^(1/2)Z_3^(-1/4)
 =4sqrt(e)pi^(3/2)Z_3^(-1/4)`.

3. If a second original row is promoted and the remaining one-volume is diffuse, the `(k,ell)=(2,1)` grouped-crossing theorem has coefficient

`2^(5/4)pi^(3/2)(S_1^2 Z_1)^(-1/4)`.

The second heavy-row identity gives `S_1^2 Z_1>J/2>Z_3/4`, hence this coefficient is below `2^(7/4)pi^(3/2)Z_3^(-1/4)`, again smaller than (2.1).

4. If a third original row is promoted, the literal rank-three crossing has singular-value product `P_3>sqrt(J)/2`. The exact-rank-three Plancherel theorem, with one side consisting of exactly three original coordinates and the other a three-dimensional product projection, gives coefficient

`2^(3/4)pi^(3/2)P_3^(-1/2)
 <2^(3/2)pi^(3/2)Z_3^(-1/4)`,

also smaller than (2.1).

Thus (2.1) holds in every source branch. Integrating its minimum gives

`(2pi)^(-1) int min(1,K|t|^(-3/2))dt
 =3K^(2/3)/pi
 =C_3 Z_3^(-1/6)`,

which exactly recovers (1.1). QED.

This pointwise tail does not contradict the live correction against law-uniform scalar quadratic van der Corput. It is a three-credit **bilinear physical crossing** estimate with `Z_3>0`, proved by product-preserving Plancherel and hub promotion.

## 3. Dimension-free spectral funnel for one physical cross block

Let `M` be a real matrix, with squared singular values

`x_1>=x_2>=x_3>=...>=0`,

`E=sum_r x_r=||M||_F^2`,

`T_2=sum_(r>=3)x_r`,

`Z_3=e_3(MM^T)`.

For `0<theta<=1/2`, define the two low-rank tubes

`R1_theta(M): x_2<theta E`,

`R2_theta(M): T_2<theta E`.                                       (3.1)

### Lemma 3.1 — `QFORM-E3-SPECTRAL-TUBE-DICHOTOMY-v1`

If neither tube in (3.1) occurs, then

`boxed: Z_3 >= theta^3 E^3.`                                      (3.2)

Hence, when `M` is an original-coordinate physical cross block, either one of the two tubes holds, or the full quadratic law has

`boxed:
 |phi_Q(t)|
 <= min{1,
 4 sqrt(e) pi^(3/2) theta^(-3/4)E^(-3/4)|t|^(-3/2)}
}`                                                                  (3.3)

and

`boxed:
 ||p_Q||_infinity <= C_3 theta^(-1/2) E^(-1/2),
 int |phi_Q| <= 2pi C_3 theta^(-1/2)E^(-1/2).
}`                                                                  (3.4)

#### Proof

The `e_3` sum contains all terms `x_1x_2x_k`, `k>=3`; therefore

`Z_3 >= x_1 x_2 T_2 >= x_2^2 T_2`.

Outside the tubes, `x_2>=theta E` and `T_2>=theta E`, which proves (3.2). Equations (3.3)-(3.4) follow from Lemma 2.1 and (1.1). QED.

No dimension appears.

## 4. Main new theorem: grouped two-star mass forces Fourier `L1` unless a genuine low-rank collar survives

Return to the physical partition `H,L,R` of Section 1 and define the total star block

`B_*:=A[L union R,H]`.                                              (4.1)

Its squared Frobenius energy is

`E_*:=||B_*||_F^2
    =sum_h (||c_h||^2+||r_h||^2)`.                                (4.2)

Let `E_N=||N||_F^2`.

### Lemma 4.1 — grouped energy inequality

`boxed: S <= (1/4) E_N E_*^2.`                                    (4.3)

#### Proof

For each h,

`T_h <= ||c_h||^2||r_h||^2 ||N||_F^2
     <= (1/4)(||c_h||^2+||r_h||^2)^2 E_N`.

Sum in h and use `sum b_h^2 <= (sum b_h)^2` for the nonnegative numbers `b_h=||c_h||^2+||r_h||^2`. QED.

### Theorem 4.2 — `QFORM-GROUPED-TWOSTAR-LOWRANK-FUNNEL-L1-v1`

Assume `S>0`. Fix `0<theta<=1/2`. Then **at least one** of the following holds:

1. the interbank block `N=A[L,R]` lies in `R1_theta(N)` or `R2_theta(N)`;
2. the total star block `B_*=A[L union R,H]` lies in `R1_theta(B_*)` or `R2_theta(B_*)`;
3. the full ambient quadratic form has a continuous `C_0` density and

`boxed:
 |phi_Q(t)|
 <= min{1,
 2sqrt(2e) pi^(3/2) theta^(-3/4)S^(-1/4)|t|^(-3/2)},
}`                                                                  (4.4)

`boxed:
 ||p_Q||_infinity
 <= 6 e^(1/3) theta^(-1/2) S^(-1/6),
}`                                                                  (4.5)

`boxed:
 int_R |phi_Q(t)|dt
 <= 12pi e^(1/3) theta^(-1/2)S^(-1/6).
}`                                                                  (4.6)

#### Proof

Put

`rho=(2 sqrt(S))^(1/3)`.                                           (4.7)

If `||N||_F>=rho` and N is outside both tubes, Lemma 3.1 applied to the literal physical cross block N gives

`E_N^(1/2)=||N||_F>=rho`,

so its tail constant in (3.3) is at most

`4sqrt(e)pi^(3/2)theta^(-3/4)rho^(-3/2)
 =2sqrt(2e)pi^(3/2)theta^(-3/4)S^(-1/4)`.                         (4.8)

If `||N||_F<rho`, (4.3) gives

`E_* >= 2sqrt(S)/||N||_F > 2sqrt(S)/rho = rho^2`.                  (4.9)

If `B_*` is outside both tubes, Lemma 3.1 applied to the literal physical cross block `B_*` gives the same bound (4.8), since `E_*^(-3/4)<rho^(-3/2)`.

Thus, unless N or `B_*` lies in one of the two stated low-rank tubes, the common tail (4.4) holds. Integrating the minimum yields

`(2pi)^(-1)*6[2sqrt(2e)pi^(3/2)]^(2/3)
 theta^(-1/2)S^(-1/6)
 =6e^(1/3)theta^(-1/2)S^(-1/6)`,

which is (4.5), and (4.6) is `2pi` times (4.5). QED.

This is the desired aggregate-before-selection step: diffuse third-star volume is not selected one physical triple at a time. Either one whole physical cross block supplies the third exterior volume, or the geometry is forced into an explicit near-rank-one/two collar.

## 5. Application to the live `V_1` grouped two-star branch

Insert (1.3) into Theorem 4.2. Unless `N` or `B_*` lies in a `theta` low-rank tube,

`||p_Q||_infinity
 <= 3*2^(2/3)*5^(5/6)*e^(1/3)
    theta^(-1/2)V_1^(-1/6)`.                                      (5.1)

For the convenient quantitative choice `theta=1/4`,

`boxed:
 ||p_Q||_infinity <= 50.8250418687 V_1^(-1/6).
}`                                                                  (5.2)

On the actual target-scale branch `V_1>1/4`,

`boxed:
 ||p_Q||_infinity <64.0355401123,
 int |phi_Q|<402.3471647704.
}`                                                                  (5.3)

Hence the generic grouped two-star residue is now paid by genuine Fourier `L1`. The surviving B02 geometry is sharply restricted to

- `x_2(N)<E_N/4` or `T_2(N)<E_N/4`, or
- `x_2(B_*)<E_*/4` or `T_2(B_*)<E_*/4`.

Those are actual near-rank-one/two collars on literal original-coordinate blocks, not a statement about rotated random variables. The fresh account02/B20 exact-rank-two four-currency theorem (`math-open-problems@246f7b039bd6a1411ceccfa38bf922cac02ab5dc`) is therefore a directly relevant successor: it already pays the transverse exact-rank-two currencies and isolates Schur/internal-star/extreme-condition remnants.

## 6. Designated account04/B02 theorem applied at a new equation

Assume additionally the exact scope of partner theorem (1.5), and stay on the Fourier exit of Theorem 4.2. Write

`D_0=|det H_0|`.

The new high-frequency envelope is

`|phi_Q(t)| <= K_S |t|^(-3/2)`,

`K_S=2sqrt(2e)pi^(3/2)theta^(-3/4)S^(-1/4)`.                      (6.1)

Partner account04/B02 supplies

`L=int|phi_Q|^2 <=6pi2^(2/3)D_0^(-1/3)`.                          (6.2)

For every `T>0`, Cauchy-Schwarz below T and the tail above T give

`int |phi_Q|
 <= sqrt(2LT)+4K_S T^(-1/2)`.                                    (6.3)

Optimizing at `T=4K_S/sqrt(2L)` yields

`int |phi_Q| <=4K_S^(1/2)(2L)^(1/4)`.                             (6.4)

Fourier inversion therefore gives the **new partner hybrid**

`boxed:
 ||p_Q||_infinity
 <= 2^(29/12) 3^(1/4) e^(1/4)
    D_0^(-1/12) theta^(-3/8) S^(-1/8).
}`                                                                  (6.5)

The numerical front coefficient before the scale factors is

`2^(29/12)3^(1/4)e^(1/4)=9.02283655442...`.                       (6.6)

On the r39 resource `S>=(4/3125)V_1`, with `theta=1/4`,

`boxed:
 ||p_Q||_infinity
 <=34.8910742403 D_0^(-1/12)V_1^(-1/8).
}`                                                                  (6.7)

At `V_1>1/4`,

`boxed:
 ||p_Q||_infinity
 <41.4927137367 D_0^(-1/12).
}`                                                                  (6.8)

This is an equation-level use of the designated account04/B02 theorem. Continuity on this overlap comes from Theorem 4.2's genuine Fourier `L1`, not from the partner `L2` estimate alone.

As a separate compatibility check, account04/B02's strong-cut theorem has the same physical cross block energy `E>11907/16384` and, outside its `E/64` near-rank-one/two tubes, the exact product floor

`x_1x_2T_2>(63/1048576)E^3`.

Since `Z_3>=x_1x_2T_2`, (1.1) gives again

`||p_Q||_infinity<62.5333117910`,
`int|phi_Q|<392.9083858543`,                                      (6.9)

agreeing with the earlier r35 transfer. I record this only as a consistency check, not a new claim.

## 7. Failed shortcut explicitly preserved

A tempting extension of the r36 `3x2` kernel-curvature theorem is to rotate a large rank-two star block to two active directions plus one kernel direction and then integrate the remaining kernel complement away. This is **not** justified for arbitrary rough product laws: after the analytic rotation, the same-bank quadratic phase couples the chosen kernel direction to the leftover kernel complement, so integrating the complement produces a `t`-dependent amplitude in the scalar quadratic fiber. The r36 translation-uniform `L_t^4` scalar estimate does not apply to such an arbitrary `t`-dependent amplitude, and conditioning on rotated variables would violate product provenance. This run therefore does not use that shortcut.

The new grouped theorem avoids the issue entirely by applying the already-proved whole-block physical `Z_3` receiver before any low-rank reduction.

## 8. Deterministic regression and status

`CHECK.py` beside this report tests two symbolic inequalities on 3,000 seeded random instances:

1. `S <= (1/4)||N||_F^2 ||B_*||_F^4`;
2. outside the `theta=1/4` tubes, `e_3(MM^T)>=theta^3||M||_F^6`.

There were zero violations. The maximum observed ratio in (1) was `0.8787736084703642`; the minimum observed ratio `e_3/(theta^3 E^3)` on the sampled non-tube states was `2.0524329468659417`. These are corroborative checks only; Sections 3-4 are the proof.

The full universal QFORM conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The unrestricted target-wide universal statement `sup int_R |phi_Q|<infinity` remains **OPEN / not refuted**. This run proves Fourier `L1` only on the stated grouped two-star non-low-rank branch.

The next precise B02 mechanism is

`QFORM-LOWRANK-PAIRBLOCK-STARBLOCK-COUPLED-PAYMENT-v1`:

start from the four surviving literal tubes in Section 5, combine the fresh account02/B20 exact-rank-two four-currency theorem with r40's coherent-rank-one Schur receiver, and pay the coupled case where one block is near rank two while the other supplies the missing third smoothing credit, without deleting the nonzero tail. The extreme-condition/Schur currency must remain explicit.

No task identity, schedule, cadence, enabled/paused state, notification, email, Drive, public release, paid API/model, installation, permission, or cross-account authentication state was changed.
