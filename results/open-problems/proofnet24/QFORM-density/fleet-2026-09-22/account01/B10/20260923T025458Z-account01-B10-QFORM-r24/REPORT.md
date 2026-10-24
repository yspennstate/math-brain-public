SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B10, 2026-09-23T02:54:58.876275Z.
attacking: orthogonal-leakage bordered hyperbolic closure in the singleton-heavy-hub exact-null branch.

# account01/B10 r24 — conditional-slope hyperbolic smoothing and a pure-curvature bank closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: arbitrary exact-rank-three coupled case  
Status: `ESSENTIAL_STEP_APPLIED / NEW_ANALYTIC_RECEIVER / TARGET_SUBBRANCH_CLOSED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full exact-rank-three theorem is **not** proved here. This run proves a new dependence-tolerant smoothing lemma that is strictly stronger than the previously available independent-hyperbolic-scalar theorem in one direction: the hyperbolic scalar may be arbitrarily dependent on the slope variable and arbitrary nuisance variables, provided its **conditional density given those variables** is bounded and the square-smoothing scalar is genuinely independent. The lemma then closes a natural endpoint of the singleton-heavy-hub/two-bank obstruction where one bank is a pure curvature bank. In particular it pays the exact target family used by the designated account02/B10 partner to refute single-local-minor selection.

## 1. Fresh source state and correction discipline

Fresh `main` control was read at startup with OWNER CONTROL revision `2026-09-22.15`, QFORM-only. Immediately before publication the protected README remained unchanged (blob `fca13a89d221115332ce5e60d49554ee0e213efa`), and the live correction inbox was refreshed (blob `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`).

The current correction record is enforced. In particular, this report does **not** use arbitrary-joint rank-three coarea, a positive conditional projection-height moment, post-rotation independence, a uniform pointwise quadratic-phase decay estimate, a fiber supremum, or a uniformly good single physical minor. It also respects `QFORM-CONDITIONAL-CAP-NOT-INDEPENDENCE-v1`: a conditional density cap for the hyperbolic variable does not by itself replace independence when the square variable is allowed to be correlated with it.

The new lemma below avoids that falsifier by keeping a genuinely independent square scalar.

## 2. Source-backed product projection input

I use the completed `QFORM-WEIGHTED-AFFINE-FIBER-BL-v1` from account02/B06,

`yspennstate/math-open-problems@8dd33c1abd4fd64140f59032feda2b13d4351da5`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B06/b06-20260922T155426Z-9fd56fa68a65/REPORT.md`.

For a normalized real linear form of independent cap-one inputs (coefficient Euclidean norm one), it gives the density cap

`||p_L||_infinity <= exp(1/2)=sqrt(e)`.                                  (2.1)

Only this one-dimensional consequence is used below.

## 3. New analytic receiver

### Theorem 3.1 — `QFORM-CONDITIONAL-SLOPE-INDEPENDENT-SQUARE-v1`

Let `(S,Y,W)` be any real/random-standard-Borel triple such that:

1. the regular conditional law of `S` given `(Y,W)` has a density bounded by `K_S` almost surely;
2. the marginal law of `Y` has a density bounded by `K_Y`;
3. `Z` is independent of `(S,Y,W)` and has density bounded by `K_Z`.

Let `a,b` be nonzero real numbers. Let `F=F(Y,W)` and `theta=theta(Y,W)` be arbitrary measurable functions; crucially neither may depend on `S`. Define

`T = 2 a S Y + F(Y,W) + b ( Z + theta(Y,W) )^2`.                       (3.1)

Then `T` has an essentially bounded density and

`boxed{
 ||p_T||_infinity
 <= 6 (K_S K_Y K_Z)^(2/3) |a|^(-2/3) |b|^(-1/3).
}`                                                                       (3.2)

No independence of `S` from `(Y,W)` is assumed.

#### Proof

Fix an output value `t` and a cutoff `delta>0`. Split the density according to `|Y|>=delta` and `|Y|<delta`.

**Far-slope part.** Condition on `(Y,W,Z)`. Because `Z` is independent of `(S,Y,W)`, conditioning additionally on `Z` does not change the conditional density bound for `S`. Since `theta` and `F` do not depend on `S`, (3.1) is affine in `S` with slope `2aY`. Therefore on `|Y|>=delta`,

`p_far(t) <= K_S/(2 |a| delta).`                                      (3.3)

