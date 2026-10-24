SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B13, 2026-09-23T20:16:53Z.
attacking: optimizer-free transfer from arbitrary cap-one product laws to geometric slab witnesses, followed by a quantitative diffuse rank-two slab dichotomy.

# B13 — optimizer-free slab transfer and diffuse rank-two geometric dichotomy

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T201653Z-account04-B13-extremal-slab-dichotomy-r1`  
Status: **PROVED SUPPORTING TARGET-LEVEL LEMMAS / FULL QFORM OPEN / CONTINUITY SEPARATE**

## 1. Sources and scope

Brain controls were refreshed through `yspennstate/math-research-brain@ed014f9bc0fd9de0d17566dde501ac8c934ce257`. The required Claude package and live corrections were retained. In particular, no interval extremality, optimizer attainment on the infinite line, bounded support, moment hypothesis, or independence after rotation is used.

The completed account01/B13 input actually used is
`yspennstate/math-open-problems@6ee8e95ab3f01ae94ff48a163d253a2eb82cd967`.
For
[
A=D+ULambda U^T,qquad U^TU=I_2,
]
write (u_i^T) for the rows of (U), (c_i=|u_i|_2^2), (d_i=D_{ii}), and (a_i=A_{ii}). If (max_i c_ile1/3), then every index (k) with (d_k a_k
e0) satisfies
[
|p_{X^TAX}|_infty
le4sqrt{2e}igl((1-c_k)|a_kd_kdetLambda|igr)^{-1/4}. 	ag{1.1}
]
This theorem is already valid for arbitrary cap-one product laws and keeps the diagonal and affine terms inside the estimate.

## 2. Bathtub supremum without an attained threshold

Let (g:mathbb R	o[0,infty]) be measurable. Then
[
sup_{substack{0le fle1\ int f=1}}int gf
=
sup_{|E|=1}int_E g. 	ag{2.1}
]

No maximizer and no threshold level are asserted.

For bounded (g), let (g^*) be the decreasing rearrangement. Hardy--Littlewood gives
[
int gfleint_0^1g^*(s),ds
]
for every admissible (f). Conversely, by the definition of rearrangement, for every (arepsilon>0) there is a measurable (E_arepsilon), (|E_arepsilon|=1), with
[
int_{E_arepsilon}ggeint_0^1g^*(s),ds-arepsilon.
]
This remains valid when a quantile level is not attained; one takes all of a strict superlevel set and an appropriate measurable part of a level set, or an approximating sequence if the relevant level lies at infinity. Applying this to (gwedge m) and using monotone convergence proves (2.1) for general nonnegative (g).

Successively applying (2.1) to the coordinates of a nonnegative measurable kernel (K) yields the exact optimizer-free product identity
[
sup_{substack{0le f_ile1\int f_i=1}}
int_{mathbb R^n}K(x)prod_i f_i(x_i),dx
=
sup_{substack{|E_i|=1}}
int_{prod_iE_i}K(x),dx. 	ag{2.2}
]
Only suprema are interchanged; no simultaneous optimizer is required.

For the slab kernel (K=1_{{x^TAxin J}}), every product-set witness can be approximated by bounded finite unions (F_i) of intervals, still with (|F_i|=1), and
[
left|int Kprod_i1_{E_i}-int Kprod_i1_{F_i}ight|
lesum_i|E_i	riangle F_i|. 	ag{2.3}
]
Hence a strict slab ratio (ho) transfers with arbitrary prescribed loss to bounded finite-union product sets. There is no uniform diameter or fragment-count conclusion.

## 3. Actual geometric slab inequality

Assume (s_3(A)ge1), (A=D+ULambda U^T), (operatorname{rank}(ULambda U^T)=2), and (max_i c_ile1/3). Since the rank-two part cannot cover the third singular direction,
[
1le s_3(A)le|D|_{m op}=max_i|d_i|. 	ag{3.1}
]
Choose (k) with (|d_k|ge1). If an interval (J) has
[
ho=rac{mathbb P{X^TAXin J}}{|J|},
]
then (1.1), (1-c_kge2/3), and (|d_k|ge1) give
[
oxed{|A_{kk}detLambda|le1536e^2,ho^{-4}.} 	ag{3.2}
]
Numerically, (1536e^2=11349.590167957478).

Equation (3.2) applies directly to every arbitrary cap-one product law. Equivalently, by (2.2), it is a geometric slab bound on every arbitrary measurable unit product set, and by (2.3) it suffices to test bounded finite-union witnesses without assuming a maximizer.

## 4. New pivot-or-rank-one dichotomy

Set
[
H=sqrt{1536e^2}=106.53445530886934.
]
From (3.2), at least one of the following holds:
[
oxed{|A_{kk}|le Hho^{-2}} 	ag{4.1}
]
or
[
oxed{|detLambda|le Hho^{-2}.} 	ag{4.2}
]
In the second case, if (lambda_1,lambda_2) are the eigenvalues of the symmetric (2	imes2) matrix (Lambda), then
[
min(|lambda_1|,|lambda_2|)
le|lambda_1lambda_2|^{1/2}
le H^{1/2}ho^{-1}.
]
Since (U) is an isometry on coefficient space,
[
oxed{operatorname{dist}_{m op}(ULambda U^T,{	ext{symmetric rank}le1})
le10.321552950446426,ho^{-1}.} 	ag{4.3}
]

Thus every high-ratio diffuse exact rank-two endpoint has a concrete deterministic alternative:

1. a genuine original-coordinate pivot (A_{kk}) is (O(ho^{-2})), despite (|d_k|ge1), so the obstruction is a near-exact physical cancellation; or
2. the rank-two carrier is (O(ho^{-1})) in operator norm from rank one.

The residual in (4.3) is not discarded as a random quadratic error; it is only a coefficient-space certificate for the next product-preserving argument.

## 5. Remaining gap

The full conjecture remains open. The next geometric slab step is now sharply localized:

- treat the near-null physical-pivot branch (4.1) using the existing affine-stable/null-pivot receiver without assuming the pivot contribution is a small random variable; and
- treat the near-rank-one branch (4.3) while retaining the (O(ho^{-1})) second mode inside the product estimate.

The heavy-carrier case (max_i c_i>1/3) is separately localized to at most five original-coordinate hubs because (sum_i c_i=2). No counterexample is produced.
