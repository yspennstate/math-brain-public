# B18 FEI proof integration — positive interface-C contraction no-go and the required signed-compensation floor

**Scope:** `account03 / B18`, joint FEI interface C.  
**Execution:** **WITHOUT_VERIFIED_BRAIN**.  
**Full unrestricted FEI:** **OPEN / NOT PROVED**.  
**Claim level:** a universal impossibility theorem for the formerly proposed *positive/PSD* compiler-to-signed-flag contraction at all-Boolean scope, plus a quantitative necessary lower bound on any replacement signed compensation. This is not a counterexample to FEI.

## 0. Why this run changes mechanism

The entering interface-C chain attempted to send the authentic positive clone-pair current, after same-syndrome cancellation and terminal subtraction, into the account03 signed physical flag bank

\[
\mathcal K_\pi(f):=\sum_i \mathbb E_{W\sim\nu_i^\pi}\kappa_i^{K_*}(W),
\qquad
\mathcal K_\pi(f)\le 2J(f).
\tag{0.1}
\]

The newest completed cross-account artifact changes the admissible target:

`proofnet24/P03-fei/fleet-2026-09-21/account02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md`

(blob `2efc5dedf145a262700649c6e711c6a6fb91d622`, package commit `dfb0dffbe472f19a15e3c3b22bc563d527a979ab`). It proves on a genuine Boolean family that the **exact positive current itself**, with the authentic active-syndrome law, retained Reed--Muller terminal code, same-syndrome sums, and charged current multipliers, is not `O(J)` even on the canonical half-band live Borel window.

That artifact is applied below to the precise account03 signed-sink target. The conclusion is stronger than the earlier codimension-normalization obstruction: no uniformly bounded positive/PSD contraction of the whole live positive current into *any* target whose total expenditure is controlled by (0.1) can exist. Therefore interface C must either retain a compensating signed source credit before positivity is imposed, or be restricted by a separately proved critical-core reduction that excludes the counterfamily.

No scheduler or cross-account state is changed here.

---

## 1. Exact source and sink quantities

Let the source counterfamily have fine dimension `D`, put

\[
n=D-1,\qquad N=2^D,
\]

and take the genuine Boolean function from the consumed artifact: before the mandatory dummy split it is `-1` at two points differing in exactly two coordinates and `+1` elsewhere. The consumed theorem proves

\[
J(f_D)=I(f_D)=\frac{8n}{N},
\qquad H(f_D)<4I(f_D).
\tag{1.1}
\]

At the half-band terminal degree `d=ceil(D/2)`, with canonical endpoint

\[
S_f=\frac{N}{\sqrt{2n}},
\]

write

\[
\mathcal P_D^{\rm cur}
:=\int_{40}^{S_f}\mathcal E_{\rm cur}(s)\,\frac{ds}{s^3}.
\tag{1.2}
\]

For every `D>=128`, the completed peer theorem gives

\[
\boxed{
\mathcal P_D^{\rm cur}
\ge \frac{7}{3145728\,n^3}.
}
\tag{1.3}
\]

Moreover

\[
\boxed{
\mathcal P_D^{\rm cur}\sim \frac{4}{27n^3}.
}
\tag{1.4}
\]

In this family every nonzero charged odd mode is a triple with

\[
(q,k)=(3,1).
\]

The full-current multiplier and the central-current multiplier are respectively

\[
e_{3,1}=\frac49,
\qquad
\varepsilon_{3,1}=\frac{11}{288},
\]

so their ratio is exactly

\[
\frac{\varepsilon_{3,1}}{e_{3,1}}=\frac{11}{128}.
\tag{1.5}
\]

Hence the genuine **central** live positive current

\[
\mathcal P_D^{\rm cen}
:=\int_{40}^{S_f}\mathcal E_{\rm cen}(s)\,\frac{ds}{s^3}
\]

satisfies, for the same family,

\[
\boxed{
\mathcal P_D^{\rm cen}
=\frac{11}{128}\mathcal P_D^{\rm cur}
\ge \frac{77}{402653184\,n^3},
}
\tag{1.6}
\]

and asymptotically

\[
\boxed{
\mathcal P_D^{\rm cen}
\sim \frac{11}{864n^3}.
}
\tag{1.7}
\]

The account03 signed physical sink is the previously proved character-folded derivative curvature

\[
\kappa_i^{K_*}(w)
=\mathbb E_y(d_i^{K_*}(y)-d_i^{K_*}(y+w))^2
=p_i(w)+4o_i^{K_*}(w),
\]

with ordered-flag payment

\[
\boxed{
\mathcal K_\pi(f)\le 2J(f).
}
\tag{1.8}
\]

