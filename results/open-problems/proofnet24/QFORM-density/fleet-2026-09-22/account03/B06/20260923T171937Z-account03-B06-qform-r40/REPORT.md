SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B06, 2026-09-23T17:19:37Z.
attacking: the ultra-thin near-rank-two survivor; convert low determinant-pair disjointness into a single physical row and column carrying a majority of the dominant two-dimensional singular planes, before any reciprocal-minor payment.

# account03/B06 r40 — low pair-disjointness forces literal >19/32 top-plane hubs

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Owner control:** revision `2026-09-22.15`, programme revision `2026-09-22.5`  
**Assignment:** Curved fiber integration  
**Status:** `NEW SUPPORTING STRUCTURAL THEOREM + PAID LARGE-EDGE SUBBRANCH / FULL TARGET OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Exact scope and source-valid inputs

The full target remains open: for independent ORIGINAL real coordinates with probability densities bounded by one and every real symmetric matrix `A` having at least three eigenvalues of modulus at least one, prove a universal density bound for `Q=X^TAX`, or give a valid counterexample. No moment, support, iid, Gaussian, log-concavity, sign, finite-rank or post-rotation independence assumption is introduced. Continuity is tracked separately.

The run starts from the literal ORIGINAL-coordinate cut supplied by the completed account04/B20 theorem

`yspennstate/math-open-problems@c6f29397b3d45a7cf7ab67633a5451767b478912`

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B20/20260923T142031Z-account04-B20-QFORM-r10/REPORT.md`.

In the no-moderate-diagonal branch

`|A_ii|<1/64` for every physical coordinate, `s_3(A)>=1`,

it gives an ORIGINAL-coordinate partition `[n]=J disjoint_union K` with

`N=A[J,K]`,

`E:=||N||_F^2 > E0:=11907/16384`.                                      (1.1)

The compatible B06 r39 ultra-thin branch has squared singular values

`x1>=x2>=...>=0`, `sum_r x_r=E`,

`T:=sum_{r>=3}x_r < T0:=14211/141070336`,                               (1.2)

`x2 > E0/64 =11907/1048576`,                                           (1.3)

and the earlier B06 r37 estimate gives

`x1*x2 > (31/2048)E^2`,                                                (1.4)

`Z2:=e_2(N^T N) > (31/2048)E^2`.                                      (1.5)

The determinant-only physical-pair theorem actually used below is the arbitrary-rank Theorem 3.1 in

`yspennstate/math-open-problems@472b70df7d1edbb3afac23269bc2e4368ae0e371`

`proofnet24/QFORM-density/interactive/20260922T225732Z-claude-synthesis/GEOMETRIC_SYNTHESIS.md`:
if an ORIGINAL physical 2x2 principal block is indefinite with determinant magnitude `D>0` and `s_3(A)>=1`, then

`||p_Q||_infinity <= D^(-1/2)[9.2+log_+(10000 sqrt(D))]`.                (1.6)

The exact designated `account04/B06` current-QFORM canonical directory was again absent at the source check, so no theorem is fabricated there. The completed account04/B20 result above is the account04 theorem applied to the actual inequality (1.1).

Live corrections retained: no law-uniform pointwise quadratic-phase decay, no arbitrary-joint coarea cap, no positive moment of worst conditional projection-density caps, no independence after rotation, no unrestricted fiber supremum, no one-good-minor extraction, and no deletion of a small nonzero quadratic tail on arbitrary unbounded inputs.

## 2. A purely combinatorial pair-law theorem

Let `mu` be any probability distribution on two-element subsets of an arbitrary finite or countable set. For `S,S'` independent with law `mu`, define

`alpha_i=P(i in S)`, `m=max_i alpha_i`,

`delta=P(S cap S'=empty)`.                                             (2.1)

### Lemma 2.1 — `PAIRLAW-DISJOINTNESS-SINGLE-HUB-v1`

If

`delta<1/256`,                                                         (2.2)

then

`boxed: max_i alpha_i >3/5.`                                           (2.3)

#### Proof

For an edge `e={a,b}` in the support of `mu`, let

`C(e)=P(S cap e=empty)`.

Since `E_{e~mu} C(e)=delta`, choose `e={a,b}` with `C:=C(e)<=delta`.
Write

`x=mu({a,b})`,
`p_u=mu({a,u})`, `q_u=mu({b,u})` for `u notin {a,b}`,
`A=sum_u p_u`, `B=sum_u q_u`.

Then

`1=x+A+B+C`.                                                          (2.4)

Because `alpha_a=x+A<=m` and `alpha_b=x+B<=m`,

`A>=1-C-m`, `B>=1-C-m`.                                                (2.5)

The ordered disjoint pairs consisting of one `a`-star edge and one `b`-star edge contribute

`2 sum_{u!=v}p_u q_v =2(AB-sum_u p_u q_u)`                             (2.6)

to `delta`. For every `u`,

`p_u+q_u <= alpha_u <=m`,

so

`p_u q_u <=(p_u+q_u)^2/4 <= m(p_u+q_u)/4`.                            (2.7)

