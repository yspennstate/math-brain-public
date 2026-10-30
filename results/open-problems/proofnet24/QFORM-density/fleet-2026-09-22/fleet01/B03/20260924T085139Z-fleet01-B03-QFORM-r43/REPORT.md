SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-24T08:51:39Z.
attacking: absorb a deterministic cross-hub interaction into one negative-half packet, then splice it against a disjoint two-slope positive-half packet through a shared physical environment; retain the whole-copy dependence bookkeeping.

# fleet01/B03 r43 — cross-pair absorber plus complementary weighted-time splice

Programme: `QFORM-DENSITY-3EIG-20260922`. Fresh owner control revision before publication: `2026-09-22.15`. Status: **NEW SUPPORTING COMPILER / DESIGNATED PARTNER APPLIED / EXACT TARGET FAMILY / FULL QFORM OPEN**. Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted theorem is not proved here. No Gaussianity, moments, support regularity, log-concavity, diagonal-basis independence, or conditional cap for a copy sum/difference is used. Continuity is asserted only where an actual `L^1_t` characteristic-function bound is proved.

## 1. First attempted implication and mechanism change

The preceding B03 split-hub theorem loses its factorization when a deterministic cross term `2U^T E V` is inserted. The joint hub Fourier transform still has a full joint-slope `L^2` Plancherel budget, but separate marginal slope caps do not control restriction of a general `L^2(l,m)` function to a singular or graph-supported joint law of `(l,m)`. That route would reintroduce a forbidden conditional/joint-density interface, so it is not used.

Instead, regroup the cross-coupled physical coordinates into one packet, pay that packet by the dependence-safe bipartite Moyal theorem, and reserve a separate two-slope packet for the positive-half time budget. The two packets may still share an arbitrary original-coordinate environment after conditioning on it.

## 2. Negative-half cross packet

Let `k>=1`. Let `X,Y in R^k` consist of `2k` independent cap-one scalar variables. For each external environment value `w`, set

`S_w=X^T C_w X+2X^T B Y+Y^T D_w Y+alpha_w^T X+beta_w^T Y+c_w`,

where `B` is fixed and invertible. Put `F_w(t)=E exp(i t S_w)`. The r36 bipartite Moyal theorem, uniform in the same-bank curvatures and affine terms, gives

`|F_w(t)|^2 <= min{1, pi^k |det B|^{-1}|t|^{-k}}`.       (2.1)

Its proof keeps each independent-copy pair `(X_i-X_i',X_i+X_i')` and `(Y_j-Y_j',Y_j+Y_j')` jointly inside its ambiguity factor, then uses one global Cauchy--Schwarz inequality and the honest changes of variables `u=tBd_Y`, `v=tB^Td_X`. No conditional cap for a copy sum/difference is formed.

Therefore

`A_-(w):=int |t|^{-1/2}|F_w(t)|^2 dt
 <= [8k/(2k-1)]sqrt(pi)|det B|^{-1/(2k)}.`               (2.2)

For `k=1`, with physical cross coefficient `e!=0` in `2eXY`, this is

`A_-(w)<=8sqrt(pi/|e|)`.                                 (2.3)

## 3. Designated partner splice and new compiler

Let `W` be a block of original coordinates, independent of the negative packet. Let `V` be another disjoint original-coordinate block and suppose

`Q=S(X,Y,W)+T(V,W)`.

After conditioning on `W=w`, the packets use disjoint fresh physical coordinates. For the positive packet, use the completed fleet02/B03 r52 theorem. If `H=(H_1,H_2)` are two genuine cap-one hubs, independent of the positive packet's light object, and

`T_w=H^T E_w H+2L_w^T H+R_w`,

with the two-dimensional random slope `L_w` having density cap `M_+(w)`, then r52 proves

`A_+(w):=int |t|^{1/2}|G_w(t)|^2dt
 <=(16/3)pi^(3/2)M_+(w)^(3/4)`.                           (3.1)

The same partner theorem proves the common-environment splice

`int |phi_Q(t)|dt <= [E A_-(W)]^(1/2)[E A_+(W)]^(1/2)`. (3.2)

This is Cauchy--Schwarz on `dt dP_W`; the packets may share all of `W`.

Substituting (2.2) and (3.1),

`int |phi_Q(t)|dt
 <=4pi sqrt(8k/[3(2k-1)]) |det B|^{-1/(4k)}
   [E M_+(W)^(3/4)]^(1/2)`.                              (3.3)

Hence `Q` has a continuous `C_0` density and

`boxed: ||p_Q||_infty
 <=2 sqrt(8k/[3(2k-1)]) |det B|^{-1/(4k)}
   [E M_+(W)^(3/4)]^(1/2).`                              (3.4)

