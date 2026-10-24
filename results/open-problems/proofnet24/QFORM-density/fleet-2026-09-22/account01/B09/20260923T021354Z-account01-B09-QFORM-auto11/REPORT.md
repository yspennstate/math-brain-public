SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B09, 2026-09-23T02:13:54Z.
attacking: the exact low-cut-rank hub/star survivor with arbitrary physical diagonal curvature; compile the star and clique-factor branches into source-valid mixed-frame estimates and isolate the genuinely aligned/heavy-row remainder.

# account01/B09 auto11 — exact cut-rank-one hub compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T021354Z-account01-B09-QFORM-auto11`  
Assignment: Bilinear block mechanism  
Status: **ESSENTIAL_STEP_APPLIED / NEW ROUTING THEOREM / FULL_TARGET_OPEN**  
Execution: **WITHOUT_VERIFIED_BRAIN**

The unrestricted conjecture remains OPEN. This report does not claim a universal proof. It closes the diffuse part of the exact physical cut-rank-one leaf geometry while retaining all diagonal same-bank curvature and all outside couplings. When the cut-rank classification is applied to the entire physical complement of one hub, it also excludes the triangle exception inside the strict no-pivot class `N3(1/128)`. The remaining exact low-cut-rank obstruction is either exact alignment or a frame whose transverse wedge is concentrated on at most three physical rows.

Fresh owner control at startup was QFORM-only, OWNER CONTROL revision `2026-09-22.15`. The live correction ledger was read before the proof. In particular nothing below uses pointwise law-uniform van der Corput decay, post-rotation independence, arbitrary-joint three-dimensional coarea, a conditional projection-height moment, deletion of small coefficients, or a single-good-minor implication.

## 1. Sources actually used

