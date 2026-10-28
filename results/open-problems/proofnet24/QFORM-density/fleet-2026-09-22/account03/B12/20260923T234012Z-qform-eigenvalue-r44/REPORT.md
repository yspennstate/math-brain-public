SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B12, 2026-09-23T23:40:12Z.
attacking: multi-packet spectral-tail stability and a fixed-original-core density compiler under arbitrary signed additions; apply account04/B12 hybrid square-defect reserve at a stronger global spectral inequality.

# account03/B12 r44 — multi-packet spectral budgets and continuous physical-core stability

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260923T234012Z-qform-eigenvalue-r44`  
Status: **PROVED SUPPORTING STABILITY THEOREMS / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Continuity: **proved for the fixed-physical-core density corollary below; full target continuity remains open together with the full universal height theorem.**

## 1. Scope, controls and source boundary

The target is unchanged: for every dimension, every product law of independent original coordinates with scalar probability densities bounded by one, and every real symmetric coefficient matrix with at least three eigenvalues of modulus at least one, prove a dimension-free universal density bound, or give a valid counterexample.


The same UTC-hour canonical login path already belonged to this slot's earlier real run `20260923T231212Z-qform-eigenvalue-r43`; it was preserved rather than overwritten, exactly as the current continuation requires. This r44 run has its own unique immutable run/start/finish records.

The one-packet Schur estimate proved in r43 is **not** re-claimed as new. The new contributions are:

1. an additive **multi-packet** spectral budget, with an optimized allocation among unrelated signed packets;
2. the same budget at the level of a physical column-square carrier;
3. an explicit **fixed-original-core density theorem** with bound `2 sqrt(6 pi m)/sigma`, valid in arbitrary ambient dimension and stable under arbitrary leading signed eigenmodes plus full-rank tails;
4. a stronger equation-level use of the completed account04/B12 hybrid square-defect theorem, which reveals an eleven-mode global reserve and survives eight further completely unbounded signed modes.

No random coordinate is rotated. No term `X^T E X` is declared independent of the old quadratic form. Small operator tails enter only deterministic singular-value inequalities.

Source-valid analytic receivers used below:

- finite physical-core projected-gradient theorem: `yspennstate/math-open-problems@51d2edb29d7a4c150e4d47ed3a6685875a8483ae`, `proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/REPORT.md`; for an `m`-coordinate quadratic-plus-affine form whose actual coefficient matrix has three singular values at least `sigma`, the density is at most `2 sqrt(6 pi m)/sigma`;
- fixed-matrix `C_0` regularity: recorded from the independently completed account02/B15 result `yspennstate/math-open-problems@9b8bb7e84811978a2c46c7bb5ec50f2570dbc056`, `proofnet24/QFORM-density/fleet-2026-09-22/account02/B15/20260922T200544Z-account02-B15-qform-r11/REPORT.md`; rank at least three gives an instance-dependent continuous density vanishing at infinity;
- designated partner account04/B12: `yspennstate/math-open-problems@3df1475f988c811570dc5c249a7756d24adb51bf`, `proofnet24/QFORM-density/fleet-2026-09-22/account04/B12/20260923T191531Z-account04-B12-hybrid-square-defect-r7/REPORT.md`.

## 2. Multi-packet singular-budget theorem

Let `A_0=A_0^T` be any real symmetric `n x n` baseline matrix. Let

`E_1,...,E_M`

be arbitrary real symmetric added matrices. They need not commute with `A_0`, with one another, or have any sign relation. Put

`A=A_0+sum_{ell=1}^M E_ell`.

Choose arbitrary integers `q_ell>=0`. Define

`Q=sum_ell q_ell`,

and

`delta_ell=s_{q_ell+1}(E_ell)`,
`Delta=sum_ell delta_ell`,

with the convention `s_{q+1}(E)=0` when `rank(E)<=q`.

Each `E_ell` has a signed spectral truncation

`E_ell=R_ell+T_ell`,

where `rank(R_ell)<=q_ell` and `||T_ell||op=delta_ell`. Hence

`R=sum R_ell`, `T=sum T_ell`

satisfy

`rank(R)<=Q`, `||T||op<=Delta`,

while `A=A_0+R+T`.

### Theorem 2.1 — `QFORM-MULTIPACKET-SPECTRAL-BUDGET-v1`

Let `I` be any set of `r` ORIGINAL coordinates such that the **final** principal pivot

`B=A[I,I]`

is invertible. Let `J=I^c` and let

`S=A[J,J]-A[J,I] B^{-1} A[I,J]`

be the exact final Schur complement. Then for every `k>=1` with

`k+r+Q<=n`, one has

`boxed: s_k(S) >= (s_{k+r+Q}(A_0)-Delta)_+ .`                    (2.1)

In particular, the first `q_ell` eigenmodes of every packet may have arbitrary magnitude, arbitrary sign and arbitrary orientation. The remaining eigenvalues of every packet may be full-rank and mixed-sign; they enter only through the additive tail budget `Delta`.

#### Proof

Since `rank(R)<=Q`, the singular-value rank-perturbation inequality gives

`s_j(A_0+R)>=s_{j+Q}(A_0)`                                      (2.2)

for all admissible `j`. One direct derivation applies

`s_{u+v-1}(X+Y)<=s_u(X)+s_v(Y)`

to `A_0=(A_0+R)-R` with `v=Q+1` and `s_{Q+1}(R)=0`.

The reverse Weyl inequality then gives

`s_j(A)>=s_j(A_0+R)-||T||op
       >=s_{j+Q}(A_0)-Delta`.                                  (2.3)

For the final physical pivot,

`A-diag(0_I,S)
 = [[B,A[I,J]],
    [A[J,I],A[J,I]B^{-1}A[I,J]]]`

factors as

`[I_r; A[J,I]B^{-1}] B [I_r, B^{-1}A[I,J]]`,                   (2.4)

so this difference has rank at most `r`. Therefore

`s_k(S)=s_k(diag(0_I,S))>=s_{k+r}(A).`                          (2.5)

Insert `j=k+r` in (2.3). This proves (2.1). QED.

### Optimized budget form

Because the integers `q_ell` are free choices, one may maximize the certified scale:

`boxed:
 s_k(S) >=
 max_{q_1,...,q_M>=0, k+r+sum q_ell<=n}
 [s_{k+r+sum q_ell}(A_0)-sum_ell s_{q_ell+1}(E_ell)]_+ .`       (2.6)

This is a discrete infimal-budget/knapsack profile: spending one additional reserve mode on packet `ell` replaces its charged tail `s_{q_ell+1}` by the next singular value, at the cost of moving one place deeper into the baseline spectrum.

A useful threshold formulation is immediate. If `q_ell` is the number of eigenvalues of `E_ell` with absolute value strictly larger than `tau_ell`, then `delta_ell<=tau_ell` and

`boxed:
 s_k(S)>=
 [s_{k+r+sum q_ell}(A_0)-sum tau_ell]_+ .`                      (2.7)

Thus all eigenvalues above the chosen packet thresholds are free in magnitude and sign; every smaller eigenvalue is paid only through the sum of the thresholds, not through a random-error estimate.

## 3. Physical column-square form

The same argument works before any Schur completion on an actual original-coordinate carrier.

Let `H` be a set of `m` original coordinates and let `P_H:R^m -> R^n` be the coordinate embedding. Since

`(A^2)[H,H]=(AP_H)^T(AP_H)`,

one has

`s_j(AP_H)=sqrt(lambda_j((A^2)[H,H])).`

Also `rank(RP_H)<=Q` and `||TP_H||op<=Delta`. Therefore:

### Theorem 3.1 — `QFORM-MULTIPACKET-COLUMN-SQUARE-STABILITY-v1`

For `k+Q<=m`,

`boxed:
 sqrt(lambda_k((A^2)[H,H]))
 >= [sqrt(lambda_{k+Q}((A_0^2)[H,H]))-Delta]_+ .`               (3.1)

This is useful when a density compiler is phrased in terms of physical square energy rather than a principal-block spectrum. Again, no probability enters the proof.

## 4. Fixed-original-core density stability

A particularly clean consequence directly answers the assignment at the level of the **law of the full ambient quadratic form**.

Fix an ORIGINAL-coordinate set `H` of size `m>=3`. Let

`B_0=A_0[H,H]`, `B=A[H,H]`.

With the same `q_ell,Q,Delta` as above and `Q<=m-3`, define

`sigma_H=[s_{3+Q}(B_0)-Delta]_+`.                                (4.1)

### Theorem 4.1 — `QFORM-MULTIPACKET-PHYSICAL-CORE-DENSITY-STABILITY-v1`

If `sigma_H>0`, then for every product law of independent original coordinates with scalar densities at most one, and for arbitrary ambient blocks/couplings and arbitrary affine terms,

`boxed:
 ||p_Q||_(infinity,ess)
 <= 2 sqrt(6 pi m)/sigma_H .`                                   (4.2)

Moreover the full output law has a representative in `C_0(R)`, and that continuous representative obeys the same pointwise bound.

#### Proof

Compress each spectral truncation to `H`. The rank of `R_ell[H,H]` is at most `q_ell`, while

`||T_ell[H,H]||op<=delta_ell`.

Applying the same rank-plus-Weyl argument to the `m x m` matrix gives

`s_3(B)>=s_{3+Q}(B_0)-Delta=sigma_H`.                            (4.3)

Condition on every ORIGINAL coordinate outside `H`. The variables `X_H` remain independent and each retains its original density cap one. The conditional quadratic coefficient is exactly the **final** block `B`; all outside couplings produce only a deterministic affine term in `X_H`. The completed projected-gradient finite-core theorem therefore gives the conditional interval-density bound

`2 sqrt(6 pi m)/sigma_H`,                                       (4.4)

uniformly in the conditioned outside value. Averaging proves (4.2).

Since `B` has rank at least three, the full coefficient matrix `A` has rank at least three. The completed fixed-matrix regularity theorem supplies an instance-dependent `C_0` density representative for the full law. A continuous function whose essential supremum is at most the right-hand side of (4.2) cannot exceed that value at a point, because then it would exceed it on an interval. Hence the same bound holds pointwise for the continuous representative. QED.

### Optimized physical-core form

Define

`sigma_H^*=
 max_{q_1,...,q_M>=0, sum q_ell<=m-3}
 [s_{3+sum q_ell}(B_0)-sum_ell s_{q_ell+1}(E_ell)]_+ .`         (4.5)

Whenever `sigma_H^*>0`,

`boxed:
 ||p_Q||_infinity <=2 sqrt(6 pi m)/sigma_H^* ,`                 (4.6)

with a continuous `C_0` representative. This makes the tradeoff between many very large added modes and their residual tails explicit and algorithmic.

## 5. Sharpness of the spectral reserve arithmetic

The mode loss `Q` and coefficient one in front of `Delta` in Theorem 2.1 are simultaneously sharp without extra structure.

Take `n=Q+r+k`. Let the diagonal baseline `A_0` have its first `Q+r` diagonal entries much larger than a fixed `a>0`, followed by `k` entries equal to `a`. Partition the first `Q` coordinates into groups of sizes `q_ell`. For packet `ell`, let its leading rank-`q_ell` part cancel exactly its assigned large diagonal entries, and add a tail

`-delta_ell I`

on the final `k` coordinates, with all cancelling magnitudes much larger than every `delta_ell`. Then

`s_{q_ell+1}(E_ell)=delta_ell`.

Choose the next `r` untouched large coordinates as the physical pivot. The final Schur complement on the last `k` coordinates is exactly

`S=(a-sum delta_ell)I_k`,

while

`s_{Q+r+k}(A_0)=a`.

Therefore equality holds in (2.1):

`s_k(S)=a-Delta`.

So one cannot in general replace `Q=sum q_ell` by a smaller reserve loss or replace `Delta=sum delta_ell` by `c Delta` with a universal `c<1`.

For the density-core compiler, retaining three final core modes is also structurally necessary for this mechanism: if arbitrary packet modes are allowed to consume all but two core modes, the remaining opposite-sign two-dimensional quadratic can have a logarithmically unbounded density. This is only a sharpness control on the local compiler, not a counterexample to the full three-large-eigenvalue conjecture.

## 6. Required account04/B12 application — eleven global reserve modes

Now apply the completed partner theorem at a new equation, stronger than the six-mode consequence used in r43.

The account04/B12 r7 family starts from `n=16` and `A_0^2=4I_16`, permits:

- at most two severe commuting square losses (`d_3=0`), while all other commuting eigenvalue replacements may reverse sign or become arbitrarily large;
- an arbitrary noncommuting packet with destructive-square tail `nu_3=0`;
- an arbitrary-magnitude rank-one packet;
- a dense symmetric tail of operator norm at most `1/4`.

Call its final matrix `A_p`. The partner's Theorem 2.1 is valid for every physical set `H`. Take **the full set of all sixteen original coordinates** and choose in the partner inequality

`k=11, r=1, q=2, p=2`.

Because `k+r+q+p=16`, `d_3=nu_3=0`, and the baseline square is `4I_16`, the partner theorem gives

`boxed:
 s_11(A_p)=sqrt(lambda_11(A_p^2))
 >= sqrt(lambda_16(4I_16))-1/4
 =7/4 .`                                                        (6.1)

This eleven-mode conclusion is not the six-mode principal-compression specialization used in the partner report or in r43; it is a direct new spending of the partner's proved general inequality.

Now place this sixteen-coordinate block on any set `H` of original coordinates inside an arbitrarily large ambient system. All baseline blocks and couplings outside `H` may be arbitrary. Add **any finite number** of further symmetric matrices

`F_1,...,F_M`

on the full ambient space. Choose integers `q_ell` such that

`sum q_ell<=8`,                                                  (6.2)

and assume only the residual-tail budget

`sum s_{q_ell+1}(F_ell)<=1/4`.                                  (6.3)

The first `q_ell` signed eigenmodes of each `F_ell` are unrestricted in magnitude, sign, support and orientation. The remainder of every packet may be full rank and mixed-sign.

Apply Theorem 4.1 to the sixteen-coordinate core, using (6.1). Since `3+sum q_ell<=11`,

`s_3(A[H,H])
 >=s_{3+sum q_ell}(A_p)-1/4
 >=7/4-1/4
 =3/2.`                                                         (6.4)

Hence the **full ambient quadratic form**, after all the new signed packets and with all outside interactions still present, has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= 2 sqrt(6 pi *16)/(3/2)
 = (8/3)sqrt(96 pi)
 =23.155240145864564... .`                                      (6.5)

