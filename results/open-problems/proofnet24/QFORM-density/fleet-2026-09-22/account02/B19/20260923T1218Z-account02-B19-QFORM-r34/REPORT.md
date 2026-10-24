SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B19, 2026-09-23T12:17:59Z.
attacking: the first global no-pivot gap M-BIG2 by an exact Theorem-H transverse-area payment, and the current account03/B19 TRIANGLE pair-near-coloop residue by a strict-N3 punctured stress family testing local-pivot forcing and the sqrt(det(I-K)) transfer loss.

# account02/B19 r34 — huge-direction hub payment and punctured pair-coloop sharpness

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: `ESSENTIAL_STEP_APPLIED + CANDIDATE_STRUCTURAL_IMPLICATION_REFUTED`; full target OPEN.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The target throughout is the exact owner target: independent real coordinates with densities at most one, arbitrary real symmetric A with at least three eigenvalues of modulus at least one, no moment/support/log-concavity assumptions, no diagonal-basis or post-rotation independence, and continuity treated separately.

## 1. Source-pinned proof graph entering this run

The current Claude continuation proof tree reduces arbitrary A by physical Schur pivots to three no-pivot problems. NP1 is paid. NP2 has one stated missing mechanism `M-BIG2`: a heavy physical hub whose leaf block can contain a huge eigen-direction, so the elementary hub-reduction lower bound can be swallowed by `|a| ||M_{-h,-h}||`. NP3 has the stated missing mechanisms `M-TW`, `M-PEEL`, `M-DEG`, `M-2H`, and `M-MH`; all other nodes of that source tree are marked proved. This is source-pinned at the current `architecture/PROOF_TREE.md` continuation of the owner-required Claude source.

Inside the fleet's exact-rank-three/rank-two-cross NP3 subgraph, the current named partner account03/B19 r33 starts from

`A=R M R^T`, `R^T R=I_3`, `s_min(M)>=1`, an ORIGINAL-coordinate split `I union J`, `rank G=3`, `rank H=2`,

`rho=s_1(A[I,J]) s_2(A[I,J]) >= rho_0 := sqrt(29/3072)`,

and a physical TRIANGLE pair `T subset J`, with normalized pair covariance `K` satisfying

`d:=det K > d_0:=377/1344`.

After literally moving T into the source, account03/B19 proves

`rho' >= rho sqrt(r_T)`, where `r_T:=det(I-K)`,

and, using the completed uniform near-null receiver, pays every `r_T>=1/64` by `||p_Q||_infinity<65`. Its exact residue is therefore the punctured/or exact physical pair-near-coloop state `r_T<1/64`. The parallel B19 STAR debt remains the two quantitative star channels plus a genuine leaf spectral source, with the earlier fixed rank-three cross-volume closure already refuted.

The proof graph used here is therefore:

ROOT arbitrary A
  -> physical pivot tree [proved]
     -> NP1 [paid]
     -> NP2 [first global missing gate M-BIG2]
     -> NP3
        -> light-row / D,D',D5 / physical-core / pivot exits [paid]
        -> exact-rank-three rank-two-cross compiler
           -> balanced/repartitioned branches [paid]
           -> TRIANGLE: r_T>=1/64 [paid <65]
                        r_T<1/64 [open physical-pair near-coloop]
           -> STAR: grouped two-channel + leaf-source payment [open]
        -> remaining global NP3 gates M-TW/M-PEEL/M-DEG/M-2H/M-MH.

No step below promotes an exact-rank-three result to arbitrary extra spectrum.

## 2. First-gap payment: one huge leaf direction transverse to a physical hub

The owner-required Claude `RESULTS.md` proves Theorem H. I record the following direct corollary because it pays a real, previously explicit piece of `M-BIG2`.

### Theorem 2.1 — `QFORM-MBIG2-ONEEIG-TRANSVERSE-AREA-v1`

Split ORIGINAL coordinates as `{h} union I union J`. Assume

`A_II = Lambda u u^T + D`,

where `Lambda !=0`, `u in R^I`, and D is diagonal. Put

`m=(A_{ih})_{i in I}`

and

`G = sum_{i in I} (u_i,m_i)^T (u_i,m_i)
   = [[||u||^2,<u,m>],[<u,m>,||m||^2]].`

