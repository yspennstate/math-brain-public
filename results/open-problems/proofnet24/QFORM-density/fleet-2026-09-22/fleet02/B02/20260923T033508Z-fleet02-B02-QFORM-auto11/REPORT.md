SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B02, 2026-09-23T03:35:08Z.
attacking: the Integrated Fourier nested near-coloop collar; use D-prime as the branching test and show that its exact-rank-two descendant is automatically transverse, hence paid by the partner exact-rank-three L1 Fourier theorem.

# fleet02/B02 — nested volume-coloop descent and automatic transverse closure of the rank-two floor

Programme: `QFORM-DENSITY-3EIG-20260922`.
Run: `20260923T033508Z-fleet02-B02-QFORM-auto11`.
Full target: **OPEN / NOT PROVED / NOT DISPROVED**.
Continuity: proved on every Fourier branch stated below; full-target continuity remains open.
Execution: authenticated repository retrieval and this worker's prior source-pinned memory snapshot were actually consumed; no native learned-memory ingestion is asserted.

## 1. Exact obligation and source pins

The target is unchanged: independent original real coordinates, each with probability density at most one; arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one; prove one dimension/law/matrix-independent essential density bound for `X^T A X`, or give a target-valid counterexample. No moments, bounded support, log-concavity, diagonal-basis independence, or post-rotation independence are assumed.

Required Claude-source package actually used at equation level:

- `yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
  `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`;
- current volume-stability continuation `yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, especially its fractional three-volume theorem.

The prior B02 run independently checked the sharp-Hausdorff--Young fractional-volume theorem and derived the live compiler

`||p_Q||_infinity <= [3e/((3-2q)sqrt(q))] Z_3^(-1/6),`                (1.1)

for `1<=q<3/2` whenever every row three-volume marginal is at most `q/2`. At `q=4/3` the gate is `<=2/3` and the coefficient is `9sqrt(3)e/2`. It also proved the ungated D5 compiler

`||p_Q||_infinity <= (5e/sqrt(2)) Z_5^(-1/10)`.                       (1.2)

Those are not re-proved here; they are used as exits/branching tests.

The latest compatible designated partner is `fleet03/B02` r18, current report commit

