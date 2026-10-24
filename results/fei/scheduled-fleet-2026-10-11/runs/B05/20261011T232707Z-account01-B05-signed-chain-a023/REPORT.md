# B05 / A023: signed terminal refund on the Boolean point-defect chain

**Run:** `20261011T232707Z-account01-B05-signed-chain-a023`  
**Primary packet:** A023 (amortized rarity budget)  
**Stable gap:** `B05_RARE_REFUNDS`  
**Status:** a complete signed, single-use payment is proved for the unbounded genuine-Boolean family `q_n`; extension to arbitrary Boolean restriction trees and full FEI remains **OPEN**.

## 1. Bounded objective and prior status

The exact obstruction inherited from the preceding B05/B19 work was:

> For the one-point defect `q_n`, every physical first data/selector order-swap credit for the complete `L+Q` packet is negative for `n>=3`. Does this order-`n 4^{-n}` debt accumulate without bound down the exceptional restriction chain, or is it paid by a nonreused terminal packet?

The conditional-label `L` sign was independently accepted in B19. B19 then repaired the physical scope and proved the phase `Q` sign as a contributor, so the strengthened complete `D=L+Q` sign remains pending a fresh independent review. Before this run, no multilevel signed telescope or terminal refund had been proved for `q_n`.

This run freezes one exact target: reveal data coordinates until the exceptional branch reaches `q_t`, retain every negative logarithmic credit with its reach probability, and determine whether a single terminal packet pays the entire sum.

## 2. Complete physical packet

For a midpoint/half-difference Fourier pair `(a,v)`, put

\[
\phi(u)=u\log_2(1/u),\qquad
L(a,v)=\phi(a^2)+\phi(v^2)-\phi(a^2+v^2),
\]

and

\[
Q(a,v)=(a^2+v^2)\left[1-h_2\left(
\frac12+\frac{|av|}{a^2+v^2}\right)\right],\qquad D=L+Q.
\]

Let `q_n` be `+1` only at the origin and `-1` elsewhere, and write `delta=2^{-n}`. Its complete selector packet is exactly

\[
D_n=D(-1+\delta,\delta)+(2^n-1)D(\delta,\delta).                 \tag{1}
\]

Restricting any data coordinate gives one constant child, whose packet is zero, and one exceptional child equal to `q_(n-1)`. Hence

\[
\Gamma_n^D=D_n-\frac12D_{n-1}.                                  \tag{2}
\]

The source-pinned B05/B19 theorem gives `Gamma_n^D<0` for every `n>=3`. Its exact finite certificate covers `3<=n<=40`, and its analytic proof covers all dimensions.

## 3. PROVED: the renormalized credit is a discrete derivative

Define

\[
C_n=2^nD_n.
\]

Multiplying (2) by `2^n` gives the exact identity

\[
\boxed{2^n\Gamma_n^D=C_n-C_{n-1}.}                               \tag{3}
\]

Thus the locally negative credit is not an uncontrolled new liability: it is precisely the decrease of one scalar renormalized packet.

The sign theorem implies that `C_n` is strictly decreasing for `n>=3`. Also `D(delta,delta)=4delta^2` exactly, while the empty-cell contribution is `O(n delta^2)`. Therefore

\[
C_n\longrightarrow4.                                             \tag{4}
\]

This already identifies the missing global quantity: local nonnegativity fails, but the complete exceptional chain has finite renormalized variation `C_2-4`.

## 4. PROVED: exact single-use terminal refund

Fix integers `2<=t<n`. Reveal any predetermined `n-t` physical data coordinates. Only the unique exceptional branch carries a nonzero packet; its node `q_m` is reached with probability `2^{m-n}`. Define the total expected negative credit by

\[
\mathfrak D_{n,t}
=\sum_{m=t+1}^n2^{m-n}(-\Gamma_m^D).                              \tag{5}
\]

Using (3),

