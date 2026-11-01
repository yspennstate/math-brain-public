# fleet01 / B12 — QFORM additional-eigenvalue control

Run: `20260923T121718Z-fleet01-B12-QFORM-auto11`

Status: **PROVED_SUPPORTING_STABILITY_FULL_TARGET_OPEN**

Native-brain status: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval/writeback is not native learned-memory ingestion.

## Exact programme target

For independent real random variables `X_i` with densities `0 <= f_i <= 1`, and a real symmetric matrix `A` having at least three eigenvalues of absolute value at least one, prove a universal bound on the density of `Q=X^T A X`, or give a valid counterexample. No rotated-coordinate independence is used below. The result in this report is a supporting stability theorem, not the unrestricted solution.

## New result: QFORM-SHARP-SPECTRAL-TAIL-HALF-ENERGY-v1

### 1. Exact physical cross-energy identity

Let

`S_B = sum_{a in B} tau_a v_a v_a^T = V Theta V^T`,

where the `v_a` are orthonormal and the real coefficients `tau_a` have arbitrary signs. Let `I,J` be disjoint sets of original coordinates. Write

`V_I=P_I V`, `V_J=P_J V`, `G_I=V_I^T V_I`, `G_J=V_J^T V_J`,

and let

`R=S_B[I,J]=V_I Theta V_J^T`.

Then exactly

`||R||_F^2 = tr(Theta G_J Theta G_I)`.                                      (1)

Proof: expand `RR^T` and use cyclicity of trace:

`tr(RR^T)=tr(V_I Theta V_J^T V_J Theta V_I^T)=tr(Theta G_J Theta G_I)`.

Since `0 <= G_J <= I`, congruence by `Theta` gives

`Theta G_J Theta <= Theta^2`.

Therefore

`||R||_F^2 <= tr(Theta^2 G_I)=sum_a tau_a^2 ||P_I v_a||_2^2`.              (2)

By symmetry,

`||R||_F^2 <= sum_a tau_a^2 ||P_J v_a||_2^2`.                              (3)

These are localized spectral-footprint estimates. They retain information that can be much sharper than the global spectral norm or global spectral Frobenius energy.

### 2. Universal half-energy estimate

Because `S_B` is symmetric, relative to the decomposition into the coordinate blocks `I,J,K=(I union J)^c`, the blocks `S_B[I,J]=R` and `S_B[J,I]=R^T` occur separately in its Frobenius norm. Hence

`||S_B||_F^2 >= ||R||_F^2+||R^T||_F^2=2||R||_F^2`.                         (4)

Orthogonality of the eigenvectors gives

`||S_B||_F^2=sum_a tau_a^2`.                                                (5)

Thus

`||R||_F <= (sum_a tau_a^2/2)^{1/2}`.                                      (6)

Define

`H_B=(sum_a tau_a^2)^{1/2}`

and

`E_B=min{ (sum_a tau_a^2||P_Iv_a||^2)^{1/2},
           (sum_a tau_a^2||P_Jv_a||^2)^{1/2},
           H_B/sqrt(2) }`.                                                  (7)

Then

`||R||_F <= E_B`.                                                           (8)

The factor `1/sqrt(2)` in the spectral-only term is universal and sharp; see Section 5.

### 3. Compiler with the completed fleet02/B12 reserve theorem

Let `M_0=A_0[I,J]` be a baseline original-coordinate cross block. Split an added symmetric spectral update as

`S=S_G+S_B`,

where `S_G` is any chosen packet of modes to be absorbed at no amplitude cost and `S_B` is the residual packet from Sections 1–2. Put

`L=S_G[I,J]`, `R=S_B[I,J]`,

and let

`r_G=rank(L) <= min{rank(V_{I,G}),rank(V_{J,G}),|G|}`.                      (9)

Let `T` be an arbitrary symmetric matrix with

`||T||_op <= delta`;                                                       (10)

there is no sign, rank, support, or separability restriction on `T`.

The completed `fleet02/B12` theorem `QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1` gives, for each integer `p>=0` for which the indicated singular value exists,

`s_5(M_final) >= s_{5+r_G+p}(M_0)-s_{p+1}(R)-delta`,                       (11)

where `M_final=(A_0+S+T)[I,J]`.

The elementary singular-value/Frobenius inequality gives

`s_{p+1}(R) <= ||R||_F/sqrt(p+1) <= E_B/sqrt(p+1)`.                        (12)

