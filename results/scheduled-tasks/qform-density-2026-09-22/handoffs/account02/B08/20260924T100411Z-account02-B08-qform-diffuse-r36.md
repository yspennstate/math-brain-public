# account02/B08 r36 handoff — three-bank literal energy and punctured double-alignment collar

Programme: `QFORM-DENSITY-3EIG-20260922`; OWNER CONTROL revision `2026-09-22.15`; execution `WITHOUT_VERIFIED_BRAIN`. Full QFORM remains OPEN.

Canonical mathematics:
- repository: `yspennstate/math-open-problems`
- commit: `26422be5c2a10a666dfc7480c9e37a203718c146`
- root: `proofnet24/QFORM-density/fleet-2026-09-22/account02/B08/account02-B08-20260924T094502Z-r36/`
- files: `REPORT.md`, `CHECKS.md`
- check marker: `QFORM_B08_R36_CHECK_PASS`

Fresh localized/diffuse input actually used: account01/B08 r47, `math-open-problems@73e69c64a5499c82342a527bc232d531b54f6874`. Fresh designated partner actually used: account03/B08 `QFORM-PUNCTURED-CROSSSTAR-DOUBLEALIGN-ROUTER-v1`, `math-open-problems@19c12072f7e67266ce894042034bcabb9c376bea`, handoff `20260924T061920Z-account03-B08-qform-diffuse-r51.md`. The required fixed source `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` RESULTS/FOURIER_ROUTE_REPORT/COUNTEREXAMPLE_SEARCH was reread and generalized Theorem F was applied to the actual family below.

## New theorem: `QFORM-THREEBANK-R2-LITERAL-ENERGY-v1`

On the newest account01/B08 r47 unpaid rank-two branch, write `D=A[S\{k},T]`. One has

`s_2(D)>=sigma L`, `sigma=sqrt(67/800)/2=0.14469796128487783...`,

and a unit `u` in the top-two right singular plane with `||u_{K_r}||>=1/8` on three pairwise-disjoint ORIGINAL-coordinate banks `K_1,K_2,K_3`.

For `w_r=u_{K_r}/||u_{K_r}||`, the PSD inequality

`D^T D >= s_2(D)^2 P_{V_2(D)}`

gives

`boxed: ||D w_r|| >= (sigma/8)L =0.01808724516060973...L`

for all three banks. Hence each literal sub-crossing obeys

`boxed: s_1(D[:,K_r])>=0.01808724516060973...L`

(and the same lower bound for its Frobenius norm). This converts the carrier footprint into three target-scale literal coefficient-energy gates while retaining disjoint original product blocks. No rotated residual independence is claimed.

A source-safe auxiliary lemma was also proved: if `Y=<w,X_K>` for a unit vector on one ORIGINAL product block, then `||p_Y||_infinity<=sqrt(2)`, and for any internal measurable phase `tau`,

`G(s)=E exp(i tau(X_K)+isY)`

satisfies for every `p>=2`

`integral |G(s)|^p ds <=4 pi sqrt(2)/sqrt(p)`.

This follows by disintegration, domination of the signed pushforward by `p_Y`, dilation, and the fixed twisted one-dimensional Fourier lemma. It preserves block provenance but does not yet expose the needed common Fourier parameter through the unrestricted rank-two crossing.

## Exact target-valid punctured-collar stress family

For `m=2^q>=16384`, choose normalized Walsh characters `u_1,u_2,u_3` and an independent sign character giving a half-cut `J union K`. Put

`C_epsilon=L(u_1u_1^T+u_2u_2^T+epsilon u_3u_3^T)`,
`b=sqrt(2)L u_1`, `a=0`,
`A_epsilon=[[0,b^T],[b,C_epsilon]]`,

with `0<epsilon<1/4096`.

The nonzero spectrum is exactly

`{2L,-L,L,epsilon L}`,

so there are exactly three eigenvalues of modulus at least `L`. On the Walsh half-cut the child crossing has singular values exactly

`L/2, L/2, epsilon L/2`,

and both star halves lie exactly in the corresponding top-two singular planes. Thus this is a genuinely punctured (`s_3(C)=epsilon L>0`) **double-aligned** account03 collar state. Every physical `2 x 2` principal block has `sigma_min<L/64` for `m>=16384`. Also `||A_epsilon-A_0||_op=epsilon L`, while `A_0` is the paid exact endpoint.

The fixed-source generalized Fresnel--Brascamp--Lieb Theorem F, used on the ORIGINAL light coordinates with frame `[u_1,u_2,u_3]`, gives the real target inequality

`boxed: ||p_{X^T A_epsilon X}||_infinity <=12 epsilon^(-1/3)/L`,

with a continuous `C_0` density, for every admissible cap-one product source. At `epsilon=2^-16` this is `483.8096831596312/L`. The estimate diverges as `epsilon->0` while the exact endpoint has the partner bound `<362.039/L`; hence the missing collar compiler is genuinely nonperturbative.

## First unpaid implication

`QFORM-THREEBANK-TWISTED-CARRIER-OR-DOUBLECANCEL-COMPILER-v1`:

pay either the newest three-bank rank-two carrier with three literal sub-crossing energies `>=0.01808724516L`, or the two-mode complementary-cancellation branch, while retaining arbitrary same-bank curvature and complementary spectrum. On the deletion-child aligned branch, make the proof uniform through `0<s_3(C)<L/4096` down to the paid exact endpoint. Do not rotate the product law and do not treat a small coefficient tail as a small random perturbation.
