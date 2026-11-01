# B14 — signed-source closure of the physical nine-core FEI selector

**Classification:** `ESSENTIAL_STEP_APPLIED (current shared-core critical family)`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`.

## 1. Version/change summary and live target

The current owner control remains revision `2026-09-22.2`. Its newest FEI message asks the fleet to converge on the all-gate inequality rather than keep opening unrelated auxiliary routes. The advertised read-once-`Gamma` / AND-extremality subcandidate is already source-validly refuted by the explicit composition-prime ten-input gate in

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B13/20260922T0055Z-arity10-prime-falsifier/REPORT.md`

(report blob `d71f08f9a2fd0b417ac7b0cdbac19bacac85c01b`): at uniform bias it has `H/(I-1)>6.4593722816378554`, hence asks the old `C0=6.4548` potential for margin `c_G>0.0182891265514229`, larger than the quoted AND margin. Thus this run does not try to prove the refuted AND-extremality statement.

The still-live B14 execution-reset duty is to analyze an **actual physical block-selection policy** against the current source-valid critical construction. The previous B14 report

`fleet01/B14/20260922T0225Z-shared-graft-core-block/REPORT.md`

proved that revealing the nine genuine outer-core coordinates has price `<6.528` for the adaptive-depth **monotone/reachable** shared-graft family, using `q=b` and `0<=b<=1/4`. The first missing inference was whether the same physical policy survives arbitrary source signs and nonmonotone coordinates, where the selected Fourier singleton `b` and physical influence `q` are no longer equal.

This report closes that inference.

## 2. Exact named other-account result consumed

