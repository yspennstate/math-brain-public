SIGNED IN - working on the quadratic-form bounded-density conjecture (universal constant), account account02, slot B08, 2026-09-24T10:44:26.864724Z.
attacking: intersect the newest five-large/ten-bank localized-diffuse router with account03/B08's split-alignment Pythagoras; turn the two surviving collars into literal original-coordinate bank packets and stress them on an exact target Walsh family.

# account02/B08 r37 — split-slope eight-bank packet and ultra-common sixteen-bank exact-frame crossing footprint

Programme: `QFORM-DENSITY-3EIG-20260922`  
Assignment: diffuse eigenvector case / complementary constructions and source-valid obstructions  
Status: **NEW SUPPORTING HYBRID ROUTER + TARGET-VALID COLLAR STRESS FAMILY / FULL QFORM OPEN**  
Execution: `WITHOUT_VERIFIED_BRAIN`.

The unrestricted cap-one product-source conjecture remains **OPEN**. No moment, support, log-concavity, Gaussianity, diagonal-basis independence, post-rotation independence, arbitrary-joint coarea, fiber-supremum estimate, or law-uniform pointwise quadratic-phase decay is used. Continuity is claimed only on the explicit fixed-source Fourier payment below.

## 0. First unpaid implication

After the already-completed continuous third-compound payment and the newest account01/B08 five-large-eigenvalue inductive exit, the primitive thin-puncture survivor can be forced into one of two product-coordinate packets:

1. **split-slope mismatch packet:** a source-safe scalar coefficient vector of norm `>6.328856436640812e-6 L` that can be partitioned into **eight disjoint original-coordinate banks**, each carrying coefficient norm at least `1.582214109160203e-6 L`; or
2. **ultra-common exact-frame packet:** the exact child top-two spectral frame contains a unit direction carrying norm `>0.14977509401605973` on **sixteen disjoint original-coordinate banks**, and at least **thirteen** of those banks have an actual literal child cross block of operator norm `>0.10455383978519894 L`.

The first unpaid implication is therefore

`QFORM-EIGHTBANK-MISMATCH-OR-SIXTEENBANK-EXACTR2-COMPILER-v1`:

> consume either the eight-bank split-slope packet or the sixteen-bank exact-rank-two packet while retaining arbitrary same-bank child curvature, arbitrary complementary spectrum, affine terms, and the original product coordinates. The compiler must remain uniform as the child third singular value tends to zero; it may not infer an independent convolution factor from the mismatch scalar or infer a positive third exterior volume merely from many large rank-two cross blocks.

The Walsh family in Section 5 shows that the second warning is real.

## 1. Fresh inherited gates

The newest completed localized/diffuse B08 source used here is account01/B08 r48,

`yspennstate/math-open-problems@6aeabdd6343abdea18945673eafbb3ed9fa42fe5`,
`proofnet24/QFORM-density/fleet-2026-09-22/account01/B08/20260924T094957Z-account01-B08-qform-r48/REPORT.md`.

Its exact selected spectral component is `A_3=U Lambda U^T`, with three actual eigenvalues of modulus at least `L`. In the two-mode complementary-cancellation branch it proves

`s_2((A-A_3)[S\{k},T]) > sigma L`,
` sigma=(1/2)sqrt(67/800)=0.14469796128487783...`.

Compression monotonicity then gives two additional eigenvalues of `A` of modulus `>sigma L`, hence at least five eigenvalues at the scale `sigma L`. By the hereditary five-large-eigenvalue theorem this branch is an inductive dimension-drop exit, with cost factor

`sqrt(3200/67)<6.911`

relative to the lower-dimensional constant. Thus it is no longer a primitive B08 obstruction in a dimension induction.

The same r48 source leaves a relative rank-two aligned branch and proves a ten-bank carrier footprint there. Its immediate predecessor account01/B08 r47 supplies the sharper physical star data needed below. For the actual physical star `b=A[k,-k]`, it selects a literal cut with `z=b_T` satisfying

