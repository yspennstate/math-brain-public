SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet02, slot B05, 2026-09-24T02:29:15.800755Z.
attacking: correct the heavy-null puncture normalization, extract a source-disjoint aggregate determinant-star crossing, and pay the exact coloop endpoint plus the residual-diffuse collar without selecting a tiny physical minor.

# fleet02/B05 — heavy-null normalized puncture and cross-star compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: quadratic coarea bound / complementary constructions and source-valid obstructions  
Execution: `WITHOUT_VERIFIED_BRAIN`  
Status: **PROVED SUPPORTING GEOMETRIC REDUCTION + TWO ENDPOINT PAYMENTS / FULL QFORM OPEN**  
Continuity: separate; the new endpoint payments below assert essential boundedness only unless inherited from the cited source theorem.

The first unpaid implication is now

`QFORM-HEAVY-NULL-CROSSSTAR-PUNCTURED-RECEIVER-v1`:

> in the exact-rank-three heavy-null branch below, with `c>1/2` and `rho=1-c` small but positive, use the universal **source-disjoint cross determinant-star mass** constructed in Section 5 before inverting any individual physical triple. The exact endpoint `rho=0` is paid and the residual-diffuse chamber with `rho>=1/64` is paid. What remains is the near-coloop/high-residual-leverage convex/two-sheet chamber, where the same-bank normalized longitudinal coordinate `P` cannot be deleted merely because its coefficient is `O(sqrt(rho))`.

This report also corrects one sentence from the immediately preceding B05 handoff: the raw coefficient `s/sqrt(c)` is indeed at least one, but the coefficient relevant to an **independent-hub plus normalized residual-product** decomposition is `beta=s sqrt((1-c)/c)`, which can tend to zero. Thus the punctured problem is real; it was not eliminated by the raw-coordinate inequality.

## 1. Live sources and corrections used

The required pinned source was reread at

`math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/`,
through `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, and `COUNTEREXAMPLE_SEARCH.md`.

Two completed facts are applied below:

1. its residual/conditioned form of Theorem F: after conditioning a set of physical coordinates, if the remaining normalized rank-three frame has row leverage at most `1/2`, then

`||p_Q||_infinity <= 12 (|det Lambda| det G)^(-1/3)`,

where `G` is the remaining spectral Gram matrix;

2. its ruled Theorem C: for signature `(2,1)`, the one-sheet half-line is already bounded by `pi sqrt(2)` at target normalization. Hence the new unpaid receiver is genuinely directed at the complementary convex/two-sheet side.

The pinned counterexample search still reports no target-valid counterexample.

Fresh designated partner fleet03/B05 is r36,

`math-open-problems@511a1258a94b754b1306f24ac56122696792f6f4`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B05/20260924T010727Z-fleet03-B05-QFORM-r36/REPORT.md`.

Its theorem `QFORM-RATIOPACKET-NEAR-DOUBLEZERO-AFFINE-v1` closes the immediately preceding B05 exact-double-zero interpolation debt on the fixed indefinite collar: if `B=[[a,c],[c,d]]`, `D=|det B|`, `max(|a|,|d|)<=sqrt(D)/5`, then with all packet affine terms retained it proves

`P(Q in I) <=128 (D |L|)^(-1/3)|I|`

in its normalized three-bank form and, for the live ratio packet,

`||p_Q||_(infinity,ess) <312 (mu m)^(-1/3)`.

This is a real application of the partner result: the older B05 theorem paid only `a=d=0`; r36 pays the punctured nonzero-diagonal collar without conditioning the dependent Schur-null coordinate. Therefore that old interpolation debt is retired here.

Live corrections remain binding: no arbitrary-joint 3D coarea, no conditional-cap-as-independence, no post-rotation independence, no interval-to-Borel promotion, no unrestricted curved-fiber supremum, and no deletion of a small random coefficient tail.

## 2. Canonical exact heavy-null geometry

Write the exact active rank-three form as

`A=V Lambda V^T`, `V^T V=I_3`,

with the three eigenvalues of `Lambda` satisfying `|lambda_k|>=1`. Let physical coordinate `i` be heavy,

`r=V_i`, `c=||r||^2>1/2`,

and suppose its physical pivot is exactly null,

`A_ii=r^T Lambda r=0`.

Put

`u=Lambda r`, `s=||u||`.

Then `r.u=0`, and since every singular value of `Lambda` is at least one,

`boxed: s^2=r^T Lambda^2 r >= ||r||^2=c.`                         (2.1)

Choose an orthonormal spectral basis

`e_1=u/s`, `e_3=r/sqrt(c)`, `e_2 perpendicular to e_1,e_3`.

In this basis

`Lambda'=[[alpha,delta,s/sqrt(c)],
          [delta,gamma,0],
          [s/sqrt(c),0,0]].`                                      (2.2)

Indeed `e_3^T Lambda e_3=0`, `e_2^T Lambda e_3=0`, and `e_1^T Lambda e_3=s/sqrt(c)`.

