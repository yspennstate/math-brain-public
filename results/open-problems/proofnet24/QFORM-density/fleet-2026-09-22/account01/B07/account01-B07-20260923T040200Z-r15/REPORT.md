SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B07, 2026-09-23T04:02:00Z.
attacking: coordinate-minor selection via determinant-weighted Schur-complement averaging, converting the bi-anchor / fifth-volume-small survivor into a large mixture of physical 2x2 pivots with a small-energy or rank-two-tube residual.

# account01/B07 r15 — determinant-weighted Schur compound compiler

**Programme:** `QFORM-DENSITY-3EIG-20260922`  
**Role:** coordinate minor selection / aggregate-before-inversion  
**Status:** `ESSENTIAL_STEP_APPLIED / NEW SCHUR-COMPOUND MIXTURE REDUCTION / FULL QFORM OPEN / WITHOUT_VERIFIED_BRAIN`.

The unrestricted conjecture is not proved here. The new result is a deterministic matrix identity plus a quantitative application to the live B07 no-pivot branch. It avoids choosing and reciprocating one tiny coordinate minor: all inverse 2x2 pivots are weighted by their squared determinants before any conclusion is extracted.

## 1. Fresh sources and correction boundary

Final pre-publication control refresh: `yspennstate/math-research-brain@9bb30554b8625b25eac1b533e76655d1cb4735ce`, OWNER CONTROL revision `2026-09-22.15`; the sole target remained QFORM. The live correction inbox blob remained `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`.

The two mathematical inputs actually applied are:

1. **Designated partner account02/B07, latest completed run.**  
   `yspennstate/math-open-problems@67a5863d5e97c6b27499ccf7690d6008965f62c3`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account02/B07/20260923T033624Z-account02-B07-fd9b69f8f3ff/REPORT.md`.  
   In its non-low-tail four-bank branch, for a physical cross block `M`, `F=||M||_F`, and `0<theta<=1/2`,
   
   `P:=E3(M) >= (theta^2/6) F^6`.                                      (1.1)
   
   Its D5/rank-four dichotomy uses
   
   `eta_*(theta)=theta^6/(120*3072^2)`.                                (1.2)
   
   If the fifth-volume exit fails, then
   
   `E5(M)<eta_* F^10`.                                                  (1.3)
   
   Those are the exact partner inequalities used below. No claim is made that the partner's later physical heavy anchors coincide with the anchors selected here.

2. **Previous own B07 volume-gate reduction.**  
   `yspennstate/math-open-problems@024b6fce8657363e2999433732e0a3438c7a63c5`,  
   `proofnet24/QFORM-density/fleet-2026-09-22/account01/B07/account01-B07-20260923T033248Z-r14/REPORT.md`.  
   For the squared `3x3`-minor law of the same actual physical cross block `M`, the completed `q=4/3` fractional-volume theorem pays the form continuously unless there are a physical row anchor `i` and column anchor `j` for which the anchored third-compound mass
   
   `H3^(i,j):=sum_{R contains i,C contains j, |R|=|C|=3} det M[R,C]^2`
   
   satisfies
   
   `H3^(i,j)>P/3`.                                                       (1.4)

The false arbitrary-joint coarea lemma, conditional-density positive-moment gate, pointwise van-der-Corput bound, spectral-coordinate independence, and any one-tiny-minor reciprocal step are not used.

## 2. The Schur compound sandwich

Let `M` be any real `m x n` matrix. Fix a physical row anchor `i` and a physical column anchor `j`. For every integer `u>=3`, define the anchored `u`-compound mass

`H_u^(i,j)(M)
 := sum_{|R|=|C|=u, i in R, j in C} det M[R,C]^2`.              (2.1)

For each residual row `k!=i` and residual column `l!=j`, set

`P_ik={i,k}`, `Q_jl={j,l}`,
`d_kl=det M[P_ik,Q_jl]`.                                      (2.2)

Whenever `d_kl!=0`, reorder rows/columns only algebraically and form the exact rectangular Schur complement

`S_kl
 = M[P_ik^c,Q_jl^c]
   - M[P_ik^c,Q_jl] M[P_ik,Q_jl]^(-1) M[P_ik,Q_jl^c]`.        (2.3)

No random coordinate is rotated or transformed in probability space.

For any real matrix `S`, write

`E_t(S)=sum_{|A|=|B|=t} det S[A,B]^2=e_t(SS^T)`.               (2.4)

### Theorem 2.1 — `QFORM-ANCHORED-SCHUR-COMPOUND-SANDWICH-v1`

For every integer `t>=1`,

`boxed:
 H_(t+2)^(i,j)(M)
 <= sum_{k!=i,l!=j: d_kl!=0} d_kl^2 E_t(S_kl)
 <= (t+1)^2 H_(t+2)^(i,j)(M).
