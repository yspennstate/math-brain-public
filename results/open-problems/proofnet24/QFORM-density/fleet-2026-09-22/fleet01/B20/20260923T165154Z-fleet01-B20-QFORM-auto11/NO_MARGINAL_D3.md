# Post-refresh strengthening: a physical third-volume block needs no marginal gate

Run: `20260923T165154Z-fleet01-B20-QFORM-auto11`  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM STILL OPEN**

This note supersedes the provisional “double-anchor survivor” conclusion in `REPORT.md`. It uses the new owner-linked restricted theorem in

`yspennstate/math-open-problems@4f92aeb74083c6f95cb314a11fed1b812eacef9a`

`proofnet24/QFORM-density/interactive/20260923T164118Z-full-proof-paper/NEW_PROJECTED_CROSSING.md`,

whose complete written proof gives the grouped-hub arbitrary-rank projected-crossing estimate. The unrestricted QFORM conjecture is explicitly still open there. The direct diffuse third-volume receiver used in the first branch remains Theorem D from

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.

The three-hub terminal receiver is Theorem 6.3 in the current continuation

`yspennstate/math-open-problems@c4c23b784395630c094ba299a50712209921d1ae`

`proofnet24/QFORM-density/interactive/20260922T231000Z-semidefinite-and-hub-reduction/README.md` and its cited `single_hub_core/REPORT.md`.

All banks below are literal ORIGINAL-coordinate banks. No rotated coordinate is declared independent.

## Theorem — `QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1`

Let `A` be an arbitrary real symmetric matrix and let `I,J` be disjoint sets of original coordinate indices. Put

`M=A[I,J]`,

`Z_3=e_3(M M^T)
    =sum_{|R|=|C|=3} det(M[R,C])^2`.

