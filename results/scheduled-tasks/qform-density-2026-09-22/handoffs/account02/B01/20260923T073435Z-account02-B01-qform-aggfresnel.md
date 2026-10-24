SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account 02, slot B01, 2026-09-23T07:34:35Z.
attacking: the two-sided-curved rank-two bicore by averaging the full rank-two cross coefficient first, then spending an overlapping transverse receiver square through joint Fresnel–Brascamp–Lieb rather than any scalar pointwise phase decay.

# account02/B01 handoff — grouped cross-area + overlapping receiver Fresnel packet

Outcome: `PROVED_SUPPORTING_TARGET_LEVEL_THEOREM + PAID_STRICT_N3_FAMILY`; full QFORM remains `OPEN`; execution `WITHOUT_VERIFIED_BRAIN`.

Final prepublication control refresh observed `yspennstate/math-research-brain@d95fceaa80e0498172d2d98a8fdf869a60d51a71`; the control README blob remained on OWNER CONTROL revision `2026-09-22.15`, QFORM-only, with no account02/B01 stop. The live correction inbox had no newer merge than its previously consumed source-backed corrections. The required Claude/Fourier package at `math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837` was used at the actual `L^p` Fourier and geometric Brascamp--Lieb inequalities; later same-directory commits added compatible geometric/continuation material and did not revoke those lemmas.

Canonical mathematics: `yspennstate/math-open-problems@d16921498c8ca82b8ab89f115b8b6bded05da4e9`, directory `proofnet24/QFORM-density/fleet-2026-09-22/account02/B01/20260923T073435Z-account02-B01-qform-aggfresnel/`. `REPORT.md` is the full proof; `SOURCE_REFRESH_ADDENDUM.md` applies the newest designated partner result; `CHECK_OUTPUT.txt` ends `STATUS=PASS` and is auxiliary regression evidence only.

## New theorem

Split original independent coordinates into active banks `I,J` and condition all others. Let the exact physical cross matrix `K=A_IJ` have rank two, singular values `kappa_1,kappa_2>0`, and `Delta=kappa_1 kappa_2`. Let `V` span `range(K^T)`. Suppose

`A_JJ = D + R Lambda R^T`,

where `D` is diagonal, `R` has `r` orthonormal columns, and `Lambda` is invertible diagonal. Put

`Omega^2 = det(R^T(I-VV^T)R)>0`,

and assume every physical-coordinate leverage of `span(V,R)` is at most `1/2`. Then for

`Q=H(X_I)+2X_I^T K X_J+X_J^T(D+R Lambda R^T)X_J+b^T X_J+c`,

with completely arbitrary real measurable `H` and arbitrary affine terms,

`|phi_Q(t)| <= min(1, B_r |t|^(-(2+r/2)))`,

`B_r=(4*pi)^(2+r/2)/(2 Delta Omega sqrt(|det Lambda|))`,

and therefore

`||p_Q||_infinity <= 4(r+4)/(r+2) [2 Delta Omega sqrt(|det Lambda|)]^(-2/(r+4)).`

For one overlapping receiver square (`r=1`),

`||p_Q||_infinity <= [20/(3*2^(2/5))](Delta Omega sqrt(|lambda|))^(-2/5) <5.053(Delta Omega sqrt(|lambda|))^(-2/5).`

The proof first uses the product-projection cap `||p_{K^T X_I}||_infinity<=2/Delta`, then Fresnel-linearises only the receiver low-rank curvature, changes variables jointly in the two cross-frequency directions and the `r` Fresnel variables, paying the transverse Jacobian `Omega`, and applies the source `int |g_hat|^p <=4*pi/sqrt(p)` lemma through geometric Brascamp--Lieb on the entire augmented receiver subspace. The arbitrary same-bank curvature `H(X_I)` disappears only after taking modulus outside the coefficient average. Thus this is a joint averaged-frequency mechanism, not a law-uniform scalar Fresnel estimate; the phase-aligned-density refutation remains intact.

