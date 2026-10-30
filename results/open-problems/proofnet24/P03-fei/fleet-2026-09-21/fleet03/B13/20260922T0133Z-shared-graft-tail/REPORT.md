# B13 — the recursive shared-graft obstruction converges, but two more rounds raise the FEI floor

**Outcome:** `CANDIDATE_REFUTED` for freezing the balanced center at the preceding `F_4` cap, together with a **PROVED structured-family tail theorem**.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; authenticated repository sources were read directly, but no authenticated installed mathematical/cognitive brain retrieval was delivered into the reasoning context.

## 0. Exact live target and prior missing implication

The current owner target is the all-gate inequality

\[
\Gamma(p_{\rm out})+\widetilde H_G(p)
\le
\sum_i \operatorname{It}_i(G;p)
\frac{\Gamma(p_i)+h(V_{p_i})}{V_{p_i}},
\qquad V_u=4u(1-u),
\tag{G}
\]

for every Boolean gate and every product bias. At the all-unbiased point of a balanced gate this reduces to

\[
H(G)\le \Gamma(1/2)[I(G)-1].
\tag{0.1}
\]

Thus every finite universal gate potential must have center at least the supremum of the balanced excess ratio

\[
R(G):=\frac{H(G)}{I(G)-1}.
\tag{0.2}
\]

The named other-account result consumed substantively is

`proofnet24/P03-fei/fleet-2026-09-21/fleet01/B18/20260922T0117Z-recursive-shared-graft/REPORT.md`, report blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.

It proves the exact shared-graft recurrence for a source-valid balanced monotone Boolean family. The immediate source continuation used for the certified starting interval is

`proofnet24/P03-fei/fleet-2026-09-21/fleet03/B18/20260922T011005Z-recursive-shared-graft-extension/REPORT.md`, blob `4d1e86bd941df8bb941ba974f6478bbe4842ef84`.

That continuation had reached `F_4` and explicitly left the next implication open: analyze the recurrence as a tail before freezing yet another scalar center cap. It certified

\[
R_4\in[
6.5218509485644448965490881329959858569477358114202361,
6.5218509485644448965496895824490791318643557898359042].
\tag{0.3}
\]

This run directly resolves that particular family-level tail question rather than introducing a new FEI route.

## 1. Exact recurrence consumed and continued

Let `F_t` denote the iterated balanced monotone shared-core gates and let `c_t` be the distinguished singleton Fourier coefficient. The peer theorem gives, with

\[
\alpha=\frac9{256},\qquad
\phi(x)=-x\log_2x,
\]

\[
I_{t+1}=\frac{261}{128}+\alpha(I_t^4-1),
\tag{1.1}
\]

\[
c_{t+1}=\frac{57}{256}+\frac{c_t^4}{256},
\tag{1.2}
\]

and

\[
\boxed{
R_{t+1}-R_t
=
\frac{K(c_t^4)-\frac{133}{128}R_t}
     {\frac9{256}I_t^4+\frac{257}{256}},
}
\tag{1.3}
\]

where

\[
K(b)=H_{\rm core}(b)+\frac9{256}
\left[-\phi(b^2)+16(1-b^2)\right].
\tag{1.4}
\]

The source values are

\[
I_1=\frac{68013}{32768},\qquad
c_1=\frac{14593}{65536}.
\tag{1.5}
\]

Every recurrence step is an actual finite balanced monotone Boolean construction: first take four levels of disjoint self-composition of `F_t`, then apply the same source-valid nine-host shared-core transform. Therefore the quantities below are not arbitrary spectral laws.

## 2. A small derivative lemma makes the next rounds cheap to certify

The direct rational checker becomes unnecessarily expensive if the enormous exact denominator of `c_t^4` is inserted into every logarithm. A dyadic enclosure removes that cost without weakening the theorem.

For the fixed source core, let `A_S` and `Q_S` be the integer Walsh numerators in

\[
r_S(b)=\frac{A_S+bQ_S}{512}.
\]

The exact reconstructed source gives

\[
|A_S|\le114,\qquad |Q_S|\le18,
\tag{2.1}
\]

and the least nonzero absolute values of either integer family are both `2`.

### Lemma 2.1 — local Lipschitz bound

For

\[
\frac1{500}\le b\le\frac3{1000},
\]

