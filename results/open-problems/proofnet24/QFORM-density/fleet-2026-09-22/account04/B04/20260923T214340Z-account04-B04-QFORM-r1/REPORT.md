{
  "login": {
    "account": "account04",
    "slot": "B04",
    "signed_in_at": "2026-09-23T21:43:40Z",
    "canonical_login": "account04/B04",
    "statement": "SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B04, 2026-09-23T21:43:40Z."
  }
}

# account04/B04 r1 — marginal-free third-compound payment of the nested double anchor

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T214340Z-account04-B04-QFORM-r1`  
Status: `ESSENTIAL_STEP_APPLIED / LIVE BRANCH PAID / FULL TARGET OPEN`.

The full unrestricted conjecture remains OPEN. This report closes the nested anchored-third-volume outcome in the current rank-five/double-anchor proof graph. It does not close the heavy-carrier branch, the shear-flat exact-rank-three hybrid, the convex/two-sheet collar, or the remaining extra-spectrum glue.

No random variable is rotated. No moment, support, smoothness, conditional-density, arbitrary-joint coarea, small-tail deletion, or pointwise scalar quadratic-phase assumption is used.

## 1. Sources and exact scope

The live structural input is `QFORM-ANCHORED-D3-EXTERIOR-COMPRESSION-v1`,
`math-open-problems@95d5c3b6e8a753f5da44f742f8449d51470f4a11`.
It consumes account01/B20’s rank-five carrier theorem and gives a literal original-coordinate cross block
[
M=A[I,J]
]
with a physical row (i), physical column (j), residual banks, and separated anchored mass
[
mathcal J_3^{m sep}(i,j)
=sum_{substack{r_1in I_1,r_2in I_2\\
                 c_1in J_1,c_2in J_2}}
 det M[{i,r_1,r_2},{j,c_1,c_2}]^2
>delta,
]
where
[
delta=rac{47045881}{12cdot10^{18}}
=3.920490083333333ldots	imes10^{-12}.                 	ag{1.1}
]

The completed account01/B04 theorem applied below is
`QFORM-THIRDCOMPOUND-CROSS-PROMOTION-v1`,
`math-open-problems@c2ce876df8b5483a00802170001d4144bb4cdbfa`.
For any literal original-coordinate cross block (B), it proves, with no row-marginal hypothesis,
[
|p_Q|_inftyle6^{4/3}E_3(B)^{-1/6},qquad
E_3(B)=sum_{|R|=|T|=3}det B[R,T]^2,                    	ag{1.2}
]
and gives a continuous (C_0) density while retaining arbitrary same-bank terms.

The newer account01/B04 r19 source
`05f3b074cd84ad6f9dae4dab93e2fb84d83c39de`
was also checked. Its scalar-pivot/Schur-(E_2) theorem is not silently applied here: the two anchor indices (iin I), (jin J) are generally distinct, so the cross coefficient (M_{ij}) is not a physical diagonal pivot. The third-compound theorem is the exact matched source.

Controls were refreshed at
`math-research-brain@e31e523430a429316ab599478efa12580bdc7c44`.

## 2. Main theorem

### Theorem — `QFORM-NESTED-ANCHOR-D3-MARGINALFREE-PAYMENT-v1`

In the live nested double-anchor outcome above, for every independent cap-one product input,
[
oxed{ |p_{X^	op AX}|_infty<868.251. }                    	ag{2.1}
]
The output has a continuous representative vanishing at infinity.

### Proof

Every determinant in (mathcal J_3^{m sep}(i,j)) is one of the physical (3	imes3) minors in the full third compound of the SAME cross block (M). All summands are nonnegative. Therefore
[
E_3(M)
=sum_{substack{Rsubset I, Tsubset J\\|R|=|T|=3}}
 det M[R,T]^2
ge mathcal J_3^{m sep}(i,j)
>delta.                                                       	ag{2.2}
]

Condition on every original coordinate outside (Icup J). The remaining coordinates in (I) and (J) are still independent with their original density caps. The conditioned outside couplings become affine terms inside the two banks, while (A[I,I]) and (A[J,J]) remain arbitrary same-bank quadratic phases. These are exactly permitted by the account01/B04 theorem.

Apply (1.2) to (B=M) and use (2.2):
[
|p_{Qmid X_{(Icup J)^c}}|_infty
<6^{4/3}delta^{-1/6}
=868.2502970517490ldots.                                      	ag{2.3}
]
The bound is uniform in the outside conditioning, so averaging proves (2.1). The conditional characteristic-function estimates have the same integrable envelope; equivalently, uniform boundedness plus dominated convergence for the conditional (C_0) densities gives a continuous (C_0) unconditional density. QED.

This is an actual equation-level use of account01/B04 mathematics on the live survivor, not a status citation.

## 3. Optimized volume weights and same-matrix comparison

For this (M), use the canonical third-volume law
[

u(R,T)=rac{det M[R,T]^2}{E_3(M)}.                           	ag{3.1}
]
This is the admissible volume-sampling weight whose determinant/entropy currency is exactly (E_3(M)). If a row marginal exceeds (1/2), the account01 promotion algorithm moves that original scalar coordinate into the physical hub and preserves the exact recursion
[
S_+^2Z_{ell-1}^+=alpha_hS^2Z_ell.                            	ag{3.2}
]
Thus no marginal gate or endpoint factor is dropped: the worst-case promoted constant is already the (6^{4/3}) in (1.2).

On the SAME (M):

- **Marginal-free (D')/third compound:** (2.2) forces (E_3(M)>delta), hence the payment (2.3).
- **(D_5):** no positive fifth exterior volume follows from the anchored mass. The live packet was reached only after the earlier fifth-volume exit was exhausted; (M) may have rank three or four, in which case (E_5(M)=0).
- **Ridge:** (E_3(M)>delta) does not force three well-scaled singular values or the ridge-leverage gate. It controls the product aggregate, not an individual (s_3(M)).

The separation is genuine. For
[
M_R=operatorname{diag}!left(R,R,rac{sqrtdelta}{R^2}ight),
qquad Rge1,                                                    	ag{3.3}
]
one has
[
E_3(M_R)=delta,qquad E_5(M_R)=0.                              	ag{3.4}
]
At any ridge scale (gamma>0), write
[
k_ell=rac{s_ell(M_R)^2}{gamma^2+s_ell(M_R)^2}.
]
The ridge criterion would require some (qge1) with
[
max_ell k_ellle q/2,qquad sum_{ell=1}^3k_ell>2q.         	ag{3.5}
]
The first inequality gives (qge2max k_ell), whereas
[
sum_{ell=1}^3k_ellle3max k_ell<4max k_ellle2q,          	ag{3.6}
]
a contradiction. Hence ridge fails at every scale and (D_5) vanishes, while the canonical third-compound theorem still gives
[
|p_Q|_inftyle6^{4/3}delta^{-1/6}.                          	ag{3.7}
]
This example is only a certificate comparison; the live payment itself is (2.2)-(2.3).

## 4. Proof-graph consequence

Account01/B20’s rank-five carrier theorem had three outcomes:

1. carrier leverage (>1/25);
2. direct density payment (<1353);
3. the nested anchored-third-volume packet.

Outcome 3 is now paid by (<868.251), which is even smaller than the existing outcome-2 constant. Therefore the entire non-heavy-carrier part of that theorem is bounded by
[
oxed{ |p_Q|_infty<1353. }                                	ag{4.1}
]

The next uncovered implication is strictly narrower:
`QFORM-RANKFIVE-HEAVY-CARRIER-COMPILER-v1`.
It must pay the branch where the rank-five carrier projection has a physical leverage (>1/25), or route it product-preservingly to a physical pivot/star receiver. The shear-flat exact-rank-three hybrid, convex/two-sheet collar, and arbitrary additional-spectrum assembly also remain open.

The full universal theorem and a counterexample are not claimed.