For the present family this gives

\[
\boxed{
\mathcal K_\pi(f_D)\le \frac{16n}{N}.
}
\tag{1.9}
\]

The sink includes the orientation bank; this is not the already-refuted unsigned-support shortcut.

---

## 2. PROVED — no universal positive/PSD contraction from authentic live current to the J-paid signed sink

### Theorem 2.1 — `P03-B18-POSITIVE-C-INTERFACE-NOGO`

There is no finite universal constant `C` such that, for every Boolean `f` and every authentic half-band interface-C source state,

\[
\boxed{
\mathcal P^{\rm cen}(f)
\le C\,\mathcal K_\pi(f)
}
\tag{2.1}
\]

for a fixed or averaged physical order `pi`. More generally, no positive/PSD pushforward of the whole authentic central live-current bank into any nonnegative physical target `T(f)` satisfying

\[
T(f)\le C_0J(f)
\tag{2.2}
\]

with universal `C_0` can have uniformly bounded distortion.

### Proof

Apply (1.6) and (1.9) to the consumed genuine Boolean family. If the sink is nonzero,

\[
\frac{\mathcal P_D^{\rm cen}}{\mathcal K_\pi(f_D)}
\ge
\frac{77N}{6442450944\,n^4}.
\tag{2.3}
\]

The right side tends to infinity exponentially because `N=2^D` and `n=D-1`. If the sink vanishes for some member, (2.1) fails even more directly because (1.6) is positive. This contradicts every finite `C`.

The same argument with (2.2) gives

\[
\frac{\mathcal P_D^{\rm cen}}{T(f_D)}
\ge
\frac{77N}{402653184\,C_0\,8\,n^4},
\]

again unbounded. This proves the general statement. \(\square\)

### Strengthening by the exact asymptotic

Using (1.7), the ratio to the maximal account03 sink payment `2J` satisfies

\[
\boxed{
\frac{\mathcal P_D^{\rm cen}}{2J(f_D)}
\sim
\frac{11N}{13824\,n^4}
\longrightarrow\infty.
}
\tag{2.4}
\]

The consumed source proves that the construction survives the original anchor/order averaging on an event of probability at least `1/8`. Hence even after that outer averaging the corresponding asymptotic lower scale is at least

\[
\frac{11}{6912n^3},
\tag{2.5}
\]

up to the stated source asymptotics, and its ratio to `2J` still diverges.

### What exactly is refuted

The theorem refutes the formerly sought all-Boolean arrow

\[
\text{positive authenticated live current}
\xrightarrow{\text{bounded positive/PSD contraction}}
\text{account03 J-paid signed flag bank}.
\]

It also refutes any repair that merely changes the positive parent/mask representation while keeping a universal `O(J)` nonnegative target. It does **not** refute:

- FEI;
- the exact signed current identities;
- account02's authentic parent/mask representation;
- account03's signed-curvature sink theorem;
- a contraction after a genuine signed credit is retained;
- a contraction on a separately proved narrower high-ratio critical class.

The counterfamily itself has `H/I<4`.

---

## 3. PROVED — quantitative compensation floor for every replacement signed interface

The no-go theorem identifies the size that a valid compensation must carry.

### Theorem 3.1 — `P03-B18-C-INTERFACE-COMPENSATION-FLOOR`

Suppose a future source-exact signed interface proves, for universal finite constants `A,B`,

\[
\boxed{
\mathcal P_D^{\rm cen}-\mathcal C_D
\le A\mathcal K_\pi(f_D)+B J(f_D),
}
\tag{3.1}
\]

where `C_D>=0` is a retained compensating credit coming from the authentic signed compiler (for example an R16/entropy/terminal/source term) and is not reused elsewhere. Then on the consumed half-band counterfamily

\[
\boxed{
\mathcal C_D
\ge
\mathcal P_D^{\rm cen}-(2A+B)J(f_D).
}
\tag{3.2}
\]

Consequently

\[
\boxed{
\liminf_{D\to\infty} n^3\mathcal C_D
\ge \frac{11}{864}.
}
\tag{3.3}
\]

For an outer anchor/order average for which only the guaranteed `1/8` favorable event is used, the necessary asymptotic floor is at least

\[
\boxed{
\liminf n^3\mathcal C_D^{\rm avg}
\ge \frac{11}{6912}.
}
\tag{3.4}
\]

### Proof

Equation (3.2) follows from (3.1) and the proved sink inequality `K_pi<=2J`. Multiply by `n^3`. Since

\[
n^3J(f_D)=\frac{8n^4}{2^D}\to0,
\]

while (1.7) gives

\[
n^3\mathcal P_D^{\rm cen}\to\frac{11}{864},
\]