`yspennstate/math-open-problems@7f0da7bc3a8072d96033846b208d43d446bedb8c`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B02/20260923T025843Z-fleet03-B02-qform-r18/REPORT.md`.

It retains the predecessor exact-rank-three physical-cross-block theorem at
`yspennstate/math-open-problems@484c89f85cda352b2c4318364a6206ebc4154950`:
if an original-coordinate cross block has exact rank three and nonzero singular-value product `Gamma`, then

`|phi_Q(t)| <= min(1,(2pi)^(3/2) Gamma^(-1/2)|t|^(-3/2)),`            (1.3)
`||p_Q||_infinity <= 6 Gamma^(-1/3)`,                                (1.4)

with arbitrary same-bank quadratic phases, outside couplings and affine terms, and with a continuous output density. The latest r18 report further isolates a scalar Schur resonance only when the surviving rank-two packet is span-aligned on both sides. The result below shows that this span-aligned residue cannot occur at the exact-rank-two floor of the live nested four-volume collar.

All live corrections against pointwise scalar decay, post-rotation independence, single-minor extraction, universal rank-three cuts, and conditioning-fiber suprema are preserved. No argument below selects one physical minor.

## 2. Live D5/D-prime branch before the new step

Let `M=A[I,J]` be a physical cross block between disjoint original-coordinate banks and put

`Z_k=e_k(M^T M)`.

If the fifth exterior volume is quantitatively usable, (1.2) is already a law-uniform unweighted `L^1` Fourier exit with no volume-marginal gate. Thus the difficult collar is the low-fifth-volume/effective-rank-at-most-four regime.

Inside that collar, suppose `Z_4>0` and row `i` has four-volume inclusion marginal `h_i`. Write its row as `r_i` and delete it:

`N=M[-i,:]`.

The preceding B02 run proved by Cauchy--Binet and the exterior contraction inequality

`h_i Z_4 <= ||r_i||^2 Z_3(N)`,                                       (2.1)

where `Z_3(N)=e_3(N^T N)`. If every row three-volume marginal of `N` is at most `2/3`, condition on the original coordinate `X_i` and apply (1.1) with `q=4/3`. In particular, when `h_i>=3/4`,

`||p_Q||_infinity < 22.228 (s_2(M)s_3(M)s_4(M))^(-1/3)`.             (2.2)

Hence the first genuinely unpaid nested case is precisely when `N` fails this D-prime gate. Then some original row `j` of `N` has third-volume marginal

`g_j>2/3`.                                                            (2.3)

Delete that row as well and put

`P=M[-{i,j},:]`.

The same aggregate exterior argument gives

`g_j Z_3(N) <= ||r_j||^2 Z_2(P)`.                                    (2.4)

Combining (2.1) and (2.4) gives the useful but non-exhaustive descendant lower bound

`Z_2(P) >= h_i g_j Z_4/(||r_i||^2 ||r_j||^2)`.                        (2.5)

The central question is what happens when this descendant reaches exact rank two.

## 3. New exact exterior identity at the rank-two floor

### Theorem 3.1 — `QFORM-NESTED-COLOOP-RANK2-AUTOTRANSVERSE-v1`

Let `M` be any real matrix with `Z_4=e_4(M^T M)>0`. Pick two distinct rows `r_i,r_j`, and let

`P=M[-{i,j},:]`.

Assume `rank(P)=2`. Put

`Delta=s_1(P)s_2(P)>0`,
`W=Row(P)`,
`u=Proj_(W^perp) r_i`,
`v=Proj_(W^perp) r_j`.

Then

`boxed( Z_4 = Delta^2 ||u wedge v||^2 ).`                              (3.1)

Consequently `u` and `v` are both nonzero and linearly independent. In particular

`Delta dist(r_i,W) >= sqrt(Z_4)/||r_j||`,                              (3.2)
`Delta dist(r_j,W) >= sqrt(Z_4)/||r_i||`.                              (3.3)

Therefore, for every quadratic form whose physical cross block on `I|J` is `M`, arbitrary same-bank blocks and all outside couplings included,

`boxed(
 ||p_Q||_infinity
 <= 6 min(||r_i||,||r_j||)^(1/3) Z_4^(-1/6)
 <= 6 (s_2(M)s_3(M)s_4(M))^(-1/3).
)`                                                                   (3.4)

Moreover the characteristic function is in `L^1`, so the density on this branch is continuous and vanishes at infinity.

### Proof

Because `rank(P)=2`, any nonzero four-fold wedge of rows of `M` must contain **both** `r_i,r_j` and exactly two rows of `P`. For any two rows `p_a,p_b` of `P`, the components of `r_i,r_j` lying in `W` disappear after wedging with `p_a,p_b`, while `u,v` are orthogonal to `W`. Hence

`||r_i wedge r_j wedge p_a wedge p_b||^2
 = ||u wedge v||^2 ||p_a wedge p_b||^2`.                               (3.5)

Summing (3.5) over all two-row subsets of `P` and using Cauchy--Binet gives

`Z_4 = ||u wedge v||^2 e_2(P^T P)
     = Delta^2 ||u wedge v||^2`,                                      (3.6)

which is (3.1). Since `Z_4>0`, `u wedge v` is nonzero, so in particular neither `u` nor `v` vanishes.

Now

`||u wedge v|| <= ||u|| ||v|| <= dist(r_i,W) ||r_j||`                 (3.7)

and symmetrically with `i,j` interchanged. Combining (3.1) and (3.7) proves (3.2)--(3.3).

Condition on the original coordinate `X_j`. The remaining cut

`({i} union (I\{i,j})) | J`

has physical cross block obtained by adjoining `r_i` to `P`. Since `u!=0`, this block has exact rank three. The exterior identity from the partner r17 theorem gives its nonzero singular-value product

`Gamma_i = Delta dist(r_i,W)`.                                        (3.8)

Every term generated by conditioning `X_j` is only a same-bank/affine phase for this cut, exactly within the partner theorem's stated scope. Therefore (1.4) and (3.2) yield

`||p_Q||_infinity <= 6 Gamma_i^(-1/3)
                   <= 6 ||r_j||^(1/3) Z_4^(-1/6)`.                    (3.9)

Conditioning on `X_i` instead yields

`||p_Q||_infinity <= 6 ||r_i||^(1/3) Z_4^(-1/6)`.                    (3.10)

Taking the minimum proves the first inequality in (3.4). Finally each row norm is at most `s_1(M)`, while

`Z_4=e_4(s_1(M)^2,s_2(M)^2,...) >= s_1^2 s_2^2 s_3^2 s_4^2`.         (3.11)

Thus

`s_1^(1/3) Z_4^(-1/6) <= (s_2 s_3 s_4)^(-1/3)`,                       (3.12)

which proves the second inequality. The partner bound came from the explicit integrable envelope (1.3), so continuity follows on this branch. QED.

## 4. What this changes in the nested D-prime collar

The live high-four-volume-row recursion is now:

1. **D5 exit.** If `Z_5` is usable, apply (1.2), no marginal gate.
2. **D-prime after one heavy row.** If `h_i` is large and the row-deleted `N` has all third-volume marginals `<=2/3`, apply (2.2).
3. **D-prime fails.** Choose a physical row `j` with `g_j>2/3` and form `P=M[-{i,j},:]`.
4. **New closure at rank two.** If `rank(P)=2`, Theorem 3.1 applies and gives (3.4), independently of how close `h_i` or `g_j` are to one.

Thus the former `critical exact-rank-two global-third` residue was spurious inside this particular `Z_4>0` nested-coloop geometry. The fourth exterior volume itself forces the two deleted rows to supply two linearly independent directions transverse to `Row(P)`. After conditioning either deleted coordinate, the other one raises `P` to an exact-rank-three physical cross block. In the language of the latest partner r18 report, the two-sided span-aligned scalar-resonance obstruction cannot occur here: the surviving scalar row is necessarily transverse before any Schur completion is attempted.

For the quantitatively heavy case `h_i>=3/4`, `g_j>2/3`, the aggregate bound (2.5) also records

`Z_2(P) > Z_4/(2||r_i||^2||r_j||^2)`,                                (4.1)

but Theorem 3.1 is stronger at the exact-rank-two floor because it uses the full four-volume identity rather than only this lower bound.

## 5. First unpaid implication after this run

The remaining near-coloop obstruction is now narrower:

`QFORM-NESTED-DPRIME-RANKGE3-CONCENTRATION-v1`.

After a four-volume-heavy row is removed and the residual third-volume D-prime gate fails at a second row, the twice-deleted physical block `P` may still have rank at least three. The exact-rank-two floor is paid by Theorem 3.1. What remains is to spend the residual third/fourth exterior mass when `rank(P)>=3` but its own third-volume measure is again concentrated, without selecting a tiny local minor or invoking false scalar pointwise decay. A viable next step is a repeated aggregate deletion/conditioning recursion in which every rank-two floor is now an exit, together with D5 whenever the surviving tail stable rank rises above the low-rank collar.

No target-valid counterexample to a universal full-target unweighted `integral |phi_Q(t)| dt` estimate was found in this run. The stronger Fourier criterion therefore remains **OPEN, not refuted**.

## 6. Status

New result: `QFORM-NESTED-COLOOP-RANK2-AUTOTRANSVERSE-v1`.
Status: **proved supporting implication / partner theorem applied at an actual inequality**.
Full QFORM target: **OPEN**.
Independent review of this new theorem: **not yet performed**.
