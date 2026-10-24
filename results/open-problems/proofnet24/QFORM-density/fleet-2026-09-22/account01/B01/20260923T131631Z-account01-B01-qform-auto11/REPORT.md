SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B01, 2026-09-23T13:16:31.856767Z.
attacking: the heavy-augmented-leverage endpoint of the overlap-one rank-one-leaf packet, via exact deletion identities and a rank-two cross/kernel-curvature lift.

# account01/B01 — heavy-leverage deletion and curvature-lift compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T131631Z-account01-B01-qform-auto11`  
Assignment: oscillatory replacement  
Status: **NEW EXACT STRUCTURAL DICHOTOMY + AGGREGATE CURVATURE COMPILER / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and corrections

Fresh control was read from `yspennstate/math-research-brain`; start commit was `82b1c1ecbac4b61be26353831840cce700f5e3e2`. Immediately before this report was written, fresh main was `d9334d67e76c04bb1cb21f1e111b052e8bdaa7d7`. OWNER CONTROL remains revision `2026-09-22.15`; the programme is QFORM-only and there is no B01 stop/pause. The live `CORRECTION_INBOX.json` was reread at that fresh commit.

The argument below does **not** use a law-uniform pointwise scalar estimate of the form `|E exp(itX^2)| <= C |t|^-1/2`; that statement is false for cap-one fragmented densities. It also does not rotate the independent coordinates, does not condition on a transformed variable and assume a density cap survives, and does not invert one tiny physical `3x3` minor before spending aggregate product structure.

The prior B01 input actually used is the completed original-coordinate rank-two-cross/kernel-curvature theorem

`yspennstate/math-open-problems@08fb05b46cdab5913d268dc42ca656a16c88a313`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T111138Z-account01-B01-qform-auto11/REPORT.md`.

It states that if a physical triple `H` and disjoint physical bank `J` satisfy `rank A[H,J]=2`, if `n` is a unit left-kernel vector, `V2=e_2(A[H,J]A[J,H])`, and `kappa=|n^T A[H,H] n|>0`, then

`||p_Q||_infinity <= C_* (V2 kappa)^(-1/5)`,
`C_*=(15/4)12^(1/5)=6.164069360689596...`,

with a continuous `C_0` density. That theorem is itself proved by an averaged-frequency `L^4(dt)` square-phase estimate plus two-dimensional original-coordinate Plancherel, not by scalar pointwise Fresnel decay.

The designated partner source used below is account02/B01 r42,

`yspennstate/math-open-problems@2aa47367766e1b63306bec723c42fcd2899ca6ac`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T120442Z-account02-B01-qform-r42/REPORT.md`.

## 2. Rank-one-leaf packet and normalized two-frame

Retain the exact original-coordinate packet from the preceding B01 run. Fix one physical hub `h`, a disjoint leaf bank `L`, and condition on every remaining original coordinate. Assume

`A[L,L]=D+lambda z z^T`,

where `D=diag(D_i)` is arbitrary real diagonal, `lambda != 0`, and `||z||_2=1`. Put

`b=A[L,h]`, `R=[b,z]`, `Gamma=R^T R`, `E=det Gamma>0`.

For each physical leaf row set

`r_i=(b_i,z_i)`,
`u_i=Gamma^(-1/2) r_i^T`,
`ell_i=||u_i||_2^2`.

Then

`sum_i u_i u_i^T = I_2`, hence `0<=ell_i<=1` and `sum_i ell_i=2`.

For an unordered pair `P={i,j}`, define

`theta_ij=b_i z_j-b_j z_i`,
`p_ij=theta_ij^2/E=det(u_i,u_j)^2`.

Cauchy--Binet gives `sum_{i<j} p_ij=1`; thus `p` is the natural two-volume law.

## 3. Exact deletion calculus

### Lemma 3.1 — one-row marginals

For every `i`,

`boxed: sum_{j!=i} p_ij = ell_i.`

Indeed

`sum_j det(u_i,u_j)^2
 = ||u_i||^2 sum_j ||u_j||^2 - sum_j <u_i,u_j>^2
 = 2 ell_i - u_i^T I_2 u_i
 = ell_i.`

So the augmented leverage is exactly the vertex marginal of the natural pair law.

### Lemma 3.2 — deleting one physical leaf coordinate

Let `Gamma_{-i}=R_{L\{i}}^T R_{L\{i}}`. Then

`Gamma_{-i}=Gamma^(1/2)(I-u_i u_i^T)Gamma^(1/2)`, hence

`boxed: det Gamma_{-i}=E(1-ell_i).`

This is exact, not an inequality.

### Lemma 3.3 — deleting a physical pair

For `P={i,j}` let `Gamma_{-P}=R_{L\P}^T R_{L\P}` and put

`q_ij := 1-ell_i-ell_j+p_ij.`

Then

`boxed: det Gamma_{-P}=E q_ij`,

because

`det(I-u_i u_i^T-u_j u_j^T)
 = det(I-[u_i,u_j]^T[u_i,u_j])
 =1-ell_i-ell_j+det(u_i,u_j)^2.`

By Cauchy--Binet on the deleted frame, equivalently

