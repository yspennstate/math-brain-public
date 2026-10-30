SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet03, slot B13, 2026-09-23T20:30:53Z.
attacking: quantitative stability of the rank-two physical-pair volume law: prove that small disjointness forces a near-coloop star or a three-coordinate triangle, then apply the fleet04/B13 diffuse slab dichotomy at an actual inequality.

# fleet03/B13 r34 — quantitative rank-two pair-volume stability

Programme: `QFORM-DENSITY-3EIG-20260922`. Role: extremal product laws. Owner continuation acknowledged: `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z`. Execution: `WITHOUT_VERIFIED_BRAIN`.

Status: **NEW PROVED DETERMINISTIC GEOMETRIC THEOREM + NEW APPLICATION TO THE DIFFUSE EXACT-RANK-TWO SLAB ENDPOINT / FULL QFORM OPEN / FULL CONTINUITY OPEN**.

No Gaussian, log-concavity, moment, compact-support, connected-support, post-rotation independence, single-interval extremality, bounded support diameter, fixed fragment count, or deletion of a coefficient-small quadratic tail is used.

## 1. Fresh sources and exact premises


The designated partner report actually applied is

`yspennstate/math-open-problems@d1764f29884bf14ce505d36668105edfcaf8315e`

`proofnet24/QFORM-density/fleet-2026-09-22/fleet04/B13/20260923T201653Z-fleet04-B13-extremal-slab-dichotomy-r1/REPORT.md`.

It proves the optimizer-free product reduction

`sup_{0<=f_i<=1, int f_i=1} int K prod_i f_i
 = sup_{|E_i|=1} int_{prod E_i} K`                                  (1.1)

for nonnegative measurable `K`, as equality of suprema without asserting an optimizer. Strict slab witnesses can be approximated by bounded finite unions of intervals with arbitrary small loss, but with no uniform diameter or fragment count.

For the diffuse exact-rank-two endpoint

`A=D+U Lambda U^T`, `U^T U=I_2`, `max_i c_i<=1/3`,
`c_i=||u_i||^2`, `s_3(A)>=1`,                                      (1.2)

it chooses an original coordinate `k` with `|d_k|>=1` and proves that a slab ratio

`rho=P{X^T A X in J}/|J|`                                          (1.3)

obeys

`boxed: |A_kk det Lambda| <=1536 e^2 rho^(-4).`                    (1.4)

Equivalently, with

`H=sqrt(1536 e^2)=106.534455308869...`,                            (1.5)

either

`|A_kk|<=H rho^(-2)`                                               (1.6)

or

`dist_op(U Lambda U^T, SymRank_{<=1})
 <=sqrt(H) rho^(-1)=10.3215529504464... rho^(-1).`                 (1.7)

The completed fleet01/B13 Schur-DPP source used below is

`proofnet24/QFORM-density/fleet-2026-09-22/fleet01/B13/20260923T173034Z-fleet01-B13-qform-auto11/REPORT.md`.

For a genuine scalar pivot in (1.2), it constructs a normalized leave-one-out rank-two frame `W` with `W^T W=I_2`. If `q_{ij}=det(w_i,w_j)^2`, then `q` is a probability law on physical pairs. For two independent `q`-pairs `E,F`, put

`delta=P(E cap F=empty)`.                                          (1.8)

Its exact endpoint `delta=0` was classified as a star or triangle, but the source explicitly left quantitative near-zero stability unpaid. The present report fills that gap.

## 2. Weighted graph theorem: quantitative stability of an intersecting pair law

### Theorem 2.1 — `QFORM-WEIGHTED-PAIR-STAR-TRIANGLE-STABILITY-v1`

Let `q=(q_e)` be any probability distribution on the unordered two-element subsets of a finite vertex set. Let `E,F` be independent with law `q`, and put

`delta=P(E cap F=empty)`.                                          (2.1)

Then, with `d=delta^(1/3)`, at least one of the following holds:

1. **near-star:** there is a vertex `v` such that

   `boxed: P(v in E)>=1-2d;`                                      (2.2)

2. **near-triangle:** there is a three-element set `T` such that

   `boxed: P(E subset T)>=1-2d.`                                  (2.3)

For `delta=0`, the conclusion is exact: all positive-mass edges either share one common vertex or are supported on the three edges of one triangle.

#### Proof

If `delta>=1/8`, then `d>=1/2` and the right sides in (2.2)-(2.3) are nonpositive, so the assertion is trivial. Assume henceforth `0<delta<1/8`; thus `0<d<1/2`.

For an edge `e`, let

`r(e)=sum_{f: f cap e=empty} q_f`.

Because

`sum_e q_e r(e)=delta`,                                           (2.4)

there is a positive-mass edge `e_0={a,b}` with

`R:=r(e_0)<=delta=d^3`.                                           (2.5)

Write

`r=q_{ab}`,
`A_c=q_{ac}`, `B_c=q_{bc}` for `c notin {a,b}`,
`A=sum_c A_c`, `B=sum_c B_c`.                                     (2.6)

Every edge is either `{a,b}`, an `a`-edge, a `b`-edge, or disjoint from `{a,b}`; hence

