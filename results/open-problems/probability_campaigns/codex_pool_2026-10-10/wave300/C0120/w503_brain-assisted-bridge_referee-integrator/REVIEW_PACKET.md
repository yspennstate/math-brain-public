# C0120 referee packet — 2026-10-10

## Pinned inputs

- w501/LEMMAS.md SHA-256 `29e531611d35eaef4015da7c523212e0d5eab956641e479a73887ff903c2ae9a`
- w501/STATEMENT_ONLY.md SHA-256 `dae3f4f7360ee48896b928a2013fb49d66740c3516decc75f1d3da89021b564f`
- w502/ATTEMPT.md SHA-256 `6568afc36273568f6356b2e1dcf04e8e0ef8d74cb4151e3a67e1ec855afd5581`
- w502/CLAIMS.jsonl SHA-256 `ac4f5626327faee18d3a13372c6472de6a8b4d848b5f27f3e6acb1b44c19072f`
- Chatterjee arXiv:0810.4221v2 PDF SHA-256 `17f13a871b84417a83514995c70d2ebf49f5464faeac9dd95e8c4d823b600658` (586944 bytes fetched from `https://arxiv.org/pdf/0810.4221v2`).

## Exact source and status

**FIX** the C0120 intake and live math-brain C0120 concept's source attribution. Section 8 defines independent standard Gaussian weights on the nonnegative quadrant and the *maximum path sum* M_n over n-vertex up/right paths from the origin with free endpoint. Theorem 8.1 proves Var(M_n) <= C n/log n. Section 12(3) asks to improve the fluctuation exponent beyond that logarithmic correction. The current intake/live node instead says Var(log Z_n) in general dimension. The latter is a related finite-temperature problem, with different hypotheses, and is not the cited question. A power bound Var(M_n) <= C n^(1-epsilon) is a precise proposed interpretation, not the source's verbatim words. The dated ranking and local solved register do not certify present openness. Current status remains UNKNOWN.

## Independent mathematical check

For the source model, distinct path incidence vectors imply almost-sure uniqueness. Let f_v(g)=1{v belongs to the maximum path}, and couple g^t=e^(-t)g+sqrt(1-e^(-2t))g'. The maximum's weak gradient is (f_v)_v almost everywhere, with squared norm n. Gaussian covariance interpolation gives Var(M_n)=integral_0^infinity e^(-t) Q_n(t)dt, where Q_n(t)=sum_v E[f_v(g)f_v(g^t)]. Self-adjoint OU semigroup gives each term as ||P_(t/2)f_v||_2^2, hence Q_n is nonincreasing, 0<=Q_n<=n. For h>0, integration on [0,h] and [h,infinity) yields (1-e^(-h))Q_n(h)<=Var(M_n)<=n(1-e^(-h))+e^(-h)Q_n(h). Thus Q_n(n^(-a))<=K n^(1-b) for fixed a,b>0 would imply a variance power saving with exponent min(a,b). This is a conditional reduction. The overlap premise is unproved and is the hardest open piece.

## Scoped peer verdicts

| Claim | Verdict | Reproduction and limit |
|---|---|---|
| w501 L1; w502 L02 | KEEP | Independent interpolation and split above. The OU time exponent must not be confused with independent-noise amplitude; amplitude is asymptotic to sqrt(2t). No polynomial overlap estimate was supplied. |
| w501 L2 | KEEP | Gaussian hypercontractivity for P_(t/2) has p=1+e^(-t). Since f_v is an indicator, ||f_v||_p^2=q_v^(2/p)=q_v^(1+tanh(t/2)). This uses Gaussian product law, not independence of site-selection events. |
| w501 L3 | KEEP, scoped | At layer k there are k+1 sites with marginal masses summing to one. Jensen gives sum q_v^(1+a)>= (k+1)^(-a), hence B_n(t)>=n^(1-a). With u=e^(-t), a=(1-u)/(1+u)<=1-u, so integral e^(-t)B_n(t)dt >= (n-1)/log n. At t=n^(-alpha), B_n(t)/n tends to one. This lower-bounds the *upper-bound certificate*, never actual overlap or variance. It only kills the direct unweighted one-site envelope. |
| w501 L4 | KEEP, conditional | If both Var(F_n)=n^(2chi+o(1)) and chi=2xi-1 hold, the variance exponent is 4xi-2. xi=4/5 gives 6/5 despite xi<1. A strict power saving needs xi<3/4, with endpoint inequality as written in L4. The scaling relation is not proved here for the source model. |
| w502 L01 | KEEP | For fixed q,delta>0, n/(log n)^q divided by n^(1-delta) tends to infinity. This refutes an implication from a logarithmic *bound* to a power *bound*, not a claim about actual variance. |
| w502 S01 | KEEP | Checked directly against source Section 8 and Section 12(3), and against intake problems.jsonl:120. |
| w502 L03 | KEEP | 0<=F_beta-M<=A=log(|P|)/beta. With D in [0,A], Var(D)<=A^2/4. Reverse centered-L2 triangle inequality gives a standard-deviation error <=A/2. Uniform control along beta(n) growing at least n^((1+epsilon)/2) is a sufficient condition for this comparison to transfer a variance power bound; no fixed-beta theorem supplies it automatically. |
| w502 L04 | KEEP as wording correction | On the uniform 3-cube, f=x_1 1{x_2=x_3=1} has Delta_1 f=x_1 1_A, ||Delta_1 f||_1=1/4 and ||Delta_1 f||_2=1/2. The Talagrand denominator is 1+log 2, so a rare indicator-like derivative *does* gain. This refutes only the explanatory sentence of live card `claim_19af561bcf040b56cc9b3aa80d52d5dd62e1e00c1b7ecb97b574cbacb19b5603`; the displayed inequality is not refuted. |

**Parent verdict:** no solved C0120 claim. Needed: Q_n(n^(-a)) <= C n^(1-b) for fixed a,b>0 in the *source's* Gaussian free-endpoint model, or another valid route yielding a power variance bound. Source/hash checks and small n computations do not prove that premise. Served-model identity and a different-model final review remain unverified.

## Brain and integration

The live exported C0120 concept `claim_2b6b7c1da300a8ed1c28367cabd584f2c02769a03a64ed519cf081b1af04693d` repeats the intake's incorrect source scope. The live attempt card `claim_7891e285a213a1ead9b1e54b02b29177a06d86c6f3df76b6447ca94dbe6add7f` also imports the finite-temperature observable and asserts an inadequate xi<1 threshold. Route the source correction to the integrator for a reviewed replacement or quarantine before treating either card as source-faithful. A draft bundle may add the exact problem and scoped barrier; it does not remove or validate the old cards by itself.

NEXT: Validate the small draft correction bundle and give the integrator the exact live-card IDs and this pinned packet.
