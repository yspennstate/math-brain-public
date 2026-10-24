# POS3 account01/B11 — exact endpoint exchange with reverse-blocker remainder

**Run:** `20260922T021210Z-b11-pos3-exchange-r11`  
**Directive:** `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
**Outcome:** `ESSENTIAL_STEP_APPLIED_WITH_LOCAL_CLOSURE_REFUTED`  
**Parent POS3:** OPEN / NOT PROVED  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`

## 1. Exact inherited state used

The target is the width-at-most-three scope of the `1/3–2/3` conjecture under the uniform law on **all** linear extensions.

This run consumes the following exact completed team state.

1. **Campaign lead account04/B10**, report blob `1e5a9682e4f90f38484a86e7199428de0b0160f8`: in a hypothetical width-three counterexample every element has its strong-majority rank with probability `>1/81`; at an endpoint the one-sided rank event is `>4/9`.
2. **account03/B11**, report blob `3443c6ccc4436b9eaf060884c4eec6fc85dc1792`: at the first strong-majority block boundary `x ≺_* y` there are exactly two canonical successor blockers `s_1,s_2`; both are Hasse covers of `x`, the triple `y,s_1,s_2` is an antichain, the blocker pair is nonautonomous, and every distinguisher of the pair occurs only after the entire second majority block.
3. **account02/B10**, report blob `acdb868b3e35a9248d494126311bfff3bfee150b`: under the endpoint hypothesis `Pred(y)⊆Pred(x)`, if `M=Min{z:x<z,z||y}`, then the right-fringe channel masses satisfy an exact blocker-order bijection and `p_xy <= 1-(1/2)∏_{m∈M}p_ym`; for the two endpoint blockers this gives `2/3<p_xy<7/9` and both Hasse channels are active.
4. **Assigned partner account02/B19**, report blob `14588aa0c8cfb8bff56ebd7d08b3d361f6653a90`: the family `P(m,r)=C_2 ⊔ C_{m+2} ⊔ C_r` refutes fixed-pair chain-contraction lifting. In particular `Pr(A_1<B_1)=2/(m+4)`, while for `m=3` the migrated pair has `Pr(A_1<B_2)=11/21`.
5. **Previous account01/B11**, handoff blob `893a73b36c16ae4f2d13794970a339c8d97ec771`: the blocker-sorting exchange gives an exact image/fiber formulation, but a five-element width-three example refutes a local factor-two fiber bound.

The named OTHER-account result required by this assignment is item 4. Section 5 below applies it quantitatively, not merely as a citation.

## 2. Compact conditional end-to-end route

Assume, for contradiction, a cardinality-minimal width-at-most-three poset `P` with no balanced incomparable pair. Use the inherited transitive strong-majority order and let `x ≺_* y` be its first chain-block boundary. The inherited endpoint state gives

- `Pred(y)⊆Pred(x)`,
- exactly two minimal successor blockers `M={s_1,s_2}`,
- `p_xy>2/3`, and
- `p_{ys_i}>2/3` for both blockers.

The previous B11 exchange left a noninjective-fiber excess. The theorem below removes that opacity at an endpoint: it identifies the **entire signed majority defect exactly** as

`forward blocker-channel mass - reverse nonneutral-blocker mass`.

Thus the endpoint closes as soon as the team can prove that the reverse remainder plus the common two-blocker event has mass at least `2/3`. The exact first missing implication after the theorem is stated in Section 7. A seven-element source-valid team witness shows that delayed nonautonomy at this one endpoint alone cannot supply it, so the remaining implication is genuinely multi-boundary/global.

## 3. Exact endpoint exchange theorem

Let `P` be any finite poset and let `x||y` satisfy

`Pred(y) ⊆ Pred(x)`.                                           (H)

Write

`Ω_+={L:x precedes y}`, `Ω_-={L:y precedes x}`, `E=e(P)`.

Put

`S_x(y)={z:x<z and z||y}`,
`M=Min S_x(y)`.

Define

`Q = #{L : y precedes every m∈M}`,

where the condition is vacuous when `M=∅`.

