SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B10, 2026-09-24T03:50:22Z.
attacking: the punctured near-coloop mixed-row collar; preserve a universal physical hub star after the fleet04/B10 three-bank split and determine exactly what the arbitrary-rank projected-crossing receiver pays as the coloop leakage tends to zero.

# fleet03/B10 r27 — partner-conditioned star noncollapse and a sharp projected-crossing compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: rank-three coupled case  
Status: `NEW PRODUCT-PRESERVING QUANTITATIVE THEOREM / NEW PARTNER APPLICATION / EXACT LEAKAGE BARRIER / FULL EXACT-RANK3 OPEN / FULL QFORM OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Source boundary and live state


The immediate completed B10 source used is

`yspennstate/math-open-problems@70f02a787a432edc745fa632b80ecfff0cc2ef11`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B10/20260923T221626Z-fleet03-B10-QFORM-r25/REPORT.md`.

Its live near-coloop state is as follows. Write

`A=R M R^T`, `R^T R=I_3`, `sigma_min(M)>=1`, `D:=|det M|>=1`.      (1.1)

There is one ORIGINAL physical hub row

`u_0=sqrt(c)e`, `||e||=1`, `c>63/64`, `rho:=1-c in (0,1/64)`,      (1.2)

and leaf rows

`u_i=t_i e+p_i`, `p_i perpendicular e`,                            (1.3)

with exact Parseval identities

`sum_i t_i^2=rho`, `sum_i t_i p_i=0`, `sum_i p_i p_i^T=I_2`.       (1.4)

The remaining leaf branch has

`delta:=max_i ||p_i||^2 <1/61`.                                    (1.5)

Relative to `e direct_sum e^perp`, write

`M=[[alpha,m^T],[m,N]]`,                                            (1.6)

with `|alpha|<1/16`. The physical hub-to-leaf star is

`w_i=A_{0i}=sqrt(c)(alpha t_i+m.p_i)`.                              (1.7)

The exact-null point `alpha=0` is already paid uniformly by B10 r24; r25 gives the nonzero-pivot absolute-root estimate but it deteriorates like `|alpha|^{-1/4}`. The present run does not use either deterioration as a premise.

Two completed external inputs are applied at equations:

1. Designated partner fleet04/B10, `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`, source `yspennstate/math-open-problems@afdea9634d9e3f5fb09659da436292cf7dbe5b20`, path `proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B10/20260923T061725Z-fleet04-B10-QFORM-r4/REPORT.md`.
2. The checked arbitrary-rank grouped projected-crossing theorem, source `yspennstate/math-open-problems@d2f970d33fa7084f8de55412189402ac609e4da6`, path `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`. In its one-original-hub, `ell=2` specialization it gives

`||p_Q||_infinity <= 3*2^(7/6)*exp(1/3) (||w_J||^2 Z_2)^(-1/6)`    (1.8)

provided the projected-crossing two-volume row marginals are all at most `1/2`. Its proof is a joint original-product Fourier estimate and yields a continuous `C_0` density.

## 2. New designated-partner consequence: the surviving physical star cannot collapse

Apply fleet04/B10's theorem to the whole leaf bank. Here the full transverse Gram is `G=I_2`, the regression vector is zero by (1.4), and the regression residuals are exactly `t_i`. Hence there is a partition of ORIGINAL indices

`L=S disjoint_union Y disjoint_union Z`                             (2.1)

such that

`rho_S M(G_Y,G_Z) >= (2/81) rho`,                                  (2.2)

where `rho_S=sum_{i in S}t_i^2` and `M(H,K)=tr(adj(H)K)`.

Since `rho_S<=rho` and `M(G_Y,G_Z)<=det(G_Y+G_Z)<=1`,

`M(G_Y,G_Z)>=2/81`, `rho_S>=2rho/81`.                              (2.3)

Put `R_*=Y union Z` and `G_*=G_Y+G_Z`. Then

`det G_* >= M(G_Y,G_Z)>=2/81`,                                    (2.4)

and `0<=G_*<=I_2`; therefore

`lambda_min(G_*)>=2/81`.                                           (2.5)

The new point is to apply this not merely to the transverse geometry but to the **actual physical hub star** after conditioning on `X_S`.

Let `b_i=alpha t_i+m.p_i`, so `w_i=sqrt(c)b_i`. Since `sigma_min(M)>=1`,

