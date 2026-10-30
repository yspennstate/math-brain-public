SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B03, 2026-09-24T07:52:12Z.
attacking: partial source overlap in the decoupled time integral — two independent physical hub groups may share the entire slope bank; combine their separate marginal Plancherel gains before any conditional density is formed.

# Shared-slope split-hub Fourier theorem

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **new supporting theorem / designated fleet02-B03 result applied / exact target family / full QFORM OPEN / unrestricted continuity OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Motivation and first missing implication

The preceding fleet01/B03 compiler paid a critical two-hub packet when the residual weighted collision resource was source-disjoint on one side. The newest fleet02/B03 r51 result identified the next debt as source-disjointification / partial-overlap: can a negative-half or third smoothing resource share the same coefficient bank as the two-slope packet without conditioning on that bank and thereby destroying density caps?

The answer is yes for an important exact architecture. One does **not** need the two slope vectors to be independent, or even jointly absolutely continuous. It is enough that they are attached to two disjoint physical hub groups and that the quadratic hub block has no cross term between those two groups. The two marginal Plancherel gains can then be combined by Cauchy--Schwarz over the common environment **before** any reciprocal coefficient or conditional density is paid.

This directly avoids the live corrections `QFORM-UV-CONDITIONAL-CAP-FALSE` and `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`: no conditional law of one slope given the other is capped, and no absolute mixed fiber norm is integrated.

## 2. The theorem

### Theorem — `QFORM-SHARED-SLOPE-SPLIT-HUB-L1-v1`

Let `r,s>=1`, `d=r+s>2`. Let

- `U=(U_1,...,U_r)` and `V=(V_1,...,V_s)` be disjoint collections of independent real random variables, each coordinate having a probability density bounded by one;
- `Y` be an arbitrary random object, independent of `(U,V)`;
- `L=L(Y) in R^r` and `M=M(Y) in R^s` have Lebesgue densities `p_L,p_M` satisfying
  `||p_L||_infinity <= K_L` and `||p_M||_infinity <= K_M`;
- **no independence is assumed between `L` and `M`**; they may be deterministic functions of one another on part or all of their support;
- `C` and `D` be arbitrary real symmetric `r x r` and `s x s` matrices;
- `R=R(Y)` be arbitrary measurable real-valued phase.

Define

`Q = U^T C U + V^T D V + 2 U^T L(Y) + 2 V^T M(Y) + R(Y).`

Then for every `t != 0`,

`boxed: |phi_Q(t)|^2 <= min{1, pi^d K_L K_M |t|^{-d}}.`

Consequently `phi_Q in L^1(R)` and `Q` has a continuous density vanishing at infinity with

`boxed: ||p_Q||_infinity <= [d/(d-2)] (K_L K_M)^(1/d).`

In particular, for the critical `2+1` split,

`boxed: ||p_Q||_infinity <= 3 (K_2 K_1)^(1/3).`

If the scalar slope appears as `2 gamma V M(Y)` in the `s=1` factor and the unscaled `M(Y)` has density cap `K_1`, then the scaled slope has cap `K_1/|gamma|`, hence

`boxed: ||p_Q||_infinity <= 3 (K_2 K_1/|gamma|)^(1/3).`

Arbitrary deterministic affine terms in `U,V` are absorbed by translating `L,M`; arbitrary affine/quadratic terms involving only `Y` are absorbed in `R(Y)`.

The only structural exclusion in this theorem is a quadratic cross term between the physical hub groups `U` and `V`. Self-curvature inside each group is completely arbitrary.

## 3. Proof

For fixed `t`, set

`F_t(l) = integral_{R^r} [prod_i f_i(u_i)] exp(i t u^T C u + 2 i t l^T u) du`,

`G_t(m) = integral_{R^s} [prod_j g_j(v_j)] exp(i t v^T D v + 2 i t m^T v) dv`.

Independence of `U,V,Y` and absence of `U-V` quadratic coupling give the exact conditional factorization

`phi_Q(t) = E_Y[ exp(i t R(Y)) F_t(L(Y)) G_t(M(Y)) ].`

Crucially, `L(Y)` and `M(Y)` may be arbitrarily dependent. Apply Cauchy--Schwarz **only in the common environment `Y`**:

`|phi_Q(t)|^2 <= E|F_t(L)|^2 * E|G_t(M)|^2.`

We now bound the two factors separately using only their **marginal** slope densities.

For the `U` block,

