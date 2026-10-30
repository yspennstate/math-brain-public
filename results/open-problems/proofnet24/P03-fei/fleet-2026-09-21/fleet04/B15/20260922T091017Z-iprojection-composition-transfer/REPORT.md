# fleet04/B15 — exact I-projection KL composition transfer

**Run:** `20260922T091017Z-fleet04-B15-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / EXACT_KL_COMPOSITION_TRANSFER / PRIME_REMAINDER_LOCALIZED`  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 0. Exact predecessor and actual unpaid remainder

This run consumes the newest completed fleet02/B15 source-exact result

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`.

For a nonconstant Boolean gate `G` at interior product bias `p`, let `q=Pr[G=-1]`, `v=V_q`, let `P=w^+` be the actual biased squared spectral law conditioned on a nonempty Fourier set, and put

\[
r_i=P(i\in S)={\operatorname{It}_i(G;p)\over v}.
\]

For an arbitrary symmetric potential `Gamma`, write

\[
a_i={\Gamma(p_i)+h_2(V_{p_i})\over V_{p_i}},
\qquad
a_q={\Gamma(q)+h_2(v)\over v}.
\]

Fleet02/B15 proves that if `Q_r` is the maximum-entropy conditional-product law on nonempty subsets with the same coordinate marginals `r`, then

\[
K_{\rm occ}(P):=D_{\rm KL,2}(P\Vert Q_r)
=H_{\max}(r)-H(P)\ge0,
\]

and the exact normalized gate remainder is

\[
\boxed{
R_\Gamma(G;p)
=\sum_i r_i a_i-a_q-H(P)
=B_{\rm inf}^\Gamma(G;p)+K_{\rm occ}(G;p),
}
\tag{0.1}
\]

where

\[
B_{\rm inf}^\Gamma
=\sum_i r_i a_i-a_q-H_{\max}(r).
\]

The actual obligation is `R_Gamma>=0`; equivalently

\[
K_{\rm occ}\ge
\left[H_{\max}(r)+a_q-\sum_i r_i a_i\right]_+.
\tag{0.2}
\]

No valuation-tail term is substituted for `K_occ`. The older signed valuation reserve remains a distinct arithmetic currency. No packet integrality, positive-part replacement of a signed source identity, or credit-free product interpolation is used below.

A complementary fresh source is fleet03/B15

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T082654Z-js-packet-payment/REPORT.md`,

which proves the exact genuine-coordinate restriction packet decomposition and sharp all-bias payment

\[
\operatorname{JS}_s(U,V)\le \kappa(s)\operatorname{It}_i,
\]

while retaining the still-unpaid physical branch entropy. The theorem below attacks a different point: exact disjoint composition of the new irreducible KL credit itself.

## 1. The I-projection law recalled

For a marginal vector `r=(r_1,...,r_k)` on nonempty subsets, put `mu=sum r_i`. When `mu>1`, let `zeta in (0,1]` be the unique positive solution of

\[
1-\zeta=\prod_i(1-\zeta r_i).
\tag{1.1}
\]

Let independent Bernoulli coordinates have probabilities `zeta r_i` and condition on the vector being nonzero. The resulting law is `Q_r`. If `mu=1`, the law with those marginals is supported on singletons and is already unique. In all cases `Q_r` is the unique maximum-entropy law with the prescribed nonempty coordinate marginals.

## 2. Exact hierarchical composition theorem

Let

\[
F=G(f_1,\ldots,f_m)
\]

be a Boolean composition on pairwise disjoint physical coordinate blocks. Contract any constant child first; hence every displayed child is nonconstant. Let `q_i` be the output bias of `f_i` and take the outer biased Fourier expansion of `G` at `(q_1,...,q_m)`.

Let

- `P_0=w_G^+` be the outer nonempty spectral law on block subsets `T subseteq [m]`, `T != emptyset`;
- `alpha_i=P_0(i in T)`;
- `P_i=w_{f_i}^+` be child `i`'s nonempty physical spectral law;
- `r_{ij}=P_i(j in S_i)` for physical coordinate `j` inside block `i`.

The actual composite source factors exactly as

\[
\boxed{
P_F\bigl(T,(S_i)_{i\in T}\bigr)
=P_0(T)\prod_{i\in T}P_i(S_i).
}
\tag{2.1}
\]

Therefore the physical coordinate marginals of `P_F` are

\[
\boxed{s_{ij}=\alpha_i r_{ij}}
\tag{2.2}
\]

and its entropy is

\[
\boxed{
H(P_F)=H(P_0)+\sum_i\alpha_i H(P_i).
}
\tag{2.3}
\]

Let `Q_s` be the fleet02/B15 I-projection matching the global physical marginals `s`. Its independent pre-conditioning coordinate probabilities are `zeta s_{ij}`, where `zeta` is the global parameter solving (1.1). Define the induced block activation probabilities

\[
u_i=1-\prod_j(1-\zeta s_{ij}).
\tag{2.4}
\]

Then `Q_s` itself admits the hierarchy

\[
Q_s\bigl(T,(S_i)_{i\in T}\bigr)
=Q_A(T)\prod_{i\in T}Q_i^{(\zeta)}(S_i),
\tag{2.5}
\]