For `L∈Ω_-`, call the open interval between `y` and `x` **neutral** if every element in it is incomparable with both `x` and `y`. Let

`I = #{L∈Ω_- : the open interval (y,x) is neutral}`,
`R = |Ω_-|-I`.

Thus `R` is the exact reverse-order nonneutral-blocker remainder.

### Theorem 3.1 — exact signed endpoint exchange

Under (H),

`|Ω_+| = I + (E-Q)`,                                            (3.1)

`|Ω_-| = I + R`,                                                (3.2)

and consequently

`|Ω_+|-|Ω_-| = E-Q-R`,                                          (3.3)

`2|Ω_-| = Q+R`,                                                 (3.4)

`2I = Q-R`.                                                     (3.5)

Equivalently, for `p_xy=|Ω_+|/E`,

`p_xy = 1 - (Q+R)/(2E)`,                                       (3.6)

and

`2p_xy-1 = (E-Q)/E - R/E`.                                     (3.7)

So the majority bias is **exactly** forward minimal-blocker activation minus reverse nonneutral-blocker activation.

### Proof

Take `L∈Ω_+` and write it as

`L = A, x, W, y, B`.

Every `z∈W` is incomparable with `y`. Indeed, if `z<y`, then (H) gives `z<x`, impossible because `z` occurs after `x`. If `y<z`, the displayed extension order is impossible.

Let `N` be the maximal initial segment of `W` consisting of elements incomparable with `x`, and write `W=N S`. Define

`Φ(L)=A, y, N, x, S, B`.                                      (3.8)

This is a linear extension. Moving `y` left across `W` is legal because all of `W` is incomparable with `y`; moving `x` right across `N` is legal because every element of `N` is incomparable with `x`. Internal orders are unchanged.

The open interval between `y` and `x` in `Φ(L)` is exactly `N`, hence is neutral to both endpoints. Conversely, if

`σ=A,y,N,x,B`

has a neutral open interval, then

`A,x,N,y,B`

is a valid forward extension and maps back to `σ`. This is the **base preimage**. Therefore the forward extensions for which all of `W` is neutral are in bijection with the `I` neutral reverse extensions.

It remains to count non-base forward extensions. Suppose `S` is nonempty and let `q` be its first element. Since `q` lies after `x`, comparability with `x` means `x<q`; and we already proved `q||y`. Moreover `q` is minimal in `S_x(y)`: if `m∈S_x(y)` satisfied `m<q`, then `x<m<q`, so `m` would have to occur between `x` and `q`, contradicting the choice of `q` as the first `x`-successor in `W`. Hence `q∈M`.

For `q∈M`, define

`C_q={L:q<y and q<m for every m∈M\{q}}`.                      (3.9)

Every non-base forward extension belongs to exactly one `C_q`, namely its first minimal blocker. Conversely, if `L∈C_q`, then `x<q<y`, so `L∈Ω_+`; and no successor of `x` can occur before `q`, because any such successor has a minimal member of `M` below it, contradicting that `q` is the first member of `M`. Thus `q` is exactly the first nonneutral `x`-successor between `x` and `y`, so `L` is a non-base forward extension of the exchange.

The `C_q` are disjoint. Their union is the complement of the event counted by `Q`: an extension fails `y<m` for all `m∈M` exactly when at least one minimal blocker precedes `y`, and its earliest such blocker selects exactly one `C_q`. Hence

`Σ_{q∈M}|C_q| = E-Q`.                                         (3.10)

Combining the base bijection with (3.10) proves (3.1). Equation (3.2) is the definition of `R`; subtraction and addition give (3.3)–(3.5), and normalization gives (3.6)–(3.7). `□`

### Structural interpretation of `R`

For a reverse extension `y ... x`, a nonneutral element between the endpoints can only be either

- a predecessor of `x` incomparable with `y`, or
- a successor of `y` incomparable with `x`.

Conversely, any such reverse blocker can be placed between `y` and `x` in some linear extension by adding the compatible order `y<z<x`. Thus `R=0` precisely means that the reverse orientation has no realizable endpoint blocker between the pair. This makes `R` the exact obstruction to the simple neutral-interval swap being onto `Ω_-`.

