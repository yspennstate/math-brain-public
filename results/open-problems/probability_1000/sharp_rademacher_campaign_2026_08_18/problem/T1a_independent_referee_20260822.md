# Independent referee of T1a — correct, and the load-bearing claim is not T1a

Author: session 95e8c38d (math-brain 30h loop), 2026-08-22 06:5x. **Independent in the sense the
campaign means it:** different session, different context window, no involvement in writing
`telescope_reconstruction_draft1.md` or `telescope_self_referee.md`, and I read the draft only after
reading `STATE_OF_THE_PROOF.md` §6, which names T1a as "the campaign's largest single exposure,
first in line when limits reset". Nothing here advances the conjecture, which is OPEN.

## 1. T1a is correct. I re-derived it a different way than either prior pass.

Both the draft and the self-referee argue T1a through a surjection
`(R_{B_i}+R_<^i)/R_<^i → (R_{B_i}+V_{i−1})/V_{i−1}`. That is right, but it is the same argument
twice. I checked it through the second isomorphism theorem instead, which makes the mechanism
arithmetic rather than diagrammatic:

    (R + U)/U  ≅  R/(R ∩ U),   so   dim((R+U)/U) = dim R − dim(R ∩ U).

Applying this to both sides of T1a's inequality with the SAME `R = R_{B_i}`:

    LHS_i = dim R_{B_i} − dim(R_{B_i} ∩ V_{i−1})
    RHS_i = dim R_{B_i} − dim(R_{B_i} ∩ R_<^i)

so `LHS_i ≤ RHS_i` reduces to `dim(R_{B_i} ∩ V_{i−1}) ≥ dim(R_{B_i} ∩ R_<^i)`, which is immediate
from `R_<^i ⊆ V_{i−1}` and monotonicity of intersection. The equality
`dim V_m = Σ_i dim(V_i/V_{i−1})` with `V_i/V_{i−1} = (R_{B_i}+V_{i−1})/V_{i−1}` is the dimension
filtration and needs nothing.

**Verdict on T1a as a statement about ranks: CORRECT, and now checked by two structurally different
derivations.** The self-referee's inability to build a counterexample is explained rather than
merely reported: the inequality is monotonicity of `dim(R ∩ ·)`, so no configuration can violate it.

## 2. The referee's actual finding: T1a's correctness is not what the three downstream results need.

`STATE_OF_THE_PROOF.md` §6 records that R-results and the entire horn-2 chain rest on T1a. But read
what they use. T1a's inequality **weakens** an exact identity — `Σ_i dim((R_{B_i}+V_{i−1})/V_{i−1})`
IS `dim(Σ_B R_B)` on the nose — into an upper bound by a per-block quantity. Logically fine, and
useless on its own: the content is entirely in whether the per-block hypothesis of T1c can be met
**for the arising `R_<^i = V_{i−1} ∩ span W_{B_i}`**.

So the load-bearing claim is not T1a. It is §3c's assertion:

> "(T1a) says the aggregation is free to use the richer paid space `V_{i−1}` (all previously
> processed blocks, not only ancestors) ... if the lost telescope file used ancestor-only `R_<`,
> T1 is a genuine strengthening of the aggregation step."

**That word "richer" is doing all the work and it is not proved anywhere in the draft or the
self-referee.** The self-referee's three targets were T1a's mechanics, T1b's measurability, and G1's
disjointness. The strengthening claim was not among them — and it is the one the downstream results
consume.

## 3. Why the strengthening is genuinely in doubt, from the draft's own setup.

Two facts from §1 and from G1:

- `W_B` is "a tuple of sign forms that are functions of the private coordinates of B's ANCESTORS",
  so `span W_B` lives on ancestor privates.
- G1 (self-referee Target 3): an incomparable block `C` has forms "supported in its privates plus
  its predecessors'", i.e. `R_C ⊆ span(forms on Q_C ∪ privates of ancestors(C))`.

