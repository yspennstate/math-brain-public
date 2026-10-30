# fleet03/B07 — weighted near-bent slack transport on the balanced FEI slice

**Programme:** `FEI-ALL-TEAM-20260922T095941Z`  
**Assignment:** `FEI-20260922-fleet03-B07` — near-bent slack transport  
**Run:** `20260922T103431Z-fleet03-B07-FEI-r11`  
**Classification:** `ESSENTIAL_STEP_APPLIED / QUANTITATIVE_NEAR_EQUALITY_NEIGHBORHOOD`.  
**Full unrestricted uniform-cube FEI:** **OPEN / NOT PROVED**.  
**Execution:** `WITHOUT_VERIFIED_BRAIN`; `full_brain_connected=false`.

## 0. Fresh authority and correction state

The invocation text still named the historical MOC4 programme, but the fresh owner control in `yspennstate/math-research-brain` is revision `2026-09-22.3`, programme `FEI-ALL-TEAM-20260922T095941Z`, and explicitly redirects every account/slot to FEI. This later owner order was applied. No new MOC4 work was performed.

The compact assignment card for fleet03/B07 asks for a quantitative neighborhood theorem around the exact balanced `K_occ=0` family, with all entropy errors priced and no ambient-alphabet entropy loss. The current correction inbox observed at the start was empty. The recursive-majority low-level barrier is treated as mandatory preflight: no fixed-depth labelled-spectrum truncation or one-tail merge is used below.

## 1. Source-pinned premises and named other-account result consumed

The mathematical premises are:

1. **I-projection identity** — `yspennstate/math-open-problems`, commit `4bd6d05f1eb8325d665f2748f4d74dcee2550a04`, `proofnet24/P03-fei/fleet-2026-09-21/fleet02/B15/20260922T0829Z-influence-iprojection-kl/REPORT.md`, Sections 2–5. For a balanced uniform Boolean source with squared Walsh law `P`, occurrence marginals `r_i`, maximum-entropy nonempty law `Q_r`, and `K_occ=D_2(P||Q_r)`, one has
   \[
   K_{\rm occ}=H_{\max}(r)-H(P),\qquad I(f)=\sum_i r_i.
   \]
2. **Exact equality classification** — `yspennstate/math-open-problems`, commit `84c69136ca6b008badb76f15bf1071d029c927aa`, `proofnet24/P03-fei/fleet-2026-09-21/fleet03/B15/20260922T085625Z-product-equality-rigidity/REPORT.md`, Theorem 1. On the balanced uniform slice, `K_occ=0` iff, after irrelevant coordinates are discarded,
   \[
   f=\chi_F b(x_A),
   \]
   where `F` is nonempty, `A` is even, and `b` is bent; equivalently the squared spectrum is uniform on `\{F\cup R:R\subseteq A\}`.
3. **Named other-account result actually used** — fleet04/B17, `B-BIASED-BOOLEANITY-GAP-v1`, `yspennstate/math-open-problems`, commit `603b35e74227d1c2d8ee34c0c527c439c686e30b`, `proofnet24/P03-fei/fleet-2026-09-21/fleet04/B17/20260922T092422Z-biased-booleanity-gap/REPORT.md`, Sections 1–3. At the balanced uniform point, its arbitrary-bias theorem specializes to
   \[
   K_{\rm occ}\ge \mathcal G(r):={1\over4\ln2}\max_{\varnothing\ne U\subseteq[n]}\mathfrak g_U(Q_r)^2,
   \tag{1.1}
   \]
   since `v=1` and every operator factor `L_U=1`.

The assignment names fleet04/B07 as the preferred partner. At the observed fresh state there was no current FEI deliverable or handoff at the prescribed fleet04/B07 FEI paths, so no nonexistent partner theorem is claimed. The completed fleet04/B17 result above is an assignment-listed other-account source and is applied quantitatively in Theorem 2.1.

The unweighted-L2 and fixed-low-level barriers are not used as positive premises. They are respected by retaining every coordinate's binary-entropy weight and the exact `K_occ` / Booleanity credits.

## 2. Setup

Let
\[
f:\{-1,1\}^n\to\{-1,1\}
\]
be balanced under the uniform measure, and let
\[
P(S)=\widehat f(S)^2,\qquad S\ne\varnothing,
\]
so `P` is a probability law on nonempty subsets. Put
\[
r_i=P(i\in S),\qquad \mu=\sum_i r_i=I(f).
\]
Let `Q_r` be the maximum-entropy nonempty law with these occurrence marginals, let
\[
H_{\max}(r)=H(Q_r),\qquad
K_{\rm occ}=H_{\max}(r)-H(P),
\]
and define the **nonempty-conditioning credit**
\[
T(r):=\sum_{i=1}^n h_2(r_i)-H_{\max}(r)\ge0.
\tag{2.1}
\]
The inequality is ordinary entropy subadditivity applied to `Q_r`.