`                                                                       (2.5)

This is dimension free and remains valid with singular coordinate `2x2` pivots present.

### Proof

Fix one invertible physical pivot `B=M[P_ik,Q_jl]`. For any residual row `t`-set `A` and residual column `t`-set `C`, the block determinant formula gives exactly

`det M[P_ik union A,Q_jl union C]
 = det(B) det S_kl[A,C]`.                                      (2.6)

Squaring and summing over all such `A,C` proves

`d_kl^2 E_t(S_kl)
 = sum_{A,C} det M[P_ik union A,Q_jl union C]^2`.              (2.7)

Now sum (2.7) over every invertible incident physical pivot `(k,l)`. Consider a fixed nonzero anchored `(t+2)x(t+2)` determinant `D=det M[R,C]`, with `i in R,j in C`.

We need one elementary fact: inside an invertible square matrix with a distinguished row and distinguished column, at least one `2x2` minor containing both distinguished indices is invertible. Indeed, suppose all such minors vanish. If the distinguished entry `a` is nonzero, every entry of the complementary block equals `column*row/a`, so its Schur complement is zero and the whole matrix has rank at most two. If `a=0`, the identities `r_l c_k=0` for all residual `k,l` force either the distinguished row or distinguished column to vanish whenever one of them has a nonzero off-anchor entry; otherwise both are already zero. In every case a square matrix of order at least three is singular, contradiction.

Therefore `D^2` is counted at least once in the middle sum of (2.5). It can be counted at most once for each choice of the second pivot row in `R\{i}` and second pivot column in `C\{j}`, hence at most `(t+1)^2` times. Summing over all nonzero anchored `(t+2)` minors proves both inequalities. QED.

Two instances will be used:

`H3 <= Sigma1:=sum d_kl^2 E1(S_kl) <=4 H3`,                    (2.8)

`H5 <= Sigma3:=sum d_kl^2 E3(S_kl) <=16 H5 <=16 E5(M)`.       (2.9)

For a generic matrix every incident `2x2` pivot is nonzero and the upper factors `4` and `16` are exact counting multiplicities. Sparse matrices may attain the lower factor one; thus keeping the sandwich rather than asserting equality is essential.

## 3. A determinant-weighted residual law

Assume `H3>0`. Equation (2.8) gives `Sigma1>0`. Define a probability law on **invertible original-coordinate 2x2 pivots** by

`nu(k,l)=d_kl^2 E1(S_kl)/Sigma1`.                                  (3.1)

This is the key aggregate-before-inversion measure. A tiny determinant is automatically suppressed by its square; no bound on `1/|d_kl|` is requested.

Under `nu`, equations (2.8)-(2.9) give the exact useful ratio bound

`E_nu [ E3(S_kl)/E1(S_kl) ]
 = Sigma3/Sigma1
 <=16 E5(M)/H3`.                                               (3.2)

Terms with `E1(S_kl)=0` have zero `nu`-weight and need no convention beyond omission.

This identity is the main structural advance of the run: fifth compound mass of the original cross block controls, **in a determinant-extension weighted sense**, the residual third compound after conditioning on a physical `2x2` pivot.

## 4. Apply the designated partner result at the actual inequality

Now enter the partner account02/B07 branch (1.1)-(1.3), and suppose the previous `q=4/3` volume exit did not already pay the full quadratic form. Choose the anchors supplied by (1.4). Then

`H3>P/3`.                                                          (4.1)

Using (1.3) and (3.2),

`E_nu[E3(S)/E1(S)]
 < 16 eta_* F^10 /(P/3)
 = 48 eta_* F^10/P
 <=288 eta_* theta^(-2) F^4`.                                  (4.2)

By Markov, a set `G` of pivots carrying at least one half of the `nu`-mass satisfies

`E3(S_kl)/E1(S_kl)
 <576 eta_* theta^(-2)F^4
 = (24/5) theta^4 F^4/3072^2`.                                 (4.3)

Moreover the **un-normalized determinant-extension currency** on this good set is bounded below by

`sum_(k,l in G) d_kl^2 E1(S_kl)
 >=Sigma1/2
 >=H3/2
 >P/6
 >=theta^2 F^6/36`.                                            (4.4)

Thus a constant amount of third-volume currency is carried by good physical `2x2` pivots even if every individual pivot determinant is tiny.

This is an equation-level use of the newest completed account02/B07 theorem: its forced `E3` lower bound and its `E5`-small alternative are what make (4.3)-(4.4) dimension free.

## 5. Each good pivot has a small-energy or rank-two-tube Schur residual

Set

`rho:=theta^2/(16 sqrt(5))`.                                     (5.1)

Take any good pivot `(k,l) in G`, and write

`s=E1(S_kl)=||S_kl||_F^2`,
`T2(S_kl)=sum_(r>=3) sigma_r(S_kl)^2
         =dist_F(S_kl,{rank<=2})^2`.                             (5.2)

There are two cases.

### Case I: small residual energy

If

`s<rho F^2`,                                                     (5.3)

then

`boxed: ||S_kl||_F < [theta/(4*5^(1/4))] F.`                    (5.4)

### Case II: non-small residual energy

Assume `s>=rho F^2`. From (4.3),

`E3(S_kl)/s^3
 < [(24/5)theta^4/3072^2] F^4/s^2
 <= [(24/5)theta^4/3072^2]/rho^2
 =1/1536
 =(1/16)^2/6`.                                                   (5.5)

Use the same elementary tail-to-third-volume lemma already proved in the incoming partner chain: for any matrix `S`, if `T2(S)>=delta E1(S)`, then

`E3(S)>=(delta^2/6)E1(S)^3`.                                    (5.6)

The contrapositive of (5.6), with `delta=1/16`, and (5.5) yield

`boxed:
 T2(S_kl)<s/16,
 dist_F(S_kl,{rank<=2}) < (1/4)||S_kl||_F.