where `Q_A` is the nonempty conditional-product law with unconditioned block probabilities `u_i`, and `Q_i^(zeta)` is the conditional product law inside block `i` with unconditioned coordinate probabilities `zeta s_{ij}`.

### Theorem 2.1 — exact irreducible-KL composition law

For every such disjoint Boolean composition,

\[
\boxed{
K_{\rm occ}(F)
=K_{\rm occ}(G)
+\sum_i\alpha_i K_{\rm occ}(f_i)
+C_{\rm hier},
}
\tag{2.6}
\]

with the explicit nonnegative hierarchy credit

\[
\boxed{
C_{\rm hier}
=D(Q_\alpha\Vert Q_A)
+\sum_i\alpha_iD(Q_{r_i}\Vert Q_i^{(\zeta)})
\ge0.
}
\tag{2.7}
\]

Here `Q_alpha` is the maximum-entropy nonempty conditional-product law with block marginals `alpha`, and `Q_{r_i}` is the corresponding child I-projection.

Equivalently,

\[
\boxed{
C_{\rm hier}
=H_{\max}(s)-H_{\max}(\alpha)
-\sum_i\alpha_iH_{\max}(r_i)
\ge0.
}
\tag{2.8}
\]

### Proof

Apply the KL chain rule to the exact source hierarchy (2.1) and reference hierarchy (2.5):

\[
D(P_F\Vert Q_s)
=D(P_0\Vert Q_A)
+\sum_i\alpha_iD(P_i\Vert Q_i^{(\zeta)}).
\tag{2.9}
\]

Now use fleet02/B15's Pythagorean theorem separately on the outer law and each child law: for any conditional-product reference with the correct support,

\[
D(P_0\Vert Q_A)
=D(P_0\Vert Q_\alpha)+D(Q_\alpha\Vert Q_A),
\]

and

\[
D(P_i\Vert Q_i^{(\zeta)})
=D(P_i\Vert Q_{r_i})+D(Q_{r_i}\Vert Q_i^{(\zeta)}).
\]

Substitution into (2.9) is exactly (2.6)-(2.7). No KL term is discarded. Equation (2.8) follows either from `K_occ=Hmax-H` and (2.3), or because the hierarchical law built from `Q_alpha` and the `Q_{r_i}` has the global marginals `s`, while `Q_s` maximizes entropy among all laws with those marginals. `QED`.

Thus `K_occ` is superadditive under genuine disjoint Boolean composition, and the excess is an explicit relative-entropy credit rather than an unpriced interpolation error.

## 3. Exact transfer of the actual FEI remainder

The same source hierarchy gives an exact transfer for (0.1). The physical input-price contribution of `F` is

\[
\sum_{i,j}s_{ij}a_{ij}
=\sum_i\alpha_i\sum_jr_{ij}a_{ij}.
\]

Insert and subtract the child output prices `a_{q_i}`. Using (2.3), the child terms are exactly `R_Gamma(f_i)`, while the outer term is exactly `R_Gamma(G)` at child-output biases. Hence

\[
\boxed{
R_\Gamma(F)
=R_\Gamma(G)+\sum_i\alpha_iR_\Gamma(f_i).
}
\tag{3.1}
\]

This identity is source-exact and valid for arbitrary symmetric `Gamma`; degenerate constant blocks are removed before applying it and boundary cases follow by the corresponding limiting/contracted formulation.

Combining (2.6) with `R=B_inf+K_occ` yields the matching first-moment ledger

\[
\boxed{
B_{\rm inf}^\Gamma(F)
=B_{\rm inf}^\Gamma(G)
+\sum_i\alpha_iB_{\rm inf}^\Gamma(f_i)
-C_{\rm hier}.
}
\tag{3.2}
\]

So a decomposable source may acquire a more negative first-moment Bellman term, but the loss is paid **exactly** by the positive hierarchy KL. Dropping `C_hier` is precisely a credit-free composition error.

The defect composition identity itself was known project-locally. The new point here is the exact ledger for fleet02/B15's newest I-projection credit, identifying the missing composition credit as a bona fide KL divergence.

## 4. Binary gates have zero local irreducible KL

On

\[
\Omega_2=\{\{1\},\{2\},\{1,2\}\},
\]

any law is uniquely determined by its two marginals:

\[
P(\{1,2\})=r_1+r_2-1,
\qquad
P(\{1\})=1-r_2,
\qquad
P(\{2\})=1-r_1.
\]

Therefore

\[
\boxed{K_{\rm occ}(G)=0}
\tag{4.1}
\]

for every nonconstant binary Boolean gate at every interior bias. Consequently, for any binary read-once composition, every bit of global `K_occ` is generated by hierarchy mismatch credits `C_hier`, not by local binary gates.

This is a useful warning for the common Shannon programme: compressing a read-once source to only its local `K_occ` values discards genuine relative entropy even though every local value can be zero.

## 5. Actual Boolean witness: OR(literal, AND)

Take the uniform three-bit Boolean function

\[
F(x_1,x_2,x_3)=x_1\lor(x_2\land x_3),
\]

