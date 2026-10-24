# Addendum — latest account04/B10 predecessor funnel consumed

After the main report was committed, fresh shared state supplied a newer named-partner result:

- account04/B10 run `20260922T031005Z-B10-POS3-r11`, report blob `fb5b7e5f9b8e596f4b6bafff4d56164094336361`.

It proves that at the inherited first-boundary sibling fork the predecessor sets are always nested. After relabelling,

`Pred(b) subseteq Pred(a)`,

and the proper difference

`D=Pred(a)\Pred(b)`

is a delayed chain. This sharpens the lower-distinguisher branch identified in the main B19 report. The cut-charge identity has a particularly simple exact specialization to this new partner state.

## 1. Predecessor-difference deletion identity

Write the delayed difference chain as

`D={d_1<...<d_k}`

and put `Q=P\D`. Since every `d_j<a` and `d_j||b`, deleting `D` makes the two sibling predecessor sets equal inside `Q`:

`Pred_Q(a)=Pred_Q(b)`.

The induced law on `L(Q)` is still the exact nonuniform chain-deletion law; it is **not** replaced by the uniform law.

Let `E=e(P)`. For each `d in D`, because `d<a`,

`B_P(a,d)=-E`.

Hence

`B_P(a,d)-B_P(b,d)=-2 N_P(b<d)`.

Substituting this into the cut-charge identity from the main report gives the exact rank correction

`R_Q^D(a,b)-R_P(a,b)=sum_{d in D} N_P(b<d)`.             `(PD)`

Normalized,

`E_{mu_D}[r_Q(b)-r_Q(a)] - E_P[r_P(b)-r_P(a)]`

`= sum_{d in D} Pr_P(b<d)`.                               `(PDn)`

Thus the whole bias introduced by deleting the strict predecessor-difference chain is a positive, explicit sum of actual sibling/distinguisher pair probabilities. No corridor error term is hidden.

## 2. Exact crossing trichotomy on the delayed chain

Set

`p_j=Pr_P(b<d_j)`.

Because `d_1<...<d_k`, the events are nested:

`{b<d_j} subseteq {b<d_{j+1}}`,

so `p_1<=...<=p_k`, and in fact

`p_{j+1}-p_j = Pr_P(d_j<b<d_{j+1})`.                      `(X)`

Therefore one of the following holds:

1. some pair `(b,d_j)` is already balanced;
2. all `p_j<1/3`;
3. all `p_j>2/3`; or
4. there is a unique threshold `j` with `p_j<1/3<p_{j+1}` and, because no value is allowed in `[1/3,2/3]`, necessarily

   `Pr_P(d_j<b<d_{j+1})=p_{j+1}-p_j>1/3`.                `(BIG-GAP)`

In a hypothetical POS3 counterexample alternative 1 is excluded, so every strict nested-predecessor corridor is forced into one of the three exact extreme regimes 2–4.

If the larger-predecessor sibling is majority-early, `a prec_* b`, then every `d_j prec_* a prec_* b`, hence the no-balanced hypothesis forces `p_j<1/3` for all `j`; `(PDn)` is then `<k/3`.

If it is majority-late, `b prec_* a`, the delayed chain may lie wholly before `b`, wholly after `b`, or straddle `b` in the strong-majority order. These are exactly the low-correction, high-correction and `BIG-GAP` cases above. In particular, if all `d_j` lie after `b`, `(PDn)>2k/3`; if the chain straddles `b`, one adjacent chain gap contains `b` in more than one third of all extensions.

## 3. Effect on the current global residual

The newest account04/B10 report asks to follow the top delayed predecessor difference together with the first minimal successor blocker while retaining its endpoint counts `Q,R`. The identities `(PD)`–`(BIG-GAP)` supply the exact chain side of that coupling:

- the chain-deletion rank shift is no longer an unspecified weighted-corridor effect;
- it is the sum of actual `b`-vs-`D` pair probabilities;
- unless one such pair is balanced, the delayed chain is forced to one side of the `1/3–2/3` band, except for a single adjacent gap carrying probability `>1/3`.

The next proof step should combine this three-way predecessor-corridor regime with the partner's endpoint polarity (`Q+R<2E/3` in the majority-early case, `Q+R>4E/3` in the majority-late case), its first minimal successor blocker, and the inherited next-boundary/heavy-slice constraints. A contradiction must arise from one of: a balanced `b,d_j`; a `BIG-GAP` event incompatible with the successor channel; a four-antichain; a proper autonomous nonchain; or a strict span descent.

This addendum does not claim that the crossing trichotomy alone closes POS3. It converts the latest partner's strict nested-predecessor corridor into exact pair probabilities under the original uniform law, while preserving the nonuniform projected law exactly.