A concrete two-packet instance is

`q_1=q_2=4`,
`s_5(F_1)<=1/8`, `s_5(F_2)<=1/8`.

Thus each packet may contain four completely uncontrolled huge signed eigenvalues, while all remaining eigenvalues in both packets can be arbitrary mixed-sign full-rank tails at the stated spectral scale. Eight new unbounded modes in total are absorbed and the output density still satisfies (6.5). No convolution or post-rotation independence is invoked.

For comparison, if only `sum q_ell<=2` with the same total tail `<=1/4`, Theorem 3.1 preserves four of the partner's six local square-energy modes on every eleven-coordinate carrier at scale `3/2`. Feeding that actual final carrier into the previously proved four-mode compiler (r40) gives another fully explicit essential-density bound; with the simple admissible parameters `m=11`, `g=s=3/2`, `c=29/20`, `b=1/8`, `a=1/500`, that bound is `<19291`. The sixteen-coordinate core estimate (6.5) is much sharper for this explicit family.

## 7. Finite deterministic consistency checks

The analytic proof above does not depend on computation. A seeded checker was nevertheless run on random symmetric packets with deliberately huge random low-rank signed components.

- Multi-packet Schur theorem: 10,000 generated trials, 8,996 admissible index configurations, **0 violations**. Minimum numerical margin `0.01551755259354376`; median margin `11.921349974122489`.
- Fixed-core singular theorem: 10,000 generated trials, 6,359 admissible reserve allocations, **0 violations**. Minimum numerical margin `0.27137368353966024`; median margin `6.435903300407748`.

The checker tests only the deterministic matrix inequalities; it does not simulate output-density histograms and is not evidence for the unrestricted conjecture.

## 8. What remains open

**Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.**

This run solves a broad stability problem **once there is a bounded physical core with enough reserve spectrum**, and it allows arbitrary large added signed eigenmodes plus dependent full-rank tails. The still-unpaid target-level implication is structural:

> Starting from only `s_3(A)>=1`, force a bounded original-coordinate core with enough reserve after an optimal spectral-budget allocation, or route the failure into one of the already proved hub, grouped-crossing, ridge, common-plane or diffuse-bank receivers.

The theorem does not assert that the bare three-eigenvalue hypothesis produces a core with `s_{3+Q}` bounded below. Large delocalized forms may have no such small principal core. That is exactly where the fleet's bank/hub/ridge mechanisms remain necessary.

The new result also does not make a small coefficient tail into a small random quadratic variable; only deterministic singular values are perturbed. All signs, affine terms from conditioning, fragmented/unbounded input supports and arbitrary outside couplings are retained.
