SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T01:03:50Z.
attacking: the no-pivot low-cross-rank/hub remainder by combining the mixed-hub Fresnel–Brascamp–Lieb estimate with an exact grouped-pair endpoint, then testing the near-parallel interface on a strict N3 Walsh family.

# account02/B01 r32 — mixed rank-two bank plus one hub, and a near-parallel N3 interface

**Programme:** QFORM-DENSITY-3EIG-20260922  
**Assignment:** Oscillatory replacement / complementary constructions and source-valid counterexamples  
**Status:** ESSENTIAL_STEP_APPLIED / SUPPORTING N3 CLASS / FULL QFORM OPEN  
**Review status:** no end-to-end independent review of this report; full candidate requirements are not met.  
**Execution:** WITHOUT_VERIFIED_BRAIN (authenticated repository retrieval occurred, but no native learned-memory receiver use was established).

## 1. Target and correction boundary

The target is unchanged: for arbitrary independent real original-coordinate inputs with densities bounded by one and arbitrary real symmetric `A` with at least three eigenvalues of modulus at least one, prove one universal bound on the essential supremum of the density of `X^T A X`, or give a valid counterexample. No moments, compact/connected support, Gaussianity, log-concavity, diagonal-basis independence, or post-rotation independence are introduced.

The phase-aligned obstruction to a law-uniform scalar Fresnel estimate remains decisive. For every fixed nonzero frequency `s` and every small `delta>0`, the set

`{x: dist(s x^2,2 pi Z)<=delta}`

has infinite measure, so one can choose a measure-one subset and use its indicator as an admissible density. Then

`Re E exp(i s X^2) >= cos(delta)`.

Nothing below asserts a uniform scalar `|s|^{-1/2}` envelope. The useful estimate is joint and integrated in frequency.

Fresh programme sources consumed include the live correction inbox, the newest-Claude `RESULTS.md`, `FOURIER_ROUTE_REPORT.md`, `COUNTEREXAMPLE_SEARCH.md` at `e5f71d79eff325201dd0274053d20268ce65b837`, and the subsequent volume-stability package at `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`. The latter explicitly leaves low-cross-rank/hub configurations outside its three-volume exits.

## 2. Source theorem actually applied: mixed hubs

