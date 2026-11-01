SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B01, 2026-09-22T23:45:37Z.
attacking: grouped-defect disjoint-innovation square smoothing and its exact signed-Fejer consequence; no uniform pointwise Fourier-decay claim.

# fleet04/B01 — grouped square innovations pay the diffuse completion-defect witness

Run: `20260922T234537Z-fleet04-B01-grouped-square-fejer-r2`  
Programme: `QFORM-DENSITY-3EIG-20260922`  
Classification: `SUPPORTING_TARGET-LEVEL_THEOREM / ESSENTIAL_STEP_APPLIED / FULL_TARGET_OPEN`  
Execution: `WITHOUT_VERIFIED_BRAIN`

## 1. Source and correction boundary

The full target is unchanged. The input coordinates are independent and have arbitrary real probability densities bounded by one. The matrix is an arbitrary real symmetric matrix with at least three eigenvalues of modulus at least one. No moment, support, Gaussian, log-concavity, identical-law, centering, or post-rotation independence assumption is used.

Fresh controls were read at owner revision `2026-09-22.15`. The current correction inbox blob is `c7000cf3822ae4935a2faf43b89ac92ea65ac0fe`; the assignment blob is `0aabfb0233abb7f67e46808b03987c0300502329`; and the memory protocol blob is `0d902d56688f4b5c575f5b921ddf9f6709e88312`.

The newest source-directory history ends at
`math-open-problems@2f3340cd21be3e8b1a0d3a738e1fa7b7c6b76926`.
The relevant current blobs are `RESULTS.md@56edacbd7aa105e7aaabfcfb6f377c268a134817`, `FOURIER_ROUTE_REPORT.md@9da148eed6cd43b1046a6f91d0f9329e12921cb4`, and `COUNTEREXAMPLE_SEARCH.md@d11ace6dbf5ecdf6ce5921f80f727e92e95bf8fc`. The previous Claude-review corrections are retained. In particular, this report neither asserts a law-uniform pointwise Fresnel bound nor an absolute-Wiener bound.

The designated fleet01/B01 input is the completion-defect report
`math-open-problems@bf06839b97a3af3f800751cd9bd8502bcf8011d0`,
report blob `aa1343f693b62b27fde3c16fb109b52b0bb00a78`.
It constructs a target matrix whose two unit completion defects are diffuse grouped squares although every fixed physical coefficient vanishes. That report paid the witness only for Gaussian laws. The theorem below pays the entire witness for every admissible cap-one product law.

## 2. Projection and shifted-square inputs

I use the one-dimensional case of the standard Ball/Livshyts-Paouris-Pivovarov product-marginal theorem: if (X_i) are independent with densities at most one and
[
Y=sum_i a_iX_i,qquad sigma=|a|_2>0,
]
then (Y) has a density (g_Y) satisfying
[
|g_Y|_inftyle {sqrt2over sigma}.                                      	ag{2.1}
]
This is an original-coordinate product-marginal statement; no independence is asserted after an arbitrary rotation.

If (Y) has density bounded by (M), then for every shift (h) and every (lambda
e0), the variable
[
Z=lambda(Y+h)^2
]
has a density. For (lambda>0),
[
p_Z(s)=
 {g_Y(-h+sqrt{s/lambda})+g_Y(-h-sqrt{s/lambda})
  over 2sqrt{lambda s}},1_{{s>0}}
 le {Moversqrt{lambda s}},1_{{s>0}}.                    	ag{2.2}
]
For (lambda<0), the reflected version of (2.2) holds on (s<0).

Consequently, if (Z_1,Z_2) are independent shifted squares with coefficients of the same sign, then
[
|p_{Z_1+Z_2}|_infty
 le {pi M_1M_2oversqrt{|lambda_1lambda_2|}},              	ag{2.3}
]
because
[
int_0^s {duoversqrt{u(s-u)}}=pi .
]
This is an interval/density calculation. It makes no claim about pointwise decay of either characteristic function.

## 3. Grouped disjoint-innovation theorem

**Theorem 3.1 (QFORM-GROUPED-SQUARE-INNOVATIONS-v1).**
Partition the original coordinates into four disjoint sets
[
C,B_1,B_2,B_3.
]
For (j=1,2,3), let
[
L_j=a_j^TX_{B_j},qquad sigma_j=|a_j|_2>0.
]
Suppose the quadratic form has the exact representation
[
Q=R(X_C)+sum_{j=1}^3lambda_j
       igl(L_j+h_j(X_C)igr)^2,                              	ag{3.1}
]
where (lambda_j
e0), while (R,h_j) are arbitrary measurable functions for which (3.1) is defined. Then (Q) has a bounded density. For every same-sign pair (j
e k),
[
oxed{;
 |p_Q|_infty
 le {2piover
       sigma_jsigma_ksqrt{|lambda_jlambda_k|}}; .         	ag{3.2}
}
]
Hence one may take the minimum of the right side over all same-sign pairs. Such a pair always exists among three nonzero real coefficients.

Moreover (p_Q) has a representative in (C_0(mathbb R)).