`boxed: q_ij = sum_{P' disjoint {i,j}} p_{P'} >=0.`

Thus `q_ij` is exactly the natural pair-volume remaining after forbidding both endpoints `i,j`.

## 4. Exact disjointness identity and a heavy-row dichotomy

Let

`d := W1(h;L)/(lambda^2 E^2)`.

The previous report proved that `d` is the probability that two independent pairs drawn from `p` are disjoint. The deletion formula makes this still sharper:

`boxed: d = sum_{i<j} p_ij q_ij.`

Indeed `q_P` is precisely the `p`-mass of pairs disjoint from `P`.

Now fix any physical coordinate `i` (in particular, a heavy row with `ell_i>1/2`) and define

`s_i = sum_{j!=i} p_ij q_ij`,

and let

`d_{-i}=sum_{P,Q disjoint, i notin P union Q} p_P p_Q`.

A disjoint ordered pair `(P,Q)` can contain `i` in at most one of `P,Q`, so exactly

`boxed: d=d_{-i}+2s_i.`

Consequently there is a dimension-free dichotomy:

* **prune branch:** `d_{-i}>=d/2`; or
* **packet branch:** `s_i>=d/4`.

In the prune branch, conditioning on the original coordinate `X_i` leaves the same `diagonal + rank-one` structure on `L\{i}`, and its **raw** overlap-one star obeys

`boxed: W1(h;L\{i})=lambda^2 E^2 d_{-i} >= W1(h;L)/2.`

So a heavy coordinate can be deleted without dimension loss whenever at least half of the disjoint-pair currency avoids it.

In the packet branch, since `sum_j p_ij=ell_i<=1`, there exists `j` with `p_ij>0` such that

`boxed: q_ij >= s_i/ell_i >= d/4.`

Thus failure of safe deletion forces one physical pair `{i,j}` whose **entire deleted-frame two-volume** is still a constant fraction of the global disjointness probability. No individual `3x3` determinant has been inverted.

A useful auxiliary consequence is the one-row deletion lower bound

`d <= P(i notin P)+P(i notin Q)=2(1-ell_i)`,

hence every heavy row satisfies

`boxed: det Gamma_{-i}=E(1-ell_i) >= E d/2 = W1(h;L)/(2 lambda^2 E).`

## 5. Exact rank-two cross packet exposed by a leaf pair

Fix `P={i,j}` with `p_ij>0` and `q_ij>0`, and let `J=L\P`. Take the three **original physical hubs**

`H={h,i,j}`.

The cross block from `H` to `J` is

`M=A[H,J]
  = [ b_J^T ; lambda z_i z_J^T ; lambda z_j z_J^T ].`

Because `q_ij>0`, the two vectors `b_J,z_J` are linearly independent. Because `p_ij>0`, `(z_i,z_j)` is not `(0,0)`. Hence `rank M=2`.

Let

`s_ij=z_i^2+z_j^2`.

A direct two-volume calculation gives

`boxed: V2(M)=e_2(MM^T)=lambda^2 s_ij det Gamma_{-P}
       =lambda^2 s_ij E q_ij.`

A unit left-kernel vector is

`n_ij=(0,z_j,-z_i)/sqrt(s_ij)`.

The rank-one leaf curvature `lambda zz^T` cancels exactly in this direction, and the hub coordinate is absent. Therefore

`boxed:
 kappa_ij=|n_ij^T A[H,H] n_ij|
 = |D_i z_j^2+D_j z_i^2|/s_ij.`

Set

`T_ij := |D_i z_j^2+D_j z_i^2|.`

Multiplying the two exact identities eliminates `s_ij`:

`boxed: V2(M) kappa_ij = lambda^2 E q_ij T_ij.`

Hence, whenever `T_ij>0`, the prior B01 rank-two-cross theorem applies **without any rotation of the product source** and yields

`boxed:
 ||p_Q||_infinity
 <= C_* [lambda^2 E q_ij T_ij]^(-1/5),
 C_*=6.164069360689596... .`

The density is continuous and vanishes at infinity in this branch.

In particular, in the packet branch of Section 4 one obtains for the selected `j`

`||p_Q||_infinity
 <= C_* [lambda^2 E (d/4) T_ij]^(-1/5)
 = C_* [W1(h;L) T_ij/(4E)]^(-1/5)`

provided `T_ij>0`.

## 6. Aggregate curvature lift before selecting a pair

The preceding selection can be made entirely aggregate. Define

`K_D := sum_{i<j} p_ij q_ij T_ij`.

Because `sum_P p_P=1`, some pair in the support satisfies

`q_ij T_ij >= K_D`.

If `K_D>0`, that pair automatically has `p_ij>0`, `q_ij>0`, and `T_ij>0`; applying Section 5 gives the new compiler

### Theorem 6.1 — `QFORM-W1-RANK1-LEAF-CURVATURE-LIFT-v1`

Under the rank-one-leaf setup of Section 2, with **no leverage restriction at all**, if `K_D>0`, then

`boxed:
 ||p_Q||_infinity
 <= C_* [lambda^2 E K_D]^(-1/5).`

