# fleet01/B06 — near-character descent and strict-record separation

**Run:** `20260922T110445Z-a01-b06-fei-r11`  
**Programme:** `FEI-ALL-TEAM-20260922T095941Z`, owner-control revision `2026-09-22.3`.  
**Assignment:** Path A, `Balanced extremal restriction structure`.  
**Classification:** `ESSENTIAL_STEP_APPLIED / BALANCED_RECORD_NEAR_CHARACTER_EXCLUSION / FULL_FEI_OPEN`.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Control correction and scope

Fresh owner control supersedes the older BT4 prompt still present in the scheduled-task payload: all eighty existing workers now work on uniform-cube Fourier entropy–influence, and B06 is assigned balanced extremal restriction structure. Accordingly this run contains no new BT4 research.

The target here is to obtain a structural consequence of extremizing

\[
\rho(F):={H(F)\over I(F)-1}
\]

on balanced genuine Boolean functions, while keeping raw physical restriction distinct from character suspension.

The named partner `fleet02/B06` still had no compatible completed all-team FEI deliverable visible at the prepublication source check. The current asynchronous order says not to wait. This run therefore consumes the completed **OTHER-account** theorem from `fleet03/B06` described below.

## 1. Source-pinned inputs actually used

### PREVIOUS-B06 — exact raw-restriction suspension ledger

Repository `yspennstate/math-open-problems`, commit
`374c4874e914c7414abc9109fadf77cfc3947298`, path

`proofnet24/P03-fei/fleet-2026-09-22/fleet01/B06/b06-20260922T103931Z-fei-r11/REPORT.md`.

For a balanced Boolean function `F`, with

\[
\rho={H(F)\over I(F)-1},
\]

and a physical coordinate `j` having disagreement

\[
d=\operatorname{Inf}_j(F),
\]

it distinguishes the two raw restrictions `F_+,F_-` from their character suspensions and proves, with

\[
T_\pm:=\rho I(F_\pm)-H(F_\pm),
\qquad
\Delta_j H:=H(F)-{H(F_+)+H(F_-)\over2},
\]

the exact identity

\[
{T_++T_-\over2}=\rho(1-d)+\Delta_jH.
\tag{1.1}
\]

It also proves the character-suspension identity

\[
H(\Sigma g)=H(g),\qquad I(\Sigma g)=I(g)+1,
\qquad
{H(\Sigma g)\over I(\Sigma g)-1}={H(g)\over I(g)}.
\tag{1.2}
\]

### OTHER-account theorem actually applied: fleet03/B06

Repository `yspennstate/math-open-problems`, commit
`11640269577cb955ad32c15f615ddd0da5df8ce9`, path

`proofnet24/P03-fei/fleet-2026-09-22/fleet03/B06/20260922T104822Z-fleet03-B06-fei-r11/REPORT.md`.

Its theorem `FEI-CHARACTER-FOLD-LEDGER-v1` applies the gauge

\[
g=x_jF
\]

to a balanced `F` with

\[
\operatorname{Inf}_j(F)=1-\epsilon.
\]

Writing

\[
u=F_+,\qquad v=-F_-,
\]

the two gauged children have the same mean. Let their common output variance be

\[
V=1-(\mathbb E u)^2.
\]

The source proves

\[
\epsilon\le V
\tag{1.3}
\]

and, for `0<=epsilon<=1/2`, the dimension-free entropy-debit bound

\[
0\le\Delta_jH
\le
Vh_2\!\left({\epsilon\over V}\right)
+\kappa\epsilon,
\qquad
\kappa={2\over\ln2}.
\tag{1.4}
\]

The sign change from `F_-` to `-F_-` does not change its squared Fourier law, entropy, or influence, so (1.4) applies to the same `Delta_j H` used in (1.1).

### BALANCED admission fact

Repository `yspennstate/math-open-problems`, commit
`7d20a4bb4067085af7c5e7c9a82aef31998a7d36`, path

`proofnet24/P03-fei/fleet-2026-09-21/fleet02/B18/20260922T093253Z-balanced-slice-admission/REPORT.md`.

