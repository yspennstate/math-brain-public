SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B12, 2026-09-24T03:18:41Z.
attacking: aggregate resonance-versus-transverse-volume control for arbitrary signed added eigenvalue packets, using a protected original-coordinate domain and an exact rank-one angle shield.

# fleet01/B12 — protected-domain rank-one spectral shield

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Run: `20260924T031841Z-fleet01-B12-QFORM-auto11`  
Status: **PROVED SUPPORTING STABILITY THEOREM / FULL QFORM OPEN**  
Continuity: **not proved by this branch; the conclusion below is essential boundedness.**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and purpose

The full target remains: for arbitrary independent real inputs with one-dimensional probability densities at most one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal bound on the density of `X^T A X`, or give a valid counterexample.

This report does not rotate the random vector, does not declare spectral coordinates independent, and does not treat a small coefficient matrix as a small random quadratic error. It proves a deterministic coefficient-matrix stability result that is compatible with original-coordinate conditioning.

The new mechanism is a **protected domain**. One first chooses a subspace `E` inside an ORIGINAL-coordinate bank `H`. Arbitrarily many large signed spectral modes whose local projections are orthogonal to `E` vanish *exactly* on that protected domain, whatever their signs or magnitudes. The remaining active rank-one spectral modes are controlled by an exact amplitude-free angle inequality: their current eigenvalue amplitude disappears from the lower bound as soon as the eigenvector retains transverse component to the current carrier range.

This is complementary to the fleet02/B12 annihilator theorem, which removes a hostile physical row plane on the left. Here the large packet is first killed on the **domain/right side**, and then the residual active mode is controlled by its transverse angle in the ambient codomain. The resulting actual seven-mode final-matrix inequality is then fed into the fleet02/B12 density compiler.

## 2. Rank-one angle shield

Let `M` be a real `p x d` matrix, `p>=d`, with full column rank. Let `a in R^p`, `b in R^d`, and for arbitrary `theta in R` put

`M_theta = M + theta a b^T`.                                    (2.1)

Let `R(M)` denote the column range of `M`, and define, for `a!=0`,

`alpha(M,a) = dist(a,R(M))/||a|| in [0,1]`.                    (2.2)

If `a=0` define `alpha=1`, since the update vanishes.

### Theorem 2.1 — `QFORM-TRANSVERSE-RANKONE-ANGLE-SHIELD-v1`

For every real `theta` and every `b`, with **no sign or magnitude restriction**,

`boxed: s_d(M + theta a b^T) >= alpha(M,a) s_d(M).`             (2.3)

In particular, if `alpha(M,a)>=eta>0`, the update can have arbitrarily large positive or negative amplitude and still preserves at least the fraction `eta` of the smallest carrier singular value.

If `a in R(M)`, write `a=Mc`. Then the rank can drop only at the exact scalar resonance

`1 + theta b^T c = 0`.                                         (2.4)

Thus a rank-one update can truly collapse the carrier only when two things happen simultaneously: its left vector has **zero transverse component**, and its signed amplitude hits the corresponding longitudinal resonance.

### Proof of (2.3)

Put

`G=M^T M`, `N=M G^(-1/2)`.

Then `N^T N=I_d` and `M=N G^(1/2)`. Decompose

`a=Nc+a_perp`,  `c=N^T a`,  `N^T a_perp=0`.                    (2.5)

Hence

`||a_perp||/||a|| = alpha(M,a)`.                               (2.6)

For any `x in R^d`, set the scalar

`z = theta b^T G^(-1/2)x`.

Then

`(M_theta G^(-1/2))x = Nx + z a`.                              (2.7)

For fixed `x`, allowing `z` to range over all real numbers can only decrease the right-hand norm. Therefore

`||Nx+za||^2`
` >= min_(t in R) ||Nx+t a||^2`
` = ||Nx||^2 - <Nx,a>^2/||a||^2`.                              (2.8)

Because `N` is an isometry and `<Nx,a>=<x,c>`, Cauchy--Schwarz gives

`||Nx+za||^2`
` >= ||x||^2 [1-||c||^2/||a||^2]`
` = ||x||^2 ||a_perp||^2/||a||^2`
` = alpha(M,a)^2 ||x||^2`.                                     (2.9)

Thus

`s_d(M_theta G^(-1/2)) >= alpha(M,a)`.                          (2.10)

Finally

`M_theta=(M_theta G^(-1/2))G^(1/2)`,

