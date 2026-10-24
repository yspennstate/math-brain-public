# account01/B01 continuation — zero-curvature active-edge receiver

Continuation of canonical run `20260923T131631Z-account01-B01-qform-auto11`; no duplicate actual-hour login is created.

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: oscillatory replacement  
Status: **NEW EXACT RECEIVER + ZERO-CURVATURE ENDPOINT SHARPENING / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary

Fresh prepublication owner control remained revision `2026-09-22.15`, QFORM-only, with no B01 pause/stop. The current correction inbox was reread. In particular, the argument below does not use any law-uniform pointwise scalar quadratic-phase decay, post-rotation independence, unrestricted joint coarea estimate, conditional projection cap, or inversion of a tiny physical `3 x 3` minor before aggregate product structure is spent.

The same canonical-run report already proved the exact pair-volume/deletion calculus for a common-hub rank-one-leaf packet. The prior B01 receiver used below is `QFORM-HIGH-LEVERAGE-RECEIVER-SCHUR-v1`, proved at

`yspennstate/math-open-problems@995ecef79fea84985a483b6a25d695c7131d934c`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B01/20260923T081748Z-account01-B01-qform-auto11/REPORT.md`.

Its invariant content is: if a rank-two physical cross block has singular-value product `Delta`, a physical receiver coordinate has nonzero pivot `a`, and the exact post-pivot cross product is `Delta_j=Delta sqrt(N_j)/|a|` with `N_j>0`, then

`||p_Q||_infinity <= 8 |a|^(-1/4) Delta^(-1/4) N_j^(-1/8)`.

Only essential boundedness is asserted by that receiver.

The designated partner result actually applied remains account02/B01 r42,

`yspennstate/math-open-problems@2aa47367766e1b63306bec723c42fcd2899ca6ac`,
`proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T120442Z-account02-B01-qform-r42/REPORT.md`,

whose exterior decomposition gives `W0+W1+W2+W3=e_3(A^2)>=1` and whose strict-N3 hub-square family has

`(W0,W1,W2,W3)=(0,(1-1/m)^2,2(m-1)/m^2,1/m^2)`.

## 2. Setup and previously proved currencies

Fix one ORIGINAL physical hub `h` and a disjoint leaf bank `L`. After conditioning all other original coordinates, assume

`A[L,L]=D+lambda z z^T`,

where `D=diag(D_i)`, `lambda!=0`, `||z||_2=1`. Let

`b=A[L,h]`, `R=[b,z]`, `Gamma=R^T R`, `E=det Gamma>0`.

For `i<j`, put

`theta_ij=b_i z_j-b_j z_i`,
`p_ij=theta_ij^2/E`,
`ell_i=sum_{j!=i} p_ij`,
`q_ij=1-ell_i-ell_j+p_ij`.

The canonical report proves

`sum_{i<j} p_ij=1`,
`det Gamma_{-i}=E(1-ell_i)`,
`det Gamma_{-ij}=E q_ij`,

and

`d:=W1(h;L)/(lambda^2 E^2)=sum_{i<j} p_ij q_ij`.

An edge `{i,j}` will be called **active** when `p_ij q_ij>0`.

The same report defined the kernel-curvature quantity

`T_ij=|D_i z_j^2+D_j z_i^2|`

and paid the aggregate currency

`K_D=sum_{i<j} p_ij q_ij T_ij`

through the rank-two cross/kernel-curvature theorem. The remaining exact endpoint was `K_D=0`.

## 3. A second exact receiver that survives `T_ij=0`

Fix an active edge `{i,j}` and orient it from `i` to `j`. Since `q_ij>0`, `det Gamma_{-ij}>0`; hence `ell_i<1`.

Assume for the moment

`z_i!=0`, `D_j!=0`, `a_j:=D_j+lambda z_j^2!=0`.                 (3.1)

Take the two ORIGINAL physical coordinates `{h,i}` as the first bank and the receiver bank `J=L\{i}`. Its cross block is

`K_i = [ b_J^T ; lambda z_i z_J^T ]`.

By Cauchy--Binet,

`det(K_i K_i^T)=lambda^2 z_i^2 det Gamma_{-i}`,

so its rank-two singular-value product is

`boxed: Delta_i=|lambda z_i| sqrt(E(1-ell_i)).`                    (3.2)

Now complete the square only in the ORIGINAL receiver coordinate `X_j`. For every `k notin {i,j}`, the two post-pivot cross rows are

`b_k - (lambda z_j b_j/a_j) z_k`,
`lambda z_i z_k (D_j/a_j)`.

Therefore every two-column wedge is multiplied by `lambda z_i D_j/a_j`, and another Cauchy--Binet computation gives the exact post-pivot area

`boxed:
 Delta_{i->j}
 = |lambda z_i D_j| sqrt(E q_ij)/|a_j|.`                           (3.3)

Compare (3.3) with the exact residual-area parametrization of the prior B01 receiver,

`Delta_{i->j}=Delta_i sqrt(N_{i->j})/|a_j|`.

The dependence on the potentially tiny deletion factor `1-ell_i` cancels exactly:

`boxed:
 N_{i->j}= D_j^2 q_ij/(1-ell_i).`                                  (3.4)

Applying `QFORM-HIGH-LEVERAGE-RECEIVER-SCHUR-v1` and substituting (3.2)--(3.4) yields

### Theorem 3.1 — oriented pivoted-edge receiver

Under (3.1), for arbitrary cap-one product input laws and arbitrary affine terms created by the outside conditioning,

`boxed:
 ||p_Q||_infinity
 <= 8 [lambda^2 E q_ij z_i^2 D_j^2 a_j^2]^(-1/8).`                 (3.5)

No leverage upper bound appears. No factor `1-ell_i` remains. This is essential boundedness; continuity is not claimed from this branch.

The proof uses only original-coordinate Schur completion and rank-two projected averaging. It does not assert pointwise scalar Fresnel decay.

## 4. Aggregate pivoted currency

For every unordered leaf edge set

`a_i=D_i+lambda z_i^2`,

`G_ij=max{ z_i^2 D_j^2 a_j^2, z_j^2 D_i^2 a_i^2 }`,                (4.1)

and define the nonnegative aggregate

`K_P = sum_{i<j} p_ij q_ij G_ij`.                                  (4.2)

Because `sum p_ij=1`, some active edge satisfies

`q_ij G_ij >= K_P`.

Orient that edge toward the endpoint realizing the maximum in (4.1). If `K_P>0`, all hypotheses of Theorem 3.1 hold for that orientation. Hence

### Theorem 4.1 — `QFORM-W1-RANK1-LEAF-PIVOTED-EDGE-v1`

In the common-hub `diagonal + rank-one` leaf setup, with **no leverage restriction**, if `K_P>0`, then

`boxed:
 ||p_Q||_infinity <= 8 [lambda^2 E K_P]^(-1/8).`                   (4.3)

The selection loses no factor depending on `|L|`. Under matrix scaling `A -> cA`, the quantity `lambda^2 E K_P` scales as `|c|^8`, so (4.3) has the correct density scaling `|c|^-1`.

This theorem is independent of the preceding curvature lift: `K_D` can vanish identically while `K_P` is positive.

## 5. Exact resolution of the nonzero-`z` zero-curvature active edge

Assume now `K_D=0`. Every active edge then satisfies

`D_i z_j^2+D_j z_i^2=0`.                                          (5.1)

Take an active edge with `z_i z_j!=0`. Equation (5.1) has only two possibilities:

1. `D_i=D_j=0`; or
2. both `D_i,D_j` are nonzero and have opposite signs after weighting by `z_i^2,z_j^2`.

In case 2, the two total pivots `a_i=D_i+lambda z_i^2` and `a_j=D_j+lambda z_j^2` cannot both vanish. Indeed, if both vanished then

`D_i=-lambda z_i^2`, `D_j=-lambda z_j^2`,

so the left side of (5.1) would be

`-2 lambda z_i^2 z_j^2 !=0`, a contradiction.

Thus at least one orientation in (4.1) has strictly positive `G_ij`, and Theorem 4.1 pays that edge.

Consequently:

### Corollary 5.1 — double-zero sharpening

If

`K_D=0` **and** `K_P=0`,

then every active edge `{i,j}` with `z_i z_j!=0` satisfies

`boxed: D_i=D_j=0.`                                                 (5.2)

So the previous alternating-curvature graph does not remain as a genuinely unpaid analytic endpoint: every active nonzero-curvature alternating edge is absorbed by a physical pivoted receiver. What survives on the nonzero-`z` active graph is exact zero diagonal curvature.

## 6. Stronger Schur identity on a nonzero-curvature zero-curvature edge

The preceding payment has an additional exact structural interpretation. Suppose an active edge has `z_i z_j!=0` and `D_iD_j!=0` while (5.1) holds. Its leaf principal block is

`B_ij=diag(D_i,D_j)+lambda z_{ij}z_{ij}^T`.

Then

`det B_ij=D_iD_j+lambda(D_i z_j^2+D_j z_i^2)=D_iD_j<0`,            (6.1)

so it is an invertible **indefinite physical pair**.

Moreover

`z_{ij}^T diag(D_i,D_j)^(-1) z_{ij}
 = z_i^2/D_i+z_j^2/D_j=0`,                                        (6.2)

again by (5.1). Sherman--Morrison therefore gives

`z_{ij}^T B_ij^(-1) z_{ij}=0`.

Completing this physical pair leaves the rank-one leaf curvature on the complement **exactly unchanged**:

`boxed:
 A[L\{i,j},L\{i,j}] / B_ij
 = D_{-ij}+lambda z_{-ij}z_{-ij}^T.`                               (6.3)

The hub slope changes only by a multiple of `z_{-ij}`,

`b_{-ij}'=b_{-ij}-c z_{-ij}`,