Fix `C>2`. For a character-times-bent equality template choose disjoint `F,A\subseteq[n]` with `F\ne\varnothing` and `|A|` even, and let `Z=[n]\setminus(F\cup A)`. Its occurrence vector is
\[
r_i^*=\begin{cases}
1,&i\in F,\\
1/2,&i\in A,\\
0,&i\in Z.
\end{cases}
\tag{2.2}
\]
Define
\[
\phi_C(t):=Ct-h_2(t)
\tag{2.3}
\]
and its exact template slack
\[
S_*(F,A;C)
:=C(|F|-1)+\left({C\over2}-1\right)|A|.
\tag{2.4}
\]
This is precisely `C(I-1)-H` on the equality family.

## 3. Main theorem: a weighted neighborhood with every entropy error priced

### Theorem 2.1 — `B07-WEIGHTED-BENT-NEIGHBORHOOD-v1`

For every balanced uniform Boolean `f`, every `C>2`, and every character-times-bent template `(F,A)` as above, define
\[
\mathcal E_C(r;r^*)
:=\sum_{i=1}^n
\bigl[\phi_C(r_i^*)-\phi_C(r_i)\bigr]_+.
\tag{3.1}
\]
Then
\[
\boxed{
C(I(f)-1)-H(f)
\ge
S_*(F,A;C)-\mathcal E_C(r;r^*)+T(r)+K_{\rm occ}(f).
}
\tag{3.2}
\]
Using the named fleet04/B17 Booleanity theorem,
\[
\boxed{
C(I(f)-1)-H(f)
\ge
S_*(F,A;C)-\mathcal E_C(r;r^*)+T(r)+\mathcal G(r),
}
\tag{3.3}
\]
where `\mathcal G` is (1.1). Consequently the source is FEI-safe at constant `C` whenever
\[
\boxed{
\mathcal E_C(r;r^*)
\le
S_*(F,A;C)+T(r)+\mathcal G(r).
}
\tag{3.4}
\]
All terms in (3.4) are source-measurable from occurrence marginals plus the actual Booleanity matrices. There is no `\log|2^{[n]}|`, no merged-tail entropy, and no unpriced ambient-alphabet term.

#### Proof

By the exact I-projection identity,
\[
H(P)=H_{\max}(r)-K_{\rm occ}.
\]
Therefore
\[
\begin{aligned}
C(I-1)-H(P)
&=C\left(\sum_i r_i-1\right)-H_{\max}(r)+K_{\rm occ}\\
&=\sum_i\bigl(Cr_i-h_2(r_i)\bigr)-C
  +\left(\sum_i h_2(r_i)-H_{\max}(r)\right)+K_{\rm occ}\\
&=\sum_i\phi_C(r_i)-C+T(r)+K_{\rm occ}.
\end{aligned}
\tag{3.5}
\]
For the template vector (2.2),
\[
\sum_i\phi_C(r_i^*)-C
=C(|F|-1)+\left({C\over2}-1\right)|A|
=S_*.
\tag{3.6}
\]
Hence, with the **signed** perturbation
\[
\Delta_C:=\sum_i\bigl(\phi_C(r_i^*)-\phi_C(r_i)\bigr),
\]
we have the exact identity
\[
C(I-1)-H(P)=S_*-\Delta_C+T(r)+K_{\rm occ}.
\tag{3.7}
\]
Termwise `\Delta_C\le\mathcal E_C`, which gives (3.2). Applying the fleet04/B17 lower bound `K_occ\ge\mathcal G(r)` yields (3.3)–(3.4). `QED`

### Explicit rare-event form

The weighted error in (3.1) can be bounded without any alphabet-size factor. For `i\in F`, writing `\epsilon_i=1-r_i`,
\[
[\phi_C(1)-\phi_C(r_i)]_+
=C\epsilon_i+h_2(\epsilon_i).
\tag{3.8}
\]
For `i\in A`,
\[
[\phi_C(1/2)-\phi_C(r_i)]_+
=[h_2(r_i)-1+C(1/2-r_i)]_+
\le C(1/2-r_i)_+.
\tag{3.9}
\]
For `i\in Z`,
\[
[\phi_C(0)-\phi_C(r_i)]_+
=[h_2(r_i)-Cr_i]_+.
\tag{3.10}
\]
Thus the directly checkable sufficient condition
\[
\boxed{
\sum_{i\in F}\bigl(C(1-r_i)+h_2(1-r_i)\bigr)
+C\sum_{i\in A}(1/2-r_i)_+
+\sum_{i\in Z}[h_2(r_i)-Cr_i]_+
\le S_*+T+\mathcal G
}
\tag{3.11}
\]
implies `C(I-1)-H\ge0`.

The last sum is the essential sparse-leakage term. When `r_i\downarrow0`, it is of order `r_i\log_2(1/r_i)`, not merely `r_i^2` or an unweighted L2 norm. This is exactly the rare-event logarithm that the current Path-B barriers require us not to discard.

## 4. Dimension-free TV collar on the exact affine support

### Corollary 4.1 — `B07-AFFINE-BENT-TV-COLLAR-v1`