## Exact strict-N3 target family

For `m=2^q`, take the normalized symmetric Sylvester-Hadamard matrix `H_m`; diffuse Walsh vectors `u_1,u_2` on bank `I`; diffuse orthonormal `v_1,v_2,w` on bank `J`; `0<eta<=1/4`; `c=1+eta`; and

`K=c(u_1v_1^T+u_2v_2^T)`,

`A_{m,eta}=[[eta H_m,K],[K^T,ww^T]]`.

The unperturbed block has singular values `c,c,c,c,1`; the Hadamard perturbation has operator norm `eta`, hence the first four singular values of `A_{m,eta}` are at least `c-eta=1`. Since the matrix is symmetric, the exact target spectral condition holds. All physical diagonals and all physical `2x2` principal determinants tend to zero with `m`, so this enters strict N3 for every fixed threshold at large `m`.

Here `Delta=c^2`, `Omega=1`, `lambda=1`, and augmented receiver leverage is `3/m<=1/2`, so

`boxed: ||p_{X^T A_{m,eta}X}||_infinity <= [20/(3*2^(2/5))]c^(-4/5) <=5.0523885551.`

At `eta=1/4`, the bound is `4.2263818466`. The dense full-rank non-diagonal `eta H_m` curvature on the opposite active bank is retained exactly rather than treated as a small random quadratic perturbation.

## Newest designated partner result actually applied

Before publication, account03/B01 published `QFORM-RANK2-CROSS-PLUS-SQUARE-L3-v1` at brain commit `00703d7b1378fd37c26de163532b2790acbdb7c4`, canonical math `yspennstate/math-open-problems@e8c8cc633f1fe33ec6b568f80c5c7f68a105a159`. For a rank-two cross packet plus a **source-disjoint** square it proves

`||p_Q||_infinity <= (16/3)12^(1/4)(kappa_1 kappa_2)^(-3/8)(|lambda|sigma^2)^(-1/4).`

Apply it to the source-disjoint strict-N3 variant

`A_disj=[[eta H_m,K,0],[K^T,0,0],[0,0,ww^T]]`.

It has the same four absolute eigenvalues at least `c-eta=1`, plus the disjoint square eigenvalue `1`; all physical local pivots still vanish with `m`. With `kappa_1=kappa_2=c`, `lambda=1`, `sigma=1`, the partner gives

`||p_{X^T A_disj X}||_infinity <= (16/3)12^(1/4)c^(-3/4) <9.927 c^(-3/4)`,

and at `eta=1/4` this is `<8.400`.

This newest partner result is complementary rather than duplicative: it allows arbitrary self phases on both cross banks but needs the third square on a disjoint source bank; the theorem proved in this run handles the genuinely **overlapping** square on the receiver bank under transversality/leverage hypotheses.

## First unpaid implication

`QFORM-CURVED-RECEIVER-TRANSVERSE-OR-ALIGN-ROUTING-v1`: in an arbitrary strict-N3 rank-two bicore with substantial nonlinear self-curvature on both active banks, quantitatively route either to (i) a transverse low-rank receiver packet satisfying the new `Omega`/leverage gate, (ii) the newest source-disjoint-square partner receiver, or (iii) an already-paid one-sided-affine/physical-pair/hub/ridge/volume/grouped-square/exact-null branch, before any reciprocal tiny local determinant is paid. The analytic overlapping receiver is now paid; the remaining debt is structural and exhaustive.

Full QFORM is not proved or disproved, and no full candidate has two independent end-to-end reviews. The same actual-hour B01 login already existed from the preceding invocation and was preserved rather than overwritten; this invocation created its own unique start/finish records. Repository retrieval was authenticated, but no native learned-memory receiver use was established, so execution remains `WITHOUT_VERIFIED_BRAIN`. Model self-report is `GPT-5.6 Sol`; configured/self-reported thinking level is `UNKNOWN`; reasoning-token and provider-thinking-time telemetry are `null/not exposed`.
