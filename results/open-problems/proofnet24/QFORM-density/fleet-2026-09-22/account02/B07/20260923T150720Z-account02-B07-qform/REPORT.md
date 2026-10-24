SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B07, 2026-09-23T15:07:20Z.
attacking: the partner r32 star-star plus aggregate-E2 survivor — regenerate a third-compound packet by determinant-weighted physical pivot averaging, or force the far physical block into a genuine rank-two tube without paying one reciprocal coordinate.

# account02/B07 — anchored compound pivot downgrade

Status: `NEW_STAR-E2-TO-E3-OR-R2TUBE_COMPILER / DESIGNATED_PARTNER_APPLIED / BOUNDED-SUPPORT CORE PAID / EXACT TARGET STRESS / FULL_QFORM_OPEN / WITHOUT_VERIFIED_BRAIN`.

Fresh owner control before this write: `yspennstate/math-research-brain@06de7635862ca416dc52deb2d305c2c50d1106e5`; OWNER CONTROL revision `2026-09-22.15`, QFORM-only, no B07 pause/reassignment. Required Claude/Fourier source was read at the pinned base `e5f71d79eff325201dd0274053d20268ce65b837` and at compatible master `cf899d49f739244e9df6759c1cda8fdc5ead5c6b`. The latest designated-partner handoff used below is account03/B07 r32, canonical mathematics `math-open-problems@b684b8edb29274a17fd5e8ed7fc8049ce12a4595`.

## First unpaid implication after this result

