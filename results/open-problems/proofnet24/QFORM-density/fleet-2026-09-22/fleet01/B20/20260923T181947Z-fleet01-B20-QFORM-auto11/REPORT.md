SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B20, 2026-09-23T18:19:47Z.
attacking: fleet02/B20's first unpaid rank-at-most-five finite-core carrier branch; first spend any literal H-to-H^c third singular value with the marginal-free physical E3 theorem, then force a strong carrier mode into either a quantitative original-coordinate rank-one/rank-two cross packet or two diffuse original-coordinate source banks.

# fleet01/B20 — finite-core cross-E3 exit and strong-mode escape compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T181947Z-fleet01-B20-QFORM-auto11`  
Role: Proof closure and keeper / SYNTHESIS  
Status: **ESSENTIAL_STEP_APPLIED / FINITE-CORE SURVIVOR SHARPENED / FULL QFORM OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**  
Continuity: continuous on the paid E3 branch below; full-target continuity remains OPEN.

## 1. Scope and protected corrections

The target is unchanged: arbitrary dimension, independent ORIGINAL real coordinates with probability densities bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one. No iid, moment, compact-support, connected-support, Gaussian, log-concavity, diagonal-basis, or post-rotation-independence assumption is introduced.

The live corrections are retained: no law-uniform pointwise quadratic-phase decay, no dimension-free worst-fiber supremum, no arbitrary-joint coarea theorem, no independence after spectral rotation, no conditional-density supremum shortcut, no deletion of a nonzero random quadratic tail, and no conversion of aggregate determinant volume into one uniformly good physical minor.

