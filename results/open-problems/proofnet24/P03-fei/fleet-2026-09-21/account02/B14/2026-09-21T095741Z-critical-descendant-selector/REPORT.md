# B14 — restriction-critical descendant / erasure-heavy selector localization

**Run:** 2026-09-21T09:57:41Z, account02/B14  
**Role:** FEI erasure and selector proof  
**Brain status:** `WITHOUT_VERIFIED_BRAIN`  
**Target:** full uniform-cube FEI, still **OPEN / NOT PROVED**.  
**Creative route:** `APPROACHES.md` Route 5 (potential-free restriction step / ubiquitous informative bit), sharpened by FLEET_RULES moves **#27 swap the quantifiers**, **#12 find the exact telescope**, and **#2 attack the converse first**.

## 1. Exact statement obtained

Let `f:{-1,1}^n->{-1,1}` be nonconstant. All logarithms in Fourier entropy are base 2. Write

\[
H(f)=\sum_S \widehat f(S)^2\log_2\frac1{\widehat f(S)^2},\qquad
I(f)=\sum_S |S|\widehat f(S)^2.
\]

For a relevant physical coordinate `i`, let

\[
\alpha_i(f)=\operatorname{Inf}_i(f)>0,
\]

let `f_{i,+},f_{i,-}` be the two physical restrictions, and define the exact restriction entropy decrement

\[
\Delta_i H(f)=H(f)-\frac{H(f_{i,+})+H(f_{i,-})}{2}.
\]

A **physical restriction descendant** of `f` means a function obtained by fixing an arbitrary subset of the original coordinates. For a nonconstant Boolean function set

\[
r(f)=\frac{H(f)}{I(f)}.
\]

### Theorem (restriction-critical descendant)

For every nonconstant Boolean `f` there exists a nonconstant physical restriction descendant `g` such that

1. `r(g) >= r(f)`; and
2. for **every relevant coordinate** `i` of `g`,

\[
\boxed{\Delta_i H(g)\ge r(g)\,\alpha_i(g).}
\tag{1}
\]

Equivalently, with

\[
\rho_0(g)=\min_{i:\alpha_i(g)>0}\frac{\Delta_i H(g)}{\alpha_i(g)},
\]

one has

\[
\boxed{\rho_0(g)\ge r(g)\ge r(f).}
\tag{2}
\]

This is an **existential descendant statement followed by an all-coordinate lower bound at that special descendant**. It is not the refuted stronger proposal that an arbitrary prescribed coordinate admits a universal upper payment.

### Proof

There are finitely many physical restriction descendants of `f`. Choose a nonconstant descendant `g` maximizing `r=H/I` over all nonconstant descendants. Then `r(g)>=r(f)`.

Fix any relevant coordinate `i` of `g`, and write `g_+=g_{i,+}`, `g_-=g_{i,-}`. Each nonconstant child is itself a restriction descendant of `f`, hence by maximality

\[
H(g_\pm)\le r(g)I(g_\pm).
\]

If a child is constant, both its Fourier entropy and influence are zero, so the same inequality still holds. The exact physical-restriction influence telescope is

\[
I(g)=\alpha_i(g)+\frac{I(g_+)+I(g_-)}2.
\tag{3}
\]

Using the definition of `Delta_i H`,

\[
\begin{aligned}
H(g)
&=\Delta_i H(g)+\frac{H(g_+)+H(g_-)}2\\
&\le \Delta_i H(g)+\frac{r(g)}2\bigl(I(g_+)+I(g_-)\bigr)\\
&=\Delta_i H(g)+r(g)\bigl(I(g)-\alpha_i(g)\bigr).
\end{aligned}
\]

Since `H(g)=r(g)I(g)`, cancellation gives (1). The coordinate `i` was arbitrary among the relevant coordinates of `g`, so (1) holds for all of them. QED.

## 2. Counterexample localization — actual implication toward full FEI

Fix a candidate universal coefficient `C>0`.

### Corollary (C-critical core)

If some Boolean `f` violates `H(f)<=C I(f)`, then it has a physical restriction descendant `g` satisfying simultaneously

\[
\frac{H(g)}{I(g)}>C
\]

and, for **every relevant coordinate** `i`,

\[
\boxed{\Delta_i H(g)>C\,\operatorname{Inf}_i(g).}
\tag{4}
\]