`                                                                        (5.7)

Therefore every pivot in a determinant-extension set carrying at least the currency (4.4) has the following **physical Schur residual dichotomy**:

`boxed:
 ||S_kl||_F < theta F/(4*5^(1/4))
 OR
 dist_F(S_kl,{rank<=2}) < ||S_kl||_F/4.
`                                                                        (5.8)

The constants line up exactly because

`[(24/5)/3072^2] / [1/(16sqrt5)]^2 =1/1536`.                    (5.9)

## 6. Main compiled theorem

### `QFORM-BIANCHOR-SCHUR-RANK2-MIXTURE-v1`

Let `M` be the actual original-coordinate cross block in the current non-low-tail partner branch, with `F=||M||_F` and `P=E3(M)>=(theta^2/6)F^6`. Assume:

1. the fifth-volume payment fails at the partner scale `eta_*=theta^6/(120*3072^2)`, so `E5(M)<eta_*F^10`;
2. the completed `q=4/3` third-volume gate does not already pay the full form, so physical anchors `i,j` exist with `H3^(i,j)>P/3`.

Then there exists a determinant-extension weighted set `G` of invertible **physical coordinate** `2x2` pivots containing row anchor `i` and column anchor `j` such that

`sum_G det(M[P,Q])^2 E1(S_PQ) > theta^2 F^6/36`,               (6.1)

and every pivot in `G` satisfies the dichotomy (5.8).

No selected pivot is asserted to have a determinant bounded below. No inverse determinant is averaged without its compensating determinant square. The result is dimension free and works with rectangular physical cross blocks.

## 7. Why this advances the unresolved bi-anchor curvature branch

The prior B07 survivor was: two physical anchors carry `>P/3` third-volume mass, a light residual determinant packet remains, and arbitrary same-bank curvature prevents replacing the light bank by a rank-two toy model.

The new theorem attacks exactly that obstruction at a different level. Rather than deleting the light curvature or selecting a single small minor, it conditions algebraically on **all** invertible anchored `2x2` pivots with determinant-extension weights. Partner `E5` smallness then forces at least constant aggregate extension currency into Schur residuals that are either:

- small in Frobenius energy relative to the original cross block, or
- quantitatively inside a relative Frobenius tube around rank two.

Thus the arbitrary-curvature residual has been compressed to a `small-energy OR rank-two-tube` mixture. This is substantially narrower than the previous unrestricted diffuse bi-anchor branch and lines up with the fleet's existing rank-two affine half-Riesz / pivot-plus-two-ridge receivers.

The remaining implication is not automatic: a mixture-level receiver is still needed because the good set may consist of many individually tiny pivots, and same-bank quadratic curvature plus the actual small-but-nonzero cross tail must remain present. One must not pick one pivot and pay `1/|det|`.

## 8. First unpaid implication

`QFORM-SCHUR-RANK2-MIXTURE-RECEIVER-v1`:

Starting from (6.1) and (5.8), prove a product-preserving density or half-Riesz bound for the **mixture** of physical `2x2` pivots, retaining arbitrary within-bank quadratic terms and the true residual cross block. The promising split is:

- small-energy residual: route the determinant-weighted pivot through a two-coordinate translated kernel while retaining the residual by a direct fractional-energy estimate;
- rank-two-tube residual: combine the orientation-free rank-two affine half-Riesz theorem with the determinant weight **before** reciprocal inversion, so the `det^2` currency cancels the `|det|^{-1/4}` loss on average.

A proof of that receiver would directly splice into the partner D5/rank-four survivor. It is not proved here.

## 9. Continuity and full-target status

This run proves a deterministic structural reduction only. It does not itself assert a new density bound, so there is no new continuity conclusion. The previously paid `q=4/3` branch remains continuous; the full conjecture and global continuity remain OPEN / NOT PROVED / NOT DISPROVED.

## 10. Finite verification

The companion `CHECKS.py` verifies the Schur compound sandwich on dense Gaussian matrices and sparse integer matrices (including a 3-cycle permutation example where the lower counting factor one is attained), and checks the constant identity in (5.9). These checks are regression controls, not a proof.
