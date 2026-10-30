# B15 — balanced two-point mutation barrier around the explicit prime FEI gate

**Outcome:** `AUXILIARY_ONLY` for full FEI, with a new source-exact local extremality theorem and a quantitative negative-entropy decomposition.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED.**  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository mathematical sources were retrieved directly; no authenticated cognitive-brain receiver/context was consumed.

## 0. Live target and exact peer result consumed

The current owner convergence order sends every FEI worker to the all-gate formulation
\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i {\rm It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u).
\tag{G}
\]
On the balanced uniform slice this reduces exactly to
\[
H(G)\le \Gamma(1/2)\,[I(G)-1],
\tag{0.1}
\]
so
\[
R(G):=\frac{H(G)}{I(G)-1}
\tag{0.2}
\]
is the center obstruction.

The exact named other-account result consumed and applied is fleet04/B15,
`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B15/20260922T020955Z-adaptive-depth-shared-core-ceiling/REPORT.md`.
It proves for the source-bound nine-host shared-core transform that **every adaptive integer self-composition depth schedule** stays below
\[
M_+
=
6.52185121301287772365150440023918196647146413881.
\tag{0.3}
\]
The proof is not a finite extrapolation: its exact recurrence is a convex interpolation with scalar target
\(K(c^d)/(133/128)\), and a rigorous concavity maximization bounds that target on the full reachable interval.
Thus continuing the old shared-core depth schedule is analytically exhausted; a useful construction attack must change mechanism.

I therefore changed mechanism and attacked a different possibility: can the explicit small composition-prime gate be locally mutated, while preserving balance, into a larger balanced-center obstruction?

## 1. Source-exact prime gate

The seed is the explicit balanced monotone composition-prime ten-input gate from the source chain
fleet03/B12 -> fleet01/B16.  Its truth-table SHA-256 is
`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`.

The source checker gives
\[
I(G)=\frac{257}{128},
\qquad
H(G)=6.509836127588151\ldots,
\]
hence
\[
R(G)=6.459372281637855\ldots .
\tag{1.1}
\]
It is already known to be composition-prime; that fact is not re-audited here.

A balance-preserving Hamming-distance-two mutation is obtained by choosing one truth-table point with value \(+1\), one with value \(-1\), and swapping the two signs. Since the gate is balanced, there are exactly
\[
512\cdot512=262144
\tag{1.2}
\]
such mutations.

## 2. New theorem — strict local maximum under every balanced two-point swap

### Theorem 2.1