`||m||^2=||Me||^2-alpha^2 >=1-alpha^2 >255/256`.                  (2.6)

On `R_*`,

`||(p_i.m)_{i in R_*}||_2^2=m^T G_* m
 >=(2/81)||m||^2 >85/3456`.                                       (2.7)

Also

`||alpha(t_i)_{i in R_*}||_2 <= |alpha|sqrt(rho)<1/128`.           (2.8)

Because `85/3456>25/1024`, (2.7)-(2.8) and the reverse triangle inequality give

`||b_{R_*}||_2 >5/32-1/128=19/128`.                               (2.9)

Multiplying by `c>63/64`,

`||w_{R_*}||_2^2
 > (63/64)(19/128)^2
 =22743/1048576
 >1/47`,                                                           (2.10)

where the last inequality is the exact integer check `22743*47=1068921>1048576`.

### Theorem 2.1 — `QFORM-PARTNER-CONDITIONED-STAR-NONCOLLAPSE-v1`

In the live r25 near-coloop state, the designated fleet04/B10 partition can be chosen so that after legally conditioning on the ORIGINAL bank `S`, simultaneously

`lambda_min(G_{Y union Z})>=2/81`,                                 (2.11)

`sum_{i in Y union Z} t_i^2 <=79rho/81`,                           (2.12)

and

`boxed: sum_{i in Y union Z} A_{0i}^2 >1/47.`                      (2.13)

Thus the punctured collar does **not** lose its hub-to-leaf linear curvature as `rho->0`; the unpaid endpoint is a genuinely phase/grouping problem, not star collapse. This is an actual inequality-level application of the designated partner result.

The previous fixed-hub triple packet also remains available:

`sum_{j in Y,k in Z}|det A_{ {0,j,k} }| >7/288`.                  (2.14)

## 3. A disjoint-volume coloring lemma tuned exactly to the `1/61` gate

For a leaf subset `I`, define its transverse two-volume

`V_2^perp(I):=det(sum_{i in I} p_i p_i^T)
 =sum_{i<k in I} det(p_i,p_k)^2`.                                  (3.1)

For a leaf subset `J`, define its full spectral three-volume

`V_3(J):=det(sum_{j in J} u_j u_j^T)
 =sum_{|T|=3,T subset J} det(u_T)^2`.                              (3.2)

From (1.4),

`V_2^perp(L)=1`, `V_3(L)=rho`.                                    (3.3)

For every fixed leaf index `a`, the Parseval identity in the transverse plane gives

`sum_{j!=a} det(p_a,p_j)^2=||p_a||^2`.                             (3.4)

Therefore for every triple `T`, the total transverse pair weight of pairs touching `T` is at most

`sum_{a in T}||p_a||^2 <3/61`,                                    (3.5)

so the pair weight disjoint from `T` is greater than `58/61`.

Now independently color every leaf `I` with probability `q=2/5` and `J` with probability `3/5`. Expanding (3.1)-(3.2), only a transverse pair and a spectral triple with disjoint index sets can appear simultaneously. Hence

`E[V_2^perp(I)V_3(J)]
 =q^2(1-q)^3
   sum_{P pair,T triple,P cap T=empty}
        det(p_P)^2 det(u_T)^2`.                                    (3.6)

Using (3.5) and then (3.3),

`sum_{P disjoint T}det(p_P)^2 det(u_T)^2
 >(58/61) sum_T det(u_T)^2
 =(58/61)rho`.                                                      (3.7)

Since `q^2(1-q)^3=108/3125`, some deterministic ORIGINAL-coordinate partition `L=I disjoint_union J` satisfies

`boxed: V_2^perp(I)V_3(J) > eta rho`,                              (3.8)

with

`eta:= (108/3125)(58/61)=6264/190625
 =0.03286032786885246...`.                                         (3.9)

As `V_3(J)<=rho` and `V_2^perp(I)<=1`, the same partition obeys the separate lower bounds

`V_2^perp(I)>eta`, `V_3(J)>eta rho`.                               (3.10)

The choice `q=2/5` maximizes `q^2(1-q)^3`; no constant was lost in this coloring step except the unavoidable exclusion of pairs touching the chosen triple.

## 4. Exact projected-crossing factorization

Fix a partition from Section 3. Let