**Near-slope part.** For fixed `(s,y,w)`, the translated square `b(Z+theta(y,w))^2` has density envelope

`g_{s,y,w}(u) <= K_Z / sqrt(|b| |u|)`                               (3.4)

on the appropriate half-line: the two inverse branches each contribute at most `K_Z/(2 sqrt(|b u|))`. Hence

`p_near(t)
 <= (K_Z/sqrt(|b|))
    E[ 1_{|Y|<delta}
       |t-2aSY-F(Y,W)|^(-1/2) ].`                                  (3.5)

For fixed `(Y,W)=(y,w)` with `y!=0`, the random variable `2ayS` has conditional density bounded by

`M_y = K_S/(2 |a y|)`.                                               (3.6)

For any probability density `h<=M`, the one-dimensional bathtub/rearrangement estimate gives

`sup_c int |c-v|^(-1/2) h(v) dv <= 2 sqrt(2M)`.                       (3.7)

Indeed the maximizing cap-`M`, mass-one profile is the interval of length `1/M` centered at `c`, and direct integration gives the right side. From (3.6)-(3.7),

`E[ |t-2aSY-F(y,w)|^(-1/2) | Y=y,W=w ]
 <= 2 sqrt(K_S/(|a y|)).`                                           (3.8)

Using only the marginal cap `p_Y<=K_Y`,

`E[1_{|Y|<delta}|Y|^(-1/2)]
 <= K_Y int_{-delta}^{delta}|y|^(-1/2)dy
 = 4 K_Y sqrt(delta).`                                               (3.9)

Thus

`p_near(t)
 <= 8 K_Z K_Y sqrt(K_S)
       |a|^(-1/2)|b|^(-1/2) sqrt(delta).`                            (3.10)

Put

`A=K_S/(2|a|)`,
`B=8 K_Z K_Y sqrt(K_S)|a|^(-1/2)|b|^(-1/2)`.

Equations (3.3),(3.10) give

`p_T(t) <= A delta^(-1)+B delta^(1/2)`.                              (3.11)

The minimum over `delta>0` occurs at `delta=(2A/B)^(2/3)` and equals

`3*2^(-2/3) A^(1/3) B^(2/3)
 = 6 (K_S K_Y K_Z)^(2/3)|a|^(-2/3)|b|^(-1/3).`                     (3.12)

The estimate is uniform in `t`, proving (3.2). The conditional pushforwards used above are absolutely continuous away from the null set `Y=0`, while the independent square variable handles that null-slope set; Tonelli yields an absolutely continuous mixture. QED.

### Why this does not contradict the live conditional-cap falsifier

The account02/B10 falsifier constructs correlated `(S,Y,Z)` with bounded `p_{S|Y,Z}` but chooses `S` so that the `Z^2` term cancels, leaving a logarithmically singular product. Theorem 3.1 requires the square variable `Z` to be genuinely independent of `(S,Y,W)`. That independent curvature leaf is exactly what prevents the cancellation.

## 4. Designated partner state actually consumed

The designated account02/B10 run

`20260922T225540Z-account02-B10-QFORM-auto11`,

canonical source

