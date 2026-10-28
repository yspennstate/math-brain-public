SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B08, 2026-09-24T07:21:14Z.
attacking: the localized-row residue of the diffuse top-three router; prove that a physical deletion retains three spectral directions unless the fourth eigenvector itself localizes, then apply the account04/B08 child-window theorem at the forced scale.

# account03/B08 r51 — four-frame deletion retention and localized-row compiler

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / quantitative inequalities and rigorous computations  
Status: **NEW SUPPORTING SPECTRAL-DELETION THEOREM / DESIGNATED PARTNER APPLIED / FULL TARGET OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture remains **OPEN**. The new point is a deterministic compression inequality which converts the r50 unpaid physical-row branch into either (i) a child with three quantitatively large singular directions, hence consumable by the completed account04/B08 theorem, or (ii) a genuinely localized fourth eigenvector. No moment, compact-support, Gaussian, log-concavity, connected-support, post-rotation independence, arbitrary-joint coarea, or law-uniform scalar quadratic-phase decay is used.

## 1. Source boundary and inherited live state


The inherited B08 theorem is my r50 report

`yspennstate/math-open-problems@647a9d9a5f52b6867cedf6d7469ce3fd6e6e466a`

`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T042041Z-account03-B08-qform-diffuse-r50/REPORT.md`.

Let `s_1(A)>=s_2(A)>=...` denote the singular values of the real symmetric coefficient matrix, equivalently the ordered absolute eigenvalues. r50 proved the following router. If

` s_3(A)>=L>0`                                                    (1.1)

and the selected top-three absolute-eigenvalue frame `U_3` obeys

` p_i^(3):=||(U_3)_{i,*}||_2^2 <=1/48` for every physical i,     (1.2)

then either

`p_Q in C_0(R),  ||p_Q||_infinity <197.779/L`,                  (1.3)

or, on the unpaid large-fourth-spectrum branch,

` s_4(A)>eta_* L`,                                               (1.4)

with

` eta_*=0.31987395050000694...`,                                (1.5)

and there is an ORIGINAL physical coordinate `k` satisfying

` max{|A_kk|,||A[k,-k]||_2}>eta_* L/512`
` =0.0006247538095703261... L.`                                  (1.6)

This coordinate comes from failure of the ambient ridge-window leverage gate. r50 deliberately stopped here because a single scalar/star witness is not by itself a universal density theorem.

The designated partner theorem used below is account04/B08 r2,

`QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`,

`yspennstate/math-open-problems@a5e66e2944c89857a41d5e18c283d53a4307be76`,

`proofnet24/QFORM-density/fleet-2026-09-22/account04/B08/20260923T212412Z-account04-B08-QFORM-r2/REPORT.md`.

For an ORIGINAL-coordinate deletion child `C`, if `s_3(C)>=m>0` and the physical spectral projection of `C` onto `|lambda(C)|>=m/64` has maximum diagonal at most `1/32`, then the full parent quadratic form has

` ||p_Q||_infinity <= [288 sqrt(3e)/(13m)] <64/m`,               (1.7)

and `p_Q in C_0(R)`. The deleted parent coordinate, its whole cross vector, all signs, and all other child coefficients are retained.

## 2. Spectral deletion retention

The central new lemma is purely deterministic.

### Theorem 2.1 — `QFORM-SPECTRAL-DELETION-RETENTION-v1`

Let `A=A^T in R^(n x n)`. Fix `r>=2`. Let `E_r` be an invariant subspace spanned by eigenvectors corresponding to the `r` largest absolute eigenvalues, let `P_r` be the orthogonal projection onto `E_r`, and put

