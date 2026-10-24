# POS3 account04/B19 — thin F2/F3 discrepancy chains export the full 2/33 charge to a strict outer ray

**Run:** `B19-20260922T081503Z-r11`  
**Outcome:** `ESSENTIAL_STEP_APPLIED`  
**Parent target:** every finite nonchain poset of width at most three has incomparable `u,v` with `1/3 <= Pr(u<v) <= 2/3` under the uniform law on all full linear extensions.  
**Parent status:** **OPEN / NOT PROVED**.  
**Execution context:** `WITHOUT_VERIFIED_BRAIN`.

All probabilities below are under the original uniform law on all full linear extensions of the original poset. No deletion-induced law is treated as uniform.

## 1. Exact source-bound state consumed

The latest complete campaign-lead version used is

- **account04/B10 r17**, `proofnet24/collective-POS3/account04/B10/20260922T071036Z-B10-POS3-r17/REPORT.md`, Git blob `61c94984acd303d2fbed96f2f3bb77664a51297b`.

The immediately preceding same-slot result is

- **account04/B19 r46**, `proofnet24/collective-POS3/account04/B19/B19-20260922T071535Z-r46/REPORT.md`, Git blob `26c2eab1c40a8da73357764efd0aab4160391e07`.

It combines the lead's low-endpoint heavy-cover state with the charged equal-neighborhood fork funnel. After every high `F1` or `F4` channel has been discharged, the sole high-packet local type left is

`ell in F2`, `r in F3`,

with the exact Hasse/strong-order geometry

`ell lessdot a lessdot r`,

`ell prec_* x prec_* a prec_* y prec_* r`,

where `x lessdot y`, `a||x,y`, `ell||x`, `r||y`. The old endpoint minorities obey

`Pr(a<x)<3/11`, `Pr(y<a)<3/11`,

and the two canonical sides retain total assigned packet mass `>4/33` each; selected individual `F2` and `F3` channels retain `>2/33` marks. R46 leaves **F2/F3 DISCREPANCY-CHAIN TRANSPORT** unpaid.

The required named OTHER-account partner consumed and applied here is the newest complete

- **account01/B10**, `proofnet24/collective-POS3/account01/B10/20260922T072132Z-b10-pos3-r11/REPORT.md`, Git blob `85fa62968e584b5db7fe6270260f55f92c071438`.

It proves that in a hypothetical no-balanced counterexample the strong-majority relation `prec_*` is a genuine strict total order. Writing `rho(v)` for its rank and `sigma(p,q)=rho(q)-rho(p)`, it proves the right-ray and left-ray integer potentials

`Psi_R(p,q)=n rho(q)+sigma(p,q)`,

`Psi_L(p,q)=n(n-1-rho(p))+sigma(p,q)`,

strictly increase along its already-controlled fixed-ray mechanisms. Its first unpaid issue is ray-switch / crossed accounting.

One earlier lead result is used as an exact identity, not as a new target claim:

- **account04/B10 r12**, `proofnet24/collective-POS3/account04/B10/20260922T034709Z-B10-POS3-r12/REPORT.md`.

For an oriented incomparable pair `p prec_* q` with

`Pred(p) subseteq Pred(q)`, `Succ(q) subseteq Succ(p)`,

put `D=Pred(q)\Pred(p)` and `U=Succ(p)\Succ(q)`. Then

`2 Pr(p<q)-1 = Pr(A_D union B_U)`,                    (1.1)

where `A_D={exists d in D: p<d}` and `B_U={exists u in U: u<q}`. In width at most three only maximal elements of `D` and minimal elements of `U` matter, with at most two of each.

## 2. Compact conditional route

The `F2/F3` state contains two boundary pairs:

- left pair `(ell,x)`, whose central distinguisher is `a in Succ(ell)\Succ(x)`;
- right pair `(y,r)`, whose central distinguisher is `a in Pred(r)\Pred(y)`.

The first uncovered low-complexity case is the **thin laminar** one: on a boundary, the central `a` is the unique extremal discrepancy on its side, the opposite neighborhoods are nested in the crossed direction needed by (1.1), and the opposite canonical fringe has only one member.

The theorem below pays this case exactly. The old interior minority contributes less than `3/11`; the endpoint identity requires more than `1/3` total fringe mass; therefore more than the exact gap

`1/3-3/11 = 2/33`

must cross the *new outer fringe*. If that fringe is a singleton, one actual outer incomparable pair receives the whole `>2/33` packet. Its endpoint moves strictly outward in `prec_*`, so the assigned partner's integer potential rises. Thus a thin `F2/F3` discrepancy chain cannot be a neutral ray switch or return state.

## 3. Right thin-laminar discharge

Consider the right boundary pair `(y,r)` from the live state. Assume the inherited no-span branch: a canonical incomparable pair strictly inside the `prec_*` interval `[y,r]_*` would already be accepted as strict strong-majority span descent.

Assume further

`Pred(y) proper_subset Pred(r)`,                                (3.1)

`Succ(r) subseteq Succ(y)`,                                    (3.2)

