# B16 Campaign C adversary — the half-band sparse defect forces the Ward refund coefficient 11/192 exactly

**Date:** 21 September 2026 UTC  
**Scope:** `fleet03 / B16`, FEI Campaign C under `FEI-PROOF-EXECUTION-20260921T230620Z`  
**Execution:** **WITHOUT_VERIFIED_BRAIN**  
**Outcome:** **ESSENTIAL_STEP_APPLIED (adversarial narrowing); full unrestricted FEI remains OPEN / NOT PROVED.**

## 0. Latest assignment and exact candidate attacked

The execution reset supersedes this slot's earlier generic interface-C assignment. The new assignment is:

> attack the **same net bound** with exact sparse-defect and tensor/asymptotic Boolean constructions.

No newer complete fleet02/B18 net-candidate report was visible at the source snapshot used here, so I apply the reset's explicit fallback and reconstruct the smallest source-exact candidate from the current completed C dependencies.

The named other-account theorem consumed is fleet04/B16,

`proofnet24/P03-fei/fleet-2026-09-21/fleet04/B16/20260921T211200Z-brownian-cayley-signed-remainder/REPORT.md`.

For each odd active syndrome `R`, it defines the central current multiplier `epsilon_R`, the Ward selector multiplier

\[
W_R=1-\frac1{q_R},
\]

and proves

\[
0\le\varepsilon_R\le \frac{11}{192}W_R,
\qquad
\rho_R:=\frac{11}{192}W_R-\varepsilon_R\ge0,
\tag{0.1}
\]

with equality precisely at `(q_R,k_R)=(3,1)`. For the authentic same-syndrome Brownian energy `I_R>=0`, the peer therefore has the exact algebraic decomposition

\[
\sum_R\varepsilon_R I_R
=rac{11}{192}\sum_RW_RI_R-\sum_R\rho_RI_R.
\tag{0.2}
\]

The peer correctly does **not** book `11/192` of the Ward square as a free negative compiler credit; that co-location/no-reuse statement is still unproved. Campaign C's smallest net candidate is therefore:

> **C-NET-WARD-v1.** Prove that the authentic pre-positive compiler ledger contains an unspent co-located Ward/R16/Shapley/terminal credit equal to at least `(11/192) sum_R W_R I_R`, or an equivalent collection of credits whose total dominates the same amount, before passing any nonnegative remainder to the physical sink.

If this booking theorem holds, (0.2) cancels the entire central Brownian current up to the already nonnegative `rho` refund. The task here is to attack its sharpness on the genuine half-band Boolean obstruction before accepting it as a plausible repair.

## 1. Stress family retained exactly

