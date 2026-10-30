SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B04, 2026-09-24T10:51:22Z.
attacking: the coherent low-tetrad collar by an explicit physical Schur-numerator perturbation; test whether volume/ridge/projected-crossing currencies can stay uniform, and force the missing principal-curvature exit.

# fleet02/B04 r22 — coherent tetrad collar and principal-curvature necessity

Programme: `QFORM-DENSITY-3EIG-20260922`.
Status: **NEW SUPPORTING CONSTRUCTION / SOURCE-VALID INTERMEDIATE-ROUTE OBSTRUCTION / GLOBAL PHYSICAL-VOLUME OPTIMIZATION / PINNED RESULT APPLIED / FULL QFORM OPEN**.
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted target remains OPEN. Continuity is kept separate. No moment, support, log-concavity, diagonal-basis reduction, post-rotation independence, arbitrary-joint coarea, worst-fibre supremum, law-uniform pointwise quadratic-phase decay, or deletion of a nonzero random quadratic tail is used.

## 1. Fresh sources and first unpaid implication

Fresh owner control remained revision `2026-09-22.15`, QFORM-only. The required pinned source was re-read at

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

under `proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`, including `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

The exact pinned inputs used below are:

1. Localized Theorem A: if a literal physical principal `3x3` block has all three eigenvalues of modulus at least `sigma`, conditioning every other original coordinate gives

`||p_Q||_infinity <= 6 sqrt(pi)/sigma`.

2. Arbitrary-weight Theorem D: for a literal cross block `M=A[I,J]`, any supported physical `3x3` minor law `w` whose I-side row marginals are at most `1/2` gives

`||p_Q||_infinity <= 6 sqrt(e) G(w)^(-1/6)`,

where `G(w)=exp(E_w log det(M_ST)^2+H(w))`. The D' extension allows an I-side cap `h<3/4` with multiplier `(2h)^(-1/2)(3-4h)^(-1)`. There is no J-side marginal gate.

The newest compatible designated partner at refresh is fleet03/B04 r55,

`yspennstate/math-open-problems@8943de4ce7adbeef5a110d0bf0fc634b2fce39c5`,

whose `QFORM-ONE-HUB-PROJECTED-E2-BALANCED-FALLBACK-v1` says that for a literal hub row `m=A[h,J]`, `s=||m||`, residual crossing `B=A[I,J]`, projection `P=I-mm^T/s^2`, `C=BP`, and `Z=e_2(CC^T)>0`,

`||p_Q||_infinity <= C_PF (s^2 Z)^(-1/6)`,
`C_PF=3*2^(7/6)*e^(1/3)=9.39913188784886...`,

without a projected-E2 row-marginal gate. All promotions in its proof are literal physical coordinates.

The first unpaid implication is therefore sharpened to

`QFORM-LOW-TETRAD-STABILITY-TO-PRINCIPAL-OR-KERNELSTAR-v1`:

from a fixed physical pair with target-scale overlap-two energy and very small disjoint Schur-numerator tetrad volume, prove a dimension-free exit to either a target-scale literal principal-curvature block, a completed kernel-star/rank-two/grouped endpoint, or renewed numerator two-volume. A theorem whose only alternatives are renewed cross-E3, ridge, or one-hub projected-E2 is not sufficient.

The construction below proves that last sentence quantitatively.

## 2. A fully dense coherent collar

Use the literal physical pair `H={1,2}` and let the residual bank have nine original coordinates. Put

`B=[[3,1],[1,-3]]`,
`v=(1/10,1/5)`,
`C=1_9 v`,
`S=2 I_9+J_9`.

Since `B^2=10I`,

`v B^(-1) v^T=-1/200`,

so

`C B^(-1) C^T=-(1/200)J_9`.

Let `E_e` be the symmetric residual matrix supported on the four unordered physical edges

`(5,9), (6,9), (7,10), (8,10)`

with value `e` on each of those edges and its transpose, and zero elsewhere. Define

`D_e=S+C B^(-1)C^T+E_e`,
`A_e=[[B,C^T],[C,D_e]]`.

For `0<=e<=1/16` every physical entry of `A_e` is nonzero. In particular the residual diagonal is `599/200`, every unperturbed residual off-diagonal is `199/200`, and every perturbed residual off-diagonal is `199/200+e`.

The Schur complement at the literal pair is exactly

`D_e-CB^(-1)C^T=S+E_e`,

and since `det B=-10`, its polynomial Schur numerator is

`boxed: N_H=-10(S+E_e).`

Thus `e=0` is the exact coherent rank-one-off-diagonal clique boundary from the previous run, while `e>0` moves genuinely into the positive-tetrad collar.

## 3. Uniform target spectrum

Take the block-diagonal reference

`A_ref=diag(B,S)`.

Its spectrum is

`{-sqrt(10), sqrt(10), 2 (multiplicity 8), 11}`.

The perturbation obeys

`||A_e-A_ref||_op
 <= ||C|| + ||CB^(-1)C^T|| + ||E_e||_F
 <= sqrt(9/20)+9/200+sqrt(8)e.`

For `e<=1/16` the right side is

`delta_* =0.8925970885465738...`.

Hence Weyl gives every positive eigenvalue at least

`2-delta_*=1.107402911453426...>1`,

and the negative eigenvalue has modulus at least

`sqrt(10)-delta_*=2.269680571621805...>1`.

Therefore **all eleven eigenvalues of every `A_e`, `0<=e<=1/16`, have modulus greater than one**. This is a uniform target-valid family, not merely a near-target perturbation.

## 4. Exact low-tetrad geometry

The overlap-two energy for the chosen pair is

`J_2(H)=sum_(i!=j)(N_H)_(ij)^2
       =7200+1600e+800e^2.`

In particular it stays bounded away from zero as `e->0`.

Use exactly the ordered disjoint-tetrad convention of fleet03/B04 r52:

`D_2^disj(N_H)
 =sum_(|R|=|T|=2, R cap T=emptyset) det N_H[R,T]^2`,

with ordered row/column pairs. Direct exact expansion gives

`boxed:
 D_2^disj(N_H)
 =160000 e^2(e^2+4e+20).`

For example, on rows `{5,7}` and columns `{9,10}`,

`det N_H[{5,7},{9,10}]=100(2e+e^2)`,

so the tetrad currency is genuinely positive for every `e>0`, but tends quadratically to zero.

At the concrete stress value `e=1/16`,

`J_2(H)=7303.125`,
`D_2^disj(N_H)=3240625/256=12658.69140625`,

and

`D_2^disj/J_2(H)^2=0.000237340222196... < 1/64`.

Thus the example lies deep inside the coherent low-tetrad chamber of r52 while retaining an extremely large overlap-two packet.

The older completed r52 disjoint-numerator theorem nevertheless gives a finite, deteriorating collar estimate

`||p_Q||_infinity
 <=49.64302065931249... [D_2^disj(N_H)]^(-1/12)
 =22.59396569486268...`

at `e=1/16`. As `e->0` this scales only as `e^(-1/6)`, but it is not uniform.

## 5. The missing principal-curvature exit is present and uniform

Now condition every original coordinate except physical coordinates `{3,4,11}`. None of the four perturbed edges meets two coordinates of this triple, so its literal principal block is **independent of `e`** and equals

`P=2I_3+(199/200)J_3`.

Its eigenvalues are

`2, 2, 997/200`.

The pinned localized Theorem A therefore applies with `sigma=2`, retaining all affine terms generated by conditioning, and gives the actual target-valid inequality

`boxed:
 ||p_(X^T A_e X)||_infinity
 <= 6sqrt(pi)/2
 =3sqrt(pi)
 =5.317361552716548...`

for every `0<=e<=1/16` and every independent cap-one product input law.

This is the completed pinned `e5f71d...` result spent at an actual inequality. It proves that the coherent collar is harmless, but for a mechanism invisible to the cross-volume currencies below.

## 6. Globally optimized physical E3 weights on one natural cut

Take the literal residual crossing

`I={3,4,5,6,7,8}`,
`J={9,10,11}`.

Write `c=199/200` and `u=c(1,1,1)`. Its six physical rows are

`u, u, u+e e_1, u+e e_1, u+e e_2, u+e e_2`.

For `e>0` this crossing has rank three. A `3x3` row minor is nonzero iff it selects exactly one row from each duplicate pair. There are exactly eight supported minors, and every one has

`|det|=c e^2`.

Consequently

`boxed: Z_3=E_3(M)=8c^2e^4.`

The canonical squared-minor law is uniform on the eight choices and every I-side physical row marginal is exactly `1/2`.

This law is also the **global determinant-entropy optimum under the Theorem-D cap**. Indeed every supported minor chooses exactly one member of each duplicate pair, so the two row marginals in each pair sum to one; the cap forces both to equal `1/2`. Since all eight determinant magnitudes are equal, entropy is maximized uniquely by the uniform law. Hence

`G_*=8c^2e^4=Z_3`.

There is no gain anywhere in the proved D' window: for every `h>=1/2` the uniform law is already feasible and globally maximizes entropy, while

`(2h)^(-1/2)(3-4h)^(-1)`

is strictly increasing for `h in [1/2,3/4)`. Thus `h_*=1/2` is the global optimum over **all supported physical third-minor weights and every proved D/D' exponent**.

The pinned Theorem D gives

`boxed:
 ||p_Q||_infinity
 <=6sqrt(euler_e)[8c^2e^4]^(-1/6)
 =3sqrt(2euler_e)c^(-1/3)e^(-2/3).`

At `e=1/16` this is

`44.48932210648922...`.

The pinned D5 currency is zero on this cut because the cut has only three columns and rank three.

## 7. Fresh partner r55 on the identical physical cut

Promote physical residual row `h=3` as the literal hub and keep `J={9,10,11}`. Then

`m=c(1,1,1)`,
`s^2=3c^2`.

Project the remaining crossing rows orthogonally to `m`. The duplicate row `4` vanishes. Rows `5,6` become `e P e_1`, rows `7,8` become `e P e_2`, where `P` projects orthogonally to `(1,1,1)`. Since

`||Pe_1||^2=||Pe_2||^2=2/3`,
`<Pe_1,Pe_2>=-1/3`,

one has

`||Pe_1 wedge Pe_2||^2=1/3`.

There are four cross-pair choices, so

`boxed: Z=e_2(CC^T)=4e^4/3`,
`boxed: s^2Z=4c^2e^4.`

The four nonzero projected physical rows each have incident E2 marginal exactly `1/2`, while the zero projected row has marginal zero. Hence this example sits exactly on the old projected-E2 gate, and the new marginal-free r55 theorem applies without any extra assumption:

`boxed:
 ||p_Q||_infinity
 <=9.39913188784886... [4c^2e^4]^(-1/6).`

At `e=1/16` this is

`47.447868412612785...`.

This positively applies the newest designated partner theorem on the identical physical matrix. Its own branch proves a continuous `C_0` density, but no full-target continuity statement is inferred.

## 8. Direct ridge comparison on the same natural crossing

Use the completed determinant-retaining direct ridge certificate from the existing QFORM route. Put `g=gamma^2`,

`K_g=M(M^TM+gI)^(-1)M^T`,
`theta=tr K_g`,
`D_g=det(I+MM^T/g)`.

When `q>=1`, `max_i(K_g)_(ii)<=q/2`, and `theta>2q`, the certificate is

`B_ridge
 = euler_e/[sqrt(2q)gamma]
   * theta/(theta-2q)
   * D_g^(-1/(2theta)).`

For the displayed duplicate-pair rank-three crossing, as `g->0` the ridge projector has diagonal exactly `1/2` on each of the six rows and trace three. Hence the critical choice `q=1` is approached from the admissible side.

At `e=1/16`, take the explicit scale

`g=e^8=2^(-32)`

and `q=1`. Direct deterministic evaluation gives

`theta=2.999999694372081...`,
`max_i(K_g)_(ii)=0.4999999701978409...<1/2`,

so the gate is valid, and

`boxed:
 ||p_Q||_infinity
 <=25.933293668389332... .`

The limiting small-`g` scale is exact:

`B_ridge -> (3 euler_e/sqrt(2)) Z_3^(-1/6)
          =(3 euler_e/2)c^(-1/3)e^(-2/3),`

which is `25.93331503373287...` at `e=1/16`. Thus ridge is better than ambient D on this cut but still diverges like `e^(-2/3)` and misses the fixed principal-curvature payment.

## 9. Why this is a genuine structural obstruction

At `e=0`, `A_0` can be written as

`diagonal + rank-one + one physical pair edge`.

Indeed its residual off-diagonal is the constant `c=199/200`; taking the rank-one vector with residual entries one and pair entries `(20/199,40/199)` reproduces every pair-to-residual coefficient, while the remaining `(1,2)` edge is a single pair term. Therefore every literal physical crossing of `A_0` has rank at most two.

It follows by polynomial continuity, and the finiteness of the set of physical cuts, that

`max_(I cap J=empty) E_3(A_e[I,J]) ->0`

as `e->0`. Likewise, for every literal one-hub configuration used by r55, the augmented crossing has rank at most two at `e=0`, so after projecting out the hub row the residual rank is at most one and its projected E2 currency is zero. Hence the maximum r55 currency `s^2Z` over all physical choices also tends to zero.

So a low-tetrad stability theorem cannot close the owner target by asserting that coherent Schur numerator geometry must regenerate target-scale cross-E3 or one-hub projected-E2 currency. The present target-valid family simultaneously has:

- overlap-two energy `J_2(H)->7200`;
- disjoint tetrad volume `D_2^disj(N_H)->0`;
- every literal cross-E3 currency tending to zero;
- every literal r55 one-hub projected-E2 currency tending to zero;
- the direct ridge gate closed on every cut at the exact boundary `e=0` because every crossing has rank at most two;
- a fixed physical principal `3x3` curvature block with third singular/eigenvalue exactly two.

The correct stability conclusion therefore needs a principal-curvature/square-bank/diagonal-plus-low-rank exit, not only renewed crossing currency.

At the concrete `e=1/16` same-matrix stress point, the certified hierarchy is

`boxed:
 5.317362  pinned principal Theorem A
 <22.593966 r52 disjoint Schur numerator
 <25.933294 displayed direct ridge
 <44.489323 globally optimized pinned D/D'
 <47.447869 newest partner r55.`

The whole QFORM theorem remains OPEN. The unpaid step is to prove the dimension-free structural dichotomy announced in Section 1 for an arbitrary low-tetrad pair packet forced by the global overlap decomposition.

## 10. Source and execution notes

Pinned interactive source: `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`.
Newest designated partner used: fleet03/B04 r55 at `math-open-problems@8943de4ce7adbeef5a110d0bf0fc634b2fce39c5`.
The prior pair Schur-numerator receiver r52 used for the collar comparison is at `math-open-problems@fbc50959f73f2a66b91acacbbacc37cbf2b66720`.

Model self-report: `GPT-5.6 Sol`.
Configured reasoning effort: `UNKNOWN`.
Reasoning-token/provider-thinking-time telemetry: `null / not exposed`.
No FEI, installation, benchmark, new task, email, notification, cross-account authentication, paid call, public release, remote workflow, permission change, unrelated-data mutation, or gold-data action was performed.
