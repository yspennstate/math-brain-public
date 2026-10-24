# Addendum II — nested-predecessor endpoint escalation without an equality hypothesis

This addendum applies the newest named partner result, account04/B10 report blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`, together with account01/B11's exact endpoint exchange. It pays the majority-early half of the partner's new strict nested-predecessor corridor.

Assume the hypothetical no-balanced width-three state. At the inherited first-boundary sibling pair relabel so that

`Pred(b) subseteq Pred(a)`.

The newest partner proves that the proper difference is a delayed chain. Let

`M=Min{z : a<z and z||b}`,

`Q=#{L : b precedes every m in M}`,

and let `R` be the exact reverse nonneutral-blocker remainder. Account01/B11 gives

`Pr(a<b)=1-(Q+R)/(2E)`

and the forward endpoint channels `C_m`, `m in M`, are disjoint with total mass

`sum_{m in M}|C_m|=E-Q`.                                     `(E1)`

## Theorem — majority-early nested-predecessor span/fork escalation

Suppose the sibling carrying the larger predecessor set is majority-early:

`a prec_* b`.

Then exactly one of the following structural outcomes occurs.

1. **Strict span descent.** There is `m in M` with
   `a prec_* m prec_* b` and `a<_P m`, `m||b`.
2. **Two-blocker fork escalation.** `M={m_1,m_2}`, the triple
   `{b,m_1,m_2}` is an antichain, both blockers lie after `b` in the strong-majority order, the total canonical forward-channel mass is `>E/3`, and at least one channel has mass `>E/6`.

This conclusion requires only the nested-predecessor endpoint theorem, not `Pred(a)=Pred(b)`.

### Proof

Since `a prec_* b` in a no-balanced candidate,

`Pr(a<b)>2/3`.

The exact endpoint identity therefore gives

`Q+R<2E/3`, hence in particular `Q<2E/3`.                    `(E2)`

It also forces `M` to be nonempty: if `M` were empty then `Q=E`, contradicting `(E2)`.

Distinct elements of `M` are incomparable by minimality. Every member of `M` is incomparable with `b` by definition. Hence `{b} union M` is an antichain, and width at most three gives

`1<=|M|<=2`.                                                   `(E3)`

Take `m in M`. Since `a<_P m`, the strong-majority order, which extends the poset, has `a prec_* m`. If `m prec_* b`, then

`a prec_* m prec_* b`,

which is outcome 1.

Suppose no such blocker exists. Then `b prec_* m` for every `m in M`. Because `b||m` and there is no balanced pair,

`Pr(b<m)>2/3`.                                                 `(E4)`

If `|M|=1`, the event defining `Q` is exactly `{b<m}`, so `(E4)` gives `Q>2E/3`, contradicting `(E2)`. Therefore `|M|=2`.

The two blockers are incomparable by minimality, and both are incomparable with `b`; hence they form the stated width-saturating fork after `b`. Finally `(E1)` and `(E2)` give

`|C_{m_1}|+|C_{m_2}|=E-Q>E/3`,

so one of the two disjoint channels has mass `>E/6`. This is outcome 2. `□`

## Why this matters

The campaign's earlier span/fork theorem required equal predecessor sets. The newest partner reduced every first-boundary sibling pair to **nested** predecessor sets with a chain difference. The theorem above shows that, in the majority-early orientation, strict nesting causes no new structural exception: the exact same span-descent versus quantitative two-blocker-fork alternative survives.

The blockers in `M` are minimal `a`-successors incomparable with `b`; unlike the equal-predecessor case, they are not asserted here to be Hasse covers of `a`, because an intermediate common successor of `a,b` may exist. The proof does not need that stronger claim.

Thus the remaining genuinely new nested-predecessor obstruction is concentrated in the **majority-late larger-predecessor orientation** `b prec_* a`, where the endpoint identity gives `Q+R>4E/3` and `Q>2E/3` when `M` is nonempty. The first addendum's predecessor-difference-chain identity and crossing trichotomy are tailored to that residual.

## Additional exact majority-late fact when there is no successor distinguisher

If there is no successor distinguisher at all, then `M=empty`, so `Q=E`. The only possible reverse nonneutral blockers are elements of the predecessor-difference chain `D`. Writing its top element as `d_top`, a reverse extension `b...a` contains some element of `D` between the endpoints iff it contains `d_top` between them. Therefore

`R/E = Pr(b<d_top)`.

The endpoint identity becomes

`Pr(a<b) = (1-Pr(b<d_top))/2`.                                `(E5)`

In a hypothetical no-balanced candidate this branch is necessarily majority-late. Since `Pr(a<b)<1/3`, `(E5)` gives `Pr(b<d_top)>1/3`; absence of a balanced pair strengthens this to

`Pr(b<d_top)>2/3`

and consequently

`Pr(a<b)<1/6`, equivalently `Pr(b<a)>5/6`.                    `(E6)`

So the no-successor-distinguisher subbranch is not merely extreme; it is forced beyond the `5/6` endpoint threshold. This is an exact quantitative target for the inherited pinned-rank/heavy-slice constraints.

POS3 remains open. The next global implication is now concentrated in the majority-late nested-predecessor corridor (especially the `>5/6` no-successor subcase) and in propagating a quantitative two-blocker fork across a later boundary without losing the original uniform-law multiplicities.
