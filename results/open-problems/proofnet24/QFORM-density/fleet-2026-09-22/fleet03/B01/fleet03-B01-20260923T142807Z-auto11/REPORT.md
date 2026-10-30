SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B01, 2026-09-23T14:28:07Z.
attacking: the singular/near-singular overlap-two star left by fleet04/B01, by preserving its diffuse leakage through a global diagonal-plus-low-rank completion and feeding that into a genuine one-hub integrated-Fourier receiver.

# B01 — no-conditioning low-rank completion and a signed-Fejer receiver for the overlap-two leakage branch

Status: **NEW SUPPORTING THEOREM + STRICT-N3 APPLICATION / FULL QFORM OPEN / CONTINUITY PROVED ONLY IN THE STATED BRANCH**.

Execution label: `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact sources used

Fresh owner controls keep all workers on `QFORM-DENSITY-3EIG-20260922`; the full unrestricted theorem remains open.

I use two completed results at equations.

1. **Designated partner fleet04/B01**, canonical proof
   `yspennstate/math-open-problems@8410ab9d8238baa40c033f83dbae6af44b0b2582`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B01/20260923T131003Z-fleet04-B01-singular-star-routing-r2/REPORT.md`.
   For a physical pair with `a!=0`, its scalar-Schur variables satisfy

   `W2=a^2 sum_{k!=l}(delta M_kl-ell_k ell_l)^2`,

   and hence either

   `|delta|^2 sum_{k!=l}M_kl^2 >= W2/(4a^2)`

   or

   `L(ell):=sum_{k!=l}ell_k^2 ell_l^2 >= W2/(4a^2)`.

   At the exact singular endpoint `det B=0`, `delta=0` and

   `L(ell)=W2/a^2`.