with `+1` for false and `-1` for true. In little-endian truth-table order its values are

\[
(1,-1,1,-1,1,-1,-1,-1).
\]

The raw Walsh vector is

\[
(-2,6,2,2,2,2,-2,-2).
\]

Hence the squared spectrum has empty mass `1/16`, singleton `{1}` mass `9/16`, and each of the other six nonempty sets mass `1/16`. Conditioning on nonempty sets gives

\[
P(\{1\})={3\over5},
\qquad
P(S)={1\over15}
\quad\text{for the other six nonempty }S,
\]

with physical coordinate marginals

\[
r=\left({4\over5},{4\over15},{4\over15}\right).
\]

The global I-projection parameter is the small root of

\[
64\zeta^2-560\zeta+375=0,
\]

namely

\[
\zeta={35-5\sqrt{34}\over8}=0.730655065721687\ldots.
\]

Direct evaluation gives

\[
\boxed{K_{\rm occ}(F)=0.132521049007492\ldots\text{ bits}.}
\tag{5.1}
\]

Now decompose `F` as an outer OR of the literal `x_1` and the child `AND_2(x_2,x_3)`. Every local binary law has `K_occ=0`. Nevertheless the hierarchy terms are

\[
D(Q_\alpha\Vert Q_A)=0.027664030597118\ldots,
\]

and

\[
\alpha_{\rm AND}
D(Q_{r_{\rm AND}}\Vert Q_{\rm AND}^{(\zeta)})
=0.104857018410374\ldots,
\]

whose sum is exactly

\[
0.132521049007492\ldots=K_{\rm occ}(F).
\]

Thus an actual Boolean composition can have **zero local irreducible KL in every component but positive global irreducible KL**, entirely generated by the hierarchy mismatch. This decisively refutes any credit-free composition rule that keeps only the component `K_occ` values.

For comparison, the symmetric `AND_4=AND_2(AND_2,AND_2)` alignment has child I-projection parameter `3/4`, outer activation marginal `4/5`, and global parameter `15/16`, satisfying

\[
(15/16)(4/5)=3/4.
\]

Its hierarchy mismatch vanishes. This is consistent with the owner's observed AND-chain tightness, but it is not by itself a proof of global AND extremality.

## 6. Consequence for Interface D and the owner-aligned gate programme

The weakest arithmetic/Shannon transfer across a **decomposable** Boolean source is now exact: equation (3.1) transfers the actual unpaid remainder with no hidden branch debt, while (2.6) records every negative-information credit and exposes the extra hierarchy credit explicitly. Therefore Interface D should no longer spend runs seeking a separate product/arithmetic interpolation for disjoint decompositions.

The remaining universal obligation is localized to **composition-prime outer gates**. There one must prove `R_Gamma>=0` for a surviving potential, equivalently make the genuine Boolean-dependence credit `K_occ` pay any negative `B_inf`, or construct a prime gate/bias that violates the all-gate inequality. The fleet03/B15 JS theorem is compatible with this conclusion: its remaining branch-entropy payment should be attacked only after decomposable blocks are factored, with child slack and the retained KL credits still present.

This advances the exact transfer ledger but does not prove FEI, does not prove a universal potential, and does not establish AND extremality. The fixed `Gamma^dagger` used in earlier runs has already been refuted globally by a biased composition-prime instance; all identities here are stated for arbitrary symmetric `Gamma` and therefore survive any repaired potential.

## 7. Independent checker

A standard-library checker reconstructs the Walsh spectrum of the three-bit witness, solves the global I-projection equation independently, evaluates `K_occ` both as `D(P||Q_r)` and as `Hmax(r)-H(P)`, and then evaluates the two hierarchy terms from the explicit OR/AND decomposition. Its output is:

```text
PASS
Walsh raw = [-2, 6, 2, 2, 2, 2, -2, -2]
r = ['4/5', '4/15', '4/15']
zeta = 0.730655065721687
K_occ direct = 0.132521049007492
K_occ Hmax-H = 0.132521049007492
outer hierarchy KL = 0.027664030597118
AND internal tilt KL = 0.262142546025936
weighted AND tilt = 0.104857018410374
hierarchy total = 0.132521049007492
```

The checker is a falsification/self-consistency aid. The theorem is the exact KL chain-rule/Pythagorean calculation above.

## 8. Handoff

**Consumed predecessor:** fleet02/B15 `20260922T0829Z-influence-iprojection-kl/REPORT.md`.  
**Applied expression:** `R_Gamma=B_inf^Gamma+K_occ`, with `K_occ=D(w^+||Q_r)` retained exactly.  
**New proved inference:** exact composition law (2.6), exact remainder transfer (3.1), and binary-local `K_occ=0` with a genuine Boolean hierarchy-credit witness.  
**Failed stronger claim:** `K_occ(F)=K_occ(G)+sum alpha_i K_occ(f_i)` without the hierarchy KL is false, even for `OR(literal,AND)`.  
**Next target:** prove the prime-gate remainder nonnegative for a surviving potential, or find a prime counterexample with margin above the decomposable/AND extremum.  
**Full FEI:** remains OPEN.
