# fleet04/B13 — the arity-10 gate obstruction is a balanced-restriction atom

**Outcome:** `ESSENTIAL_STRUCTURE_APPLIED / OLD_AND_EXTREMALITY_ALREADY_REFUTED`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**. Repository sources were read through the authorized connector, but no authenticated cognitive-brain retrieval and receiver-context use occurred.

## 0. Why this is the live B13 task

Fresh owner control revision `2026-09-22.2` supersedes the earlier interface-B/all-row-stability prompt for this invocation. The FEI fleet is ordered to converge on the all-gate reformulation and either prove decomposable/AND extremality or falsify it. Compatible peers have now rigorously falsified that old extremality claim. The useful next question is therefore not another sweep but the structure of the smallest certified obstruction and what an induction must retain.

I consume two exact other-account results.

1. `fleet03/B12/20260922T004418Z-arity10-gate-refutation/REPORT.md`, blob `d12fe592f4fa6db16cb571557f6cc41392dd5860`, gives the explicit genuine monotone balanced 10-input restriction of the Numaro seed, truth-table SHA-256
   `3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`, with
   \[
   I(G)=257/128,\qquad
   \frac{H(G)}{I(G)-1}>6.459372281637855731,
   \]
   hence for the read-once base cap \(C_0=6.4548\),
   \[
   c_G>0.018289126551422926.
   \]

2. The newer compatible result
   `fleet02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`, blob
   `335d6ffa58cae84c7b47e742a250a20d2e2bddd4`, proves the exact stopping-time identity
   \[
   P(G)c_G
   =
   \mathbb E\!\left[\sum_{r<\sigma}Q_r c_r
   +P(G_\sigma)c_{G_\sigma}\right].
   \tag{0.1}
   \]
   This changes the argument decisively: once the root obstruction is known, the right question is whether it descends to a smaller balanced gate or instead lives in the **unbalanced transient continuation credits** of (0.1).

The theorem below answers that question for the certified arity-10 witness.

## 1. Exact finite theorem

Let \(G\) be the exact 10-input gate above. A coordinate restriction is encoded by a word in
\(\{*,0,1\}^{10}\), with `*` meaning free. Call the restriction **balanced** when its remaining truth table has equally many \(+1\) and \(-1\) values.

### Theorem 1 — balanced-restriction atom

Every proper balanced coordinate restriction \(R\) of \(G\) is safe for the old balanced gate-margin inequality:

* if \(I(R)=1\), \(R\) is affine and carries zero Poincare currency;
* if \(I(R)>1\), then
  \[
  \boxed{\frac{H(R)}{I(R)-1}<6.4548.}
  \tag{1.1}
  \]

More sharply, among **all** proper balanced non-affine restrictions,
\[
\boxed{
\frac{H(R)}{I(R)-1}
<
6.347067498701918874,
}
\tag{1.2}
\]
so at uniform bias their read-once-base gate margin satisfies
\[
\boxed{c_R< -0.430930005192324506.}
\tag{1.3}
\]

There are no balanced codimension-one or codimension-two restrictions at all. The first non-affine balanced descendants occur only after at least three coordinates have been fixed.

### Exact certificate

The checker enumerates all \(3^{10}=59049\) ternary restriction patterns. It finds:

* `9514` proper balanced restrictions;
* `460` proper balanced non-affine restrictions;
* balanced free-arity counts
  \[
  \{1:1028,\,2:2882,\,3:3112,\,4:1788,\,5:512,\,6:152,\,7:40\};
  \]
* no balanced restrictions with 8 or 9 free coordinates.

For every one of the 460 non-affine cases it computes exact edge influences and an integer Walsh transform, then encloses each logarithm by a rational atanh series. The assertion checked is the strict rational inequality
\[
H_{\rm upper}(R)<\frac{16137}{2500}\,[I(R)-1].
\tag{1.4}
\]

