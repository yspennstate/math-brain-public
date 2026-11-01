# C0052 referee packet, w473, 2026-10-10

## Scope and source

The precise 2017 source target is nonvanishing of the near-critical renormalized four-point coupling g(beta), with beta increasing to beta_c in the nearest-neighbor zero-field Ising model on Z^3. The source defines g by its equation (7.1) as the sum of U4 divided by chi^2 xi^3, defines chi and xi in (7.2), and says that g tending to zero is triviality. Source: Duminil-Copin, *Lectures on the Ising and Potts models on the hypercubic lattice*, printed p.94, https://www.ihes.fr/~/duminil/publi/2017PIMS.pdf. Its Exercise 34 defines U4 and states U4<=0. Thus g_+=-g is the positive convention used by w471. The primary source's other 4D clause has a later 2021 result; this packet makes no claim of a rigorous 3D solution. Current openness is UNKNOWN after a bounded search.

My independent Lee-Yang route was saved in ROUTE_PRECOMMIT.md before I read either peer proof. W471 and w472 independently chose the same zero method, so my own finite-volume lemma is mathematically redundant with their L1. I review their actual author claims directly here; I do not promote my own lemma without w476 review.

## Independent reproduction of the hardest step

Let K=-U4 and A=sum_{x2,x3,x4}K(0,x2,x3,x4). For beta<beta_c, assume finite chi and xi, translation invariance, G>=0, and K>=0. The source gives K>=0 for distinct sites; repeated-site cases also follow directly from sigma_x^2=1: four equal gives K=2; a triple and one other gives K=2G; two pairs give K=2G^2; one pair plus two other sites gives K=2G(a,b)G(a,c). The assumed A<infinity is the required absolute summability. It follows, without any independence assumption, that for S=sum_{x in Lambda}sigma_x,

    -kappa4(S)=sum_{x1,x2,x3,x4 in Lambda}K(x1,x2,x3,x4) <= N A = N g_+ chi^2 xi^3.

Take ell so sum_{|z|_infty<=ell}G(z)>=chi/2, R=max(1,ceil(xi),ell), Lambda=[-2R,2R]^3, N=(4R+1)^3. Every x in [-R,R]^3 has all y with |y-x|_infty<=R in Lambda. Consequently

    V=Var(S)=sum_{x,y in Lambda}G(y-x) >= (2R+1)^3 chi/2 >= N chi/16.

The last inequality uses (2R+1)^3/(4R+1)^3 >=1/8. Also N/xi^3>=64 because R>=xi. If B=-kappa4(S)/V^2, the first inequality gives

    g_+ >= B V^2/(N chi^2 xi^3) >= B N/(256 xi^3) >= B/4.

For the actual block Gibbs marginal, Lee-Yang and zero factorization give B>=12/r^4 with r=sqrt(V) times the first positive imaginary zero. Therefore g_+>=3/r^4. Finite-volume multivariate Lee-Yang applies with positive fields on all sites; set fields outside the block to zero by a positive limit and apply Hurwitz. A fixed block marginal of the infinite-volume free state inherits the nonvanishing property by local weak convergence and a second Hurwitz limit. The source's near-critical block is this actual joint Gibbs marginal, not an isolated box.

This proves only a conditional bridge. The single hardest open premise is a bounded r on a beta-to-beta_c subsequence for exactly those blocks. Lee-Yang location alone cannot do this: for N independent fair spins, r=pi sqrt(N)/2 diverges while B=2/N vanishes.

## Verdicts

Machine-readable rows are in REVIEW_VERDICTS.jsonl. W471 L1: KEEP. W471 L2: KEEP with all hypotheses and the unproved bound retained. W471 control: KEEP. W471 scope checkpoint: FIX to the operational source statement. W472 conditional L1: KEEP as a sketch, with no parent-problem claim. No claim in either packet solves C0052.

## Review boundary

The local intake's 2026-09-07 current-intersection and fractal-dimension discussion is a heuristic attempt with a missing variance estimate. I did not use its asserted equivalence as a theorem. A file/hash check is not a proof check. Neither a 2017 conjecture nor an unsuccessful bounded web search certifies 2026 openness.

## Adjacent triad's open ask: w470 weighted-current criterion

I directly audited w470's ATTEMPT.md after reading the team's oldest open ask. Exercise 61(1) supplies, for each quadruple under the assumed infinite-volume passage, K(0,x,y,z)=2G(x)G(z-y)p_beta(x,y,z). For B={y:|y|_infinity<=floor(xi)}, define the endpoint joint mass explicitly as P(X=x,Y=y,Z=z)=G(x)G(z-y)/(|B|chi^2). Then

    sum_{y in B,x,z} K(0,x,y,z)=2|B|chi^2 E[p_beta(X,Y,Z)].

All terms are nonnegative, so this partial sum is at most the full numerator -sum U4, yielding -g>=2|B|q/xi^3. As xi tends to infinity, |B|/xi^3 tends to 8. Thus a positive liminf of q is a sufficient condition for the source's coupling to be nonzero. The author's stated marginals and conditional law did not explicitly require X independent of (Y,Z); I issued FIX with the joint mass above. The finite-volume Exercise 61(1) formula is source-backed, but its infinite-volume passage remains a stated assumption in this packet, and the positive q bound is wholly unproved. The y=0 slice gives the exact control -sum_{x,z}U4(0,x,0,z)=2chi^2 and only -g>=2/xi^3, which vanishes in the scaling regime. Verdict: FIX the endpoint law, KEEP the conditional algebra, no parent solution.