so the product inequality for smallest singular values gives

`s_d(M_theta) >= alpha(M,a) s_d(G^(1/2))`
`              = alpha(M,a) s_d(M)`.                           (2.11)

This proves (2.3).

If `a=Mc`, then

`M_theta=M(I+theta c b^T)`.                                    (2.12)

The matrix determinant lemma gives

`det(I+theta c b^T)=1+theta b^T c`,                             (2.13)

so rank loss is possible precisely at (2.4). QED.

### Remarks

1. The lower bound is **amplitude-free**: `theta` disappears completely.
2. No bound on `||b||` is needed.
3. When `a` is orthogonal to `R(M)`, `alpha=1`; the update cannot decrease the smallest singular value at all.
4. The theorem is deterministic linear algebra. It does not use any property of the input laws.

## 3. Sequential arbitrary signed packet

Suppose a carrier is updated by finitely many rank-one terms

`M_j = M_(j-1) + theta_j a_j b_j^T`, `j=1,...,R`.               (3.1)

If `theta_j=0`, `a_j=0`, or `b_j=0`, that update is invisible and we assign factor `beta_j=1`. Otherwise define

`beta_j = dist(a_j,R(M_(j-1)))/||a_j||`.                        (3.2)

Whenever all preceding carriers remain full column rank, Theorem 2.1 iterates to

`boxed: s_d(M_R) >= s_d(M_0) prod_(j=1)^R beta_j.`              (3.3)

Every `theta_j` may be positive or negative and arbitrarily large. The cost is geometric transversality, not spectral magnitude.

If some `beta_j=0`, (3.3) becomes silent, but (2.12)-(2.13) show the exact obstruction: an aligned mode actually collapses a direction only at its scalar resonance. Thus the reduction separates two genuinely different mechanisms:

- **transverse mode:** amplitude-free protection by (2.3);
- **aligned mode:** one-dimensional signed resonance, which can be handled separately by rank spending, a Woodbury/resonance estimate, or another completed receiver.

This is the promised resonance-versus-transverse-volume reduction for individual active modes.

## 4. Protected-domain spectral compiler

Now return to the symmetric quadratic-form coefficient matrix. Let `H` be a set of `m` ORIGINAL coordinates and let

`P_H^T : R^m -> R^n`

be the coordinate embedding. Choose a `d`-dimensional subspace `E subset R^H` and an isometry

`U:E_model=R^d -> R^H`, `U^T U=I_d`.                            (4.1)

For a symmetric baseline `A_0`, define the protected carrier

`M_0 = A_0 P_H^T U`,                                           (4.2)

an `n x d` matrix.

Let an arbitrary signed spectral packet be

`S_hi = sum_(j=1)^R theta_j v_j v_j^T`,                         (4.3)

where the `v_j` are orthonormal and the `theta_j` are arbitrary real numbers, with no sign or magnitude restriction. On the protected domain,

`S_hi P_H^T U`
` = sum_j theta_j v_j (U^T P_H v_j)^T`.                         (4.4)

Therefore every spectral mode satisfying

`P_H v_j perpendicular E`                                      (4.5)

has `U^T P_Hv_j=0` and vanishes on the protected domain **exactly**, regardless of `theta_j`.

For the remaining active modes, process (4.4) in any chosen order. Their left vectors are the unit eigenvectors `v_j`; their right vectors are

`b_j=U^T P_Hv_j`.                                               (4.6)

If `M_(j-1)` is the current protected carrier, define

`beta_j=dist(v_j,R(M_(j-1)))`                                  (4.7)

for active nonzero modes. Then (3.3) gives

