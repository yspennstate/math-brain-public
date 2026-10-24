SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B18, 2026-09-23T16:54:32Z.
attacking: near-null physical-pivot collar — transfer a source-valid bounded-density theorem into the completed account02/B18 receiver without deleting the small Rayleigh term.

# account01/B18 r34 — source-separated near-null heavy-anchor collar

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Status:** `NEW SUPPORTING EXACT-RANK3 SUBBRANCH / DESIGNATED PARTNER APPLIED / FULL QFORM OPEN`  
**Continuity:** essential density bound only for the new punctured-collar theorem; continuity is retained only where an already-completed partner theorem explicitly supplies it.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

Fresh owner control was reread from `math-research-brain` main at invocation; OWNER CONTROL remains revision `2026-09-22.15`, QFORM-only. The later `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` continuation was acknowledged. No FEI or unrelated research was performed.

## 1. Incoming designated-partner state

The latest completed `account02/B18` report consumed in this run is

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B18/20260923T154246Z-account02-B18-QFORM-auto11b/REPORT.md`.

For an exact-rank-three representation

`A = R M R^T`, `R^T R = I_3`,

with all three eigenvalues of `M` of modulus at least one, write `u_i` for the physical spectral rows and `c_i=||u_i||^2`. Its completed results imply:

1. if a heavy row `u_0` has `c_0>1/2` and `|A_00|>=1/32`, then

   `||p_Q||_infinity < 256 sqrt(2) < 363`;

2. if `A_00=0`, then the exact-null heavy anchor is completely paid: the transverse-diffuse side has the sharper continuous bound `<3*2^(5/3)`, and any second transverse-heavy row is paid by the partner's double-heavy theorem;

3. if some other original physical row has transverse leverage `>1/2` relative to the heavy direction, then the full form is paid by `<363`, regardless of whether the first pivot is zero, tiny, or large.

Thus the only exact-rank-three heavy-anchor state left by that mechanism is the punctured collar

`0 < |A_00| < 1/32`, `c_0>1/2`,
`||P_(r^perp) u_j||^2 <=1/2` for all residual rows,

where `r=u_0/sqrt(c_0)`.

This run closes a concrete product-preserving subbranch of that collar: exact source separation between the residual longitudinal direction and the residual transverse two-plane.

## 2. Primary literature transfer, with hypotheses matched literally

Livshyts--Paouris--Pivovarov, *On sharp bounds for marginal densities of product measures*, Israel J. Math. 216 (2016), Theorem 1.1, assumes an actual product density `prod_i f_i` with `||f_i||_infinity<=1` and proves that every `k`-dimensional orthogonal marginal has density at most `2^(k/2)`. No moment, support, iid, log-concavity, symmetry, centering, or smoothness hypothesis is imposed.

I use this theorem only on projections of disjoint sets of ORIGINAL coordinates. In particular:

- a norm-one scalar aggregate has density cap `sqrt(2)`;
- a two-dimensional orthogonal projection has joint density cap `2`.

No independence is inferred after rotation. Independence below comes solely from disjoint original-coordinate source banks.

The quadratic-form receiver used below is the already-completed `QFORM-NEARNULL-SCALAR-DEPENDENT-PAIR-v1` from account02/B05 r21. It allows a cap-one scalar independent of an arbitrarily dependent pair of joint density cap `M_pair`; for

`B=[[a,beta,0],[beta,alpha,delta],[0,delta,gamma]]`

invertible with `beta*gamma !=0`, it proves

`||p_Q||_infinity <=31 M_pair^(2/3)|beta^2 gamma det B|^(-1/6)`,  (2.1)

uniformly as the scalar pivot `a` tends to zero. Its proof retains the root selector and therefore does not use the false conditional-cap-as-independence or arbitrary-joint coarea interfaces.

The second receiver is the completed rank-two half-Riesz theorem: for a two-dimensional orthogonal projection `(C,D)` of a cap-one product source and an invertible symmetric `2x2` matrix `S`,

`sup_t E |[C,D]S[C,D]^T-t|^(-1/2)
 <=16 sqrt(30)|det S|^(-1/4)`                                      (2.2)

in the zero-affine case.

## 3. Source-separated collar theorem

### `QFORM-NEARNULL-SOURCE-SPLIT-COLLAR-v1`

Assume the exact-rank-three target above and choose the heavy row

`u_0=sqrt(h) r`, `h>1/2`, `||r||=1`.

Assume

`0<|A_00|<1/32`.

In addition assume the residual ORIGINAL coordinates split into disjoint sets

`J_parallel disjoint_union J_perp`

such that

- `u_j` is parallel to `r` for every `j in J_parallel`;
- `u_j` is perpendicular to `r` for every `j in J_perp`.

Then for arbitrary independent original-coordinate input densities bounded by one,

`boxed: ||p_(X^T A X)||_infinity <147.530.`                         (3.1)

More precisely, one branch is `<69.639`; the complementary mixed-transverse branch is `<147.530`.

The theorem does **not** assert continuity.

### Proof

Put

`epsilon = r^T M r = A_00/h`.

Because `h>1/2` and `|A_00|<1/32`,

`|epsilon|<1/16`.                                                   (3.2)

Since every singular value of `M` is at least one,

`M^2 >= I`,

so

`||Mr||^2>=1`.                                                       (3.3)

Let

`s=||P_(r^perp)Mr||`.

If `s=0`, then `r` would be an eigenvector of `M` with eigenvalue `epsilon`, contradicting the singular-value lower bound. Hence `s>0`. Define

`v=P_(r^perp)Mr/s`

and choose unit `q` so `(r,v,q)` is an orthonormal basis. In this basis

`M=[[epsilon,s,0],[s,b,c],[0,c,d]]`.                                (3.4)

Equation (3.3) gives

`s^2=||Mr||^2-epsilon^2 >=1-epsilon^2 >255/256`.                    (3.5)

Write the residual rows as

`u_j=t_j r` for `j in J_parallel`,

and

`u_j=alpha_j v+beta_j q` for `j in J_perp`.

Parseval and the exact source separation imply

`sum_(J_parallel)t_j^2=1-h`,
`sum_(J_perp)alpha_j^2=sum_(J_perp)beta_j^2=1`,
`sum_(J_perp)alpha_j beta_j=0`.                                     (3.6)

Define the ORIGINAL-source aggregates

`Y=sqrt(h)X_0 + sum_(J_parallel)t_j X_j`,
`C=sum_(J_perp)alpha_j X_j`,
`D=sum_(J_perp)beta_j X_j`.                                         (3.7)

The source sets of `Y` and `(C,D)` are disjoint, hence

`Y independent of (C,D)`.                                          (3.8)

The coefficient vector defining `Y` has squared norm

`h+(1-h)=1`,

so the primary marginal theorem gives

`||p_Y||_infinity <=sqrt(2)`.                                      (3.9)

Likewise (3.6) says `(C,D)` is an orthogonal two-dimensional projection of a genuine product source, and therefore

`||p_(C,D)||_infinity <=2`.                                        (3.10)

Most importantly, the full quadratic form is **exactly**

`Q=epsilon Y^2+2sYC+bC^2+2cCD+dD^2`.                              (3.11)

There is no discarded error and no perturbative use of the small pivot.

#### Branch I: `|d|>=1/2`

Rescale only the scalar: let `K=sqrt(2)` and `Y_*=K Y`; then `Y_*` has density cap one. In variables `(Y_*,C,D)` the coefficient matrix is

`B_*=diag(K^(-1),1,1) M diag(K^(-1),1,1)`.

Thus

`beta_*=s/K`, `gamma_*=d`, `det B_*=det M/K^2`.

Apply (2.1) with pair cap `M_pair=2`. Since `|det M|>=1`, (3.5), and `|d|>=1/2`,

`||p_Q||_infinity
 <=31*2^(2/3)*K^(2/3)*|s^2 d det M|^(-1/6)
 <=62*(512/255)^(1/6)
 =69.6380582404... .`                                              (3.12)

This is an actual near-null application; the estimate contains no negative power of `epsilon`.

#### Branch II: `|d|<1/2`

The direct curvature in the cross-orthogonal pair direction is now small, but the inverse matrix forces a compensating mixed coefficient. Let

`x=M^(-1)e_3`.

Since `sigma_min(M)>=1`, `||x||<=1`. The first and third rows of `Mx=e_3` are

`epsilon x_1+s x_2=0`,
`c x_2+d x_3=1`.

Therefore

`|x_2|<=|epsilon|/s`

and, because `|d|<1/2`,

`|epsilon c|/s >1/2`.                                              (3.13)

Also

`(M^(-1))_(31)=s c/det M`,

so `||M^(-1)||<=1` implies

`|det M|>=s|c|`.                                                     (3.14)

Multiplying (3.13)--(3.14),

`|epsilon det M| >s^2/2 >255/512`.                                (3.15)

Complete the square only in the genuine scalar aggregate `Y`:

`Q=epsilon (Y+(s/epsilon)C)^2 + [C,D]S[C,D]^T`,                    (3.16)

where

`S=[[b-s^2/epsilon,c],[c,d]]`

and the exact scalar Schur determinant identity gives

`det S=det M/epsilon`.                                              (3.17)

The translated scalar in (3.16) still has conditional density cap at most `sqrt(2)` because the shift is deterministic once the independent pair is fixed. The ordinary square-root kernel followed by (2.2) therefore yields

`||p_Q||_infinity
 <=sqrt(2)*16*sqrt(30)*|epsilon det M|^(-1/4)
 <sqrt(2)*16*sqrt(30)*(512/255)^(1/4)
 =147.529222282... .`                                               (3.18)

This proves (3.1). QED.

## 4. Designated account02/B18 result applied at an actual inequality

The new theorem plugs directly into the latest account02/B18 exhaustive heavy-row split.

For a source-separated heavy anchor:

- if `|A_00|>=1/32`, the partner physical-pivot estimate gives
  `||p_Q||_infinity <256 sqrt(2)=362.038671968...`;
- if `A_00=0`, the partner exact-null theorem plus its transverse-heavy alternative gives `<363` (with the transverse-diffuse exact-null subcase continuous and `<9.525`);
- if `0<|A_00|<1/32` and a second row is transverse-heavy, the partner double-heavy theorem gives `<363`;
- if `0<|A_00|<1/32` and the residual geometry is the source-separated collar above, (3.18) gives `<147.530`.

Hence:

### `QFORM-SOURCE-SPLIT-HEAVY-ANCHOR-COMPLETE-v1`

Every exact-rank-three target whose heavy row has an exactly source-separated residual longitudinal/transverse decomposition as above satisfies

`boxed: ||p_Q||_infinity <363.`                                    (4.1)

The punctured near-null part actually satisfies `<147.530`.

By scaling, if the three nonzero eigenvalues have modulus at least `s0>0`, the same statements hold with the right-hand sides divided by `s0`, and the pivot threshold `1/32` replaced by `s0/32`.

## 5. Why this does not solve the full collar

The exact source separation is a real hypothesis. In a general Parseval frame the residual rows have simultaneous longitudinal and transverse components

`u_j=t_j r+alpha_j v+beta_j q`.

Then the natural longitudinal aggregate shares ORIGINAL coordinates with `(C,D)`. Replacing it by an independent scalar would be exactly the live forbidden move “conditional density cap => independence.” Smallness of `epsilon` also cannot justify deleting `epsilon Y^2`, because the source class has no moment or support bound.

Thus the unresolved state after this run is the **overlapping-source** version of the partner collar. The source-separated theorem identifies the missing currency precisely: not spectral curvature, which is already forced by (3.5) and the inverse certificate (3.15), but product provenance when the longitudinal and transverse residual projections use the same original coordinates.

The fresh grouped-projection theorem in `interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` is compatible with this diagnosis: it pays many grouped hub/crossing configurations while preserving product provenance, but explicitly does not guarantee a uniformly nondegenerate split in the remaining small-leak geometry.

## 6. Literature/prior-solution status

The primary marginal-density theorem above matches exactly the bounded-density product assumptions used here. A targeted search also checked Juškevičius--Lee's sharp rearrangement theorem for sums of independent bounded-density variables; it is useful only when genuine independent summands are already present and does not manufacture independence among overlapping spectral projections.

I did not find an exact published theorem in the targeted search that directly supplies the full owner statement for arbitrary non-iid cap-one inputs and arbitrary symmetric `A` with three large eigenvalues. This is only a hypothesis comparison / search result, not a novelty claim.

## 7. Status

- full arbitrary-dimensional QFORM: **OPEN / NOT PROVED / NOT DISPROVED**;
- latest account02/B18 heavy-anchor reduction: applied literally;
- source-separated punctured collar: **PROVED HERE**, `<147.530`;
- source-separated exact-rank-three heavy-anchor branch: **COMPLETE after partner splice**, `<363`;
- overlapping-source punctured collar: **OPEN**;
- full-target continuity: **OPEN**;
- continuity on the new nonzero-pivot theorem: **NOT CLAIMED**.

No task identity, schedule, enabled/quiet state, notification/email setting, cross-account authentication, paid/remote call, public release, repository visibility, permission, or installation state was changed.
