# fleet01/B17 r11 — complete multiplicity-eight, constant-400 replacement proof

Run: `20260924T201439Z-fleet01-B17-auto11`  
Status: **NEW COMPLETE MATHEMATICAL CANDIDATE / B17 PASS; unrestricted multiplicity 3 remains OPEN.**

## Theorem QFORM-FIXED-MULTIPLICITY-8-400-B17-v1

Let (X=(X_1,ldots,X_n)) have independent real coordinates with probability densities bounded by (K). Let (A=A^T), (binmathbb R^n), (cinmathbb R), and suppose
[
s_8(A)ge s>0.
]
Then (Q=X^TAX+b^TX+c) has an essentially bounded density and
[
oxed{|p_Q|_inftyle 400,K^2/s.}
]
No moment, support, smoothness, Gaussianity, log-concavity, exact-rank, diagonal-basis or leverage assumption is imposed. Global continuity is not claimed.

This improves the separately reconstructed multiplicity-eight bound 6010 in
`improvements/fleet01/B13/20260924T152809Z-fleet01-B13-FIXMULT-auto11/EIGHT_EIGENVALUE_REPLACEMENT.md`
(blob `8f792f8f80d70fd1eda26dfdabd855b9a6235e29`) by combining its robust two-anchor collar with the sharper pivot thresholds and constant-400 analytic package in the source-pinned nine paper.

## 1. Normalize and inherit the paid pivot branches

Scale to (K=s=1). Use exactly the nine-paper parameters
[
d=3/40,qquad p=1/400,qquad h=2/25,qquad kappa=h^2=4/625.
]
A physical pivot is either (|A_{ii}|ge d) or a principal two-coordinate determinant of modulus at least (p).

The nine-paper pivot proofs require less spectral multiplicity than eight:

- scalar pivot: its Schur complement retains at least seven unit-scale eigenvalue moduli; Proposition 7.3 there needs only five. The three scalar branches are (<280,<320,<383);
- definite pair: (<80);
- indefinite pair: the Schur complement retains at least six unit-scale directions; the logarithmic receiver needs only one. Its bound is (<392.5).

Thus every pivot state already obeys (|p_Q|_infty<400) under (s_8(A)ge1).

Hence assume no pivot. Then
[
|A_{ii}|<3/40,qquad |A_{ij}|<1/11quad(i
e j).
	ag{1.1}
]

## 2. The ordinary third volume either pays immediately or is small

Let (V_r) be the ordered disjoint minor volume from the nine paper. Since (s_8ge1) implies (s_5ge1), its audited order-two spectral-to-volume proposition gives
[
V_2gekappa^2.
	ag{2.1}
]

If (V_3gekappa^3), a fair physical coordinate cut has
[
Z_3ge kappa^3/64.
]
The marginal-free order-three receiver gives
[
|p_Q|_inftyle C_3 Z_3^{-1/6}
le25C_3<375.
	ag{2.2}
]

It remains to treat
[
V_3<kappa^3,qquad V_3/V_2<kappa.
	ag{2.3}
]

## 3. A good two-seed forces two robust physical anchors

Sample every invertible disjoint two-seed (B=A[S,T]) with probability
(det(B)^2/V_2), and use the audited completion
[
A=D+R+E,
]
where (D) is diagonal and zero on (Scup T), (E) is zero-diagonal,
[
operatorname{rank}Rle6,qquad operatorname{rank}R[L,L]le2,
]
and
[
mathbb E|E|_F^2le9V_3/V_2<9kappa.
	ag{3.1}
]

Call a seed good when
[
|E|_F^2le18kappa.
]
By Markov and the strict inequality in (3.1), good seeds carry more than half of (V_2).

For a good seed put
[
arepsilon=|E|_Flesqrt{18kappa}=rac{6sqrt2}{25}<rac{17}{50}.
	ag{3.2}
]
Since (s_8(A)ge1),
[
s_8(D+R)=s_8(A-E)ge1-arepsilon.
]
Because (operatorname{rank}Rle6),
[
s_2(D)ge1-arepsilon.
]
Thus two coordinates (H={h_1,h_2}subset L) satisfy
[
|D_{hh}|ge1-arepsilon.
	ag{3.3}
]