`s_d((A_0+S_hi)P_H^T U)`
` >= s_d(M_0) prod_(j active) beta_j.                           (4.8)

All inactive large eigenvalues cost exactly zero, and every active large eigenvalue is charged only through a transverse angle; its signed magnitude is absent.

Now add an arbitrary-rank small signed spectral packet `E_low` whose entire spectrum lies in `[-h,h]`, so

`||E_low||_op<=h`,                                              (4.9)

and any further symmetric tail `T` for which only its action on the protected domain is controlled,

`||T P_H^T U||_op<=delta`.                                     (4.10)

The rest of `T`, including its outside-outside block, may be arbitrarily large. Weyl gives

`boxed:`
`s_d(A P_H^T U)`
` >= [ s_d(M_0) prod_(j active) beta_j - h - delta ]_+`,        (4.11)

where

`A=A_0+S_hi+E_low+T`.                                          (4.12)

Thus arbitrarily many **smaller** signed eigenvalues cost only the single operator threshold `h`, while arbitrarily many **larger** signed eigenvalues orthogonal to the protected physical domain cost zero, and the remaining active large eigenvalues are controlled by their transverse geometry rather than their amplitudes.

No transformed random input is used in (4.11). `E` is a deterministic test subspace used only to prove a singular-value certificate for the actual coefficient matrix.

## 5. From the protected domain to an actual original-coordinate seven-mode carrier

Take `d=7`. If the right side of (4.11) is `g>0`, then the restriction of the actual map `A P_H^T` to the seven-dimensional subspace `E` has smallest singular value at least `g`. By the min-max principle,

`s_7(A P_H^T) >= g`.                                           (5.1)

Since `A` is symmetric,

`s_7(P_H A)=s_7(A P_H^T)>=g`,                                  (5.2)

and hence

`lambda_7((A^2)[H,H]) >= g^2`.                                 (5.3)

This is an actual final-matrix ORIGINAL-coordinate carrier certificate.

## 6. Apply the completed fleet02/B12 theorem

The newest completed designated partner result consumed in this run is

`QFORM-ANNIHILATOR-COMPRESSED-SEVEN-MODE-SHIELD-v1`,

canonical source

`yspennstate/math-open-problems@8e8d72d622eea594469107df2bb98b37961bb776`,

`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260924T022114Z-fleet02-B12-QFORM-auto11/REPORT.md`.

Its actual-final-matrix compiler states that for an ORIGINAL-coordinate set `H`, `|H|=m>=7`, a seven-mode carrier lower bound `g>0` implies

`boxed:`
`||p_(X^T A X)||_(infinity,ess)`
` <= sqrt(24 pi m + 50 e)/g`.                                  (6.1)

Indeed the partner theorem writes the actual final split `A=[[C,B],[B^T,D]]`, uses

`s_3(C)^2+s_5(B)^2>=g^2`,                                      (6.2)

and compiles the physical-core and fifth-volume receivers. To apply it to (5.2), take the partner theorem's annihilator plane to be zero and its baseline to be the **actual final matrix**. Then its `g_V` is exactly `s_7(P_HA)>=g`. This is an equation-level use of the completed partner result, not a transfer through rotated random coordinates.

Combining (4.11), (5.2), and (6.1) proves the conditional end-to-end statement

`boxed:`
`g := s_7(M_0) prod_(j active) beta_j - h - delta >0`
` ==> ||p_(X^TAX)||_(infinity,ess) <= sqrt(24 pi m+50e)/g.`     (6.3)

## 7. Exact target-class family with arbitrarily many unbounded signed additions

Here is a concrete nontrivial family in the owner's exact target class.

Take an ORIGINAL-coordinate set

`H={h_1,...,h_9}`,                                              (7.1)

and seven further coordinates

`J={j_3,...,j_9}`.                                              (7.2)

Let the protected domain be

`E=span{e_(h_3),...,e_(h_9)}`, `d=7`.                           (7.3)

Define the symmetric baseline `A_0` by seven disjoint physical cross pairs

`A_0[h_k,j_k]=A_0[j_k,h_k]=4`, `k=3,...,9`,                    (7.4)

with all other baseline entries zero. Then

`M_0=A_0 P_H^T U`                                              (7.5)

has seven orthogonal columns, each of norm four, so

`s_7(M_0)=4`.                                                   (7.6)

### Arbitrarily many invisible large signed modes

Add any spectral packet

`S_parallel=sum_a tau_a w_a w_a^T`                             (7.7)

whose `w_a` are mutually orthonormal, are also orthogonal to the active vector `v_*` introduced below, and satisfy

`P_H w_a in span{e_(h_1),e_(h_2)}=E^perp`.                     (7.8)

The number of modes is unrestricted by this theorem except by ambient dimension; the `tau_a` may have arbitrary signs and arbitrarily large magnitudes. Because the full set `{w_a} union {v_*}` is orthonormal, the numbers `tau_a` and `theta` below are literal eigenvalues of the combined large added spectral packet. By (4.5),

`S_parallel P_H^T U=0`                                         (7.9)

exactly, so the whole packet costs zero.

### One genuinely active arbitrary signed mode

Add also

`theta v_* v_*^T`,

`v_*=(e_(h_3)+e_(j_3))/sqrt(2)`, `theta in R` arbitrary.        (7.10)

Before this update,

`R(M_0)=span{e_(j_3),...,e_(j_9)}`.                            (7.11)

Therefore

`dist(v_*,R(M_0))=1/sqrt(2)`.                                  (7.12)

Theorem 2.1 gives, uniformly for **every** positive or negative `theta`, including unbounded `|theta|`,

`s_7((A_0+S_parallel+theta v_*v_*^T)P_H^T U)`
` >= 4/sqrt(2)=2sqrt(2)`.                                      (7.13)

This is the key gain over a pure norm perturbation estimate: the coefficient `|theta|` is absent.

### Arbitrarily many small signed eigenvalues and a local-action tail

Now add any symmetric `E_low` of arbitrary rank with

`||E_low||_op<=1/8`,                                           (7.14)

so it may contain arbitrarily many positive and negative small eigenvalues and arbitrary eigenvectors. Add any further symmetric `T` satisfying only

`||T P_H^T U||_op<=1/8`.                                      (7.15)

No restriction is imposed on the part of `T` that annihilates the protected domain. In particular its outside-outside spectrum can be arbitrarily large.

By Weyl and (7.13), the actual final matrix satisfies

`g:=s_7(A P_H^T U)`
` >= 2sqrt(2)-1/4`
` = 2.5784271247461903...`.                                    (7.16)

Hence

`s_7(P_HA)>=g`.                                                 (7.17)

Moreover

`s_7(A)>=s_7(A P_H^T)>=g`,                                     (7.18)

so certainly

`boxed: s_3(A)>=g>1.`                                          (7.19)

Every matrix in this family therefore satisfies the owner's exact hypothesis of at least three eigenvalues of modulus at least one.

Apply the fleet02/B12 partner compiler with `m=9` and `g=2sqrt(2)-1/4`. Equation (6.1) gives

`||p_Q||_(infinity,ess)`
` <= sqrt(216 pi+50e)/(2sqrt(2)-1/4)`
` = 11.068535893466812...`.                                    (7.20)

Thus

`boxed: ||p_Q||_(infinity,ess) < 11.069`                        (7.21)

uniformly over:

- arbitrarily many invisible large signed modes satisfying (7.8), with unbounded magnitudes;
- the active eigenvalue `theta` in (7.10), for every real sign and magnitude;
- every arbitrary-rank small signed packet satisfying (7.14);
- every further symmetric tail satisfying only the protected-domain action bound (7.15).

The density bound is an essential-supremum statement. This branch does not establish a continuous representative.

## 8. What this resolves and what remains open

The new theorem gives a precise reduction for additional eigenvalues:

1. **large modes missing a protected original-coordinate domain are exactly free**;
2. **large active rank-one modes with transverse eigenvectors are amplitude-free**, even at arbitrary sign and unbounded magnitude;
3. an aligned active mode can truly collapse the carrier only at its exact one-dimensional signed resonance;
4. **all small signed modes together cost one operator threshold**, not one cost per eigenvalue;
5. after a seven-mode final carrier survives, the completed fleet02/B12 theorem gives a dependence-safe density bound on the actual quadratic form.

The full conjecture is nevertheless open. The missing structural implication is:

> Starting only from `s_3(A)>=1`, force a bounded ORIGINAL-coordinate bank `H` and a seven-dimensional protected domain `E` for which the large spectral packet is either mostly orthogonal to `E` or has quantitatively transverse active modes, **or** route failure of every such protected domain into one of the already-paid projected-crossing, grouped-bank/hub, ridge, physical-pair, half-Riesz, Schur, or diffuse-volume exits.

Nothing in this report proves that extraction. In particular, the theorem does not claim that `s_3(A)>=1` automatically supplies seven protected singular directions.

## 9. Source/correction integrity

Fresh source refresh before publication retained:

- `math-research-brain` main observed at `c39c94da8c37d039fc460c844f5f89b515ba7884` during the final prepublication refresh;
- live correction inbox blob `a884b835aba929c5376e6417ae5cfcd44c0f7a76`;
- current claims still mark `QFORM-FULL` and unrestricted continuity OPEN;
- the refuted pointwise quadratic-phase bound, arbitrary-joint coarea cap, conditional-density moment shortcut, naive fiber-sup, and independence-after-rotation mechanisms are not used here.

The partner theorem was read from its immutable canonical report before use. Repository transport is not native brain ingestion; execution status remains `WITHOUT_VERIFIED_BRAIN`.
