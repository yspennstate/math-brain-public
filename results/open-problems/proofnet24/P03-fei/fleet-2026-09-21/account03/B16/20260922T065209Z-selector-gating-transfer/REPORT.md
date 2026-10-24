# account03/B16 — arbitrary-selector nonamplification at the live FEI center

**Run:** `20260922T065209Z-b16-auto11`  
**Classification:** `AUXILIARY_ONLY / EXACT_ADVERSARIAL_FAMILY_EXCLUDED`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`. Authenticated GitHub control and scientific artifacts were consumed, but no authenticated installed-brain retrieval/context entered the mathematics.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.

## 0. Version and why this is the live attack

Fresh owner control is revision `2026-09-22.2`. Its later natural-language OWNER MESSAGE supersedes the older Campaign-C half-band assignment where they conflict and converges the FEI workers on the all-gate formulation. The current common post-falsifier center used by the live gate programme is

\[
C^\dagger=6.521851214,
\qquad
\Gamma^\dagger(p)=\Gamma_0(p)+0.268204856\,p(1-p).
\]

The universal missing implication remains the all-gate inequality, equivalently the current `LIMIT-PRIME-GATE-LIFT-v1` target. At balanced uniform gates this reduces to

\[
S_C(f):=C[I(f)-1]-H(f)\ge0.
\tag{0.1}
\]

The old AND/decomposable-extremality claim for the read-once potential has already been rigorously refuted by the balanced Numaro gate, so this run does not repeat an arity sweep. B16's adversarial obligation is instead to test whether sparse-selector, tensor, or asymptotic Boolean constructions can amplify a safe balanced core past the live center.

## 1. Named cross-account result consumed and applied

I consume **account04/B17**,

`proofnet24/P03-fei/fleet-2026-09-21/account04/B17/20260922T061604Z-character-cofactor-local-threshold/REPORT.md`, report blob `865131123fbceeb0d41109308d531ace9e926af6`.

That report proves, for `0<d<=1/2`, the exact character-cofactor scalar request

\[
Q(d)=
{2-m-m h_2\!\left({b^2\over1+b^2}\right)
+m h_2\!\left({d^2\over m}\right)\over d},
\qquad b=1-2d,\quad m={1+b^2\over2},
\tag{1.1}
\]

satisfies

\[
\boxed{Q(d)<5.1.}
\tag{1.2}
\]

It also gives an exact Boolean witness at `d=235/1024` with

\[
4.872321043042353<Q(d)<4.872321043042355.
\tag{1.3}
\]

Below I identify exactly the same scalar inside an arbitrary Boolean selector construction. Thus the peer theorem is used as the rigorous scalar payment, not merely cited.

## 2. Arbitrary-selector suspension: exact formula

Use the convention `true=-1`. Let

- `a:{+-1}^m->{+-1}` be an arbitrary nonconstant Boolean selector, with
  \(\delta=\Pr[a=-1]\in(0,1)\);
- `f:{+-1}^n->{+-1}` be an arbitrary **balanced** Boolean core on disjoint variables;
- `z` be a fresh unbiased character.

Define

\[
h=\operatorname{AND}(a,f),
\qquad
G=z\,h.
\tag{2.1}
\]

Thus `h=-1` exactly when `a=f=-1`; multiplication by `z` makes `G` balanced while translating its Fourier support by one fresh coordinate. Hence

\[
H(G)=H(h),
\qquad
I(G)-1=I(h).
\tag{2.2}
\]

The exact AND composition formula at input measures `(delta,1/2)` gives

\[
I(h)={1\over2}I(a)+\delta I(f).
\tag{2.3}
\]

The four biased gate spectral masses are

\[
(1-\delta)^2,\quad \delta(1-\delta),\quad
\delta^2,\quad \delta(1-\delta),
\tag{2.4}
\]

whose entropy is exactly `2 h_2(delta)`. Therefore

\[
H(h)
={1\over2}\bigl[H(a)-h_2(V_\delta)\bigr]
+\delta H(f)+2h_2(\delta),
\qquad
V_\delta=4\delta(1-\delta).
\tag{2.5}
\]

For an arbitrary constant `C`, put

\[
E_C(a):=CI(a)-H(a),
\qquad
S_C(f):=C[I(f)-1]-H(f).
\tag{2.6}
\]

Substitution of (2.3)--(2.5) into (2.2) yields the exact signed identity

\[
\boxed{
S_C(G)
={1\over2}E_C(a)+\delta S_C(f)
+\delta\,[C-T(\delta)],
}
\tag{2.7}
\]

where

\[
\boxed{
T(d):={2h_2(d)-\tfrac12h_2(4d(1-d))\over d}.
}
\tag{2.8}
\]

No positive part, total-variation replacement, or asymptotic approximation has been taken.

## 3. The scalar is exactly the peer's `Q(d)`

For `0<d<=1/2`, let `b=1-2d` and `m=(1+b^2)/2=1-2d+2d^2`. Direct expansion of binary entropy gives

\[
\boxed{T(d)=Q(d).}
\tag{3.1}
\]

One short verification is to write `phi(x)=-x log_2 x`. Then

\[
m h_2\!\left({b^2\over1+b^2}\right)
=\phi(b^2/2)+\phi(1/2)-\phi(m),
\]

\[
m h_2(d^2/m)
=\phi(d^2)+\phi((1-d)^2)-\phi(m),
\]

and use

\[
\phi(d^2)=2d\phi(d),
\quad
\phi((1-d)^2)=2(1-d)\phi(1-d),
\quad
\phi(b^2/2)=\tfrac12\phi(b^2)+\tfrac12b^2.
\]

After cancellation the numerator of (1.1) is exactly
`2h_2(d)-h_2(4d(1-d))/2`.

Consequently the peer theorem (1.2) proves

\[
T(d)<5.1\qquad(0<d\le1/2).
\tag{3.2}
\]

For `1/2<=d<1`, the crude bound is already stronger:

\[
T(d)\le{2h_2(d)\over d}\le4<5.1.
\tag{3.3}
\]

Therefore

\[
\boxed{\sup_{0<d<1}T(d)<5.1.}
\tag{3.4}
\]

The peer's exact witness (1.3) transfers to this scalar and shows that the scalar request is genuinely near `4.872321...`; one cannot replace it by a uniform value below `4.8723` by a mere sharpening of the same scalar argument.

## 4. New theorem: arbitrary Boolean selector gating cannot amplify a safe core

### Theorem 4.1

For every `C>=5.1`, every arbitrary Boolean selector `a`, and every balanced Boolean core `f` on disjoint variables, the suspension (2.1) satisfies

\[
\boxed{
S_C(G)
\ge {1\over2}E_C(a)+\delta S_C(f)+\delta(C-5.1).
}
\tag{4.1}
\]

In particular, if

\[
H(a)\le CI(a),
\qquad
H(f)\le C[I(f)-1],
\tag{4.2}
\]

then `G` obeys the balanced-excess inequality strictly whenever `0<delta<1`:

\[
H(G)<C[I(G)-1].
\tag{4.3}
\]

### Proof

Equation (4.1) is (2.7) plus (3.4). Under (4.2) the first two terms on its right are nonnegative. If `C>=5.1`, the remaining term is nonnegative, and for the live center it is strictly positive. Boundary selectors are direct degeneracies and follow by continuity/direct substitution. `square`

At the live center this gives the explicit reserve

\[
\boxed{
S_{C^\dagger}(G)
\ge {1\over2}E_{C^\dagger}(a)
+\delta S_{C^\dagger}(f)
+1.421851214\,\delta.
}
\tag{4.4}
\]

This strictly generalizes the all-zero-cylinder rare-gating calculation: the selector may now be **any Boolean function of any arity**, including a high-complexity or recursively constructed selector.

## 5. Two balanced data children are even safer

Let `f_0,f_1` be balanced Boolean functions on disjoint variable blocks, let `a` be an arbitrary Boolean selector of measure `delta`, let

\[
h=\operatorname{MUX}(a;f_0,f_1),
\qquad G=z h.
\tag{5.1}
\]

The same biased-gate calculation gives

\[
I(G)-1={1\over2}I(a)+(1-\delta)I(f_0)+\delta I(f_1),
\tag{5.2}
\]

\[
H(G)
={1\over2}[H(a)-h_2(V_\delta)]
+(1-\delta)H(f_0)+\delta H(f_1)+2h_2(\delta).
\tag{5.3}
\]

Hence

\[
\boxed{
S_C(G)
={1\over2}E_C(a)
+(1-\delta)S_C(f_0)+\delta S_C(f_1)
+C-\delta T(\delta).
}
\tag{5.4}
\]

For `C>=5.1`, all three safe-child terms nonnegative imply

\[
S_C(G)>0,
\tag{5.5}
\]

with at least `C-5.1` scalar reserve. Thus an arbitrary disjoint Boolean selector between two balanced safe children cannot manufacture a new balanced record either.

## 6. Tensor/asymptotic attack: exact nonamplification

If `f,g` are balanced Boolean functions on disjoint variables, their product has product spectral law, so

\[
H(fg)=H(f)+H(g),
\qquad
I(fg)=I(f)+I(g).
\]

Therefore

\[
\boxed{
S_C(fg)=S_C(f)+S_C(g)+C.
}
\tag{6.1}
\]

More generally, if `f` is balanced and `a` is arbitrary,

\[
S_C(fa)=S_C(f)+E_C(a).
\tag{6.2}
\]

So tensor powers/products of already `C`-safe factors cannot amplify the balanced-excess ratio. Together with Theorem 4.1, this eliminates two natural B16 adversarial mechanisms at once: independent tensor amplification and arbitrary disjoint sparse-selector gating of a safe core.

## 7. Attempted refutation and numerical falsification checks

The strongest way this route could have failed was if the selector scalar `T(delta)` exceeded the live center, or if the exact composition identity acquired an unpriced entropy term. Neither happens.

The adjacent checker independently reconstructs Fourier entropy and influence from truth tables and verifies (2.7) on **42,120** selector/core/constant cases: every nonconstant selector through three bits, every balanced core through three bits, and both `C=5.1` and the live `C^dagger`. Maximum numerical identity error is `3.55e-15`. Among cases where both component inequalities are safe, the minimum directly computed parent slack is `0.8487622244`.

It also checks the tensor identity (6.1) on **6,084** pairs of balanced truth tables through three bits, with maximum error `3.55e-15`, and checks `T(d)=Q(d)` on **1,022** dyadic points through denominator `2^10`, maximum numerical discrepancy `6.66e-14`. A one-million-point diagnostic grid places the scalar maximum at approximately

\[
d=0.2294415,
\qquad T(d)=4.872321071783793,
\]

consistent with the peer's rigorous `4.8723 < sup T < 5.1` bracket. The grid is diagnostic only; the rigorous upper payment is inherited from account04/B17.

## 8. Exact scope, replacement obligation, and next recipient

**Version attacked:** `LIMIT-PRIME-GATE-LIFT-v1`, live center `C^dagger=6.521851214`.

**Old missing implication:** rule out or find an exact sparse-defect/tensor/asymptotic Boolean construction that takes individually safe pieces and crosses the live balanced all-gate center.

**New proved inference:** arbitrary Boolean selector gating of one or two balanced safe cores is nonamplifying for every `C>=5.1`, with exact formulas (2.7) and (5.4); balanced tensor products are nonamplifying by (6.1). At the live center the one-core selector construction has an explicit extra reserve `1.421851214 delta`.

**Attempted refutation / dead route:** the scalar-transfer mechanism cannot be sharpened below `4.8723` uniformly: the consumed account04/B17 Boolean witness forces the same scalar `T=Q` above `4.872321043...`. This does **not** refute FEI or the live candidate; it only fixes the local scalar scale.

**Replacement obligation:** a genuine adversary to the live center must now leave these disjoint mechanisms. It must use an intrinsically unsafe smaller component, or a genuinely shared-variable/composition-prime mechanism, or a product-bias direction not reducible to the selector identities above. The universal all-arity/all-bias prime-gate implication remains unpaid.

**consumed_peer_artifact:** `account04/B17/20260922T061604Z-character-cofactor-local-threshold/REPORT.md`, blob `865131123fbceeb0d41109308d531ace9e926af6`.

**applied_to_claim:** exact identification `T(d)=Q(d)` followed by the peer's rigorous `Q(d)<5.1` bound, yielding arbitrary-selector nonamplification.

**remaining_implication:** prove `D_{Gamma^dagger}(P;p)>=0` for every finite composition-prime Boolean gate `P` and every interior product-bias vector, or produce a source-valid counterexample.

**next_recipient:** `account02/B18` as the all-gate/C lead, and `account02/B17` as the current prime-gate adversary. The useful message is that arbitrary disjoint selector gating and tensoring cannot create a new violation from safe children; adversarial search should stay on genuinely prime/shared-variable or off-center mechanisms.

**full-FEI implication:** direct but partial. Two broad asymptotic construction mechanisms are excluded exactly, but no universal prime-gate theorem and no dimension-independent full-FEI proof is obtained. **Full FEI remains OPEN / NOT PROVED.**

Scoped privacy review: mathematical formulas, logical account/slot labels and repository-bound scientific identifiers only. No credentials, scheduler IDs, machine paths, unrelated private transcripts, benchmark gold, email/Drive actions, paid/remote model calls, workflow dispatch, permission change, or public posting.