\[
\boxed{
\mathfrak D_{n,t}=2^{-n}(C_t-C_n).
}                                                                 \tag{6}
\]

The expected terminal packet is `2^{t-n}D_t=2^{-n}C_t`, so

\[
\boxed{
D_n+\mathfrak D_{n,t}=2^{t-n}D_t=2^{-n}C_t.
}                                                                 \tag{7}
\]

This is an exact nonlocal amortization. Each local debt is created once when its coordinate is first revealed, weighted by the probability that the defect survives to that node, and spent once in (6). The terminal packet appears once in (7). No descendant reuses an ancestor's credit. The stopping rule is physical, deterministic, nonadaptive, and finite.

## 5. Uniform bound and the unpaid logarithm

From monotonicity and (4),

\[
0\le\mathfrak D_{n,t}\le2^{-n}(C_t-4)\le2^{-n}(C_2-4),           \tag{8}
\]

and

\[
4\,2^{-n}<2^{-n}C_t\le C_2,2^{-n}.                              \tag{9}
\]

An exact expression at the terminal gate is

\[
D_2=\frac34+\phi(9/16)+\phi(1/16)-\phi(5/8)
+\frac58\bigl(1-h_2(4/5)\bigr).
\]

The rigorous certificate gives

\[
C_2=4D_2=4.867668746754\ldots,
\qquad C_2-4=0.867668746754\ldots.                               \tag{10}
\]

Thus the total debt is uniformly below `0.8677*2^{-n}` and the single terminal price is below `4.8677*2^{-n}`. The limiting debt consumes only

\[
1-4/C_2=0.17825139545\ldots                                      \tag{11}
\]

of that terminal price.

The rare logarithm is retained rather than charged to a pointwise `O(I)` budget. B19's full-credit expansion is

\[
\Gamma_m^D=4^{-m}\left(-2m+8-\frac3{\ln2}\right)+O(8^{-m}).     \tag{12}
\]

After multiplying by reach probability, its contribution at depth `m` is

\[
2^{m-n}(-\Gamma_m^D)
=2^{-n}(2m+O(1))2^{-m}+O(2^{-n}4^{-m}).                           \tag{13}
\]

The factor `m=log_2(1/delta_m)` remains explicit and is amortized geometrically. Equation (6), not a discarded upper bound, performs the exact cancellation. Summing (12) backward from the limit (4) gives

\[
C_n=4+2^{-n}\left(2n-4+\frac3{\ln2}\right)+O(n4^{-n}).          \tag{14}
\]

## 6. Mandatory falsifiers and scope

| Control | Result |
|---|---|
| Sparse one-point defect | This is the theorem's exact family; all truth tables are genuine Boolean. |
| Rare suspension | Independent activation by probability `p` multiplies `D_n`, every reached debt, and the terminal price by `p`; (7) is preserved. Pure control/constant cells remain separate. |
| Bent selector | The preceding bent family has nonnegative first credits, so it incurs no signed debt. This is compatible with the present telescope. |
| Near tensor | `q_4 tensor q_5` has negative full first credits, but its two-factor histories are not the single exceptional chain used in (5). A factorwise terminal analysis is still required. |
| Addressing/multiplexer | No conclusion is drawn. In particular, no universal terminal-packet-versus-influence bound is proved. The manuscript's fresh-selector endpoint remains intact. |
| Actual prime gate | `q_n` is AND/OR up to signs and relabeling, not a non-Boolean prefix law. |
| Shared-variable interference | Outside the one-branch disjoint restriction chain; no product or convolution claim is made. |
| Parity-zero erasure | Not used. Both `L` and `Q` are retained. |

The new theorem proves a complete signed first-revelation payment for one unbounded Boolean family. It does **not** show that arbitrary Boolean functions admit such a chain, that the terminal packet is controlled by total influence, or that a globally chosen tree avoids reused influence. It is neither a proof nor a counterexample for full FEI.

## 7. Verification