Assume `Z_3>0`. Let the coordinates of `X` be independent with densities at most one. Then the FULL ambient quadratic form `Q=X^T A X` has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= C_3 Z_3^(-1/6),
 C_3=3*2^(4/3)*exp(1/3)
     =10.5501688311... .`

There is **no row- or column-marginal hypothesis** in this theorem. Same-bank quadratic blocks, every diagonal, all outside coordinates and all exterior couplings are arbitrary.

### Proof

Normalize the squared `3x3` minors of `M` to the probability law

`w_(R,C)=det(M[R,C])^2/Z_3`,

and let

`alpha_i=P(i in R)` for `i in I`.

There are four exhaustive branches.

### Branch 0: diffuse third-volume rows

If every `alpha_i<=1/2`, the reviewed physical Theorem D applies directly to the literal cross block `M` and gives

`||p_Q||_infinity <=6 sqrt(e) Z_3^(-1/6)`.

Since `6sqrt(e)=9.8923276...<C_3`, the desired estimate follows, with continuous `C_0` density.

### Branch 1: promote one heavy row to an original hub

Suppose `alpha_i>1/2` for some physical row `i`. Write

`m=M[i,J]`,

`N=M[I\{i},J]`,

and let `Pi_m` be the orthogonal projection in `R^J` onto `span(m)`. Define

`C_1=N(I-Pi_m)`,

`S_1=||m||_2`,

`Z_2=e_2(C_1 C_1^T)`.

The row-anchored third-volume mass is

`W_i=sum_(R contains i, |R|=|C|=3) det(M[R,C])^2`.

The exact identity

`boxed: W_i=S_1^2 Z_2`

follows from Cauchy--Binet and Gram--Schmidt. Indeed, for two distinct residual rows `n_r,n_s`,

`sum_(|C|=3) det([m;n_r;n_s]_C)^2
 =det Gram(m,n_r,n_s)
 =||m||^2 det Gram(c_r,c_s)`,

where `c_r,c_s` are the corresponding rows of `C_1`; summing over unordered residual row pairs gives the identity.

Because `alpha_i>1/2`,

`S_1^2 Z_2=W_i>Z_3/2`.

Now view the single ORIGINAL coordinate `i` as a one-dimensional hub and split the light coordinates as `(I\{i}) | J`. The hub crossing into `J` is the row `m`, and the projected light crossing in the new grouped-hub theorem is exactly `C_1`.

If every natural order-two row marginal of `C_1` is at most `1/2`, the one-hub, `ell=2` consequence of the new projected-crossing theorem gives

`||p_Q||_infinity
 <=3*2^(7/6)*exp(1/3) (S_1^2 Z_2)^(-1/6)
 <3*2^(4/3)*exp(1/3) Z_3^(-1/6)
 =C_3 Z_3^(-1/6).`

This receiver retains arbitrary internal hub functions and arbitrary same-side light curvature.

### Branch 2: promote a second heavy projected row

Otherwise some physical residual row `r in I\{i}` has order-two projected-volume marginal greater than `1/2` in `C_1`. Let `c_r` be its row in `C_1` and put

`B_2=[m;n_r]`,

where `n_r=M[r,J]`. Since the marginal is positive, `c_r!=0`, so `B_2` has row rank two. Let

`S_2=s_1(B_2)s_2(B_2)=sqrt(det(B_2 B_2^T))
   =||m|| ||c_r||`.

For every remaining row `s`, project `n_s` orthogonally to `row(B_2)` and denote the resulting row by `d_s`. Let `D` be the matrix with rows `d_s` and

`Z_1=e_1(D D^T)=sum_s ||d_s||^2`.

The order-two volume incident to row `r` in `C_1` is

`V_r=sum_(s!=r) det Gram(c_r,c_s)
    =||c_r||^2 Z_1`.

Therefore the original third-volume mass containing **both** physical rows `i,r` is

`W_(i,r)
 =||m||^2 V_r
 =S_2^2 Z_1
 > (1/2)S_1^2 Z_2
 > Z_3/4.`

Now take the two ORIGINAL coordinates `{i,r}` as a two-dimensional hub. Their crossing into `J` is `B_2`, with singular-value product `S_2`, and the projected remainder crossing is exactly `D`.

If every order-one row marginal of `D` is at most `1/2`, equivalently

`||d_s||^2<=Z_1/2` for every `s`,

the grouped-hub theorem with `k=2`, `ell=1` (for which its exponential factor is omitted) gives

`||p_Q||_infinity
 <=3*2^(5/6) (S_2^2 Z_1)^(-1/6)
 <3*2^(7/6) Z_3^(-1/6)
 <C_3 Z_3^(-1/6).`

Again all internal hub and same-side light terms are retained.

### Branch 3: three physical hubs

Finally suppose the order-one marginal gate also fails. Then some remaining physical row `s` has

`||d_s||^2>Z_1/2`.

Let

`B_3=[m;n_r;n_s]`.

Gram--Schmidt gives

`det(B_3 B_3^T)
 =S_2^2 ||d_s||^2
 > (1/2)S_2^2 Z_1
 > Z_3/8.`

Thus the product `S_3` of the three singular values of `B_3` satisfies

`S_3^2>Z_3/8`.

Take the three ORIGINAL coordinates `H={i,r,s}` as the hub bank. The full off-diagonal block `A[H,H^c]` contains the columns `J` represented by `B_3`. Adding its other columns only adds a positive-semidefinite matrix to `B_3B_3^T`, so the product of the three singular values of the full hub crossing is at least `S_3`.

The proved three-hub theorem therefore gives

`||p_Q||_infinity
 <=3 sqrt(2) S_3^(-1/3)
 <3 sqrt(2) *8^(1/6) Z_3^(-1/6)
 =6 Z_3^(-1/6)
 <C_3 Z_3^(-1/6).`

The characteristic-function estimates in all four receiver branches have an integrable `|t|^(-3/2)` (or stronger) tail, so the density is continuous and vanishes at infinity. This proves the theorem. QED.

## Corollary: fleet02/B20 in-plane diffuse carrier is fully paid

The completed fleet02/B20 packet gives

`rank(S_0)<=5`,

`s_3(S_0)>1597/2000`,

`||A-S_0||_op<403/2000`.

The physical rank-five paving proved in this run shows that if

`max_i (P_(S_0))_(ii)<=1/25`,

there is a literal original-coordinate cut `I|J` for which

`s_3(A[I,J])>19/1000`.

Consequently

`Z_3=e_3(A[I,J]A[I,J]^T)>(19/1000)^6`.

Applying `QFORM-PHYSICAL-D3-NO-MARGINAL-GATE-v1` gives the unconditional payment

`boxed:
 ||p_Q||_infinity
 < C_3 *1000/19
 =555.2720437455... <556,`

with a continuous `C_0` density.

Thus the in-plane rank-at-most-five branch from the completed fleet02/B20 compiler has only **one** remaining survivor:

`boxed: max_i(P_(S_0))_(ii)>1/25.`

The provisional double-anchor survivor in `REPORT.md` is not a final debt: the new projected-crossing theorem pays it by successively promoting heavy physical volume rows to one, two and finally three genuine original-coordinate hubs.

The full QFORM conjecture nevertheless remains **OPEN**. The partner's transverse near-rank-two Frobenius collar remains a separate debt, and the heavy-leverage in-plane carrier above still requires a product-valid whole-law receiver.

## Correction/scope audit

- The proof never chooses a large individual minor from aggregate volume.
- Every promoted hub is an ORIGINAL coordinate, so independence is genuine.
- Projection is used only inside deterministic coefficient matrices; projected random variables are never declared independent.
- No small nonzero quadratic tail is dropped.
- No uniform pointwise scalar quadratic oscillatory decay is used.
- Same-bank curvature and outside couplings remain present in every invoked receiver.
- No additional probabilistic assumptions are introduced.