The structural source is my preceding theorem `QFORM-EXACT-CUTRANK1-CLASSIFICATION-v1`, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B09/B09-20260922T214429Z-r18/REPORT.md`.

It proves: if a symmetric matrix `S` satisfies

`rank S[L,R] <= 1` for every pair of disjoint physical coordinate sets `L,R`,

then its off-diagonal support is exactly one of:

1. a star;
2. a triangle; or
3. a clique plus isolated vertices, with exact factorization `S_ij=lambda v_i v_j` on the clique.

The analytic source is Theorem H of

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

For original-coordinate hubs `H`, a product leaf bank `I`, and

`A_II=D+sum_(k=1)^r lambda_k v_k v_k^T`

with `D` diagonal, it keeps `A_HH,A_HJ,A_IJ,A_JJ` arbitrary. With augmented rows

`rho_i=((v_k)_i : k<=r ; A_ih : h in H)`,
`G=sum_i rho_i rho_i^T`,

and `rho_i^T G^{-1}rho_i<=1/2`, it gives

`|phi_Q(t)| <= (2|t|)^(-|H|) prod_k(4 pi |t lambda_k|)^(-1/2)
               (4 pi)^(r+|H|) det(G)^(-1/2)`.

The newest designated partner account02/B09 run `20260923T004108Z-account02-B09-QFORM-auto11` specializes this at one hub and rank-one leaf curvature, proving

`||p_Q||_infinity <= 3*2^(4/3)
 [ |lambda| (||v||^2||c||^2-<v,c>^2) ]^(-1/3)`

under the same row-leverage condition, with arbitrary diagonal leaf curvature and arbitrary outside blocks retained. I apply that result below to the clique branch produced by the exact classification.

## 2. Exact frame identities: aggregate before reciprocal payment

For two real vectors `u,c` indexed by a physical leaf set `I`, set

`rho_i=(u_i,c_i) in R^2`,
`G=sum_i rho_i rho_i^T`,
`W=det G`.

Then Cauchy--Binet gives the exact aggregate identity

`boxed: W = ||u||^2||c||^2-<u,c>^2
             = sum_(i<j) (u_i c_j-u_j c_i)^2.`                 (2.1)

If `W>0`, define the normalized row leverage

`ell_i=rho_i^T G^{-1}rho_i`.

A two-dimensional adjugate calculation gives the second exact identity

`boxed: ell_i
 = [sum_(j != i)(u_i c_j-u_j c_i)^2]/W.`                       (2.2)

Indeed `rho_i^T adj(G)rho_i` equals the sum of the squared `2x2` determinants formed by `rho_i` with all other rows. Consequently

`sum_i ell_i=2`.                                                  (2.3)

Thus the condition `max ell_i<=1/2` is not an opaque Fourier hypothesis. It says that no single physical row carries more than half of the total transverse wedge energy (2.1). If it fails, at most three rows can have leverage above `1/2`, and every such row carries more than half of `W` through its incident wedge packet.

This is the exact aggregate-before-inversion currency used below.

## 3. New two-hub payment for an exact physical star

Let the original coordinates be split as

`{h,s} union I union J`,

where `h` is the outer hub, `s` is the center of a star in the leaf operator, and `I` contains all other star leaves. Assume only that `A_II` is diagonal. Put

`c=A[I,h]`, `b=A[I,s]`,
`rho_i=(c_i,b_i)`,
`G_star=sum_i rho_i rho_i^T`,
`W_star=det G_star`.

No restriction is imposed on the physical `2x2` hub block `A[{h,s},{h,s}]`, on any coupling to the conditioned bank `J`, on `A_JJ`, or on affine terms.

### Theorem 3.1 — `QFORM-TWOHUB-PHYSICAL-STAR-DIFFUSE-v1`

If

`W_star>0`,
`max_i rho_i^T G_star^{-1}rho_i <=1/2`,                       (3.1)

then `Q=X^TAX+linear+constant` has a bounded continuous density and

`boxed: ||p_Q||_infinity <= 4 W_star^(-1/4).`                 (3.2)

Hence every interval `L` satisfies

`boxed: P{Q in L} <= 4 W_star^(-1/4)|L|.`                     (3.3)

### Proof

Apply source Theorem H with the two actual source-coordinate hubs `H={h,s}`, rank parameter `r=0`, and product leaf bank `I`. Its hypotheses are exactly (3.1); all self-curvature in the leaf bank is diagonal and remains inside the complex one-coordinate amplitudes. Conditioning `J` changes only affine shifts and phases.

The source estimate becomes

`|phi_Q(t)| <= 4 pi^2 W_star^(-1/2)|t|^(-2)`.                 (3.4)

Together with `|phi_Q(t)|<=1`, put `K=4 pi^2 W_star^(-1/2)`. Then

`int_R min(1,K/t^2)dt = 4 sqrt(K)
                         =8 pi W_star^(-1/4)`.                 (3.5)

Fourier inversion gives (3.2). Since the characteristic function is integrable, the inverted density is continuous and vanishes at infinity. The bound is uniform under the outside conditioning, so averaging over `J` preserves it. QED.

The point is that the star curvature is not thrown into a worst conditional fiber. Its center `s` is promoted to a second **physical** hub, and the two source-coordinate arms are aggregated through the full wedge `W_star` before a reciprocal Jacobian is paid.

## 4. Exact cut-rank-one compiler around one outer hub

Fix one original-coordinate hub `h`, let `I` be a leaf set, and let `J` contain every remaining coordinate. Assume the off-diagonal part of `A_II` satisfies

`rank A[L,R] <=1`

for every disjoint `L,R subset I`. The r18 classification leaves star, triangle, or clique-factor geometry on this leaf set.

### 4.1 Star branch

If the leaf off-diagonal support is a star centered at `s in I`, put `I0=I\{s}`. Then `A[I0,I0]` is diagonal. Set

`b=A[I0,s]`, `c=A[I0,h]`.

If the two-vector frame `(b,c)` is nondegenerate and has row leverage at most `1/2`, Theorem 3.1 applies **with every coefficient involving the conditioned bank `J` arbitrary**:

`boxed: ||p_Q||_infinity
 <=4 (||b||^2||c||^2-<b,c>^2)^(-1/4).`                        (4.1)

This pays a genuine same-bank star without requiring the center-to-leaf coefficients to be selected one at a time.

### 4.2 Clique-factor branch — designated partner applied

If the leaf support contains two disjoint edges, the exact classification gives, after extending `v` by zero on isolated leaves,

`A_II=D+lambda v v^T`                                            (4.2)

for a diagonal matrix `D`. Let `c=A[I,h]` and

`G_cl=sum_i (v_i,c_i)^T(v_i,c_i)`,
`W_cl=det G_cl=||v||^2||c||^2-<v,c>^2`.                       (4.3)

If `W_cl>0` and every row leverage is at most `1/2`, apply the newest account02/B09 theorem at its actual inequality (rank `r=1`):

`boxed: ||p_Q||_infinity
 <=3*2^(4/3) [|lambda| W_cl]^(-1/3)
 <7.560 [|lambda|W_cl]^(-1/3).`                                (4.4)

This is not citation-only use of the partner result: (4.2), forced by the exact B09 cut-rank classification, is substituted into the partner's mixed-frame theorem, and the aggregate wedge (4.3) is exactly its determinant resource. The conclusion is a direct `O(|L|)` interval bound and a continuous density.

### 4.3 Global triangle branch is impossible in strict `N3(1/128)`

For this subsection only, take the leaf set to be the **entire physical complement** `I={1,...,n}\{h}` (so there is no unclassified outside bank). Also assume the strict sufficient no-pivot conditions

`|A_ii|<tau`,
`|det A[{i,j},{i,j}]|<tau` for every `i!=j`,                    (4.5)

with `tau=1/128`, and assume `s_3(A)>=1`.

Suppose the classified leaf off-diagonal support is a triangle. For any triangle edge `e=A_ij`,

`e^2=A_ii A_jj-det A[{i,j},{i,j}]`,

so

`|e|<q:=sqrt(tau+tau^2)`.                                      (4.6)

Let `S_h` be the hollow physical star consisting of all edges from the outer hub `h`; `rank S_h<=2`. Let `T_triangle` be the hollow three-vertex triangle matrix, and let `D0=diag(A)`. Because the classification is now on the full complement of `h`, there are no other leaf off-diagonal edges, hence

`A=S_h+(D0+T_triangle)`.                                       (4.7)

The triangle has maximum absolute row sum at most `2q`, while `||D0||_op<tau`. Therefore

`||D0+T_triangle||_op < tau+2q
 =1/128+2 sqrt(1/128+1/128^2)
 <0.186.`                                                      (4.8)

Since `S_h` has rank at most two, the Eckart--Young characterization gives

`s_3(A) <= ||A-S_h||_op <0.186`,                               (4.9)

contradicting `s_3(A)>=1`.

Thus the triangle exception from the exact graph classification is not part of the strict N3 target survivor when the cut-rank-one classification applies to the full leaf complement.

## 5. Resulting exact low-cut-rank frontier

Combining Sections 2--4 gives the new routing theorem.

### Theorem 5.1 — `QFORM-CUTRANK1-HUB-COMPILER-v1`

Inside strict `N3(1/128)`, fix an outer physical hub `h` and suppose every disjoint cross block of the off-diagonal operator on its **full physical complement** has rank at most one. Then the full target `s_3(A)>=1` cannot be in the triangle case. In the star and clique cases, the full ambient quadratic form is already paid with a bounded continuous density whenever the corresponding two-dimensional mixed frame has positive determinant and maximum row leverage at most `1/2`, by (4.1) or (4.4).

Therefore every still-unpaid exact cut-rank-one state in this global chamber is forced into one of only two mechanisms:

1. **exact alignment:** `W_star=0` or `W_cl=0`; or
2. **physical-row concentration:** `W>0` but some row has leverage `>1/2`.

By (2.2)--(2.3), the second mechanism means that one of at most three physical leaf coordinates carries more than half of the entire transverse wedge packet. This is a finite physical localization statement; it is not a single-minor selection and it does not lose the aggregate wedge mass.

This is materially narrower than “one hub with arbitrary within-bank curvature.” In the exact global low-cut-rank chamber, all diffuse star and clique curvature is now paid. Only the aligned/heavy-row compiler remains.

## 6. Target-valid stress family for the new star theorem

Let `m>=4` be even. Take two physical hubs `h,s` and one disjoint leaf bank `I` of size `m`. Let

`b=m^(-1/2)(1,...,1)`,
`c=m^(-1/2)(1,...,1,-1,...,-1)`,

with equal numbers of plus and minus signs, so `||b||=||c||=1` and `<b,c>=0`. Set all diagonal coefficients to zero and let the only nonzero entries be

`A[I,s]=b`, `A[I,h]=c`

and their transposes. Then in the four-dimensional grouped span generated by the two hubs and the two orthogonal leaf projections, the coefficient matrix is a direct sum of two hyperbolic `[[0,1],[1,0]]` blocks. Thus

`spec_nonzero(A)={1,-1,1,-1}`.                                  (6.1)

This is a genuine full-target family. Every physical edge is only `m^(-1/2)`, while

`G_star=I_2`, `W_star=1`,
`ell_i=b_i^2+c_i^2=2/m<=1/2`.                                  (6.2)

Theorem 3.1 gives for **every** admissible independent cap-one product law

`boxed: ||p_(X^TAX)||_infinity <=4,`                            (6.3)

and the density is continuous. The analytic bound remains valid if arbitrary diagonal curvature is inserted on the leaf bank and arbitrary outside blocks/couplings are attached, provided the stated star frame is retained; the target spectral condition is needed only when interpreting a particular instance as part of the global conjecture.

## 7. First unpaid implication

The first B09 implication is now

`QFORM-CUTRANK1-ALIGNED-OR-HEAVYROW-COMPILER-v1`:

> In strict N3, assume the full leaf off-diagonal operator has exact cut rank at most one and hence is star or clique-factor. Pay the branch where its mixed hub/curvature frame is either exactly aligned (`det G=0`) or has a row leverage above `1/2`. Use the exact identity
>
> `ell_i det G = sum_(j!=i)(u_i c_j-u_j c_i)^2`
>
> to elevate at most three heavy physical rows before any reciprocal-minor operation, and route the residual aligned bank to a completed physical-pair, grouped-square, zero-pair/two-slope, or additional-spectrum theorem. Do not perturbatively delete a nonzero hub edge or arbitrary same-bank curvature.

This is the correct next step on the SAME target. A source-valid counterexample already shows that a single aligned mixed frame may retain a logarithmic rank-two singularity, so the third target spectral resource must be preserved explicitly rather than conditioned away.

## 8. Continuity and status

Both newly compiled paid branches have integrable characteristic functions, hence bounded **continuous** densities. The full target remains OPEN, and the full-target continuity claim remains OPEN.

No email, scheduler mutation, task creation, public release, cross-account authentication, installation work, paid model/API call, or notification change was performed in this run.