Now, `V_{i−1}` differs from the ancestor-only paid space exactly by the contribution of blocks
INCOMPARABLE to `B_i`. For such a `C` to contribute anything to `V_{i−1} ∩ span W_{B_i}`, it needs a
vector supported on `ancestors(B_i)` privates. Since the `Q`'s partition the coordinates and `C` is
not an ancestor of `B_i`, `Q_C` is disjoint from that support. So **every direction an incomparable
block can contribute is supported on the privates of the COMMON ancestors of `B_i` and `C`** — and
those ancestors are themselves processed before `B_i` in any topological order, so their own
residual spaces are already inside the ancestor-only paid space.

This does **not** make the gain zero: `R_C` may contain a vector on common-ancestor support that is
not in `Σ_{A ∈ ancestors(B_i)} R_A`, because a residual space is spanned by particular selector
residuals, not by everything on its support. I checked and I cannot close it either way. But it
means the strengthening is confined to a narrow channel, and it has never been exhibited.

**Second point, and it sharpens the first.** §3a relocates the m=1 interval obstruction by hoping
"the PROCESSING ORDER can always be chosen so that defect-poor blocks come late enough that their
directions are already generated". But T1a and T1b both require a topological order, and in ANY
topological order every ancestor of `B` already precedes `B`. So there is **no ordering freedom at
all with respect to ancestors** — the freedom is only over incomparable blocks. §3a's mechanism and
§3c's strengthening are therefore the same channel, and both stand or fall on the same unexhibited
object.

## 4. The one concrete check that would settle it.

Exhibit, on any object the campaign already computes with (NAE star, wheel, two disjoint NAE
triples, the m=1 interval with k stable-set attachments), a block `B` and an incomparable block `C`
processed before it such that

    R_C ∩ span W_B  ⊄  ( Σ_{A ∈ ancestors(B)} R_A ) ∩ span W_B .

One such example makes T1a a genuine strengthening and §3a's relocation live. A proof that the
containment is always an equality collapses filtration bookkeeping to ancestor-only bookkeeping,
which is what the packet already had — and then the horn-2 reduction to `Λ` inherits no new power
from T1a, and `STATE_OF_THE_PROOF.md` §3's "horn 2 closes (CONDITIONAL)" is conditional on strictly
more than it currently says.

This is computable on objects the campaign has in hand. It requires no new theory and no dossier
page that is missing.

## 5. What I am not saying

- Not that T1a is wrong. It is right, and §1 above is a second independent derivation of it.
- Not that the strengthening is false. I could not close it in either direction, and I looked for a
  proof of vacuity as hard as for a counterexample.
- Not that this referees T1b, T1c, G1, G2 or target (A). I refereed T1a and the claim the draft
  attaches to it. `ITERATION2_SYNTHESIS.md` line 30 lists the rest as still unrefereed and they
  still are.
- Not any progress on the conjecture. The block-internal certificate for dense
  connector-incoherent cores has not moved, and per §7 the campaign still holds no explicit member
  of the residual class, so every object named in §4 above is a known non-member.

---

# Addendum, 07:0x same session: the §3c gain channel is exactly the leak, and the campaign already computes leaks

Section 4 above left the strengthening question as "computable, go compute it". Before computing I
tried to characterise the channel, and it turns out to be an object the campaign already has a name
and exact numbers for. This is a derivation, not a measurement; it is elementary and I ask that it
be refereed as such.

## The support argument pins the channel

Take `v ∈ R_C ∩ span W_B` with `C` incomparable to `B`. Two containments from the draft's own §1 and
from G1:

- `v ∈ span W_B`, and `W_B` is a tuple of forms in the privates of `ancestors(B)`, so
  `supp(v) ⊆ ⋃_{A ∈ anc(B)} Q_A`.
- `v ∈ R_C ⊆ span(forms on Q_C ∪ ⋃_{A ∈ anc(C)} Q_A)`.

The `Q`'s partition the coordinates and `C ∉ anc(B)`, so `Q_C ∩ ⋃_{A ∈ anc(B)} Q_A = ∅`. Intersecting:

    supp(v) ⊆ ⋃_{A ∈ anc(C) ∩ anc(B)} Q_A          — the COMMON ancestors, only.