The primary new peer input is fleet02/B18:

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T030354Z-global-shared-core-ceiling/REPORT.md`

(report blob `45a336c34c134b5da2a82a0b82a489d183f23891`).

It validates the exact signed source domain `-1<=b<=1` for the same nine-host core and the 19 exact Walsh numerator classes
\[
(A_s,Q_s),\qquad p_s(b)=\frac{(A_s+bQ_s)^2}{512^2},
\]
and proves that its scalar source term
\[
K(b)=H_{\rm core}(b)+\alpha[-\phi(b^2)+16(1-b^2)],
\qquad
\alpha=\frac9{256},\quad \phi(t)=-t\log_2t,
\]
has no larger maximum outside the previously studied interval. I use the exact signed source classes, not a surrogate or a non-Boolean relaxation.

The second source-exact input is the standard one-coordinate entropy identity already in the FEI archive,
\[
L_i(h):=H(h)-\frac{H(h_{i=0})+H(h_{i=1})}{2}=B_i+JS_i,
\]
with
\[
B_i\le h_2(q),\qquad
JS_i\le \frac{2}{\ln2}\min(q,1-q),
\qquad q=\operatorname{Inf}_i(h).
\]
No FEI hypothesis is used in these bounds.

## 3. Exact physical policy

Let `h` be an arbitrary **balanced Boolean** source gadget, and choose any distinguished physical coordinate `i`. Write
\[
b=\widehat h(\{i\})\in[-1,1],
\qquad
q=\operatorname{Inf}_i(h)\in[0,1].
\]
No monotonicity is assumed; in particular `q=b` is not used. Feed this signed singleton coefficient into the exact source-bound nine-host graft
\[
F=T(h,b).
\]

Let
\[
X=\{x_0,\ldots,x_8\}
\]
be the nine genuine outer-core physical coordinates.

**Policy `SIGNED-SHARED-CORE-9`: reveal the whole block `X`.**

There are no packet names, component labels, affine changes of coordinates, or auxiliary selector bits. This is the same original-coordinate block as in the preceding B14 report.

Put
\[
B_0=\frac{257}{256}.
\]

## 4. New exact Poincare identity: the monotonicity assumption disappears

For any Boolean function `g` with mean `mu`,
\[
4P(g)=I(g)-1+\mu^2,
\qquad
P(g):=\frac{I(g)}4-p_g(1-p_g).
\tag{4.1}
\]
Because `h` is balanced, its two `i`-cofactors have means `+b` and `-b`. Also fixing coordinate `i` removes exactly its influence `q` on average:
\[
\frac{I(h_{i=0})+I(h_{i=1})}{2}=I(h)-q.
\tag{4.2}
\]
Therefore
\[
4\,\mathbb E P(h_i)=I(h)-q-1+b^2,
\]
and hence the exact one-coordinate currency is
\[
\boxed{4Q_i(h)=q-b^2.}
\tag{4.3}
\]
For an actual Boolean source this is automatically nonnegative by Poincare; the proof below will not even need to impose the constraint `q>=b^2`.

The shared-graft root has the source-exact value
\[
4P(F)=B_0+\alpha I(h).
\tag{4.4}
\]
After revealing `X`, constants contribute zero and the eighteen host endpoints expose the two `i`-cofactors of `h`. Combining (4.2)--(4.4) gives the new exact identity
\[
\boxed{
4Q_X(F)=B_0+\alpha(1+q-b^2).
}
\tag{4.5}
\]
When the selected coordinate is monotone, `q=b`, and (4.5) reduces exactly to the previous formula `B0+alpha(1+b-b^2)`. Thus (4.5), rather than a comparison inequality, is the correct nonmonotone replacement.

## 5. Exact entropy drop and a two-variable envelope

The exact source entropy decomposition remains
\[
\boxed{
L_X(F)=K(b)+\alpha L_i(h).
}
\tag{5.1}
\]
Using the one-coordinate identity and the universal `B_i`, `JS_i` payments, define
\[
\eta(q):=h_2(q)+\frac{2}{\ln2}\min(q,1-q).
\]
Then
\[
\boxed{
L_X(F)\le K(b)+\alpha\eta(q).
}
\tag{5.2}
\]

Consequently the physical block price obeys
\[
\rho_X(F):=\frac{L_X(F)}{4Q_X(F)}
\le
\frac{K(b)+\alpha\eta(q)}
     {B_0+\alpha(1+q-b^2)}.
\tag{5.3}
\]

The essential point is that (5.3) is now valid for arbitrary signed `b` and arbitrary physical influence `q`; no reachable-interval or monotonicity assumption remains.

## 6. Rigorous global bound on the enlarged rectangle

Set
\[
C=\frac{816}{125}=6.528.
\]
To prove (5.3) is strictly below `C`, rearrange:
\[
K(b)+\alpha\eta(q)
-C[B_0+\alpha(1+q-b^2)]
=A_C(b)+\alpha F_C(q),
\tag{6.1}
\]
where
\[
A_C(b)=K(b)-C[B_0+\alpha(1-b^2)],
\]
\[
F_C(q)=h_2(q)+\frac{2}{\ln2}\min(q,1-q)-Cq.
\]
This is the useful new separation: source interference and physical influence can be bounded independently.

`CHECKER.py` reconstructs the exact 19 source classes from the original nine-host source and uses `Fraction` arithmetic plus positive-remainder atanh enclosures for every logarithm. It covers the **larger independent rectangle**
\[
-1\le b\le1,\qquad 0\le q\le1,
\]
so it does not rely on the additional Boolean constraint `q>=b^2`.

With 1024 rational cells in `b` and 8192 rational cells in `q`, it proves
\[
\sup_{[-1,1]} A_C(b)
<
-0.005232947095775132,
\tag{6.2}
\]
at the printed floating representation of the exact rational upper bound, and
\[
\sup_{[0,1]} F_C(q)
<
0.11192052659882938.
\tag{6.3}
\]
The exact rational comparison gives
\[
\boxed{
\sup_b A_C(b)+\alpha\sup_qF_C(q)<0,
}
\tag{6.4}
\]
with printed upper bound
\[
-0.0012982410825350362.
\]

Therefore:

### Theorem — signed-source nine-core selector

For every balanced Boolean source gadget `h`, every distinguished physical coordinate `i`, every signed singleton `b=hat h({i})`, and every influence `q=Inf_i(h)`, the exact source-bound nine-host graft `F=T(h,b)` satisfies
\[
\boxed{
H(F)-\mathbb E_xH(F_{X=x})
<
4(6.528)\,[P(F)-\mathbb E_xP(F_{X=x})].
}
\tag{6.5}
\]
Equivalently,
\[
\boxed{\rho_X(F)<6.528.}
\tag{6.6}
\]

This theorem includes nonmonotone sources, negative singleton coefficients, and source seeds outside the forward-reachable adaptive-depth family.

## 7. What changed and what remains missing

**OLD missing implication.** The nine-core policy was proved only after `q=b` and `0<=b<=1/4`, so changing the source sign or using a nonmonotone selected coordinate was an unclosed escape route.

**NEW proved implication.** The same fixed nine-coordinate physical block works with price `<6.528` for the **entire exact nine-host transform applied to any balanced Boolean source and any chosen physical coordinate**. The certificate is stronger than needed because it covers all independent `(b,q)` in `[-1,1]x[0,1]`.

Thus varying only the seed sign, seed singleton magnitude, monotonicity, or selected-coordinate influence cannot make this exact nine-host geometry a counterexample to the `C=6.528` physical-block selector.

**NEXT target-level obligation.** This does **not** prove that an arbitrary Boolean gate/restriction state is an exact nine-host graft, and it does not construct one finite symmetric `Gamma` satisfying the all-gate inequality for every gate and every product bias. A universal coverage theorem or a different global potential is still missing. The current read-once AND-extremality candidate is separately refuted by the cited ten-input prime gate, so it cannot serve as that missing universal theorem.

Full FEI therefore remains **OPEN / NOT PROVED**.

## 8. Verification and source boundary

The analytic identities (4.3), (4.5), and (5.1) are independent of finite enumeration. The executable certificate proves only the scalar two-variable inequality (6.4) from the exact source classes. Its successful run prints `PASS` and the strict negative rational upper bound.

The artifact contains only mathematical formulas, source-bound private FEI research material already present in the authorized repository, immutable provenance, and sanitized fleet labels. It contains no credentials, scheduler identifiers, machine paths, unrelated private transcripts, email/Drive actions, paid/remote-compute instructions, workflow changes, permission changes, or public-posting instructions.