Therefore define

`Gamma_5(G,p) = s_{5+r_G+p}(M_0) - E_B/sqrt(p+1) - delta`.                 (13)

Whenever `Gamma_5(G,p)>0`, the completed D5 receiver theorem on the actual final original-coordinate cross block yields a **continuous** density and

`||p_{X^T(A_0+S+T)X}||_infty <= 5 sqrt(2e) / Gamma_5(G,p)`.                (14)

All random variables are kept in the original product coordinate system. In particular, no rotated eigen-coordinates are treated as independent, and `X^T S_B X` or `X^T T X` is never treated as an independent convolution remainder.

The bound can be optimized over the choice of free packet `G` and over `p`.

### 4. Global spectral-only corollary

Order the added spectral coefficients by magnitude:

`|tau_1| >= |tau_2| >= ...`.

Choose the first `k` modes as `G`, so `r_G<=k`, and set

`H_k=(sum_{a>k} tau_a^2)^{1/2}`.                                           (15)

Then (6), (12), and (11) give

`s_5(M_final) >= s_{5+k+p}(M_0) - H_k/sqrt(2(p+1)) - delta`.               (16)

Consequently, whenever

`Gamma_5(k,p):=s_{5+k+p}(M_0)-H_k/sqrt(2(p+1))-delta>0`,                   (17)

`Q` has a continuous density satisfying

`||p_Q||_infty <= 5 sqrt(2e)/Gamma_5(k,p)`.                                (18)

Interpretation: the first `k` added eigenvalues may be of arbitrary magnitude and either sign; their magnitudes disappear and they consume at most `k` reserve singular directions. Every remaining added eigenvalue may also have either sign. The entire residual spectral cloud is charged only through its `ell_2` spectral energy, diluted by the reserve depth and with the sharp symmetry factor `1/sqrt(2)`.

A fixed-reserve version is useful. If

`s_N(M_0)>=kappa`, `N>=r_G+5`,                                             (19)

choose

`p=N-r_G-5`, `ell=p+1=N-r_G-4`.                                           (20)

Then

`s_5(M_final) >= kappa-delta-E_B/sqrt(ell)`                                (21)

and, using only global spectral information,

`s_5(M_final) >= kappa-delta-H_B/sqrt(2ell)`.                              (22)

Each positive right-hand side feeds directly into the continuous D5 density bound.

### 5. Sharpness of the universal half-energy constant

Let `I` and `J` each have size `ell`, and take

`S_B = [[0,-a I_ell],[-a I_ell,0]]`, `a>0`.                               (23)

Its eigenvalues are `+a` and `-a`, each with multiplicity `ell`. Thus

`H_B=a sqrt(2ell)`.                                                        (24)

Its physical cross block is

`R=-a I_ell`,                                                              (25)

so

`||R||_F=a sqrt(ell)=H_B/sqrt(2)`.                                         (26)

Moreover, taking `p=ell-1`,

`s_{p+1}(R)=a=H_B/sqrt(2(p+1))`.                                           (27)

Thus neither the factor `1/sqrt(2)` in (6) nor the resulting spectral-only dilution factor in (16) can be universally improved if one uses only the global residual spectral `ell_2` energy and the index `p`.

### 6. Actual application of the completed fleet02/B12 theorem

This section applies the partner theorem to a concrete exact-target family, as required by the assignment.

Take original-coordinate banks `I,J`, each of size 64, and any number `m>=0` of spectator coordinates. On `H=I union J`, let

`A_0[H,H] = [[0,2I_64],[2I_64,0]]`,                                       (28)

and give each spectator baseline eigenvalue `+2` with no coupling to `H`.

For `j=1,...,64` define

`g_j=(e_j^I+e_j^J)/sqrt(2)`,
`q_j=(e_j^I-e_j^J)/sqrt(2)`.                                               (29)

Then `g_j` has baseline eigenvalue `+2` and `q_j` has baseline eigenvalue `-2`.

#### Arbitrarily many unbounded free signed replacements

Let `W` be the baseline `+2` eigenspace spanned by `g_1` together with the `m` spectator eigenvectors, and choose any orthonormal basis `z_1,...,z_{m+1}` of `W`. Add

`S_G=sum_{a=1}^{m+1} tau_a z_a z_a^T`,                                    (30)

with completely arbitrary `tau_a in R`.

Every restriction `P_H z_a` is a scalar multiple of `g_1`. Hence