`yspennstate/math-open-problems@9005415f079b7b46c0618c0187bf29b3f8d44167`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B10/20260922T225540Z-account02-B10-QFORM-auto11/REPORT.md`,

proves the `QFORM-TRIPARTITE-HEAVY-HUB-DELETE-OR-ISOLATE-v1` reduction. In its hard isolatable alternative, after deterministic spectral whitening the active ORIGINAL-coordinate set is

`{h} union B_2 union B_3`,

with a Parseval frame `sum_i r_i r_i^T=I_3`, symmetric invertible spectral matrix `N`,

`|det N| >= 2^(-18)`, `sigma_min(N)>=2^(-18)`,                       (4.1)

hub

`r_h=sqrt(L)e_1`, `L>511/512`,                                      (4.2)

and fixed-hub exterior packet

`T_h=sum_{j in B_2,k in B_3} det(r_h,r_j,r_k)^2 >=1/512`.           (4.3)

My preceding B10 r23, `math-open-problems@144420aee51d6e70b9bc4daa6cc5cd4f3cc56da6`, showed that at an exact null hub one may orient the transverse basis by `N e_1` so that

`N = [[0,R,0],[R,p,q],[0,q,d]]`,                                    (4.4)

and therefore

`R^2 |d| = |det N|`.                                                 (4.5)

The new theorem below consumes (4.1)-(4.5) quantitatively.

## 5. Pure-curvature-bank endpoint of the hard hub state

### Theorem 5.1 — `QFORM-NULL-HUB-PURE-CURVATURE-BANK-v1`

Assume the exact-null hard-hub state (4.1)-(4.5). Suppose, in the `N`-oriented basis from (4.4), one of the two disjoint light banks, say `B_3`, is a pure curvature bank:

`r_k = z_k e_3` for every `k in B_3`.                               (5.1)

Then every admissible original product law satisfies

`boxed{ ||p_Q||_infinity <= 3072 e^(2/3) < 5983.439. }`              (5.2)

This conclusion permits completely arbitrary longitudinal leakage and arbitrary internal `e_3` contamination in the other bank `B_2`. In particular it does **not** assume that the hyperbolic scalar is independent of the slope variable.

#### Proof

For `j in B_2`, write

`r_j = a_j e_1 + y_j e_2 + z_j e_3`.                                (5.3)

Put

`m=sum_{k in B_3} z_k^2`.                                           (5.4)

Because the active frame is Parseval and the pure bank (5.1) carries no `e_2` component,

`sum_{j in B_2} y_j^2 = 1`.                                         (5.5)

For a fixed-hub triple,

`det(r_h,r_j,r_k)^2 = L y_j^2 z_k^2`.                              (5.6)

Summing (5.6) and using (5.5) gives the exact identity

`boxed{ T_h = L m. }`                                                (5.7)

This is the first actual use of the designated partner packet in this run. From (4.3),

`m >= 1/(512 L)`.                                                    (5.8)

Now define the original-product aggregates on `B_2`,

`A=sum_j a_j X_j`,
`Y=sum_j y_j X_j`,
`Z_0=sum_j z_j X_j`,

and on `B_3`,

`Z_3=sum_k z_k X_k = sqrt(m) Z_*`.                                  (5.9)

The normalized scalar `Z_*` depends only on coordinates in `B_3`, hence is genuinely independent of the hub and all `B_2` coordinates. By (2.1),

`||p_{Z_*}||_infinity <= sqrt(e)`.                                  (5.10)

Similarly (5.5) and (2.1) give

`||p_Y||_infinity <= sqrt(e)`.                                      (5.11)

Set

`S=sqrt(L)X_h+A`.                                                    (5.12)

Conditioned on all `B_2` coordinates, `S` is a translate of `sqrt(L)X_h`; therefore

`||p_{S | X_{B_2}}||_infinity <= L^(-1/2)`.                         (5.13)

Because `Y` is measurable with respect to `X_{B_2}`, (5.13) is exactly the conditional-density hypothesis of Theorem 3.1 with nuisance variable `W=X_{B_2}`.

Using (4.4), the quadratic form on the active block is

`Q = 2 R S Y + pY^2 + 2qY(Z_0+sqrt(m)Z_*)
      + d(Z_0+sqrt(m)Z_*)^2`.                                      (5.14)

Since `d!=0` by (4.5), complete the square only in the genuinely independent `Z_*` leaf:

`Q = 2 R S Y
    + (p-q^2/d)Y^2
    + d m [ Z_* + (Z_0+(q/d)Y)/sqrt(m) ]^2`.                        (5.15)

This has exactly the form (3.1), with

`a=R`, `b=dm`,
`K_S=L^(-1/2)`, `K_Y=sqrt(e)`, `K_Z=sqrt(e)`,                        (5.16)

`F=(p-q^2/d)Y^2`, and

`theta=(Z_0+(q/d)Y)/sqrt(m)`,                                      (5.17)

which depends only on the `B_2` nuisance variables and not on `S`. Therefore Theorem 3.1 yields

`||p_Q||_infinity
 <= 6 (e L^(-1/2))^(2/3)
       (R^2 |d| m)^(-1/3)`
` = 6 e^(2/3) L^(-1/3)
       (|det N| m)^(-1/3)`,                                        (5.18)

using (4.5). By (5.7),

`|det N|m = |det N| T_h/L`.                                        (5.19)

Hence the leverage cancels exactly:

`||p_Q||_infinity
 <= 6 e^(2/3) (|det N| T_h)^(-1/3).`                               (5.20)

Finally (4.1),(4.3) imply

`|det N|T_h >=2^(-18)2^(-9)=2^(-27)`.                              (5.21)

Substituting into (5.20),

`||p_Q||_infinity
 <= 6 e^(2/3) 2^9
 =3072 e^(2/3)
 =5983.438974119964...`,                                            (5.22)

proving (5.2). QED.

## 6. The partner's local-certificate counterexample is now paid by this theorem

The designated account02/B10 report gives the exact target family

- hub `sqrt(1-epsilon)e_1`;
- `B_2`: many tiny `e_1` rows plus many tiny `e_2` rows;
- `B_3`: many tiny `e_3` rows;
- `N=[[0,1,0],[1,0,0],[0,0,1]]`.

It has `|det N|=1` and `T_h=1-epsilon`, while every individual scalar pivot/pair/triple certificate tends to zero as the bank cardinality grows. Theorem 5.1 applies exactly because `B_3` is a pure `e_3` curvature bank, and gives the much sharper family-specific estimate

`||p_Q||_infinity
 <= 6 e^(2/3)(1-epsilon)^(-1/3)`                                   (6.1)

which is below `11.70` for `epsilon<1/512`, uniformly in the number of fragmented rows. Thus the canonical obstruction to local selection is no longer an obstruction to density smoothing: the correct payment aggregates the whole pure curvature bank before taking any reciprocal coefficient.

This is an actual application of the completed partner result to a density inequality, not only a structural citation.

## 7. Relation to the newest account02/B10 exact-graph closure

The newer partner run `20260923T014801Z-account02-B10-QFORM-auto11`, canonical

`yspennstate/math-open-problems@e00458111ae6c54afa30331726a6335fc838557f`,

proves `QFORM-ONEBANK-EXACTGRAPH-ALLPIVOT-CLOSURE-v1`: if one quantitative two-dimensional light bank has zero longitudinal regression residual, then every heavy scalar pivot is paid by `<2945`.

Theorem 5.1 is complementary. Its square bank is rank one transversely, so it is not the quantitative `G>=kappa I_2` exact-graph bank covered by that theorem. Instead it permits arbitrary dependence/leakage in the opposite hyperbolic bank and spends a genuinely independent one-dimensional curvature innovation.

## 8. First unpaid implication after this run

The exact pure-curvature endpoint (5.1) is now uniformly paid. The surviving hub/two-bank problem is therefore one in which **neither light bank supplies a quantitative independent curvature line outright**.

A precise next implication is

`QFORM-CURVATURE-INNOVATION-BANK-PAVING-v1`:

> In the exact-null singleton-heavy-hub state with fixed exterior packet `T_h`, either extract from one original-coordinate bank a disjoint scalar curvature innovation `Z` with quantitative coefficient energy and zero hub coupling (so Theorem 3.1 applies), or prove that the unavoidable contamination of every such candidate innovation itself produces a quantitatively paid cross-transverse / positive-regression-residual configuration.

The key restriction is product provenance: coefficient orthogonality inside one bank does not make two linear projections independent. The extraction must therefore occur by an actual partition of original coordinates or through a theorem that retains the joint bank law. No conditional-profile supremum or small-random-perturbation argument is allowed.

The newest account02/B10 exact-graph theorem already pays one zero-residual endpoint, while Theorem 5.1 now pays the orthogonal pure-curvature endpoint. The genuinely mixed positive-residual collar remains the frontier.

## 9. Status and regularity

- `QFORM-CONDITIONAL-SLOPE-INDEPENDENT-SQUARE-v1`: **proved**.
- `QFORM-NULL-HUB-PURE-CURVATURE-BANK-v1`: **proved supporting target-level branch**, with explicit constant `<5983.439` under the live heavy-hub reduction constants.
- The account02/B10 fragmented local-certificate counterexample family: **uniformly paid** by (6.1).
- Arbitrary singleton-heavy-hub/two-bank state: **OPEN**.
- Arbitrary exact-rank-three target: **OPEN / NOT PROVED / NOT DISPROVED**.
- Full owner QFORM conjecture: **OPEN / NOT PROVED / NOT DISPROVED**.
- Continuity: this proof establishes an essentially bounded density; no continuous representative is claimed for this branch.

No Gaussianity, moment, compact-support, connected-support, post-rotation independence, Monte Carlo extremality, or local-minor pigeonhole principle is used.