Consume the exact half-band construction in

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`.

Let `D>=128`, `N=2^D`, and `n=D-1`. The Boolean negative set is an affine two-plane of four physical points. All `n` original coordinates are relevant and

\[
J(f_D)=I(f_D)=\frac{8n}{N},
\qquad H(f_D)<4I(f_D).
\tag{1.1}
\]

At the actual half-band cutoff `d=ceil(D/2)`, the retained coefficient is the **authentic** difference between the affine code and terminal Reed--Muller code. The terminal code is therefore already inside the energy below; it is not discarded and cannot be charged again.

The active spectrum has exactly four charged triple modes with

\[
(q_R,k_R)=(3,1),
\tag{1.2}
\]

and four singleton odd modes with `q_R=k_R=1`, whose current multiplier is zero. The half-band theorem gives a genuine positive-current lower bound and proves that the terminal-code perturbation is asymptotically negligible in the same weighted norm.

## 2. PROVED — exact finite-D coefficient locking on the obstruction

For `(q,k)=(3,1)`, the central multiplier is

\[
\varepsilon_*=
2\frac{2^{-3}}3\left(\frac{2^{-1}}1-\frac{2^{-3}}3\right)
=\frac{11}{288},
\tag{2.1}
\]

while

\[
W_*=1-\frac13=\frac23.
\tag{2.2}
\]

Hence

\[
\boxed{\varepsilon_*=\frac{11}{192}W_*},
\qquad \rho_*=0.
\tag{2.3}
\]

Let

\[
C_D:=\sum_R\varepsilon_R I_R,
\qquad
\mathcal W_D:=\sum_RW_RI_R
\tag{2.4}
\]

for the actual retained half-band packet of this family. Because every nonzero central-current mode is a `(3,1)` mode and every singleton mode has both central current and Ward multiplier zero,

\[
\boxed{C_D=\frac{11}{192}\,\mathcal W_D}
\tag{2.5}
\]

**exactly at every finite `D` for which this packet is defined**, independent of the detailed retained coefficient values `I_R`. In particular, the terminal-code subtraction, same-syndrome cancellation, and finite live window cannot perturb the ratio (2.5): they alter `I_R`, but both sides carry the same `I_R`.

This is stronger than an asymptotic comparison. It says the sparse-defect obstruction is an exact equality case for the proposed Ward compensation coefficient.

## 3. PROVED — any smaller fixed Ward booking still fails exponentially against `J`

The half-band source proves for `D>=128` that the **full** current has

\[
\int_{40}^{S_f}E_{\rm cur}(s)\frac{ds}{s^3}
\ge \frac{7}{3145728\,n^3}.
\tag{3.1}
\]

On the four charged modes the full multiplier is `e_*=4/9`, while the central multiplier is `epsilon_*=11/288`; their ratio is

\[
\frac{\varepsilon_*}{e_*}=\frac{11}{128}.
\tag{3.2}
\]

Therefore the same exact packet gives

\[
\boxed{
C_D\ge \frac{77}{402653184\,n^3}.
}
\tag{3.3}
\]

Using (2.5),

\[
\boxed{
\mathcal W_D\ge \frac{7}{2097152\,n^3}
=\frac7{2^{21}n^3}.
}
\tag{3.4}
\]

Now suppose a proposed booked Ward credit has coefficient `a_D` and no other independent, nonreused credit has yet been supplied. Its residual on this exact Boolean family is

\[
C_D-a_D\mathcal W_D
=\left(\frac{11}{192}-a_D\right)\mathcal W_D.
\tag{3.5}
\]

For every `a_D<11/192`, (3.4) and (1.1) imply

\[
\boxed{
\frac{C_D-a_D\mathcal W_D}{J(f_D)}
\ge
\left(\frac{11}{192}-a_D\right)
\frac{7\,2^D}{2^{24}n^4}.
}
\tag{3.6}
\]

Consequences:

1. **Every fixed coefficient `a<11/192` is refuted** as a stand-alone Ward repair: the right-hand side of (3.6) tends to infinity.
2. More sharply, if `delta_D=11/192-a_D>0` and
   \[
   \delta_D\,\frac{2^D}{n^4}\to\infty,
   \tag{3.7}
   \]
   the residual is still not `O(J)`.
3. Thus on this family a subcritical Ward coefficient must approach the sharp value to essentially exponential accuracy unless a **separate authentic credit of order `n^{-3}`** is booked at the same live stage.

This is an adversarial theorem about the actual retained half-band source, not a non-Boolean relaxation.

## 4. PROVED — the sharp coefficient exactly neutralizes this obstruction, so the next issue is booking, not constant optimization

At

\[
a=\frac{11}{192},
\tag{4.1}
\]

equation (2.5) gives

\[
\boxed{C_D-a\mathcal W_D=0}
\tag{4.2}
\]

exactly on the sparse-defect half-band packet. Equivalently `rho_R=0` on every charged mode.

Therefore this construction does **not** refute the sharp algebraic candidate (0.2). It instead proves that the coefficient `11/192` is forced by the current obstruction: there is no room to weaken it by a dimension-independent factor and hope that the ordinary influence budget absorbs the difference.

The decisive remaining implication is consequently not another kernel bound. It is the source-side **booking theorem**:

\[
\boxed{
\text{show that }\frac{11}{192}\sum_RW_RI_R
\text{ is an actually unspent, co-located R16/Shapley/terminal/entropy credit,}
}
\tag{4.3}
\]

or exhibit a different authentic credit of the same size, with no reuse. Only after (4.3) is proved can (0.2) be spent as a net cancellation. A comparison bank, a post-square inequality, or a credit already used in the terminal/high-resolvent estimate is insufficient.

## 5. Quantitative obligation for any alternative net repair

Suppose an alternative authentic net decomposition on this family is

\[
\operatorname{NET}_D=C_D-a_D\mathcal W_D-X_D,
\tag{5.1}
\]

where `X_D` denotes the sum of **additional independently booked nonnegative credits** after removing any double-counted terminal contribution already present in `I_R`. If one wants `NET_D<=C J(f_D)` for a fixed universal `C`, then (3.4) forces

\[
\boxed{
X_D\ge
\left(\frac{11}{192}-a_D\right)_+
\frac7{2^{21}n^3}
-C\frac{8n}{2^D}.
}
\tag{5.2}
\]

So if `a_D` stays a fixed amount below `11/192`, an alternative credit must supply a genuine `Theta(n^{-3})` cancellation. An `O(J)=O(n2^{-D})` bookkeeping correction is exponentially too small. This gives fleet02/B18 a concrete falsification criterion for any proposed NET ledger.

## 6. Asymptotic leading constants

The source also proves the sharper weighted-energy asymptotic: each charged triple has

\[
I_R\sim \frac1{12n^3}.
\tag{6.1}
\]

Hence

\[
C_D\sim \frac{11}{864n^3},
\qquad
\mathcal W_D\sim \frac{2}{9n^3},
\tag{6.2}
\]

and for `delta_D=11/192-a_D`,

\[
C_D-a_D\mathcal W_D
\sim \frac{2\delta_D}{9n^3}.
\tag{6.3}
\]

Dividing by `J=8n/2^D` gives

\[
\boxed{
\frac{C_D-a_D\mathcal W_D}{J(f_D)}
\sim \frac{\delta_D}{36}\frac{2^D}{n^4}.
}
\tag{6.4}
\]

This agrees with the exact lower-bound scale (3.6).

## 7. Attempted tensor amplification — not source-admissible yet

A natural adversarial move is to tensor several copies of the four-point defect. The ordinary spectral quantities would behave cleanly under disjoint products (`H` and `I` are additive). I did **not** use that as a compiler counterexample, because the retained terminal code `RM(d,D)^perp`, the active q-flip syndrome law, and the same-syndrome Brownian energies have not been proved to factor under that tensor operation. Claiming current/refund additivity here would repeat the kind of surrogate substitution the new execution order forbids.

The existing one-parameter sparse family `D->infinity` already gives the exponential stress (3.6) without such an unproved tensor factorization. Tensor amplification remains a possible next adversary only after the exact NET candidate is shown to tensorize.

## 8. What this does and does not settle

### PROVED / applied

- The genuine half-band sparse-defect packet is an **exact equality case** for `epsilon_R <= (11/192)W_R`.
- Any Ward refund coefficient below `11/192` by a fixed amount leaves a residual whose ratio to `J` diverges exponentially.
- More generally, the gap must be exponentially small on this family unless another co-located credit of order `n^{-3}` is present.
- The sharp `11/192` coefficient cancels the central-current obstruction exactly, including the retained terminal-code effect inside `I_R`.

### OPEN

- Whether `11/192` of the Ward selector bank is genuinely an **unspent compiler credit** at the correct pre-positive stage.
- If not, whether the exact R16/Shapley/negative-entropy/terminal ledger supplies an alternative `Theta(n^{-3})` credit on this family without reuse.
- A complete NET identity whose booked credits imply a universal `O(J)` bound.
- Full FEI.

### REFUTED / dead route

- Any stand-alone Ward repair with fixed coefficient `a<11/192`.
- Treating the terminal-code perturbation as a possible way to change the sharp coefficient: it is already inside `I_R` and cancels from the ratio (2.5).
- Unproved tensor amplification of this compiler packet.

## 9. Next attack / handoff

**Next recipient:** `fleet02/B18` Campaign-C lead, with `fleet01/B16` and the fleet04/B16 signed-remainder source as derivation partners.

The next proof step should not optimize kernels. It should write the exact authentic R16/Shapley/terminal/negative-entropy NET ledger at the same stage as `I_R` and answer one binary question:

> Is `(11/192) sum_R W_R I_R` already present as an unspent signed refund (or dominated by such refunds) before positivity?

If yes, combine it with (0.2) and push the remaining `rho`/physical part through the signed sink. If no, evaluate the exact deficit on this sparse family using (5.2). Any proposed replacement credit smaller than the displayed `Theta(n^-3)` requirement is decisively insufficient.

**Full unrestricted FEI remains OPEN / NOT PROVED.**
