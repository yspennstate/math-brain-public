SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 03, slot B07, 2026-09-23T13:40:21Z.
attacking: coordinate-minor aggregation in the r30 residual-E3/six-bank branch, with determinant weight preserved before conditioning.

# Early substantive checkpoint — residual E3 concentration and overlap-aware star/core disjointification

Programme: `QFORM-DENSITY-3EIG-20260922`. Full target remains OPEN. Continuity remains separate. Execution: `WITHOUT_VERIFIED_BRAIN`.

Incoming own r30 branch: an ORIGINAL-coordinate far cross block `D` has

`Z3=E3(D) > (8/3) a^6`,

where the inherited stable-core scale satisfies `a=s3(M_parent)` and, from the completed designated-partner account04/B07 scale combined with the already-proved r31 stable-core inequality,

`a > a0 := 16 sqrt(beta h^2/4617) = 1.9279762269984055e-7`,

`h=(2sqrt(2)-1)/1572864`, `beta=sqrt(63)/16`.

## 1. Diffuse residual E3 is already paid

Normalize the squared `3x3` minors of `D` to a probability law. If all row inclusion marginals are at most `2/3`, or all column marginals are at most `2/3` after transposing, the completed full-ambient third-volume theorem gives

`||p_Q||_infinity <= (9sqrt(3)e/2) Z3^(-1/6)
                   < 17.991727/a
                   < 9.332e7`.

This branch has a continuous density.

If neither side is diffuse, choose a physical row `i` and column `j` whose inclusion marginals exceed `2/3`. The union bound under the SAME squared-minor law gives a double-anchored packet

`G = sum det D[{i}+R,{j}+T]^2 > Z3/3 > (8/9)a^6`.

Writing the literal block as

`D=[[b,r^T],[c,E]]`,

Laplace expansion and the Hilbert-Schmidt norm of the exterior contraction map give

`sqrt(G) <= |b| sqrt(E2(E)) + ||r|| ||c|| ||E||F`.

Since `sqrt(G)>(2sqrt(2)/3)a^3`, at least one of

`|b| sqrt(E2(E)) > (sqrt(2)/3)a^3`,

`||r|| ||c|| ||E||F > (sqrt(2)/3)a^3`

holds. This independently reproduces the algebra in the concurrent account02/B07 early checkpoint and then continues in a different coordinate-selection direction.

## 2. Edge-E2 branch

The N3 cap gives physical diagonals `<tau0=h^2/128`. If `|b|>2tau0`, the physical principal pair on the two anchor coordinates is invertible indefinite with

`|det Bpair|>3b^2/4`, `sigma_min(Bpair)>|b|/2`,

so the completed arbitrary-rank physical-pair theorem pays the full ambient density.

If instead `|b|<=2tau0=h^2/64`, then

`sqrt(E2(E)) > (64sqrt(2)/(3h^2))a^3`.

A physical two-coloring of the rows and columns retains at least one matching of four mutually disjoint ORIGINAL-coordinate banks whose two matched Frobenius norms `F1,F2` satisfy

`F1 F2 >= sqrt(E2(E))/4
        > (16sqrt(2)/(3h^2))a^3`.

No individual `2x2` minor is selected.

## 3. New overlap-aware star/core selector

For arbitrary vectors `c` on row bank `I`, `r` on column bank `J`, and matrix `E` on `I x J`, set

`C=||c||`, `R=||r||`, `F=||E||F`.

There is an exhaustive dimension-free alternative:

1. four mutually disjoint banks `L0,L1 subset I`, `R0,R1 subset J` satisfy

   `||c_L0|| ||r_R0|| ||E[L1,R1]||F >= CRF/(4sqrt(2))`;

2. a physical row `k` satisfies

   `|c_k| >= C/sqrt(8)`, `||E[k,*]|| >= F/8`;

3. a physical column `ell` satisfies

   `|r_ell| >= R/sqrt(8)`, `||E[*,ell]|| >= F/8`.

Proof sketch. Normalize `p_k=c_k^2/C^2`, `q_l=r_l^2/R^2`, `w_kl=E_kl^2/F^2`, with row/column energy marginals `u_k,v_l`. Put `A=sum p_k u_k`, `B=sum q_l v_l`. For an independent fair star/core coloring on each side,

`E[ C0^2 R0^2 F11^2 ]
 = (C^2R^2F^2/16) sum_kl w_kl(1-p_k)(1-q_l)
 >= (C^2R^2F^2/16)(1-A-B)`.

If `A+B<=1/2`, alternative 1 follows. If `A>1/4`, the set `{k:p_k>=1/8}` has size at most eight; its `u`-mass is `>1/8`, so one member has `u_k>1/64`, giving alternative 2. `B>1/4` gives alternative 3.

Applied to the star/core term `CRF>(sqrt(2)/3)a^3`, the outputs become

- genuine four-bank packet `>a^3/12`; or
- row nested packet `|c_k| R ||E[k,*]|| > a^3/48`; or
- column nested packet `|r_l| C ||E[*,l]|| > a^3/48`.

The genuine four-bank packet can now be fed into the completed r22 tail/core router with `theta=1/16` and `Lambda=a^2`; the nested packets are retained for a separate two-hub curvature receiver.

## 4. Nested collision branch becomes almost perfectly disjoint when its edge is small

Consider the row nested packet, write `e=c_k`, `U=||r||`, `V=||E[k,*]||`. If `|e|>2tau0`, the same physical-pair payment applies. Otherwise

`UV > (4/3)a^3/h^2`.

Both physical star vectors have coordinate cap `h/8`. Therefore their normalized same-coordinate collision obeys

`sum_j r_j^2 E_kj^2/(U^2V^2)
 <= h^2/(64 UV)
 < epsilon0 := 3h^4/(256a^3)
 <= 3h^4/(256a0^3)
 = 2.9862227399e-6`.

A fair bipartition of the common leaf bank consequently has disjoint sets `S,T` with

`||r_S|| ||E[k,T]||
 >= (1/2)sqrt(1-epsilon0) UV`.

Hence the still-unpaid nested state carries the genuine disjoint ORIGINAL-coordinate edge/two-star packet

`|e| ||r_S|| ||E[k,T]||
 > [sqrt(1-epsilon0)/96] a^3
 = 0.0104166511... a^3`.

Moreover `max(U,V)>sqrt(UV)>72.335 h`; thus the completed account04/B07 diffuse-bank lemma applies to the larger of these two actual physical stars and supplies four disjoint leaf banks each of norm at least `h/4`. This is an actual current-run use of the designated partner result.

The symmetric column statement is identical.

Full QFORM remains OPEN. The next step is to finish the four-bank analytic routing and record the narrowed nested-edge/two-star and small-edge/E2 debts without claiming that bounded projection density alone pays their curved pushforwards.