The extremal proper balanced restriction is represented by
\[
(*,*,*,*,*,*,0,0,1,*),
\]
has seven formally free coordinates but only six essential ones, and satisfies
\[
I=13/8,
\]
with influence vector
\[
(3/8,3/8,1/16,3/8,3/8,1/16,0).
\]
Its truth-table SHA-256 is
`f5b69981139d94c61b8658495920225a04dbeb1db9781dcfc69d6855e3348f17`, and the checker proves
\[
3.966917186688699295
<
H
<
3.966917186688699296.
\]

The exact checker source SHA-256 executed in this run is
`af9b89074c7d1557cbf649463e37ae7013e359cc8cd790e000d62054384895b8`.

## 2. Consequence for restriction induction

At the balanced root,
\[
P(G)=\frac{I(G)-1}{4}=\frac{129}{512},
\qquad
c_G>0.018289126551422926.
\tag{2.1}
\]
Hence
\[
P(G)c_G>0.00460800258815148.
\tag{2.2}
\]

Now let \(\sigma\) be any stopping time which stops when the restriction first becomes either affine or a **proper balanced** non-affine gate. By Theorem 1 every non-affine terminal balanced gate has \(c_{G_\sigma}<0\), while affine terminals have zero Poincare currency. Therefore the exact peer martingale identity (0.1) yields
\[
\boxed{
\mathbb E\sum_{r<\sigma} Q_r c_r
\ge P(G)c_G
>0.00460800258815148.
}
\tag{2.3}
\]

Since the consumed block currency obeys
\[
\mathbb E\sum_{r<\sigma}Q_r\le P(G),
\]
its signed average local margin satisfies
\[
\boxed{c_\sigma\ge c_G>0.018289126551422926.}
\tag{2.4}
\]

So the arity-10 obstruction is not hiding a smaller balanced obstruction. It is created in the unbalanced restriction excursion before balance returns. Because balance cannot return in one or two coordinate fixes, any depth-one or depth-two argument specialized only to balanced descendants is structurally incapable of locating this excess.

This is exactly how the newest fleet02/B16 theorem changes the proof strategy: the all-depth continuation credits are not bookkeeping. For this witness they are the only place the positive root excess can live.

## 3. What this rules out and what it does not

This rules out a natural attempted repair of the dead AND-extremality claim:

> “Pass to a smaller balanced coordinate restriction carrying the same positive gate-margin obstruction, then induct.”

The exact 10-input witness has no such proper balanced descendant.

It does **not** refute a source-exact induction through unbalanced gates, and it does not prove any universal finite-block bound. In fact, fleet02/B16 shows that a successful restriction proof must keep the unbalanced descendant potential \(\Gamma(p_{\rm out})\) and its signed continuation credits.

The next decisive calculation is therefore narrower than another gate sweep: evaluate the certified replacement potential on the **unbalanced codimension-one and codimension-two descendants** of this exact 10-input gate and compute their two-step block margins. A proof should then explain the sign of that transient, not erase it by balancing.

## 4. Preserved prior B13/B18 mathematics

Nothing here weakens or replaces fleet04/B18's mixed-curvature conservation
\[
\kappa_{ik}=\kappa_{ki}=p_{ik}+4o_{ik},
\qquad
\sum_{i\ne k}\kappa_{ik}=4d_k,
\]
including the opposite-sign overlap term, and nothing changes the exact zero-defect classification by a character-twisted signed one-point defect. Those remain valid inherited results. The current owner order simply supersedes their use as this invocation's live route.

No small-cube-measure-times-ambient-dimension estimate is used here.

## 5. Status

**Full FEI remains OPEN / NOT PROVED.**

The old decomposable/AND-extremality program for the read-once potential is already rigorously refuted. This run adds a source-exact structural fact about the certified smallest obstruction currently in hand: it is a **balanced-restriction atom**, forcing any restriction martingale proof to pay attention to genuinely unbalanced transient states.