`1=r+A+B+R`.                                                       (2.7)

The star masses at `a,b` are

`s_a=r+A`, `s_b=r+B`.                                              (2.8)

If either is at least `1-2d`, (2.2) holds. Suppose not. From `s_a<1-2d` and (2.7),

`B+R>2d`, hence `B>2d-R>=2d-d^3>d`;                               (2.9)

similarly `A>d`.

An `a`-edge `{a,c}` and a `b`-edge `{b,c'}` are disjoint exactly when `c!=c'`. Counting both orders inside (2.1) gives

`2(AB-sum_c A_c B_c)<=delta`.                                     (2.10)

Normalize

`p_c=A_c/A`, `q_c=B_c/B`,
`eta=delta/(2AB)`.                                                 (2.11)

Then

`sum_c p_c q_c >=1-eta`,                                          (2.12)

and by (2.9)

`eta<delta/(2d^2)=d/2`.                                           (2.13)

Choose `c_*` maximizing `p_c`. Since the left side of (2.12) is at most `max_c p_c`,

`p_{c_*}>=1-eta`.                                                  (2.14)

Also

`sum_c p_c q_c
 <=q_{c_*}+(1-p_{c_*})
 <=q_{c_*}+eta`,                                                   (2.15)

so (2.12) implies

`q_{c_*}>=1-2eta`.                                                 (2.16)

Let `T={a,b,c_*}`. Its edge mass is

`q(binomial(T,2))=r+A_{c_*}+B_{c_*}`.                             (2.17)

Using (2.7), (2.14), (2.16), `A,B<=1`, and (2.13),

`1-q(binomial(T,2))`
` =R+A(1-p_{c_*})+B(1-q_{c_*})`
` <=R+3eta`
` <=d^3+3d/2`
` <=7d/4`
` <2d`,                                                           (2.18)

where `d^3<=d/4` because `d<1/2`. Thus (2.3) holds.

If `delta=0`, choose a positive edge `{a,b}`. Every other positive edge intersects it. If all contain `a`, the support is a star. Otherwise there is a positive `{b,c}`. If all edges contain `b`, again it is a star. Otherwise a positive edge meeting `{a,b}` but not containing `b` and also meeting `{b,c}` must be `{a,c}`. Any further positive edge must meet all three of `{a,b}`, `{b,c}`, `{a,c}`, so it is one of those three. This proves the exact endpoint. QED.

### Comment on the exponent

The `delta^(1/3)` scale arises from balancing the two necessary losses: if neither endpoint star is heavy, the two opposite edge families have masses of order `epsilon`; their normalized mismatch is paid by `delta/epsilon^2`. Balancing `epsilon` with `delta/epsilon^2` gives `epsilon` of order `delta^(1/3)`. No claim of sharp constants is made.

## 3. Rank-two Parseval-frame corollary

### Theorem 3.1 — `QFORM-RANK2-DPP-STAR-TRIANGLE-STABILITY-v1`

Let `W` be an `m x 2` real matrix with

`W^T W=I_2`,                                                      (3.1)

and rows `w_i`. Define

`q_{ij}=det(w_i,w_j)^2`, `i<j`.                                   (3.2)

Then by Cauchy--Binet

`sum_{i<j}q_{ij}=1`,                                               (3.3)

so `q` is a probability law on physical pairs. Put

`ell_i=sum_{j!=i} q_{ij}`.                                        (3.4)

Then

`boxed: ell_i=||w_i||_2^2.`                                       (3.5)

Indeed, with the quarter-turn matrix `J`,

`sum_j det(w_i,w_j)^2`
`=w_i^T J (sum_j w_j w_j^T) J^T w_i`
`=||w_i||^2`.                                                      (3.6)

If `delta` is the disjointness probability (2.1), Theorem 2.1 yields one of two quantitative physical-coordinate alternatives:

1. **near physical coloop:** some `h` satisfies

   `ell_h>=1-2 delta^(1/3)`,                                      (3.7)

   and therefore

   `boxed: s_2(W_{[m]\{h}})
   <=sqrt(2) delta^(1/6).}`                                       (3.8)

   This follows because

   `W_{-h}^T W_{-h}=I_2-w_h w_h^T`,                              (3.9)

   whose smaller eigenvalue is `1-ell_h`.

2. **near three-coordinate support:** some three-set `T` satisfies

   `sum_{ij subset T}q_{ij}>=1-2 delta^(1/3)`,                    (3.10)

   and hence

   `boxed: ||W_{T^c}||_F^2
   =sum_{i notin T}ell_i
   <=4 delta^(1/3),}`                                             (3.11)

   so

   `boxed: ||W_{T^c}||_op<=2 delta^(1/6).}`                       (3.12)

For (3.11), an edge outside the triangle has at most two endpoints outside `T`, hence

`sum_{i notin T}ell_i
 =E_q[#(E\T)]
 <=2 P_q(E notsubset T)
 <=4 delta^(1/3)`.                                                 (3.13)

The statements concern deterministic coefficient geometry only. In particular, (3.8) or (3.12) is **not** permission to delete the corresponding mode in a rough product law.

