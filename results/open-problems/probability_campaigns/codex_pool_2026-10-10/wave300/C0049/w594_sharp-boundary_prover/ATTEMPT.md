# C0049: the q=4 endpoint and a quantitative finite-graph bridge

Scope: an auxiliary result. C0049 remains unresolved in this packet. Current openness of the exact Dobrushin formulation is UNKNOWN. No novelty claim is made for the original problem or the already published endpoint equation.

The recovered intake row is C0049 in probability_1000_intake_claude_20260907/problems.jsonl, line 49. It points to Duminil-Copin's 2017 Ising/Potts lectures, Conjecture 3, page 93. Its formula is kappa=4*pi/(pi-arccos(sqrt(q)/2)). This equals 4*pi/arccos(-sqrt(q)/2). The exact cited 2017 source is being checked. The 2012 paper arXiv:1208.3787, Conjecture 2, states the same prediction.

An explicit working formulation is: fix q in (0,4] excluding 2, a bounded simply connected Jordan domain D, distinct marked boundary points a,b, and square-lattice Dobrushin approximations (D_delta,a_delta,b_delta) whose boundaries and marked points converge uniformly. At critical p_c(q), the interface separating the wired primal arc from the dual/free arc converges in law, in the uniform curve metric modulo increasing reparametrization, to chordal SLE(kappa(q)) from a to b. These domain and topology hypotheses make the brief precise; the historical abbreviated conjecture itself does not spell out all these quantifiers. For q<1, the equality p_c(q)=sqrt(q)/(1+sqrt(q)) is a separate status question, not an assumption silently promoted to a theorem.

Prior attempt C0049-A001 (2026-09-07) used the FK-Ising observable route. It noted missing full discrete analyticity, available crossing estimates for q>=1, and problems below one. Its assertion that the problem reduces *exactly* to finding one additional discrete equation is stronger than justified: a discrete analytic identity is one possible sufficient route; no necessity was proved. Endpoint q=4 additionally needs the winding-weighted replacement described below. Targeted H/I/Lean reads returned no C0049 attempt row. No proof was inferred from a source/hash receipt.

## Lemma 1: spin one is exactly a flow equation

On the consistently oriented square medial lattice, let gamma be any random oriented edge-simple path with fixed terminal edge e_b. Internal vertices may be visited twice; source and terminal vertices are excluded. Let d_e be the complex unit direction of oriented edge e, p_e=P(e in gamma), and W(e,e_b) its total signed turning. Since the initial and final directions determine turning modulo 2*pi,

    exp(i W(e,e_b)) = d_b/d_e,
    F_1(e) = (d_b/d_e) p_e.

At a vertex with incoming NW and SE edges and outgoing NE and SW edges, their oriented directions are exp(-i*pi/4), exp(3i*pi/4), exp(i*pi/4), exp(-3i*pi/4), respectively. Thus

    F_1(NW)-F_1(SE)-i*(F_1(NE)-F_1(SW))
      = d_b*exp(i*pi/4)*(p_NW+p_SE-p_NE-p_SW).

Every individual path has equal incoming and outgoing visit counts at this vertex. Taking expectations proves the equation. At the other vertex type all four oriented directions are reversed, multiplying the displayed expression by -1. The equation therefore holds there too. No probabilistic independence, criticality, FKG or random-cluster weight was used.

For actual FK at q=4 this holds at every p, a fact already explicit in Duminil-Copin 2012, Section 4.3. The short source phrase is "holds for every p". Attribution is retained; this is a rederived known fact.

## Counterexample to the equation-only identification bridge

In the directed medial lattice, a path taking alternating NE,SE steps has net displacement east. Scale its zigzags by delta=1/n between (-1,0) and (1,0), with n even, in the square (-1,1)^2. Every tested internal vertex obeys Lemma 1; terminal normalization F_1(e_b)=1 and |F_1(e)|<=1 hold. With x as the parameter the path stays within delta of the horizontal diameter, hence the Dirac path laws converge uniformly to that deterministic diameter. Chordal SLE(4) has driving function 2B_t and is not a Dirac curve law; a fixed simple trace determines a fixed capacity-parametrized driving function. This falsifies only the assertion that the ordinary spin-one vertex equation, these bounds and terminal normalization alone force SLE(4). This constructed path law is not asserted to be the critical FK law, or to satisfy all of its geometric assumptions.