` p_i^(r):=<P_r e_i,e_i>.                                       (2.1)

Let `C_i=A[-i,-i]` be the ORIGINAL-coordinate principal deletion. Then

` boxed: s_(r-1)(C_i) >= s_r(A) sqrt(1-p_i^(r)). `               (2.2)

This has no hypothesis on `s_(r+1)(A)`, no sign hypothesis, and no coefficient-size hypothesis outside the first `r` spectral directions.

### Proof

Identify the child coordinate space with

` H_i=e_i^perp subset R^n`,                                     (2.3)

so the child operator is exactly

` C_i=P_(H_i) A |_H_i`.                                         (2.4)

Because `dim E_r=r`, the intersection

` F_i:=E_r cap H_i`                                              (2.5)

has dimension at least `r-1`.

Take `x in F_i`. Since `E_r` is spectral and therefore invariant under `A`,

` Ax in E_r`.                                                    (2.6)

For every `y in E_r`,

` <e_i,y>=<P_r e_i,y>`,                                         (2.7)

and Cauchy-Schwarz gives

` |<e_i,y>| <= ||P_r e_i|| ||y|| =sqrt(p_i^(r)) ||y||`.         (2.8)

Hence

` ||P_(H_i)y||^2
 =||y||^2-|<e_i,y>|^2
 >=(1-p_i^(r))||y||^2`.                                        (2.9)

Apply (2.9) to `y=Ax`. Since every eigenvalue of `A|_(E_r)` has modulus at least `s_r(A)`,

` ||C_i x||
 =||P_(H_i)Ax||
 >=sqrt(1-p_i^(r)) ||Ax||
 >=s_r(A)sqrt(1-p_i^(r)) ||x||`.                               (2.10)

Finally use the max-min characterization of singular values,

` s_(r-1)(C_i)
 =max_(dim F=r-1) min_(0!=x in F) ||C_i x||/||x||`,             (2.11)

and choose any `(r-1)`-dimensional subspace of `F_i`. This proves (2.2). QED.

The crucial feature is that the tail spectrum never appears as an operator-norm perturbation. The proof spends an actual `(r-1)`-dimensional physical-deletion subspace on which `A` remains spectrally large before the final coordinate projection.

### Corollary 2.2 — four-frame child persistence

For `r=4`, if `U_4` is a nested four-eigenvector frame and

` p_i^(4)=||(U_4)_{i,*}||^2`,                                  (2.12)

then

` boxed: s_3(A[-i,-i]) >= s_4(A) sqrt(1-p_i^(4)). `             (2.13)

This is exactly the dimension needed by the account04/B08 child-window theorem.

## 3. Apply the lemma to the r50 unpaid coordinate

Stay in the r50 diffuse-top-three state (1.1)-(1.6). Extend the selected top-three eigenframe `U_3` to a nested top-four absolute-eigenvalue frame

` U_4=[U_3,v_4]`,                                               (3.1)

where `v_4` is a unit eigenvector with eigenvalue magnitude `s_4(A)`. At the r50 localized coordinate `k`,

` p_k^(4)=p_k^(3)+|v_4(k)|^2`.                                  (3.2)

A useful parameterized dichotomy is immediate. For any `tau in (0,47/48)`, either

` p_k^(4)>1-tau`,                                                (3.3)

in which case (1.2) and (3.2) force

` boxed: |v_4(k)|^2 > 1-tau-1/48 =47/48-tau, `                 (3.4)

or

` p_k^(4)<=1-tau`,                                              (3.5)

in which case Theorem 2.1 and (1.4) give the literal deletion child

` C_k=A[-k,-k]`                                                  (3.6)

three large singular directions at scale

` boxed: s_3(C_k) >= s_4(A)sqrt(tau) > eta_* sqrt(tau) L. `     (3.7)

This is the missing implication r50 did not have: a fourth ambient spectral direction survives a physical deletion as a third child direction unless the deleted coordinate itself carries a large portion of the four-dimensional spectral packet.

## 4. Designated account04/B08 result applied at the forced scale

Take the concrete balanced choice

` tau=1/2`.                                                      (4.1)

Then (3.4) becomes the strong fourth-eigenvector localization certificate

` boxed: |v_4(k)|^2>23/48=0.4791666666... . `                   (4.2)

Otherwise (3.7) gives

` s_3(C_k)>m_*L`,                                                (4.3)

where

` m_*:=eta_*/sqrt(2)=0.22618503952348493... .`                  (4.4)

Now apply the completed account04/B08 theorem (1.7) to this ACTUAL child and this ACTUAL forced scale. Let

` P_child=1_{|C_k|>=m_*L/64}`.                                  (4.5)

If

` max_j (P_child)_jj <=1/32`,                                  (4.6)

then

` boxed:
 p_Q in C_0(R),
 ||p_Q||_infinity
 <=288sqrt(3e)/(13m_*L)
 =279.7004258595.../L
 <282.955/L.
 `                                                                  (4.7)

This is a literal use of the designated partner result, not only a citation.

If (4.6) fails, choose a child physical coordinate `j` with `(P_child)_jj>1/32`. The child spectral energy gives

` ||C_k e_j||_2 > (m_*L/64)/sqrt(32)
 =m_*L/(256sqrt(2)).`                                           (4.8)

Splitting this row norm into its diagonal and off-diagonal parts gives

` max{|(C_k)_jj|,||(C_k)[j,-j]||_2}>m_*L/512`.                 (4.9)

Because `C_k` is a literal principal child, the parent diagonal is the same and the parent off-diagonal row norm can only be larger. Therefore there is a SECOND ORIGINAL coordinate `j!=k` with

` boxed:
 max{|A_jj|,||A[j,-j]||_2}
 > eta_*L/(512sqrt(2))
 =0.0004417676553193065... L.
 `                                                                  (4.10)

Together with (1.6), the surviving state now has two distinct quantitative physical-row witnesses.

## 5. Compiled diffuse-to-structured router

Combining r50 with Sections 2-4 gives the following sharpened conclusion.

### Theorem 5.1 — `QFORM-DIFFUSE-TOP3-FOURFRAME-CHILD-COMPILER-v1`

Assume `s_3(A)>=L` and the selected top-three frame has maximum physical leverage at most `1/48`. Then at least one of the following holds:

1. `p_Q` is continuous and vanishes at infinity with

   `||p_Q||_infinity<197.779/L`;                                (5.1)

2. `p_Q` is continuous and vanishes at infinity with

   `||p_Q||_infinity<279.701/L`;                                (5.2)

3. there is an original coordinate `k` carrying the r50 row witness (1.6), and the selected fourth eigenvector satisfies

   `|v_4(k)|^2>23/48`;                                          (5.3)

4. there are two distinct original coordinates `k!=j` satisfying

   `max{|A_kk|,||A[k,-k]||_2}>0.0006247538095703261 L`,          (5.4)

   `max{|A_jj|,||A[j,-j]||_2}>0.0004417676553193065 L`.          (5.5)

The second paid branch is logically nested inside the former r50 unpaid branch; (5.1) remains the better numerical payment where it already applies. The value of (5.2) is structural: it consumes the r50 deletion residue using a theorem of the designated partner at a scale forced by the ambient fourth spectral direction.

Equivalently, the one-row remainder of r50 is no longer the correct diffuse obstruction. The only unpaid diffuse descendants are a **strongly localized fourth eigenvector at that physical row** or **two distinct localized physical rows**.

A parameterized version replaces `23/48` by `47/48-tau`, the child scale by `eta_*sqrt(tau)L`, the partner bound by

` [288sqrt(3e)/(13 eta_* sqrt(tau))] L^(-1)`,                   (5.6)

and the second-row witness by

` eta_*sqrt(tau)L/512`.                                         (5.7)

No probabilistic input is used before the final partner theorem.

## 6. Rigorous computation / regression

A seeded finite-dimensional regression checked Theorem 2.1 in the live `r=4` specialization on 60,000 random symmetric deletion instances in dimensions `5` through `19`. For each instance the eigenvectors were sorted by absolute eigenvalue, `p_i^(4)` was computed directly, and the literal child singular value `s_3(C_i)` was compared with

` s_4(A)sqrt(1-p_i^(4))`.                                       (6.1)

There were zero violations. The smallest observed ratio

` s_3(C_i)/[s_4(A)sqrt(1-p_i^(4))]`

was `1.0042204030179638`. This is regression evidence only; Theorem 2.1 is proved analytically above.

The live constants evaluate to

`eta_*=0.31987395050000694`,
`m_*=0.22618503952348493`,
`288sqrt(3e)/(13m_*)=279.70042585957196`,
`64/m_*=282.95416944830623`,
`m_*/512=0.0004417676553193065`,
`eta_*/512=0.0006247538095703261`.                               (6.2)

## 7. Remaining implication

The full target remains OPEN. This run replaces

`QFORM-LOCALIZED-ROW-PLUS-THREE-SPECTRAL-DIRECTIONS-COMPILER-v2`

by the sharper two-way debt

`QFORM-LOCALIZED-V4-OR-TWO-PHYSICAL-ROWS-COMPILER-v1`.

One must now consume either:

- the same physical coordinate has the r50 scalar/star witness and carries `>23/48` of the selected fourth eigenvector, or
- two distinct physical coordinates have the explicit row currencies (5.4)-(5.5).

The newest exact single-leaf theorem from account02/B01 shows why the almost-single-edge limit should be split only after spending the third spectral direction, but it is not silently promoted to the arbitrary two-row state. A valid next step is to prove that the two-row alternative forces either a nontrivial edge/tail half-Riesz currency, a uniformly controlled two-coordinate Schur pivot, or a further child retaining three large directions. The strong-v4 branch should be attacked separately by a product-preserving localized-coordinate completion. Full-target essential boundedness and global continuity are not claimed.