`QFORM-R32-R2TUBE-OR-R1CYCLE-MIXEDHUB-STABILITY-v1`: once the theorem below has removed every star+E2 state that regenerates usable third volume, consume the remaining physical rank-two tube (and r32's separate coherent four-block rank-one-cycle tube) while preserving the nonzero tail and arbitrary same-bank curvature. The completed volume-stability theorem explicitly does not cover a rank-two cross block with an arbitrarily small third singular value, so the missing step is a genuine low-cross-rank/hub stability theorem, not another bounded-core extraction.

## 1. New theorem — `QFORM-STAR-E2-TO-E3-OR-R2TUBE-v1`

All indices below are ORIGINAL physical coordinates. Let one physical row `u`, a disjoint star-column bank `J0`, residual row bank `I`, and residual column bank `J` be fixed. Write the corresponding physical cross block as

`M = [[s^T, r^T], [C, K]]`,

where `s in R^{J0}`, `r in R^J`, `C in R^{I x J0}`, and `K in R^{I x J}`. Put `S=||s||_2>0`.

For every `j in J0` with `s_j != 0`, define the physical-slice Schur residual

`K_j = K - C[:,j] r^T / s_j`.

Define the star-supported anchored third-compound packet

`G_* = sum_{j:s_j!=0} sum_{|R|=2, R subset I} sum_{|T|=2, T subset J}
          det M[{u} union R, {j} union T]^2`.

Then the exact identity

`boxed:  G_* = sum_{j:s_j!=0} s_j^2 E_2(K_j)`                                      (1.1)

holds, where `E_2(L)=e_2(L^T L)` is the full squared `2x2`-minor mass of `L`. Consequently

`boxed: dist_F(K, rank<=2) <= (2 G_*/S^2)^(1/4).`                                 (1.2)

More generally, for every lower bound `Omega <= E_2(K)` and every `0<eps<1`, exactly one need not hold but at least one of the following always holds:

`boxed: G_* >= (eps^4/2) S^2 Omega,`                                                (1.3)

or

`boxed: dist_F(K, rank<=2) < eps Omega^(1/4).`                                     (1.4)

This is determinant-weight aggregation before reciprocal selection. The proof selects a physical pivot only to construct a structural approximant; the final estimate contains no inverse pivot magnitude.

### Proof

Fix `j` with `s_j != 0`, two residual rows `p,k`, and two residual columns `q,l`. Subtract `(C_pj/s_j)` times the first row from row `p`, and `(C_kj/s_j)` times the first row from row `k`. This preserves the determinant and gives

`det M[{u,p,k},{j,q,l}] = s_j det K_j[{p,k},{q,l}]`.

Squaring and summing proves (1.1). Averaging `E_2(K_j)` with weights `s_j^2/S^2` therefore gives a nonzero actual star pivot `j_*` with

`E_2(K_{j_*}) <= G_*/S^2`.                                                         (1.5)

For any matrix `L`, let squared singular values be `x_1>=x_2>=...` and set `T=sum_{nu>=2}x_nu`. Then `T=dist_F(L,rank<=1)^2`, while

`2 E_2(L) = 2 x_1 T + T^2 - sum_{nu>=2}x_nu^2 >= T^2`,

because `sum_{nu>=2}x_nu^2 <= x_1 T`. Hence

`dist_F(L,rank<=1) <= (2E_2(L))^(1/4)`.                                           (1.6)

Finally `K = K_{j_*} + C[:,j_*] r^T/s_{j_*}`, a rank-one correction. Approximating `K_{j_*}` by rank one and adding that correction gives a rank-at-most-two approximation of `K`; (1.2) follows from (1.5)-(1.6). Splitting according to whether `G_*` is at least `(eps^4/2)S^2 Omega` proves (1.3)-(1.4).

## 2. Actual application to designated partner account03/B07 r32

Partner r32 proves that the r30 six-bank packet has, on its aggregate branch, two disjoint physical star banks of norms `S_L,S_R` and a four-bank residual rectangle with literal cross-minor mass `Omega`, satisfying

`S_L S_R sqrt(Omega) > a^4/(6912 sqrt(6)).`                                       (2.1)

Its four residual blocks are all retained; crossed blocks are not deleted. Apply Theorem 1 to either physical star and to the full residual matrix `K` containing the r32 bank-cycle minors. Since `Omega <= E_2(K)`, at `eps=1/8` one gets

`boxed: G_* >= S^2 Omega/8192`                                                     (2.2)

or

`boxed: dist_F(K,rank<=2) < Omega^(1/4)/8.`                                       (2.3)

Thus an aggregate E2 bank plus a genuine physical star cannot simply disappear: it either regenerates an aggregate physical third-compound packet or forces the entire far cross block into a dimension-free rank-two Frobenius tube. This directly advances r32's first unpaid aggregate-E2 receiver without selecting one `2x2` minor.

### 2.1 Required newest-Claude result applied to a real inequality

Use the proved D' volume-sampling theorem from the required `e5f71d79...` source. If either orientation of the natural determinant-volume law of the packet `G_*` in (2.2) has every inclusion marginal at most `2/3`, then arbitrary same-bank quadratic curvature, outside couplings, affine terms, and extra spectrum are all retained and

`||p_Q||_inf <= 9 sqrt(3e) G_*^(-1/6)`

`             <= 9 sqrt(3e) 8192^(1/6) (S^2 Omega)^(-1/6)`

`boxed:       < 115.394 (S^2 Omega)^(-1/6).`                                     (2.4)

This is a genuine full-ambient analytic payment on the regenerated-E3 branch. No Schur-completion survival of the original E2 packet is assumed.

### 2.2 Bounded physical support closes by an actual spectral core

The complementary bounded-support branch is also complete. Normalize the squared determinants in `G_*` to a probability law. Suppose original row/column support sets `R0,C0` leave total inclusion-marginal tail `delta<1`. The union bound retains at least `(1-delta)G_*` in the physical cross block `B=A[R0,C0]`, hence

`E_3(B) >= (1-delta)G_*`.                                                          (2.5)

Let `r0=min(|R0|,|C0|)` and `L=||B||op`. Since every term in `e_3(s_1(B)^2,...)` is at most `L^4 s_3(B)^2`,

`s_3(B) >= sqrt((1-delta)G_*) / (sqrt(C(r0,3)) L^2).`                             (2.6)

The symmetric principal block on `H=R0 union C0` has third singular value at least `s_3(B)`. Conditioning only on ORIGINAL coordinates outside `H` leaves a bounded-dimensional quadratic-plus-affine form. The compatible current fixed-dimensional theorem (`||p||<=250 m(8+log m)` at unit third spectral scale, uniformly in affine terms) therefore yields, for `m=|H|`,

`boxed:
 ||p_Q||_inf <= 250 m(8+log m) sqrt(C(r0,3)) L^2 / sqrt((1-delta)G_*).`             (2.7)

So every fixed-cardinality determinant-support branch is paid without asserting a universally good individual minor. In the strict no-pivot chamber the physical coefficient cap gives a further dimension-only bound on `L` for fixed `m`.

The only regenerated-E3 states not disposed of by (2.4) or (2.7) are genuinely support-diffuse and coheavy; they feed the already-existing B07 double-anchor descent rather than a reciprocal-minor argument.

## 3. Exact target-class stress — the rank-two alternative is necessary

For every even `N`, let

`s=a=b=N^(-1/2)(1,...,1)`,
`x=y=N^(-1/2)(1,-1,1,-1,...)`,

with `a,x` orthonormal and `b,y` orthonormal. Set

`C=a s^T`,
`K=a b^T + x y^T`,
`M_N=[[s^T,b^T],[C,K]]`,
`A_N=[[0,M_N],[M_N^T,0]]`.

Then

`M_N = [1;a] [s;b]^T + [0;x][0;y]^T`,

and the two summands have orthogonal left and right factors. Therefore the nonzero singular values of `M_N` are exactly `2,1`, and the nonzero spectrum of `A_N` is

`boxed: {2,1,-1,-2}.`                                                             (3.1)

So this is a valid target family with four eigenvalues of modulus at least one. The far block `K` has singular values `1,1`, hence `E_2(K)=1`, while for every star pivot `j`,

`K_j = K - (C[:,j]/s_j)b^T = x y^T`,

so

`boxed: S=1, E_2(K)=1, G_*=0.`                                                     (3.2)

Thus no inequality of the form `G_* >= c S^2 E_2(K)` can hold universally: the rank-two-tube alternative in Theorem 1 is essential.

This family also defeats a bounded-cardinality core shortcut. Every physical coefficient has magnitude at most `N^(-1/2)`, so for every fixed physical `H`,

`||A_N[H,H]||op <= ||A_N[H,H]||F <= |H| N^(-1/2) -> 0`.                           (3.3)

For `N>128`, all physical diagonals vanish and every physical `2x2` principal determinant has magnitude at most `1/N<1/128`, so the family lies in the standard no-pivot chamber as well.

This is not a QFORM counterexample. It is paid by a completed theorem from the required Fourier source. The range projection of `A_N` has maximum physical leverage exactly `1/2` (at the single anchor row); all other leverages are `O(1/N)`. The proved rank-`r` Fresnel-Brascamp-Lieb theorem therefore applies with `r=4` and eigenvalue product `|2*1*(-1)*(-2)|=4`, giving

`boxed: ||p_{X^T A_N X}||_inf <= [4r/(r-2)]*4^(-1/4) = 4 sqrt(2) < 5.657.`          (3.4)

This source-valid stress identifies the correct geometry: star+E2 can collapse all anchored third volume through an exact rank-two residual cancellation while still satisfying the full spectral target. The right next mechanism is low-rank/hub Fourier stability, not bounded-core extraction.

## 4. Relation to r32's other branch

Partner r32's complementary small-`Omega` branch forces all four residual bank blocks into simultaneous rank-one Frobenius tubes by determinant-weighted physical pivot averaging. The present theorem is orthogonal to that result: on the aggregate-`Omega` branch it forces `E3` regeneration or a rank-two tube; on the cancellation branch r32 already supplies the rank-one-cycle tube. Both surviving geometries are now explicitly low-cross-rank/hub states. The volume-stability report at `c2414ef...` states that rank-two tubes with arbitrarily small third singular value are outside its scope, so no density claim is made for the nonzero-tail tube solely from its Frobenius closeness.

## 5. Scope and correctness

No moments, bounded support, log-concavity, iid assumption, diagonal-basis assumption, or rotation of random coordinates is used. All conditioning is on original coordinates. The determinant packet is carried before inversion. A tiny selected physical pivot appears only inside a structural rank-one correction; its reciprocal is never paid in an analytic bound. The exact stress family is a counterexample only to the intermediate `star times E2 => E3/bounded-core` shortcut, not to QFORM.

Full QFORM remains `OPEN / NOT PROVED / NOT DISPROVED`. Full-target continuity remains separate.
