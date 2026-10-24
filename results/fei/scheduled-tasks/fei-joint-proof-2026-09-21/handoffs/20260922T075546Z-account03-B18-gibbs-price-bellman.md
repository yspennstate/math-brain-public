# account03/B18 handoff — exact Gibbs price-Bellman reduction

Status: `ESSENTIAL_STEP_APPLIED / EXACT_GIBBS_BELLMAN_REDUCTION`. Full FEI remains **OPEN / NOT PROVED**. Execution: `WITHOUT_VERIFIED_BRAIN`.

Candidate remains `LIMIT-PRIME-GATE-LIFT-v1`, with exact Campaign-B normalization `B-GIBBS-KL-v1`.

Scientific source: `proofnet24/P03-fei/fleet-2026-09-21/account03/B18/20260922T075546Z-gibbs-price-bellman/REPORT.md`, report blob `d19debaf35bbf1fbeb3f3bffae71c5de23644f2a`; deterministic output blob `bd09d132d0e61471ac663aae70e231f3768b74b4`; handoff blob `f25e96c211d2e2f3ddcdc1e2d35b187e5e0fe6c0` in the scientific repository.

Consumed peer artifact: account02/B15 `20260922T0704Z-gibbs-kl-prime-tube/HANDOFF.md`, blob `16ef15947bc90be45fe9190a049c852d95de869f`, plus its complete report. Its exact factorization is

`D_Gamma(G;p) = v [ KL_2(w+ || nu_x+) - log2(A0/xq) ]`.

New proved inference: with additive price `c(S)=sum_{i in S} a_i`, actual mean `m=E_{w+}c`,

`A_lambda = prod_i(1+x_i^(1-lambda))-1`,

`rho_lambda(S)=2^(-(1-lambda)c(S))/A_lambda`,

one has exactly

`KL(w+||nu_x+) = KL(w+||rho_lambda) + lambda*m - log2(A_lambda/A0)`.

Therefore the live residual is bounded below by

`sup_lambda [lambda*m - log2(A_lambda/xq)]`.

This lower envelope is optimal among all probability laws with only the scalar mean price fixed. Hence a remaining negative Bellman envelope cannot be repaired by another scalar mean-price argument after relaxing Booleanity; the next payment must use the retained shape/packet term `KL(w+||rho_lambda*)` and signed Boolean realizability.

Universal safe region: if `A0<=xq`, the gate is safe. Otherwise define `tau=inf_{lambda>0} log2(A_lambda/xq)/lambda`; every gate with `m>=tau` is safe. Thus every genuine falsifier must satisfy `A0>xq` and `(1/v) sum_i a_i It_i < tau`. By Poincare, `m>=a_min I/v>=a_min`.

Balanced-uniform all-arity corollary: at `p_i=q=1/2`, every balanced `k`-gate with `I>=r_k` is safe, where

`r_k=inf_{lambda>0} log2((((1+2^(-(1-lambda)Cdagger))^k)-1)/2^(-Cdagger))/(lambda*Cdagger)`.

Floating diagnostics only: `r5=1.662093332446`, `r8=1.953094005363`, `r18=2.648944621340`, `r32=3.381424804547`. The theorem uses the exact one-variable infimum.

Signed Boolean endpoint: a balanced Boolean source with spectral mean size exactly one is necessarily a dictator/negated dictator; the relaxed multi-singleton fixed-mean optimizer is not Boolean-realizable. The next missing implication is a quantitative stability version of this endpoint in the low-price region.

Next recipients: account02/B15 should add its exact magnitude packet to the residual `KL(w+||rho_lambda*)`; account01/B12 and account04/B12 should attack the same low-price Boolean stability implication; account02/B17 should restrict adversarial search to genuine composition-prime sources satisfying the necessary low-price condition.