`verify_signed_chain.py` uses exact `Fraction` arithmetic and rigorously remainder-bounded atanh-series intervals for logarithms. Signed interval division uses all four quotient corners. It independently checks:

- exact integer Walsh spectra of `q_n` for `2<=n<=10`;
- every coordinate restriction has one constant child and one `q_(n-1)` child;
- `Gamma_n^D<0`, `C_n-C_(n-1)<0`, and `C_n>4` for `3<=n<=40`;
- the terminal/refund interval overlap for every `3<=n<=40`;
- `4.8676<C_2<4.8677`, `0.8676<C_2-C_40<0.8678`, and debt fraction in `(0.1782,0.1783)`.

Command:

```text
python3 verify_signed_chain.py
```

The archived run reports 2,303 exact or rigorous interval assertions, no randomness, and `status=PASS`. Representative values are `C_3=4.7422334580...`, `C_8=4.0637374543...`, `C_20=4.0000384599...`, and `C_40=4.000000000073...`.

## 8. Claim and dependency delta

New claim `B05-A023-QN-SIGNED-TERMINAL-REFUND-v1` is **ANALYTICALLY_PROVED_PENDING_INDEPENDENT_REVIEW**.

Movement from the prior obstruction is exact: the first-credit signs remain negative, but the full expected chain debt is now proved to telescope to `2^{-n}(C_t-C_n)` and to be paid once by the terminal `q_t` packet. This retires “negative first credits necessarily accumulate without a bounded refund” for the `q_n` family.

The claim depends on the source-pinned all-dimension negativity of the full `D=L+Q` credit. Since B19 materially supplied the phase proof, the combined full-packet package still needs review by A087 or another noncontributor. No registry label is treated as acceptance evidence.

A023 remains **PARTIAL_PROGRESS** rather than complete because its universal consumer interface still lacks:

1. a terminal-packet bound by nonreused influence or another universal FEI budget;
2. a treatment of branching exceptional histories such as near tensors and addressing;
3. a stopping rule for arbitrary Boolean functions.

## 9. Next exact action

Test whether the same renormalized terminal potential is additive for the two-factor witness `q_a tensor q_b` when coordinates of one factor are exhausted first. Freeze both factor orders, include all branch reach probabilities, and determine whether the terminal remainder decomposes without paying either factor twice. A success would move from the one-branch theorem toward near tensors; a failure should produce an explicit cross-factor interference term.

## 10. Immutable sources

- B05 author boundary report: repository `yspennstate/math-open-problems`, commit `f8af483622a55611c7933f7d8252fe3c94e4c06e`, report blob `0f097b74548e4be301b39a918774c4465638b2df`.
- B19 full-credit scope repair: repository `yspennstate/math-open-problems`, commit `aa80187df752adcf9ff221823df9815c6b0960b9`, report blob `8281ad83ec178bd98a8a9cbfac192959d7d996bd`, checker blob `f9959307004980bfd57b96d9558532fb841c16ab`.
- B05 stream contract blob `05447e6d999437bb82a266b427bd76a4b37266b6`.
- Stream index blob `58e3eb0b1f0e9c03ebf709f83ad496ee8f2df704`.
- Execution protocol blob `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Campaign status blob `8c9c63579ecdd4afa385bb94caf79ee6296addcf`.

The immediate predecessor reports already checked the relevant primary decision-tree/composition literature and made no novelty claim. This run makes no external priority or novelty claim; it advances the source-pinned campaign ledger only.

## 11. Execution and delivery record

The runtime exposed Codex described as based on GPT-5. No separate model selector, reasoning-effort selector, continuous-hour guarantee, billing identity, or allowance meter was exposed. Mathematical derivation, finite verification, repository persistence, independent review, and Brain ingestion are recorded separately. No protected evaluation material, held request, email, public release, scheduler mutation, merge, or live-store mutation was accessed.

Delivery fields in `PROGRESS.json` describe the final repository results. Independent review and native Brain ingestion are not claimed in this author run.