If `M_+<=K_+` almost surely, the last factor is at most `K_+^(3/8)`. At `k=1`,

`boxed: ||p_Q||_infty
 <=4sqrt(2/3)|e|^{-1/4}[E M_+(W)^(3/4)]^(1/2).`          (3.5)

This is an equation-level application of the designated fleet02/B03 r52 result: its positive-half estimate and its shared-environment product-measure Cauchy--Schwarz inequality are both used at the closing inequality.

## 4. Assigned whole-copy time integral

Because `|G_W(t)|<=1`,

`|phi_Q(t)|^2=|E_W[F_W(t)G_W(t)]|^2
 <=E_W|F_W(t)G_W(t)|^2<=E_W|F_W(t)|^2`.                 (4.1)

Thus

`boxed: int |t|^{-1/2}|phi_Q(t)|^2dt
 <=[8k/(2k-1)]sqrt(pi)|det B|^{-1/(2k)}.`                (4.2)

Using only the whole-output independent-copy identity

`|phi_Q(t)|^2=E exp(i t(Q-Q'))`,                          (4.3)

with `Q'` an independent copy of the entire scalar output, the regularized half-Riesz identity gives

`boxed: E|Q-Q'|^{-1/2}
 <=[8k/((2k-1)sqrt(2))]|det B|^{-1/(2k)}.`               (4.4)

At `k=1`, these are `8sqrt(pi/|e|)` and `4sqrt(2)|e|^{-1/2}`. No coordinatewise difference is separated from its conjugate sum. Linear small-ball scaling comes from the stronger `L^1_t` bound (3.3), not from reversing (4.2).

## 5. Exact target family

Take seven independent cap-one variables `X,Z,W,H_1,H_2,Y_1,Y_2` and

`Q_*=2XZ+2XW+2H_1(Y_1+W)+2H_2Y_2`.                      (5.1)

Condition on the original coordinate `W=w`. The negative packet is

`S_w=2XZ+2wX`

with `k=1,e=1`. The positive packet is

`T_w=2H_1(Y_1+w)+2H_2Y_2`,

whose slope vector `(Y_1+w,Y_2)` has joint density cap at most one. Hence

`boxed: ||p_Q_*||_infty <=4sqrt(2/3)
 =3.265986323710904...`,                                  (5.2)

so `P(Q_* in I)<=3.265986323710904... |I|` for every interval `I`. The proof gives a continuous `C_0` density.

In the variable order `(Z,X,W,H_1,Y_1,H_2,Y_2)`, the coefficient matrix is the adjacency matrix of `P_5` plus one disjoint edge. Its spectrum is exactly

`{sqrt(3),-sqrt(3),1,1,-1,-1,0}`.                        (5.3)

Thus six eigenvalues have modulus at least one: this is a strict owner-target instance with both a genuine deterministic cross edge and a physical environment shared by the two weighted-time packets.

For the same family,

`int |t|^{-1/2}|phi_Q_*(t)|^2dt <=8sqrt(pi)
 =14.179630807244127...`,                                 (5.4)

`E|Q_*-Q_*'|^{-1/2}<=4sqrt(2)=5.656854249492381...`.     (5.5)

## 6. Remaining implication

This pays a dimension-free cross-pair absorption branch: an invertible physical crossing can be grouped into the negative-half packet, while a separate two-slope packet supplies the positive-half budget, and the two packets may share arbitrary conditioned original-coordinate environment variables. The cross interaction need not be perturbatively small and is not removed by rotation.

It does not close the critical `2+1` cross-hub case when regrouping the cross edge leaves only one fresh smoothing hub. The remaining global task is to show that every `s_3(A)>=1` survivor either contains a quantitative cross packet plus a disjoint two-slope packet of this kind, or routes to one of the already-paid grouped-hub/ridge/principal-pair/exterior-mass/aggregate receivers.

Full universal boundedness: **OPEN**. Unrestricted continuity: **OPEN**. Continuity is proved only for the branch (3.4).

## 7. Source pins

- Negative packet theorem: `yspennstate/math-open-problems@6c4698000d4fd206b465a18231ba8c7a8f643f59`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B03/20260924T000609Z-fleet01-B03-QFORM-r36/REPORT.md`.
- Designated partner actually applied: `yspennstate/math-open-problems@54243d0668be2be7879ae467ed9cb6b962f24652`, `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260924T081949Z-fleet02-B03-QFORM-auto11-r52/REPORT.md`.

The live correction inbox was reread immediately before publication. In particular, the proof avoids the refuted conditional copy-sum/difference cap and mixed-fiber interfaces.
