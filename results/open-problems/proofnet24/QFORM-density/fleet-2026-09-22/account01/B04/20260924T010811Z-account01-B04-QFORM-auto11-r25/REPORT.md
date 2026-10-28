SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B04, 2026-09-24T01:08:11Z.
attacking: replace the max-leverage paving gate by an exterior-power collision estimate: show diffuse range leverage forces most third-compound mass onto disjoint physical triples, then feed that directly into the marginal-free cross-E3 Fourier compiler.

# account01/B04 r25 — disjoint third-compound energy from exterior leverage collision

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: Product Fourier rearrangement  
Status: **NEW SUPPORTING THEOREM / CURRENT SMALL-PAIR SUBBRANCH PAID / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Continuity: the new paid branch has a continuous `C_0` density. The unrestricted full-target continuity statement remains open.  
Execution label: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. All coordinates remain literal original independent product coordinates. No rotated random variables are declared independent, no moment/support/log-concavity assumption is added, and no law-uniform pointwise quadratic-phase decay, arbitrary-joint coarea bound, or conditional-density-cap shortcut is used.

## 1. Fresh source boundary


The analytic receiver used below is the completed marginal-free cross-third-volume theorem from account03/B04 r42, source

`yspennstate/math-open-problems@563bc41e4f9247f9daf3343a57757f45e3f6e703`

at

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B04/20260923T215155Z-account03-B04-QFORM-auto11-r42/REPORT.md`.

For every literal physical cross block `M`, with arbitrary same-bank quadratic terms and affine terms,

`||p_Q||_infinity <= C_* E_3(M)^(-1/6)`,                          (1.1)

where

`C_*=8.45302122552817687470491804598...`,                         (1.2)

and the resulting density belongs to `C_0(R)`.

The designated account02/B04 source actually applied below is r16,

`yspennstate/math-open-problems@779dc7079332af772c3445c0f58dbb5a59b504cf`,

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B04/20260924T001554Z-account02-B04-QFORM-r16/REPORT.md`.

Its completed residual-paving theorem says that for a symmetric carrier `S=U Lambda U^T`, after deleting a physical set `H`, if

`G=U_L^T U_L >= gamma I`, `beta=max_(i in L)||u_i||^2`, `r beta<gamma`,

then with

`g=(1-sqrt(r beta/gamma))/2`,                                     (1.3)

a literal physical cut exists whose third crossing singular value is at least `g gamma s_3(S)`, and hence

`||p_Q||_infinity <= C_*/(g gamma s_3(S))`.                       (1.4)

That result is correct in its stated scope; the theorem below removes its max-leverage style gate in a different diffuse regime.

## 2. Exterior-power collision lemma

Let `S` be a real symmetric `m x m` matrix of rank `r>=3`, with spectral factorization

`S=U Lambda U^T`, `U^T U=I_r`.                                    (2.1)

Write the physical row leverage scores

`ell_i=||u_i||_2^2`,
`tau=sum_i ell_i^2`.                                               (2.2)

For physical triples `R,T`, let

`D_3(S)_{R,T}=det S[R,T]`.                                        (2.3)

The total third-compound energy is

`||D_3(S)||_F^2=e_3(S^2)`.                                        (2.4)

Define the disjoint part

`Delta_3^disj(S)
 =sum_(|R|=|T|=3, R intersect T=empty) det S[R,T]^2`.              (2.5)

### Theorem 2.1 — `QFORM-EXTERIOR-LEVERAGE-DISJOINT-E3-v1`

One has the exact lower bound

`boxed:
 Delta_3^disj(S) >= (1-tau) e_3(S^2).`                            (2.6)

In particular the right side is useful whenever `tau<1`.

### Proof

Let

`W=wedge^3 U : wedge^3 R^r -> wedge^3 R^m`.                       (2.7)

Because `U` is an isometry, `W` is an isometry. If `D=wedge^3 Lambda`, then

`D_3(S)=W D W^T`,                                                 (2.8)

and

`||D||_F^2=e_3(S^2)`.                                             (2.9)

For a physical coordinate `i`, let `P_i` be the orthogonal coordinate projection in `wedge^3 R^m` onto basis wedges containing `e_i`.

The key point is

`boxed: ||P_i W||_op^2 <= ell_i.`                                 (2.10)

Indeed, for `z in wedge^3 range(U)`, contraction by `e_i` equals contraction by the range projection `P_U e_i`. Since the contraction operator by a vector `v` has norm `||v||`,

`||P_i z|| <= ||iota_(e_i) z||
            = ||iota_(P_U e_i) z||
            <= ||P_U e_i|| ||z||
            = sqrt(ell_i)||z||`.                                  (2.11)

Now let `O` be the overlap energy, i.e. the sum of `det S[R,T]^2` over `R intersect T != empty`. Union-bounding by a shared physical coordinate gives

`O <= sum_i ||P_i D_3(S) P_i||_F^2`.                              (2.12)

Using (2.8), (2.10), and `||A D A^T||_F <= ||A||_op^2 ||D||_F`,