`||z|| >= sqrt(9/20) ||b||`,

and sixteen disjoint original-coordinate banks `J_1,...,J_16 subset T` satisfying

`||z_{J_r}|| > (sqrt(31)/24)||z||` for every `r`.

The newest completed designated partner is account03/B08 r51,

`yspennstate/math-open-problems@b72d0f5814183fc536c65a4b9dbbbec4ae93d611`,
`proofnet24/QFORM-density/fleet-2026-09-22/account03/B08/20260924T092359Z-account03-B08-qform-diffuse-r51/REPORT.md`.

It works in the same thin-puncture hub/child state

`A=[[a,b^T],[b,C]]`,
`C=V Lambda V^T+E`,

where `V` has two orthonormal columns,

`s_2(C)>=m_0 L`, `m_0=sqrt(47/48)`,
`||E||_op=s_3(C)<L/4096`,
`max_i ||V_{i,*}||^2<=1/16`.

For a balanced child split `J union K`, define the bankwise least-squares coefficient mismatch `delta=c_J-c_K`, the global exact-frame distance

`beta=dist(b,range V)`,

and use `eta=2^-20`. Its exact Pythagoras identity and tunable third-compound payment give the trichotomy:

- `||p_Q||_infinity <2369.566/L` with `p_Q in C_0`; or
- split-slope mismatch; or
- ultra-common alignment
  `beta/||b|| < eps_*`,
  `eps_*=0.005848650958799406`.

If the mismatch branch occurs while the ultra-common inequality fails, r51 gives the target-scale gate

`||delta|| > d_* L`,
`d_*=6.328856436640812e-6`.

## 2. New theorem A: mismatch gives an eight-bank original-coordinate packet

### Theorem `QFORM-SPLITMISMATCH-EIGHTBANK-PACKET-v1`

In the r51 split-slope mismatch branch, define the physical coefficient vector `q` by

`q_i=(V_i delta)` for `i in J`,
`q_i=-(V_i delta)` for `i in K`.

Then

`||q||_2=||delta||_2`,

and every physical coordinate obeys

`|q_i|^2 <= ||delta||^2/16`.

Consequently there exist eight pairwise-disjoint ORIGINAL-coordinate banks `B_1,...,B_8` such that

`boxed:  ||delta||/4 <= ||q_{B_r}|| < ||delta||/sqrt(8),  r=1,...,8.`

On the target-scale mismatch gate this becomes

`boxed: ||q_{B_r}|| > 1.582214109160203e-6 L` for all eight banks.

#### Proof

Because `V^T V=I_2`, changing signs between `J` and `K` does not change Euclidean norm:

`||q||^2=delta^T(V_J^T V_J+V_K^T V_K)delta=||delta||^2`.

The physical leverage bound gives

`|q_i|<=||V_i|| ||delta||<=||delta||/4`.

Normalize squared atom masses `a_i=|q_i|^2/||delta||^2`. Then `sum_i a_i=1` and `a_i<=1/16`. Greedily form a bank by adding unused atoms until its mass first reaches `1/16`. Each completed bank has mass in `[1/16,1/8)`. After seven such banks, less than `7/8` of the total mass has been used, so the remainder still contains more than `1/8` and an eighth bank can be completed in the same way. Taking square roots proves the claim.

This upgrades r51's legitimate scalar mismatch into a distributed physical coefficient packet without declaring that scalar independent of any longitudinal slope. In particular each normalized bank projection has the standard cap-`sqrt(2)` product-source density bound, and the twisted Fourier `L^p` estimate from the cap-one projection lemma is available bankwise; the missing step is a dependence-safe compiler through the inter-bank quadratic phases.

## 3. New theorem B: ultra-common alignment gives sixteen exact-frame banks

Set

`a_* = sqrt(31)/24`,
`s_* = sqrt(9/20)`,
`eps_* = 0.005848650958799406`,
`c_* = a_* s_* - eps_*`.

Numerically

`boxed: c_*=0.14977509401605973.`

