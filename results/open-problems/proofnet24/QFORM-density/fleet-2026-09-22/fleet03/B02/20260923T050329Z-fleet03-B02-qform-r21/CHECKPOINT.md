SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B02, 2026-09-23T05:03:29Z.
attacking: repair the compound-hub edge-times-E2 branch by comparing the cross-only anchored Schur packet with the TRUE full physical-pair Schur packet, then apply fractional-volume smoothing only at its stated marginal gates.

# Early substantive checkpoint — exact rank-one repair of the cross-only / true-pair Schur gap

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Execution: `WITHOUT_VERIFIED_BRAIN`.

The immediate live obstruction is fleet03/B06's target-valid witness showing that a large cross-only anchored `e_2` packet may disappear after the true full indefinite physical pair is completed. The missing algebra is nevertheless only rank one.

Let two physical anchor coordinates be `x,y`. Write their principal pair

`P=[[d,a],[a,e]]`, `delta=de-a^2`,

with `a!=0`, `delta!=0`. For disjoint residual physical banks `U,V`, set

`u=A[U,x]`, `c=A[U,y]`, `r=A[x,V]`, `v=A[y,V]`, `N=A[U,V]`.

The cross-only anchored Schur block and the TRUE full-pair Schur cross block are

`S=N-c r^T/a`,

`T=N-[u,c] P^{-1} [r;v]`.

Define

`xi0=a u-d c`, `eta0=a v-e r`.

A direct expansion gives the exact identity

`T = S + xi0 eta0^T/(a delta)`.                                      (C.1)

Thus the full-pair correction that invalidated the naive splice is always rank one.

For arbitrary matrices `S` and vectors `p,q`, exterior squaring gives

`C_2(S+p q^T)=C_2(S)+L_p S iota_q`.                                  (C.2)

Moreover

`||L_p S iota_q||_HS
 =||p|| ||q|| ||P_(p^perp) S P_(q^perp)||_F`,                         (C.3)

and the transverse matrix in (C.3) is unchanged if `S` is replaced by `S+p q^T`.

Applying (C.2)-(C.3) to (C.1), with

`F=||P_(xi0^perp) S P_(eta0^perp)||_F
  =||P_(xi0^perp) T P_(eta0^perp)||_F`,

produces

`sqrt(E2(S))
 <=sqrt(E2(T)) + ||xi0|| ||eta0|| F/(|a delta|)`.                     (C.4)

Hence

`max{ a^2 E2(T),
      (||xi0||^2 ||eta0||^2/delta^2) F^2 }
 >= a^2 E2(S)/4`.                                                     (C.5)

For the anchored cross block `B=[[a,r^T],[c,N]]`, the exact incident-volume identity from the previous B02 run is

`J_xy=a^2 E2(S)`.

Therefore

`max{ a^2 E2(T),
      (||a u-d c||^2 ||a v-e r||^2/delta^2) F^2 }
 >= J_xy/4`.                                                          (C.6)

This is the desired correction-safe structural compiler: heavy cross-only `E2` cannot simply vanish. It either survives as TRUE full-pair-Schur `E2`, where pair-log/fractional-volume receivers are legal, or its destruction forces an explicit same-side correction packet.

The newest fractional third-volume theorem is applied as follows. For an original cross block `B` with `Z=E3(B)>0`, let `alpha_i,beta_j` be the squared-3-minor inclusion marginals. For any `1<q<3/2`, if all row marginals or all column marginals are at most `q/2`, the newest volume-stability result gives the continuous bound

`||p_Q||inf <= [3e/((3-2q)sqrt(q))] Z^(-1/6)`.

If both gates fail, there are physical anchors with joint incident mass

`J_xy>(q-1)Z`.

When their cross edge is nonzero and principal pair is nonsingular, (C.6) sharpens the failure branch to

`max{ a^2 E2(T), same-side-correction-resource } > (q-1)Z/4`.         (C.7)

This goes beyond the already-known gate-failure-to-anchor statement by preserving the TRUE pair Schur currency demanded by the live correction.

The first remaining analytic substep is to spend the second term of (C.7), or the first term when its own `E2` minor-marginal gate is concentrated. The full QFORM conjecture and the target-wide unweighted `L1` characteristic-function criterion remain OPEN.
