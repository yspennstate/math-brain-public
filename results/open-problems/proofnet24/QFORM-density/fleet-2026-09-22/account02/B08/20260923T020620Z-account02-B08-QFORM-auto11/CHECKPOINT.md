SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-23T02:06:20.291113Z.
attacking: the one-child/two-cross hybrid left by the actual spectral gate, using collective-tail volume smoothing before isolating the genuinely low-rank/high-leverage survivors.

# SUBSTANTIVE CHECKPOINT — one-child/two-cross hybrid trichotomy

Programme: QFORM-DENSITY-3EIG-20260922. Full target remains OPEN. This checkpoint uses only original-coordinate product structure and actual blocks of the full matrix; it does not delete the complementary spectrum or rotate the random inputs.

## Sources used at equations

1. Designated partner account03/B08, commit `b588302bae921f92fa9f1af9c04f44ad113facb8`, theorem `QFORM-DIFFUSE-CURVATURE-TRANSFER-LADDER-v1`. For selected three-eigenvector leverage at most 1/48 and large-eigenvalue scale L, it supplies a balanced physical cut with

`c0=(L/2)sqrt(3/5)`, `beta=(3L/16)sqrt(3/5)`,

and if one child has fewer than two actual eigenvalues of modulus at least c0 then the ACTUAL cross block B has `s2(B)>beta`.

2. `c2414ef633b9d4b7f04a83e1aeefbe713ed82bba`, `PEER_TAIL_EXTENSION.md`. For a cross block B, top-two left projection P, `T2=sum_(j>=3)s_j(B)^2`, if `max_i P_ii<=1/2` and `s3(B)<=sqrt(T2)/15`, then

`||p_Q||_inf <= (9 sqrt(3) e/2)[s1(B)^2 s2(B)^2 T2]^(-1/6)`.

All same-side blocks/outside couplings remain arbitrary. Independent review is pending at source.

3. Newest-Claude `e5f71d79eff325201dd0274053d20268ce65b837`, Theorem D. If the 3-volume row marginals of B are all at most 1/2 and `Z=e3(B^T B)`, then

`||p_Q||_inf <= 6 sqrt(e) Z^(-1/6)`.

## Lemma — quantitative survivor split

Assume the partner gate gives `s2(B)>beta`. Let P be a top-two left singular projection of B and let `T2=sum_(j>=3)s_j(B)^2`. Fix `0<eta<=1`. Then at least one of the following holds.

(A) LOW-TAIL: `T2<eta^2 beta^2`. Consequently the rank-two truncation `B2=PB` satisfies
`||B-B2||_F<eta beta` and `s2(B2)>beta`.

(B) PHYSICAL-ROW HUB: `max_i P_ii>1/2`. Then for some physical row i,
`||B[i,*]||_2^2 >= s2(B)^2 P_ii > beta^2/2`, hence `||B[i,*]||_2>beta/sqrt(2)`.

(C) COLLECTIVE-TAIL EXIT: `T2>=eta^2 beta^2`, `max_i P_ii<=1/2`, and `s3(B)<=sqrt(T2)/15`. The peer-tail theorem gives

`||p_Q||_inf <= (9 sqrt(3)e)/(2 beta eta^(1/3))`.

(D) THREE-VOLUME EXIT OR VOLUME HUB: `T2>=eta^2 beta^2`, `max_i P_ii<=1/2`, and `s3(B)>sqrt(T2)/15`. Then

`s3(B)>eta beta/15`,
`Z>=s1^2 s2^2 s3^2 > beta^6 eta^2/225`.

If every 3-volume row marginal is at most 1/2, newest-Claude Theorem D gives

`||p_Q||_inf < [6 sqrt(e) 15^(1/3)]/[beta eta^(1/3)]`.

Otherwise some physical row carries more than half of the complete squared 3-volume; call this the VOLUME-HUB survivor.

The four alternatives are exhaustive by the definitions of T2, P, s3 and the volume marginal gate. This converts the k=1 actual-spectral hybrid into two paid branches and two sharply named survivors, instead of leaving an undifferentiated 'one child + two cross directions' case.

For the clean choice `eta=1/8` and L>=1,

`beta=(3/16)sqrt(3/5)L = 0.14523687548... L`.

The paid constants are respectively

`(C) < 291.757/L`,
`(D) < 335.956/L`.

Thus outside LOW-TAIL (`||B-B2||_F<beta/8`) and the two explicit hub conditions, the full ambient quadratic form already has a universal continuous density bound `<336/L`.

## N3 interpretation of the physical-row hub

At the standard no-pivot scale `tau0=1/8192`, the physical pair determinant gate and diagonal gate imply every cross entry obeys

`|A_ij|<eps0=sqrt(tau0+tau0^2)=0.011049217785...`.

In the PHYSICAL-ROW HUB branch, a row has squared norm `>beta^2/2`. At L=1 this cannot be supported on 86 or fewer cross coordinates because

`beta^2/(2 eps0^2)=86.3894544...`.

Hence such a survivor is necessarily a genuinely broad physical star (at least 87 nonzero cross entries at this cap), not a hidden single good pair.

## Genuine low-tail witness

Let U be three normalized Hadamard columns in R^m and put
`P0=diag(1-delta,1/5,1/5)`,
`C=U P0 U^T`, `B=U(I-P0)U^T`, `A=[[C,B],[B,C]]`.
For 0<delta<=1/10, A has exactly three eigenvalues of modulus at least 1 (the + block eigenvalues 1,1,1); the - block eigenvalues are `1-2delta,-3/5,-3/5`. The selected three-large-eigenvector leverage is `3/(2m)`. Each physical child has exactly one c0-large eigenvalue, while B has singular values `4/5,4/5,delta` and top-two projection diagonal `2/m`.

Thus as delta -> 0 this family lies genuinely in LOW-TAIL with a diffuse top-two cross range. Cross-volume-only payment necessarily degenerates like delta^(-1/3); the missing mechanism really must mix retained child curvature with an almost-rank-two cross block, or exploit additional full-range structure unavailable for an arbitrary spectral remainder.

Status of checkpoint: ESSENTIAL_STEP_APPLIED / SUPPORTING STRUCTURAL CLASSIFICATION. Full QFORM remains open. First unpaid implication after this split: pay the LOW-TAIL diffuse rank-two survivor, or transfer a PHYSICAL/VOLUME-HUB survivor into an existing product-preserving grouped-coordinate theorem, without perturbatively deleting the tail.