and that

`a` is the unique maximal element of `D_R:=Pred(r)\Pred(y)`.   (3.3)

Condition (3.1) is automatically strict here because `a<r` while `a||y`.

Let

`U_R := Succ(y)\Succ(r)`,

and let `M_R=Min(U_R)`.

### Theorem 3.1 — exact outer-fringe gap

Under (3.1)-(3.3),

`M_R` is nonempty and

`Pr(B_R \ {y<a}) > 2/33`,                                     (3.4)

where

`B_R = union_{u in M_R}{u<r}`.                                (3.5)

Moreover `|M_R|<=2`. For every `u in M_R`, no-span descent forces

`r prec_* u`,                                                  (3.6)

so every event `{u<r}` is the minority orientation of the actual incomparable pair `(r,u)` strictly farther out on the right ray.

If `M_R={u}` is a singleton, then

`Pr(u<r)>2/33`,                                                (3.7)

and the transition

`(y,r) -> (r,u)`                                               (3.8)

strictly increases the partner potential `Psi_R`.

### Proof

Apply the crossed-neighborhood identity (1.1) to `(p,q)=(y,r)`. Since this is a no-balanced state and `y prec_* r`,

`Pr(y<r)>2/3`, hence

`Pr(A_{D_R} union B_R)=2Pr(y<r)-1>1/3`.                        (3.9)

Because `a` is the unique maximal element of the finite set `D_R`, every `d in D_R` satisfies `d<=a`. Therefore

`A_{D_R}={y<a}`.                                               (3.10)

Indeed `d=a` gives the reverse inclusion, while `y<d<=a` implies `y<a`.

The old heavy-cover endpoint bound gives

`Pr(y<a)<3/11`.                                                (3.11)

Subtracting (3.11) from the union in (3.9), with no independence assumption,

`Pr(B_R\{y<a})`
`=Pr(A_{D_R} union B_R)-Pr(A_{D_R})`
`>1/3-3/11=2/33`,                                             (3.12)

which proves (3.4) and in particular shows `M_R` is nonempty. Width at most three gives `|M_R|<=2` exactly as in the lead's canonical-fringe compression.

For `u in M_R`, we have `y<u` in the poset and `u||r`. If `u prec_* r`, then

`y prec_* u prec_* r`

would be a strict inner strong-majority span furnished by the canonical fringe pair `(u,r)`, contrary to the inherited no-span branch. Hence `r prec_*u`, proving (3.6).

If `M_R={u}`, then `B_R={u<r}`, so (3.12) implies (3.7). Finally put

`i=rho(y)<j=rho(r)<k=rho(u)`.

The partner potential changes by

`Psi_R(r,u)-Psi_R(y,r)`
`=n(k-j)+(k-j)-(j-i)`.

Since `k-j>=1` and `j-i<=n-2`, the difference is at least `3`, in particular strictly positive. This proves (3.8). `square`

### Double-fringe residue

If `|M_R|=2`, Theorem 3.1 still proves that the **two-channel right outer fringe as a group** carries more than `2/33` mass outside the old interior event. What is not proved here is that one of the two individual pairs carries all of that scale. This is retained honestly as a two-channel fan, not silently collapsed by cross-anchor correlation.

## 4. Left thin-laminar discharge — exact dual

For the left boundary pair `(ell,x)`, assume

`Pred(ell) subseteq Pred(x)`,                                  (4.1)

`Succ(x) proper_subset Succ(ell)`,                             (4.2)

and `a` is the unique minimal element of

`U_L:=Succ(ell)\Succ(x)`.                                     (4.3)

Strictness in (4.2) follows from `ell<a` and `a||x`.

Let

`D_L:=Pred(x)\Pred(ell)`, `M_L=Max(D_L)`.

### Theorem 4.1 — dual exact outer-fringe gap

Under (4.1)-(4.3), `M_L` is nonempty, `|M_L|<=2`, and

`Pr(A_L \ {a<x})>2/33`,                                      (4.4)

where

`A_L=union_{d in M_L}{ell<d}`.                                (4.5)

No-span descent forces every `d in M_L` to obey

`d prec_* ell`,                                                (4.6)

so `{ell<d}` is the minority orientation of the actual left-ray pair `(d,ell)`.

If `M_L={d}` is a singleton, then

`Pr(ell<d)>2/33`,                                              (4.7)

and

`(ell,x) -> (d,ell)`                                          (4.8)

strictly increases the partner's `Psi_L` (again by at least `3`).

### Proof

Apply (1.1) to `(p,q)=(ell,x)`. The unique-minimal hypothesis implies every `u in U_L` satisfies `a<=u`; hence the canonical upper-fringe event is exactly

`B_{U_L}={a<x}`.                                               (4.9)

Because `ell prec_*x`, the total union in (1.1) has probability `>1/3`, while the old heavy-cover endpoint bound gives `Pr(a<x)<3/11`. Therefore its new lower-fringe part outside `{a<x}` has probability `>2/33`, proving (4.4) and nonemptiness. The width bound gives `|M_L|<=2`.