It proves that controlling `H/(I-1)` uniformly on balanced Boolean functions is already equivalent to uniform-cube FEI with the same constant. Thus a structural reduction of balanced extremizers is relevant to the full target, but is not itself a proof of FEI.

## 2. Exact setup for a high-influence coordinate

Let

\[
F:\{-1,1\}^n\to\{-1,1\}
\]

be balanced and satisfy `I(F)>1`. Put

\[
L:=I(F)-1>0,
\qquad
\rho:={H(F)\over L}.
\tag{2.1}
\]

Fix a coordinate `j`, and write

\[
d:=\operatorname{Inf}_j(F),
\qquad
\epsilon:=1-d.
\tag{2.2}
\]

The exact uniform restriction identity is

\[
I(F)=d+{I(F_+)+I(F_-)\over2}.
\tag{2.3}
\]

Hence

\[
{I(F_+)+I(F_-)\over2}
=I(F)-d
=L+\epsilon.
\tag{2.4}
\]

Combining (1.1) with `1-d=epsilon` gives

\[
\boxed{
{T_++T_-\over2}=\rho\epsilon+\Delta_jH.
}
\tag{2.5}
\]

The point is that the entire loss from balancing a raw restriction by a fresh character is now an explicit scalar quantity.

## 3. Main theorem: a near-character coordinate forces a lower-dimensional near-extremizer

### Theorem A — `FEI-B06-NEAR-CHARACTER-DESCENT-v1`

Under the setup above, assume

\[
\operatorname{Inf}_j(F)\ge {1\over2},
\qquad\text{equivalently}\qquad 0\le\epsilon\le {1\over2}.
\]

Let `V` be the common child variance from (1.3). Then at least one nonconstant raw restriction

\[
G\in\{F_+,F_-\}
\]

satisfies the exact lower bound

\[
\boxed{
{H(G)\over I(G)}
\ge
\rho-{\rho\epsilon+\Delta_jH\over L+\epsilon}.
}
\tag{3.1}
\]

Consequently, using the named fleet03/B06 theorem,

\[
\boxed{
{H(G)\over I(G)}
\ge
\rho-
{(\rho+\kappa)\epsilon
+Vh_2(\epsilon/V)
\over L+\epsilon},
\qquad \kappa={2\over\ln2}.
}
\tag{3.2}
\]

#### Proof

For a nonconstant child define

\[
r_\pm:={H(F_\pm)\over I(F_\pm)}.
\]

Then

\[
T_\pm=I(F_\pm)(\rho-r_\pm).
\tag{3.3}
\]

At least one child is nonconstant, because (2.4) gives positive total child influence. Weight the quantities `T_\pm/I(F_\pm)` by the nonnegative child influences. Their weighted average is

\[
{T_++T_-\over I(F_+)+I(F_-)}
={\rho\epsilon+\Delta_jH\over L+\epsilon},
\tag{3.4}
\]

where (2.4)-(2.5) were used. Therefore one nonconstant child `G` has

\[
{T_G\over I(G)}
\le {\rho\epsilon+\Delta_jH\over L+\epsilon}.
\]

Since `H(G)/I(G)=rho-T_G/I(G)`, this proves (3.1). Inserting (1.4) proves (3.2). `QED`

### Interpretation

A coordinate whose influence is close to one cannot simply disappear inside a balanced extremizer. It produces an actual lower-dimensional raw Boolean descendant whose ordinary FEI ratio is close to the parent's balanced excess ratio, with an explicit loss retaining the correct rare-event logarithm

\[
Vh_2(\epsilon/V).
\]

At the exact character endpoint `epsilon=0`, (3.1) gives equality. Indeed `Inf_j(F)=1` means `F=x_jG` up to sign, so this recovers the exact suspension identity (1.2).

## 4. Strict dimension-record extremizers are quantitatively separated from the character boundary

For a fixed dimension define the lower-dimensional ordinary FEI record

\[
M_{n-1}:=
\max\left\{
{H(g)\over I(g)}:
 g\text{ Boolean on at most }n-1\text{ variables},\ I(g)>0
\right\}.
\tag{4.1}
\]

This maximum exists because there are finitely many Boolean functions in each fixed dimension.

