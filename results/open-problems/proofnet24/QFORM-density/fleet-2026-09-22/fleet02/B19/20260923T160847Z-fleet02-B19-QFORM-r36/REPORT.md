SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B19, 2026-09-23T16:08:47Z.
attacking: fleet03/B19 r36 branch (II), where a quantitative self-bank off-diagonal packet overlaps the old rank-two J-K bicore; extract the exact mixed exterior three-volume and spend it before absolute-value separation.

# fleet02/B19 r36 — overlapping self-packet plus bicore: exact mixed exterior-volume payment

Programme: `QFORM-DENSITY-3EIG-20260922`

Status: **ESSENTIAL_STEP_APPLIED / ONE OVERLAP SUBBRANCH PAID / FULL QFORM OPEN**.

Execution: **WITHOUT_VERIFIED_BRAIN**. Repository retrieval is not native authenticated learned-memory ingestion.

## 1. Source-pinned proof graph entering this run


The owner-required Claude directory was read at the requested baseline `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`. The same directory has later changes on current master: `FOURIER_ROUTE_REPORT.md` is unchanged at blob `9da148eed6cd43b1046a6f91d0f9329e12921cb4`, while `RESULTS.md` and `COUNTEREXAMPLE_SEARCH.md` were updated. I use the proved D' / fractional three-volume estimate below, at equation level, not merely as a citation.

The immediate fleet02/B19 predecessor is `math-open-problems@744a54e89abb033ca3ce34db0c51b66a499dba88`, which paid the exact union-leaf rank-three-plus-diagonal diffuse Fresnel chamber and showed that a third source need not be source-disjoint or transverse to the old two singular planes.

The newest completed designated partner fleet03/B19 is `math-open-problems@6dfd43d5519df1fc40ea26f7d0bbe300ad32412d`, run `20260923T145843Z-fleet03-B19-QFORM-r36`. In the aligned STAR4 survivor it proves the dichotomy:

* (I) an aligned skeleton `S` with `rank(S)<=5` and `s_3(S)>=1/4`; or
* (II) one actual self bank, say `B=A[J,J]`, with
  `||B||op>0.673586637`, off-diagonal Frobenius square `>0.453717673`, and a physical cut `J=D_1 disjoint_union D_2` satisfying
  `||B[D_1,D_2]||_F^2>F_*`,
  where
  `F_*=0.11342941839244327`.

The old J-K cross block remains in the quantitative rank-two STAR4 branch with

`rho=s_1(A[J,K])s_2(A[J,K])>rho_*`,
`rho_*=0.0038452075095882221056...`.

This run directly attacks branch (II).

## 2. Exact mixed exterior currency

### Theorem 2.1 — `QFORM-OVERLAP-MIXED-EXTERIOR-VOLUME-v1`

Let `I,J,K` be pairwise disjoint sets of ORIGINAL physical coordinates. Put

`N=A[I,K]`, `M=A[I,J]`, `C=A[I,J union K]=[M N]`.

Let

`N=U diag(s_1,s_2,...) V^T`, `s_1>=s_2>=...>=0`,

and for `p<q` let `P_{pq}` be the orthogonal projection in `R^I` onto `span(u_p,u_q)`. Define

`Omega(N,M) := sum_{p<q} s_p^2 s_q^2 ||(I-P_{pq})M||_F^2`.       (2.1)

Then the actual third cross-volume of the enlarged physical cut satisfies

`boxed: e_3(C^T C) >= Omega(N,M).`                               (2.2)

Equivalently, if `P_N` is projection onto the left range of `N`,

`Omega(N,M)`
` = sum_r e_2((s_j^2)_{j != r}) ||u_r^T M||_2^2`
`   + e_2(s_1^2,s_2^2,...) ||(I-P_N)M||_F^2`.                  (2.3)

In particular, if `P_2` is any top-two left singular projection of `N`,

`boxed: Omega(N,M) >= (s_1(N)s_2(N))^2 ||(I-P_2)M||_F^2.}`       (2.4)

For exact rank two, (2.4) is an equality.

### Proof

Write the columns of `N` as `n_a` and of `M` as `m_c`. By Cauchy-Binet in exterior form,

`e_3(C^T C)=sum_{three columns of C} ||c_a wedge c_b wedge c_c||^2`.

Every term is nonnegative. Retain only triples containing exactly two columns of `N` and one column of `M`:

`e_3(C^T C)`
` >= sum_{a<b,c} ||n_a wedge n_b wedge m_c||^2`.                 (2.5)

The Hilbert-Schmidt spectral decomposition of the second exterior power of `N` is

`(wedge^2 N)(wedge^2 N)^*`
` = sum_{p<q} s_p^2 s_q^2 (u_p wedge u_q)(u_p wedge u_q)^*`.

Therefore, for each fixed `m_c`,

`sum_{a<b} ||n_a wedge n_b wedge m_c||^2`
` = sum_{p<q} s_p^2 s_q^2 ||(I-P_{pq})m_c||^2`.

Summing over `c` proves (2.2). Expanding each orthogonal complement in the left singular basis gives (2.3). Keeping only the `(p,q)=(1,2)` term gives (2.4). No random-coordinate rotation has occurred; this is deterministic coefficient geometry.

## 3. Spend the mixed currency with the completed D' theorem

Let `Z_3=e_3(C^T C)` and let `alpha_i(C)` be the canonical squared-minor row inclusion marginals for the actual cross block `C`. The completed D' / fractional-volume theorem from the owner-required Claude source says that if

`max_{i in I} alpha_i(C) <= 2/3`,                                 (3.1)

then, with all self-block quadratic terms, all outside couplings, and all affine terms arbitrary,