**Proof.**
Condition on (X_C=c). The variables (L_1,L_2,L_3) remain independent because their banks are disjoint original-coordinate banks. By (2.1),
[
M_ell:=|p_{L_ell}|_inftyle {sqrt2oversigma_ell}.
]
Choose a same-sign pair (j,k). Apply (2.3) to the corresponding two shifted squares. Their conditional sum has density cap
[
{pi M_jM_koversqrt{|lambda_jlambda_k|}}
le {2pioversigma_jsigma_k
                 sqrt{|lambda_jlambda_k|}}.
]
The third shifted square is conditionally independent and has an (L^1) probability density. Convolution with it cannot increase the (L^infty) norm. The remaining (R(c)) only translates the output. Thus the conditional interval inequality
[
Pr{Qin Imid X_C=c}
le {2pi |I|over
       sigma_jsigma_ksqrt{|lambda_jlambda_k|}}
]
holds uniformly in (c). Averaging proves (3.2) and absolute continuity.

For fixed (c), each shifted square has an (L^1) density; the convolution of the selected pair belongs to (C_0), and convolution with the third probability density remains in (C_0). These conditional densities are uniformly bounded by (3.2). Dominated convergence first under translations and then as (|y|	oinfty) shows that their average is in (C_0). QED.

The theorem is stable under arbitrary conditioning-generated shifts. It pays the whole grouped coefficient norm (sigma_j) before choosing a physical coordinate.

## 4. The fleet01 completion-defect family for all laws

The designated report defines five disjoint blocks (U,V,W,Z,T), normalized all-ones vectors (e_U,ldots,e_T), and
[
A_m=r_1r_1^T+r_2r_2^T+r_3r_3^T,
quad
r_1=e_U+e_V+e_W,quad
r_2=e_U+e_Z,quad
r_3=e_V+e_T .
]
Its nonzero eigenvalues are exactly
[
4, 2, 1,                                                       	ag{4.1}
]
while every physical coefficient is (O(m^{-1})). Write
[
u=e_U^TX_U, v=e_V^TX_V, w=e_W^TX_W, z=e_Z^TX_Z, 	au=e_T^TX_T .
]
Then
[
Q_m=(u+v+w)^2+(u+z)^2+(v+	au)^2.                              	ag{4.2}
]

Condition on the original banks (U,V). Equation (4.2) is exactly (3.1) with innovation banks (W,Z,T), coefficient norms
[
sigma_W=sigma_Z=sigma_T=1,
]
and (lambda_1=lambda_2=lambda_3=1). Therefore, for **every** choice of independent cap-one coordinate laws,
[
oxed{;
 |p_{Q_m}|_inftyle2pi,qquad p_{Q_m}in C_0(mathbb R),
;}                                                               	ag{4.3}
]
uniformly in (m).

This is the required actual application of the completed fleet01/B01 result. The partner's obstruction says no fixed coordinate, edge, or bounded principal block can harvest the two completion defects. Inequality (4.3) shows that grouped innovation smoothing nevertheless pays the entire target-valid family with no dimension loss and with no Gaussian-law restriction.

## 5. Exact averaged-frequency consequence

For a probability law (mu), define the signed triangular Fejer average
[
D_Tmu(y)={1over2pi}int_{-T}^T
 left(1-{|t|over T}ight)
 Re!left(e^{-ity}widehatmu(t)ight),dt .                 	ag{5.1}
]
The previous fleet04/B01 theorem proves
[
|p_mu|_infty=sup_{T>0, yinmathbb R}D_Tmu(y),           	ag{5.2}
]
with both sides (+infty) if no bounded density exists.

Applying (5.2) to Theorem 3.1 gives the actual averaged-frequency inequality
[
oxed{;
 D_Toperatorname{law}(Q)(y)
 le {2piover
       sigma_jsigma_ksqrt{|lambda_jlambda_k|}}
 quad	ext{for all }T>0, yinmathbb R ,
;}                                                               	ag{5.3}
]
for every same-sign pair (j,k). In particular,
[
D_Toperatorname{law}(Q_m)(y)le2pi                            	ag{5.4}
]
for every (m,T,y).

Equation (5.3) is phase-sensitive and retains time cancellation. It does not assert
(int|widehatmu(t)|dt<infty), nor any law-uniform pointwise (|t|^{-1/2}) bound.

## 6. What remains

The full conjecture is still open. The no-pivot reduction N3 does not automatically furnish an exact representation (3.1). In a general dense no-pivot matrix, the putative defect banks can have self-curvature and mutually overlapping innovation maps. Conditioning one bank can therefore destroy the disjoint product structure needed above.

The next precise implication is structural: convert two completion defects into two **disjoint original-coordinate innovation sources**, or prove a replacement inequality for overlapping grouped sources that retains their full singular-value mass. The fleet01 family proves why descending to one coordinate first is impossible; Theorem 3.1 proves that exact disjoint group innovations are already sufficient.

Essential boundedness and continuity are distinguished: this theorem proves both on its branch, while the unrestricted universal height conjecture remains open.