The newest-Claude Theorem H in

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`

`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`

states the following. Split original coordinates as `H union I union J`. If

`A_II = sum_(k=1)^r lambda_k v_k v_k^T + D`

with `D` diagonal, and the augmented row vectors

`rho_i=((v_k)_i; A_ih, h in H)`

have Gram `G` and normalized leverages at most `1/2`, then

`|phi_Q(t)| <= (2|t|)^(-|H|) prod_k (4 pi |t lambda_k|)^(-1/2)
              (4 pi)^(r+|H|) det(G)^(-1/2).`                 (2.1)

All blocks `A_HH,A_HJ,A_IJ,A_JJ` are arbitrary. The proof keeps the product structure in the original coordinates and integrates physical hub variables before applying Fresnel linearization and Brascamp–Lieb.

## 3. Derived corollary: rank-two grouped bank plus one physical hub

Let the original coordinates be partitioned as `{0} union B union J`. Assume

`A_BB = M^T H M + D`,                                             (3.1)

where `M` is real `2 x |B|` of rank two, `H` is a real invertible symmetric `2 x 2` matrix, and `D` is diagonal. Put

`c=A_{B0}`, `R=range(M^T)`, `P=P_R`, `c_perp=(I-P)c`.

Assume `c_perp !=0`, set `u=c_perp/||c_perp||_2`, and suppose

`max_(i in B) [P_ii+u_i^2] <= 1/2`.                              (3.2)

No restriction is placed on the remaining blocks or on affine terms.

### Theorem 3.1 — `QFORM-RANK2-BANK-ONE-HUB-MIXED-FRESNEL-v1`

Under (3.1)-(3.2), `Q=X^T A X+b^T X+c0` has a continuous density and

`boxed:
 ||p_Q||_infinity
 <= 4 sqrt(2) [|det H| det(MM^T) ||c_perp||_2^2]^(-1/4).`       (3.3)

### Proof

Let `V` be an orthonormal eigenframe for the rank-two matrix `M^T H M`, with nonzero eigenvalues `lambda_1,lambda_2`. Its range is exactly `R`. The nonzero eigenvalues of `M^T H M` equal those of `H M M^T`, hence

`|lambda_1 lambda_2|=|det H| det(MM^T).`                        (3.4)

Apply Theorem H with the single physical hub `{0}` and `r=2`. The augmented matrix of column directions is `[V,c]`. Its Gram determinant is the Schur complement

`det([[I,V^Tc],[c^TV,||c||^2]])
 = ||c||^2-||V^Tc||^2
 = ||c_perp||^2.`                                                (3.5)

Moreover, the normalized row leverage is the diagonal of the orthogonal projector onto `span(V,c)=R direct_sum span(c_perp)`, namely

`ell_i=P_ii+u_i^2`,                                               (3.6)

so (3.2) is exactly Theorem H's leverage gate. Substituting `r=2`, `|H|=1`, (3.4) and (3.5) into (2.1) gives

`|phi_Q(t)|
 <= 8 pi^2 |t|^(-2)
    [|det H| det(MM^T)||c_perp||^2]^(-1/2).`                    (3.7)

Let the coefficient of `|t|^-2` be `K`. Since also `|phi_Q(t)|<=1`,

`int_R min(1,K|t|^-2) dt =4 sqrt(K).`                            (3.8)

Fourier inversion therefore gives

`||p_Q||_infinity <= (2pi)^(-1) 4 sqrt(K)`,

which simplifies to (3.3). The integrable envelope also gives a continuous representative vanishing at infinity. QED.

This is the requested averaged-frequency replacement: the physical hub contributes a full `|t|^-1`, the two grouped quadratic directions contribute another `|t|^-1`, and the argument never claims law-uniform scalar quadratic-phase decay.

## 4. A strict no-pivot transverse-hub family paid by (3.3)

Let `m` be divisible by four and define three orthonormal Walsh vectors on one original-coordinate bank `B`:

`a=(1,1,1,1,...)/sqrt(m)`,
`b=(1,-1,1,-1,...)/sqrt(m)`,
`w=(1,1,-1,-1,...)/sqrt(m)`.

Let `X_0` be one further original coordinate and set

`Q_perp=(a^T X_B)^2+(b^T X_B)^2+2 sqrt(2) X_0 (w^T X_B).`       (4.1)

The nonzero spectrum is exactly

`{-sqrt(2),1,1,sqrt(2)}`.                                       (4.2)

Every bank diagonal is `2/m`. Every physical hub-bank `2x2` principal determinant has magnitude `2/m`; every bank-bank `2x2` determinant has magnitude at most `4/m^2`. Hence for every fixed no-pivot threshold `tau in (0,1]`, (4.1) lies in the strict N3(tau) class for all sufficiently large `m`.

In (3.1), take the two rows of `M` to be `a,b`, `H=I_2`, `D=0`, and `c=sqrt(2)w`. Then

`det(MM^T)=1`, `||c_perp||^2=2`, `ell_i=3/m`.

For `m>=8`, (3.2) holds and (3.3) yields

`boxed: ||p_Qperp||_infinity <=4*2^(1/4)<4.757.`                (4.3)

This is a full-target-valid N3 subclass with arbitrary cap-one input laws.

## 5. A cross-volume-blind aligned family, paid by the assigned partner

Now define

`Q_parallel=(a^T X_B)^2+(b^T X_B)^2
            +2 sqrt(2) X_0(a^T X_B).`                          (5.1)

Its nonzero spectrum is exactly `{-1,1,2}` and it has the same physical diagonal and pair-determinant scales as above. More strongly, **every original-coordinate cross cut has rank at most two**. If the hub lies on the `I` side, the cross block is the sum of

`a_I^* a_J^T + b_I^* b_J^T`,

where the extended `a_I^*` has hub component `sqrt(2)`; the other side is symmetric. Consequently every three-volume and five-volume certificate is zero. Thus neither D', D5, nor the subsequent three-volume stability/tail theorem can fire on this family.

The newest completed assigned partner, account03/B01 r21, source-pinned at

`yspennstate/math-research-brain@8b3939cff4def148fd1a005b506c99e684176053`

with canonical proof

`yspennstate/math-open-problems@6a63d945b3e2409e5ff5799d2d13c3654bdd27e6:proofnet24/QFORM-density/fleet-2026-09-22/account03/B01/account03-B01-20260923T002425Z-r21/REPORT.md`,

proves that for a definite rank-two grouped pair sourced by one original-coordinate bank,

`||p_Q||_infinity <= pi e/[sqrt(det(MM^T))sqrt(|det H|)]`,       (5.2)

even when the two grouped directions overlap completely, provided the remaining term uses only a disjoint conditioned/remainder bank as stated there.

Complete the square in (5.1):

`Q_parallel=(a^T X_B+sqrt(2)X_0)^2+(b^T X_B)^2-2X_0^2.`         (5.3)

This is exactly the partner theorem with conditioning bank `C={0}`, pair bank `B`, `M=(a;b)`, `H=I_2`, and empty remainder bank. Therefore

`boxed: ||p_Qparallel||_infinity <= pi e <8.540.`               (5.4)

The partner's exact signed-Fejer interface simultaneously gives the same bound for its averaged density kernels `sup_(T,y) D_T law(Q_parallel)(y)`. Equation (5.4) is an actual application of the completed partner theorem, not a summary.

The point is structural: a target-valid strict-N3 family can make **all** D'/D5 cross-volume currencies vanish while remaining uniformly bounded after one aggregates the overlapping same-sign pair before paying a physical minor.

## 6. The near-parallel interface and why the two current certificates do not glue by themselves

Interpolate between the aligned and transverse hub directions:

`Q_eta=(a^T X_B)^2+(b^T X_B)^2
       +2 sqrt(2) X_0((a+eta w)^T X_B),  eta>=0.`              (6.1)

For every `eta>=0`, this remains inside the full spectral target. Indeed `b` is an exact eigenvector with eigenvalue `1`, while the compression to `span{X_0,a}` is

`[[0,sqrt(2)],[sqrt(2),1]]`,

with eigenvalues `-1,2`; min-max gives one full eigenvalue at most `-1` and one at least `2`. For `0<=eta<=1`, all physical diagonals are `2/m`, all bank-bank pair determinants are at most `4/m^2`, and all hub-bank pair determinants are at most `8/m`, so fixed-tau N3 again holds for large `m`.

At `eta=0`, the partner endpoint (5.4) gives `pi e`. For `eta>0`, Theorem 3.1 has

`c_perp=sqrt(2) eta w`,

hence

`||p_Qeta||_infinity <=4*2^(1/4) eta^(-1/2).`                  (6.2)

The divergence of (6.2) as `eta downarrow0` is a **certificate loss**, not a QFORM counterexample. It isolates an exact proof interface: current mixed-hub Fourier control spends only transverse Gram volume, while the grouped-pair endpoint spends only the aligned definite pair. A general N3 proof needs a mechanism that spends both currencies before either small quantity is inverted.

Crucially, one may not declare the `eta` term a small random quadratic perturbation: the input supports are arbitrary and unbounded, so small matrix operator norm does not imply a uniformly small random error.

## 7. The Walsh interpolation itself is uniformly bounded after regrouping

The preceding gap is a gap in the two abstract certificates, not in the concrete family (6.1). For `m` divisible by eight, write `m=4r` with even `r` and split the bank into the four residue classes of the Walsh sign pattern. Define

`T_k=r^(-1/2) sum_(j in G_k) X_j`, `k=1,2,3,4`.

These four variables are independent because the `G_k` are disjoint original-coordinate banks. The Rogozin/Ball estimate used in newest-Claude Lemma 1 says that the sum of `r=2s` cap-one independent variables has density at most `1/sqrt(s)`. Scaling therefore gives

`||p_Tk||_infinity <= sqrt(2).`                                 (7.1)

The Walsh forms become

`a^T X=(T_1+T_2+T_3+T_4)/2`,
`b^T X=(T_1-T_2+T_3-T_4)/2`,
`w^T X=(T_1+T_2-T_3-T_4)/2`.                                  (7.2)

Condition on `X_0,T_3,T_4`. The quadratic part in the two remaining independent variables is exactly

`(1/2)T_1^2+(1/2)T_2^2`;                                      (7.3)

all dependence on `eta` is in affine terms. Completing squares preserves the density caps. If a variable has density cap `L`, then `(1/2)(T-h)^2` has density bounded by `L/sqrt((1/2)y)` on `y>0`. Convolving the two positive square densities and using the beta integral gives

`pi L_1 L_2/sqrt((1/2)(1/2)) <=4 pi.`                          (7.4)

The conditional bound is uniform in the conditioned variables and in `eta`, so averaging proves

`boxed: sup_(eta in R) ||p_Qeta||_infinity <=4 pi.`            (7.5)

Thus the exact near-parallel Walsh family is paid by a **regroup-before-inversion** mechanism. The genuinely unpaid problem is to extract an analogue of this regrouping, or an equivalent three-way overlap inequality, from an arbitrary N3 matrix whose bank row directions are not confined to finitely repeated sign patterns.

## 8. Relation to the newest volume-stability package

The subsequent package

`yspennstate/math-open-problems@c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`

proves a continuous-density bound `<23/a` for a cross block that is an operator-norm perturbation of a diffuse block with `s_3>=a`, and a tail extension using two large cross singular values plus substantial collective tail. Those are important exits. Family (5.1), however, has cross rank at most two on every cut, so its `E_3` and `E_5` currencies vanish exactly; it lies on the low-cross-rank/hub side explicitly left open by that package. Equations (5.3)-(5.4) show that an overlapping grouped definite pair can close such a state even when cross-volume methods see nothing.

## 9. Regression check and status

`CHECK.py` and the executed `CHECK.txt` in this directory verify, at `m=8`, Walsh orthogonality, the exact target spectra to floating precision, the physical pivot scales, the all-cut rank-two property of the aligned family, and the numerical constants. The output ends `STATUS=PASS`. This is regression evidence only; the proofs above are analytic.

The first unpaid implication on this route is now:

`QFORM-NEAR-PARALLEL-THREE-WAY-OVERLAP-ROUTING-v1` — in an arbitrary strict N3 state that escapes the three-volume/tail exits, either expose a source partition/grouping on which the aligned definite-pair currency and transverse hub currency can be spent with a uniform constant, or route to another already-paid scalar/pair/ridge/double-null packet. Repeated sign-pattern banks are handled by Section 7; arbitrary continuously varying row directions are not.

Full QFORM remains **OPEN / NOT PROVED / NOT DISPROVED**. No full-proof candidate and no pair of independent end-to-end reviews are claimed.
