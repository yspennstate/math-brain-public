SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account01, slot B12, 2026-09-24T02:16:12Z.
attacking: spectral-packet transfer through resolvent defect and inverse-free compression stability; mechanism switched to exact physical cross-volume resonance repair.

# account01/B12 — rank-one cross-volume resonance repair for arbitrary signed eigenvalue additions

Programme: `QFORM-DENSITY-3EIG-20260922`  
Role: Additional eigenvalue control  
Status: **PROVED SUPPORTING THEOREM / FULL QFORM OPEN**  
Continuity: **continuous C0 density is proved for the explicit D5 family below; unrestricted continuity remains OPEN.**

## 1. Purpose and first missing implication

Earlier carrier/Woodbury estimates isolate a finite-dimensional resonance matrix, but become weak precisely when a large signed eigenvalue is tuned near a destructive resonance. This run attacks that resonance rather than assuming it away.

The key observation is that for a physical ORIGINAL-coordinate cross block, a rank-one spectral update has an exact Gram-determinant formula with two terms:

1. the scalar destructive resonance `(1+theta q)^2`;
2. a nonnegative **transverse repair** `theta^2 r`.

If the added eigenvector has any quantitative component transverse to the old cross-column range, exact cancellation is impossible for every sign and every magnitude of the added eigenvalue.

No random coordinates are rotated and no quadratic remainder is treated as an independent convolution.

## 2. Exact rank-one cross-volume identity

Let `M` be a real `p x m` matrix, `p>=m`, with full column rank. Put

`G=M^T M`.

Let `a in R^p`, `b in R^m`, and add the arbitrary rank-one matrix

`M_theta=M+theta a b^T`, `theta in R`.

Define

`c=M^dagger a=G^{-1}M^T a`,
`a_perp=(I-MM^dagger)a`,
`q=b^T c`,
`r=||a_perp||^2 b^T G^{-1}b`.

Then `r>=0` and:

### Theorem 2.1 — `QFORM-RANKONE-CROSS-VOLUME-RESONANCE-REPAIR-v1`

`det(M_theta^T M_theta)`
` = det(G) [ (1+theta q)^2 + theta^2 r ].`                 (2.1)

Consequently, if `q^2+r>0`,

`inf_{theta in R} det(M_theta^T M_theta)/det(G)`
` = r/(q^2+r).`                                             (2.2)

If `q=r=0`, the determinant ratio is identically one.

In particular:

- if `r>0`, the physical `m`-volume never collapses for **any** `theta`, positive or negative and arbitrarily large;
- if `r=0` and `q!=0`, the only exact destructive amplitude is `theta=-1/q`;
- if `q=0`, then the update is volume nondecreasing.

Thus amplitude and sign are not the correct currencies. The dangerous object is the ratio of longitudinal resonance `q^2` to transverse repair `r`.

### Proof

Decompose

`a=M c+a_perp`, `M^T a_perp=0`.

Then

`M_theta=M L+theta a_perp b^T`,
`L=I_m+theta c b^T`.

The two codomain pieces are orthogonal, hence

`M_theta^T M_theta=L^T G L+theta^2 ||a_perp||^2 b b^T`.       (2.3)

If `1+theta q!=0`, then the matrix determinant lemma and the rank-one inverse formula give

`det(L)=1+theta q`,
`L^{-T}b=b/(1+theta q)`.

Therefore

`det(M_theta^T M_theta)`
`=det(G)det(L)^2 [1+theta^2||a_perp||^2 b^T(L^TGL)^{-1}b]`
`=det(G)[(1+theta q)^2+theta^2||a_perp||^2 b^TG^{-1}b]`,

which is (2.1). Both sides are polynomials in `theta`, so the identity extends across `1+theta q=0` by continuity.

Finally,

`(1+theta q)^2+theta^2 r`
`=1+2q theta +(q^2+r)theta^2`.

For `q^2+r>0` its minimum occurs at `theta=-q/(q^2+r)` and equals `r/(q^2+r)`. QED.

## 3. Spectral-packet iteration

Let an arbitrary symmetric added packet be written spectrally as

`E=sum_{j=1}^R theta_j v_j v_j^T`,

with orthonormal `v_j` and arbitrary real eigenvalues `theta_j` of either sign and magnitude. Fix disjoint ORIGINAL-coordinate banks `I,J`, `|I|=p>=m=|J|`, and let