Assume now that `F` is a **strict balanced record over inherited lower-dimensional suspensions**:

\[
\rho>M_{n-1}.
\]

Put

\[
\gamma:=\rho-M_{n-1}>0.
\tag{4.2}
\]

### Theorem B — `FEI-B06-RECORD-CHARACTER-EXCLUSION-v1`

For every coordinate with `Inf_j(F)>=1/2`, hence `epsilon<=1/2`, one has

\[
\boxed{
\gamma L
\le
Vh_2(\epsilon/V)
+(M_{n-1}+\kappa)\epsilon.
}
\tag{4.3}
\]

In particular,

\[
\boxed{
\gamma L
\le
h_2(\epsilon)
+(M_{n-1}+\kappa)\epsilon.
}
\tag{4.4}
\]

#### Proof

Every raw restriction uses at most `n-1` variables. Hence, for each nonconstant child,

\[
{H(F_\pm)\over I(F_\pm)}\le M_{n-1}=ho-\gamma.
\]

Equivalently,

\[
T_\pm
=\rho I(F_\pm)-H(F_\pm)
\ge\gamma I(F_\pm).
\tag{4.5}
\]

The same is trivially true for a constant child because both sides vanish. Average (4.5), then use (2.4)-(2.5):

\[
\gamma(L+\epsilon)
\le\rho\epsilon+\Delta_jH.
\]

Since `rho-gamma=M_{n-1}`,

\[
\gamma L
\le M_{n-1}\epsilon+\Delta_jH.
\tag{4.6}
\]

Insert (1.4) to obtain (4.3).

For (4.4), set

\[
\phi(t):={h_2(t)\over t}.
\]

On `(0,1)`,

\[
\phi'(t)={\log_2(1-t)\over t^2}<0.
\]

Because `epsilon<=V<=1`, we have `epsilon/V>=epsilon`, so

\[
Vh_2(\epsilon/V)
=\epsilon\phi(\epsilon/V)
\le\epsilon\phi(\epsilon)
=h_2(\epsilon).
\]

The endpoint `epsilon=0` follows by continuity. This proves (4.4). `QED`

### Explicit forbidden collar

Define

\[
\Psi_M(t):=h_2(t)+(M+\kappa)t,
\qquad 0\le t\le {1\over2}.
\tag{4.7}
\]

`Psi_M` is strictly increasing on this interval, because

\[
\Psi_M'(t)=\log_2{1-t\over t}+M+\kappa>0.
\]

Therefore Theorem B has the following direct consequences.

If

\[
\gamma L>\Psi_{M_{n-1}}(1/2)
=1+{M_{n-1}+\kappa\over2},
\tag{4.8}
\]

then **no coordinate of `F` has influence at least `1/2`**.

Otherwise every coordinate with influence at least `1/2` satisfies

\[
\boxed{
\epsilon
\ge
\Psi_{M_{n-1}}^{-1}(\gamma L),
\qquad
\operatorname{Inf}_j(F)
\le
1-\Psi_{M_{n-1}}^{-1}(\gamma L).
}
\tag{4.9}
\]

In particular, a strict new record (`gamma>0`) has **no influence-one coordinate**.

This is a quantified exclusion of an entire near-character class of putative strict-record extremizers. It does not assume a universal FEI bound.

## 5. Why the record gap is necessary

For every nonconstant Boolean `g`, its character suspension

\[
\Sigma g(y,x)=yg(x)
\]

is balanced, has

\[
\operatorname{Inf}_y(\Sigma g)=1,
\]

and satisfies exactly

\[
{H(\Sigma g)\over I(\Sigma g)-1}
={H(g)\over I(g)}.
\tag{5.1}
\]

Thus a lower-dimensional ordinary record can always be inherited on the balanced slice with an exact influence-one coordinate. Consequently there can be no gap-independent theorem excluding the character boundary merely from balancedness and the value of the ratio. The strict gap `gamma` in Theorem B is doing real mathematical work.

For example, taking `g=AND_2` gives the genuine three-variable Boolean suspension `F=yAND_2`, with

\[
H(F)=2,
\qquad I(F)=2,
\qquad {H(F)\over I(F)-1}=2,
\qquad \operatorname{Inf}_y(F)=1.
\]