Assume G is positive definite and every normalized augmented leverage obeys

`ell_i := (u_i,m_i) G^{-1} (u_i,m_i)^T <= 1/2.`

No restriction is imposed on `A_hh`, `A_hJ`, `A_IJ`, `A_JJ`, or any affine term. Then Q has a continuous density and

`|phi_Q(t)| <= 4 pi^(3/2) (|Lambda| det G)^(-1/2) |t|^(-3/2)`,

hence

`boxed: ||p_Q||_infinity <= 3*4^(2/3) (|Lambda| det G)^(-1/3).`      (2.1)

Numerically `3*4^(2/3)=7.559526299369...`.

#### Proof

Apply Theorem H with one physical hub `H={h}` and one Fresnel direction (`r=1`) equal to u. Its augmented rows are exactly `(u_i,A_{ih})=(u_i,m_i)`, and its Gram is G. The theorem gives

`|phi(t)| <= (2|t|)^(-1) (4 pi |t Lambda|)^(-1/2) (4 pi)^2 det(G)^(-1/2)`

`             = 4 pi^(3/2) (|Lambda|det G)^(-1/2) |t|^(-3/2).`

With `K=4 pi^(3/2)(|Lambda|detG)^(-1/2)`, integrate `min(1,K|t|^(-3/2))`:

`integral_R min(1,K|t|^(-3/2)) dt = 6 K^(2/3)`.

Fourier inversion gives `(2pi)^(-1)6K^(2/3)`, which simplifies to (2.1). The theorem is uniform in the arbitrary blocks listed above, so conditioning on J and all affine shifts is already included. QED.

If `||u||=1` and `m=m_parallel+m_perp` relative to u, then

`det G = ||m_perp||^2`.

Thus the huge-direction branch is paid whenever

`|Lambda| ||m_perp||^2 >= eta>0`,

with

`||p_Q||_infinity <= 7.55953 eta^(-1/3).`                           (2.2)

Consequently, in the exact one-huge-direction-plus-diagonal model, a still-unpaid `M-BIG2` state must be one of two genuinely narrower geometries: an augmented-frame heavy coordinate (`ell_i>1/2`), or alignment of the physical hub coupling to the huge leaf eigenvector at scale

`||m_perp|| = o(|Lambda|^(-1/2))`.

This is an exact product-coordinate statement; the small transverse component is not deleted perturbatively.

## 3. Punctured TRIANGLE stress family

The named partner leaves `r_T=det(I-K)<1/64`. A natural hoped-for next implication would be that this very strong two-coordinate near-coloop, together with the live rank-two cross determinant, forces a fixed physical scalar/pair pivot or that the pair-transfer cross determinant loses less than `sqrt(r_T)`. Both hopes are false.

### Theorem 3.1 — `QFORM-TRIANGLE-PUNCTURED-PAIRCOLOOP-TRANSFER-SHARPNESS-v1`

For every `tau>0` and every `r in (0,1/64)` there is an exact-rank-three target matrix A and an ORIGINAL-coordinate source/receiver split satisfying all of the following simultaneously:

1. `spec_nonzero(A)={a,1,-1}` with `a>=1`;
2. strict no-pivot inequalities
   `max_i |A_ii|<tau` and `max_{i!=j}|det A[{i,j},{i,j}]|<tau`;
3. the rank-two cross block obeys
   `rho=s_1(A[I,J])s_2(A[I,J]) >= sqrt(15/16)/(4sqrt2)=0.1711632992... > rho_0`;
4. there is a physical TRIANGLE pair `T subset J` whose normalized covariance is
   `K=(1-sqrt(r)) I_2`, hence
   `det K=(1-sqrt(r))^2>49/64>d_0` and `det(I-K)=r`;
5. after moving T from receiver to source, the new cross product is

   `rho' = sqrt(r)/(4sqrt2) * sqrt(1-sqrt(r) h)`,

   while

   `rho sqrt(r) = sqrt(r)/(4sqrt2) * sqrt(1-h)`.

   Therefore

   `rho'/(rho sqrt(r)) = sqrt((1-sqrt(r)h)/(1-h)) -> 1`

   as `h->0`. The partner's `sqrt(det(I-K))` cross-loss is asymptotically sharp on a target-valid strict-N3 family.

