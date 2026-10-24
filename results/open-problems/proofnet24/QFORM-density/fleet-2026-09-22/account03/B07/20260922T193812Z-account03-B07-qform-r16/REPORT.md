SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-22T19:38:12Z.
attacking: coordinate-minor selection by random physical colorings; convert aggregate second/third compound mass into disjoint original-coordinate matching banks without selecting one tiny minor.

# account03/B07 — colored exterior matching for aggregate coordinate minors

**Run:** `20260922T193812Z-account03-B07-qform-r16`  
**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Fresh owner control:** revision `2026-09-22.15`, source brain main `f571209fbad50281e9cbe2065102fe9dc8aa5a0f`  
**Assignment:** Coordinate minor selection / GEOMETRY  
**Execution:** `WITHOUT_VERIFIED_BRAIN` (`full_brain_connected=false`)  
**Classification:** `ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL THEOREM / FULL TARGET OPEN`.

## 1. Exact target and correction discipline

The target remains the unrestricted owner conjecture: for arbitrary dimension, independent real coordinates whose one-dimensional densities are bounded by one, and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove a universal finite bound for the density of `Q=X^TAX`, or give a target-valid counterexample. Continuity is a separate desired conclusion.

This run changes mechanism after the preceding heavy-row/exclusion sequence. It does **not** select one good coordinate minor and invert it. It does not rotate the product source, assume conditional density caps after dependent conditioning, use law-uniform pointwise quadratic-phase decay, use the refuted arbitrary-joint rank-three coarea estimate, or suppress arbitrary self-block curvature.