Thus a global counterexample can always be localized to a core in which **every** coordinate defeats the potential-free restriction selector at the same coefficient. This converts the universal FEI obstruction into the search for a restriction-critical Boolean core; it does not assert that every coordinate of every Boolean function is bad.

The proof is immediate from the theorem: choose the maximizing descendant `g`; then `r(g)>=r(f)>C`, and (1) gives (4).

This is the useful quantifier swap: rather than trying to prove a false `for every function, every coordinate pays` statement, a hypothetical global counterexample may be replaced by one special descendant on which every relevant coordinate is locally critical.

## 3. Exact erasure payment forced on a critical core

The recovered erasure reduction gives, for every physical coordinate,

\[
\Delta_i H=B_i+JS_i,
\tag{5}
\]

where `B_i=H(X_i\mid X_{-i})` is the mass-weighted Fourier erasure entropy and `JS_i>=0` is the recombination/Jensen--Shannon term. The recovered September-20 recombination theorem proves

\[
JS_i\le B_i,
\tag{6}
\]

and the erasure reduction also gives

\[
JS_i\le c\min\{\alpha_i,1-\alpha_i\},\qquad c=\frac2{\ln 2}=2.885390081777\ldots.
\tag{7}
\]

Combining (1), (5)--(7), every relevant coordinate of a restriction-critical descendant obeys

\[
B_i\ge \frac{r(g)}2\alpha_i
\]

and

\[
B_i=\Delta_iH-JS_i\ge \bigl(r(g)-c\bigr)\alpha_i.
\]

Hence

\[
\boxed{
\frac{B_i}{\alpha_i}\ge
\beta(r(g)):=\max\left\{\frac{r(g)}2,\ r(g)-\frac2{\ln2},\ 0\right\}
\quad\text{for every relevant }i.
}
\tag{8}
\]

For `r(g)>4/ln 2=5.7707801635...`, the stronger branch is `r(g)-2/ln2`.

Therefore any FEI counterexample at a coefficient `C>4/ln2` has a descendant on which **every coordinate is simultaneously erasure-heavy**:

\[
\frac{B_i}{\operatorname{Inf}_i}>C-\frac2{\ln2}.
\tag{9}
\]

This is an exact new reduction inside the recovered P03 state: the remaining universal job can be phrased as ruling out Boolean functions that are at once globally high-`H/I` and all-coordinate erasure-heavy after passing to an extremal physical restriction descendant.

At the Hod-scale calibration `C=6.454784`, (9) demands

\[
B_i/\alpha_i>3.5693939182\ldots
\]

at every relevant coordinate of the critical core. This number is a calibration only; it is not a proof that the universal sharp constant equals Hod's constant.

## 4. Same descendant also inherits the known low-influence and diffuse-profile obstructions

The recovered concave-restriction theorem gives

\[
\Delta_iH\le \Psi(j_i),\qquad
j_i=\min\{\alpha_i,1-\alpha_i\},
\]

where

\[
\Psi(t)=h_2(t)+1-h_2\!\left(\frac12+\sqrt{t(1-t)}\right),
\]

and the recovered proof establishes that `kappa(t)=Psi(t)/t` is decreasing on `(0,1/2]`.

At a critical descendant with `r(g)>4`, (1) and `Psi(j_i)<=2` rule out `alpha_i>=1/2`; hence `j_i=alpha_i` and

\[
\kappa(\alpha_i)\ge r(g).
\tag{10}
\]

For `C>4`, let `tau(C)` be the unique solution of `kappa(tau)=C`. Any counterexample to FEI with coefficient `C` therefore has the **same** restriction-critical descendant `g` satisfying

\[
\alpha_i(g)<\tau(C)\qquad\text{for every relevant }i.
\tag{11}
\]

At `C=6.454784`, numerical inversion gives `tau(C)≈0.1805539925`.

The inherited global influence-profile/Huffman bound has the form

\[
H(g)\le c\,I(g)\bigl(H_2(w)+1\bigr),\qquad
w_i=\alpha_i/I(g),\quad c=2/\ln2.
\tag{12}
\]

Thus if `r(g)>C`,

\[
H_2(w)>C/c-1.
\tag{13}
\]

At `C=6.454784`, this lower bound is approximately `1.2370577389` bits.

So a hypothetical counterexample can be localized to **one and the same descendant** that simultaneously has:

\[
\boxed{
H/I>C,\qquad
\alpha_i<\tau(C)\ \forall i,\qquad
H_2(\alpha/I)>C/c-1,\qquad
B_i/\alpha_i>\beta(C)\ \forall i.
}
\tag{14}
\]

The last all-coordinate erasure-heavy condition is the new ingredient relative to the previously recorded hard-core localization.

## 5. The tempting converse fails — preserved dead route

Move #2 was to try to reverse the theorem: perhaps a function with

\[
\Delta_iH>C\alpha_i\quad\text{for all relevant }i
\]

must itself violate `H<=CI`. That does **not** follow. Let

\[
F_C(f)=H(f)-CI(f).
\]

The exact restriction telescopes give

\[
F_C(f)=\frac{F_C(f_{i,+})+F_C(f_{i,-})}{2}
      +\bigl(\Delta_iH-C\alpha_i\bigr).
\tag{15}
\]

A positive local excess at every coordinate can still be offset by sufficiently negative child residuals. Therefore `all coordinates locally bad` is a **necessary property of a suitably localized global counterexample**, not by itself a sufficient condition for a global counterexample. This failed converse must not be used later.

Likewise, the September-20 endpoint counterexample to an `EVERY prescribed coordinate` upper-payment proposal remains intact. Nothing here revives it: (1) is a lower bound at an existentially selected extremal descendant.

## 6. Literature / recovered-state check

The live P03 continuation of 21 September records the potential-free quantity

\[
\rho_0(f)=\min_i \Delta_iH/\operatorname{Inf}_i
\]

and notes that a dimension-free bound on `sup_f rho_0(f)` would imply FEI. It reports the current exact/numerical frontier (maximum `4.8677` through five variables and `6.0037` for width-2 tribes, with no tested family showing growth). The recovered report did not state the maximal-restriction-descendant principle above.

González--MacManus--Pereyra, arXiv:2606.00246 (2026), explicitly use the restriction entropy decrement and stopping binary trees: a suitable coordinate inequality at branching nodes plus FEI at leaves yields FEI. That is directly relevant prior art and is why no novelty claim is made here. A bounded current web search did not locate the exact extremal-descendant statement (1)--(2), but a search miss is not evidence of priority; the lemma is elementary enough that it may be implicit or known.

Potapov, arXiv:2609.21563 (18 September 2026), proves FEI for Boolean plateaued functions with sharp class constant 4 and for partially bent functions with sharp class constant 2. This confirms that plateaued/structured-class results are not to be re-announced here as universal progress.

**Priority status:** `UNVERIFIED`.  
**Full FEI status:** `OPEN`.

## 7. Before / after and next exact obligation

**Before this run:** the recovered route said that a finite universal bound on `rho_0(f)` would prove FEI, while strong every-coordinate payment proposals were known to fail. The hard-core localization imposed small influences and diffuse normalized influence profile, but did not force the exact erasure entropy itself to be large at every coordinate of the same descendant.

**After this run:** any putative FEI(C) counterexample can be replaced by a single physical restriction descendant satisfying the simultaneous critical-core package (14), in particular the exact all-coordinate erasure lower payment (8)--(9). This is a genuine reduction, not closure.

**Remaining universal obligation:** prove that no Boolean function can satisfy the critical-core package (14) for some universal `C`, or directly prove a universal upper bound on `rho_0` by exploiting Booleanity. The next B14 attack should work at the exact erasure/recombination level rather than re-trying the false arbitrary-coordinate statement. A concrete next dichotomy comes from the recovered logarithmic-edge/overlap decomposition: on a `C`-critical core, every coordinate must spend a fixed fraction either in logarithmic spectral-edge contrast or in paired-fibre overlap. The missing step is a dimension-free Booleanity argument showing that these coordinatewise expenditures cannot occur simultaneously on all relevant coordinates.

### Suggested dated README ledger line for the integrator

`2026-09-21 B14/account02: restriction-critical descendant lemma: any FEI(C) counterexample has a physical restriction descendant g with Delta_i H > C Inf_i for every relevant i; combining Delta=B+JS and JS<=B, JS<=(2/ln2)min(Inf_i,1-Inf_i) forces B_i/Inf_i > max(C/2,C-2/ln2) at every coordinate of the same low-influence/diffuse-profile core. Full FEI remains OPEN; converse local-badness=>global-counterexample fails.`