### Theorem `QFORM-ULTRACOMMON-SIXTEENBANK-EXACTFRAME-v1`

Assume the r47 sixteen-bank star packet and the r51 ultra-common branch. Let `P=VV^T`, `v=Pb`, and `u=v/||v||`. Then for every one of the sixteen inherited physical banks,

`boxed: ||u_{J_r}|| > c_* =0.14977509401605973.`

#### Proof

Write `e=b-v`. Then `||e||=beta<eps_*||b||`. Since `J_r subset T`, `b_{J_r}=z_{J_r}`. Therefore

`||v_{J_r}|| >= ||b_{J_r}||-||e_{J_r}||`
`               > a_*||z||-eps_*||b||`
`               >= (a_* s_*-eps_*)||b||`
`               = c_*||b||`.

Since orthogonal projection gives `||v||<=||b||`, division by `||v||` proves the assertion. No random variable is rotated; this is a statement about deterministic coefficients in the exact child spectral plane.

This is substantially stronger than the r48 ten-bank `1/24` carrier footprint, but only on r51's ultra-common collar: all sixteen inherited star banks survive in the exact child frame, at a per-bank norm above `0.1497`.

## 4. New theorem C: thirteen literal target-scale child cross blocks

For each bank put

`G_r=V_{J_r}^T V_{J_r}`.

The banks are disjoint and `V^T V=I_2`, so

`sum_{r=1}^{16} tr(G_r) <=2`.

Hence at most three banks can satisfy `tr(G_r)>1/2`. Therefore at least thirteen banks satisfy

`G_r <= (1/2)I_2`,
`V_{J_r^c}^T V_{J_r^c}=I_2-G_r >=(1/2)I_2`.

### Theorem `QFORM-ULTRACOMMON-THIRTEEN-LITERAL-CROSSBLOCKS-v1`

On at least thirteen of the sixteen banks,

`boxed: s_1(C[J_r^c,J_r]) > kappa_* L`,

where

`kappa_* = (m_0 c_*)/sqrt(2)-1/4096`
`        =0.10455383978519894... .`

#### Proof

Fix a good bank and set `w_r=u_{J_r}/||u_{J_r}||`, an ORIGINAL-coordinate unit vector supported on `J_r`. Because `u in range(V)`,

`||V^T w_r|| >= |<u,w_r>|=||u_{J_r}||>c_*`.

The rank-two spectral part gives

`||V_{J_r^c} Lambda V^T w_r||`
` >= (1/sqrt(2)) ||Lambda V^T w_r||`
` >= (m_0 L/sqrt(2)) c_*`.

The exact residual contributes at most `||E||op<L/4096`. Therefore

`||C[J_r^c,J_r]w_r||`
` >= ||V_{J_r^c}Lambda V^T w_r||-||E[J_r^c,J_r]w_r||`
` > [(m_0 c_*)/sqrt(2)-1/4096]L`.

Taking the operator norm proves the claim.

Thus the ultra-common collar contains not merely abstract rank-two leverage but at least thirteen literal original-coordinate cross blocks at a fixed target scale. What it still need not contain is any positive third exterior volume: all thirteen blocks may be generated by the same two-dimensional carrier.

## 5. Exact target-valid stress family: abundant cross blocks but vanishing third child curvature

Let `m=2^q` with `m>=32768`, and choose three distinct normalized Walsh characters `u,v,w in R^m`. Add one separate physical hub coordinate `0`. For

`0<eps<1/4096`, define

`A_eps = [[0, (sqrt(2)L u)^T],
          [sqrt(2)L u, L uu^T+L vv^T+eps L ww^T]].`

In the orthonormal basis `(e_0,u,v,w)` the nonzero matrix is

`L * [[0,sqrt(2),0,0],
      [sqrt(2),1,0,0],
      [0,0,1,0],
      [0,0,0,eps]].`

Hence its nonzero eigenvalues are exactly

`boxed: {2L,-L,L,eps L}.`