The active continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` is acknowledged. The full unrestricted conjecture remains OPEN.

## 2. Completed fleet02/B20 result actually consumed

The freshest completed designated partner package is

`yspennstate/math-open-problems@391bc53a0249051fde8383684519350051ae4384`

with underlying report commit

`cbbf02361424fcf02504cf6f7f786aef1760bc8a`,

run `20260923T172757Z-fleet02-B20-QFORM-auto11`.

Its first unpaid in-plane branch inherits the fleet03/B20 r35 carrier

`S0 = U Lambda U^T`, `U^T U = I_r`, `r<=5`,                      (2.1)

with

`s_3(S0)>1597/2000`,
`||A-S0||_op<403/2000`.                                             (2.2)

The source r35 heavy set is

`H={i: ||U(i,:)||_2^2>1/25}`,                                     (2.3)

so `|H|<=124`, every `i in L:=H^c` satisfies

`||U(i,:)||_2^2<=1/25`,                                            (2.4)

and in the surviving heavy branch a carrier direction has mass `>1/20` on `H`.

Fleet02/B20 then proves the fixed-dimensional exit: if the physical principal block `A[H,H]` has three absolute eigenvalues at least `1/64`, the full ambient density is bounded by `<25435439`. Therefore every unpaid finite-core state satisfies

`boxed: s_3(A[H,H])<1/64`,                                         (2.5)

where for the symmetric principal block `s_3` is its third singular value / third absolute eigenvalue. This is the partner statement used below at an actual inequality.

## 3. First new closure: spend the literal H-to-L third singular value

Let

`C=A[H,L]`, `L=H^c`.                                                (3.1)

The completed marginal-free physical E3 theorem from fleet03/B20 r34 states that for any literal ORIGINAL-coordinate cross block `M`,

`Z_3=e_3(MM^T)>0`

implies the full ambient quadratic law has a continuous `C_0` density with

`||p_Q||_infinity <= K_3 Z_3^(-1/6)`,
`K_3=3*2^(4/3)*e^(1/3)=10.5501688311...`.                          (3.2)

### Theorem 3.1 — `QFORM-R5-124CORE-CROSS-E3-EXIT-v1`

Under (2.1)-(2.5), if

`s_3(C)>=1/64`,                                                     (3.3)

then

`boxed: ||p_Q||_infinity <=64 K_3 <675.211`,                        (3.4)

and the density is continuous and vanishes at infinity.

### Proof

Since the singular values decrease,

`e_3(CC^T)>=s_1(C)^2 s_2(C)^2 s_3(C)^2>=s_3(C)^6>=64^(-6)`.         (3.5)

Insert (3.5) into (3.2). This is a literal physical cross block; same-bank curvature, all outside coordinates, affine terms produced inside the receiver, signs, and every extra spectral direction are retained. QED.

Hence every still-unpaid fleet02/B20 finite-core state may additionally be assumed to satisfy

`boxed: s_3(A[H,L])<1/64`.                                         (3.6)

This is already a strict sharpening of the partner's first unpaid implication: both the finite principal core and its entire physical cross coupling are now rank-at-most-two in the `1/64` operator-collar sense.

## 4. Pull the low physical-core third singular value back to carrier space

Set

`G=U_H^T U_H`,                                                     (4.1)

so `0<=G<=I_r`. Take the polar factorization

`U_H=Q G^(1/2)`,                                                    (4.2)

where `Q` is a partial isometry. Then

`S0[H,H]=Q T Q^T`,
`T:=G^(1/2) Lambda G^(1/2)`.                                       (4.3)

By (2.2), coordinate restriction, Weyl, and the consumed partner inequality (2.5),

`s_3(S0[H,H])
 <=s_3(A[H,H])+||S0[H,H]-A[H,H]||_op
 <1/64+403/2000
 =1737/8000`.                                                       (4.4)

The nonzero singular values of (4.3) are those of `T`, with zeros padded when `G` is singular. Thus

`boxed: s_3(T)<eta:=1737/8000`.                                    (4.5)

Let `E` be the three-dimensional spectral subspace of `Lambda` corresponding to its three largest singular values. From (2.2),

`||Lambda w||>s ||w||` for every nonzero `w in E`,
`s:=1597/2000`.                                                     (4.6)

Let `K` be the span of all right singular/eigenvectors of the symmetric `T` except its two largest-in-modulus directions. Then

`dim K>=r-2`, and `||Tw||<eta||w||` for `w in K`.                   (4.7)

Since `dim E=3` and `r<=5`,

`dim(E intersect K)>=(3)+(r-2)-r=1`.                               (4.8)

Therefore there exists a unit vector

`boxed: w in E, ||w||=1, ||Tw||<eta`.                              (4.9)

This is a genuine strong carrier mode forced into the low-action sector of the physical finite core. No random variable is rotated; `w` is deterministic coefficient geometry only.

## 5. Strong-mode escape to the physical H-L cross block

Define its physical core mass

`a:=w^T G w=||U_H w||_2^2`.                                       (5.1)

We now obtain an exact quantitative dichotomy.

First note that, because `0<=G<=I`, functional calculus gives `G^(1/2)>=G`. Since `w in E`,

`||P_E G^(1/2)w||
 >=|<w,G^(1/2)w>|
 >=<w,Gw>=a`.                                                       (5.2)

Consequently (4.6) gives

`||Lambda G^(1/2)w||>=s a`.                                       (5.3)

The global vector `U Lambda G^(1/2)w` splits orthogonally between the physical coordinate sets `H` and `L`. Its `H` component is

`U_H Lambda G^(1/2)w=QTw`,                                        (5.4)

whose norm is `<eta` by (4.9). Hence its `L` component satisfies

`||U_L Lambda G^(1/2)w||^2
 >s^2 a^2-eta^2`.                                                   (5.5)

But for the physical test vector `Qw` on `H`,

`S0[L,H]Qw=U_L Lambda G^(1/2)w`.                                   (5.6)

Since `||Qw||<=1`, (5.5) implies whenever the right side is positive,

`||S0[L,H]||_op>sqrt(s^2 a^2-eta^2)`.                             (5.7)

Finally, restriction of the residual in (2.2) gives

`||A[L,H]-S0[L,H]||_op<epsilon:=403/2000`.                         (5.8)

### Theorem 5.1 — `QFORM-R5-STRONGMODE-CROSS-OR-OUTSIDE-v1`

For the `w` in (4.9), at least one of the following holds.

**(X) Strong physical cross arm:** `a>=1/2`, and

`||A[H,L]||_op
 >sqrt((1597/4000)^2-(1737/8000)^2)-403/2000
 =(sqrt(7184467)-1612)/8000
 >2/15.`                                                           (5.9)

**(O) Strong carrier mode mostly outside the finite core:**

`a<1/2`, so

`||U_L w||_2^2=1-a>1/2`.                                           (5.10)

The final rational comparison in (5.9) is exact: it is equivalent to

`9*7184467-8036^2=82907>0`.                                        (5.11)

Thus an unpaid low-physical-spectrum core cannot hide every strong carrier mode without either generating a fixed physical H-L cross arm or placing a strong-mode carrier vector mostly on the light complement.

## 6. Convert both alternatives into original-coordinate packets

We now combine Theorem 5.1 with the already-paid E3 exit (3.6).

### 6.1 Cross-arm alternative becomes a quantitative R1/R2 packet

Assume (X). Since every unpaid state satisfies `s_3(C)<1/64` and (5.9) gives `s_1(C)>2/15`, exactly one of the following occurs:

- if `s_2(C)>=1/64`, then

  `boxed: s_1(C)s_2(C)>1/480`;                                     (6.1)

- if `s_2(C)<1/64`, then by Eckart-Young

  `boxed: dist_op(C,{rank<=1})<1/64,  s_1(C)>2/15`.                 (6.2)

Thus alternative (X) is no longer a vague carrier-localization state: it is a literal ORIGINAL-coordinate strong rank-two packet or a strong rank-one tube, with the full nonzero tail retained.

### 6.2 Outside alternative supplies two diffuse physical source banks

Assume (O). For each `i in L`, put

`q_i:=|<U(i,:),w>|^2`.                                              (6.3)

By the source definition of the heavy set (2.3)-(2.4),

`q_i<=||U(i,:)||^2<=1/25`,                                        (6.4)

while (5.10) gives

`sum_(i in L) q_i>1/2`.                                             (6.5)

Partition the finitely many weights `q_i` greedily between two bins, always putting the next weight in the currently lighter bin. The final bin-mass difference is at most the largest atom, hence at most `1/25`. Therefore there is a literal ORIGINAL-coordinate partition

`L=L_1 disjoint_union L_2`                                         (6.6)

such that for `q=1,2`,

`sum_(i in L_q)|<U(i,:),w>|^2
 >=(sum_(i in L)q_i-1/25)/2
 > (1/2-1/25)/2
 =23/100`.                                                         (6.7)

Equivalently,

`boxed: ||U_{L_1}w||_2^2>23/100,  ||U_{L_2}w||_2^2>23/100`.         (6.8)

At the same time `w` remains a unit vector in the strong three-dimensional spectral subspace and satisfies the near-core-kernel relation `||G^(1/2)Lambda G^(1/2)w||<1737/8000` from (4.9).

This is an original-coordinate two-source-bank packet. It does **not** assert that `w` is itself an eigenvector of `Lambda`, and it does not treat `U_{L_q}^T X_{L_q}` as independent coordinates after any rotation. The next receiver must use only the independence of the disjoint physical banks `L_1,L_2,H`.

## 7. New compiler and first remaining implication

Combining Sections 3-6 proves the supporting compiler

`QFORM-R5-124CORE-CROSS/R1R2-OR-DIFFUSESTRONGMODE-COMPILER-v1`:

under the fleet02/B20 finite-core carrier hypotheses, one of the following holds:

1. the full ambient law has a continuous density with `||p_Q||_infinity<675.211` by a literal H-L E3 payment;
2. `A[H,L]` is a strong physical rank-two packet with `s_1s_2>1/480` and `s_3<1/64`;
3. `A[H,L]` is a strong physical rank-one tube with `s_1>2/15` and `s_2<1/64`;
4. there exists a unit strong-subspace carrier vector `w` with the near-core-kernel relation (4.9) and two disjoint original-coordinate light banks each carrying more than `23/100` of its carrier mass.

Every alternative retains arbitrary same-bank curvature, the full residual `A-S0`, all outside couplings, every nonzero spectral tail, and arbitrary signs.

The first remaining implication is therefore sharpened to

`QFORM-R5-R1/R2-CROSS-OR-TWOSOURCE-STRONGMODE-PAYMENT-v1`:

> pay alternatives 2-4 above by a full-law grouped/half-Riesz/projected-crossing receiver without declaring the carrier coordinates independent and without deleting the `1/64` cross tail or the operator residual.

This is strictly narrower than the partner's previous `QFORM-R5-124CORE-LOWPHYSICALS3-CARRIER-CAPTURE-PAYMENT-v1`.

## 8. Keeper reconciliation

Fresh native inventory shows exactly the same twenty fleet01 QFORM tasks B01-B20, each present once, enabled, hourly, with notifications disabled and email disabled. No duplicate, B21/B22, cadence defect, deliberate pause, or identity defect was present, so no scheduler mutation was made. Native task assignment is recorded separately from actual login evidence; missing login is not an outage. The current-hour fleet01 keeper lease is held by this B20 run.

## 9. Status

The unrestricted theorem is still **OPEN**; no valid counterexample is produced here. Continuity is proved only on the E3-paid branch, and remains OPEN for the full target. The new result is a source-preserving structural reduction plus one continuous-density payment, not a full solution.