Since `A+B<=1-C`,

`sum_u p_u q_u <=m(1-C)/4`.                                           (2.8)

Thus

`delta >= F(C,m):=2[(1-C-m)^2-m(1-C)/4].`                             (2.9)

Assume for contradiction `m<=3/5`. On the rectangle

`0<=C<=1/256`, `0<=m<=3/5`,

we have

`partial_C F=-4(1-C-m)+m/2<0`,
`partial_m F=4m-(9/2)(1-C)<0`.                                        (2.10)

Therefore `F(C,m)>=F(1/256,3/5)`. Direct exact arithmetic gives

`F(1/256,3/5)
 =1/256+9049/819200
 >1/256`.                                                             (2.11)

But `C<=delta<1/256`, so (2.9)-(2.11) imply `delta>1/256`, a contradiction. QED.

This lemma is deliberately about the entire weighted pair law. It selects a physical vertex only after integrating all pair weights and never maximizes a random curved fiber.

## 3. In the ultra-thin packet, more than 64/65 of the two-volume is spectral pair (1,2)

Put

`R:=Z2-x1*x2`.

Since every pair other than `(1,2)` contains at least one tail singular direction,

`R=(x1+x2)T+e_2(x3,x4,...)`.                                          (3.1)

Using `e_2(tail)<=T^2/2`, `x1+x2<=E`, and (1.4),

`R/(x1*x2)
 <(2048/31)[T/E+(T/E)^2/2].`                                          (3.2)

From (1.1)-(1.2),

`T/E < T0/E0 =6316/45565443 <1/7000`.                                (3.3)

Hence

`R/(x1*x2)
 <(2048/31)(1/7000+1/(2*7000^2))
 =224016/23734375
 <1/64`.                                                              (3.4)

Therefore the normalized spectral-pair weight

`w12:=x1*x2/Z2`

satisfies

`boxed: w12>64/65.`                                                    (3.5)

No small singular direction has been deleted from the quadratic form. Equation (3.5) is only a deterministic statement about where the aggregate physical two-volume comes from.

## 4. Determinant-pair marginals force >19/32 top-two physical leverage

Let `N=U diag(sqrt(x_r)) V^T` be an SVD. Normalize the physical squared-minor law

`w^0_(S,T)=det(N[S,T])^2/Z2`, `|S|=|T|=2`.                            (4.1)

Let `mu_R` and `mu_C` be its row-pair and column-pair marginals, and put

`delta_R=P(S cap S'=empty)`, `S,S' iid~mu_R`,
`delta_C=P(T cap T'=empty)`, `T,T' iid~mu_C`.                         (4.2)

For a physical row `i`, write

`ell_i=u_i1^2+u_i2^2`,                                                (4.3)

the leverage of the dominant two-dimensional left singular plane. Cauchy-Binet gives the exact spectral-pair mixture

`alpha_i:=mu_R{i in S}
 =sum_{r<s} [x_r x_s/Z2](u_ir^2+u_is^2).`                              (4.4)

Every parenthesized projection diagonal is at most one. Consequently, by (3.5),

`alpha_i <=w12 ell_i+(1-w12).`                                        (4.5)

If `delta_R<1/256`, Lemma 2.1 supplies an `i` with `alpha_i>3/5`. Thus

`ell_i >1-(2/5)/w12
       >1-(2/5)(65/64)
       =19/32.`                                                        (4.6)

The identical argument on `N^T` says that if `delta_C<1/256`, some physical column `a` has dominant right-plane leverage

`r_a:=v_a1^2+v_a2^2 >19/32.`                                          (4.7)

Because the sum of all left (respectively right) top-two leverages is exactly two, there can be at most three physical rows, and at most three physical columns, satisfying `>19/32`. Thus the low-disjointness ultra-thin obstruction is confined to literal at-most-three-by-at-most-three dominant-plane hub candidates.

## 5. Absolute cross-star and anchored-cofactor currencies

Assume from now on the simultaneous low-disjointness branch

`delta_R<1/256`, `delta_C<1/256`,                                     (5.1)

and choose `i in J`, `a in K` as in (4.6)-(4.7).

The top-two part `N2` of `N` gives

`||e_i^T N2||_2^2
 =x1 u_i1^2+x2 u_i2^2
 >=x2 ell_i
 >(11907/1048576)(19/32)
 =226233/33554432.`                                                   (5.2)

Therefore

`boxed: ||N[i,K]||_2 >sqrt(226233/33554432)>0.0821113.`                (5.3)

Likewise

`boxed: ||N[J,a]||_2 >0.0821113.`                                     (5.4)

These are complete ORIGINAL-coordinate cross stars, not selected edges.

There is also a cofactor bank tied to the same two heavy physical anchors. Under the joint minor law (4.1),

`P(i in S)>3/5`, `P(a in T)>3/5`,

so the union bound gives

`P(i in S and a in T)>1/5`.                                           (5.5)

Thus, with

`Z_ia:=sum_{j!=i,beta!=a}det N[{i,j},{a,beta}]^2`,

we have