`||p_Q||_infinity <= (9 sqrt(3) e / 2) Z_3^(-1/6)`.              (3.2)

Combining (2.2) and (3.2) yields the new overlap receiver

`boxed:
 ||p_Q||_infinity
 <= (9 sqrt(3)e/2) Omega(N,M)^(-1/6).
}`                                                               (3.3)

Using only the top-two term (2.4), if

`s_1(N)s_2(N)>=r`,
`||(I-P_2)M||_F>=d`,
`max alpha_i(C)<=2/3`,                                           (3.4)

then

`boxed:
 ||p_Q||_infinity
 <= (9 sqrt(3)e/2) (r d)^(-1/3).
}`                                                               (3.5)

This branch has a continuous `C_0` density by the same Fourier inversion theorem. Importantly, `M` is not source-disjoint from the old self bank: it is literally an internal physical cut of that bank. The theorem works because the two old cross columns and the new self-cut column are assembled into one genuine ORIGINAL-coordinate cross block before decoupling.

## 4. Actual application to fleet03/B19 r36 branch (II)

Let `B=A[J,J]` be the winning self bank and `J=D_1 disjoint_union D_2` the partner cut, with

`M=B[D_1,D_2]`, `||M||_F^2>F_*`.

For `r=1,2`, write `D_{3-r}` for the opposite half and define

`N_r=A[D_r,K]`,
`C_r=A[D_r,D_{3-r} union K]=[B[D_r,D_{3-r}], N_r]`,
`rho_r=s_1(N_r)s_2(N_r)`,
`P_r=top-two left singular projection of N_r`,
`delta_r^2=||(I-P_r)B[D_r,D_{3-r}]||_F^2`.

Set the fixed mixed-volume benchmark

`omega_* := rho_*^2 F_*/16`
`          =1.048202729365232e-7...`.                            (4.1)

If for either orientation `r`

`rho_r >= rho_*/2`,
`delta_r^2 >= F_*/4`,
`max_i alpha_i(C_r)<=2/3`,                                      (4.2)

then Theorem 2.1 gives

`Z_3(C_r)>=rho_r^2 delta_r^2>=omega_*`,

so the owner-required completed D' theorem gives the explicit target-level inequality

`boxed:
 ||p_Q||_infinity
 <= (9 sqrt(3)e/2) omega_*^(-1/6)
 =308.550846342... <309.
}`                                                               (4.3)

Thus a quantitatively transverse part of the partner's overlapping self packet is now paid even though it shares the same source bank as the old bicore.

Conversely, suppose `rho_r>=rho_*/2` but `Omega(N_r,M)<omega_*`. Then (2.4) forces

`delta_r^2 < omega_*/(rho_*^2/4)=F_*/4`.                         (4.4)

Since `||M||_F^2>F_*`, more than three quarters of the partner packet lies in the SAME two-dimensional physical row plane as the retained bicore:

`boxed:
 ||P_r M||_F^2 > 3F_*/4
 =0.08507206379433245... .
}`                                                               (4.5)

Therefore branch (II) is no longer merely 'an overlapping self-bank packet'. For each orientation that retains at least half of the old singular-product scale, it is either paid by (4.3), row-volume-heavy (`max alpha>2/3`), or quantitatively **in-plane** in the precise sense (4.5).

There is a genuine residual possibility that both restrictions lose the bicore:

`rho_1<rho_*/2` and `rho_2<rho_*/2`.                              (4.6)

This cannot be ruled out by a universal inequality of the form `max(rho_1,rho_2)>=c rho`: a rank-two matrix can have its two left singular directions supported on opposite halves, making both row restrictions rank one while the full block has nonzero singular product. Thus (4.6) is a real split-bicore geometry, not a proof artefact.

## 5. Sharpened first gap

The designated partner's first unpaid implication was

`QFORM-ALIGNED-SKELETON-OR-SELFPAIR-PAYMENT-v1`.

After this run its self-pair branch has a strictly narrower unpaid residue. The finite-rank skeleton branch (I) is unchanged except for the union-bank rank-three-plus-diagonal Fresnel subchamber already paid in fleet02/B19 r35. In branch (II), after the new payment, every survivor must satisfy at least one of:

1. **split bicore:** on both orientations of the partner self cut, the restricted old bicore has `rho_r<rho_*/2`;
2. **volume-anchor:** every orientation retaining `rho_r>=rho_*/2` has an augmented three-volume row marginal `>2/3`;
3. **fully in-plane overlap:** on an orientation retaining the bicore, the self-cut packet has `||P_r M||_F^2>3F_*/4` and transverse energy `<F_*/4`.

This is the new first branch-II debt, `QFORM-STAR4-SPLITBICORE-OR-INPLANE-SELFOVERLAP-v1`. It asks for a product-preserving payment of the two-line split or the genuinely in-plane self packet, or a descent of the `>2/3` volume anchor to a completed physical core. No source-disjointness is assumed, and no self/cross coupling is deleted.

## 6. Full-proof graph status

The global source-pinned graph is still conditional: physical-pivot synthesis -> strict N3 -> spectral-window diffuse exit -> STAR4 compiler -> D5/selected-volume exits -> fleet03/B19 r36 third-resource carrier dichotomy. Branch (I) still contains general rank<=5 aligned skeleton plus arbitrary same-bank curvature. Branch (II) is sharpened by Sections 2-5 above. The relative-rank-one tube / other global N3 branches remain as recorded in the shared programme. Arbitrary-extra-spectrum closure and unrestricted continuity are not claimed here.

The full QFORM target remains **OPEN / NOT PROVED / NOT DISPROVED**. Two independent end-to-end reviews do not exist.