`||P_i D_3(S)P_i||_F^2
 <=ell_i^2 ||D||_F^2
 =ell_i^2 e_3(S^2)`.                                               (2.13)

Therefore

`O <= tau e_3(S^2)`.                                              (2.14)

Subtracting from the total energy (2.4) proves (2.6). QED.

This is an exterior-power statement, not a pointwise oscillatory estimate. Its useful parameter is the **collision leverage** `tau=sum ell_i^2`, rather than only `max ell_i`.

## 3. Random cut and product-Fourier density theorem

Color the physical coordinates independently into labelled banks `I,J` with probability `1/2` each. Every ordered disjoint pair of triples `(R,T)` lands with `R subset I`, `T subset J` with probability `2^(-6)=1/64`. Hence

`E E_3(S[I,J])=Delta_3^disj(S)/64`.                               (3.1)

Combining (2.6) and (3.1), some literal original-coordinate cut satisfies

`boxed:
 E_3(S[I,J]) >= (1-tau)e_3(S^2)/64.`                             (3.2)

### Theorem 3.1 — `QFORM-COLLISION-LEVERAGE-CROSS-E3-v1`

Suppose a full ambient quadratic form contains a physical coordinate bank `K` whose `K x K` coefficient block is `C`. Let `S` be any symmetric carrier on `K` with the same off-diagonal entries as `C`; in particular one may take `S=C` or `S=off(C)`. Let `ell_i` be the range leverage scores of `S` and `tau=sum ell_i^2<1`.

Then the full ambient quadratic form has a continuous `C_0` density and

`boxed:
 ||p_Q||_infinity
 <= 2 C_* (1-tau)^(-1/6) e_3(S^2)^(-1/6).`                       (3.3)

### Proof

Condition on all original coordinates outside `K`. The remaining coordinates in `K` retain their product law and cap-one densities; every outside coupling becomes an affine term.

Choose the deterministic cut from (3.2). Since `C-S` is diagonal, the physical cross block of the actual conditional quadratic form is exactly

`C[I,J]=S[I,J]`.                                                   (3.4)

Apply the completed marginal-free cross-E3 theorem (1.1) and (3.2):

`||p_(Q|outside)||_infinity
 <= C_*[(1-tau)e_3(S^2)/64]^(-1/6)
 =2 C_*(1-tau)^(-1/6)e_3(S^2)^(-1/6).`                            (3.5)

The source theorem supplies an `L^1` characteristic-function envelope uniform in the induced affine terms, so averaging over the conditioned outside variables preserves the stated bound and yields a `C_0` density. QED.

Unlike the preceding paving theorem, (3.3) can remain finite even when `r max_i ell_i >=1`.

## 4. Stable-rank form with no dimension parameter

Let the nonzero squared singular values of `S` be `a_j=s_j(S)^2`, let

`F=||S||_F`, `M=||S||_op`, `rho=F^2/M^2`                          (4.1)

be the stable rank, and assume `rho>2`.

Set

`k=floor(rho)`, `theta=rho-k`,

`m_3(rho)
 =[ C(k,3)+theta C(k,2) ]/rho^3`.                                 (4.2)

### Lemma 4.1

`boxed: e_3(S^2) >= F^6 m_3(rho).`                                (4.3)

### Proof

Normalize `x_j=a_j/F^2`. Then `sum x_j=1` and `0<=x_j<=1/rho`.

For two coordinates `x,y` and the remaining vector `z`,

`e_3(x,y,z)=xy sum z +(x+y)e_2(z)+e_3(z)`.                        (4.4)

If `x+y<=1/rho`, replacing `(x,y)` by `(x+y,0)` weakly decreases `e_3`. If `x+y>1/rho`, replacing it by `(1/rho,x+y-1/rho)` also weakly decreases `e_3`, because

`xy-(1/rho)(x+y-1/rho)
 =(1/rho-x)(1/rho-y)>=0`.                                         (4.5)

Repeatedly compressing pairs therefore minimizes `e_3` at the maximally concentrated cap vector: `k` entries equal `1/rho`, one entry equals `theta/rho`, and the rest vanish. Its third elementary symmetric polynomial is exactly (4.2). Rescaling proves (4.3). QED.

Combining with Theorem 3.1 gives

`boxed:
 ||p_Q||_infinity
 <= [2 C_*/F] [(1-tau)m_3(rho)]^(-1/6).`                          (4.6)

The function `m_3(rho)` is increasing for `rho>=3`; in particular

`rho>=3  =>  m_3(rho)>=1/27`.                                    (4.7)

Thus the simple useful corollary is

`boxed:
 rho>=3, tau<=1/2
 => ||p_Q||_infinity
 <= 2 C_* 54^(1/6) / ||S||_F.`                                   (4.8)

Numerically the coefficient is

`2 C_* 54^(1/6)=32.86807342283458...`.                            (4.9)

## 5. Direct payment inside the current small-pair overlap-two branch

The preceding B04 r24 theorem showed that the still-unpaid localized overlap-two small-pair state has, in one of its two deterministic alternatives,

`||off(C)||_F >=512/15`.                                          (5.1)

Take

