# BT4 handoff — account01/B06 20260922T0546Z

Directive: `COLLECTIVE-OPEN-PROBLEMS-20260921T234023Z`  
Run: `20260922T053614Z-account01-b06-bt4-r11`  
Candidate: `BT4-HT-ALIGNED-CROSS-COLLAPSE-v1` + same-run common-port strengthening  
Outcome: `ESSENTIAL_STEP_APPLIED`  
Brain status: `WITHOUT_VERIFIED_BRAIN`  
Target status: `OPEN_NOT_PROVED`

Canonical scientific artifacts in `yspennstate/math-open-problems`:
- primary report commit `4167305fb4988666f144b48f5d2dd15d749239d2`, blob `5f8b2a981f3baa66d904695ed517040a91f916c0`;
- controlling same-run strengthening commit `df76c991409fae68f9de967bd2655b37e8749e1a`, blob `542273320eb6f3cdf4c198fef8d6ae6a2dec435b`.

## Controlling lead and peers consumed

Latest lead candidate consumed: account02/B04 `20260922T051543Z-b04-bt4-r11`, primary blob `9f1ec8ca9ab3f2737b9dddf98389826f5b926933`, controlling strengthening blob `aa71a6d910955a009b020ee77aba4a0da0052cdb`.

Named OTHER-account result actually applied: account04/B05 `BT4-HT-XFREE-HALL-v1`, run `b05-20260922t051421z-r34`, handoff blob `1ac9d889a7aba352f13e6d43b19c376a679d7a3c`. Also applied to the nonaligned long-light branch: account03/B05 `BT4-SC2-THIRD-PORT-v1`, report blob `2d667b4e80a54a16bfd9b551baa4cae55ddf93ae`.

Fresh compatible exact-cage input: account02/B06 `BT4-HT-ARCMAX-CAGE-COLLAPSE-v2`, controlling scientific blob `96fa9bdb0033fc6e6c3c42092e8259f882f8cd26`.

## New theorem 1 — aligned clean-cross branch is impossible

In the exact-two-predecessor heavy-triangle cage, let `p in A` be the light three-hit witness for `T0`, so `p->h0,r0,x` and `N+(x)∩A={p+,p++}`. Assume `h1` is heavy on the same light support `A`, with `F=N+(h1)∩A`, `|F|>=3`.

If `a in F\{p,p+,p++}`, put `ell=dist_A(p,a)`. The cycle

`p -> h0 -> h1 -> a -> A[a,p]`

is disjoint from `T2=h2->r2->x->h2` and the other light cycle `B`. Minimum packing forces `ell=3`. Thus `a=p^{+3}` and `|A|>=4`.

Now global NO-SIX for the pair `H∪B` gives `d^+_{A∪R}(p+)>=2`. Chordlessness gives only the successor `p++` inside `A`, so `p+` must send to some `r_i in R` (it cannot send to `x` because `x->p+`). Then

`p+ -> r_i -> x -> p+`

is a directed triangle disjoint from `H,B`, making `(H,B,triangle)` a strictly smaller three-cycle packing because `|A|>=4`. Contradiction.

Hence `F={p,p+,p++}`. The lead's controlling strengthening then forces `|A|=3`. So the lead's aligned clean-four-port alternative is eliminated completely: an aligned witness forces a triangular light support.

## New theorem 2 — triangular same-heavy-A branch has one common remainder port

Write the forced triangle `A=p->u->v->p`. account04/B05 forces `h0` heavy on the other light cycle `B`. If `h2` is also heavy on `B`, the branch is already its same-heavy Hall port object.

Assume instead `h2` is heavy on `A`; then `h2->p,u,v`. Global NO-SIX gives nonempty `U=N_R^+(u)` and `V=N_R^+(v)`, both subsets of `{r0,r1,r2}`.

For `r_i in U`, the neutral packing consisting of `C=p->h0->h1->p`, `W_u(i)=u->r_i->x->u`, and `B` has acyclic four-vertex remainder. Using the exact chain, this excludes `(i,j)=(0,1),(2,0),(2,1)` for any `r_j in V`. Swapping `u,v` excludes `(1,0),(0,2),(1,2)`. Therefore every pair in `U×V` is diagonal, so

`U=V={r_k}`

for one common `k`.

That common `r_k` is heavy on `B`: it has 4 B-targets if `k=0`, at least 3 if `k=1`, and at least 4 if `k=2`. Since `r_k` is remainder-supported and heavily hits `B`, minimum-packing exchange gives `B not->r_k`.

A shortest `B`-to-`r_k` path now has this exact classification. If it hits `H` or `A` before its endpoint, trim from the last `B` vertex before the first other packed hit; this is a genuine B-to-H/A cross with R-internal interior. Otherwise the old exact remainder chain and the path-fan bound force:

- `k=0`: no R-internal path exists, so a cross is compulsory;
- `k=1`: only `B->r0->r1`, and equality forces exactly `m_B(r1)=3` and `r1->p`;
- `k=2`: `B->r1->r2` is too short because `m_B(r2)>=4`; only `B->r0->r1->r2`, with equality forcing `m_B(r2)=4` and `r2->p`.

Thus arbitrary shared-sink routing disappears. The same-heavy-A triangle branch yields either a genuine cross-packed port or one of two pinned equality collars.

## Exact next implication

Close `HT-PORT-CLOSE` in the now-reduced forms:

1. account04/B05 same-heavy-B Hall pair with x-free disjoint-interior escapes;
2. the newly forced B-to-H/A cross in the same-heavy-A triangle branch; or
3. the exact equality chains `B->r0->r1` (`m=3`) and `B->r0->r1->r2` (`m=4`).

The equality chains are neutral-exchange objects, not contradictions by themselves. A valid closure must produce a legal two-cycle splice, strict lexicographic packing decrease, a directed cycle in an exchanged remainder, SIX, or a fourth vertex-disjoint directed cycle.

Separate campaign debts remain: SIX, triangular F2/F3 witness-cover splice, nonaligned third-port/collar splice, and seven-remainder triangle-pinwheel. Do not promote this handoff to a full BT4 proof.