2. **One-hub determinant-balanced integrated Fourier receiver**, fleet02/B09, read at immutable snapshot
   `yspennstate/math-open-problems@b5f173477a3889ad9432ea7d97767e969c83b279`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T074200Z-fleet02-B09-QFORM-r13/REPORT.md`.
   If, after conditioning only disjoint original coordinates, a literal hub `h` has leaf block

   `D + sum_{s=1}^r lambda_s v_s v_s^T`, `r>=1`,

   and actual star `c`, then for the augmented frame `W=[v_1,...,v_r,c]`, with Gram matrix `G`, determinant-weighted disjoint-basis mass `rho>0`,

   `||p_Q||_infinity <= C_r [rho det(G) prod_s |lambda_s|]^(-1/(r+2))`,

   `C_r=((r+2)/r) exp((r+1)/(r+2))`.

   Its characteristic-function envelope is integrable uniformly over the conditioning variables, so this branch has a continuous `C_0` density.

I also use fleet04/B01's earlier exact signed-Fejer identity at
`yspennstate/math-open-problems@a3693ed6d50e8e4143b2f33bf997c5de2cb52d79`:

`||p_mu||_infinity = sup_{T>0,y} D_T mu(y)`

for laws with bounded density, with the usual nonnegative signed Fejer averages. This is used only after the density estimate below is proved.

No law-uniform pointwise quadratic-phase decay is used. The phase-aligned fragmented-support counterexample remains valid and is not weakened by this argument.

## 2. New algebraic lemma: global diagonal plus rank `<=4 dr(M)` with no conditioning

For a real symmetric matrix `M` on an original-coordinate leaf set `K`, define its **disjoint rank**

`dr(M)=max{k: exists disjoint S,R subset K, |S|=|R|=k, det M[S,R] !=0}`.

### Theorem 2.1 (`QFORM-GLOBAL-DIAG-RANK-COMPLETION-v1`)

If `dr(M)=k`, then

`M=D+C`

for a diagonal matrix `D` and a symmetric matrix `C` satisfying

`rank(C)<=4k`.

In particular, if every disjoint `5 x 5` minor vanishes, then `dr(M)<=4` and one has a **global**, no-conditioning representation

`M=D+C`, `rank(C)<=16`.

### Proof

The case `k=0` means every off-diagonal entry is zero, hence `M` is diagonal.

Assume `k>=1`. Choose disjoint sets `S,R` of size `k` with

`P=M[S,R]`

invertible. Put

`H=S union R`, `L=K\H`, so `|H|=2k`.

For distinct `i,j in L`, maximality of `k` forces the disjoint `(k+1)x(k+1)` minor with row set `S union {i}` and column set `R union {j}` to vanish. Schur expansion around `P` gives

`M_ij = M[i,R] P^{-1} M[S,j]`.

Define on `L`

`C_L=M[L,R]P^{-1}M[S,L]`.

Its off-diagonal entries equal those of the symmetric matrix `M[L,L]`; hence `C_L` itself is symmetric. Also `rank(C_L)<=k` and, crucially,

`range(C_L) subset range(M[L,R]) subset range(M[L,H])`.

Choose the diagonal matrix `D` by

`D_ii=M_ii-(C_L)_ii` for `i in L`,

and, say,

`D_hh=M_hh` for `h in H`.

Set `C=M-D`. Then `C` is symmetric,

`C[L,L]=C_L`, `C[L,H]=M[L,H]`.

Write `B_0=M[L,H]`. If `z in ker(B_0^T)`, then `z` is orthogonal to `range(B_0)`, hence to `range(C_L)`. Since `C_L` is symmetric, this implies `C_L z=0`. Therefore

`C (0,z)^T = (B_0^T z, C_L z)^T =0`.

Thus

`nullity(C) >= dim ker(B_0^T) >= |L|-|H|`.

Since the total dimension is `|H|+|L|`,

`rank(C) <= 2|H| =4k`.

This proves the theorem. `square`

This is stronger for the present purpose than conditioning a maximal pivot away: it keeps the entire physical star vector available to the analytic receiver.

## 3. New partner-compiled theorem for the leakage branch

Fix two original coordinates `i,j`, a disjoint original leaf bank `K`, and condition any genuinely outside original coordinates. Write the resulting physical quadratic block as

`A_core = [[a,b,u^T],[b,c,v^T],[u,v,N]]`, `a!=0`.

Define the scalar-Schur quantities

`delta = c-b^2/a`,

`ell = v-(b/a)u`,

`M = N-a^{-1}uu^T`.

Let `W2` be the fleet04/B01 overlap-two aggregate.

Assume the partner leakage branch

`L(ell)>=W2/(4a^2)`                                           (3.1)

and assume every disjoint `5 x 5` minor of `M` vanishes. By Theorem 2.1,

`M=D+C_0`, `rank(C_0)<=16`.

Hence the **actual**, not Schur-completed, leaf block is

`N=M+a^{-1}uu^T = D+C`,

where

`C=C_0+a^{-1}uu^T`, `r:=rank(C)<=17`.                          (3.2)

Now condition only on the ORIGINAL coordinate `X_i` and on the already outside coordinates. The remaining `(X_j,X_K)` quadratic part is exactly

`c X_j^2 +2X_j v^T X_K + X_K^T(D+C)X_K + affine terms`.       (3.3)

This is a literal one-hub problem. No spectral rotation of the random vector has occurred; conditioning on `X_i` changes only affine terms.

Assume `r>=1`. Let `lambda_1,...,lambda_r` be the nonzero eigenvalues of `C`, choose an orthonormal eigenframe for `range(C)`, and put

`theta=dist(v,range(C))`.

Let `rho` be the determinant-weighted probability that two iid bases of the whitened augmented frame `[v_1,...,v_r,v]` are disjoint. If `theta>0` and `rho>0`, fleet02/B09 applies to (3.3), uniformly in all conditioning variables, and gives

`boxed:
 ||p_Q||_infinity
 <= C_r [rho |pdet(C)| theta^2]^(-1/(r+2)),
 C_r=((r+2)/r)exp((r+1)/(r+2)), r<=17.`                        (3.4)

The full law has a continuous `C_0` density in this branch.

### Quantitative use of the designated partner

Suppose in addition that for some `tau in (0,1]`,

`theta >= tau ||ell||_2`.                                     (3.5)

Because

`||ell||_2^4 = sum_k ell_k^4 + L(ell) >= L(ell)`,

partner inequality (3.1) yields

`theta^2 >= tau^2 ||ell||_2^2
          >= tau^2 sqrt(W2)/(2|a|)`.                          (3.6)

Substituting (3.6) into (3.4) gives the explicit overlap-two averaged receiver

`boxed:
 ||p_Q||_infinity
 <= C_r [rho |pdet(C)| tau^2 sqrt(W2)/(2|a|)]^(-1/(r+2)),
 r<=17.`                                                       (3.7)

If the physical pair is exactly singular, `det [[a,b],[b,c]]=0`, fleet04/B01 gives the exact identity `L(ell)=W2/a^2`, and the factor `2` disappears:

`boxed:
 ||p_Q||_infinity
 <= C_r [rho |pdet(C)| tau^2 sqrt(W2)/|a|]^(-1/(r+2)).`        (3.8)

Equations (3.7)--(3.8) are the requested actual application of the designated partner's completed result. They pay a piece of the near-singular overlap-two star without dividing by the physical pair determinant and without conditioning away the diffuse leakage vector.

## 4. Signed-Fejer / averaged-frequency formulation

Apply fleet04/B01's exact signed-Fejer identity to (3.7). In the same branch,

`boxed:
 sup_{T>0,y} D_T law(Q)(y)
 <= C_r [rho |pdet(C)| tau^2 sqrt(W2)/(2|a|)]^(-1/(r+2)).`     (4.1)

At the exact singular endpoint, replace the denominator by

`rho |pdet(C)| tau^2 sqrt(W2)/|a|`.                            (4.2)

This is a genuine frequency-averaged replacement for the false pointwise `|t|^{-1/2}` scalar bound. The proof never asserts such a pointwise scalar estimate.

## 5. Strict-N3 diffuse family actually paid by the new branch

The theorem is not only a localized finite-core statement. It pays a strict no-pivot family.

Let `m>=64` be even. On the leaf bank `K={1,...,m}`, define orthonormal flat vectors

`w=m^{-1/2}(1,...,1)`,

`e=m^{-1/2}(1,...,1,-1,...,-1)`

with `m/2` plus signs and `m/2` minus signs. Put `epsilon=1/16` and define the `(m+2)x(m+2)` symmetric matrix

`A_m = [[epsilon,epsilon,0^T],
        [epsilon,epsilon,2e^T],
        [0,2e,ww^T]].`                                        (5.1)

### 5.1 It is a genuine three-large-eigenvalue target

The vector `w` is an eigenvector with eigenvalue `1`. On `span{i,j,e}`, the matrix is

`H=[[epsilon,epsilon,0],[epsilon,epsilon,2],[0,2,0]]`.

Relative to

`H_0=[[0,0,0],[0,0,2],[0,2,0]]`,

whose eigenvalues are `-2,0,2`, the perturbation has operator norm `2epsilon=1/8`. Weyl therefore gives one eigenvalue of `H` in `[-17/8,-15/8]` and one in `[15/8,17/8]`. Together with the eigenvalue `1` on `w`, `A_m` has at least three eigenvalues of absolute value at least one.

### 5.2 It lies in a fixed strict N3/no-pivot regime

Take the no-pivot threshold `tau_0=1/8`. Every physical diagonal is smaller than `1/8`:

`A_ii=A_jj=1/16`, leaf diagonals are `1/m`.

Every physical `2x2` principal determinant also has magnitude below `1/8` for `m>=64`:

- pair `{i,j}`: determinant `0`;
- pair `{i,k}`: `epsilon/m`;
- pair `{j,k}`: `epsilon/m-4/m=-(63/16)/m`;
- two leaf coordinates: determinant `0`.

Hence this is a strict fixed-threshold N3 family even though the target spectrum is present.

### 5.3 Partner resource and exact averaged bound

Here

`a=b=c=epsilon`, `u=0`, `v=ell=2e`, `delta=0`, `M=N=ww^T`.

Thus the physical pair is exactly singular and

`Omega_5(M)=0`, `rank(M)=1`.

The partner identity gives

`W2=a^2 L(ell)`.

Since every coordinate of `ell` has square `4/m`,

`L(ell)=16(1-1/m)`,

and therefore

`W2=(1/16)(1-1/m)`.                                           (5.2)

Conditioning the original coordinate `i` leaves a one-hub form with low-rank leaf curvature `C=ww^T`, so

`r=1`, `|pdet(C)|=1`, `theta=dist(2e,span{w})=2`, `tau=1`.

For the whitened augmented frame `[w,e]`, the Pluecker basis law is uniform on pairs containing one plus-row and one minus-row. Consequently two iid bases are disjoint with exact probability

`rho=(1-2/m)^2`.                                               (5.3)

The direct one-hub theorem gives

`||p_Q||_infinity
 <=3e^(2/3)[4(1-2/m)^2]^(-1/3)`.                              (5.4)

Using only the partner-fed exact-null lower bound in (3.8) gives

`boxed:
 ||p_Q||_infinity
 <=3e^(2/3)
   [4(1-2/m)^2 sqrt(1-1/m)]^(-1/3)
 <3.770,
 m>=64 even.`                                                  (5.5)

The same `<3.770` bound holds for every signed Fejer average `D_T law(Q)(y)`. The density is continuous on this family.

This family shows why the aggregate overlap-two star is useful: every individual physical pivot is small at fixed N3 scale, while the diffuse aggregate `W2` stays of order one and the global no-conditioning completion preserves it.

## 6. Preserved obstruction and exact remaining gap

The phase-aligned fragmented-support construction remains a counterexample to any law-uniform pointwise positive-power quadratic Fresnel decay: for a prescribed frequency `s`, a cap-one density can be supported on finitely many components of `{x: dist(sx^2,2pi Z)<=delta}` with total mass one and `Re E exp(isX^2)>=cos(delta)`. Nothing above contradicts this.

The new result does **not** close all of the partner dichotomy. The first remaining implications are now explicit:

1. the partner alternative `|delta|^2 sum_{k!=l}M_kl^2 >= W2/(4a^2)`;
2. the leakage branch when the disjoint-five volume of `M` is nonzero but too small to be paid at target scale by the existing `D_5` receiver;
3. after the new global low-rank completion, the aligned endpoint
   `dist(v,range(C)) << ||ell||`, including `theta=0`;
4. the determinant-weighted disjointness endpoint `rho=0` (or quantitatively tiny `rho`).

These are genuine routing debts, not failures of the density theorem. In particular, no uniformly good fixed physical minor is assumed.

## 7. Independent-review status

This new global-completion lemma and its compiled receiver have **not** yet received the two independent end-to-end reviews required for a full candidate. The unrestricted QFORM conjecture remains OPEN.