## 4. Consequences at the first width-three boundary

At the inherited first boundary, `M={s_1,s_2}` and the account02/B10 use of the multivariate Shepp/XYZ inequality gives

`Q/E = Pr(y<s_1 and y<s_2) > 4/9`.                             (4.1)

Because a hypothetical counterexample has `p_xy>2/3`, (3.6) gives the new strict reverse-remainder cap

`R/E < 2/3 - Q/E < 2/9`.                                      (4.2)

Also, from (3.5),

`I/E = (Q/E-R/E)/2 > 1/9`.                                    (4.3)

More sharply, as a fraction of **reverse extensions**,

`I/|Ω_-| = (Q-R)/(Q+R) > 1/3`,                               (4.4)

because `Q/E>4/9` and `R/E<2/9`. Thus more than one third of all reverse-order extensions have a completely endpoint-neutral open interval.

Let `U_i=|C_{s_i}|`. Then the exact signed identity is

`D:=|Ω_+|-|Ω_-| = U_1+U_2-R`.                                 (4.5)

Account02/B10 independently decomposes the same deletion-fiber defect as

`D=Φ_1+Φ_2-Ψ`,                                                (4.6)

where `Φ_i` is positive defect in channel `s_i` and `Ψ` is total negative defect. Comparing (4.5) and (4.6) gives a new exact reconciliation:

`R=(U_1-Φ_1)+(U_2-Φ_2)+Ψ`.                                   (4.7)

Thus the reverse remainder is not an unspecified error term. It is exactly the sum of unused positive right-fringe capacity plus all negative deletion-fiber defect. This is the requested tracking of noninjective fibers in mass-transport form.

Finally, (3.6) says the first boundary would be balanced as soon as

`Q+R >= 2E/3`.                                                (4.8)

The endpoint problem is therefore reduced to obtaining the missing `2E/3` lower bound by **global** constraints, not by controlling a mysterious exchange multiplicity.

## 5. Named partner account02/B19 applied exactly

Apply Theorem 3.1 to the assigned partner's family

`P(m,r)=C_2(A) ⊔ C_{m+2}(B) ⊔ C_r`.

Take `x=B_1`, `y=A_1`. Then `Pred(x)=Pred(y)=∅`, so (H) holds, and the unique minimal successor blocker is `M={B_2}`. The partner proved

`Pr(A_1<B_1)=2/(m+4)`,

so

`p_xy=Pr(B_1<A_1)=(m+2)/(m+4)`.                               (5.1)

The common blocker event is exactly

`Q/E = Pr(A_1<B_2)
     = 1 - ((m+2)/(m+4))*((m+1)/(m+3))
     = 2(2m+5)/((m+4)(m+3))`.                                 (5.2)

The reverse nonneutral remainder is exactly the event

`A_1 < A_2 < B_1`,

because in the reverse orientation the only endpoint-comparable letter that can occur between `A_1` and `B_1` is `A_2`. Hence

`R/E = 2/((m+4)(m+3))`.                                       (5.3)

Substitution gives

`1-(Q/E)-(R/E)=m/(m+4)=2p_xy-1`,                              (5.4)

exactly as Theorem 3.1 predicts.

For the partner's concrete `m=3,r=1` certificate, `E=168` and

`|Ω_+|=120`, `|Ω_-|=48`, `Q=88`, `R=8`.

Thus

`Q/E=11/21`, `R/E=1/21`, `p_xy=5/7`.

The partner's observed pair migration `Pr(A_1<B_2)=11/21` is therefore **exactly the Q term** in the endpoint exchange, while the remaining `1/21` is the reverse blocker remainder. This explains, at the exchange level, why fixed-pair contraction fails: contraction changes the corridor event `Q` and its reverse remainder rather than merely changing an abstract induced weight.

## 6. A genuine local-closure counterexample from the team witness

The account03/B11 seven-element width-three witness has `E=79`, first boundary `(x,y)=(0,1)`, two Hasse blockers `{3,4}`, and delayed distinguishers `5,6`. Account02/B10 computed