The designated slot `account04/B07` still has no completed current-QFORM canonical directory at the fresh repository check; no result is fabricated for it. A current completed compatible result actually used below is account02/B19 r17, canonical report

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B19/20260922T192830Z-account02-B19-qform-r17/REPORT.md`.

That report proves, after any genuine physical scalar Schur pivot, the exhaustive second-compound branch `S0`: an original-coordinate residual cross block `B` with

`E_2(B):=e_2(BB^T) >= 1/48`,                                  (1.1)

unless the residual instead enters its shared-coordinate or principal-pair branches. The present theorem converts (1.1) into a disjoint four-bank matching certificate. I also apply the same theorem directly to the completed B07 O0 third-compound resource

`E_3(B):=e_3(BB^T) >= 1/256`,                                 (1.2)

from the full-matrix O0 reduction, producing a six-bank certificate with a substantially stronger constant than the older heavy-singleton Laplace cascade.

## 2. A general colored exterior-matching theorem

Let `B` be any real `m x n` matrix and, for `1<=k<=min(m,n)`, define

`E_k(B):=e_k(BB^T)
       = sum_{|I|=|J|=k} det(B[I,J])^2`.                        (2.1)

The equality is Cauchy--Binet / the Hilbert--Schmidt norm of the `k`th compound.

### Theorem 2.1 — `QFORM-COLORED-EXTERIOR-MATCHING-v1`

For every `k>=1`, there exist partitions of the **original row and column index sets**

`[m]=L_1 disjoint_union ... disjoint_union L_k`,
`[n]=R_1 disjoint_union ... disjoint_union R_k`,               (2.2)

and a permutation `sigma in S_k` such that

`boxed(
 prod_{a=1}^k ||B[L_a,R_{sigma(a)}]||_F^2
 >= E_k(B)/k^(2k).
)`                                                               (2.3)

Moreover the stronger mixed-minor packet can be retained simultaneously:

`boxed(
 P_k:=sum_{i_a in L_a, j_b in R_b}
       det B[{i_1,...,i_k},{j_1,...,j_k}]^2
 >= (k!/k^k)^2 E_k(B).
)`                                                               (2.4)

In (2.4), the row and column tuples contain exactly one index from each colored bank, so every bank is an original-coordinate bank and all `2k` banks used by a matching are pairwise disjoint on their respective sides.

### Proof

Color each row independently and uniformly by one of `k` row colors, and each column independently and uniformly by one of `k` column colors. Fix an unordered `k`-set of rows `I`. The probability that its members receive all `k` colors is

`k!/k^k`.                                                       (2.5)

The same holds independently for a fixed `k`-set of columns `J`. Therefore, if `P_k` denotes the sum of squared minors for which both `I` and `J` are rainbow,

`E P_k = (k!/k^k)^2 E_k(B)`.                                  (2.6)

Hence some deterministic pair of colorings satisfies (2.4).

Fix such a coloring and canonically order each rainbow row/column set by its colors. For every retained minor,

`det B[I,J]
 = sum_{tau in S_k} sgn(tau)
   prod_{a=1}^k B_{i_a,j_{tau(a)}}`.                           (2.7)

Cauchy--Schwarz on the `k!` terms gives

`det B[I,J]^2
 <= k! sum_{tau in S_k}
      prod_{a=1}^k B_{i_a,j_{tau(a)}}^2`.                      (2.8)

Sum (2.8) over all rainbow tuples. For each fixed `tau`, the indices separate and therefore

`sum_{i_a in L_a,j_b in R_b}
 prod_a B_{i_a,j_{tau(a)}}^2
 = prod_a ||B[L_a,R_{tau(a)}]||_F^2`.                          (2.9)

Thus

`P_k <= k! sum_{tau in S_k}
              prod_a ||B[L_a,R_{tau(a)}]||_F^2`.              (2.10)

There are `k!` permutations. Consequently some `sigma` satisfies

`prod_a ||B[L_a,R_{sigma(a)}]||_F^2
 >= P_k/(k!)^2
 >= [(k!/k^k)^2/(k!)^2] E_k(B)
 = E_k(B)/k^(2k)`.                                             (2.11)

This proves (2.3)-(2.4). QED.

### Why this avoids the live one-minor correction

No individual entry or minor is bounded below. The theorem deliberately spends the compound mass only after grouping it into physical banks. A diffuse example may have every retained `k x k` minor tending to zero while (2.3) remains fixed. Thus the conclusion is compatible with the existing counterexamples to reciprocal payment of one tiny coordinate minor.

## 3. Direct application to the full O0 third-compound resource

The completed full-matrix O0 reduction supplies a physical cross block `B=A[L,R]` with (1.2). Apply Theorem 2.1 with `k=3`. There are physical partitions

`L=L_1 disjoint_union L_2 disjoint_union L_3`,
`R=R_1 disjoint_union R_2 disjoint_union R_3`,                 (3.1)

and `sigma in S_3` such that

`P_3 >= (6/27)^2 * (1/256)
     = 1/5184`,                                                 (3.2)

and

`boxed(
 prod_{a=1}^3 ||A[L_a,R_{sigma(a)}]||_F^2
 >= (1/256)/3^6
 = 1/186624.
)`                                                               (3.3)

This is `QFORM-O0-THREE-DISJOINT-MATCHING-BANKS-v1`.

The three cross-energy pairs in (3.3) use six mutually separated physical banks (three on each side), so the source remains a product over all six banks. No heavy row, ridge scale, singleton edge, or finite coordinate count is required.

For comparison, the earlier heavy-singleton Laplace cascade produced the sufficient matching-energy product `>1/3981312` only after a heavy-row packet was present. The purely exterior coloring (3.3) gives the stronger constant

`1/186624 = (64/3) * 1/3981312`,                               (3.4)

and it holds on the entire O0 third-compound branch, not only the heavy-singleton subbranch. This does **not** by itself pay the density: arbitrary self blocks and cross-contamination between the six banks still have to be handled analytically.

## 4. Actual application of the newest compatible partner theorem

Now use the completed account02/B19 r17 scalar-Schur result at its exact scope. Its S0 alternative is the actual inequality (1.1):

`E_2(B)>=1/48`                                                  (4.1)

for a cross block `B` of the exact physical Schur residual.

Apply Theorem 2.1 with `k=2`. There are original-coordinate partitions

`L=L_1 disjoint_union L_2`,
`R=R_1 disjoint_union R_2`                                    (4.2)

and one of the two matchings `sigma in S_2` such that

`sum_{i_1 in L_1,i_2 in L_2}
 sum_{j_1 in R_1,j_2 in R_2}
 det B[{i_1,i_2},{j_1,j_2}]^2
 >= E_2(B)/4
 >=1/192`,                                                     (4.3)

and, quantitatively,

`boxed(
 ||B[L_1,R_{sigma(1)}]||_F^2
 ||B[L_2,R_{sigma(2)}]||_F^2
 >= E_2(B)/16
 >=1/768.
)`                                                               (4.4)

Equation (4.4) is a direct equation-level use of a completed other-account result. It refines the partner's remaining high-leverage S0 geometry into two disjoint physical cross-energy banks before any reciprocal pair/minor cost is paid.

On the partner's already-diffuse S0 subbranch, its determinant-bank half-Riesz theorem and scalar-pivot transducer already give

`||p_Q||_infinity < 12.450 |a|^(-1/2)`,                       (4.5)

and in particular `<24.900` for `|a|>=1/4`; the present matching refinement is not needed for that paid case. Its use is the complementary high-leverage S0 branch, where (4.4) supplies a finite product-provenance target for the next grouped-coordinate step.

The designated `account04/B07` source remains absent, so (4.1)-(4.4) use the newest compatible completed result rather than inventing a partner artifact.

## 5. Smallest conditional end-to-end deduction after this run

The strongest correction-safe conditional route I can state is now:

1. The completed full third-compound reduction routes the hard cross case into O0/O1/O2/O3 without choosing one physical minor.
2. In O0, (3.3) holds **unconditionally**: three pairwise-disjoint original-coordinate cross banks have squared-Frobenius product at least `1/186624`.
3. All previously paid ridge/exact-cross/physical-pivot branches remain paid at their stated scopes.
4. After any genuine scalar pivot, account02/B19 r17 lowers the remaining problem to S0/S1/S2. Its diffuse S0 branch is already paid; in its high-leverage S0 branch, (4.4) supplies two pairwise-disjoint physical cross banks with product at least `1/768`.
5. Therefore a sufficient next analytic theorem is no longer a coordinate-minor selector. It is a **matching-bank transducer**: prove a dimension-free half-Riesz/density estimate from either (3.3) or, after a scalar pivot, (4.4), while allowing arbitrary self-quadratic blocks and all extra spectrum; or show that failure of such a bank payment forces one of the already-paid ridge/grouped/zero-self/indefinite-pair branches.

Call this remaining implication

`QFORM-MATCHING-BANK-TRANSDUCER-v1` (OPEN).                    (5.1)

The theorem must aggregate each physical bank before any inverse singular value is charged. The old one-minor route is still invalid.

## 6. Verification and status

The exact constants are algebraic:

- `k=2`: rainbow retention `(2!/2^2)^2=1/4`; matching divisor `(2!)^2=4`; net `1/16`; hence `(1/48)/16=1/768`.
- `k=3`: rainbow retention `(3!/3^3)^2=4/81`; matching divisor `(3!)^2=36`; net `1/729`; hence `(1/256)/729=1/186624`.

A companion exact-arithmetic checker records these identities. No Monte Carlo or numerical histogram is used as proof.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Continuity:** not established by this structural theorem.  
**New proved claims:** `QFORM-COLORED-EXTERIOR-MATCHING-v1`, `QFORM-O0-THREE-DISJOINT-MATCHING-BANKS-v1`, and the partner-applied Schur-S0 matching inequality (4.4).  
**Native brain ingestion:** not verified; repository retrieval/write is not native learned-memory use.