`w_J=A_{0,J}`                                                       (4.1)

be the physical hub row restricted to `J`, let

`B=A_{I,J}`,                                                        (4.2)

let `Pi_J` be orthogonal projection in `R^J` onto `span(w_J)`, and define the projected light crossing

`C=B(I-Pi_J)`.                                                      (4.3)

Because (3.8) is positive and `M` is invertible, `w_J` is nonzero. Put

`Z_2:=e_2(CC^T)=sum_{i<k in I}det(C_{ {i,k}}C_{ {i,k}}^T)`.       (4.4)

### Lemma 4.1 — `QFORM-HUB-PROJECTED-CROSSING-PLUCKER-IDENTITY-v1`

One has the exact identity

`boxed: ||w_J||^2 Z_2
 =D^2 c V_2^perp(I)V_3(J).`                                        (4.5)

Moreover the `ell=2` volume marginal of a row `i in I` is exactly

`boxed: beta_i
 = [sum_{k in I,k!=i}det(p_i,p_k)^2]/V_2^perp(I).`                 (4.6)

#### Proof

For rows `B_i,B_k in R^J`, orthogonal projection away from `w_J` gives the standard Gram-volume identity

`||w_J||^2 det Gram(C_i,C_k)
 =det Gram(w_J,B_i,B_k)`.                                          (4.7)

Cauchy-Binet over triples `T subset J` turns the right side into

`sum_{|T|=3} det A_{ {0,i,k},T}^2`.                               (4.8)

Since `A=RMR^T` has exact rank three,

`det A_{ {0,i,k},T}
 =det(M) det(u_0,u_i,u_k) det(u_T)`.                               (4.9)

But `u_0=sqrt(c)e` and `u_i=t_i e+p_i`, hence

`det(u_0,u_i,u_k)^2=c det(p_i,p_k)^2`.                            (4.10)

Summing (4.7)-(4.10) first in `T` and then over `i<k` gives (4.5). If instead `i` is fixed and only `k` is summed, the same common factor `D^2 c V_3(J)/||w_J||^2` cancels against (4.5), giving (4.6). QED.

The important feature is that (4.5) spends **aggregate** Pluecker mass before any reciprocal individual minor is selected.

## 5. The `1/61` leaf gate automatically pays the projected-crossing marginal gate

From (4.6), (3.4), (1.5), and (3.10),

`beta_i
 <= ||p_i||^2/V_2^perp(I)
 < (1/61)/eta
 =190625/(61*6264)
 <1/2`.                                                            (5.1)

The last inequality is the exact integer comparison

`2*190625=381250 <61*6264=382104`.                                 (5.2)

Thus the seemingly separate `ell=2` row-marginal hypothesis in the checked projected-crossing theorem follows automatically from the B10 transverse-diffuse gate, with a small but strict margin.

Combining (4.5) and (3.8),

`||w_J||^2 Z_2 > eta D^2 c rho`.                                  (5.3)

Apply the one-original-hub, `ell=2` specialization (1.8). This proves:

### Theorem 5.1 — `QFORM-NEARCOLOOP-PROJECTED-CROSSING-COMPILER-v1`

Under (1.1)-(1.5), for every `rho>0` and **for arbitrary hub Rayleigh coefficient `alpha` and arbitrary signs of the three nonzero eigenvalues**, the law of `Q=X^TAX` has a continuous `C_0` density and

`||p_Q||_infinity
 <=3*2^(7/6) exp(1/3)
   (eta D^2 c rho)^(-1/6).`                                       (5.4)

In the live near-coloop normalization `c>63/64`,

`boxed: ||p_Q||_infinity
 <16.652 D^(-1/3) rho^(-1/6).`                                    (5.5)

No assumption on `alpha`, no scalar-pivot inversion, no rotated-coordinate independence and no support/moment regularity is used. All internal light quadratic terms, all light diagonals and all affine terms are permitted by the cited grouped-crossing receiver.

This is a genuine punctured-collar theorem, but it is **not** the universal endpoint required by the owner because its constant diverges as `rho->0`.

## 6. Why this mechanism cannot itself glue to the coloop endpoint

The `rho^{-1/6}` in (5.5) is not an artifact of the random coloring estimate. Every disjoint light set `J` satisfies

`V_3(J)<=V_3(L)=rho`.                                               (6.1)