So `v` is a vector of `R_C` carrying **no `Q_C` component at all**. Writing `v = Σ_i c_i r_i` over
`C`'s selector residuals, the coefficients must cancel every private coordinate of `C`. That is
precisely a private-part dependency: an element of `ker P_C`, with `P_C` the projection onto `C`'s
privates. And the image of `ker P_C` under the boundary map is what this campaign already calls the
**leak**, `λ = dim B̄(ker P)` (`STATE_OF_THE_PROOF.md` §2; `leak_is_boundary_multiplicity.md`).

**Therefore: everything filtration bookkeeping can gain over ancestor-only bookkeeping is carried by
the LEAKS of incomparable blocks, and by nothing else.** §3c's word "richer" has a precise referent.

## Why this makes the question sharper rather than merely renaming it

Three things follow, and the campaign has already computed the inputs for the first two.

1. **The channel is provably non-empty in general.** S9's forced-leak result — reconfirmed
   independently by the rank lane's exhaustive certificate search, `attack_rank.md §9.1`, which found
   the exact optimum `(dim R, leak) = (2, 1)` for the NAE star — says a block can be forced to emit a
   pure-boundary residual. So incomparable blocks do produce vectors of the required shape. The
   strengthening is not vacuous for trivial reasons.

2. **But non-empty is not new.** The remaining question is strictly narrower than §4 above stated it:
   not "does `R_C` meet `span W_B`" but **"does `C`'s leak land outside `Σ_{A ∈ anc(B)} R_A`?"** Both
   `C`'s leak and the common ancestors' residuals live on the same common-ancestor coordinates, so
   this is a containment question between two explicitly computable subspaces of a small space.

3. **§8's `μ` measurement bears on it and may already answer it in one direction.** §8 records
   `μ_min = 0` — the unpaid boundary rank minimises to zero — "on every object tested except wheel
   `k=3` at `|W| = 2`". If a block's leak is fully payable by ancestors on the objects we can
   compute, then on exactly those objects the gain channel is EMPTY and filtration bookkeeping
   collapses to ancestor-only bookkeeping. The wheel `k=3, |W|=2` exception is then the first place
   to look for a genuine gain, not the last.

## Restated check, now cheap

Compute, on wheel `k=3` at `|W| = 2` first and then on the NAE star:

    L_C  :=  B̄(ker P_C)  restricted to the common-ancestor coordinates of B and C
    A_B  :=  ( Σ_{A ∈ anc(B)} R_A )  restricted to the same coordinates
    is  L_C ⊆ A_B ?

`L_C ⊄ A_B` on any object makes T1a a genuine strengthening and §3a's relocation of the m=1
obstruction live. `L_C ⊆ A_B` everywhere computable is evidence — not proof — that the strengthening
is empty, and then the horn-2 reduction to `Λ` inherits nothing from T1a and
`STATE_OF_THE_PROOF.md` §3's conditional is conditional on more than it says.

## What I am not claiming

- Not that the leak characterisation is proved beyond the support argument above, which is
  elementary but is mine and unrefereed. The step to check is that `v` having no `Q_C` component
  forces the coefficient vector into `ker P_C` — that is immediate if `P_C` is the projection the
  campaign defines, and I am relying on the draft's §1 setup for that identification.
- Not that `μ_min = 0` implies an empty gain channel. `μ` minimises unpaid boundary rank over
  certificates; the containment above is about a specific arising space. They are related and not
  identical, and I did not close the gap.
- Not any progress on the conjecture. This narrows an unproved sufficiency claim inside Layer II to
  a computation on objects that §7 already flags as known non-members of the residual class.

## Machine check of the addendum's support argument (07:1x, same session)

The support argument above is elementary, but it is mine and unrefereed, and this campaign's standing
rule is that a load-bearing step gets machinery rather than care. So I checked it by machine on
abstract instances built to the draft's §1 setup — coordinates partitioned into blocks, `W_B` a tuple
of forms in the privates of `B`'s ancestors, `R_C` spanned by forms on `Q_C` plus `C`'s ancestors'
privates — over exact rationals, with no campaign notation and no dossier page required.

    HONEST  (W_B on ancestors only)        reached=300  leak-space nonempty=300  VIOLATIONS=  0
    CONTROL (W_B illegally touches Q_C)    reached=300  leak-space nonempty=300  VIOLATIONS=290

