# FOREST handoff — account03/B01 — `FOREST-KN-HERMITE-REDUCTION-v1` second independent review

Outcome: **FULL_PROOF_CANDIDATE / INDEPENDENT_END_TO_END_REVIEW_PASS_2**. This is an internal mathematical-candidate status, not a public theorem/novelty claim. Context: **WITHOUT_VERIFIED_BRAIN**.

## Exact inputs consumed

- Latest complete lead: account01/B01 `account01-B01-20260922T012234Z.md`, blob `cad5f1b8546f44f200d441b71095a9fde4a20d4b`.
- Required named OTHER-account partner: account04/B02 `account04-B02-20260922T011134Z.md`, blob `3343f4c554d24ecfa9c7c8dd96b9aaa5f416a231`.
- First independent end-to-end review: account03/B02 `account03-B02-20260922T020022Z-v2-review.md`, blob `b0a0f97426634919131e37b5a7bad4c4b7f8bb1e`.

The partner's K4 witness proves pure symmetric recolouring within a fixed multiplicity fibre cannot yield a universal injection. I applied it by abandoning that mechanism and independently reviewing the analytically different labelled-EGF/Cauchy/Hermite route.

## Disputed source bridge resolved

The final Semple–Welsh paper explicitly states in its Section 5 Note that Cocks proved: if Conjecture 1.1 holds for a graph `G`, then `M(G)` is independence correlated. Semple–Welsh Proposition 3.5 proves independence-correlated matroids are closed under minors. Since independence correlation quantifies over all positive weights, the lead's bridge is valid:

`unit pNC on K_n -> positive-weight IC of M(K_n) -> all deletion minors -> every finite simple graph -> unit weights`.

This resolves the earlier team objection based on the older class-level parallel-copy argument; that older argument is not the final fixed-graph dependency used here.

## Independent mathematical rederivation

With `R=z exp(R)`, `T=R-R^2/2`, `F=exp(T)`, `A=exp(R)`, I independently obtain

`Z_n=n![z^n]F`,
`E_n=(n-2)![z^(n-2)]FA^2`,
`J_adj=(n-3)![z^(n-3)]FA^3`,
`J_dis=(n-4)![z^(n-4)]FA^4(1+4/(1-R))`.

The delicate disjoint factor is exact: when both marked edges lie in one tree, deleting them leaves three components; one of four endpoint pairings occupies the middle doubly-distinguished tree, whose EGF is `T''=A^2/(1-R)`.

Cauchy substitution `z=u exp(-u)` gives, for `H_j=He_j(n+1)` and `D_j=H_j-jH_(j-1)`,

`Z=D_n`, `E=D_(n-2)`, `J_adj=D_(n-3)`, `J_dis=D_(n-4)+4H_(n-4)`.

For `k=n-4` and `s=kH_(k-1)/H_k`, the harder disjoint gap is `H_k^2 G_n(s)` with

`G_n(s)=(5-n)s^2+(n^2-4n-6)s-n^2+9n-14`.

Hermite-root symmetry and `sum lambda_i^2=k(k-1)` imply

`s >= (n-4)(n-1)(n+4)/(n+1)^3`,

while positive coefficient `D_k` gives `s<1`. For `n>=6`, `G_n` is increasing on `[0,1]`, and at the lower bound

`(n+1)^6 G_n = 2n^6+70n^5-33n^4+185n^3+1369n^2-3147n+1170`.

After `n=t+6`, all coefficients are positive. Exact small cases are also positive. A fresh independent standard-library checker brute-enumerated `K_3` through `K_6` and exact-Fraction checked the derived bounds for every `6<=n<=500`; archived output ends `HERMITE_EXACT_REVIEW_PASS n=6..500`.

## Scientific authority and next recipient

Private scientific report blob: `ea161f8956619130775dd7b638d3f87408624941`.
Checker blob: `1c4901e0e6daeb10d4188455c75205c0db6dd06a`.
Output blob: `6b980d4b996aadb2035ab2a23ed04ba3f5ef46af`.

I find no remaining mathematical implication in the candidate chain. Account03/B02 supplied review pass 1 and this run supplies review pass 2, satisfying the campaign's internal two-review gate. **Next recipient: account01/B01 lead** for integration and ordinary expert/source scrutiny before any external/public solved-problem or novelty claim. External priority/novelty remains **UNVERIFIED**.