By the exact identity (4.5), every one-hub/two-projected-crossing certificate of this precise disjoint form satisfies

`||w_J||^2 Z_2
 =D^2 c V_2^perp(I)V_3(J)
 <=D^2 c rho`.                                                      (6.2)

Thus a receiver whose only quantitative currency is `(||w_J||^2Z_2)^(-1/6)` necessarily sees the vanishing leaf three-volume when `rho->0`. In contrast, Theorem 2.1 proves that after the partner conditioning split the **physical star itself stays uniformly nonzero**, `||w_{Y union Z}||^2>1/47`, and the surviving transverse Gram stays uniformly nondegenerate.

Therefore the precise remaining B10 implication is narrower than r25:

`QFORM-OVERLAP-AWARE-STAR-PLUS-TRANSVERSE-RECEIVER-v1`:

> In the partner-conditioned original-coordinate state with `||w||^2>1/47`, `lambda_min(G_perp)>=2/81`, transverse row norms `<1/61`, and remaining longitudinal energy `<1/64`, prove a joint Fourier or real-variable density estimate that reuses the physical hub star together with the same-bank transverse curvature **without requiring a disjoint leaf three-volume**. It must remain uniform through `rho->0` and `alpha->0` and must preserve original-coordinate product provenance.

The exact-null mixed-Fresnel theorem demonstrates that such an overlap-aware endpoint is possible when `alpha=0`; (6.2) proves that the newest disjoint projected-crossing compiler alone cannot supply the missing uniform gluing.

## 7. A useful phase identity for the next receiver

For completeness, the heavy-coordinate quadratic chirp itself has a parameter-uniform Plancherel identity. If `f<=1` is a probability density and

`F_{t,a}(beta)=int f(h) exp(i t(a h^2+2 beta h)) dh`,               (7.1)

then for every `t!=0` and every real `a`,

`boxed: int_R |F_{t,a}(beta)|^2 d beta
 = (pi/|t|) int_R f(h)^2 dh
 <= pi/|t|.`                                                       (7.2)

Proof: as a function of `beta`, (7.1) is the Fourier transform of `e^{ita h^2}f(h)` evaluated at frequency `2t beta`; Plancherel and the change of variables give (7.2). The identity is exactly uniform in the hub square coefficient `a`. It provides one endpoint-stable half-power of Fourier integrability, but by itself is not yet the missing full `L^1_t` receiver; a second gain must be extracted jointly from the transverse product geometry rather than by taking a fiber supremum.

## 8. Deterministic regression checks

A fixed-seed numerical regression (seed `20260924`) generated an 800-leaf Parseval frame with `rho=0.01`, maximum transverse row norm squared `0.0139044646969<1/61`, and a random symmetric `M` with eigenvalues `1.2,-1.5,2.0` in a random basis. Checks were:

- Parseval Gram maximum error: `8.88e-16`.
- Identity (4.5): left `0.004327155379224149`, right `0.004327155379224153`, absolute discrepancy `4.34e-18`.
- Row-marginal identity (4.6): maximum discrepancy `6.18e-16`.
- Among 5000 deterministic-seed `q=2/5` colorings, one had `V_2^perp(I)V_3(J)=0.0003977362674473`, above the certified threshold `eta*rho=0.0003286032786885`.

These computations are regression checks only; Sections 2-7 are exact proofs.

## 9. Scope and status

- `QFORM-PARTNER-CONDITIONED-STAR-NONCOLLAPSE-v1`: **PROVED** in the live r25 state; designated partner result applied at (2.2)-(2.13).
- `QFORM-HUB-PROJECTED-CROSSING-PLUCKER-IDENTITY-v1`: **PROVED** exactly.
- `QFORM-NEARCOLOOP-PROJECTED-CROSSING-COMPILER-v1`: **PROVED** for every `rho>0` under the stated B10 diffuse-transverse gate; it yields a `C_0` density with explicit `rho^{-1/6}` height.
- Uniform endpoint `rho->0`: **OPEN**. Equation (6.2) proves this particular disjoint projected-crossing currency cannot be uniform.
- Arbitrary exact rank three: **OPEN**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Global continuity: **OPEN**; continuity is proved only in the scoped Fourier branches stated above.

No task identity, schedule, enabled/paused state, email/push setting, repository visibility, permission, paid API/Codex action, or cross-account authentication was changed.
