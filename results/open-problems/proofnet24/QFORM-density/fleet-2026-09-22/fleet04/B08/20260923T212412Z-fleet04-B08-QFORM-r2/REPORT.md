SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account fleet04, slot B08, 2026-09-23T21:24:12Z.
attacking: compile fleet01/B08 deletion rigidity with the affine-uniform ridge-window theorem on the same physical deletion block, paying the genuine third-child branch or isolating a localized child window.

# fleet04/B08 r2 — child-window receiver for the diffuse-star hybrid

Programme: `QFORM-DENSITY-3EIG-20260922`  
Run: `20260923T212412Z-fleet04-B08-QFORM-r2`  
Status: `ESSENTIAL_STEP_APPLIED / PROVED_SCOPED_TARGET_ROUTER / FULL_TARGET_OPEN`  
Execution: repository publication is not native ingestion.

The unrestricted conjecture remains OPEN. This note removes the diffuse part of the “genuine third-child” obstruction in fleet01/B08 r35. It does not pay the near-aligned star, a heavy combined star/two-child frame row, or a localized high spectral window inside the child. It uses only original-coordinate conditioning and preserves all signs, all complementary spectrum, and arbitrary cap-one laws.

## 1. Exact inputs

The new structural input is fleet01/B08 r35,
`math-open-problems@68f8d8a91987834d73fa06849d9ec8795a3df883`,
theorems `QFORM-DELETE1-TWOCHILD-RIGIDITY-v1` and
`QFORM-DUAL-K2-STAR-HALFCUT-v1`.

The analytic input is the affine-uniform spectral-window theorem,
`math-open-problems@9c1167db05c7b0f520f060796fde921ed769a4e7`,
`interactive/20260922T151048Z-ridge-window/REPORT.md`, Section 7. At scale (m>0), it states that if a symmetric matrix (C) has three eigenvalues of modulus at least (m), and its spectral projection (P_C(m/64)) onto (|\lambda(C)|\ge m/64) obeys
[
max_j (P_C(m/64))_{jj}le rac1{32},
]
then every cap-one product input, with arbitrary coordinate-separable measurable perturbations finite almost surely, has a continuous (C_0) output density bounded by
[
rac{288sqrt{3e}}{13m}<rac{64}{m}.
]
The permission for arbitrary coordinate-separable perturbations is essential below.

The control state was refreshed at

## 2. Conditional child-window lemma

### Theorem — `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1`

Let
[
A=egin{pmatrix}a&b^	op\\ b&Cend{pmatrix}
]
be written after moving one ORIGINAL coordinate (i) first. Let (X_i) be independent of the remaining original-coordinate vector (Y), whose coordinates have densities bounded by one. Suppose (C) has at least three eigenvalues of modulus at least (m>0), and
[
max_j(P_C(m/64))_{jj}lerac1{32}.
]
Then
[
oxed{ |p_{X^	op AX}|_infty
 le rac{288sqrt{3e}}{13m}<rac{64}{m}. }
]
Moreover the output has a continuous (C_0) density.

#### Proof

Condition only on the original physical coordinate (X_i=x). The conditional output equals
[
Y^	op C Y+sum_j 2x b_jY_j+a x^2.
]
For fixed (x), the remaining coordinates are still independent and retain their original density caps. The linear term is coordinate-separable:
[
sum_j h_{j,x}(Y_j),qquad h_{j,x}(y)=2xb_jy,
]
and the final scalar (ax^2) is only a translation. The affine-uniform spectral-window theorem therefore gives, for every finite (x),
[
|p_{Qmid X_i=x}|_infty
 le rac{288sqrt{3e}}{13m}.
]
Mixing these conditional densities yields the same essential-supremum bound for (Q). Their common uniform bound also permits dominated convergence, first for (t_k	o t) and then for (|t|	oinfty); hence the mixture is continuous and vanishes at infinity. QED.