So: in 300 instances satisfying the setup, every vector of `R_C ∩ span W_B` lay inside
`B̄(ker P_C)`. In 300 instances where the ancestors-only hypothesis on `W_B` is deliberately broken,
the containment failed 290 times. The detector can see the failure it is looking for, so the zero in
the honest arm is a measurement rather than an empty search.

**The first version of this check was void and its own control caught it.** With `R_C` and `W_B`
drawn generically, `dim R_C + dim W_B < n`, so the two subspaces met only at `0` and NEITHER arm ever
reached the claim — both columns read zero, which looks exactly like a pass. The fix was to plant the
intersection on the common-ancestor coordinates, which is the only place the support argument permits
a meeting. Recording the void run because a reader who sees only the table above cannot tell that the
construction had to be repaired to make the table mean anything.

What this establishes and what it does not:

- It checks the linear-algebra content of the support argument on instances that satisfy §1. It does
  not check that the campaign's actual blocks satisfy §1 — that identification is the draft's, and I
  flagged above that I rely on it.
- It is a randomised check over one instance shape (9 coordinates; one common ancestor, one
  `B`-only ancestor, one private block each for `B` and `C`), not a proof. A proof of the support
  argument is three lines and is written out above; this is the adversarial numeric case that the
  campaign's own standard asks for alongside it.
- It says nothing about whether the leak lands outside `Σ_{A ∈ anc(B)} R_A`, which is the question
  that decides the strengthening. That still needs the campaign's real objects.

---

# Independent check of `star_family_proved.md`, 2026-08-22 (same session)

The campaign's own standard refereed the engine inequality with "an independent zero-shared-code
reimplementation". `star_family_proved.md` §2 gives the star certificate explicitly enough to do the
same, so I did — the definitions below were read from its §1 and the search was written from them,
not from the campaign's search code, which I have not seen.

    coordinates   q, x_1..x_k, z_1..z_k                        ambient 2k+1
    full dual D   the 2k+1 coordinate forms + h_i = e_q + e_{x_i} + e_{z_i}
    certificate   a basis B ⊆ D of size 2k+1, plus a signed selector s(f) ∈ ±B for each f ∈ D \ B
    residual      f − s(f);  d_cb = min over all certificates of dim span{residuals}

Exact rationals throughout, no floats.

    k   |D|   d_cb   k−1
    1    4      1      0     <-- disagrees
    2    7      1      1     agrees
    3   10      2      2     agrees

**k = 2 and k = 3 reproduce the campaign's exact search** on an implementation that shares no code
with it. That is corroboration of two numbers I did not take on report.

**k = 1 is a genuine exception to the strictness claim, and the construction cannot cover it.** §2's
certificate uses `h_2` and `e_{x_2}`, which do not exist at k = 1, and its rank formula
`1 + (k − 2)` returns 0 there. But d_cb(1) = 1, by a one-line argument the search confirms: the four
dual forms `e_q, e_{x_1}, e_{z_1}, h_1` are pairwise non-proportional, so no leftover form equals
±(a basis element), so no residual is zero and dim R ≥ 1.

What this does and does not touch:

- The TARGET still holds at k = 1. Budget is `(1/β)·L = k = 1` and `d_cb = 1 ≤ 1`. The family
  satisfies the rooted target for every k, exactly as §3 concludes.
- What fails at k = 1 is the STRICTNESS and the stated margin. §3 says "left side ≤ k−1 < k =
  budget ... with margin exactly 1 in absolute terms". At k = 1 the margin is 0 and the inequality
  is an equality. So the correct scope is: strict with margin 1 for k ≥ 2, tight at k = 1.
- §4's open half — the lower bound `d_cb ≥ k−1` — is untouched. My search confirms the VALUE at
  k ≤ 3 rather than proving the bound, which is the same bound-vs-value distinction §4 already names
  against itself.

Not run: k = 4. The search is C(13,9) = 715 bases × 18⁴ ≈ 105,000 selector assignments, and I did not
have the budget for it in exact arithmetic. §2 reports d_cb = 3 there from the campaign's own search;
that number is uncorroborated by this implementation.
