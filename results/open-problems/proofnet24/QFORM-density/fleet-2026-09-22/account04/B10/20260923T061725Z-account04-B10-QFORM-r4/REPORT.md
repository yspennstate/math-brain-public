SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 04, slot B10, 2026-09-23T06:17:25Z.
attacking: the exact-rank-three positive-regression near-null collar by a three-way original-coordinate curvature split, followed by the mixed-Fresnel receiver on the non-near-null subbranch.

# account04/B10 — three-bank regression/curvature split

Programme: `QFORM-DENSITY-3EIG-20260922`  
Status: `ESSENTIAL_STEP_APPLIED / NEW_PRODUCT-PRESERVING_IDENTITY / QUANTITATIVE_SUBBRANCH_CLOSED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The full conjecture remains open. This report proves a new three-colour product-preserving split for the positive regression-residual bank and applies account01/B10's completed mixed-Fresnel theorem to an actual target inequality. No post-rotation independence, moment, support, conditional-density supremum, or small-random-perturbation assumption is used. Continuity is proved only in the mixed-Fresnel subbranch below.

## 1. Source boundary


The newest completed account01/B10 source actually used is

`yspennstate/math-open-problems@6e2925e1a210871b4cfe53f5731578d0a71cb6d4`

`proofnet24/QFORM-density/fleet-2026-09-22/account01/B10/20260923T035230Z-account01-B10-QFORM-r25/REPORT.md`.

Its regression notation is retained. For one original-coordinate light bank,
[
r_i=t_i u+p_i,qquad p_iin u^perp,qquad
G=sum_i p_ip_i^T>0,
]
put
[
w=G^{-1}sum_i t_ip_i,qquad e_i=t_i-wcdot p_i,qquad
ho=sum_i e_i^2.
]
Then (sum_i e_ip_i=0), and the full bank Gram has determinant (hodet G).
Writing
[
a_i=e_i/sqrtho,qquad q_i=G^{-1/2}p_i,qquad
alpha_i=a_i^2,quadeta_i=|q_i|^2,
]
the rows ((a_i,q_i)) form a Parseval frame in (mathbb R^3).
Account01/B10 proved
[
sum_i e_i^2det(G-p_ip_i^T)
=hodet GBigl(1-sum_ialpha_ieta_iBigr)
ge rac13hodet G. 	ag{1.1}
]

I also use account01/B10's mixed source Fresnel theorem from

`yspennstate/math-open-problems@d28d8311f1c84a56c4c74727847322e9a79b8932`.

In the heavy-null two-bank state it gives
[
|p_Q|_infty
le 3,2^{5/6}D^{-1/3}c^{-1/6}
       [det S_Jdet S_K,	au_*]^{-1/6}, 	ag{1.2}
]
where (D=|det M|), (c) is the heavy leverage, and
(	au_*=max(	au_J,	au_K)). The proof remains in original product
coordinates and yields a continuous density.

## 2. Three-colour mixed-volume theorem

For positive semidefinite (2	imes2) matrices define
[
mathcal M(H,K)=operatorname{tr}(operatorname{adj}H,K).
]
If (H=sum_{jin Y}p_jp_j^T) and
(K=sum_{kin Z}p_kp_k^T), then the two-dimensional
Cauchy--Binet identity gives
[
mathcal M(H,K)=sum_{jin Y}sum_{kin Z}det(p_j,p_k)^2. 	ag{2.1}
]

### Theorem 2.1 — `QFORM-REGRESSION-THREEBANK-CURVATURE-SPLIT-v1`

There is a partition of the ORIGINAL bank indices
[
B=Ssqcup Ysqcup Z
]
such that, with
[
ho_S=sum_{iin S}e_i^2,quad
G_Y=sum_{jin Y}p_jp_j^T,quad
G_Z=sum_{kin Z}p_kp_k^T,
]
one has
[
oxed{ho_S,mathcal M(G_Y,G_Z)
ge rac{2}{81}hodet G.} 	ag{2.2}
]

Consequently the residual scalar supported on (S), the (Y)-bank
transverse vector, and the (Z)-bank transverse vector are three
mutually independent original-product sources.

#### Proof

Colour each original coordinate independently and uniformly by
(S,Y,Z). Expanding (2.1) and using that a nonzero determinant requires
distinct (j,k),
[
mathbb E[ho_Smathcal M(G_Y,G_Z)]
=rac{2}{27}sum_i e_i^2
  sum_{substack{j<k\j,k
e i}}det(p_j,p_k)^2. 	ag{2.3}
]
Indeed, (i) receives colour (S) with probability (1/3), while the
unordered pair ({j,k}) receives the two different colours (Y,Z)
in either order with probability (2/9).

The inner sum is precisely (det(G-p_ip_i^T)). Therefore (1.1)
inserted in (2.3) gives
[
mathbb E[ho_Smathcal M(G_Y,G_Z)]
ge rac{2}{27}rac13hodet G
=rac{2}{81}hodet G.
]
Some deterministic colouring attains at least its expectation. QED.

If (Ggekappa_0I_2), (kappa_0=7/800), then
[
oxed{ho_Smathcal M(G_Y,G_Z)
ge rac{49}{25920000}ho.} 	ag{2.4}
]

This strengthens the preceding two-bank split: it supplies three
genuinely independent source groups, the exact source count needed by
a conditional-slope/square or mixed-Fresnel receiver. It does not by
itself remove the same-bank longitudinal and transverse contamination,
so it is not claimed as a full density theorem.

## 3. Actual mixed-Fresnel payment away from the puncture

Return to account01/B10's heavy-null two-bank state, where
[
Dgerac12,qquad cgerac79,qquad
det S_Jdet S_Kgerac1{640}. 	ag{3.1}
]
If either positive regression defect satisfies
[
	au_*=max(	au_J,	au_K)gerac1{100}, 	ag{3.2}
]
then (1.2) gives
[
egin{aligned}
|p_Q|_infty
&le 3,2^{5/6}2^{1/3}(9/7)^{1/6}(64000)^{1/6}\
&<44.417. 	ag{3.3}
end{aligned}
]
Thus this entire non-near-null exact-rank-three hybrid subbranch has a
continuous density with the explicit universal cap (44.417).

For signature ((2,1)), the previously completed ruled-side theorem
also gives the orientation-free one-sheet estimate
[
operatorname*{ess,sup}_{sge0}p_Q(s)lepisqrt2, 	ag{3.4}
]
with signs reversed for signature ((1,2)). Equation (3.4) is used
only on its stated one-sheet side; it is not a full-density estimate.
Equation (3.3), not (3.4), pays both sides when (3.2) holds.

## 4. Exact remaining implication

After (3.3), account01/B10's exact-graph endpoint, and the earlier
leverage-one deletion branch, the live exact-rank-three obstruction is
confined to
[
0<	au_J,	au_K<rac1{100}, 	ag{4.1}
]
on the convex/two-sheet side, with neither a usable exact-graph
deletion nor a pure independent curvature bank.

Theorem 2.1 now supplies in each positive-defect bank a three-source
certificate of size (2hodet G/81). What is not yet proved is a
receiver that absorbs the remaining same-bank contamination without a
fiber supremum. The first unpaid statement is therefore:

`QFORM-THREEBANK-MIXED-CURVATURE-RECEIVER-v1`: convert (2.2) into a
uniform density bound while retaining all longitudinal/transverse
terms carried by the same original banks.

The arbitrary exact-rank-three theorem remains OPEN. Additional
spectrum remains a separate interaction problem. No counterexample to
the full conjecture is produced here.