Let `U_{F,A}` be the uniform law on
\[
\mathcal L_{F,A}=\{F\cup R:R\subseteq A\},
\]
with `F\ne\varnothing`, `|A|=m>0` even. Suppose the actual balanced squared spectrum `P` is supported on exactly this affine coordinate cube and
\[
\|P-U_{F,A}\|_{\rm TV}\le\varepsilon.
\tag{4.1}
\]
Then
\[
\boxed{
C(I-1)-H(P)
\ge
C(|F|-1)+m\left(C(1/2-\varepsilon)-1\right).
}
\tag{4.2}
\]
In particular, every such genuine Boolean source is safe whenever
\[
\boxed{
\varepsilon\le {1\over2}-{1\over C}.
}
\tag{4.3}
\]
For `C=6.5584452830718245` this radius is approximately `0.3475248391`.

#### Proof

Support in `\mathcal L_{F,A}` forces `r_i=1` on `F` and `r_i=0` on `Z`. For each `i\in A`, the event `\{S:i\in S\}` has probability `1/2` under `U_{F,A}`, so total variation gives
\[
r_i\ge1/2-\varepsilon.
\]
Entropy subadditivity gives `H(P)\le\sum_{i\in A}h_2(r_i)\le m`. Therefore
\[
\begin{aligned}
C(I-1)-H(P)
&\ge C\left(|F|-1+\sum_{i\in A}r_i\right)-m\\
&\ge C(|F|-1)+m\left(C(1/2-\varepsilon)-1\right),
\end{aligned}
\]
which proves (4.2). Since `|F|\ge1`, (4.3) makes the right side nonnegative. `QED`

This is a true dimension-independent neighborhood, but only on the exact affine support. Theorem 2.1 is the leakage-robust version and explicitly charges any new coordinates through (3.10).

## 5. Mandatory recursive-majority preflight

The low-level barrier uses depth-`m` recursive ternary majority. At the balanced center every leaf has occurrence marginal
\[
r=2^{-m},\qquad n=3^m,
\]
and hence `I=(3/2)^m`. Theorem 2.1 does **not** merge these rare coordinates into one tail. If such a coordinate lies in a template's `Z` set, then
\[
h_2(2^{-m})-C2^{-m}\ge (m-C)2^{-m},
\tag{5.1}
\]
because `h_2(p)\ge p\log_2(1/p)`. Thus, for `m>C`, the aggregate rare-coordinate charge over `3^m` such coordinates is at least
\[
(m-C)(3/2)^m.
\tag{5.2}
\]
So this neighborhood certificate cannot falsely erase the recursive-majority logarithm through a fixed-depth or one-tail compression. Recursive majority is simply outside a small character-times-bent neighborhood in this metric unless another positive credit pays the displayed charge. This is the intended preflight behavior; it is not a claim that the present local theorem alone proves FEI for recursive majority.

## 6. What changed and the smallest conditional full deduction

Before this run, the exact `K_occ=0` endpoint was classified, but the current state explicitly had **no dimension-independent neighborhood theorem**. Theorems 2.1 and 4.1 fill a concrete part of that gap:

* exact equality slack is transported under a weighted occurrence perturbation;
* all first-moment entropy errors are charged coordinate by coordinate;
* the nonempty-conditioning credit `T(r)` is retained rather than dropped;
* fleet04/B17's genuine signed-Booleanity credit is spent quantitatively rather than merely cited;
* sparse leakage pays `r\log(1/r)` and therefore survives the current rare-event barriers;
* on the exact affine support there is an explicit dimension-free TV radius `1/2-1/C`.

The smallest remaining implication for this B07 route is now **quantitative template recovery**:

> If a balanced genuine Boolean source lies in the dangerous I-projection corridor (`B_inf<0` and `K_occ<-B_inf`), prove that the signed Boolean equations and Walsh lattice force the occurrence vector close to some character-times-bent template strongly enough that (3.4), or the stronger exact identity (3.7), holds.

Equivalently, it is enough to prove a gap-or-template theorem: either the Booleanity/dependence credits already satisfy the exact FEI payment, or there exists `(F,A)` for which the weighted error `\mathcal E_C` is at most `S_*+T+K_occ`. The present run proves the **slack-transport half** of that dichotomy; it does not prove the template-recovery half.

If this quantitative template-recovery implication is proved for every balanced source at one finite `C`, then the balanced-slice equivalence from the current programme yields full uniform-cube FEI at the same constant. Singular bias issues are irrelevant to this balanced theorem; arbitrary-bias transport remains a separate Path-A/Path-B task.

## 7. Scope and integrity

No fixed `Gamma^dagger`, obsolete `0.337/0.34` repair, raw-U4 shortcut, unweighted convolution-L2 closure, or fixed-depth retained-spectrum payment is used. No claim of full FEI is made. No paid/remote model or API, email, Drive, public release, workflow dispatch, scheduler mutation, cross-account native action, credentials, benchmark material, or unrelated private transcript was used. Repository access is durable source transport only and does not establish native brain ingestion.