In particular, no universal implication of the form

`TRIANGLE pair-near-coloop + rho>=rho_0 => fixed scalar/pair pivot`

can be true, even throughout the punctured interval `0<det(I-K)<1/64`.

#### Construction and proof

Work in an orthonormal three-dimensional spectral basis `(e_u,e_v,e_w)` and take

`M = [[a,0,0],[0,0,1],[0,1,0]],`                                  (3.1)

whose eigenvalues are `{a,1,-1}`. Build an isometric row frame R using three disjoint ORIGINAL-coordinate ray banks U,V,W, rows in the three banks being scalar multiples of `e_u,e_v,e_w`, respectively, with total squared coefficient one on each ray. Then `R^T R=I_3` and `A=RMR^T` has exactly the nonzero spectrum above.

Put `epsilon=sqrt(r) in (0,1/8)` and choose a large enough that

`a>=1`, `1/(16a)<tau`.

Set

`h=1/(16a^2)`.

Receiver U-mass is h: one distinguished physical coordinate `t_u` has squared coefficient `(1-epsilon)h`, and the residual receiver U-mass is `epsilon h`. Source U-mass is `1-h`, distributed over `N_u` physical coordinates so that

`a(1-h)/N_u < tau`.

Receiver V-mass is `1/2`: a distinguished coordinate `t_v` has squared coefficient `(1-epsilon)/2`, and residual receiver V-mass is `epsilon/2`. The remaining V-mass `1/2` is on the source side. All W-mass is source-side and is distributed over `N_w` rows with

`1/(2N_w)<tau`.

Take `T={t_u,t_v}`. The receiver spectral Gram is

`H=diag(h,1/2,0)`.

Whitening on `W=span(e_u,e_v)` sends the T rows to

`sqrt(1-epsilon)e_u`, `sqrt(1-epsilon)e_v`,

so

`K=(1-epsilon)I_2`, `det K=(1-epsilon)^2`, `r_T=epsilon^2=r`.       (3.2)

The source-to-receiver cross block is the orthogonal direct sum of two rank-one blocks. The U-to-U block has singular value

`a sqrt(h(1-h)) = (1/4)sqrt(1-h)`,

and the W-source to V-receiver block has singular value `1/sqrt2`. Hence

`rho = sqrt(1-h)/(4sqrt2) >= sqrt(15/16)/(4sqrt2)>rho_0`           (3.3)

because `a>=1` gives `h<=1/16`.

After moving T to the source, residual receiver masses are `epsilon h` on U and `epsilon/2` on V. The two cross singular values become

`a sqrt(epsilon h(1-epsilon h)) = (sqrt(epsilon)/4)sqrt(1-epsilon h)`

and `sqrt(epsilon/2)`, so

`rho' = epsilon/(4sqrt2) sqrt(1-epsilon h)`,                       (3.4)

which proves item 5 and the asymptotic sharpness.

It remains to verify strict N3. A U-row with coefficient alpha has diagonal `a alpha^2`; the distinguished and residual receiver U diagonals are respectively `(1-epsilon)/(16a)` and `epsilon/(16a)`, and source U rows are below tau by choice of `N_u`. V- and W-diagonals are zero. Every two-row principal determinant vanishes except a V-W pair; for such a pair it is `-(beta gamma)^2`. Since every V coefficient has square at most `1/2` and every W coefficient has square `1/N_w`, its modulus is at most `1/(2N_w)<tau`. Thus all scalar and pair pivots can be made arbitrarily small while (3.2)-(3.3) remain fixed. QED.

## 4. Apply the required Claude result to the actual obstruction

The stress family is not a counterexample to QFORM. In fact it is exactly the sort of geometry for which Theorem H sees the correct grouped currency before the partner's pair transfer.

Take the physical hub to be `t_v`. Take the Theorem-H leaf set I_H to consist of all source U rows and all W rows; condition on every other original coordinate. On I_H,

`A_{I_H,I_H} = a u u^T`

with no non-diagonal residual besides that rank-one square. The hub column on I_H is zero on U and equals `beta_h gamma` on W, where

`beta_h^2=(1-epsilon)/2`.

