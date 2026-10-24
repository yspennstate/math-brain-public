SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B03, 2026-09-23T13:13:11Z.
attacking: strict near-coloop/selector extraction — remove the separability restriction inside the newest dependence-safe selector Plancherel compiler, then apply the strengthened time integral to arbitrary physical selector curvature and an exact target-valid hyperbolic family.

# account02/B03 — joint-selector-phase Plancherel compiler

Programme: `QFORM-DENSITY-3EIG-20260922`. Assignment: Decoupled time integral.
Status: `NEW SUPPORTING THEOREM / SELECTOR-CURVATURE OBSTRUCTION REMOVED / FULL TARGET OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted QFORM conjecture and unrestricted continuity conclusion remain open. This report proves a dependence-safe analytic compiler that strictly strengthens the newest account03/B03 selector theorem: arbitrary joint selector-only curvature is harmless to the whole-copy time estimate. The remaining debt is structural extraction at the strict nonzero near-coloop collar.

## Source boundary

Fresh owner control remained QFORM-only, OWNER CONTROL revision `2026-09-22.15`; no pause/stop applied to account02/B03. Live correction inbox blob before publication: `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

Required pinned package: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`, `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/{RESULTS.md,FOURIER_ROUTE_REPORT.md,COUNTEREXAMPLE_SEARCH.md}`. Its Theorems D/D' and D5 are used only with their stated volume-sampling gates.

Newest designated partner consumed: account03/B03 r34, `proofnet24/QFORM-density/fleet-2026-09-22/account03/B03/20260923T125915Z-account03-B03-QFORM-r34/REPORT.md` on current master. It proves finite-L^p dependent-coefficient selector Plancherel for separable selector phases, the exact weighted independent-copy integral, and a uniform payment of the near-triangle collar. Outside its near-coloop alternative it gives `||p_Q||_infinity<263/s_3(A)`.

The product-projection input used below is the completed source theorem: if `R R^T=I_k` and `Z` is an original-coordinate cap-one product vector, then `RZ` has joint density cap at most `exp(k/2)`.

## 1. Main theorem: arbitrary JOINT selector phase

### Theorem — `QFORM-JOINT-SELECTOR-PHASE-LP-PLANCHEREL-v1`

Let `X=(X_1,...,X_k)` have independent real coordinates with densities `0<=f_j<=1`, and let `W` be independent of the whole selector bank. Let `C(W)` have an arbitrary JOINT probability density `g in L^p(R^k)`, `1<p<=infinity`. Put

`G=||g||_p`, `theta=1-1/p` (`theta=1` for `p=infinity`), `alpha=k theta`, and `B=prod_j|beta_j|`, with every `beta_j!=0`.

Let `P:R^k->R` be an arbitrary measurable joint phase — it need not split coordinatewise and may contain arbitrary quadratic cross terms among the physical selectors. Let `R(W)` be arbitrary and set

`Q=R(W)+P(X)+2 sum_j beta_j X_j C_j(W)`.                             (1.1)

Then, for every `t!=0`,

`|phi_Q(t)|^2 <= min{1, A |t|^(-alpha)}`,
`A=G pi^alpha B^(-theta)`.                                         (1.2)

For every `0<gamma<alpha`,

`int_R |t|^(gamma-1)|phi_Q(t)|^2 dt
 <= [2alpha/(gamma(alpha-gamma))] A^(gamma/alpha)`.                 (1.3)

If `alpha>1`, then

`||p_Q||_2^2 <=[alpha/(alpha-1)]G^(1/alpha)B^(-1/k)`,               (1.4)

and

`sup_s E|Q-s|^(-1/2)
 <=[2sqrt(2)alpha/(alpha-1)]G^(1/(2alpha))B^(-1/(2k))`.             (1.5)

If `alpha>2`, then `Q` has a continuous `C_0` density and

`||p_Q||_infinity
 <=[alpha/(alpha-2)]G^(1/alpha)B^(-1/k)`.                           (1.6)

In particular, at `p=infinity,k=3`,

`||p_Q||_infinity <=3(G/B)^(1/3)`.                                 (1.7)

### Proof

Write `f(x)=prod_j f_j(x_j)`. For fixed `t`, keep the selector bank intact and define the k-dimensional twisted Fourier transform

`F_t(xi)=int f(x) exp(itP(x)+i xi.x) dx`.                           (1.8)

Conditioning only on the full background gives

`phi_Q(t)=E_W exp(itR(W))F_t(2tD_beta C(W))`,                       (1.9)

where `D_beta=diag(beta_j)`. Cauchy-Schwarz over the WHOLE background gives

`|phi_Q(t)|^2 <=int g(c)|F_t(2tD_beta c)|^2 dc`.                    (1.10)

Let `p'=p/(p-1)`, so `1/p'=theta`. Holder gives

`(1.10)<=G[int|F_t(2tD_beta c)|^(2p')dc]^(1/p')`.                  (1.11)

Since `|F_t|<=1` and `2p'>=2`,

`int|F_t|^(2p')<=int|F_t|^2`.                                      (1.12)

The arbitrary joint twist has unit modulus. Plancherel therefore gives

`int|F_t(xi)|^2dxi=(2pi)^k int f(x)^2dx <=(2pi)^k`,                 (1.13)

because each `f_j<=1` and has mass one. Changing deterministic variables `xi=2tD_beta c` now yields

`|phi_Q(t)|^2
 <=G[(2|t|)^(-k)B^(-1)(2pi)^k]^(1/p')
 =G pi^(ktheta)B^(-theta)|t|^(-ktheta)`,                            (1.14)

proving (1.2). Splitting the weighted time integral at `T=A^(1/alpha)` gives (1.3). Integrating (1.2) gives (1.4). Taking square roots, integrating against `|t|^(-1/2)`, and using the standard Riesz representation gives (1.5). If `alpha>2`, the square-root envelope is in `L^1`; Fourier inversion gives (1.6). QED.

The independent-copy identity is used only for the whole variable,

`|phi_Q(t)|^2=E exp(it(Q-Q'))`.                                     (1.15)

No coordinate sum/difference pair is split or declared independent. The coefficient coordinates may be fully dependent. The theorem does NOT permit an arbitrary background-dependent phase `P(X,W)` beyond the displayed linear coefficient vector.

## 2. Quadratic cross-block consequences

Take a physical original-coordinate split with `k` selector variables `U` and disjoint product background `V`:

`Q=U^T C U+2U^T M V+R(V)`,                                        (2.1)

where `C` is arbitrary symmetric and `R` is arbitrary. Suppose `M` has full row rank and put

`Delta_k=sqrt(det(MM^T))=prod_{j=1}^k s_j(M)`.                     (2.2)

Factor `M=H R_0`, `H=(MM^T)^(1/2)`, `R_0R_0^T=I_k`. Product-projection density gives `||p_{R_0V}||_infinity<=e^(k/2)`, so

`||p_{MV}||_infinity<=e^(k/2)/Delta_k`.                            (2.3)

Theorem 1 applies with the joint selector phase `P(U)=U^TCU`; no selector diagonalization is made.

### Three physical selector rows

For `k=3`,

`||p_Q||_infinity
 <=3sqrt(e)Delta_3^(-1/3)
 =3sqrt(e)det(MM^T)^(-1/6)`.                                       (2.4)

The density is continuous `C_0`, and the assigned whole-copy integral is

`int_R |t|^(-1/2)|phi_Q(t)|^2dt
 <=(24/5)sqrt(pi)e^(1/4)Delta_3^(-1/6)`.                            (2.5)

Equivalently,

`E|Q-Q'|^(-1/2)
 <=[24/(5sqrt(2))]e^(1/4)Delta_3^(-1/6)`.                           (2.6)

Thus all within-selector quadratic curvature is free; only quantitative cross-image geometry remains.

### Two residual selectors plus one genuine physical square

Suppose exact completion in an original coordinate gives

`Q=d[Z+h(W)]^2+R(W)`, `d!=0`,                                      (2.7)

and in the Schur residual two physical selectors `U` satisfy

`R=U^TCU+2U^TMV+R_0(V)`, `rank M=2`.                               (2.8)

With `Delta_2=sqrt(det(MM^T))`, (2.3) gives coefficient cap `e/Delta_2`; hence

`sup_s E|R-s|^(-1/2)
 <=4sqrt(2)e^(1/4)Delta_2^(-1/4)`.                                 (2.9)

The genuine square pushforward satisfies conditionally

`p_{d[Z+h]^2}(u|W)<=|d|^(-1/2)|u|^(-1/2)`,                         (2.10)

so

`||p_Q||_infinity
 <=4sqrt(2)e^(1/4)|d|^(-1/2)Delta_2^(-1/4)`.                       (2.11)

Therefore every interval `I` obeys the linear output bound

`P(Q in I)
 <=4sqrt(2)e^(1/4)|d|^(-1/2)Delta_2^(-1/4)|I|`.                    (2.12)

Arbitrary `2x2` selector self-curvature, arbitrary residual background curvature, and arbitrary dependence between `h(W)` and the residual are allowed.

## 3. Exact target-valid curved hyperbolic family

Let `C` be ANY real symmetric `3x3` matrix and take six independent cap-one coordinates grouped as `U,V in R^3`. Define

`A_C=[[C,I_3],[I_3,-C]]`,
`Q_C=U^TCU+2U^TV-V^TCV`.                                           (3.1)

The coefficient vector for the physical selector bank `U` is exactly `V`, whose joint density is at most one. Hence (1.7) gives

`||p_{Q_C}||_infinity<=3`,                                         (3.2)

with continuous `C_0` density, uniformly in the arbitrary dense matrix `C`.

The dependence-safe copy certificate is

`int_R |t|^(-1/2)|phi_{Q_C}(t)|^2dt <=(24/5)sqrt(pi)`,              (3.3)

and

`E|Q_C-Q_C'|^(-1/2)<=24/(5sqrt(2))=3.3941125496...`.               (3.4)

This is an exact owner-target family. Deterministically,

`A_C^2=diag(C^2+I_3,C^2+I_3)`,                                     (3.5)

so every eigenvalue of `A_C` has modulus at least one. This deterministic spectral computation makes no probabilistic post-rotation independence claim.

The example isolates the gain of the present theorem: both physical banks may carry arbitrary opposite dense self-curvature, yet the whole selector-bank Plancherel norm is unchanged because the joint selector phase is unimodular.

## 4. Actual application of pinned and newest-partner results

For the natural split `I=U,J=V` in (3.1), the pinned e5 cross block is `M=I_3`. The normalized three-volume exists, but the volume-sampling law has only one nonzero three-row choice, so each physical selector row has marginal one. Thus e5 Theorem D's `alpha_i<=1/2` hypothesis fails and D' also fails (`h<3/4`); D5 is unavailable on this rank-three cross block. This is an actual source-valid obstruction to the pinned volume-marginal compiler on this natural cut, while (3.2) pays the same cut uniformly. No claim is made that every other cut of every `C` fails the e5 package.

Newest partner account03/B03 r34 applies to the live exact angular packet and proves, outside its near-coloop alternative,

`||p_Q||_infinity<263/s_3(A)`.                                     (4.1)

Combining that completed inequality with the preceding account02/B03 augmented-BL run means the first unpaid angular implication is now the strict nonzero near-coloop collar, not the near-triangle branch.

The present theorem removes a separate analytic restriction inside any selector extraction from that collar: once two or three genuine physical selectors are found, arbitrary cross-quadratic curvature among the selectors no longer invalidates the dependence-safe Plancherel estimate.

## 5. First unpaid implication

`QFORM-STRICT-NEAR-COLOOP-SELECTOR-OR-GROUPED-EXIT-v1`:

In the strict nonzero near-coloop collar surviving r34 and the preceding augmented-BL theorem, prove a product-preserving alternative at universal scale:

- either two physical residual selectors plus one genuine square with quantitatively nondegenerate `|d|` and `Delta_2`, so (2.11) applies;
- or three physical selectors with quantitative `Delta_3`, so (2.4) applies;
- or route the same residual direction into an existing grouped-hub/ridge/exact-coloop exit.

The selector principal block may now be completely arbitrary and should not be charged as structural debt. The remaining issue is coefficient-image geometry. One must not perturbatively delete the small nonzero near-coloop direction; arbitrary cap-one laws need not have bounded support, and the live near-zero-half-Riesz corrections forbid that shortcut.

## 6. Corrections preserved

No step uses law-uniform pointwise quadratic-phase decay; post-rotation independence; independence of conjugate sums/differences; conditional conjugate density caps; arbitrary-joint rank-three coarea; a universal fixed good physical minor or rank-three cut; false single-Schur-rank-two extraction; or deletion of a small quadratic coefficient as a small random error. All selectors are genuine original coordinates, and coefficient-density bounds come only from an actual product bank or the source-valid projection theorem.

Full QFORM: OPEN. Unrestricted continuity: OPEN. Continuity is proved only in the direct `alpha>2` branches above.