Write (P=A_{cdot,T}B^{-1}A_{S,cdot}), so (R[L,L]=P[L,L]).
For (hin H), (1.1) and (3.2) give
[
|P_{hh}|ge1-arepsilon-d>rac{117}{200},
]
while for distinct (h,h'in H),
[
|P_{hh'}|le |A_{hh'}|+|E_{hh'}|
<rac1{11}+rac{17}{50}=rac{237}{550}.
]
Therefore
[
|det P[H,H]|
>
left(rac{117}{200}ight)^2-
left(rac{237}{550}ight)^2
=rac{151533}{968000}
>rac3{20}.
	ag{3.4}
]
The exact interpolation identity
[
P[H,H]=A[H,T],B^{-1}A[S,H]
]
now yields
[
oxed{
|det A[S,H],det A[H,T]|
>rac3{20},|det B|.
}
	ag{3.5}
]

## 4. Aggregate collar mass extracts one robust literal two-anchor block

For every two-set (H), define
[
D_H=sum_{substack{Usubset H^c\|U|=2}}det A[H,U]^2.
	ag{4.1}
]
By definition of ordered (V_2),
[
sum_H D_H=V_2.
	ag{4.2}
]

Assign each good seed one pair (H) supplied by Section 3 and let (w_H) be the sum of (det(B)^2) over good seeds assigned to (H). Since good mass is (>V_2/2), some (H_*) satisfies
[
w_{H_*}>D_{H_*}/2.
	ag{4.3}
]
Squaring (3.5), summing over seeds assigned to (H_*), and then dropping disjointness in a nonnegative double sum gives
[
rac9{400}w_{H_*}
<
sum_{m assigned}
det A[S,H_*]^2det A[H_*,T]^2
le D_{H_*}^2.
]
Together with (4.3),
[
oxed{
g:=D_{H_*}>rac9{800}.
}
	ag{4.4}
]

Let (H=H_*), (L=H^c), and (C=A[H,L]). Cauchy–Binet gives
[
g=det(CC^T).
	ag{4.5}
]

## 5. Exact leave-one-column identity and leverage split

Put
[
Q_C=C^T(CC^T)^{-1}C,qquad P=I-Q_C,
]
and
[
q_i=(Q_C)_{ii},qquad p_i=1-q_i.
]
Since (Q_C) has rank two,
[
sum_iq_i=2.
	ag{5.1}
]

Write (A) in the block form
[
A=egin{pmatrix}B&C\C^T&Dend{pmatrix}
]
and let (d_i) be row (i) of the (L	imes L) block (D). Put (r_i=d_iP). Define
[
W_i=
sum_{substack{Tsubset Lsetminus{i}\|T|=3}}
det A[Hcup{i},T]^2,
qquad W_{m dis}=sum_iW_i.
	ag{5.2}
]
The leave-one-column Cauchy–Binet identity is
[
oxed{
W_i=gleft(p_i|r_i|_2^2-r_{ii}^2ight).
}
	ag{5.3}
]
Proof: the total sum of squared (3	imes3) minors of the three rows
((C;d_i)) is (g|r_i|^2). The leverage of column (i) in their row
space is (q_i+r_{ii}^2/|r_i|^2); deleting all minors using column (i)
therefore leaves (5.3). The zero-residual case follows by continuity/direct
inspection.

Set
[
J={i:q_i>2/3},qquad U=Lsetminus J.
]
For (iin U), (p_ige1/3), define
[
lambda_i=r_{ii}/p_i,qquad
e_i^TE=(d_i-lambda_i e_i^T)P.
]
For (iin J), put (lambda_i=0) and the row of (E) equal to zero.
Then (E_{ii}=0), and (5.3) gives
[
oxed{
|E|_F^2lerac3g,W_{m dis}.
}
	ag{5.4}
]

## 6. There are at most one high-leverage coordinate

For every pair ({a,b}subset L), put
[
w_{ab}=det(C_{{a,b}})^2/g.
]
Cauchy–Binet gives (sum_{a<b}w_{ab}=1), and the determinantal
one-point marginals are
[
q_i=sum_{b
e i}w_{ib}.
	ag{6.1}
]
If distinct (i,j) both had (q_i,q_j>2/3), then
[
w_{ij}ge q_i+q_j-1>1/3
]
and hence
[
det(C_{{i,j}})^2>g/3>rac3{800}.
	ag{6.2}
]
But all four entries of this literal (2	imes2) cross minor are
off-diagonal entries of (A), so (1.1) gives
[
|det C_{{i,j}}|<2/121,qquad
det(C_{{i,j}})^2<4/14641<3/800,
]
a contradiction. Therefore
[
|J|le1.
	ag{6.3}
]

## 7. A dimension-free disjoint incident third volume is forced

Assume for contradiction
[
W_{m dis}le g/50.
	ag{7.1}
]
Then by (5.4),
[
|E|_F^2le3/50,qquad
|E|le|E|_F<49/200,
	ag{7.2}
]
where (3/50<(49/200)^2).

Let (D_0) be diagonal with entries (lambda_i) on (U) and zero on
(Hcup J), and set
[
R=A-D_0-(0_Hoplus E).
]
Every row outside (J) lies in the direct sum of the two physical
(H)-coordinate directions and the two-dimensional row space of (C).
Each row in (J) contributes at most one additional row direction. Hence
[
operatorname{rank}Rle4+|J|le5.
	ag{7.3}
]
Moreover, after restriction to (U	imes U), every row lies in the
restricted row space of (C), so
[
operatorname{rank}R[U,U]le2.
	ag{7.4}
]

By (7.2) and (s_8(A)ge1),
[
s_8(D_0+R)ge3/4.
]
Using (7.3), (s_{4-|J|}(D_0)ge3/4). Since (|J|le1), at least three
coordinates (Isubset U) satisfy (|lambda_i|ge3/4).

For (iin I),
[
|R_{ii}|ge 3/4-d=27/40.
]
For distinct (i,jin I),
[
|R_{ij}|<1/11+49/200=739/2200.
]
Thus each row of (R[I,I]) has off-diagonal absolute sum less than
[
2cdot739/2200=739/1100<27/40
]
(the exact margin is (7/2200)). Strict diagonal dominance makes
(R[I,I]) invertible, contradicting (7.4). Hence
[
oxed{
W_{m dis}>g/50>rac9{40000}.
}
	ag{7.5}
]

## 8. Pay the disjoint incident volume by the audited grouped compiler

Randomly partition (L=Isqcup J'). Each packet counted by (W_{m dis})
contains four distinct coordinates (one distinguished row coordinate and
three column coordinates), so with probability (1/16) it lands with the
row in (I) and all three columns in (J'). Therefore some cut has
[
W(I,J')ge W_{m dis}/16.
	ag{8.1}
]

Retain the two literal coordinates in (H) as hubs. Let (S^2) be the
two-row Gram determinant of their crossing block to (J'); project each
residual (I)-row orthogonally off those two hub rows and let
(Z=sum_i|c_i|^2). Cauchy–Binet gives exactly
[
W(I,J')=S^2Z.
	ag{8.2}
]

If all residual row marginals are at most (1/2), the audited grouped
lemma with (k=2,ell=1) gives
[
|phi_Q(t)|
le
min{1,pi^{3/2}2^{1/4}e,W(I,J')^{-1/4}|t|^{-3/2}},
]
hence
[
|p_Q|_infty
le3,2^{1/6}e^{2/3}W(I,J')^{-1/6}.
	ag{8.3}
]
If one residual row has marginal (>1/2), retain that literal original
coordinate as a third hub. The terminal three-hub lemma has Gram determinant
(>W(I,J')/2), and gives a smaller coefficient than the right side of
(8.3) after the factor (2^{1/6}).

Combining both branches with (8.1),
[
oxed{
|p_Q|_infty
le
3,2^{5/6}e^{2/3}W_{m dis}^{-1/6}.
}
	ag{8.4}
]
Using (7.5), (e<3), (2^{5/6}<2), and
((40000/9)^{1/6}<5), we obtain the deliberately loose but explicit bound
[
oxed{|p_Q|_infty<90}
	ag{8.5}
]
in the terminal no-pivot branch.

## 9. Assemble the theorem

Every normalized (s_8(A)ge1) state is in one of the following branches:

1. scalar pivot: (<383);
2. definite pair pivot: (<80);
3. indefinite pair pivot: (<392.5);
4. no pivot and (V_3gekappa^3): (<375);
5. no pivot and (V_3<kappa^3): (<90).

Therefore
[
|p_Q|_infty<400.
]
For general (K,s), put (Y=KX) and apply the normalized theorem to
(A/s). Since
[
Q=(s/K^2)widetilde Q,
]
density scaling gives
[
oxed{|p_Q|_inftyle400K^2/s.}
]

All conditioning and hub promotion is in original independent coordinates.
The projections (P,Q_C) above are deterministic coefficient-space algebra
only. No post-rotation independence is invoked. Essential boundedness is
proved; global continuity is not asserted.

## 10. Independent audit status and remaining threshold

I independently re-derived every step above, including the two-anchor
extraction, leave-one-column identity, high-leverage exclusion and rank
contradiction. It is compatible with all currently recorded QFORM correction
events read in this run.

The B13 report (blob
`8f792f8f80d70fd1eda26dfdabd855b9a6235e29`) is a genuinely separate
complete reconstruction of the multiplicity-eight mechanism, with different
pivot thresholds and constant 6010. This B17 proof supplies a second
end-to-end reconstruction of the structural chain and sharpens the final
constant. Whether that satisfies the owner's release gate should be recorded
only after the immutable write/readback and any designated reconciliation;
it is not formal proof-assistant verification or journal peer review.

Multiplicity seven remains open in this route. At (s_7), the rank-six
two-seed completion forces only one large completed diagonal coordinate, so
the two-anchor conversion above fails. The remaining object is a genuine
one-shared-coordinate overlap packet; the audited grouped (q=3) compiler
cannot be applied by pretending that shared coordinate occurs in two
independent banks.