`a_j=P_I v_j`, `b_j=P_J v_j`.

If the baseline physical cross block is `M_0=A_0[I,J]`, define recursively

`M_j=M_{j-1}+theta_j a_j b_j^T`.

Whenever `M_{j-1}` has full column rank, Theorem 2.1 gives an exact factor

`F_j=(1+theta_j q_j)^2+theta_j^2 r_j`,

where `q_j,r_j` are computed from the **actual current** `M_{j-1}`. Hence

`boxed: det(M_R^T M_R)=det(M_0^T M_0) prod_{j=1}^R F_j.`      (3.1)

If `r_j>0`, then uniformly over the amplitude and sign of the j-th added eigenvalue,

`F_j >= gamma_j:=r_j/(q_j^2+r_j)>0`.                          (3.2)

Thus a finite or large signed spectral packet is controlled by geometric repair ratios, not by `max |theta_j|`.

This is an exact deterministic reduction. It does not assume that the eigenvectors of `E` diagonalize `A_0`, and it does not rotate the product input law.

## 4. Arbitrarily many small signed eigenvalues

Let `E_low=E_low^T` have all eigenvalues in `[-h,h]`; equivalently `||E_low||op<=h`. Let `T=T^T` be any further tail for which only the local physical cross action is controlled,

`||T[I,J]||op<=delta`.

The outside-outside block of `T` may be arbitrarily large. If a high-mode cross block `M_hi` has

`s_m(M_hi)>=g_hi`,

then singular-value Weyl gives

`boxed: s_m(A[I,J]) >= g_hi-h-delta.`                         (4.1)

Thus **arbitrarily many** smaller eigenvalues of either sign and orientation cost only the single spectral threshold `h`; no density convolution argument is used.

## 5. Exact noncommuting six-mode family with arbitrary signed amplitudes

Take two disjoint ORIGINAL-coordinate banks

`I={1,...,12}`, `H={13,...,18}`,

so `|I|=12`, `|H|=6`. Define a symmetric baseline whose `I x H` cross block is

`M_0 = [ 2 I_6 ; 0_6 ]`                                      (5.1)

and whose other core blocks may initially be zero.

For `j=1,...,6`, define a unit vector `v_j` by

`P_I v_j=(e_j+e_{6+j})/2`,
`P_H v_j=e_j/sqrt(2)`.

The six `v_j` are orthonormal. Add

`E_hi=sum_{j=1}^6 theta_j v_jv_j^T`,                          (5.2)

where the six `theta_j` are **completely arbitrary real numbers**, independently chosen in sign and magnitude. Hence the added matrix itself has six arbitrary signed eigenvalues `theta_j`.

The resulting physical cross block has mutually orthogonal columns

`M_hi e_j = 2 e_j + x_j(e_j+e_{6+j})`,
`x_j=theta_j/(2sqrt(2))`.                                    (5.3)

Therefore

`||M_hi e_j||^2=(2+x_j)^2+x_j^2`
`               =2(x_j+1)^2+2 >=2`,

and the columns are orthogonal. Hence

`boxed: s_6(M_hi)>=sqrt(2)`                                  (5.4)

**uniformly over all six signs and all six unbounded amplitudes**.

At the one-mode level, Theorem 2.1 has

`q=1/(4sqrt(2))`, `r=1/32`, `q^2=r`,

so the determinant factor is at least `1/2` for every `theta`; (5.4) is the sharper simultaneous orthogonal-column statement.

Now add:

- any symmetric `E_low` with `||E_low||op<=1/8` (arbitrary rank, signs, multiplicities and orientation);
- any symmetric `T` satisfying only `||T[I,H]||op<=1/8`;
- any further symmetric spectator `S` with `S[I,H]=0`, of arbitrary dimension/rank/sign/operator norm.

Then from (4.1),

`g:=s_6(A[I,H]) >= sqrt(2)-1/4`
` =1.1642135623730951... >1.`                                 (5.5)

Since

`(A^2)[H,H] = A[H,*]A[*,H] >= A[H,I]A[I,H]`,

we obtain the actual final-matrix inequality

`boxed: lambda_6((A^2)[H,H]) >= g^2.`                         (5.6)

Also restriction of the domain to `H` gives