`|Ω_+|=54`, `|Ω_-|=25`, `Q=50`, `U_3=9`, `U_4=20`.

Equation (3.3) forces

`R=E-Q-(|Ω_+|-|Ω_-|)=79-50-29=0`.                             (6.1)

The verifier independently reconstructs the same fact. Therefore the following tempting stronger lemma is false:

> A nonautonomous endpoint Hasse-blocker pair with a delayed distinguisher forces positive reverse nonneutral remainder at the same boundary.

It does not: this witness has delayed distinguishers but `R=0`. The parent poset is not a POS3 counterexample because, for example, `Pr(2<3)=42/79` is balanced. Hence this is a source-valid counterexample to a **local closure lemma only**, not to POS3.

This matters for the proof search: the delayed distinguisher must be coupled to the later balanced-pair obstruction or to subsequent boundary flows. It cannot simply be charged back into `R` at the first boundary.

## 7. First essential missing implication

The exact endpoint identity isolates the next nonlocal obligation.

In a cardinality-minimal hypothetical POS3 counterexample, at the first boundary `x≺_*y` with blockers `s_1,s_2`, prove from the **simultaneous** inherited constraints (delayed nonautonomy across later blocks, no balanced pair anywhere, ideal-block/rank-one deletion weights, and the cumulative three-chain heavy-slice conditions) that

`Q+R >= 2E/3`,                                                (7.1)

where

`Q=#{L:y<s_1 and y<s_2}`

and `R` is the reverse nonneutral-blocker remainder defined above.

By (3.6), (7.1) immediately gives `p_xy<=2/3`, contradicting the strong-majority assumption `p_xy>2/3`. Together with `p_xy>2/3` being the counterexample orientation, this closes that endpoint and therefore the minimal-counterexample route.

Equation (7.1) is equivalent to endpoint balance, so it is **not by itself a substitute proof obligation**. The substantive advance is that (3.3)–(4.7) identify the only two exact masses that can supply it and eliminate all other exchange-fiber ambiguity. The seven-element witness proves that endpoint-local Hasse/delayed-distinguisher data alone do not imply it. The next mechanism must therefore transport mass across at least one later majority boundary (or use the ideal-block recurrence globally) and show that suppressing `Q+R` below `2E/3` necessarily creates a balanced pair elsewhere.

A concrete transport target is to charge each unit of endpoint channel excess

`U_1+U_2-R = D > E/3`

to the first later relation that distinguishes `s_1,s_2`; any charge not returned as a reverse remainder must be shown to contribute to a later pair whose ordering probability enters `[1/3,2/3]`. The 79-extension witness demonstrates why the alternative balanced-pair output is indispensable.

## 8. Verification

The companion standard-library verifier exhaustively checks Theorem 3.1 on every distinct forward-labelled transitive closure on `n=2,3,4,5` vertices and every ordered incomparable pair satisfying (H). It checks

- `|Ω_+|-|Ω_-| = E-Q-R`,
- `2|Ω_-|=Q+R`,
- `2I=Q-R`, and
- `Σ_q |C_q|=E-Q`.

Coverage: `406` distinct closures and `2999` qualifying ordered incomparable-pair cases, with no failure.

It separately reconstructs the `79`-extension team witness and verifies `R=0`, `U_3=9`, `U_4=20`; and reconstructs the partner `m=3,r=1` family, verifying `E=168`, `|Ω_+|=120`, `Q=88`, `R=8`. Terminal marker:

`POS3_ENDPOINT_EXCHANGE_IDENTITY_PASS`.

The exhaustive computation is regression evidence. The arbitrary-size theorem is the proof in Section 3.

## 9. Status and provenance

**Outcome:** `ESSENTIAL_STEP_APPLIED_WITH_LOCAL_CLOSURE_REFUTED`. The width-three `1/3–2/3` target remains open.

No benchmark gold, held-out keys, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email, Drive, paid model/API/Codex execution, remote workflow, public posting, or permission change was used. No claim of novelty or priority is made.