for some scalar `c`. Hence all wedges with `z` are invariant:

`b_k' z_l-b_l' z_k = b_k z_l-b_l z_k`,

and therefore the remaining two-frame area is exactly

`boxed: det([b'_{-ij},z_{-ij}]^T[b'_{-ij},z_{-ij}])=E q_ij.`       (6.4)

Thus the zero-curvature relation is not a Schur-destruction state: whenever its diagonal curvature is nonzero, the corresponding physical pair is hyperbolic and pair elimination preserves the entire complementary rank-one-leaf geometry.

## 7. The only active zero-`z` endpoint is a pure hyperbolic coloop

Suppose `{i,j}` is active, `z_i=0`, `z_j!=0`. Since `p_ij>0`,

`theta_ij=b_i z_j!=0`, so `b_i!=0`.

Under `K_D=0`, (5.1) gives `D_i=0`. The physical pair `{h,i}` is therefore

`[[A_hh,b_i],[b_i,0]]`,

whose determinant is `-b_i^2<0`: it is invertible indefinite. Also leaf coordinate `i` has no coupling to any other leaf coordinate because `z_i=0`. The pair-to-rest coupling has the form `[b_{-i};0]`; the `(h,h)` entry of the inverse of the displayed hyperbolic pair is zero. Hence eliminating `{h,i}` leaves the full leaf quadratic block **exactly unchanged**:

`boxed:
 A[L\{i},L\{i}] / A[{h,i},{h,i}]
 = D_{-i}+lambda z_{-i}z_{-i}^T.`                                  (7.1)

Both endpoints cannot have `z=0` on an active edge, because then `theta_ij=0`.

Thus after `K_D=K_P=0`, every remaining active edge is one of two exact algebraic types:

- both endpoints have nonzero `z` and zero diagonal curvature (`D_i=D_j=0`); or
- one endpoint has `z_i=D_i=0`, which exposes an exact hyperbolic physical pair whose Schur elimination preserves the entire rank-one-leaf remainder.

This is a substantially narrower endpoint than the former alternating-curvature graph.

## 8. Designated partner r42 applied to an actual inequality

Account02/B01 r42 proves that every full-target matrix is first routed by exterior-three energy: if its `W0` branch has a cut with the stated `D'` marginal condition, then

`||p_Q||_infinity <64.763`,

so no overlap-one work is needed. Otherwise one reaches a two-sided coloop endpoint or an overlap-dominated state `W1+W2+W3>3/4`.

On r42's exact strict-N3 hub-square family

`Q_m=2X_0(a^T Y)+(z^T Z)^2`,

it computes

`W1=(1-1/m)^2`, `W0=0`, `W2=2(m-1)/m^2`, `W3=1/m^2`.

For this family the rank-one-leaf diagonal `D` is identically zero, so **both** new currencies satisfy

`K_D=K_P=0`.

Corollary 5.1 therefore sends it exactly to the remaining zero-diagonal endpoint, rather than spuriously claiming a pivoted-curvature payment. The previous B01 mixed-Fresnel theorem then applies directly to r42's exact `W1` value and gives

`boxed:
 ||p_(Q_m)||_infinity
 <=3*2^(4/3)(1-1/m)^(-1/3)<7.904,  m>=8.`                          (8.1)

This is an equation-level application of the current designated-partner result and confirms that the new endpoint classification is compatible with its canonical strict-N3 overlap model.

## 9. What remains

Within a common-hub `diagonal + rank-one` leaf star, the analytic picture is now:

1. diffuse augmented leverage: paid by the mixed-Fresnel `W1` theorem;
2. positive aggregate kernel curvature `K_D`: paid by the rank-two cross/kernel-curvature lift;
3. positive aggregate pivoted currency `K_P`: paid by Theorem 4.1;
4. `K_D=K_P=0`: exact zero-diagonal / pure-hyperbolic-coloop structure of Sections 5--7.

The first unpaid implication is sharpened to

`QFORM-W1-ZERODIAG-OR-HYPERBOLIC-COLOOP-ROUTING-v3`:

starting from a global `W1`-heavy state, localize dimension-free to a common hub packet or route higher leaf rank elsewhere; once in a common-hub rank-one-leaf packet, pay the exact zero-diagonal survivor by a grouped hub/square theorem or iterate the hyperbolic-coloop Schur invariance without losing the aggregate `W1` currency.

The unrestricted three-large-eigenvalue conjecture remains **OPEN**. Full-target continuity remains **OPEN**. The phase-aligned fragmented-support counterexample to law-uniform scalar pointwise decay remains fully preserved.