For every `0<eps<1`, it is therefore a genuine target matrix with exactly three eigenvalues of modulus at least `L`. The child top-two plane is exactly `span(u,v)`, the global star is exactly aligned (`beta=0`), `s_3(C)=eps L`, and the top-two physical leverage is `2/m<=1/16`.

Choose a Walsh half of the light coordinates as `T`; then `||b_T||=||b||/sqrt(2)>sqrt(9/20)||b||`. Split that half into sixteen equal physical banks. Since `u` is flat,

`||b_{J_r}||/||b_T||=1/4>sqrt(31)/24`,

so the exact family realizes the sixteen-bank collar. At `eps=0` every child and augmented star crossing generated by this low-rank component has rank at most two; the thirteen large cross-block energies therefore do not force a third compound.

No uniformly conditioned physical pair is hidden here. A hub-light `2x2` principal block has least singular value at most `sqrt(2)L/sqrt(m)<=L/128` for `m>=32768`, while every light-light `2x2` block has operator norm at most `2(2+eps)L/m<L/64`. Thus the family simultaneously has the exact target spectrum, a diffuse physical carrier, many target-scale grouped cross blocks, and weak physical two-coordinate pivots.

### Required fixed-source theorem applied to this real family

Use Theorem F from the pinned source

`yspennstate/math-open-problems@e5f71d79eff325201dd0274053d20268ce65b837`,
`proofnet24/QFORM-density/interactive/20260922T211500Z-decoupling-brascamp-lieb/RESULTS.md`.

Take the light coordinates as `I`, the three selected child squares as the rank-three frame `(u,v,w)` with coefficients `(L,L,eps L)`, and put the hub coordinate in `J`. The hub-star terms are then in the arbitrary `I-J` block, while the remaining `I-I` term is diagonal (zero). Since every light-row leverage is `3/m<=1/2` and `G_I=I_3`, Theorem F gives, for every admissible cap-one product source,

`boxed: ||p_{X^T A_eps X}||_infinity <= 12 eps^(-1/3)/L,`

with `p in C_0(R)`.

At the concrete collar point `eps=2^-16`,

`boxed: ||p||_infinity <=483.8096831596312/L.`

This is an actual target inequality from the required fixed source. It also exposes the nonperturbative obstruction cleanly: the source-F constant diverges like `eps^(-1/3)` as `eps downarrow0`, although the three target eigenvalues `{2L,-L,L}` remain fixed. Hence a uniform proof of the ultra-common branch must exploit the hub/carrier structure rather than pay for the vanishing child third curvature.

The family is a proof-mechanism obstruction, not a counterexample to QFORM.

## 6. Quantified updated hybrid router

Combining the newest localized/diffuse source and designated partner gives the following live packet in the thin-puncture diffuse chamber:

- the two-mode complementary-cancellation branch has five genuine eigenvalues at scale `sigma L` and is an inductive dimension-drop exit;
- a literal third-compound misalignment of size `eta=2^-20` pays continuously by `<2369.566/L`;
- if the split coefficients genuinely disagree, the mismatch coefficient has the new eight-bank packet of Section 2, with each bank carrying `>1.5822141e-6 L`;
- otherwise the star lies within `0.5848651%` of the exact child two-frame, and Sections 3--4 force sixteen exact-frame banks and at least thirteen literal child cross blocks above `0.1045538 L`.

The remaining obstruction is therefore not lack of physical energy. It is **rank-two coherence**: a great deal of original-coordinate cross energy can remain trapped in one common two-dimensional carrier, while the third target eigenvalue is created by the physical hub rather than by a third child direction. A successful compiler must combine the hub variable with this distributed rank-two carrier without post-rotation independence and without worst-fiber `|t|^-1` reasoning.

## 7. Status

Full universal essential density bound: **OPEN**.  
Valid counterexample: **none produced**.  
Full-target continuity: **OPEN**.  
New results in this report are deterministic coefficient/spectral routers plus one pinned-source continuous payment on the explicit Walsh collar family.