No rotated random coordinates were introduced. The cross term was retained exactly as an allowed original-coordinate separable perturbation after conditioning.

## 3. Application to the live fleet01/B08 survivor

Use the notation and constants of fleet01/B08 r35. A selected three-eigenvector frame at scale (L) is diffuse:
[
max_i(P_3)_{ii}lerac1{48}.
]
When the whole-window ridge gate fails and the scalar pivot branch is absent, r35 produces a physical deletion
[
A=egin{pmatrix}a&b^	op\\ b&Cend{pmatrix}
]
with
[
|b|>eta_0L,qquad
s_2(C)ge sigma_0L,
]
where
[
eta_0=rac{sqrt3}{128sqrt{96}},
qquad sigma_0=sqrt{rac{47}{48}}.
]
Let (d) be the distance from (b/|b|) to the top-two child eigenspace and let (
u) be the maximum row leverage of the combined star/two-child frame. At the live gates (dge1/2) and (
ule1/48), r35 gives
[
kappa_0
 =rac{eta_0sigma_0/2}
        {2sqrt{4eta_0^2+sigma_0^2}}
 =0.00034526563789691794ldots
]
and hence, if
[
s_3(C)le ho_0L,qquad
ho_0:=rac{kappa_0}{16}
 =2.157910236855737	imes10^{-5},
]
the literal rank-three crossing (with every same-bank term retained) pays
[
oxed{ |p_Q|_infty
 <rac{23}{kappa_0L}
 <rac{66615.376}{L}. }                                      	ag{3.1}
]

Now suppose instead
[
s_3(C)>ho_0L.                                                  	ag{3.2}
]
Let (P_C) be the full child spectral projection onto
[
|lambda(C)|ge rac{ho_0L}{64}.
]
If
[
max_j(P_C)_{jj}lerac1{32},                                  	ag{3.3}
]
apply `QFORM-PHYSICAL-DELETION-CHILD-WINDOW-v1` with (m=ho_0L). This consumes the completed fleet01/B08 result at the actual inequality (3.2) and gives
[
oxed{ |p_Q|_infty
 <rac{64}{ho_0L}
 <rac{2965832.356}{L}. }                                     	ag{3.4}
]
The comparison (3.1)/(3.4) is on the SAME surviving original-coordinate matrix and the SAME physical deletion (i): (3.1) uses the literal cross block ([b_S,C[S,T]]), while (3.4) uses the literal child block (C) after conditioning on (X_i). Neither route discards the other terms.

Consequently the r35 “third-child” obstruction is no longer merely (s_3(C)>ho_0L). Its diffuse subcase is fully paid. Every survivor of the compiled B08 route satisfies at least one of
[
oxed{
d<rac12,qquad

u>rac1{48},qquad
s_3(C)>ho_0L 	ext{and} 
max_j(P_C(ho_0L/64))_{jj}>rac1{32}.
}                                                               	ag{3.5}
]
Thus the last alternative carries a concrete original-coordinate witness: a child coordinate (j) with high-window leverage (>1/32).

## 4. Full router and remaining implication

Together with the earlier branches, a selected-three diffuse state is now paid when:

1. the ambient full window is diffuse: (<64/L);
2. the forced physical diagonal pivot is present: (<4.928	imes10^{10}/L);
3. the star/two-child frame is transverse and diffuse and the child third singular value is small: (<66615.376/L);
4. the child third singular value is large and the corresponding child high window is diffuse: (<2965832.356/L).

The first unproved implication is now
`QFORM-LOCALIZED-CHILD-WINDOW-COMPILER-v1`: pay the last alternative in (3.5), or combine its localized child coordinate with the existing physical star without losing product provenance. The near-aligned case (d<1/2), the heavy combined-frame row (
u>1/48), the localized selected-three branch, the convex/two-sheet collar, and arbitrary end-to-end extra-spectrum assembly also remain open.

The full universal theorem and a counterexample are not claimed.
