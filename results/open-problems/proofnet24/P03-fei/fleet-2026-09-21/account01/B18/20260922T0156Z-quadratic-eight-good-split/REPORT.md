# account01/B18 — quadratic-eight good-split compiler and the unbalanced-corridor application

**Run:** `20260922T0156Z-account01-B18-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED / FULL_FEI_OPEN`  
**Execution:** `WITHOUT_VERIFIED_BRAIN`  
**Full uniform-cube FEI:** **OPEN / NOT PROVED.**

## 0. Exact current target and named peer result consumed

The live owner control is revision `2026-09-22.2` and asks the FEI fleet to close a genuine all-gate / physical-restriction proof, not to promote finite tests or auxiliary equivalences to a solution.

This run substantively consumes the exact account04/B12 result

`proofnet24/P03-fei/fleet-2026-09-21/account04/B12/20260922T014248Z-unbalanced-corridor-game/REPORT.md`

(report blob `5477813fe8250df8a7d8728a246f65f50ad6bbbf`).  For the source-valid balanced monotone composition-prime ten-input gate `G_*` with truth-table SHA-256

`3168d8fb8ac9f5d6d7dca1d79146392aecb5eb55cc76ccb028395a9e6a62bfb4`,

that report proves, among other things, the following source-exact statement.  Along the fixed physical reveal order

`0,1,2,3,4,5,6,7,8,9`,

every positive-currency restriction state satisfies

\[
\frac{L_v}{Q_v}\le 32,
\tag{0.1}
\]

and exactly 37 unbalanced states attain equality.  Here

\[
L_i(F)=H(F)-\frac{H(F_{i=0})+H(F_{i=1})}{2},
\qquad
Q_i(F)=P(F)-\frac{P(F_{i=0})+P(F_{i=1})}{2},
\]

with

\[
P(F)=\frac{I(F)}4-q_F(1-q_F).
\tag{0.2}
\]

The same peer proves that the order avoids every proper balanced nonaffine state, so (0.1) is genuinely an **unbalanced-corridor** statement rather than a disguised balanced-return argument.

I also use account02/B16's exact restriction-margin martingale / split identity from

`proofnet24/P03-fei/fleet-2026-09-21/account02/B16/20260922T010120Z-gate-margin-restriction-martingale/REPORT.md`.

No read-once certificate is rerun here.

## 1. A concrete full-FEI compiler at constant 8

Define the pure quadratic potential

\[
\boxed{\Gamma_8(p)=32p(1-p).}
\tag{1.1}
\]

For a uniform-cube Boolean function `F`, define its corresponding defect

\[
\boxed{
D_8(F):=8I(F)-H(F)-32q_F(1-q_F)
       =32P(F)-H(F).
}
\tag{1.2}
\]

The exact split identities for `H` and `P` give, for every physical coordinate `i`,

\[
\boxed{
D_8(F)
=\frac{D_8(F_{i=0})+D_8(F_{i=1})}{2}
 +32Q_i(F)-L_i(F).
}
\tag{1.3}
\]

This has no discarded child term and no positive-part replacement.

### Proposition 1 — the `8-good-split` lemma would prove full FEI with C=8

Suppose the following statement holds:

> **GS8.** Every finite nonaffine Boolean function `F` has an essential physical coordinate `i` such that
> \[
> \boxed{L_i(F)\le32Q_i(F).}
> \tag{1.4}
> \]

Then, by induction on essential arity using (1.3),

\[
D_8(F)\ge0
\]

for every Boolean `F`.  Affine terminal functions are constants or literals after deleting dummy variables, and have `P=H=0`, so the induction base is exact.  Consequently

\[
\boxed{
H(F)\le8I(F)-32q_F(1-q_F)\le8I(F)
}
\tag{1.5}
\]

for every uniform-cube Boolean function.  Thus GS8 is a sufficient universal implication that would settle FEI with the finite dimension-independent constant `C=8`.

The constant 8 is sharp **for this local quadratic split mechanism**: the two-input AND gate at uniform bias has

\[
H=2,\qquad I=1,\qquad P=\frac1{16},
\]

and either physical split has affine children, hence

\[
L=2,\qquad Q=\frac1{16},\qquad \frac LQ=32.
\tag{1.6}
\]

So no smaller coefficient than 32 can satisfy a universal one-step statement of the form (1.4).

This proposition is a compiler, not a proof of GS8.

## 2. The current prime unbalanced-corridor obstruction is completely paid by Gamma_8

Apply the exact account04/B12 theorem (0.1) to its fixed reveal tree for `G_*`.  At every positive-currency node selected by that physical order,

\[
32Q_v-L_v\ge0.
\tag{2.1}
\]

At a zero-currency selected step, the coordinate is inessential at that nonaffine state (or the state is already affine), and the exact split residual is zero.  Therefore every edge used by this fixed physical decision tree has nonnegative `D_8` residual.  Since all terminal states are affine, backward induction in (1.3) gives

\[
\boxed{D_8(G_*)\ge0.}
\tag{2.2}
\]

More importantly, this is **not merely a root numerical check**.  The entire balance-avoiding unbalanced corridor is locally paid in the same currency.  The 37 exact states with `L/Q=32` are precisely saturation states of the quadratic payment, not counterexamples to it.

For the root itself,

\[
I(G_*)=\frac{257}{128},\qquad q_{G_*}=\frac12,
\]

so (2.2) reads

\[
H(G_*)\le 8\frac{257}{128}-8,
\]

and the peer entropy certificate `H(G_*)<6.509836127588151480` leaves substantial positive root slack.  The point of (2.1), however, is that the proof survives all off-centre states encountered by the explicit physical order; no balanced-return assumption is being smuggled in.