Delete physical row `i`. Let the remaining coefficient columns along `e_1,e_2,e_3` be `l,v,t`. Since

`sum_(j != i) V_j^T V_j = I-r^T r`,

one has

`||l||=||v||=1`, `l.v=0`,
`l.t=v.t=0`, `||t||^2=rho:=1-c`.                                  (2.3)

For the residual original product vector `X_-i`, define

`L=l.X_-i`, `V_2=v.X_-i`, `T=t.X_-i`, `H=X_i`.

Then, up to affine terms created by conditioning coordinates outside the active rank-three part,

`Q=2sHL+alpha L^2+2delta L V_2+gamma V_2^2
  +2(s/sqrt(c)) L T.`                                               (2.4)

No independence is asserted among `L,V_2,T`; only `H` is a literal original coordinate independent of the residual source bank.

The determinant of (2.2) is exact:

`det Lambda = -gamma s^2/c`.                                       (2.5)

Thus

`boxed: s^2 |gamma| = c |det Lambda| >= c >1/2.`                    (2.6)

## 3. Correction: the normalized puncture is real

For `rho>0`, normalize the longitudinal residual projection by

`P=T/sqrt(rho)`.

Then `P` has a unit coefficient vector orthogonal in coefficient space to the unit coefficient vectors of `L,V_2`. Rewriting (2.4) as an independent-hub model gives

`Q=2sHL+alpha L^2+2delta L V_2+gamma V_2^2+2 beta L P`,              (3.1)

where

`boxed: beta=s sqrt(rho/c).`                                       (3.2)

Combining (2.5) and (3.2),

`boxed: beta^2 |gamma| = rho |det Lambda|.`                         (3.3)

So `beta` may tend to zero as `c ->1`, even though the raw coefficient `s/sqrt(c)` multiplying the unnormalised variable `T` is at least one. The preceding B05 statement that the raw inequality eliminates the small-coupling puncture was therefore not the correct normalized conclusion. The correct invariant is (3.3).

There is a useful equivalent reconstruction. Define the third **spectral projection**

`U=sqrt(c) H + T = sqrt(c) H + sqrt(rho) P`.                         (3.4)

Its coefficient vector is exactly the physical vector `V e_3`; hence `(L,V_2,U)` is an orthonormal three-dimensional coefficient projection of the original independent source vector. Equation (2.4) becomes simply

`Q=alpha L^2+2delta L V_2+gamma V_2^2
  +2(s/sqrt(c)) L U`,                                               (3.5)

which is the original spectral form in the reordered orthonormal basis. In particular the eigenvalues of its 3-by-3 matrix are exactly the original three active eigenvalues; no probabilistic independence of `(L,V_2,U)` is being claimed.

Equation (3.4) shows exactly why the endpoint is subtle: `U` is a dominant literal independent coordinate plus a `sqrt(rho)` product-projection tail, and rough unbounded inputs forbid replacing that tail by zero uniformly.

## 4. Two paid chambers

### 4.1 Exact coloop endpoint `rho=0`

If `c=1`, then `T=0`, so (2.4) is

`Q=2sHL+alpha L^2+2delta L V_2+gamma V_2^2`.                         (4.1)

The pair `(L,V_2)` is a two-dimensional orthogonal projection of a product law; the standard bounded-density projection estimate used in the pinned ruled theorem gives the joint cap

`M_2<=2`.                                                           (4.2)

Scale the independent hub to `H'=sH`; then its density cap is at most `1/s`. The completed B05 theorem `QFORM-NULL-HUB-TRANSVERSE-SQUARE-v1` applies directly and yields

`||p_Q||_(infinity,ess)
 <= C_* (2/s)^(2/3)|gamma|^(-1/3),
 C_*=7.761982175235...`.                                            (4.3)

At `c=1`, (2.6) is `s^2|gamma|=|det Lambda|`. Therefore

`boxed:
||p_Q||_(infinity,ess)
 <= C_* 2^(2/3)|det Lambda|^(-1/3)
 <12.322.
}`                                                                  (4.4)

Since `|det Lambda|>=1`, the exact heavy-coloop null endpoint is universally paid. This is an essential-density statement; no continuity is inferred.

### 4.2 Residual-diffuse collar

For `0<rho<1`, condition only on the literal heavy coordinate `H`. The residual spectral Gram matrix is

`G=diag(1,1,rho)`, `det G=rho`.                                     (4.5)

For a residual physical row `j`, its normalized residual leverage is

`q_j=(l_j)^2+(v_j)^2+(t_j)^2/rho
    =(l_j)^2+(v_j)^2+(p_j)^2`.                                     (4.6)

If every `q_j<=1/2`, the conditioned form of the pinned Theorem F gives

`boxed:
||p_Q||_infinity
 <=12 (|det Lambda| rho)^(-1/3).
}`                                                                  (4.7)

Thus the fixed collar

`rho>=1/64`                                                         (4.8)

is paid by

`boxed: ||p_Q||_infinity <=48.`                                    (4.9)