(3.3) follows. The averaged version uses the source's fixed `1/8` favorable anchor/order fraction. \(\square\)

This is a **necessary**, not sufficient, compensation theorem. It gives a concrete falsification target for any proposed signed credit: on the sparse two-defect family it must carry polynomial scale `Theta(n^-3)`, not merely `O(J)`.

---

## 4. PROVED — the retained terminal-current subtraction is asymptotically too small to supply that floor by itself

The same consumed artifact gives, for one charged triple at `d=ceil(D/2)`, with

\[
T=(2n)^{-1/2},\qquad m=2^{d-1}-1,
\]

the terminal-code coefficient energy bound

\[
E_1\le \frac{4\pi T^3}{\sqrt m},
\tag{4.1}
\]

while the affine component has

\[
E_0\sim \frac23 T^6.
\tag{4.2}
\]

Therefore

\[
\boxed{
\frac{E_1}{E_0}
=O\!\left(n^{3/2}2^{-D/4}\right),
}
\tag{4.3}
\]

and the reverse triangle inequality for the actual retained coefficient `b=b^(0)-b^(1)` gives

\[
\boxed{
\frac{\|b-b^{(0)}\|_{L^2(ds/s^3)}}
     {\|b^{(0)}\|_{L^2(ds/s^3)}}
=O\!\left(n^{3/4}2^{-D/8}\right).
}
\tag{4.4}
\]

Thus the retained Reed--Muller terminal subtraction changes this current channel by an exponentially small relative amount, whereas Theorem 3.1 requires a compensation of order `n^-3` in energy. In particular, **the terminal-current subtraction already present inside `b_R` cannot by itself be the missing all-Boolean compensation mechanism for this family.**

This does not rule out a distinct terminal endpoint term elsewhere in the exact signed ledger; it rules out attributing the needed cancellation merely to the retained-code subtraction already inside the positive current.

---

## 5. Exact status and next attack

### PROVED in this run

1. The previous all-Boolean *positive/PSD* interface-C contraction into the account03 `J`-paid signed flag bank is impossible with any universal distortion.
2. The same impossibility holds for every nonnegative target already known to be `O(J)`; changing only the positive parent/mask disintegration cannot fix it.
3. Any correct signed replacement must supply a compensation of asymptotic size at least `11/(864 n^3)` on the genuine half-band counterfamily (or `11/(6912 n^3)` after using only the guaranteed outer averaging fraction).
4. The retained terminal-code subtraction inside the current coefficient is exponentially too small, relative to the surviving polynomial current, to be that compensation by itself.

### REFUTED

`authentic positive current -> bounded positive/PSD map -> J-paid signed flag sink` at universal all-Boolean scope.

### OPEN

The universal signed FEI compiler remains open. The next source-exact implication is now narrower and has the correct sign:

\[
\boxed{
\text{find an authentic nonreused signed companion }\mathcal C
\text{ with }\mathcal C\gtrsim\mathcal P^{cen}-O(J)
\text{ on the obstruction family,}
}
\]

then prove that

\[
\mathcal P^{cen}-\mathcal C
\]

admits the physical signed-flag/parent contraction. The natural first recipient is the arithmetic/refund line (`account02/B15`) to test the exact R16 / negative-entropy / refund bank against the quantitative floor (3.3), with `account03/B16` retaining the finite-window signed phase interface. If those credits fail the floor, the mechanism must change to a justified high-ratio critical-core reduction before any positive current is formed.

**Full FEI remains OPEN / NOT PROVED.**

---

## Joint-order receipt fields

- `consumed_peer_artifact`: `account02/interactive/20260921T204926Z-threshold-contraction/HALFBAND_COLLISION_EXTENSION.md` (blob `2efc5dedf145a262700649c6e711c6a6fb91d622`), together with its shared all-account handoff blob `0afa53275f7502b4279b1b214cf26a6e09f68b47`.
- `applied_to_claim`: the missing interface-C positive/PSD source-to-account03-signed-flag contraction.
- `remaining_implication`: construct and pay a source-exact nonreused signed compensation of the required `Theta(n^-3)` scale on the sparse obstruction family, then contract only the compensated remainder; alternatively prove a sufficient high-ratio critical-core reduction excluding that family.
- `next_recipient`: `account02/B15` (primary negative-credit/refund arithmetic), with `account03/B16` as the finite-window signed-interface partner.
- `full_problem_change`: no full FEI closure; one formerly open universal arrow is now REFUTED at its all-Boolean positive scope.
- `mechanism_change`: yes — positive-current contraction is retired; proceed with signed compensation before positivity or a proved critical-core restriction.
