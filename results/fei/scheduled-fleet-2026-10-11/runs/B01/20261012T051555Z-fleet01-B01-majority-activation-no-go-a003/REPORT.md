# B01 / A003 — majority obstruction to a local retained-U contraction

**Run:** `20261012T051555Z-fleet01-B01-majority-activation-no-go-a003`  
**Primary packet:** A003, minimal target formulation  
**Stable gap:** `G-UPPER-SET-ASYMMETRY`  
**Attempt:** `A003-GUP-MAJORITY-NOGO-2`  
**Status:** a precise local-transfer no-go theorem is author-proved and pending A086/A094 review. Full FEI remains **OPEN**.

## 1. Frozen target and previous status

For `p(S)=hat f(S)^2`, `pi(S)=sum_{T superset S}p(T)`, set

`U(f)=sum_S p(S) log_2(pi(S)/p(S))`

and

`G(f)=sum_i [U(f)-E U(f|x_i)]`.

The universal B01 target remains

`G(f) <= a I(f)+b U(f)`

for every Boolean `f`, with absolute `a<infinity` and `b<1`. The established implications are

`GU'(a,b), b<1  =>  U(f)<=a/(1-b) I(f)  =>  H(f)<=(2+2a/(1-b))I(f)`.

The previous B01 run proved an exact fresh-activation identity and a one-layer transfer with a child charge `<19.530 p I(g)` plus selector charge `<4.947 I_ctl`; it also proved a restricted parity-activation FEI endpoint. Its unresolved issue was whether the child charge could be replaced by a depth-free payment using only the selector and the newly created `U` increment.

This run froze that proposed strengthening before testing it:

`LT(A,B): G(F)-pG(g) <= A I_ctl + B[U(F)-pU(g)]`

with fixed finite `A,B`, for every Boolean core `g` and one fresh activation selector. If true, `LT` would have removed the per-level reuse of `pI(g)` in nested fresh activations. The theorem below proves `LT(A,B)` false for every fixed pair `A,B`.

## 2. Exact Boolean obstruction

For odd `n`, take balanced majority

`g_n(x)=sign(x_1+...+x_n)`

and one fresh selector `z`, with

`F_n(z,x)=g_n(x)` on one value of `z`, and `F_n(z,x)=1` on the other.

This is a genuine Boolean family on the uniform cube. It has activation probability `p=1/2`, depth `d=1`, defect rate `r=1/2`, and exactly

- `I_ctl(F_n)=1/2`;
- `U(F_n)-(1/2)U(g_n)=1`;
- `G(F_n)-(1/2)G(g_n)=(1/pi)log_2 n+O(1)`.

Consequently, for every finite real `A,B`, some odd `n` satisfies

`G(F_n)-(1/2)G(g_n) > A I_ctl + B[U(F_n)-(1/2)U(g_n)] = A/2+B`.

Thus a selector-only plus retained-increment local contraction cannot be the missing depth-independent GU' bridge.

## 3. Proof and the precise unpaid term

The source-pinned activation identity writes

`G(F)=pG(g)+d delta_d(r)+sum_j J_R(r;r_{j,+},r_{j,-})`,

where

`J_R=R_p(r)-[R_p(r_{j,+})+R_p(r_{j,-})]/2`,

`R_p(r)=M(pr)-pM(r)+4pr^2 log_2(1/r)-4p^2r^2 log_2(1/(pr))`,

and `M(t)=(1-2t)^2 log_2(1/(1-2t)^2)`.

For odd majority, every coordinate has influence

`a_n=binom(n-1,(n-1)/2)/2^(n-1)`,

and the two conditional defect rates are `(1+a_n)/2` and `(1-a_n)/2`. Split

`R_p(t)=-pM(t)+S_p(t)`.

At the balanced midpoint, `M(1/2)=0` while

`M((1+/-a_n)/2)=a_n^2 log_2(1/a_n^2)`.

Therefore every data coordinate contributes exactly

`p a_n^2 log_2(1/a_n^2) + J_S`.

For `p=1/2`, `S_p` is twice continuously differentiable on `[1/4,3/4]`, so Taylor's theorem gives `|J_S|<=C a_n^2`. Hence

`G(F_n)-(1/2)G(g_n)=1+(1/2)n a_n^2 log_2(1/a_n^2)+O(n a_n^2)`.

