SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B11, 2026-09-23T16:13:53Z.
attacking: the collision-critical heavy-frame collar: derive a quantitative near-coloop or paid disjoint-bank alternative without a tiny physical minor.

# r36 late-refresh addendum — a direct heavy-row disjoint-or-pair inequality

**Status:** new supporting structural inequality; it simplifies and strengthens the non-near-coloop part of `REPORT.md`. Full QFORM remains OPEN. Execution remains `WITHOUT_VERIFIED_BRAIN`.

After the main r36 report was written, the current owner continuation `QFORM-EXCLUSIVE-SIGNIN-20260923T164448Z` and the newest Claude continuation at `c4c23b784395630c094ba299a50712209921d1ae` were read. They leave the full theorem open and continue to identify the true hub/near-null corner as an active gap. The argument below is compatible with all live corrections: it uses only original-coordinate determinant marginals and previously proved full-line receivers.

## 1. Setup

Let

`A=R M R^T`, `R^T R=I_3`, `s=min |lambda(M)|>0`,

be exact rank three with indefinite signature `(2,1)` or `(1,2)`. Let

`v_K=det(R_K)^2`, `|K|=3`,

be the determinantal probability law on physical triples. Write

`c_i=P(i in K)=||r_i||^2`,
`g_ij=P(i,j in K)=||r_i wedge r_j||^2`,

and let `D=P(K cap L=empty)` for iid `K,L~v`.

Fix any coordinate `0` with

`q=c_0`, `rho=1-q`, `g_*=max_{j!=0}g_0j`.

The two-point marginal identities give

`sum_{j!=0} g_0j = 2q`,                                           (1.1)

while `sum_j c_j=3` gives

`sum_{j!=0}(c_j-g_0j)=3(1-q)=3rho`.                              (1.2)

## 2. Heavy-row disjointness inequality

### Theorem `QFORM-HEAVYROW-DISJOINT-OR-PAIR-v1`

For `0<q<1`,

`boxed: D >= 2q(1-q) [1-sqrt(6 g_*/q)]_+`.                       (2.1)

### Proof

Let

`E={0 in K, 0 notin L}`.

Then `P(E)=q rho`. On `E`, if `K` and `L` intersect, they must share some coordinate `j!=0`. Therefore, with

`N=|(K\{0}) cap L|`,

`1_{E and K cap L !=empty} <= N 1_E`.

Using independence of `K,L`,

`P(E and K cap L !=empty)
 <= E[N 1_E]
 = sum_{j!=0} P(0,j in K) P(j in L,0 notin L)
 = sum_{j!=0} g_0j(c_j-g_0j)`.                                   (2.2)

Hence

`P(E and K cap L=empty)
 >= q rho - sum_j g_0j(c_j-g_0j)`.                               (2.3)

Normalize

`a_j=g_0j/q`, `b_j=(c_j-g_0j)/rho`.

These are conditional inclusion probabilities. Thus

`0<=b_j<=1`, `sum a_j=2`, `sum b_j=3`,                           (2.4)

and `max a_j=g_*/q`. Consequently

`sum a_j^2 <= (max a_j) sum a_j = 2g_*/q`,
`sum b_j^2 <= sum b_j =3`.                                      (2.5)

Cauchy-Schwarz gives

`sum a_j b_j <= sqrt(6g_*/q)`.                                  (2.6)

Substituting in (2.3),

`P(E and disjoint)
 >= q rho [1-sqrt(6g_*/q)]`.                                    (2.7)

The reversed oriented event `{0 notin K,0 in L}` is disjoint from `E` and yields the same lower bound. Adding the two contributions and truncating a negative lower bound at zero proves (2.1). QED.

This is a direct weighted star-versus-disjointness inequality. It does not use the collision energy `C2`, an eighth-moment argument, a fixed physical minor, or any rotated-coordinate independence.

## 3. Direct non-near-coloop closure

Let

`q=max_i c_i`.