`s_6(A)>=s_6(A P_H)>=s_6(A[I,H])>=g`,

so in particular

`boxed: s_3(A)>=g>1.`                                         (5.7)

Every matrix in this family is therefore literally in the owner's exact target class.

## 6. Required account02/B12 partner theorem applied to the actual inequality

The completed partner result is:

`QFORM-SIX-MODE-SPECTRAL-SQUARE-CARRIER-v1`

from

`yspennstate/math-open-problems@e6c20a6e5a077c71e1ae7ac27e71d889a5e6a004`

`proofnet24/QFORM-density/fleet-2026-09-22/account02/B12/20260923T145451Z-account02-B12-QFORM-r36/REPORT.md`.

It states that if an ORIGINAL-coordinate set `H`, `|H|=m>=6`, satisfies

`lambda_6((A^2)[H,H])>=g^2`, `s_3(A)>=s`,

then, with `N=binom(m,2)`, the canonical choice `b=g/2`, `a=g/(4N)` gives

`||p_Q||inf <= max {`
`  8N sqrt(6 pi m)/g,`
`  4 pi N/g,`
`  3*400^(1/3)*(4N/g)^(5/6)*s^(-1/6),`
`  10sqrt(2e)/(sqrt(3)g)`
`}.`                                                           (6.1)

Apply (6.1) to the **actual final matrix** in Section 5 with `m=6`, `N=15`, and `s=g=sqrt(2)-1/4`. The four terms are

`1096.16209078571...`,
`161.908059919148...`,
`575.750918636213...`,
`11.5629582401142...`.

Therefore

`boxed: ||p_Q||_(infinity,ess) < 1097.`                       (6.2)

This is a genuine equation-level use of the designated account02/B12 theorem. The conclusion holds uniformly over all six arbitrary signed unbounded eigenvalues in (5.2), every admissible small full-rank packet, and all unrestricted spectator curvature.

There is a much sharper direct D5 consequence because the final physical cross block itself has six singular values at least `g`: the completed D5 receiver used inside the partner proof gives

`||p_Q||inf <= 5sqrt(2e)/g = 10.01381557884...`.              (6.3)

That D5 branch has a continuous `C_0` density. I record (6.2) as the required designated-partner application and (6.3) as the sharper consequence for this explicit family.

## 7. Why this is new relative to the previous B12 mechanism

The previous low-rank spectral-resonance theorem protected a carrier by requiring a Woodbury nonresonance gap. The present identity resolves the opposite situation: even **at** the scalar resonance `1+theta q=0`, the added eigenvalue is harmless if its physical eigenvector action has a transverse component `a_perp`.

The exact determinant factor

`(1+theta q)^2+theta^2 r`

shows the dichotomy cleanly:

- longitudinal mode + exact resonance can cancel;
- transverse physical action repairs the cancellation automatically.

This changes mechanism from inverse/resolvent control to exterior-volume geometry.

## 8. Remaining full-target implication

This is supporting progress, not a proof of unrestricted QFORM.

The owner hypothesis `s_3(A)>=1` alone still does not force a bounded-size physical cross carrier with six repaired modes, and existing corrections rule out several naive universal-good-minor/cross-rank dichotomies. The next useful structural statement would be an **aggregate resonance-versus-transverse-volume dichotomy**:

> from three global large spectral directions, either produce enough original-coordinate cross-volume with a quantitative transverse-repair ratio, or route the failure into one of the already-paid diffuse-bank / grouped-hub / pair / Schur / half-Riesz mechanisms.

No pointwise oscillatory decay, arbitrary-joint coarea, post-rotation independence, or naive fiber-supremum estimate is used here.

## 9. Finite sanity check

A private finite check of 5,000 random full-column-rank matrices and random rank-one updates verified (2.1) to maximum relative discrepancy `3.84e-12`, with no sign violations. This is only a sanity check; the proof is the algebra above.

## 10. Source/control record

Fresh prepublication brain main: `2d599946833908744e03e005cc46016e2e3048e7`.  
Consumed corrections include the refutations of universal pointwise quadratic-phase decay, arbitrary-joint coarea, conditional positive-density moments, universal good-minor/cross-rank extraction, and dimension-free naive fiber-supremum reduction.  
Execution state: `WITHOUT_VERIFIED_BRAIN`.