`E|F_t(L)|^2 <= K_L integral_{R^r} |F_t(l)|^2 dl.`

Write

`h_t(u) = [prod_i f_i(u_i)] exp(i t u^T C u)`.

With Fourier convention `hat h(xi)=integral h(u) exp(i xi^T u) du`, one has `F_t(l)=hat h_t(2t l)`. Hence the change of variables `xi=2t l` and Plancherel give

`integral |F_t(l)|^2 dl`
`= (2|t|)^(-r) integral |hat h_t(xi)|^2 dxi`
`= (2|t|)^(-r) (2pi)^r integral |h_t(u)|^2 du`
`<= pi^r |t|^{-r}`,

because

`integral |h_t|^2 = prod_i integral f_i^2 <= prod_i (||f_i||_infinity integral f_i) <=1.`

Therefore

`E|F_t(L)|^2 <= pi^r K_L |t|^{-r}.`

Exactly the same argument gives

`E|G_t(M)|^2 <= pi^s K_M |t|^{-s}.`

Multiplying,

`|phi_Q(t)|^2 <= pi^(r+s) K_L K_M |t|^{-(r+s)}`.

Together with the trivial `|phi_Q(t)|<=1`, this is the claimed envelope.

Set

`K = pi^d K_L K_M`,
`T = K^(1/d) = pi (K_L K_M)^(1/d).`

Then

`|phi_Q(t)| <= min{1, K^(1/2)|t|^{-d/2}}.`

Since `d>2`,

`integral_R |phi_Q(t)| dt`
`<= 2[ T + K^(1/2) integral_T^infinity t^(-d/2) dt ]`
`= 2 T [1 + 2/(d-2)]`
`= 2 pi [d/(d-2)] (K_L K_M)^(1/d).`

Fourier inversion therefore gives a continuous `C_0` density and

`||p_Q||_infinity <= (2pi)^(-1) integral |phi_Q|`
`<= [d/(d-2)] (K_L K_M)^(1/d).`

QED.

## 4. Assignment-specific whole-copy time integral

The independent-copy identity is used only at the whole-output level:

`|phi_Q(t)|^2 = E exp(i t (Q-Q'))`,

where `Q'` is an independent copy of the entire scalar output. We do **not** split any coordinate pair into `X-X'` and `X+X'`, and no conditional density cap for such a pair is asserted.

The proved envelope gives, for every `d>2`,

`A_-(Q):=integral_R |t|^(-1/2)|phi_Q(t)|^2 dt`
`<= [8d/(2d-1)] sqrt(pi) (K_L K_M)^(1/(2d)).`

Indeed, with the same crossover `T=pi(K_LK_M)^(1/d)`,

`A_- <= 2[ integral_0^T t^(-1/2) dt + K integral_T^infinity t^(-d-1/2) dt ]`
`= [8d/(2d-1)] T^(1/2).`

Using the exact one-dimensional Riesz identity

`integral_R |t|^(-1/2) exp(i t x) dt = sqrt(2pi) |x|^(-1/2)`

in the usual regularized sense,

`boxed: E|Q-Q'|^(-1/2) <= [4 sqrt(2) d/(2d-1)] (K_L K_M)^(1/(2d)).`

For the critical `d=3` case,

`boxed: A_-(Q) <= (24/5)sqrt(pi)(K_LK_M)^(1/6),`

`boxed: E|Q-Q'|^(-1/2) <= (12sqrt(2)/5)(K_LK_M)^(1/6).`

For completeness, the same envelope also yields the positive-half budget

`A_+(Q):=integral |t|^(1/2)|phi_Q(t)|^2 dt`
`<= [8d/(3(2d-3))] pi^(3/2) (K_LK_M)^(3/(2d)).`

At `d=3`, this is

`A_+(Q) <= (8/3)pi^(3/2)(K_LK_M)^(1/2).`

Thus this theorem simultaneously supplies the assigned negative-half collision currency **and** the stronger one-copy `L^1_t` estimate needed for linear small-ball scaling.

## 5. Exact application of the designated fleet02/B03 result

The newest completed fleet02/B03 r51 report is