`Z_ia>Z2/5
 >(31/10240)E^2
 >(31/10240)E0^2
 =4395076119/2748779069440
 =0.0015989193776476895...`.                                          (5.6)

After permuting these anchors first and writing

`N=[[b,r^T],[c,D]]`,                                                   (5.7)

the exact anchored-cofactor identity gives

`boxed: Z_ia=||bD-c r^T||_F^2>0.0015989193...`,                       (5.8)

so

`||bD-c r^T||_F>0.03998648`.                                          (5.9)

Again, this spends the entire cofactor bank before any individual minor is inverted.

## 6. The mutual edge is either already paid or leaves two robust disjoint stars

Let `b=N_ia=A_ia`. There are two cases.

### 6.1 Large mutual edge: a completed target-level density exit

If

`|b|>=1/32`,                                                          (6.1)

then, because the live account04/B20 branch has

`|A_ii|,|A_aa|<1/64`,                                                  (6.2)

the ORIGINAL principal pair on `{i,a}` is indefinite and its determinant magnitude obeys

`D_pair=|A_ii A_aa-b^2|
 >1/1024-1/4096
 =3/4096.`                                                            (6.3)

Apply the completed determinant-only physical-pair theorem (1.6). Since its right side decreases with `D`,

`boxed: ||p_Q||_infinity
 <(3/4096)^(-1/2)
   [9.2+log(10000 sqrt(3/4096))]
 <547.`                                                               (6.4)

This conclusion is essential boundedness/absolute continuity; the cited pair theorem does not assert a continuous representative.

### 6.2 Small mutual edge: two robust opposite physical stars survive

If instead

`|b|<1/32`,                                                          (6.5)

then (5.3)-(5.4) yield

`||r||_2^2
 =||N[i,K]||_2^2-b^2
 >226233/33554432-1/1024
 =193465/33554432`,                                                   (6.6)

and identically

`||c||_2^2>193465/33554432`.                                          (6.7)

Hence

`boxed: ||r||_2,||c||_2>0.07593224`,                                  (6.8)

and in particular

`boxed: ||r||_2||c||_2>193465/33554432
                         =0.0057657063... .}`                          (6.9)

The small nonzero mutual edge `b`, both same-bank blocks, all additional spectrum and every ambient coupling remain present. Nothing is dropped as a random perturbation.

## 7. Combined theorem and actual progress

### Theorem 7.1 — `QFORM-ULTRATHIN-PAIRLAW-SINGLE-HUB-v1`

In the account04/B20 no-moderate-diagonal cut (1.1), assume the B06 r39 ultra-thin near-rank-two packet (1.2)-(1.5) and the simultaneous low determinant-pair-disjointness condition (5.1). Then there exist one ORIGINAL row `i` and one ORIGINAL column `a` such that

1. their dominant two-plane leverages both exceed `19/32`;
2. their full physical cross-star norms both exceed `0.0821113`;
3. their common anchored cofactor bank exceeds `0.0015989193`;
4. if `|A_ia|>=1/32`, the full ambient quadratic form already has `||p_Q||_infinity<547` by a completed arbitrary-rank physical-pair theorem;
5. otherwise `|A_ia|<1/32` and the two opposite anchor stars after deleting the mutual edge both exceed `0.0759322`, with product exceeding `0.0057657063`.

The theorem narrows a formerly diffuse low-disjointness rank-two tube to a literal pair of single physical hubs, each carrying a majority of the dominant two-plane, plus a fixed cofactor and double-star currency. The exact designated partner account04/B06 still has no completed current-QFORM canonical theorem, so the account04/B20 theorem is the completed account04 result actually applied at (1.1).

## 8. What remains open

This run does **not** solve the full conjecture. Two pieces remain in the r39 ultra-thin route:

- the high determinant-pair-disjointness side currently carries a uniform half-Riesz credit but not, by itself, a bounded-density conclusion;
- in the low-disjointness side after (6.5), the remaining task is to consume the literal two-hub/double-star packet while retaining the small nonzero mutual edge, arbitrary same-bank curvature, and all extra spectrum.

The next exact B06 debt is

`QFORM-ULTRATHIN-TWO-SINGLE-HUB-RECEIVER-v1`:

> Starting from two ORIGINAL anchors with top-plane leverages `>19/32`, opposite-star product `>193465/33554432`, anchored cofactor bank `>4395076119/2748779069440`, and `|A_ia|<1/32`, prove a uniform density bound while retaining all same-bank curvature and the complete nonzero tail; or route this packet into the proved projected-crossing/grouped-hub receiver with all of its row-marginal and rank gates verified.

The fresh projected-crossing theorem in `proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md` is relevant but does not automatically pay this packet: its extra projected-crossing volume and row-marginal hypotheses still have to be proved for an actual light-coordinate split. The new result above supplies a much stronger physical starting point for exactly that verification.

**Full QFORM:** OPEN / NOT PROVED / NOT DISPROVED.  
**Universal continuity:** OPEN. The newly paid large-edge branch establishes an essentially bounded density through the physical-pair theorem; continuity is not claimed there.