whenever the normalized residual frame is diffuse. If (4.6) fails, there are at most five rows with `q_j>1/2`, since the normalized residual leverages sum to three. Hence a survivor of (4.9) is a genuinely finite-heavy-row near-coloop problem, not an unrestricted diffuse frame.

This is the required real application of a completed theorem from the pinned `e5f71d79...` package.

## 5. Exact aggregate determinant star and a source-disjoint max-cut

The physical heavy row has coordinates `(0,0,sqrt(c))` in the canonical spectral basis. For residual rows `j,k`, set

`Delta_jk=l_j v_k-l_k v_j`.

Then

`det V_{ {i,j,k} }=sqrt(c) Delta_jk`,

and the exact-rank-three principal-minor identity gives

`boxed:
|det A_{ {i,j,k} }|
 =c |det Lambda| Delta_jk^2.
}`                                                                  (5.1)

Because `(l,v)` is a Parseval two-frame,

`sum_(j<k) Delta_jk^2=1`.                                          (5.2)

Therefore the heavy null coordinate carries the exact principal-determinant star

`boxed:
sum_(j<k)|det A_{ {i,j,k} }|
 =c |det Lambda|
 >=1/2.
}`                                                                  (5.3)

This star can always be made **cross-bank** without selecting a small edge.

### Lemma 5.1 — `QFORM-NULLSTAR-MAXCUT-v1`

There is a partition of the residual original coordinates into disjoint source banks `J,K` such that

`boxed:
sum_(j in J,k in K) Delta_jk^2 >=1/2,
}`                                                                  (5.4)

and hence

`boxed:
sum_(j in J,k in K)|det A_{ {i,j,k} }|
 >= c|det Lambda|/2
 >=1/4.
}`                                                                  (5.5)

Proof. Place each residual coordinate independently into `J` or `K` with probability `1/2`. Every unordered pair `{j,k}` is separated with probability `1/2`. Taking expectation in (5.2) gives expected cross mass `1/2`, so some deterministic partition attains at least that value. Multiplying by the exact factor in (5.1) proves (5.5). QED.

This is a true original-source split: the random vectors generated by `J` and `K` are independent because the underlying physical coordinates are disjoint.

There is a useful deterministic refinement. Put

`g_j=(l_j,v_j)`, `S_J=sum_(j in J) g_j g_j^T`, `S_K=I_2-S_J`.

Let the eigenvalues of `S_J` be `a>=b`. Cauchy-Binet gives the cross mass

`C(J,K)=tr(adj(S_J)S_K)
       =a(1-b)+b(1-a).`                                            (5.6)

Since `a>=b`, the first summand is the larger. Therefore any partition from Lemma 5.1 satisfies

`boxed: a(1-b)>=C(J,K)/2>=1/4.`                                    (5.7)

Thus, after a deterministic rotation **only in coefficient-plane bookkeeping**, one source bank carries squared coefficient energy `a` in one direction while the disjoint bank carries squared energy `1-b` in the complementary direction, and their product is at least `1/4`. This is not an independence claim for rotated statistics inside either bank; the same-bank complementary tails remain present and must be retained by the next receiver.

## 6. Why the max-cut does not yet finish the proof

Equation (5.5) is precisely the aggregate currency that an individual-minor proof discards. It does **not** imply that one `Delta_jk^2` is universally large: the mass may be spread over arbitrarily many pairs. Selecting a pair and applying the completed null-pivot determinant theorem would therefore reintroduce a dimension-dependent reciprocal loss.

Likewise, (5.7) does not permit replacing either bank by its leading one-dimensional projection. Each bank may retain a small coefficient-plane tail, and with arbitrary unbounded-support inputs a small coefficient is not a small random perturbation. The valid next theorem has to integrate those tails inside the two independent original-coordinate bank laws.

The near-coloop parameter is now explicit: by (3.3) the normalized same-bank longitudinal coupling is tied to the spectral determinant through

`beta^2 |gamma|=rho |det Lambda|`,                                  (6.1)

while (5.5) supplies a cross-bank determinant-star mass independent of `rho`. A successful receiver should spend (5.5) before taking reciprocal powers and thereby remain uniform as `rho downarrow0`, matching the already-paid endpoint (4.4).

## 7. Relation to the ruled / convex split

If the active signature is `(2,1)`, the pinned Theorem C already gives

`p_Q(s)<=pi sqrt(2)`

on its one-sheet half-line. Thus the new cross-star debt is confined to the complementary two-sheet/convex side (and to the definite signature). The argument above never replaces the curved fibers by an unrestricted fiber supremum.

The fresh r36 partner theorem independently pays the near-double-zero **indefinite scalar-pair** collar. Together, these facts sharpen the remaining geometry: the open heavy-null endpoint is not the exact coloop, not the residual-diffuse moderate collar, not the ruled side, and not the fixed near-double-zero scalar-pair collar. It is the near-coloop/high-residual-leverage aggregate-cross-star receiver described at the start.

Full QFORM remains OPEN / NOT PROVED / NOT DISPROVED.