This is **not** a counterexample to FEI and is not asserted to be a global extremizer. It is a source-valid counterexample to any proposed *unconditional* character-separation lemma that omits the record-gap or an equivalent descent alternative.

## 6. Record formulation and conditional end-to-end route

Let

\[
R_n:=
\max\left\{
{H(F)\over I(F)-1}:
F\text{ balanced on }n\text{ variables},\ I(F)>1
\right\}.
\tag{6.1}
\]

By character suspension,

\[
R_n\ge M_{n-1}.
\tag{6.2}
\]

Theorem B says that whenever the inequality is strict, every maximizing `F` is quantitatively separated from the character boundary on every high-influence coordinate, with a collar width controlled explicitly by

\[
(R_n-M_{n-1})(I(F)-1).
\]

This fits the present Path-A route as follows.

1. The BALANCED source says a uniform bound on the balanced excess ratio is already full FEI.
2. The preceding B06 run proves exact co-extremality for balanced disjoint compositions, hence removes nontrivial balanced factorization from a minimum-dimensional record analysis.
3. That run also caps disagreement for genuinely balanced physical restrictions and shows `K_occ>0` above ratio two.
4. **This run closes the near-character raw-restriction geometry conditionally on the only obstruction that can genuinely remain:** inheritance from a lower-dimensional ordinary near-extremizer. Theorem A makes the descent quantitative; Theorem B proves a strict new record cannot remain arbitrarily close to the character boundary.
5. Thus a strict-record obstruction is pushed into a central, composition-prime, positive-dependence region instead of being allowed to hide in a nearly suspended lower-dimensional function.

The first unpaid implication is now a **gap-free descent-or-payment alternative**. One needs to prove that if the record gap `gamma` degenerates along a candidate extremizing sequence, then either:

- the sequence genuinely descends to lower-dimensional ordinary Boolean functions without losing the target ratio, or
- the hierarchy/I-projection/Booleanity credit supplies enough payment to compensate the exact suspension loss `rho epsilon+Delta_jH`.

Equivalently, the next useful theorem should rule out a sequence with

\[
\gamma L\to0,
\qquad
\epsilon\to0,
\]

that neither converges to an exact inherited character suspension nor generates a source-valid KL/hierarchy credit sufficient for the gate inequality.

This is narrower than the previous generic “biased raw restriction” gap: the high-influence end has an explicit descent inequality and a strict-record exclusion; the remaining issue is how to make the alternative uniform when the dimension-record gap itself vanishes.

## 7. Honest outcome

### Proved here

- `FEI-B06-NEAR-CHARACTER-DESCENT-v1`, equations (3.1)-(3.2): a high-influence coordinate produces a genuine lower-dimensional raw Boolean descendant whose ordinary FEI ratio loses only the exact suspension/selector debit.
- `FEI-B06-RECORD-CHARACTER-EXCLUSION-v1`, equations (4.3)-(4.9): a strict balanced dimension record is quantitatively separated from the character boundary, and has no influence-one coordinate.
- The record-gap hypothesis is shown necessary for any pure character-separation statement by the exact character-suspension family.

### Not proved

- full uniform-cube FEI;
- a dimension-independent positive record gap;
- a gap-free near-character closure theorem;
- universal nonnegativity of the current shaped gate potential;
- a quantitative neighborhood theorem around all positive-`K_occ` balanced sources.

**Outcome:** `ESSENTIAL_STEP_APPLIED / BALANCED_RECORD_NEAR_CHARACTER_EXCLUSION / FULL_FEI_OPEN`.

## 8. Provenance and privacy review

The decisive OTHER-account source is the completed fleet03/B06 report at commit `11640269577cb955ad32c15f615ddd0da5df8ce9`. The named fleet02/B06 partner remained unavailable at the last source check, so no result was fabricated for it. This report contains only authorized mathematical material and logical fleet labels; it contains no credentials, scheduler identifiers, machine paths, unrelated private data, benchmark answers, email/Drive data, or public-release action. Repository synchronization is not native learned-memory ingestion; execution remains `WITHOUT_VERIFIED_BRAIN`.
