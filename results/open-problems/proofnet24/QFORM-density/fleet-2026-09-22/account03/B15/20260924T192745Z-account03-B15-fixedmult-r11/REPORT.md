SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account03, slot B15, 2026-09-24T19:27:45Z.
attacking: B15 regularity audit plus an exact retuning of the independently reviewed multiplicity-eight mechanism.

# account03/B15 — candidate s8 bound <291 and same-height C0 closure

Programme: `QFORM-DENSITY-3EIG-20260922`  
Objective: `QFORM-FIXED-MULTIPLICITY-AUDIT-20260924`  
Run: `20260924T192745Z-account03-B15-fixedmult-r11`  
Execution: `WITHOUT_VERIFIED_BRAIN`.

## 1. Scope and source pins

Fresh owner control was read from `yspennstate/math-research-brain@20b732a648b4cc8e441b27a6f592c037ac050cdd`; OWNER CONTROL revision is `2026-09-24.1`. The sole research target remains QFORM.

Pinned analytic baseline:
- `yspennstate/math-open-problems@eeb752c8943536541b34b42b8bf48e924f4d3d2f`
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/interactive/20260924T145418Z-nine-400/paper.tex`
- git blob `19fb119877426b640b2c0dae19ec2f78a399fe11`.

The separately written nine-eigenvalue reconstruction at
`proofnet24/QFORM-density/nine-eigenvalues-paper-2026-09-24/paper.tex`
was also compared on the B15 analytic interfaces (Fourier normalization, Gaussian inversion, Riesz half-potential, pair half-potential, and final density/interval interpretation). No disagreement was found on those interfaces.

The multiplicity-eight structural chain and its exact retuning source used here is:
- `yspennstate/math-open-problems@e9a425b9ec3455dfe13b787fb259dec11aa1b176`
- `proofnet24/QFORM-density/fixed-multiplicity-2026-09-24/improvements/account03/B13/20260924T153511Z-account03-B13-FIXMULT-auto11/REPORT.md`.

Two independent end-to-end reviews of the underlying s8 architecture are preserved at:
- `2bf752b5944536f51357d3d3b8b17212a297c7a6` (account03/B08),
- `d4eee5296bcc7fea885435e9cee72379d0e902eb` (account03/B18).

The second review also source-checks the Livshyts--Paouris--Pivovarov projection sharpening and obtains the literal-crossing estimate
[
|p_Q|_inftyle 6^{4/3} Z_3(M)^{-1/6}.
	ag{1.1}
]

I do **not** claim a fresh full line-by-line audit of every non-B15 line of the 955-line source in this run; the B15 analytic segment and every inequality newly used below were independently checked.

## 2. Correction to the previous ephemeral B15 <348 certificate

A previous uncommitted B15 write-up used the rational majorants
[
sqrt2<14143/10000,quad e<27183/10000,quad
(9/2)^{1/6}<257/200,quad sqrt{689/5}<2937/250
]
and asserted that their product in the large-(V_3) branch was below 348.

That certificate is arithmetically false:
[
6{14143over10000}{27183over10000}{257over200}{2937over250}
=
{870557078411163over2500000000000}
=348.2228313644652ldots>348.
]
The underlying real-valued branch constant for those old parameters is about (347.89973), so this only invalidates the displayed coarse certificate, not the structural mechanism. The present retuning below avoids that issue entirely by an exact sixth-power integer comparison.

## 3. Retuned five-direction half-potential input

Retain the independently checked B13 inner parameters
[
d={11over40},qquad p={9over1000},qquad h={107over1000}.
	ag{3.1}
]
The no-inner-pivot entry bound satisfies
[
p+d^2={677over8000}<left({291over1000}ight)^2,
]
and the order-two interpolation margin is exactly
[
1-d-{291over1000}-4h={3over500}>0.
]
Thus the B13 order-two spectral-to-volume proof applies unchanged.

The three inner terminal estimates are all below (105/2):
- no inner pivot: the audited (C_2=8sqrt e,2^{-1/8}) receiver and (h=107/1000) give (C_2sqrt{2/h}<105/2);
- pair pivot: (16p^{-1/4}<105/2), equivalently (p>(32/105)^4);
- scalar pivot: (1+d^{-1/2}(J_0+2L_0)<105/2), using the exact rational logarithm certificates already checked in the B13 source.

Hence, with arbitrary affine terms,
[
oxed{
s_5(S)ge1quadLongrightarrowquad
sup_amathbb E|X^TSX+ell^TX+c-a|^{-1/2}< {105over2}.
}
	ag{3.2}
]

## 4. New outer parameters

Set
[
oxed{eta={13over399},qquad kappa={1over178}.}
	ag{4.1}
]
Here an outer pivot means either (|A_{ii}|geeta) or a principal two-coordinate determinant of modulus at least (eta).

In the no-pivot chamber,
[
|A_{ii}|<eta,qquad
|A_{ij}|^2<eta+eta^2=:u={5356over159201}.
	ag{4.2}
]
We use the simple exact bounds
[
sqrt u<{23over125},qquad
sqrtkappa<{1over13}.
	ag{4.3}
]

### 4.1 First and second disjoint volumes

If (V_1<kappa), then
[
|A|<eta+sqrtkappa<1,
]
contradicting (s_8(A)ge1). Therefore (V_1gekappa).

If (V_2<kappa V_1), the order-one completion has error norm (<2sqrtkappa), global rank at most three, and complement rank at most one. The two forced complement diagonal defects contradict that restricted rank because
[
1-eta-sqrt u-4sqrtkappa
>
1-{13over399}-{23over125}-{4over13}
=
{308449over648375}>0.
	ag{4.4}
]
Hence
[
oxed{V_2gekappa V_1gekappa^2.}
	ag{4.5}
]

## 5. Large third volume: exact bound below 291

If (V_3gekappa^3), a fair literal coordinate cut has
[
Z_3ge {kappa^3over64}.
]
Apply the source-checked LPP-sharpened crossing receiver (1.1):
[
|p_Q|_infty
le 6^{4/3}left({kappa^3over64}ight)^{-1/6}
=2,6^{4/3}sqrt{178}.
]
This is **strictly below 291** with no floating-point certificate:
[
left(2,6^{4/3}sqrt{178}ight)^6
=
2^6,6^8,178^3
<
291^6,
	ag{5.1}
]
and the exact positive integer margin is
[
291^6-2^6,6^8,178^3=989059098393.
]
Thus the entire large-(V_3) branch costs (<291).

## 6. Small third volume: collar still closes

Assume (V_3<kappa^3). Since (4.5) gives (V_2gekappa^2),
[
{V_3over V_2}<kappa.
]
The reviewed order-two volume-sampled completion therefore has good seeds carrying at least half the (V_2) mass and error
[
arepsilonlesqrt{18kappa}
=sqrt{9/89}
<{319over1000}.
	ag{6.1}
]

For each good seed the same rank-six completion forces two complement diagonal defects and yields the physical two-anchor determinant factor
[
delta=(1-arepsilon-eta)^2-(sqrt u+arepsilon)^2
=1-3eta-2arepsilon(1-eta+sqrt u).
	ag{6.2}
]
Using (4.3) and (6.1),
[
delta>
1-3{13over399}
-2{319over1000}left(1-{13over399}+{23over125}ight)
=
{4180787over24937500}
>{1over6}.
	ag{6.3}
]
The reviewed robust-anchor aggregation therefore produces a literal two-set (H), with
[
C=A[H,H^c],qquad g=det(CC^T)>{delta^2over2}>{1over72}.
	ag{6.4}
]

### 6.1 Two-high leverage is impossible

Let (Q_C=C^T(CC^T)^{-1}C), (q_i=(Q_C)_{ii}), and
[
w_{ij}={det(C_{{i,j}})^2over g}.
]
The rank-two determinantal marginal identity gives
[
q_i=sum_{j
e i}w_{ij},qquad sum_{i<j}w_{ij}=1.
]
If two indices satisfy (q_i,q_j>2/3), then (w_{ij}>1/3), hence
[
det(C_{{i,j}})^2>{gover3}>{1over216}.
]
But every entry of this physical cross minor is off-diagonal and (4.2) gives
[
det(C_{{i,j}})^2<4u^2.
]
The exact comparison is
[
{1over216}-4u^2
=
{20726611over202759667208}>0,
]
a contradiction. Thus at most one high-leverage coordinate exists.

### 6.2 One-high completion

The reviewed anchored-minor completion says
[
|E|_F^2le {3W_{m dis}over g}.
]
If (W_{m dis}le g/75), then (|E|_Fle1/5). Rank perturbation forces three low diagonal coefficients of modulus at least (4/5). Strict diagonal dominance follows because
[
sqrt u<{2/5-etaover2};
]
indeed the square comparison has exact margin
[
left({2/5-etaover2}ight)^2-u
={563over5306700}>0.
	ag{6.5}
]
Thus the low-low rank-at-most-two remainder would contain an invertible (3	imes3) block, contradiction. Therefore
[
W_{m dis}>{gover75}>{1over5400}.
	ag{6.6}
]

The already-reviewed product-safe incident-volume receiver gives
[
|p_Q|_infty
le 3,2^{5/6}e^{2/3}W_{m dis}^{-1/6}<60,
	ag{6.7}
]
using (2^{5/6}<2), (e^{2/3}<2), and (5400<5^6). Hence the small-(V_3) branch is far below 291.

## 7. Pivot branches and complete normalized assembly

### Scalar pivot
The Schur complement loses at most one large direction, so (3.2) applies:
[
|p_Q|_infty
<
{105over2}eta^{-1/2}
=
{105over2}sqrt{399over13}.
]
Exactly,
[
291^2-
left({105over2}ight)^2{399over13}
=
{4437over52}>0,
	ag{7.1}
]
so this branch is (<291).

### Definite and indefinite pair pivots
The new pair threshold (eta=13/399) is larger than the already checked (1/44) threshold in the B13 assembly. Therefore its definite-pair and indefinite-pair bounds only improve; the source bounds (<28) and (<138) remain valid.

### No pivot
Sections 5--6 are exhaustive: large (V_3) costs (<291), small (V_3) costs (<60).

Consequently the retuned architecture gives the candidate normalized theorem
[
oxed{
s_8(A)ge1
quadLongrightarrowquad
|p_{X^TAX+b^TX+c}|_{infty,mathrm{ess}}<291.
}
	ag{7.2}
]

For general coordinate cap (K) and spectral scale (s), put (Y=KX) and normalize (A) by (s). Since
[
Q={sover K^2}widetilde Q,
]
density scaling yields
[
oxed{
s_8(A)ge s>0
quadLongrightarrowquad
|p_Q|_{infty,mathrm{ess}}<291,{K^2over s}.
}
	ag{7.3}
]

This is a **candidate retuning of the independently reviewed s8 architecture**. The new parameter choice and constant 291 require independent review before owner-level promotion. It does not solve multiplicity seven or the unrestricted three-eigenvalue theorem.

## 8. B15 regularity: continuity costs zero extra height

The completed affine fixed-instance theorem
[
	ext{`yspennstate/math-open-problems@b8cb4aa22c840d8f4fc76bcca6d0cb49d4aeb9f9`}
]
at
[
	ext{`proofnet24/QFORM-density/fleet-2026-09-22/account03/B15/20260924T092642Z-account03-B15-qform-auto11/REPORT.md`}
]
proves that every fixed rank-at-least-three affine quadratic under arbitrary rough cap-one product inputs has a canonical (C_0(mathbb R)) density.

Since (s_8(A)>0) implies rank at least eight, combining that qualitative theorem with (7.3) gives, for the candidate s8 branch,
[
oxed{
p_{X^TAX+b^TX+c}in C_0(mathbb R),qquad
|p_{X^TAX+b^TX+c}|_infty<291,{K^2over s}.
}
	ag{8.1}
]
No law-uniform or matrix-uniform modulus of continuity is claimed.

### Designated account04/B15 partner applied to an actual inequality

For the homogeneous specialization (b=c=0), normalize (K=s=1). Equation (7.2) gives the actual interval inequality
[
Pr{X^TAXin I}<291|I|.
]
Account04/B15 Theorem 6.1 at
[
	ext{`yspennstate/math-open-problems@7b2b0f54db9acbd23a5f69f715178ab666e22d8e`}
]
[
	ext{`proofnet24/QFORM-density/fleet-2026-09-22/account04/B15/20260923T221909Z-account04-B15-ruled-trace-c0-r8/REPORT.md`}
]
therefore yields the canonical representative
[
oxed{p_{X^TAX}in C_0(mathbb R),qquad |p_{X^TAX}|_inftyle291.}
	ag{8.2}
]
The arbitrary-affine statement (8.1) uses the separate affine fixed-instance theorem and does not enlarge the partner theorem's stated homogeneous scope.

## 9. Absolute continuity remains logically weaker

For any nonconstant affine quadratic
[
q(x)=x^TAx+b^Tx+c
]
and any absolutely continuous joint input law, (q(X)) is absolutely continuous. The critical set
[
{2Ax+b=0}
]
is empty or a proper affine subspace. For a one-dimensional null set (N), coarea on
[
q^{-1}(N)cap{|
abla q|ge1/k}
]
shows each such set is Lebesgue-null; adjoining the null critical set proves (|q^{-1}(N)|=0).

This needs neither product structure nor a density cap. It proves density existence only; the fixed-matrix product theorem supplies qualitative (C_0), while the multiplicity estimate supplies a uniform height.

## 10. Exact status

- B15 Fourier/Gaussian/Riesz interfaces in both nine-eigenvalue write-ups: **PASS**.
- Previous ephemeral coarse rational certificate for (<348): **FALSE AS WRITTEN**, repaired here.
- Underlying reviewed s8 architecture: existing independent PASS reviews preserved.
- New retuning (s_8Rightarrow|p_Q|_infty<291K^2/s): **CANDIDATE / needs independent review of the new parameters**.
- Same-height (C_0) consequence conditional on that paid interval bound: **PROVED** by completed fixed-instance regularity.
- Absolute continuity for every nonconstant affine quadratic under any absolutely continuous joint law: **PROVED**.
- Multiplicity seven: **OPEN**.
- Full owner target with only three large eigenvalues: **OPEN / no counterexample produced**.

No Gaussian, log-concavity, moment, compact-support, connected-support, iid, diagonal-basis, post-rotation independence, pointwise rough van-der-Corput bound, or Monte Carlo extremality assumption is used.