## 4. Diffuse leverage gives a quantitative disjointness floor

### Corollary 4.1 — `QFORM-RANK2-DPP-DIFFUSE-DISJOINTNESS-FLOOR-v1`

If in Theorem 3.1

`max_i ell_i<=q_0<=2/3`,                                          (4.1)

then

`boxed: delta >= (2-3q_0)^3/64.`                                  (4.2)

In particular,

`boxed: max_i ell_i<=1/2  =>  delta>=1/512.`                      (4.3)

#### Proof

Every star has mass at most `q_0`. If `T` is a three-set, then

`2 q(binomial(T,2))
 <=sum_{i in T}ell_i
 <=3q_0`,                                                         (4.4)

so every triangle has mass at most `3q_0/2`. The latter dominates `q_0` for `q_0>=0`. If `delta>=1/8`, (4.2) is automatic because `(2-3q_0)^3/64<=1/8`. Otherwise Theorem 2.1 forces

`1-2 delta^(1/3)<=3q_0/2`,                                       (4.5)

which rearranges to (4.2). Substituting `q_0=1/2` gives `delta>=1/512`. QED.

This is the quantitative version of the exact star/triangle endpoint needed by the rank-two Schur-DPP route.

## 5. Actual application of the designated fleet04/B13 result

Return to the partner's diffuse exact-rank-two endpoint (1.2). The exact scalar-Schur normalization in the completed fleet01/B13 source gives, after pivoting the selected physical coordinate `k`, a normalized frame `W` whose row leverages satisfy

`tilde c_i<=c_i/(1-c_k)`.                                         (5.1)

Because every `c_i<=1/3` and `c_k<=1/3`,

`boxed: max_i tilde c_i<=1/2.`                                    (5.2)

Therefore Corollary 4.1 applies to the **actual leave-one-out pair-volume law** and gives

`boxed: delta_k>=1/512.`                                          (5.3)

This excludes degeneration of the physical disjoint-pair volume as a hidden failure mode inside the partner's diffuse branch.

At the same time, the designated fleet04/B13 result gives the actual slab inequality

`boxed: |A_kk det Lambda|<=1536 e^2 rho^(-4).}`                   (5.4)

Thus every high-ratio diffuse exact-rank-two witness satisfies the simultaneous quantitative pair

`boxed:
 delta_k>=1/512,
 |A_kk det Lambda|<=11349.5901679575 rho^(-4).}`                  (5.5)

Consequently, within this diffuse endpoint, a sequence with `rho->infinity` cannot escape through `delta_k->0`. It must enter the partner's genuine algebraic degeneration:

`|A_kk|<=106.534455309 rho^(-2)`                                  (5.6)

or

`dist_op(U Lambda U^T,SymRank_{<=1})
 <=10.321552951 rho^(-1)`.                                       (5.7)

This is an equation-level application of the designated partner result; it does not merely restate its theorem.

For comparison, the prior Schur-DPP density receiver has a factor `delta_k^(-1/8)`. Equation (5.3) bounds that factor by

`(512)^(1/8)=2^(9/8)`,                                            (5.8)

so that receiver is also uniformly activated throughout the partner's diffuse leverage chamber. The direct partner estimate (5.4) has better constants, so no inferior constant is promoted here.

## 6. Relation to r33 and the remaining rough-law gap

The preceding r33 theorem showed that every hypothetical high-slab target witness has, after at most four physical hubs, a complementary coefficient matrix

`A[K,K]=D+R+E`, `rank R<=2`,                                      (6.1)

with

`rho ||E||_F ->0` along a hypothetical sequence `rho->infinity`.  (6.2)

The present result supplies a quantitative geometry for the exact rank-two carrier `R`: whenever its physical pair-volume law has small disjointness, it is forced within `O(delta^(1/6))` of either a one-coloop/rank-one frame or a three-coordinate frame. In the diffuse leave-one-out chamber, disjointness is instead bounded below by the absolute constant `1/512`.

This sharpens the next structural choice but does **not** justify deleting the retained `E`. Under arbitrary unbounded/fragmented cap-one laws, a small coefficient norm need not make `X^T E X` small. The first unpaid B13 implication is therefore

`QFORM-STABLE-DPP-OR-FINITE-CENTER-TWIST-GLUE-v1`:

combine (6.1)-(6.2) with the new star/triangle stability. If the rank-two carrier remains diffuse, use the uniform disjointness floor to absorb the retained twist through a product-preserving grouped/projected-crossing estimate. If its disjointness collapses, use (3.8) or (3.12) to pass to one physical coloop or three physical carrier coordinates **without deleting** the residual mode. This is the same full target, not a switch to an easy subclass.

## 7. Scope and status

The full QFORM conjecture remains **OPEN / NOT PROVED / NOT DISPROVED**. No counterexample is produced. Global continuity remains **OPEN**. The new theorems are deterministic structural inputs and a target-level application to the exact diffuse rank-two endpoint. They cover all signs of the symmetric rank-two carrier because the pair-volume law uses squared determinants.

The extremal product reduction used here is optimizer-free and therefore compatible with arbitrarily fragmented supports; no single interval or centered uniform law is claimed extremal.
