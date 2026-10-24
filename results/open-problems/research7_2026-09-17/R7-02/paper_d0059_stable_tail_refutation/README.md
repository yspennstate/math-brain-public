# D0059 source-scope package — stable-tail refutation of literal Conjecture 1.6(b)

Model/reasoning telemetry for the producing run: **UNVERIFIED**. GPT-6 / maximum reasoning was requested by the owner prompt, but no authenticated binding model/effort selector or telemetry was exposed.

## Source and exact scope

Outside source: Xinxing Chen, Bernard Derrida, Yueyun Hu, Mikhail Lifshits and Zhan Shi, *A max-type recursive model: some properties and open questions*, arXiv:1705.04787v2 / Springer Proc. Math. Stat. 300 (2019). The repository canonical target is `D0059`; the source locator is Conjecture 4 in the PDF (Conjecture 1.6 in the current arXiv HTML), especially part (b), equation (1.6).

For fixed integer `m >= 2`, the source studies

`X_{n+1}=(X_n^(1)+...+X_n^(m)-1)^+`

under the displayed critical hypothesis

`(m-1) E[X_0 m^{X_0}] = E[m^{X_0}] < infinity`.

Literal part (b) predicts

`E[m^{X_n}]-1 ~ 2/((m-1)n)`.

Immediately after the conjecture, the source notes that additional integrability conditions, such as `E[X_0^3 m^{X_0}]<infinity`, may be necessary. This package therefore makes a deliberately narrow statement: **the displayed literal hypothesis alone is insufficient**. It does not claim to refute the repaired finite-third-weighted-moment version.

## Result

For every fixed `m >= 2` and every `alpha in (2,4)`, an explicit critical probability law is constructed with

`P(X_0=k) ~ c m^{-k} k^{-alpha}`.

It satisfies the literal source condition `E[X_0 m^{X_0}]<infinity`, but violates Conjecture 1.6(b). The contradiction uses Theorem 1.1 of Xinxing Chen and Zhan Shi, *The stable Derrida--Retaux system at criticality*, arXiv:2006.06140 (2020), which proves for this stable critical regime that

`prod_{i=0}^{n-1} E[m^{X_i}]^{m-1} = Theta(n^{alpha-2})`.

If the source endpoint asymptotic were true, taking logarithms would instead force the same product to be `n^{2+o(1)}`. Since `alpha-2<2`, both statements cannot hold.

This is best viewed as an elementary **corollary of the published Chen--Shi stable-regime theorem**, plus an explicit normalization/criticality construction. No novelty claim is made from the fact that a bounded literature search did not locate this exact corollary stated in these words.

## Explicit critical law

Let

`A = sum_{k>=2} m^{-k} k^{-alpha}`,

`B = sum_{k>=2} (((m-1)k-1) k^{-alpha})`,

`b_1 = m(m-2)`, and `c = 1/(2(A+B))`.

Set

`p_k = c m^{-k} k^{-alpha}` for `k>=2`,

`p_1 = 1/(2(1+b_1))`,

`p_0 = b_1 p_1 + cB`.

Then all `p_k` are nonnegative and

`p_0+p_1+sum_{k>=2}p_k = (1+b_1)p_1+c(A+B)=1`.

Moreover the critical identity is equivalent to

`p_0 = sum_{k>=1} (((m-1)k-1)m^k) p_k`,

whose right-hand side is exactly `b_1p_1+cB=p_0`. Finally

`E[X_0m^{X_0}] < infinity`

because its tail is a constant multiple of `sum k^{1-alpha}`, while `E[X_0^3m^{X_0}]=infinity` for `alpha<4`. Thus the witness is inside the literal conjecture and outside the repaired finite-third-moment laboratory.

## What remains open / not claimed

1. This package does **not** prove either part of Conjecture 1.6 under the added condition `E[X_0^3m^{X_0}]<infinity`.
2. It does **not** establish publication novelty. The core asymptotic input is Chen--Shi 2020.
3. It does **not** satisfy the owner's independent-audit closure protocol yet. At package creation the required independent P26 audit and distinct OTHER-track audit are both missing (`0/2`).
4. The frozen R7-02 proof-count metric `C_D0059` remains `0/2`; the source verdict changes to `REFUTED` because the admission record explicitly treats a literal counterexample as a verdict change rather than an increment of the proof-count metric.

`main.tex` contains the self-contained source-scope argument and clearly identifies the imported theorem.