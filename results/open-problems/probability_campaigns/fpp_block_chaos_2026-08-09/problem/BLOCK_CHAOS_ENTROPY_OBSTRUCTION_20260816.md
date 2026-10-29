# Block-chaos needs entropy beyond a localization cover

Date: 2026-08-16  
Status: deterministic and probabilistic obstructions proved; no variance
exponent is obtained  
Engine source: `MG2B_framework_lemma_draft.md`, SHA-256
`59c4b5a42edca0a7d53508f9b669cfaab3ba800d04b3e7effbd0312f040ab3f7`  
Arithmetic source: `CRUX_iteration_arithmetic.md`, SHA-256
`58593b9aaf82676e746933bf6ec4aed36529bec217d1ed60627e8acd051e98aa`

## The proposed gap event is the overlap event

Fix a block `L`. In environment `r=1,2`, let `A_r` be the best passage
cost among paths through `L`, let `C_r` be the best cost among paths avoiding
`L`, and assume these costs are finite. Put

`D_r=A_r-C_r,  G=C_1-A_1=-D_1,
 H=(A_2-A_1)-(C_2-C_1)=D_2-D_1.`

Then, identically,

`H-G=D_2=A_2-C_2.`                                       (1)

For any fixed measurable geodesic selector, if `U_L^(r)` is the event that
the selected path in environment `r` uses `L`, (1) gives the tie-correct
sandwich

`U_L^(1) intersect {H<G}
 subseteq U_L^(1) intersect U_L^(2)
 subseteq U_L^(1) intersect {H<=G}.`                      (2)

The only possible slack is `A_2=C_2`. With continuous weights, or whenever
through/avoiding ties have probability zero, all three events in (2) agree
almost surely.

Let `F=F_(1-kappa)` be the common environment in the standard conditional
coupling and let the two completions be conditionally iid. Define

`q_L=P(U_L|F),  r_L=P(A_L<=C_L|F).`

Conditional independence gives

`P(U_L^(1),H<=G|F)=q_L r_L,
 P(U_L^(1),U_L^(2)|F)=q_L^2.`                             (3)

Here `r_L-q_L` is exactly the conditional weak-tie mass on which the
selector avoids `L`. In the tie-free case, `r_L=q_L`; summing the proposed
gap event in (3) is then exactly

`Pbar(kappa)=sum_L E[q_L^2].`                             (4)

A gap-versus-noise tail estimate at this point would already be a proof of
the chaos hypothesis, not a new intermediate bridge.

## Collision floor

Let `p_L=P(U_L)=E[q_L]`. From conditional variance,

`Pbar(kappa)=sum_L p_L^2 + sum_L Var(q_L).`                (5)

The first term is the expected number of common block labels for two fully
independent selected paths (a collision mass, not generally a probability).
The second is the additional expected overlap caused by their shared
environment.

Now divide the longitudinal direction into `M` slabs. Suppose
`J_1,...,J_M` are pairwise disjoint deterministic block-label sets, as in a
slab-indexed tiling, with `K_s=|J_s|>=1` and `0<=delta_s<=1`, such that the
selected path hits at least one member of `J_s` with probability at least
`1-delta_s`. The union bound and Cauchy--Schwarz give

`sum_(L in J_s) p_L >= 1-delta_s,
 sum_(L in J_s) p_L^2 >= (1-delta_s)^2/K_s.`              (6)

Therefore

`Pbar(kappa) >= sum_(s=1)^M (1-delta_s)^2/K_s.`           (7)

If the same cover count is used as the `(L3)` certificate, namely

`C_occ^cover=(1/M) sum_s K_s,`

and `0<=delta_s<=delta<=1`, then another Cauchy--Schwarz inequality yields

`C_occ^cover Pbar(kappa)/M >= (1-delta)^2.`               (8)

The hit premise alone proves only (7). Treating the cover count as an `(L3)`
upper certificate additionally uses confinement or far-tail control; the
obstruction below applies when that same crude count, or a larger certificate,
is used.

The corrected CRUX 9.5 sufficient quarter-budget criterion is

`C_occ Pbar(kappa)/M <= 1/(16 kappa_4 beta^2).`            (9)

Thus the same localization-cover count cannot meet that particular
sufficient criterion whenever

`16 kappa_4 beta^2 (1-delta)^2>1.`                        (10)

This applies in particular to the intended `beta>1`, `kappa_4>=1` regime
when the cover misses only a small probability. It targets the deterministic
candidate-cover-count implementation in CRUX 9.6 and any 9.7 implementation
that uses that same count for `C_occ`. It does not rule out an `(L3)` argument,
including a random-endpoint or local-spread route, whose expected occupation
is much smaller than its candidate-cover count.

## Negative controls

1. **Straight path.** For passage from `0` to `Ne_1`, take iid continuous
   weights in `[a,a+delta]` with `N delta<2a`. The axis path costs at most
   `N(a+delta)`, while every non-axis path has at least `N+2` edges and costs
   at least `(N+2)a`. It is uniquely optimal in every completion. Each of its
   longitudinal blocks has `q_L=1`, so `Pbar>=M` despite positive, linear
   passage-time variance: for each fixed `N`,
   `Var(T(0,Ne_1))=N Var(w)>0`. This is a finite-scale, model-dependent
   control. The condition `N delta<2a` cannot persist as `N` tends to infinity
   for one fixed nondegenerate interval law.

2. **Two genuine routes.** From `(0,0)` to `(1,1)` in `Z^2`, take iid
   continuous weights in `[a,b]` with `b<2a`. The two length-two monotone
   paths beat every path of length at least four, and symmetry makes each win
   with probability `1/2`. For the two route blocks, conditionally
   `q_++q_-=1`, hence `q_+^2+q_-^2>=1/2`. Full independent resampling attains
   the lower bound; a shared environment can only increase it.

3. **Series diamonds.** Repeating the preceding two-route gadget in an
   abstract planar FPP network gives
   `X_M=sum_s min(S_(s,+),S_(s,-))` and
   `Var(X_M)=M Var(X_1)`, while `Pbar>=M/2`. This is an engine-level negative
   control, not a claim about asymptotics on the full square lattice.

Multiplying every edge weight by a constant scales costs and variances but
does not change any route event. Neither absolute variance size nor a fixed
scale-variance ratio can by itself force small overlap.

## A noncircular next target

A sufficient input would be conditional route delocalization. If

`ess sup q_L <= eta` for every relevant `L`, and
`sum_L p_L <= C_occ M,`

then

`Pbar(kappa) <= eta C_occ M.`                             (11)

The chaos/fourth-moment leg meets the corrected quarter-budget criterion when

`eta <= 1/(16 kappa_4 beta^2 C_occ^2).`                   (12)

Full halving still separately assumes `(L1')`--`(L3)` and
`kappa<=1/(4 beta C_occ)`.

Geometrically, (11) asks for many possible block labels in each slab even
after conditioning, while each realized path visits only `O(1)` of them.
That entropy--occupation decoupling is not supplied by coarsening a
localization window, and it is the next proof obligation exposed by (8).