The augmented two-dimensional Gram is therefore diagonal:

`G_H = diag(1-h,(1-epsilon)/2)`.

Choose the U and W source banks with at least two equal atoms (and, for strict N3, in fact many more), so every augmented leverage is at most `1/2`. Theorem 2.1 gives

`||p_Q||_infinity
 <= 3*4^(2/3) [a(1-h)(1-epsilon)/2]^(-1/3).`                       (4.1)

Uniformly for `a>=1` and `epsilon<1/8`,

`a(1-h)(1-epsilon)/2 >= (15/16)(7/8)/2 =105/256`,

hence

`boxed: ||p_Q||_infinity < 10.174463.`                             (4.2)

This is an equation-level application of the owner-required source `math-open-problems@e5f71d79.../RESULTS.md`, Theorem H. It preserves the original-coordinate product law; the spectral basis in (3.1) is only a deterministic representation of A, not a declaration that rotated random variables are independent.

So the new family proves three things at once:

- the physical pair-near-coloop residue does not force a local scalar/pair pivot;
- the `sqrt(r_T)` loss in account03/B19's transfer bound is asymptotically sharp;
- the same residue can nevertheless be easy when one spends the whole physical hub + one diffuse square packet by Theorem H before transferring the near-coloop pair.

## 5. Concrete regression point

Take `tau=0.01`, `r=1/256`, `epsilon=1/16`, `a=10`, `h=1/1600`, `N_u=1000`, `N_w=51`. Then

`det K=0.87890625`, `r_T=0.00390625`,

`rho=0.17672144394498`,

`rho'=0.01104832766207`,

`rho'/(rho sqrt(r_T))=1.0002931090`,

`max_i |A_ii|=0.00999375<tau`,

`max_pair |det| <= 1/(2N_w)=0.00980392157<tau`,

and (4.1) gives `||p_Q||_infinity<4.518` at this concrete point.

## 6. First unpaid implications after this run

### Global first gap

The source proof tree's first genuinely open no-pivot mechanism remains `M-BIG2` in full generality, but Theorem 2.1 removes its exact one-huge-direction-plus-diagonal, transverse/diffuse subbranch. The first unpaid implication in that model is now:

`QFORM-MBIG2-ALIGNED-OR-HEAVY-AUGMENTED-v1`:

For a no-pivot two-large-eigenvalue node with a physical heavy hub h and leaf block `Lambda uu^T+D`, pay uniformly the states in which either the augmented `(u,m)` frame has a leverage `>1/2` or `|Lambda| det G` is arbitrarily small; equivalently for normalized u, the remaining diffuse obstruction is `||m_perp||=o(|Lambda|^{-1/2)`. For a general leaf block, one must first reduce its huge spectral part to this one-direction model or spend its additional directions by D_k/LF.

(The closing parenthesis in the display should read `o(|Lambda|^{-1/2})`; no asymptotic statement beyond that scale is intended.)

### Current named-partner TRIANGLE gap

`QFORM-TRIANGLE-PHYSICAL-PAIR-NEARCOLOOP-v2` remains open in general:

`rho>=rho_0`, `det K>d_0`, `0<=det(I-K)<1/64`, arbitrary cap-one product inputs and arbitrary compatible same-bank curvature. The stress family above proves that neither a universal local-pivot threshold nor an r-independent strengthening `rho'>=c rho` after pair transfer can close it. A successful closure must spend additional grouped curvature/hub structure before or together with transfer, as Theorem H does in the ray model, or descend product-preservingly to another already-paid mechanism.

The parallel STAR grouped two-channel/leaf-source debt and the global NP3 missing gates remain. Arbitrary-extra-spectrum closure is not obtained from any exact-rank-three statement here. Full-target continuity remains OPEN. There are not two independent end-to-end reviews, so no full-proof claim is made.

## 7. No-go audit

No step uses moment/support/log-concavity hypotheses, an arbitrary-joint coarea bound, post-rotation independence, worst-fibre conditional density caps, law-uniform coefficient perturbation continuity, or a universally good local/cross minor. The spectral ray notation in the stress construction is implemented by disjoint ORIGINAL-coordinate row banks. The small but nonzero punctured remainder is retained exactly; it is not discarded by continuity.