Stirling gives `n a_n^2=2/pi+O(1/n)` and `log_2(1/a_n^2)=log_2 n+log_2(pi/2)+O(1/n)`, proving the claimed asymptotic.

The divergent term is therefore the aggregate first-level logarithmic mismatch

`p sum_j a_{n,j}^2 log_2(1/a_{n,j}^2)`.

In the `Delta_i U=B_i-Gamma_i+KL_i` ledger it is the singular balanced contribution of the data-coordinate upper-set asymmetry. Its squared mass is bounded (`sum_j a_{n,j}^2=Theta(1)`), but spreading that mass over `n` coordinates creates the unpaid `log n`.

The full line-by-line proof is in `MAJORITY_ACTIVATION_NOGO.tex`.

## 4. Exact/direct verification

`CHECK.py` performs two independent checks:

1. direct truth-table Walsh computation of `U` and every restriction term in `G` for `n=1,3,5,7`, compared to the scalar activation identity;
2. exact central-binomial evaluation and 80-digit decimal evaluation of the scalar formula for every odd `n<=1001`.

Command:

`python CHECK.py`

The four direct comparisons agree to at least 60 decimal places. There are 1008 passing assertions. At `n=1001`, the exact scalar formula gives

`G(F_n)-(1/2)G(g_n)=5.096768554458...`,

with singular total `3.381503572883...` and bounded smooth total `0.715264981576...`.

The computation is corroborative; the all-odd-`n` theorem is analytic.

## 5. Movement and non-movement

**PROVED (author, pending independent review):** Every fixed local transfer paid only by fresh-selector influence and the new `U` increment fails, already for one fresh selector and balanced majority cores.

**PROVED (author, pending independent review):** The exact obstruction is a first-level spectral logarithmic charge, not a rare-selector logarithm. The earlier child term `pI(g)` cannot simply be deleted from the one-layer transfer by spending `I_ctl` and `U(F)-pU(g)`.

**NOT PROVED:** This does not refute universal GU'. Global GU' retains `pI(g)` and `pU(g)`, and majority has large total influence. It also does not refute FEI or produce unbounded `H/I`.

**Universal status:** No dimension-independent control of the aggregate upper-set asymmetry mismatch is proved. Full FEI remains OPEN.

## 6. Implication graph and next exact action

The current source-valid graph is:

- universal `GU'(a,b)` with `b<1` -> universal `U<=a/(1-b) I` -> universal FEI with constant `2+2a/(1-b)`;
- previous fresh-activation transfer + base-class GU' -> restricted fresh-activation GU' (pending review);
- proposed `LT(A,B)` -> depth-free selector/increment-only transfer **is now REFUTED**;
- paying the first-level logarithmic term once across a hierarchy -> possible repaired bridge (**OPEN**).

The next bounded action is to freeze and test a repaired one-layer statement with the explicit child credit

`L_1(g)=sum_j (r_{j,+}-r_{j,-})^2 log_2(1/(r_{j,+}-r_{j,-})^2)`

using the continuous convention at zero, then seek a nonreused hierarchy ledger for `pL_1(g)`. A valid repair must show where this credit is debited exactly once; bounding `L_1` separately by a dimension-dependent entropy is not progress toward universal GU'. Majority is the mandatory regression family.

## 7. Source pins and execution record

- Owner order blob: `81b6d6f988aee4489512c6e62543253900620453`.
- Case-target overlay blob: `97e41262ebb4f09eec53630a918acae09efc9a48`.
- Current-status blob read this run: `c416d4b4a83fc67965cb95d06a0cc80c5c29a520`.
- B01 compact contract blob: `ac038a028831d59ad053dd56b2b527e2a71ffdee`.
- Execution protocol blob: `457358ff62cbf1141a72096bcabdf95bf18c1be2`.
- Previous B01 report blob: `b769561f7df8773b8162ec3e2c18135a87de1ea0` at canonical commit `8344aa4aa688790494e3ebd46bb94b13f659ce18`.
- Previous exact activation proof blob: `fd291e847f0f7a21591398af6b415fa00787cd17` at the same commit.
- Configuration: natural scheduled execution; no worker launched; no protected source read; no paid compute; no scheduler mutation.
- Exposed model: GPT-5 Codex as identified by the runtime instructions; reasoning-effort setting was not exposed.
- Independent review: not performed in this run; route to A086 and A094.
- Native Brain ingestion: not claimed. The complete handoff is mirrored only as a repository artifact.

