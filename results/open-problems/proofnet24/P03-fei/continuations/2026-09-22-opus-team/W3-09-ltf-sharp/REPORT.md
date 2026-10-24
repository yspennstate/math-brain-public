# FEI with the sharp constant 4 for AND/OR chains

Group W3-09 was stopped on 23 September 2026 before writing its report. The interval certificate (`code/cert_chains.py`, `logs/cert_chains.log`) is theirs. The derivation below was put together by the coordinator from the certificate's definitions. It was checked against exact Walsh sums on 300 random chains of length up to 14 (largest discrepancy 1.7e−13), and the certificate was re-run with identical output.

## Statement

An AND/OR chain on m variables is f_1 = x_1 followed by f_{j+1} = x_{j+1} ∧ f_j or f_{j+1} = x_{j+1} ∨ f_j. Every such function is a linear threshold function. Write F = (−1)^f, W(S) = F̂(S)^2, H(f) = Σ_S W(S) log2(1/W(S)) (the empty set included) and I(f) = Σ_S |S| W(S).

Theorem. Every AND/OR chain satisfies H(f) ≤ 4 I(f). The constant is sharp: for AND_m, H/I = 4(m−1)/m + o(1) → 4.

## The defect of one step

Let p = Pr[f = 1] and f' = x ∧ f with x a new variable. Then F̂'(∅) = 1 − p and W'({x}) = p^2, and for every S ≠ ∅, W'(S) = W'(S ∪ {x}) = W(S)/4. Hence

  I(f') = I(f)/2 + p,
  H(f') = H(f)/2 − φ((1−2p)^2)/2 + 4p(1−p) + φ(p^2) + φ((1−p)^2),

where φ(w) = w log2(1/w). For the defect D = 4I − H this gives D(f') = D(f)/2 + ε(p), with

  ε(p) = 4p^2 − φ(p^2) − φ((1−p)^2) + φ((1−2p)^2)/2.

In the certificate's notation, ε(p) = 4p^2 + (2/ln 2)[g(p) + g(1−p)] − g(|1−2p|)/ln 2 with g(x) = x^2 ln x. An OR step is the AND step applied to the complements, so D(f') = D(f)/2 + ε(1−p). In both cases the argument is 2 min(p', 1−p'), where p' = Pr[f' = 1]. Writing ψ(u) = ε(2 min(u, 1−u)), every step reads D(f') = D(f)/2 + ψ(p').

## Unrolling

A dictator has D = 4 = ψ(1/2). Going backwards along the chain, the probabilities are p_j = T(p_{j+1}) with T(u) = 2u mod 1. So a chain with P = Pr[f = 1] has

  D(f) = Σ_{k ≥ 0} 2^{−k} ψ(T^k P),

where the sum is finite because T^{m−1}P = 1/2, T^m P = 0 and ψ(0) = 0. Call the right-hand side D(s) for any s ∈ [0, 1]. Because ψ(0) = ψ(1) = 0, each ψ∘T^k is continuous on the circle, and the series converges uniformly, so D is continuous. Also D(1 − s) = D(s). The theorem is therefore equivalent to D ≥ 0 on [0, 1]. This D is a Takagi-type function.

## Three facts

1. ε(1/2) = 0 and ε < 0 on (0, 1/2). On (0, 1/64] this follows from the expansion ε(p) = p^2(4 − 3/ln 2 + 2 log2 p) + (2/ln 2) Σ_{n≥3} (2^n − 2) p^n/(n(n−1)(n−2)). The first part is at most −12.3 p^2, and the series is at most (2/ln 2)(2p)^3/(6(1−2p)) ≤ 0.07 p^2. The expansion was checked against the closed form to 15 digits. On [1/64, 0.45] the certificate gives ε ≤ −0.0029984 by interval arithmetic. On [0.45, 1/2] it gives ε' ≥ 2.0951, and together with ε(1/2) = 0 this shows ε < 0 there.

2. A run of AND steps. Take s ∈ (0, 1/2) not dyadic and write s = 2^{−l} u with l ≥ 1 and u ∈ (1/2, 1). For k < l, T^k s = 2^{k−l} u < 1/2, so

  D(s) = 2^{−l} [ 2 S_l(u) + D(u) ],   S_l(u) = Σ_{i=0}^{l−1} 2^i ε(2^{−i} u).

For i ≥ 1 the argument 2^{−i}u lies in (0, 1/2), so by fact 1 the partial sums S_l(u) decrease in l. Hence S_l(u) ≥ E(u) := Σ_{i≥0} 2^i ε(2^{−i}u), which converges because ε(p) = O(p^2 log(1/p)).

3. The certificate: Φ_K(u) = 2E(u) + Σ_{k<K} 2^{−k} ψ(T^k u) ≥ c = 0.020792 for every u ∈ [1/2, 1), with K = 8. This was checked on 276 dyadic cells with mpmath interval arithmetic and outward rounding; the minimum is on the cell [0.6504, 0.6523]. The small-p part of E uses the series of fact 1 truncated at n = 25 with an explicit remainder bound, and the l ≥ L tail of E uses 2^l |ε(2^{−l}s)| ≤ 2^{−l}(2l + 4).

## Proof of the theorem

Let M = min over [0, 1] of D; the minimum exists because D is continuous. Take s ∈ (0, 1/2) not dyadic, written as in fact 2. Since D(u) = Σ_{k<K} 2^{−k} ψ(T^k u) + 2^{−K} D(T^K u) ≥ Σ_{k<K} 2^{−k} ψ(T^k u) + 2^{−K} M, facts 2 and 3 give

  D(s) ≥ 2^{−l} [ 2E(u) + D(u) ] ≥ 2^{−l} [ c + 2^{−K} M ] ≥ min( 0, (c + 2^{−K} M)/2 ).

By the symmetry D(1 − s) = D(s), the same bound holds at every non-dyadic point of (1/2, 1). By continuity it holds everywhere, so M ≥ min(0, (c + 2^{−K}M)/2). If M < 0, this gives M (1 − 2^{−K−1}) ≥ c/2 > 0, which is a contradiction. So D ≥ 0 on [0, 1], and in particular D(f) ≥ 0 for every chain. ∎

## Remarks

- Sharpness comes from long runs of one gate. For AND_m, D = 2^{1−m}(2 S_{m−1}(1) + 0) and I = m 2^{1−m}, so D/I → 0. Chains whose probability sits just above a dyadic point also approach 4: H/I = 3.99515 at t = 1e−8 (`logs/chains_defect3.log`).
- Scope. A chain adds one fresh variable per gate, so this is a statement about read-once caterpillar formulas. It gives the constant 4 where the general read-once theorem gives 6.4573 and F5's LTF theorem gives 14.2142. The W2-A referee's searches over linear threshold functions (n ≤ 22, structured families and annealing) never exceeded H/I = 3.981. That makes 4 the natural conjecture for every linear threshold function. The method here uses the one-variable recursion and does not extend to general threshold functions without a new idea.
- The chains are exactly the threshold functions with weights 1, 2, 4, ..., 2^(m-1) (lexicographic order), so the theorem covers that family of linear threshold functions and no other.
- XOR and NOT steps may be mixed in. Negating the output or a variable changes neither H nor I. For f' = x ⊕ f, W'(S ∪ {x}) = W(S), so H' = H, I' = I + 1, D' = D + 4, and f' is balanced. Every later AND/OR step maps D to D/2 + ψ(p'), which is increasing in D. So the defect of the final function is at least the defect computed from a dictator start, and H ≤ 4I holds for every chain built from AND, OR, XOR and NOT with one fresh variable per step.
- The one-step identity is exact and holds for any f, not only for chains: D(x ∧ f) = D(f)/2 + ε(Pr[f = 1]). Its sign structure (ε < 0 below 1/2, ε(1) = 4) is what a longer argument for threshold functions would have to control.

## Files

`code/cert_chains.py` (the certificate), `logs/cert_chains.log` (its output), `logs/chains_defect*.log` and `logs/chains_takagi.log` (numerics). The coordinator's check of the unrolled formula against exact Walsh sums is `audit/chain_check.py` in the team folder.
