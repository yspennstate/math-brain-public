# B13 — an explicit composition-prime 10-input gate beats the AND margin

**Status:** `CANDIDATE_REFUTED` for the read-once-\(\Gamma\) / AND-extremality candidate. Full uniform-cube FEI remains **OPEN / NOT PROVED**.

**Execution:** `WITHOUT_VERIFIED_BRAIN`. Repository sources were read directly. No authenticated brain retrieval or receiver-context use is claimed.

## 1. Live target and the peer result that changes the argument

The current owner control supersedes the older interface-B assignment for this invocation and asks every FEI worker to converge on the all-gate inequality

\[
\Gamma(p_{\rm out})+H_t(G;p)
\le \sum_i {\rm It}_i(G;p)\,{\Gamma(p_i)+h(V_{p_i})\over V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

and either prove the AND/decomposable extremality claim or falsify it by exhibiting a gate with larger required margin
\[
c_G(p)=-{D_G(p)\over I(G;p)/4-p_{\rm out}(1-p_{\rm out})}.
\]

I consumed the newest compatible B13 result from another account:

`proofnet24/P03-fei/fleet-2026-09-21/account03/B13/20260922T003238Z-balanced-uniform-gate-slice/REPORT.md`, blob `cb99a17793db7919af1cfe21248198f1a6fb2f24`.

It proves that on **balanced gates at uniform input bias**, (G) is already constant-for-constant equivalent to full FEI: if \(C=\Gamma(1/2)\), then (G) becomes

\[
H(G)\le C\,(I(G)-1).
\tag{1}
\]

It also applies the certified 162-input shared-graft construction to show that no universal cap near the read-once scale \(6.455\) can work. This materially changes the argument: there is no point trying to prove AND extremality for the current read-once candidate. The useful remaining falsification task is to make the obstruction **small and structurally prime**, so it cannot be dismissed as a large decomposable gate.

For that structural step I also use account01/B13's exact cofactor theorem from

`proofnet24/P03-fei/fleet-2026-09-21/account01/B13/20260922T002604Z-gate-composition-prime/REPORT.md`.

For a proper block \(A\), a Boolean gate decomposes as \(G(x)=H(g(x_A),x_{A^c})\) iff the cofactors \(G(a,\cdot)\), \(a\in\{0,1\}^A\), contain at most two distinct functions. Thus a gate with at least three cofactors for every proper block \(2\le |A|\le k-1\) is composition-prime.

## 2. A 10-input restriction of the exact 18-input source

Start from the exact 18-input balanced monotone Numaro seed reconstructed in

`proofnet24/P03-fei/continuations/2026-09-21-three-hour-sprint/interactive/20260921T121509Z/external_seed_recovery.json`, whose truth-table SHA-256 is

`f8a7bb2c738d86368305111633376b1a3a83d8ee1f1abcc9a37d841b0f9c7839`.

Write its variables as nine core bits \(x_0,\ldots,x_8\) and nine auxiliary bits \(y_0,\ldots,y_8\). Fix

\[
(y_0,y_1,y_2,y_3,y_4,y_5,y_6,y_7)=(0,0,0,1,1,0,1,1)
\tag{2}
\]

and leave \(x_0,\ldots,x_8,y_8\) free. Call the resulting 10-input gate \(G_{10}\).

The checker reconstructs the 18-input source from the source slices, verifies the source SHA-256, applies (2), and checks exactly that the resulting 1024-point truth table is balanced. Every one of the ten coordinates is essential. The exact individual influences are

\[
{29\over128}\quad(x_0,\ldots,x_5,x_7,x_8),\qquad
{49\over256}\quad(x_6),\qquad
{1\over256}\quad(y_8),
\]

so

\[
\boxed{I(G_{10})={257\over128}},\qquad
\boxed{I(G_{10})-1={129\over128}}.
\tag{3}
\]

## 3. Exact-rational spectral certificate

The integer Walsh transform has 738 nonzero coefficients and exact square histogram

```
16:337, 64:48, 144:108, 256:28, 576:32, 784:18,
1024:34, 1296:36, 1600:24, 2304:8, 3136:8, 5184:8,
6400:16, 7056:12, 9216:8, 12544:4, 38416:1, 53824:8.
```

Parseval is checked exactly. Entropy is then enclosed with an all-`Fraction` atanh-series interval for every logarithm; the certified interval width is below \(1.202\times10^{-21}\). It gives

\[
H(G_{10})=6.5098361275881516\ldots
\]

with the displayed digits common to both endpoints, and therefore

\[
\boxed{
{H(G_{10})\over I(G_{10})-1}
>6.4593722816378554.
}
\tag{4}
\]

This already exceeds the owner's current best read-once-certificate cap \(6.4559\).

At uniform bias, because the gate is balanced,
\[
D_G=C_0(I-1)-H,
\qquad
K_G={I-1\over4},
\]
so for the live read-once fixed point \(C_0=6.4548\),

\[
\boxed{
c_{G_{10}}
=4\left({H(G_{10})\over I(G_{10})-1}-C_0\right)
>0.0182891265514229.}
\tag{5}
\]

The live two-input AND margin quoted by the owner is \(0.0043974201\). Thus this 10-input gate asks for more than **4.15 times** that margin. Larger \(c_G\) is the dangerous direction by the definition above.

## 4. The gate is composition-prime, not merely non-read-once

The checker applies account01/B13's exact cofactor criterion to **every** proper block \(A\subset[10]\) with \(2\le |A|\le9\). There are

\[
2^{10}-1-10-1=1012
\]

such blocks. For every one, at least three distinct cofactors occur; the minimum observed count before early stopping is exactly three. Hence

\[
\boxed{G_{10}\text{ is composition-prime}.}
\tag{6}
\]

As an independent simpler structural witness, the monotone gate has a minterm on local coordinates \(\{2,4,6\}\) and a minimal false clause on \(\{1,2,4,5,9\}\); their intersection has size two. A monotone read-once AND/OR formula would have every minterm and minimal false clause intersect in exactly one variable, by a direct induction on the formula tree. So \(G_{10}\) is also not read-once AND/OR.

Account01/B13 had already proved abstractly that the 18-input violating seed has some composition-prime violating descendant of arity at most 18. Equation (6) makes that descent explicit and improves the arity bound from “at most 18” to a concrete **10-input** prime gate, with its exact margin certified.

## 5. What this settles and what it does not

**Refuted:** the current read-once fixed-point potential at \(C_0=6.4548\), the universal cap \(6.4559\), and the claim that the two-input AND/decomposable gates control the all-gate margin for that candidate. The obstruction can already be taken composition-prime on ten inputs.

**Not refuted:** the existence of some different finite-cap symmetric nonnegative \(\Gamma\) satisfying (G), hence full FEI. The stronger account03/B13 162-input balanced construction still supplies the larger lower bound \(6.521850083658\ldots\); the contribution here is not a better lower bound but a much smaller explicit **prime** falsifier.

**Next target:** search the remaining arities 5--9 for a composition-prime gate whose uniform balanced margin beats the AND margin, or prove that arity 10 is minimal within a source-exact class. Separately, any replacement potential must start with \(\Gamma(1/2)\ge6.521850083658\ldots\), so the old read-once-scale potential should not be repaired further.

## 6. Reproduction boundary

`CHECKER.py` is standard-library only. It verifies source reconstruction, restriction balance, exact Walsh/Parseval/influence data, the rational logarithm enclosure, both live numerical inequalities, all 1012 composition-prime block tests, and the independent minterm/maxterm witness. Local execution exited 0. The checker source SHA-256 is `d612bb4ca2edcc5fb3561a94e100c8acbdb8ffbb8f5bdc8be55900d6dd7a54d2`; the output JSON SHA-256 is `1debc9dc588194d1064324f0982b9a3c27dd2b0db4110182ad328bc7e68e12e3`.

No claim of novelty or publication priority is made. Full FEI remains OPEN.