`yspennstate/math-open-problems@2d69242a9eb20165a65b4493a66a7f73995c43c2`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B03/20260924T072538Z-fleet02-B03-QFORM-auto11-r51/REPORT.md`.

Its Proposition 2.1 proves the two-slope random-hub Plancherel estimate. In the notation above with `r=2`, it contains the actual inequality

`E|F_t(L)|^2 <= pi^2 K_2 |t|^{-2}`

before the later source-disjoint weighted-time splice. This run applies that inequality literally. For the scalar hub block, the identical one-dimensional Plancherel calculation gives

`E|G_t(M)|^2 <= pi K_1 |t|^{-1}`.

Even though `L` and `M` are generated by the **same** `Y` and may be maximally dependent, Cauchy--Schwarz over `Y` gives

`boxed: |phi_Q(t)|^2 <= pi^3 K_2 K_1 |t|^{-3}.`

Thus the partner's two-slope estimate is not merely cited: it is one of the two factors in the actual inequality that closes the shared-source `2+1` packet.

The r51 source-disjoint splice required independence of the resulting scalar packets `S,T`; the present theorem removes that independence requirement at the slope-bank level, provided the physical hubs themselves split into two uncoupled groups.

## 6. Strict target family with maximal slope overlap

Take five genuine independent cap-one coordinates

`U_1,U_2,V,Y_1,Y_2`

and define

`Q = 2 U_1 Y_1 + 2 U_2 Y_2 + 2 V Y_1.`

Here

`L=(Y_1,Y_2)`, so `K_2<=1`,
`M=Y_1`, so `K_1<=1`,

and the scalar slope is literally the first coordinate of the two-dimensional slope. Hence the slope resources are **maximally overlapping**, not source-disjoint and not jointly three-dimensional.

The theorem gives

`boxed: ||p_Q||_infinity <=3,`

with a continuous `C_0` density, and every interval `I` satisfies

`boxed: P(Q in I) <=3 |I|.`

The symmetric coefficient matrix is the bipartite block matrix

`A = [[0,B],[B^T,0]]`,

with

`B = [[1,0],[0,1],[1,0]].`

Since

`B^T B = diag(2,1)`,

the nonzero spectrum of `A` is exactly

`{+sqrt(2), -sqrt(2), +1, -1}`,

with one additional zero eigenvalue. Therefore this is an exact owner-target family with four eigenvalues of modulus at least one.

For this family,

`A_-(Q) <= (24/5)sqrt(pi) = 8.507778484346476...`,

`E|Q-Q'|^(-1/2) <= 12sqrt(2)/5 = 3.394112549695428...`,

`A_+(Q) <= (8/3)pi^(3/2) = 14.848874658217888... .`

This family is a clean witness that a shared slope source does not itself obstruct linear small-ball scaling; the correct operation is to keep the shared environment intact until the two marginal Plancherel budgets have been formed.

## 7. Scope and remaining gap

This theorem is not the unrestricted QFORM theorem. It pays a meaningful partial-overlap architecture but requires a product-preserving physical hub split with no quadratic cross term between the two hub groups. In an arbitrary symmetric matrix, a chosen three-hub physical block need not admit such a `2+1` zero-cross partition, and one cannot rotate the physical hubs to manufacture it because rotations destroy product independence.

The next analytic question is therefore sharper:

`QFORM-CROSS-HUB-SHARED-SLOPE-BRIDGE` — can the same marginal-Plancherel mechanism survive a nonzero deterministic cross block `2 U^T E V`, perhaps through an operator-valued / mixed-norm estimate that keeps the common environment coupled until after both hub integrations?

A naive conditioning argument is not acceptable: it would require a bounded density for `M|L` or `L|M`, precisely the type of interface already refuted by the live correction corpus. If that cross-hub extension fails, the structural route must extract an uncoupled split-hub packet or route the survivor to the already-paid grouped-hub / ridge / principal-pair mechanisms.

Full universal boundedness: **OPEN**.
Full-target continuous density: **OPEN**.

## 8. Source / correction ledger

Fresh controls read from `yspennstate/math-research-brain` main with observed control revision `2026-09-22.15`. Required programme state and assignment were reread. Relevant corrections consumed include:

- `QFORM-POINTWISE-DECAY-FALSE`;
- `QFORM-UV-CONDITIONAL-CAP-FALSE`;
- `QFORM-ABSOLUTE-AMBIGUITY-HOLDER-LOG-LOSS`;
- `QFORM-HUBSTAR-FIBERL2-MIXEDNORM-UNIVERSAL-FALSE-v1`.

No Gaussian, log-concave, moment, compact-support, connected-support, diagonal-basis, conditional-density, or rotated-independence assumption is used.