## Lemma 2: a quantitative finite-graph endpoint passage

Fix one finite square-lattice Dobrushin graph G=(V,E), one boundary wiring, and one tested medial edge e. Let m=|E|, v=|V| and N=m+2v. Write I(omega)=1_{e in gamma(omega)} and set W=0 on I=0. Suppose |W|<=L on the finitely many configurations. For 0<h<=1/2 define

    c=cos(pi*h/2), q_h=4*c^2, p_h=2*c/(1+2*c),
    F_{h,s}=E_h[exp(i*s*W)*I],
    G_0=E_0[W*exp(i*W)*I],
    D_h=(F_{h,1-h}-F_{h,1})/(-i*h),

where E_h is the FK expectation at (p_h,q_h) and E_0 at (2/3,4). Then

    |D_h-G_0| <= h*L^2/2 + L*(exp(pi^2*N*h^2/4)-1).       (E)

Proof. At the self-dual p_h, cancel the common factor (1-p_h)^m from all unnormalized FK weights. A configuration with o open edges and k clusters after the fixed wiring has weight (2c)^o(4c^2)^k. Relative to h=0 its weight is c^r, r=o+2k, with 0<=r<=N. Therefore the Radon-Nikodym density R_h=c^r/E_0[c^r] lies in [c^N,c^(-N)]. For every bounded complex Y,

    |E_h[Y]-E_0[Y]| <= ||Y||_infinity*(c^(-N)-1).

For a real x, integral Taylor remainder gives |exp(-i*x)-1+i*x|<=x^2/2. Apply this with x=hW, multiply by exp(iW)I and divide by h:

    |D_h-E_h[W*exp(iW)*I]| <= (h/2)*E_h[W^2 I] <= h*L^2/2.

Use the preceding change-of-measure estimate with Y=W exp(iW)I. Finally put x=pi*h/2<=pi/4. Since sec(x)^2<=2 on this interval, tan(x)<=2x and -log cos(x)=integral_0^x tan(t)dt<=x^2. Hence c^(-N)<=exp(pi^2*N*h^2/4), proving (E). In particular D_h->G_0 on this fixed graph.

Each F_{h,1-h} satisfies the critical local parafermionic relation because sin((1-h)*pi/2)=sqrt(q_h)/2. Each F_{h,1} satisfies Lemma 1. Their difference quotient satisfies the same linear relation. Its finite-graph limit G_0 therefore does also. This recovers published Proposition 10 using an explicit error estimate instead of an unstated interchange of graph and spin limits. It uses no FKG bound and no multiplication of conditional probabilities.

## Lemma 3: the nonuniformity is real for general winding variables

Let W_n=2*pi*n deterministically, I_n=1 and h_n=1/(2n). With the same definition of a spin difference quotient under this fixed probability law,

    D_n=(exp(i*(1-h_n)*W_n)-exp(i*W_n))/(-i*h_n)=-4*i*n,
    G_n=W_n*exp(i*W_n)=2*pi*n,
    |D_n-G_n|/|G_n|=sqrt(1+4/pi^2)>1.

Although h_n->0 and q(h_n)->4, even relative first-order accuracy fails. This is an abstract winding-variable counterexample, not an FK configuration sequence or a contradiction to the fixed-graph theorem. It proves that small h alone is insufficient for a mesh-uniform Taylor argument; winding moments matter.

## The single hardest remaining gap

For the observable route at q=4, the missing step is convergence and uniform integrability of the correctly normalized winding-weighted G_delta in the evolving slit domains, strong enough to pass discrete martingales to the limiting interface. Lemma 2 alone only handles fixed finite G. A graph-independent statement requires actual normalized winding moment estimates and boundary/slit control; (E) does not provide them. The 6 October 2026 CLE(4) preprint gives a different height-function route for free-boundary loops; its exact Dobrushin consequences require a separate argument and are not claimed here.

NEXT: Run bounded endpoint controls after a fresh compute check, send the frozen proof and source packet to w596, and submit labeled concept drafts for review.