`S=off(C)`.                                                        (5.2)

If in addition

`stable-rank(S)>=3`,
`sum_i (P_range(S))_ii^2 <=1/2`,                                  (5.3)

then (4.8) and (5.1) give the explicit universal density bound

`boxed:
 ||p_Q||_infinity
 <= 2 C_* 54^(1/6)/(512/15)
 =0.9629318385596067... ,
 p_Q in C_0(R).}`                                                  (5.4)

So the complement-curvature half of the r24 small-pair branch is now paid unless its forced large off-diagonal matrix satisfies at least one of

`stable-rank(off(C))<3`,                                          (5.5)

or

`sum_i (P_range(off(C)))_ii^2>1/2`.                               (5.6)

This is a sharper structural remainder than the previous generic square-root small-ball endpoint: failure is now either **spectrally near rank two** or **physically collision-concentrated**. Neither statement is itself yet a full exit.

## 6. Genuinely rotated indefinite example beyond the old max-leverage gate

Construct an explicit `65 x 4` orthonormal frame. Let the first physical row be

`u_0=(sqrt(3/10),0,0,0)`.                                         (6.1)

Index the remaining 64 rows by `x in F_2^6` and set

`u_x=( sqrt(7/10)/8,
       (-1)^(x_1)/8,
       (-1)^(x_2)/8,
       (-1)^(x_3)/8 )`.                                           (6.2)

Walsh orthogonality gives `U^T U=I_4` exactly. Put

`Lambda=diag(2,2,-2,-2)`,
`A_*=U Lambda U^T`.                                                (6.3)

The nonzero spectrum of `A_*` is exactly

`{2,2,-2,-2}`,                                                     (6.4)

so this is a genuinely rotated indefinite target-valid form with four eigenvalues of modulus two.

Its leverage scores are

`ell_0=3/10`,
`ell_x=37/640` for each of the other 64 rows.                      (6.5)

Hence

`beta=3/10`, `r beta=6/5>1`.                                      (6.6)

So the **basic** max-leverage gate of the designated account02/B04 r16 theorem fails.

But the collision leverage is

`tau=(3/10)^2 +64(37/640)^2
    =389/1280
    =0.30390625<1`.                                                (6.7)

Also

`e_3(A_*^2)=4*2^6=256`.                                           (6.8)

Theorem 3.1 therefore gives a literal physical cut with

`E_3(A_*[I,J])
 >=(1-389/1280)*256/64
 =891/320`,                                                        (6.9)

and consequently

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_* (891/320)^(-1/6)
 =7.126736009998208... ,
 p in C_0(R).}`                                                    (6.10)

This example lies outside the undeleted `r beta<1` paving gate.

## 7. Designated account02/B04 result applied at an actual inequality

Apply account02/B04 r16 to the **same matrix** after deleting only the heavy physical row `H={0}`. Then

`G=U_L^T U_L=diag(7/10,1,1,1)`,                                   (7.1)

so one may take

`gamma=7/10`.                                                      (7.2)

Every residual row has

`beta_H=37/640`,                                                   (7.3)

and

`r beta_H/gamma
 =4*(37/640)/(7/10)
 =37/112<1`.                                                       (7.4)

Thus the partner theorem applies with

`g=(1-sqrt(37/112))/2
 =0.21261648322444499...`,                                        (7.5)

and `s_3(A_*)=2`. Its completed inequality yields

`boxed:
 ||p_(X^T A_* X)||_infinity
 <= C_*/[(7/10)*2*g]
 =28.397950207721763... .}`                                       (7.6)

The new collision-leverage theorem improves that same-matrix completed partner certificate by the factor

`28.397950207721763 / 7.126736009998208
 =3.984706346338891...`.                                          (7.7)

This comparison is not a claim that the new theorem dominates r16 globally. The partner deletion theorem remains stronger in concentrated-hub regimes where `tau>=1` but a small heavy set can be conditioned away without destroying the residual frame.

## 8. Remaining implication

The new first unpaid implication for this B04 branch is

`QFORM-SMALLPAIR-LOW-STABLERANK-OR-HIGH-COLLISION-ROUTING-v1`:

> In the current localized overlap-two small-pair state, the complement-curvature alternative is now paid whenever `stable-rank(off(C))>=3` and `sum leverage^2<=1/2`. Route the remaining cases `stable-rank(off(C))<3` or `sum leverage^2>1/2` into the completed rank-two rough-curvature, grouped-hub, fixed-pair, projected-crossing, ridge, or square-bank receivers, without deleting a nonzero random quadratic remainder and without selecting/inverting a vanishing local coefficient.

This does not solve the unrestricted conjecture. It does, however, replace one broad large-Frobenius complement-curvature branch by two concrete deterministic obstructions: near-rank-two spectrum or physical leverage collision.

## 9. Integrity notes

All arguments are deterministic exterior algebra plus completed product-Fourier inequalities. No Monte Carlo is used. The only random partition is a probabilistic-method existence proof over physical coordinate labels. The new theorem preserves all input-law quantifiers of the owner target in its stated scope. Independent review is still pending.