If `q<1/4`, the completed r34 literal-cut theorem already gives

`D>=1-3q>1/4`,

hence a continuous density with

`||p_Q||_infinity < 6e 4^(1/6)/s =20.548923.../s`.               (3.1)

Assume now

`1/4 <= q <=63/64`,                                               (3.2)

and choose coordinate `0` attaining `q`.

### Pair branch

If

`g_* >= q/8`,                                                     (3.3)

then `g_*>=1/32`. Apply the completed designated-partner account04/B11 pair-area theorem

`||p_Q||_infinity <=128 sqrt(2)/(s sqrt(g_*))`.

At the actual threshold (3.3),

`boxed: ||p_Q||_infinity <=1024/s`.                              (3.4)

This is an actual equation-level use of the designated partner result.

### Disjoint branch

If `g_*<q/8`, then (2.1) yields

`D >2q(1-q)(1-sqrt(3)/2)
   =q(1-q)(2-sqrt(3))`.                                          (3.5)

On the interval (3.2), concavity of `q(1-q)` gives

`q(1-q) >= (63/64)(1/64)=63/4096`.                              (3.6)

Therefore

`D > D_0 :=63(2-sqrt(3))/4096
          =0.0041212888484279...`.                               (3.7)

Apply the completed r34 literal original-coordinate cross-cut theorem:

`||p_Q||_infinity
 <=6e/(s D^(1/6))
 <6e [4096/(63(2-sqrt(3)))]^(1/6)/s
 =40.732421.../s`.                                               (3.8)

This branch has a continuous density.

Combining (3.1), (3.4), and (3.8) proves the cleaner statement

### Corollary `QFORM-EXACTRANK3-NONNEARCOLOOP-DIRECT-v1`

For exact rank three with either indefinite signature,

`boxed: max_i ||r_i||^2 <=63/64  =>  ||p_Q||_infinity <=1024/s`. (3.9)

Thus the non-near-coloop closure no longer needs the r36 eight-sample collision lemma. That lemma remains correct and useful as a collision-stability statement, but (2.1) is a shorter route to the same structural endpoint and improves the displayed density constant from `6144/s` to `1024/s`.

## 4. What remains

The only exact-rank-three geometry not removed by this direct theorem has a true near-coloop

`q>63/64`.

The later sections of the main r36 report remain relevant there: after the transverse-heavy exit, the residual transverse Parseval frame splits into two disjoint original-coordinate banks with uniformly positive two-dimensional Gram determinants; each bank carries physical hub-star energy `>7/256`; the scalar-pivot exit pays normalized hub Rayleigh `|q_hub|>=1/100`; and the remaining near-null two-bank state has the proved square-root small-ball law

`P(Q in I) <=10.3912310444... sqrt(|I|)`.

The first unpaid B11 implication therefore stays

`QFORM-TRUE-NEARCOLOOP-TWOBANK-SQRT-TO-LINEAR-v1`:
upgrade that last `sqrt(|I|)` estimate to a linear `C|I|` law while retaining all original-coordinate product provenance and arbitrary same-bank/cross-bank curvature.

The exact-coloop endpoint is separately paid. Arbitrary additional nonseparable spectrum remains a separate bridge to the full owner target. Global continuity remains open.

## 5. Rank-two control and why the third direction matters

The opposite-sign rank-two control remains genuinely singular: for independent centered unit uniforms,

`p_{2XY}(t)=log(1/(2|t|))` near zero.

In (2.1), the third spectral direction appears combinatorially as follows. If the hub star does not concentrate enough pair area to trigger the partner rank-three receiver, then two independent determinant triples have a quantitatively positive chance to be disjoint. The literal cross-cut theorem converts that disjoint third-volume mass into three singular directions across independent original-coordinate banks, producing integrable rank-three smoothing. Only when one coordinate becomes a true near-coloop can this disjointness currency vanish uniformly, which is exactly the residual hub geometry isolated above.