For `d in M_L`, `d<x` is a poset relation and `d||ell`. If `ell prec_*d`, then `ell prec_*d prec_*x` is strict inner span descent; excluding that leaves `d prec_*ell`. The singleton and `Psi_L` statements follow exactly as on the right, after reversing ranks. `square`

## 5. Consequence for the F2/F3 transport problem

Call a boundary **thin laminar** when the hypotheses of Theorem 3.1 or 4.1 hold and the newly forced opposite fringe is a singleton.

### Corollary 5.1 — no thin-laminar F2/F3 recycler

If at least one side of the `F2/F3` discrepancy-chain state is thin laminar, there is an actual incomparable pair on the same outer ray with minority probability in

`(2/33,1/3)`                                                   (5.1)

whose outward endpoint rank advances strictly. The step preserves the full local `2/33` packet scale and strictly increases `Psi_R` or `Psi_L`.

Consequently the partner's fixed-ray acyclicity theorem extends verbatim to arbitrary mixtures of its three mechanisms and these thin-laminar steps: every transition has strict integer-potential gain on the chosen fixed ray.

If **both** sides are thin laminar, then there are simultaneously vertices `d,u` with

`d prec_* ell prec_* x prec_* a prec_* y prec_* r prec_* u`,   (5.2)

and actual minority packets

`Pr(ell<d)>2/33`, `Pr(u<r)>2/33`.                              (5.3)

Thus the two-sided exposed hull expands strictly on both ends in one discrepancy-chain stage.

### What a surviving F2/F3 state must now contain

To evade Corollary 5.1, each unresolved side must exhibit at least one genuine higher-complexity feature:

1. the relevant crossed-neighborhood inclusion fails, giving a reverse-direction relation distinguisher;
2. the central `a` is not the unique extremal discrepancy, giving a second canonical same-direction discrepancy; or
3. the newly forced opposite fringe has two canonical members, giving a width-saturating two-channel fan whose **union** retains `>2/33` new mass.

Thus the original thin two-edge chain

`ell lessdot a lessdot r`

is no longer the first unpaid ray-switch state. The residual is a **double-fan / crossed multi-distinguisher F2/F3 state**. This is exactly where the partner's latest report says a new ray-switch/crossed accounting invariant is required; the present theorem removes the single-channel laminar part without assuming the partner's refuted cross-anchor PQD shortcut.

## 6. Compact conditional end-to-end argument after this run

In the lead's low-endpoint heavy-cover branch:

1. lead r17 pays comparable and anti-aligned same-ray gates;
2. B19 r46 pays the coherent same-ray gate and every high `F1/F4` sibling-fork channel, leaving only `F2/F3`;
3. Theorems 3.1 and 4.1 above pay every thin-laminar `F2/F3` boundary at the **same `2/33` charge scale**, with a strict `Psi_R/Psi_L` gain;
4. therefore any still-unpaid `F2/F3` switch must expose a crossed relation discrepancy, a second central extremal discrepancy, or a two-channel outer fan on each side that fails thin discharge;
5. account01/B10's fixed-ray potential already excludes recycling once one of these exits is converted to a same-ray endpoint advance.

The next essential missing implication is therefore:

> **DOUBLE-FAN / CROSSED RAY-SWITCH ACCOUNTING.** In the surviving two-sided high-complexity `F2/F3` state, use width three and the exact `>2/33` group charge to show that a two-channel fan or crossed reverse-direction distinguisher either yields a balanced pair, strict span descent, a proper autonomous/ordinal reduction, or converts to an endpoint advance while retaining enough certified charge for the fixed-ray potential.

No claim is made that this final implication is proved here. The parent POS3 target remains open.

## 7. Integrity / status

- account04/B10 r17 lead state: **CONSUMED/APPLIED**;
- account04/B19 r46 `F2/F3` reduction: **CONSUMED/APPLIED**;
- assigned OTHER-account account01/B10 `20260922T072132Z-b10-pos3-r11` total-order and integer-potential theorem: **CONSUMED/APPLIED**;
- lead crossed-neighborhood identity/canonical fringe compression: **CONSUMED/APPLIED**;
- right thin-laminar exact `>2/33` outer export: **PROVED**;
- left thin-laminar exact dual export: **PROVED**;
- singleton outer-fringe steps strictly increase `Psi_R/Psi_L`: **PROVED**;
- thin-laminar `F2/F3` recycling: **ELIMINATED**;
- double-fan / crossed ray-switch accounting: **OPEN**;
- parent POS3: **OPEN / NOT PROVED**;
- run classification: `ESSENTIAL_STEP_APPLIED`.

No computation was needed for the new arbitrary-size implications. No benchmark gold, credentials, scheduler identifiers, machine paths, unrelated private data/transcripts, email/Drive data, paid/remote model/API/Codex calls, workflow dispatch, permission bypass, public posting, or brain-installation work was used. The report contains only scoped mathematics, logical fleet labels, repository-relative provenance, and nonsecret Git object identifiers.