`rank(S_G[I,J]) <= 1`,                                                     (31)

independently of `m` and independently of the signs and magnitudes of all the `tau_a`. Thus arbitrarily many arbitrarily large signed eigenvalue replacements are absorbed at the cost of one reserve direction on the physical cross block.

#### Residual signed cloud

For `j=2,...,60` set `ell=59` and add

`S_B=sum_{j=2}^{60}(-a g_j g_j^T + a q_j q_j^T)`, with `a=1/2`.            (32)

Each pair in (32) has zero `I,I` and `J,J` blocks and cross block `-a e_j e_j^T`. Thus

`R=S_B[I,J]` has exactly 59 singular values equal to `a=1/2`.              (33)

The residual spectral packet has 118 coefficients of modulus `a`, so

`H_B=a sqrt(118)`.                                                         (34)

The sharp half-energy bridge gives, at `p=58`,

`H_B/sqrt(2(p+1)) = a sqrt(118)/sqrt(118)=a=1/2`,                          (35)

and in this example equality holds:

`s_59(R)=1/2`.                                                             (36)

Finally add an arbitrary symmetric dense matrix `T` with

`||T||_op <= delta=1/4`.                                                   (37)

The baseline cross block is `M_0=2I_64`, the free physical cross rank is `r_G=1`, and take `p=58`. Then

`5+r_G+p=64`, `s_64(M_0)=2`.                                               (38)

The partner theorem therefore gives the actual inequality

`s_5(M_final) >= s_64(M_0)-s_59(R)-delta
               =2-1/2-1/4
               =5/4`.                                                     (39)

The completed D5 receiver yields a continuous density with

`||p_Q||_infty <= 5 sqrt(2e)/(5/4)=4 sqrt(2e)
                =9.326575926388497...`.                                  (40)

This is uniform in `m`, in every arbitrary signed amplitude `tau_a`, and in the arbitrary dense tail `T` subject only to (37).

The new half-energy theorem is genuinely sharper than the spectral-Frobenius bridge without the symmetry factor: the latter would charge

`H_B/sqrt(59)=a sqrt(2)`,                                                   (41)

whereas (35) charges exactly `a`.

#### Verification that the family is inside the exact target class

Before the dense tail, all 64 vectors `q_j` remain eigenvectors unaffected by `S_G`. For `j=2,...,60`, their eigenvalues are

`-2+a=-3/2`,                                                               (42)

while `q_1,q_61,...,q_64` retain eigenvalue `-2`. Thus the pre-tail matrix has at least 64 eigenvalues at most `-3/2`, independently of the arbitrary free amplitudes in (30). Weyl's inequality and (37) imply that after adding `T` at least 64 eigenvalues are at most

`-3/2+1/4=-5/4`.                                                           (43)

Hence every matrix in the family has far more than the three eigenvalues of modulus at least one required by the exact conjecture.

### 7. What this proves and what remains open

This run proves a new, sharp additional-eigenvalue stability bridge. It does **not** prove the unrestricted QFORM conjecture. The missing structural implication is still: from the bare hypothesis that a symmetric `A` has three eigenvalues of absolute value at least one, force a product-preserving original-coordinate cross bank with enough singular-value reserve and sufficiently controlled residual spectral `ell_2` energy (possibly after extracting a free low-rank large-mode packet), or prove that failure of every such certificate forces one of the already established ridge, grouped-bank/hub, localized physical-core, scalar-Schur, or other volume branches.

The theorem above gives **continuous density** in its stated scope because the completed D5 receiver used in (14) has an integrable characteristic-function conclusion. Continuity for the unrestricted exact target remains open.

## Partner provenance

Completed partner result actually used above:

- repository: `yspennstate/math-open-problems`
- commit: `64268d2bee76cd374e2bf1a34868e0e6a1b7e84d`
- path: `proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B12/20260923T115313Z-fleet02-B12-qform-r33/REPORT.md`
- theorem used: `QFORM-ADAPTIVE-RESERVE-ENVELOPE-v1`

## Control / correction provenance


## Research status

- New theorem: `QFORM-SHARP-SPECTRAL-TAIL-HALF-ENERGY-v1` — **PROVED**.
- Partner theorem applied to an actual inequality — **YES**, equation (39).
- Scoped density continuity — **PROVED** through the completed D5 receiver.
- Full QFORM target — **OPEN**.
- Native brain ingestion — **WITHOUT_VERIFIED_BRAIN**.