**Old missing implication:** a replacement all-gate potential must pay the explicit unbalanced corridor, especially the 37 ratio-32 states.

**New proved inference:** `Gamma_8(p)=32p(1-p)` pays that entire source-exact corridor step-by-step, with equality exactly at the ratio-32 states.  Thus the current prime gate obstruction does not refute the quadratic-eight route.

## 3. Direct attempt on the first universal inference: an aggregate spectral-edge form

The first essential missing inference is GS8 itself.  A strictly stronger, concrete statement would imply it by averaging.

For a coordinate `i`, pair parent Fourier coefficients as

\[
u_T=\widehat F(T),\qquad v_T=\widehat F(T\cup\{i\}),
\qquad T\subseteq[n]\setminus\{i\}.
\]

Put `phi(x)=-x log_2 x`, with `phi(0)=0`, and define the exact edge cost

\[
\ell(a,b)
=\phi(a^2)+\phi(b^2)
-\frac12\phi((a+b)^2)
-\frac12\phi((a-b)^2).
\tag{3.1}
\]

The physical restriction transform gives exactly

\[
\boxed{L_i(F)=\sum_T \ell(u_T,v_T).}
\tag{3.2}
\]

On the other hand, account04/B18's exact Q-currency identity gives

\[
\boxed{
4Q_i(F)=\sum_{S\ni i,\ |S|\ge2}\widehat F(S)^2.
}
\tag{3.3}
\]

Therefore

\[
32\sum_iQ_i(F)
=8\sum_{|S|\ge2}|S|\widehat F(S)^2.
\tag{3.4}
\]

Hence the following single spectral-edge inequality would imply GS8:

\[
\boxed{
\sum_{i=1}^n\sum_{T\subseteq[n]\setminus\{i\}}
\ell\!\left(\widehat F(T),\widehat F(T\cup\{i\})\right)
\le
8\sum_{|S|\ge2}|S|\widehat F(S)^2.
}
\tag{E8}
\]

Indeed, (E8) is exactly `sum_i L_i <= 32 sum_i Q_i`, so some essential coordinate satisfies (1.4).

This is now a source-exact universal target in the original Fourier coefficients, with no critical-core hypothesis and no hidden coordinate labels.

## 4. The first naive proof of (E8) is genuinely false

For one Fourier edge let

\[
m=a^2+b^2,\qquad p=\frac{b^2}{a^2+b^2}.
\]

Then the exact restriction-information identity gives

\[
\ell(a,b)=m\,\Psi(p),
\tag{4.1}
\]

where

\[
\Psi(p)
=h_2(p)+1-h_2\!\left(\frac12+\sqrt{p(1-p)}\right).
\tag{4.2}
\]

Thus an edgewise attempt to charge an upward coefficient by

\[
\ell(a,b)\le8b^2
\tag{4.3}
\]

would require `Psi(p)/p <= 8`.  But

\[
\frac{\Psi(p)}p\to\infty\qquad(p\downarrow0).
\tag{4.4}
\]

So (4.3) is false by an arbitrarily large factor.  The stronger aggregate target (E8), if true, must use **Boolean signed structure across edges**, not a scalar edge majorant.

The relevant Boolean constraint is the exact convolution system

\[
\sum_S\widehat F(S)\widehat F(S\triangle R)=0
\qquad(R\ne\varnothing),
\tag{4.5}
\]

in particular, for every physical coordinate,

\[
\sum_T u_Tv_T=0.
\tag{4.6}
\]

Equation (4.6) is the first genuine cancellation available to an attempted proof of (E8).  Merely replacing `ell` by an unsigned scalar envelope loses exactly the compensation that the current campaign has repeatedly found to be necessary.

This is where the derivation stops: I do **not** have a proof that (4.5)-(4.6) imply (E8), nor a Boolean counterexample to (E8).

## 5. Obstruction discipline

The route above was checked against the currently live obstruction set rather than inferred from finite evidence:

- **AND/OR boundary:** two-input AND attains equality (1.6), so the proposed constant is calibrated rather than contradicted.
- **Current composition-prime Numaro descendant:** the exact account04/B12 corridor theorem proves it is paid step-by-step, including all 37 unbalanced equality states.
- **Balanced-return obstruction:** irrelevant to this route; `Gamma_8` is evaluated on every unbalanced physical descendant, and section 2 uses a path which never needs a proper balanced return.
- **One-coordinate old read-once obstruction:** it concerns a different base potential.  Here a bad coordinate is allowed; GS8 only asks for one good essential coordinate, and the exact ten-input witness has such choices.
- **Sparse-defect / packet-height obstruction:** no coefficientwise entropy payment is asserted.  Section 4 explicitly records that the scalar edgewise payment is false, so the route preserves the need for signed Boolean cancellation.
- **Tensor/decomposable gates:** no claim of decomposable extremality is used.  The target (E8) is stated for the actual Fourier spectrum of the full Boolean gate.

Finite checks, including the exact source gate, are evidence only; they are not promoted to a universal theorem.

## 6. Status and next mathematical move

**Classification:** `ESSENTIAL_STEP_APPLIED`.

The current hard prime unbalanced-corridor witness has been passed by an explicit off-centre potential, and the full-FEI problem has been reduced *within this route* to the universal good-split statement GS8.  The first stronger target is the exact spectral-edge inequality (E8).

The next run should attack (E8) using the signed Boolean convolution constraints (4.5), not by another scalar edge envelope.  A decisive outcome would be either:

1. derive (E8), which together with Proposition 1 would give a full proof `H(f)<=8 I(f)`; or
2. construct a genuine Boolean function with `L_i>32Q_i` for every essential coordinate, thereby refuting GS8 and forcing a deeper adaptive-block potential.

Until one of those happens, **full FEI remains OPEN / NOT PROVED.**
