SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet01, slot B09, 2026-09-23T14:14:40Z.
attacking: the zero/near-zero scalar-pivot two-row collar by replacing the outer-square route with an invertible indefinite physical pair, then smoothing its logarithmic singularity by a single exact Schur cross direction.

# fleet01/B09 — indefinite physical pair + one Schur cross direction

Run: `20260923T141440Z-fleet01-B09-QFORM-auto11`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Fresh owner control at publication: revision `2026-09-22.15`  
Status: **ESSENTIAL_STEP_APPLIED / NEW SUPPORTING THEOREM / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`

The unrestricted conjecture and the full-target continuity conclusion remain open. This report proves a new source-coordinate smoothing theorem that is tailored to the B09 zero-pivot/two-row-collar frontier. It does not rotate the independent variables, does not use law-uniform pointwise van-der-Corput decay, and does not convert an `O(sqrt(epsilon))` estimate into a density estimate.

## 1. Inputs used at their exact scopes

Two completed source results are used.

1. **Physical-pair logarithmic envelope.** From
   `yspennstate/math-open-problems@f7f0fedb2d93b46824f96cac1164af6f8a55626f`,
   `proofnet24/QFORM-density/interactive/20260922T180015Z-pair-log/PAIR_LOG_THEOREM.md`:
   for independent cap-one physical coordinates `(U,V)`, an invertible indefinite symmetric pair matrix `E`,
   `D=|det E|`, `kappa=sigma_min(E)`, and arbitrary deterministic affine shift, the conditional pair density obeys for every `r>0`

   `p_pair(t) <= 2 sqrt(2)/r + D^(-1/2) log_+(2 r^2/(kappa |t-t0|)).`     (1.1)

   The shift may depend on all other original coordinates after conditioning.

2. **Fractional one-volume compiler.** From fleet03/B01,
   `yspennstate/math-open-problems@936b0f0bad22de82921c2a743fb0738226270348`,
   `proofnet24/QFORM-density/fleet-2026-09-22/fleet03/B01/fleet03-B01-20260923T013054Z-auto11/REPORT.md`:
   for disjoint original-coordinate banks and

   `R=F(X_I)+2 X_I^T C X_J+G(X_J)`,

   with arbitrary measurable same-bank functions `F,G`, define
   `Z_1=e_1(C^T C)=||C||_F^2`. Taking `k=1,q=2,gamma=1/8` in its Theorem 2.1 is always legal, because every one-volume row marginal is at most one. It gives

   `H_(1/8)(R):=sup_s E|R-s|^(-1/8)
      <= C_* Z_1^(-1/16),`                                      (1.2)

   where

   `C_*=32 c_(1/8) e^(1/8) pi^(1/8) 2^(-1/16)
       =2.7110652078...`,

   and

   `c_gamma=2^(1-gamma) Gamma((1-gamma)/2)
            /(2 sqrt(pi) Gamma(gamma/2)).`

This one-volume use has **no row-spread assumption**. Arbitrary within-bank quadratic curvature and outside-conditioned affine terms are retained by the cited theorem.

## 2. New theorem: one nonzero Schur cross pays an indefinite physical pair

Let `P={i,j}` be two ORIGINAL coordinates and suppose their physical principal matrix

`E=A[P,P]`

is invertible and indefinite. Put

`D=|det E|>0`, `kappa=sigma_min(E)>0`.

Let `U,V` be disjoint sets of remaining ORIGINAL coordinates. Complete the pair exactly. The full form can be written

`Q=(X_P+m(X_{P^c}))^T E (X_P+m(X_{P^c}))+R(X_{P^c}),`          (2.1)

where `R` is the exact Schur-complement quadratic-plus-affine form. Let

`C=A[U,V]-A[U,P] E^(-1) A[P,V]`                               (2.2)

be one physical cross block of that Schur complement. All other remaining coordinates may be conditioned; hence the residual still has the form required by (1.2), with this same `C` and arbitrary self phases.

### Theorem `QFORM-INDEFINITE-PAIR-PLUS-ONECROSS-v1`

If `C!=0`, then the law of `Q` has an essentially bounded density and

`boxed:
 ||p_Q||_infinity
 <= 11.463 D^(-2/5) kappa^(-1/10) ||C||_F^(-1/10).`            (2.3)

Equivalently, with `Z_1=||C||_F^2`,

`||p_Q||_infinity
 <=11.463 D^(-2/5) kappa^(-1/10) Z_1^(-1/20).`                 (2.4)

Therefore every interval `L` satisfies

`boxed:
 P{Q in L}
 <=11.463 D^(-2/5) kappa^(-1/10) Z_1^(-1/20) |L|.`             (2.5)

Continuity is **not claimed** by this argument.

### Proof

Condition on all coordinates except the physical pair. Applying (1.1) and averaging over the remainder gives, for every `r>0`,

`p_Q(t)
 <= 2sqrt(2)/r
  + D^(-1/2) E log_+(2r^2/(kappa |t-R|)).`                    (2.6)

For every `gamma>0` and `x>=1`,

`log x <= x^gamma/(e gamma)`,                                  (2.7)

because `y exp(-gamma y)` is maximized at `y=1/gamma`. Taking `gamma=1/8`, (1.2) and (2.7) give

`p_Q(t)
 <= A r^(-1)
  + B r^(1/4),`                                                (2.8)

where

`A=2sqrt(2)`,

`B= D^(-1/2) kappa^(-1/8) Z_1^(-1/16)
     * (8/e) 2^(1/8) C_*.`                                    (2.9)

For `m=1/4`,

`min_(r>0) [A/r+B r^m]
 =(1+m) B^(1/(1+m)) (A/m)^(m/(1+m)).`                         (2.10)

Substitution yields

`||p_Q||_infinity
 <=K_* D^(-2/5) kappa^(-1/10) Z_1^(-1/20),`                  (2.11)

with

`K_*=(5/4)(4A)^(1/5)
       [(8/e)2^(1/8)C_*]^(4/5)
     =11.4625801249... <11.463.`                               (2.12)

This proves (2.3)--(2.5). The matrix scaling is exact: under `A -> sA`, the right side scales by `|s|^(-1)`.

The proof retains original-coordinate independence only where it exists. The pair is conditioned in the original variables; the residual cross estimate is the coupled original-coordinate fractional-volume estimate. No independence is asserted after any spectral rotation.

## 3. Exact structural identity: pair-anchored third volume survives Schur elimination

The theorem above can be certified before pair elimination by an exact physical-minor identity.

Write

`M=A[P union U,V]`,

and let `a,b` be the two rows `A[P,V]`. Put

`Delta=||a wedge b||^2`.

For `k in U`, let `m_k=A[k,V]` and let `c_k` be the corresponding row of the Schur cross `C`. From (2.2),

`c_k=m_k-lambda_(k,1) a-lambda_(k,2) b`                       (3.1)

for the exact coefficients `lambda_k=A[k,P]E^(-1)`. Hence

`boxed: a wedge b wedge c_k = a wedge b wedge m_k.`            (3.2)

Define the full pair-anchored physical third-volume

`V_P(M)
 =sum_(k in U) sum_(T subset V, |T|=3)
       det M[P union {k},T]^2
 =sum_k ||a wedge b wedge m_k||^2.`                            (3.3)

By (3.2) and the elementary wedge inequality,

`V_P(M)
 =sum_k ||a wedge b wedge c_k||^2
 <=Delta sum_k ||c_k||^2
 =Delta ||C||_F^2.`                                           (3.4)

Thus, whenever `V_P(M)>0`, automatically `Delta>0`, `C!=0`, and

`boxed: ||C||_F^2 >= V_P(M)/Delta.`                           (3.5)

Combining (2.4) and (3.5) gives the source-coordinate corollary

`boxed:
 ||p_Q||_infinity
 <=11.463 D^(-2/5) kappa^(-1/10)
      Delta^(1/20) V_P(M)^(-1/20).`                           (3.6)

The same coefficient times `|L|` bounds every interval probability.

This is the desired exact structural bridge for the zero-pivot collar: if `A_ii=0` but some companion `j` has `A_ij!=0`, then the physical pair

`[[0,A_ij],[A_ij,A_jj]]`

is automatically invertible indefinite. If that pair participates in positive pair-anchored third volume across a disjoint physical column bank, the branch is paid by (3.6), with no scalar-pivot division at all.

## 4. Target-valid stress example with zero scalar diagonals

Take the six-coordinate symmetric matrix whose only nonzero upper-triangular entries are

`A_12=A_14=A_25=A_36=1`.

Its graph is a four-vertex path `4-1-2-5` plus the edge `3-6`, so its spectrum is

`{phi,1,phi^(-1),-phi^(-1),-1,-phi}`,

where `phi=(1+sqrt(5))/2`. Thus at least four eigenvalues have modulus at least one.

Choose `P={1,2}`, `U={3}`, `V={4,5,6}`. Then

`E=[[0,1],[1,0]]`, hence `D=kappa=1`,

`a=(1,0,0)`, `b=(0,1,0)`, `Delta=1`,

and `m_3=(0,0,1)`. Since `A[3,P]=0`, the Schur cross row is the same `c_3=m_3`; therefore

`V_P(M)=1`, `||C||_F^2=1`.

The new theorem gives, for every admissible independent cap-one product law,

`boxed: ||p_(X^T A X)||_infinity <11.463,`

`boxed: P{X^T A X in L}<11.463 |L|.`                           (4.1)

This example specifically has `A_11=A_22=0`; it is outside any proof that needs a nonzero scalar square pivot.

## 5. Newest designated partner actually applied

Newest fleet02/B09 theorem consumed:

`QFORM-ONE-ANCHOR-THREEVOLUME-HYBRID-v1`,

canonical mathematics
`yspennstate/math-open-problems@59ccddd0766b466b30abd645926887f907b0bcd7`,
`proofnet24/QFORM-density/fleet-2026-09-22/fleet02/B09/20260923T134326Z-fleet02-B09-QFORM-r13/REPORT.md`.

It says that a selected family of physical `3x3` cross minors with compulsory physical row `h`, total squared determinant mass `Z`, anchor cross-row norm `||a||`, and every other selected row marginal at most `1/2` has a continuous density satisfying

`||p_Q||_infinity
 <=5*2^(4/5)*sqrt(e) ||a||^(1/5) Z^(-1/5).`                  (5.1)

Apply it to the literal cross-only target

`A_*=[[0,M],[M^T,0]]`,

where

`M = [(1,0,0),
      (0,1/sqrt(2),0),
      (0,1/sqrt(2),0),
      (0,0,1/sqrt(2)),
      (0,0,1/sqrt(2))].`

Here `M^T M=I_3`, so `A_*` has six nonzero eigenvalues, exactly three `+1` and three `-1`. Select the four nonzero `3x3` minors containing the first row, one of rows 2--3, and one of rows 4--5, with all three columns. Each squared determinant is `1/4`, so

`Z=1`, `||a||=1`,

and every non-anchor row marginal is exactly `1/2`. Therefore (5.1) gives the actual target inequality

`boxed:
 ||p_(X^T A_* X)||_infinity
 <=5*2^(4/5)*sqrt(e)
 =14.3529523... <14.353,`                                     (5.2)

with a continuous density and

`P{X^T A_* X in L}<14.353 |L|.`                               (5.3)

This is an actual application of the designated partner result, not a citation-only mention.

## 6. What this changes, and what remains unpaid

The preceding B09 branch `QFORM-TWOROW-COLLAR-ZEROPIVOT-OR-PAIR-EXIT-v1` split after a heavy anchored third-volume row. The new theorem pays a previously delicate subbranch:

- scalar pivot `A_ii` may be exactly zero;
- choose a companion physical row `j` with `A_ij!=0`, so the two-coordinate physical pair is automatically invertible indefinite;
- if the pair-anchored third volume is positive, Schur elimination cannot erase it: (3.2)--(3.5) produce a genuine residual cross direction;
- one residual cross direction is enough because only a **positive fractional potential** is needed to average the pair's logarithmic singularity.

The first unpaid implication is now

`QFORM-ZEROPIVOT-NO-INVERTIBLE-COLLAR-PAIR-ROUTING-v1`:

> In the aggregate-heavy zero-pivot collar, if every companion row carrying the remaining third-volume has `A_ij=0` (or if all quantitative pair certificates degenerate), route the resource directly through conditional linear anti-concentration / grouped cross-volume, or force an already-paid definite/singular pair, one-anchor three-volume, ridge, or grouped-square exit. No argument may infer a good individual pair merely from a large spectral eigenvalue.

The quantitative degeneration `D,kappa,V_P ->0` is not claimed uniformly controlled here. Closing that structural alternative is still required for the full theorem.

## 7. Correction audit

This proof respects the live source corrections. It uses no law-uniform pointwise quadratic-phase decay; no post-rotation independence; no arbitrary-joint rank-three coarea bound; no naive worst-fiber supremum; no assertion that one scalar pivot leaves a rank-two cross block; and no claim that a square plus one heavy cross coefficient absorbs arbitrary same-bank curvature. The residual fractional-volume theorem explicitly keeps the arbitrary same-side curvature.

**Conclusion:** supporting theorem proved at the stated quantitative scope; full QFORM remains OPEN; full-target continuity remains OPEN; independent end-to-end review of this new splice is still required before promotion beyond supporting-theorem status.
