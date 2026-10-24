# FOREST handoff — account03/B01 — exact activity unrooting + determinant-mixture no-go

Status: **ESSENTIAL_STEP_APPLIED**, with subsidiary **CANDIDATE_REFUTED**. Parent team state remains internal **FULL_PROOF_CANDIDATE** from lead `FOREST-KN-COCKS-RECONCILED-v3`; no public theorem promotion. Context: `WITHOUT_VERIFIED_BRAIN`.

Scientific report: `proofnet24/P14-probability-correlation/collective-2026-09-22/account03/B01/20260922T032940Z-account03-B01-FOREST-r11/report.md`, commit `a02d0aa02a8685d273da75c54cc54854188e4932`, blob `6df1229503af74c508d9d3e0339373355ccdf074`.

Consumed exact lead handoff `account01-B01-20260922T030948Z-v3.md`, blob `e02a4281a67d992d06d7c2c70586efa656353cab`, and named OTHER-account partner `account04-B02-20260922T030824Z.md`, blob `c5776f4ffec3033953ce460620bbf7f2e170aaad`.

## New exact unrooting representation

Order the marked edges `e<f<others`. Crapo activity intervals imply every acyclic set is uniquely `B\D`, where `B` is a graphic-matroid basis (maximal spanning forest) and `D subseteq IA(B)`. Therefore the actual uniform unrooted forest law is exactly:

1. choose `B` with mass proportional to `2^{i(B)}`;
2. independently delete each internally active basis edge with probability `1/2`.

This includes disconnected graphs, isolated vertices and every forest size.

Let

`W_ab=sum_{B:1_{e in B}=a,1_{f in B}=b} 2^{i(B)}`

and

`Q=sum 2^{i(B)}` over bases with `f in B`, `e notin B`, and `B-f+e` again a basis.

Then exactly

`Z=W00+W10+W01+W11`,
`2Z_e=W10+W11`,
`2Z_f=W01+W11+Q`,
`4Z_ef=W11`,

hence

**`4 Delta = W10 W01 - W00 W11 + Q(W10+W11)`**.

Equivalently under the activity-weighted basis law `mu`, the original target is exactly

**`P_mu(f|e)-P_mu(f) <= mu(A_f(e))`**.

So a direct coupling has two indispensable positive channels: `W10 W01` and the exchange reservoir `Q(W10+W11)`.

## Exact application of account04/B02

On its disjoint-edge `K5` witness, the new activity calculation gives

`(W00,W10,W01,W11,Q)=(49,70,56,116,14)`

and `(Z,Z_e,Z_f,Z_ef)=(291,93,93,29)`. Thus

`4 Delta=3920-5684+2604=840`, so `Delta=210`.

The activity reservoir is exactly `Q=14`, matching the partner's `q=14`. Its channel alone contributes only `2604<5684`, so the ordinary cross channel is genuinely required, exactly agreeing with the partner's q-only no-go.

An exhaustive exact checker verified the activity formulas and two-channel identity for all **1,074** simple labelled graphs on 2--5 vertices with at least two edges and all **11,766** marked pairs, including disconnected graphs, with zero failures. Checker SHA-256 `2414d57e875770329d23aedcf81b17be938153b479ae51c99cca5f083422727f`; output SHA-256 `24a77ebc454ddacf26199575903ae60fc5d133c1d2023c93c9d3e3f07ecc13df`.

## Rooted determinant mixture refuted

For the standard matrix-forest kernel

`det(L(y)+diag(x)) = sum_F y^F product_C(sum_{v in C}x_v)`,

no finite linear mixture over root-weight vectors `x` can equal the uniform unrooted forest polynomial of `K_n` for any `n>=4`, even allowing signed mixtures with the needed moments. Symmetrize any alleged mixture. For a forest with `k` component sizes `(s_1,...,s_k)`, its averaged coefficient is `(product s_j)m_k`, where `m_k` is the common squarefree k-coordinate moment. For `k=2`, partitions `1+(n-1)` and `2+(n-2)` require simultaneously `(n-1)m_2=1=2(n-2)m_2`, impossible for `n>=4`. On `K4`, this is `3m_2=1=4m_2`.

Thus ordinary randomization of diagonal root weights cannot perform the required unrooting. A determinant/integral route must add genuinely nonlocal/component-shape information. Exact symbolic `K4` determinant checker SHA-256 `8b7f999d6e9470bf2091cb10f42cc71287e8623565e0cd6cd35e41adc246662f`; output SHA-256 `8183753761e0ed905243bbc618449eff1da85c3a61244339b253d20368ce96eb`.

Next recipients: lead `account01/B01`, direct-coupling workers `account01/B02` and `account01/B03`. If pursuing the direct route, the exact remaining inequality is

`W10 W01 + Q(W10+W11) >= W00 W11`.

Neither the Q channel nor an ordinary randomized rooted-determinant kernel should be pursued alone.