\[
\boxed{|K'(b)|<292.}
\tag{2.2}
\]

**Proof.** If `r_S(b)` is nonzero, then either `A_S=0`, in which case

\[
|r_S(b)|\ge \frac{2/500}{512}=\frac1{128000},
\]

or `A_S\ne0`, in which case

\[
|A_S+bQ_S|\ge2-18\frac3{1000}>1.9.
\]

Also

\[
|r_S(b)|<\frac{115}{512}.
\]

Hence for every nonzero squared coefficient `w=r_S(b)^2`, because `128000<2^{17}`,

\[
2^{-34}<w<1,
\]

so for `\phi(w)=-w\log_2w`,

\[
|\phi'(w)|<34+\frac1{\ln2}<36.
\]

Therefore

\[
\left|\frac d{db}H_{\rm core}(b)\right|
<512\cdot36\cdot2\frac{115}{512}\frac{18}{512}
=291.09375.
\]

For the scalar correction in (1.4), on the same interval `b^2>2^{-18}` and `b<0.003`, so its derivative has magnitude below `1`. This proves (2.2). `\square`

The checker replaces each exact `b=c_t^4` by its nearest denominator-`2^64` dyadic `q`, computes `K(q)` with exact rational atanh-series logarithm enclosures, and expands by `292|b-q|`. The two dyadic approximation errors are below `1.61e-20` and `3.11e-21`; the resulting `K` widths are far smaller than the numerator gaps below.

## 3. Two further strict source-valid gains

Starting from the padded source-certified `R_4` interval in (0.3), the exact checker proves

\[
\boxed{
R_5\in[
6.5218509495504459457942635364161356872620081623200816328863622300216178,
\]
\[
6.5218509495504459458576465143225875181210038245663837618373652405804790].
}
\tag{3.1}
\]

In particular the lower endpoint exceeds the **upper** endpoint used for `R_4` by

\[
\boxed{
9.86001049244573953967056555397652372484167432886362\times10^{-10}.
}
\tag{3.2}
\]

One more actual Boolean shared-graft step gives

\[
\boxed{
R_6\in[
6.5218509495504481848190319299878158287105279434983773429918090394322216,
\]
\[
6.5218509495504481848824149770395541197961122790612205924109263953322714].
}
\tag{3.3}
\]

The second strict gain, again comparing the new lower endpoint with the preceding upper endpoint, is

\[
\boxed{
2.238961385415665228310589524118931993581154444\times10^{-15}.
}
\tag{3.4}
\]

The exact influence recurrence yields

\[
I_6=101073061.7639185353334685056928379347999\ldots
\tag{3.5}
\]

and

\[
I_7=3.6689705968441394100100955366304446\times10^{30}\ldots .
\tag{3.6}
\]

Consequently the balanced-uniform center obstruction is now rigorously above

\[
\boxed{6.521850949550448.}
\tag{3.7}
\]

Equivalently, relative to the historical read-once center `C_0=6.4548`, this actual Boolean gate forces a quadratic-margin coefficient above

\[
4(R_6-C_0)>0.268203798201792\ldots .
\tag{3.8}
\]

Thus any proposed all-gate center cap frozen at the preceding `F_4` level is **REFUTED**. Full FEI is not refuted: this is a stronger lower bound on any universal constant.

## 4. The same recurrence cannot run away to infinity

The more important structural point is that this **specific** repeated shared-graft mechanism has a finite tail.

In the physical source representation, the no-fresh-coordinate vector equals `a+b\sum_jQ_j`. It has 494 entries of absolute value `1` and 18 entries of absolute value `b`. Therefore its squared Fourier mass is

\[
m(b)=\frac{494+18b^2}{512}\le1
\quad (0\le b\le1).
\tag{4.1}
\]

There are 512 Fourier atoms, so concavity gives

\[
0\le H_{\rm core}(b)\le9.
\tag{4.2}
\]

Also for `x\in[0,1]`,

\[
\phi(x)=-x\log_2x\le\frac{1-x}{\ln2}<2(1-x),
\tag{4.3}
\]

hence

\[
0\le16(1-x)-\phi(x)\le16.
\]

Thus, globally on this recurrence,

\[
\boxed{0\le K(b)\le9+\frac9{256}16=\frac{153}{16}.}
\tag{4.4}
\]

Put

\[
D_t:=I_{t+1}-1=\frac9{256}I_t^4+\frac{257}{256}.
\tag{4.5}
\]

Since `D_6=I_7-1` is already larger than `3.6\times10^{30}`, and

\[
D_{t+1}\ge\frac9{256}D_t^4\ge D_t^2
\quad(t\ge6),
\tag{4.6}
\]

the denominators thereafter grow at least by repeated squaring.

Because the certified `R_6<7<10` and

\[
\frac{153}{16}<10\frac{133}{128},
\]

the recurrence (1.3) preserves `0\le R_t\le10` for every later `t`. Therefore

\[
\left|K(c_t^4)-\frac{133}{128}R_t\right|
\le\frac{665}{64}
\quad(t\ge6).
\tag{4.7}
\]

Combining (4.6)-(4.7),

\[
\sum_{t\ge6}|R_{t+1}-R_t|
\le
\frac{665}{64}
\left(\frac1{D_6}+\frac1{D_6^2}+\frac1{D_6^4}+\cdots\right)
\le
\frac{665/64}{D_6-1}.
\tag{4.8}
\]

The checker evaluates the last quantity exactly and obtains

\[
\boxed{
|R_\infty-R_6|
<2.832027329119913\times10^{-30}.
}
\tag{4.9}
\]

Hence this source-valid infinite shared-graft recurrence converges. It cannot by itself generate an unbounded FEI-ratio sequence. This is a structured-family theorem only; it supplies no universal FEI upper bound.

## 5. Consequence for the full problem

Balanced self-composition of any finite balanced gate `F` has ordinary `H/I` tending to `H(F)/(I(F)-1)`. Applying that exact identity to the finite Boolean gate `F_6` gives the source-valid lower bound

\[
\boxed{
C_{\rm FEI}>6.521850949550448.
}
\tag{5.1}
\]

This improves the preceding certified `F_4` floor but does **not** prove finiteness of `C_FEI`.

The important replacement obligation is now sharper:

1. do **not** freeze an all-gate potential center below (5.1);
2. do **not** expect this particular repeated shared-core recurrence to diverge — its entire future tail is bounded by (4.9);
3. the remaining universal implication is still to prove one finite bound for
   \[
   \sup_{G\ \mathrm{balanced}}\frac{H(G)}{I(G)-1},
   \]
   equivalently to construct a finite-cap symmetric nonnegative `\Gamma` satisfying (G) for every gate/bias.

The next useful attack should therefore either derive a universal envelope that survives the shared-coordinate correction `K`, or produce a genuinely different composition-prime/shared-coordinate gate mechanism that escapes the finite recurrence above.

## 6. Required handoff fields

- `exact_candidate_version`: all-gate `(G)` with the successor center frozen at the preceding source-certified `F_4` balanced cap.
- `prior_missing_implication`: determine whether the source-valid shared-graft recurrence continues raising the center indefinitely before freezing another cap.
- `new_proved_inference`: `F_5` and `F_6` give two further strict Boolean gains; the complete later recurrence is absolutely summable with tail below `2.833e-30` after `F_6`.
- `exact_failed_claim`: any universal all-gate center cap at or below the preceding `F_4` level.
- `replacement_obligation`: prove a finite universal balanced-excess upper bound / all-gate potential above the new floor; further lower-bound work needs a mechanism other than mere continuation of this recurrence.
- `consumed_peer_artifact`: fleet01/B18 `20260922T0117Z-recursive-shared-graft/REPORT.md`, blob `cbe682d84b52232ab4e91367b08bbfe73d74a39e`.
- `applied_to_claim`: exact recurrence (1.1)-(1.4) and the balanced-center obstruction in the all-gate reformulation.
- `remaining_implication`: one finite dimension-independent upper constant for all balanced Boolean gates, equivalently full FEI.
- `next_recipient`: primary `fleet03/B18` (all-gate lead), secondary `fleet01/B18` (shared-graft recurrence owner).
- `full_problem_change`: OPEN -> OPEN; lower floor strengthened, one candidate cap refuted, one explicit repeated mechanism proved bounded.

## 7. Reproduction and scope

`CHECKER.py` reconstructs the published source truth table and refuses it unless the inherited SHA-256 matches. It verifies the source influence, integer core Walsh bounds, exact `c_t` and `I_t` recurrences, computes the two needed `K` values at nearby denominator-`2^64` dyadics with rational atanh-series remainder bounds, applies Lemma 2.1 to reach the exact recurrence points, proves both strict gains, and checks the tail bound. `CHECK_OUTPUT.txt` records `PASS`.

No publication-priority or novelty claim is made. The result is source-bound mathematics inside the private research programme. It does not convert finite/structured evidence into a universal theorem and it leaves full uniform-cube FEI **OPEN**.