For every balance-preserving two-point swap \(G'\) of this ten-input gate,
\[
\boxed{
R(G')<R(G).
}
\tag{2.1}
\]
More quantitatively, the committed checker proves
\[
R(G)>6.459372280645606
\tag{2.2}
\]
while
\[
\max_{G'\sim G}R(G')
<
6.438915856460716.
\tag{2.3}
\]
Therefore the certified local gap is
\[
\boxed{
R(G)-\max_{G'\sim G}R(G')
>0.020456424184890.
}
\tag{2.4}
\]

There are 64 symmetry-related closest neighbors at the unpadded numerical value
\[
R(G')=6.438915855476099\ldots .
\tag{2.5}
\]
One representative has
\[
I(G')=2.015625,
\qquad
H(G')=6.539523915717913\ldots .
\tag{2.6}
\]

### Certificate

The checker reconstructs the external 18-bit source from its published-source hash, takes the exact ten-coordinate restriction used by the source witness, checks the witness hash, computes its integer Walsh transform, and enumerates all 262144 balanced swaps.

For every possible Walsh numerator magnitude \(a\), the entropy atom
\[
\phi(a^2/2^{20})
=
-\frac{a^2}{2^{20}}\log_2\frac{a^2}{2^{20}}
\]
is enclosed by rational atanh-series bounds. These are converted outward by one floating ulp. The scan then uses a deliberately much larger `1e-9` entropy pad; with at most 1024 nonnegative atoms this dominates the IEEE summation error by orders of magnitude. Influence numerators are accumulated exactly in signed 64-bit integers. The final gap in (2.4) is over \(2\times10^{-2}\), so the interval decision is extremely non-marginal.

This is a local finite theorem, not an exhaustive search over ten-input Boolean gates.

## 3. The requested negative entropy term: exact JS refund

For a source spectral law \(p_S=\widehat G(S)^2\), a mutated law \(q_S=\widehat {G'}(S)^2\), and midpoint
\[
m=\frac{p+q}{2},
\]
the entropy difference has the exact identity
\[
\boxed{
H(q)-H(p)
=
2\,[H(m)-H(p)]
-
2\,{\rm JS}(p,q),
}
\tag{3.1}
\]
where
\[
{\rm JS}(p,q)
=
H(m)-\frac{H(p)+H(q)}2
\ge0.
\tag{3.2}
\]
Thus \(-2{\rm JS}\) is a literal negative entropy term: it is the refund lost by replacing the true endpoint entropy change by the midpoint mixing gain.

For a closest neighbor from Theorem 2.1,
\[
2[H(m)-H(p)]
=
0.039341492692294\ldots,
\tag{3.3}
\]
\[
2{\rm JS}(p,q)
=
0.009653704562533\ldots,
\tag{3.4}
\]
and hence
\[
H(q)-H(p)
=
0.029687788129761\ldots .
\tag{3.5}
\]

At the source ratio \(R(G)\), the exact influence increment is
\[
\Delta I=\frac1{128},
\]
so its available excess-influence payment is
\[
R(G)\Delta I
=
0.050463845950296\ldots .
\tag{3.6}
\]
Consequently the local objective drops by
\[
R(G)\Delta I-\Delta H
=
0.020776057820534\ldots .
\tag{3.7}
\]

The important quantitative conclusion is slightly negative for Campaign B: **the JS credit is real but is not the decisive term in this particular local neighborhood**. Even before subtracting the \(2{\rm JS}\) refund,
\[
R(G)\Delta I-2[H(m)-H(p)]
=
0.011122353257999\ldots>0.
\tag{3.8}
\]
So the hoped-for negative entropy correction is not where this explicit small prime gate is close to breaking the balanced-center inequality. Its nearest balanced mutations are already paid by influence before the refund is used.

## 4. Consequence for the common proof programme

This rules out a natural replacement search mechanism after the shared-core depth family was closed:

> Starting from the explicit ten-input composition-prime obstruction, a single balance-preserving two-point truth-table mutation cannot raise the balanced center requirement at all.

The result also explains why ordinary one-swap hill climbing around this witness stalls: the witness is an isolated local maximum of \(H/(I-1)\) with a sizeable certified gap. To find a new center obstruction above the current shared-core ceiling, the construction must therefore make a nonlocal truth-table move, alter the shared-coordinate geometry, or exploit a genuinely biased prime-gate obstruction.

It does **not** prove that the current center cap \(M_+\) is universal, does not control nonuniform product biases, and does not prove the all-gate inequality (G).

## 5. Exact old/new missing implications

**Old missing implication after the adaptive-depth peer theorem.** Either prove the all-prime/all-bias inequality above the complete source-bound shared-core obstruction, or produce a genuinely different gate/bias obstruction.

**Attack executed here.** Change mechanism from shared-core iteration to all balance-preserving Hamming-distance-two mutations of the explicit small composition-prime witness, retaining exact source signs and the negative Jensen-Shannon entropy credit.

**New proved inference.** Every one of the 262144 balanced two-point mutations has strictly smaller \(H/(I-1)\); the certified gap is \(>0.02045642418\). The closest neighbor's entropy increase admits the exact negative-credit decomposition (3.1), with \(2{\rm JS}=0.00965370456\ldots\), but that refund is not essential for local stability.

**New first missing implication.** A useful successor must now either:
1. control (G) for all composition-prime gates and all product biases at a center above the known shared-core floor/ceiling, or
2. find a **nonlocal / different-geometry / biased** prime obstruction. Repeating one-swap mutations of this ten-input witness is mathematically exhausted.

**Classification:** `AUXILIARY_ONLY`.  
**Full FEI:** `OPEN / NOT PROVED`.

## 6. Scope and privacy

Only source-bound mathematics, public/source hashes, and sanitized provenance are recorded. No credentials, account identifiers, scheduler identifiers, machine paths, private transcripts, email/Drive actions, permission changes, public-posting instructions, workflows, or paid/remote-compute instructions are included.