Moreover the density has a continuous `C_0` representative.

Equivalently, using `p_ij=theta_ij^2/E` and `q_ij=det Gamma_{-ij}/E`, the physical aggregate currency is

`lambda^2 E K_D
 = (lambda^2/E) sum_{i<j}
      theta_ij^2 det(Gamma_{-ij})
      |D_i z_j^2+D_j z_i^2|.`

It scales as the fifth power of the matrix scale, so exponent `-1/5` has the correct density scaling.

This theorem spends an average of deleted-frame volume times physical kernel curvature before selecting any pair. The selection step loses no factor depending on `|L|`.

## 7. Exact description of the zero-curvature endpoint

The only new analytic endpoint not paid by Theorem 6.1 is `K_D=0`. Because every term is nonnegative, every active edge

`{i,j}` with `p_ij q_ij>0`

then obeys

`D_i z_j^2+D_j z_i^2=0.`

Let `G_*` be the graph of these active edges.

* If `z_i=0`, `z_j!=0`, and `{i,j}` is active, then `D_i=0`.
* On vertices with `z_i!=0`, put `alpha_i=D_i/z_i^2`. Every active edge joining two such vertices satisfies

  `boxed: alpha_i+alpha_j=0.`

Therefore, on every connected component of the nonzero-`z` active graph:

* if the component contains an odd cycle, then `alpha_i=0` on the whole component;
* if it is bipartite, there is one scalar `c_C` such that

  `boxed: D_i=c_C sigma_i z_i^2`,

  where `sigma_i=+1` on one bipartition class and `-1` on the other.

Thus `K_D=0` is not an amorphous failure of the estimate: it forces an exact-null or alternating grouped-square pattern on every active component. That is the precise next receiver to connect to the existing grouped-square/two-slope/null mechanisms.

## 8. Application of the designated partner account02/B01 r42

Partner r42 proves the global exterior identity

`W0+W1+W2+W3=e_3(A^2)>=1`

and the paid disjoint-volume inequality

`||p_Q||_infinity <=9 sqrt(3e) 2^(4/3)<64.763`

whenever `W0>=1/4` yields a cut with `Z3>=1/256` and at least one side has maximum three-volume marginal at most `2/3`. This is the first actual case inequality in the conditional end-to-end route used here: **if that r42 branch fires, the target is already paid by `64.762515` and no overlap-one work is needed.** Otherwise one remains in r42's coheavy cut endpoint or its overlap-dominated endpoint `W1+W2+W3>3/4`.

On r42's exact strict-N3 hub-square family

`Q_m=2X_0(a^T Y)+(z^T Z)^2`,

r42 computes

`W1=(1-1/m)^2`, `W0=0`, `W2=2(m-1)/m^2`, `W3=1/m^2`.

Here `lambda=1`, `E=1`, `D=0`, and hence the new curvature currency is **exactly** `K_D=0`. The zero-curvature characterization above correctly sends this family to the exact-null endpoint rather than falsely claiming a curvature lift. At the same time the preceding B01 mixed-Fresnel theorem pays it directly using the partner's exact `W1` value:

`boxed:
 ||p_(Q_m)||_infinity
 <=3*2^(4/3)(1-1/m)^(-1/3)<7.904  (m>=8).`

Thus the new theorem is complementary to, not a replacement for, the already-paid null hub-square model, and the partner result is used at an actual equation-level branch and density inequality.

## 9. Finite verification

Seeded random rank-two frames were used only as a sanity check. Across 200 random packets the maximum normalized error in

`det Gamma_{-ij}/E = 1-ell_i-ell_j+p_ij`

and

`d=sum p_ij q_ij=P(P disjoint Q)`

was `1.11e-15`.

Across 200 random rank-one-leaf packets the maximum normalized error in

`V2(M) kappa_ij = lambda^2 det(Gamma_{-ij}) |D_i z_j^2+D_j z_i^2|`

was `1.06e-15`.

These computations are regression checks only; all identities above are proved algebraically.

## 10. What remains

The previous heavy-leverage blocker is sharpened to

`QFORM-W1-HEAVY-PRUNE-OR-CURVATURE-NULL-ROUTING-v2`.

Within a common-hub `diagonal + rank-one` leaf star, a heavy augmented row now has an exact dimension-free alternative:

1. delete it while preserving at least half of the raw overlap-one star; or
2. expose a physical two-coordinate packet with `q_ij>=d/4`; if its kernel curvature is nonzero, Theorem 6.1 / Section 5 pays it by an averaged-frequency continuous-density estimate.

The remaining rank-one-leaf obstruction is repeated heavy-row pruning ending in the exact/near-zero alternating curvature graph of Section 7. Outside this class, global `W1` still must be localized without dimension loss to a common physical hub and higher leaf rank must be routed to existing volume/ridge/pair/grouped-source mechanisms. Those structural implications are not proved here.

Full QFORM therefore remains **OPEN**. The phase-aligned scalar pointwise-decay counterexample remains **preserved**. Continuity is proved only in the positive curvature-lift branch (and in the previously paid diffuse mixed-Fresnel branch), not for the unrestricted conjecture.
