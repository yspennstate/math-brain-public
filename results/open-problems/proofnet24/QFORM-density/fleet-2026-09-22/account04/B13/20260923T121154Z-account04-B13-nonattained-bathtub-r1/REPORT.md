SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account04, slot B13, 2026-09-23T12:11:54Z.

# B13 report — nonattained bathtub purification and exterior-energy slab compiler

Status: PROVED SUPPORTING REDUCTION AND A PAID FULL-TARGET BRANCH. FULL QFORM OPEN. CONTINUITY NOT CLAIMED.

## 1. Setting

Let
[
mathcal F={fin L^1(mathbb R):0le fle1, int f=1}.
]
The target is a universal bound for the density of (Q=X^TAX), for arbitrary independent marginals in (mathcal F), whenever (A) has at least three eigenvalues of absolute value at least one.

The completed input used here is account01/B13 at commit
[
	exttt{3e41aa8d5fd7726113b90ed78e8b440bc9ec6a87}.
]
For every integer (mge5), put
[
D_m^perp(A)=
 sum_{substack{Rcap C=arnothing\|R|=|C|=m}}
 |det A[R,C]|^2.
]
The completed exterior-energy theorem gives, first for unit product indicators,
[
 |{xinprod_iE_i:x^TAxin J}|
 le C_m[D_m^perp(A)]^{-1/(2m)}|J|,
 qquad
 C_m=2sqrt{2e},rac m{m-4}.
	ag{1}
]

This report repairs the infinite-line bathtub issue without assuming that a threshold or maximizer exists, transfers (1) to every cap-one product law, and isolates the first remaining geometric branch.

## 2. Bathtub supremum without attainment

### Lemma 2.1

For every measurable (h:mathbb R	o[0,infty]),
[
 sup_{finmathcal F}int fh
 =
 sup_{substack{Esubsetmathbb R {m measurable}\|E|=1}}int_Eh.
	ag{2}
]
Neither supremum is asserted to be attained.

### Proof

The (ge) direction is immediate because (1_Einmathcal F).

For the reverse direction, fix (finmathcal F), truncate (h) by (h^{(M)}=min(h,M)), and approximate (h^{(M)}) from below by nonnegative simple functions (s_k) of bounded support. For one such
[
s=sum_{
u=1}^N a_
u1_{B_
u},
qquad a_1gecdotsge a_Nge0,
]
with disjoint finite-measure cells, the finite-dimensional linear program
[
maxleft{sum_
u a_
u u_
u:
0le u_
ule |B_
u|, sum_
u u_
ule1ight}
]
is solved by filling cells in decreasing order, using a measurable subset of the last cell if necessary. Any unused measure is filled outside the bounded support of (s). Hence there is a measurable set (E_s), (|E_s|=1), such that
[
int fsleint_{E_s}slesup_{|E|=1}int_Eh.
]
Monotone convergence first in (k), then in (M), gives
[
int fhlesup_{|E|=1}int_Eh.
]
This proves (2). The construction uses only approximate finite simple selectors, so it remains valid when the formal infinite-line threshold is not attained. (square)

## 3. Exact coordinatewise purification for positive kernels

### Theorem 3.1

Let (K:mathbb R^n	o[0,infty]) be measurable. Then
[
sup_{f_1,ldots,f_ninmathcal F}
int_{mathbb R^n}K(x)prod_{i=1}^nf_i(x_i),dx
=
sup_{substack{|E_i|=1\1le ile n}}
int_{prod_iE_i}K(x),dx.
	ag{3}
]
Again, no optimizer is claimed.

### Proof

For bounded (K), fix a product law and (arepsilon>0). With all variables except (x_1) integrated out, obtain a nonnegative measurable one-variable function (h_1). Lemma 2.1 supplies a set (E_1), (|E_1|=1), whose replacement loses at most (arepsilon/n). Repeat with the updated product in coordinates (2,ldots,n). The final product indicator loses at most (arepsilon). Taking suprema and then (arepsilondownarrow0) proves (3) for bounded kernels.

For general (K), apply the bounded result to (K_M=min(K,M)), then use monotone convergence. No independence of sums or differences is introduced: only the original product coordinates are purified one at a time. (square)

### Corollary 3.2

A uniform estimate for all unit product sets transfers with exactly the same constant to all independent cap-one laws, both for slab indicators
[
K(x)=1_{{x^TAxin J}}
]
and for any nonnegative fractional-potential kernel after truncation.

This is stronger than an appeal to an attained bathtub maximizer and complementary to account01/B13's finite (L^1)-mixture theorem.

## 4. Application to the completed exterior-energy estimate

Applying Theorem 3.1 to (1) gives, for arbitrary independent cap-one marginals,
[
oxed{
 Pr{X^TAXin J}
 le
 C_m[D_m^perp(A)]^{-1/(2m)}|J|,
 quad mge5.
}
	ag{4}
]
Thus whenever (D_m^perp(A)>0), the output law has an essentially bounded density satisfying
[
oxed{
 |p_Q|_infty
 le
 2sqrt{2e},rac m{m-4}
 [D_m^perp(A)]^{-1/(2m)}.
}
	ag{5}
]
For the first order,
[
D_5^perp(A)ge1
quadLongrightarrowquad
oxed{|p_Q|_inftyle10sqrt{2e}<23.317.}
	ag{6}
]
This is a concrete full-target branch: arbitrary dimension, signs, remaining spectrum, fragmented supports, unbounded tails, and dense same-side quadratic terms are allowed.

Conversely, a slab witness with ratio
[
ho=Pr{Qin J}/|J|
]
must obey
[
D_m^perp(A)le(C_m/ho)^{2m}.
	ag{7}
]
For every disjoint physical cross block (A[I,L]), Cauchy--Binet yields
[
s_m(A[I,L])^{2m}
le e_m(A[I,L]^TA[I,L])
le D_m^perp(A),
]
hence the actual high-ratio inequality
[
oxed{
s_m(A[I,L])le C_m/ho
quad(mge5).
}
	ag{8}
]
At (m=5), every disjoint cross block therefore has
[
s_5(A[I,L])le 10sqrt{2e}/ho.
	ag{9}
]

## 5. Remaining geometric slab problem

Equations (7)--(9) show that a counterexample sequence with (ho	oinfty) must make every fixed-order disjoint exterior energy collapse. The account01 max-volume compiler sharpens this to
[
A=D+R+E,qquad operatorname{rank}Rle28,
qquad |E|_{max}le32sqrt{2e}/ho,
	ag{10}
]
outside at most fourteen physical coordinates.

The unresolved implication is not probabilistic purification. It is the geometric slab estimate for (10). Entrywise small (E) cannot simply be deleted: arbitrary translations and fragmented unbounded unit sets can magnify a small quadratic coefficient, while (|E|_{m op}) may grow with dimension.

A valid next theorem must either:

1. prove a dimension-free slab bound for diagonal plus rank-28 plus the structured residual in (10); or
2. show that (s_3(A)ge1) forces a paid square, pair, bordered, or exterior-volume certificate before all (D_m^perp(A)) collapse.

## 6. Integrity

Essential boundedness follows from the interval inequality by domination of Borel sets. Continuity is separate and is not claimed. No threshold attainment, interval extremality, support bound, moment assumption, Gaussian assumption, or independence after rotation is used.
