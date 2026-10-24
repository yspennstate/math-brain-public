# Additional serious attempt ? D0027 ? 2026-10-11

## Remaining gap read from ATTEMPT.md

The proved finite-window L2 criterion does not cover a deterministic single infection when q is small. What is missing is a uniform deterministic local-forgetting bound A exp(b R-c t), with R the nearest initial infection distance. The existing finite-set dual and BABP energy comparisons did not prove it.

## Two approaches not used in the previous attempt

1. **Search for a parity-sector Markov representation by a tensor change of basis.** BABP has a quasi-duality to a double-flip process with uniformly bounded logarithmic Sobolev constants. Instead of comparing FA-1f energies to BABP, conjugate FA-1f's three-site local generator by an arbitrary invertible real 2-by-2 matrix T, identically at every site. Require the conjugated local operator to be a Markov generator and look for a representation with parity sectors rather than an isolated absorbing state. First classify exactly when the transformed local operator has nonnegative off-diagonal entries and zero row sums. A positive result might supply a new process with stronger entropy tools; a negative result identifies a precise obstruction to this neighboring-model route. This is distinct from merely reproducing the previously known neighbor-refresh dual.

2. **Separate translation from expansion of the infection cluster.** The source proves ballistic diameter growth from finitely many infections. That does not by itself give bilateral invasion of the origin. Analyze the midpoint M=(X_plus+X_minus)/2 and width D=X_plus-X_minus; seek an exponential bound on midpoint excursions relative to width, which would imply bilateral expansion. The exact midpoint drift involves the difference of the two edge-adjacent infection indicators, so symmetry alone is insufficient. This may isolate a more geometric intermediate theorem than direct coupling. It would still need interior forgetting after invasion.

## Choice

Pursue approach 1. It has an exact finite algebraic core that can be exhaustively checked and may connect to the source's uniformly relaxing double-flip process. Do not assume similarity preserves probabilistic expectations, stationary densities, or logarithmic Sobolev constants. Even a valid transformed Markov generator must be accompanied by an explicit observable/initial-law transfer.

## Exact setup

Use the original spin basis 0=infected, 1=healthy, and column observables with row-generator matrices. Fix 0<q<1 and p=1-q. Put

    H = [[-p,p],[q,-q]],  N=diag(0,1),  I=identity_2.
    L_loc = I tensor H tensor I - N tensor H tensor N.

This is exactly the rate-one FA-1f update at the center of a three-site interval: the two neighbors suppress the update precisely when both are healthy. For an invertible real matrix T, write

    A=T^{-1}NT, B=T^{-1}HT,
    K=I tensor B tensor I - A tensor B tensor A.

Then K=(T^{-1})^{tensor 3} L_loc T^{tensor 3}. A Markov row generator means all off-diagonal entries are nonnegative and each row sums to zero. For a nonzero scalar c, replacing T by cT does not change K.

## Theorem F: complete classification of locally Markov tensor conjugacies

For 0<q<1, K is a Markov generator if and only if T, modulo a nonzero scalar, is one of

    T_identity = [[1,0],[0,1]],
    T_flip     = [[0,1],[1,0]],
    T_dual     = [[p,-p],[p,q]],
    T_dualflip = [[-p,p],[q,p]].                         (F1)

The first two yield FA-1f and its relabeling. The last two yield the neighbor-refresh finite-set dual and its relabeling. Thus this entire two-state homogeneous tensor ansatz with separately Markov local terms produces no new chain.

### Proof: reduce the row-sum condition

Let v=T*(1,1)^tr. It is nonzero because T is invertible. The condition K*1=0 is equivalent to L_loc v^{tensor 3}=0. At the outer pair (0,0) the constraint is legal and the corresponding two center entries equal v_0^2 H v. If v_0 is nonzero, this forces H v=0, so v is a nonzero constant vector. If v_0=0, v_1 is nonzero; in this case v^{tensor 3} is supported on the fully healthy triple, and is annihilated by L_loc. Scaling T, there are exactly two cases:

    Case C: T*1=(1,1)^tr;
    Case V: T*1=(0,1)^tr.

The scaling may be negative; it does not change the conjugate matrix.

### Proof: Case C

Write T=[[a,1-a],[b,1-b]], with a-b nonzero. Direct multiplication gives

    A = (1/(a-b)) * [[-b(1-a), -(1-a)(1-b)],
                      [a*b,       a(1-b)]].           (F2)

B has row sums zero and trace -1, because H does. Thus if u=B_01 and w=B_10, then u+w=1. At least one of u,w is strictly positive.

Choose that center transition s->1-s. The off-diagonal K-entry flipping all three spins, with both outer old spins 0, is -A_01^2 B_(s,1-s). Nonnegativity forces A_01=0. Using both outer old spins 1 similarly forces A_10=0. From (F2),

    (1-a)(1-b)=0 and a*b=0.

These equations and a-b nonzero give exactly (a,b)=(1,0) or (0,1): if a=1 then b=0; if b=1 then a=0. These are T_identity and T_flip. Both give Markov generators by direct relabeling. No sign assumption on T's entries was used.

### Proof: Case V

Write T=[[a,-a],[b,1-b]], with a nonzero. Direct multiplication gives

    A = [[b,1-b],[b,1-b]].

Set d=a-b, k=q-p*(1-b)/a, and h=q+p*b/a. Then

    B = [[d*k, -(1+d)*k],
         [d*h, -(1+d)*h]],  h-k=p/a.                 (F3)

First, b must lie in [0,1]. Indeed, for any fixed target outer pair (j,l) with distinct initial outer pair (i,k0), the corresponding off-diagonal entry is

    -w_j*w_l*B_st,  where w_0=b and w_1=1-b.

If b lies outside [0,1], w_0*w_1<0 while w_0^2>0 and w_1^2>0. For each of the four entries B_st we may choose an initial outer pair different from any prescribed target pair. Nonnegativity for both positive and negative products forces B_st=0. This contradicts trace(B)=-1. Thus b is in [0,1].

For a center-changing transition s->1-s, with outer pair changed, a target outer pair with w_j*w_l>0 exists, so B_(s,1-s)<=0. For a center-changing transition with outer pair fixed, its entry is B_(s,1-s)*(1-w_i*w_k0). There is an outer pair with w_i*w_k0<1 (also at b=0 or b=1). Hence B_(s,1-s)>=0. Thus

    B_01=B_10=0.

By (F3), (1+d)*k=0 and d*h=0. Since h-k=p/a is nonzero, the two solutions are as follows. If d is neither 0 nor -1, both k and h would vanish, a contradiction. If d=0, a=b and k=0, so b=a=p. If d=-1, a=b-1 and h=0, so b=q and a=-p. These are precisely T_dual and T_dualflip.

For T_dual, A has both rows (p,q) and B=diag(0,-1). Consequently K is zero when the center state is 0, and when the center state is 1 it refreshes its two outer neighbors independently to Bernoulli occupation q at rate one. This is a genuine Markov generator. T_dualflip has both A rows (q,p) and B=diag(-1,0), yielding the spin-relabeling of the same process. This proves necessity and sufficiency in every case. QED.

### Referee limitation of Theorem F

Theorem F assumes each conjugated local term is separately a Markov generator. A sum of terms could conceivably be Markov even when some local terms have negative off-diagonal entries. It would be incorrect to apply this classification to all global conjugacies without checking cancellation. The next theorem excludes parity-sector representations even after such cancellation is allowed.

## Theorem G: global no-go for a parity-preserving Markov tensor conjugacy

Let n>=5 and L_n be FA-1f on the cycle of length n, with no frozen boundary sites, 0<q<1. There is no real invertible 2-by-2 matrix T for which

    G_n=(T^{-1})^{tensor n} L_n T^{tensor n}

is both a Markov generator and parity-preserving (i.e. every positive-rate transition changes an even number of spins). Here no assumption is made on the signs or row sums of its individual local summands.

### Proof: harmonic product functions

The fully healthy state is absorbing. The set of states with at least one infection is a single irreducible closed class: add infections along adjacent sites until the whole cycle is infected; the resulting legal path can be reversed, since a spin flip's constraint is independent of that spin and both p,q are strictly positive. A last infection cannot heal, so this class is closed. The finite maximum principle implies every L_n-harmonic function is constant on each of the two classes. To see the maximum-principle step explicitly, at a state maximizing a harmonic function on the nonempty class, the sum of nonpositive rate-weighted differences is zero. Every positive-rate neighbor therefore has the same value. Irreducibility propagates that value throughout the class.

For a nonzero vector y=(y_0,y_1), the product function y^{tensor n} is harmonic if and only if y is either a nonzero constant vector or a nonzero multiple of (0,1). Proof: if both coordinates are nonzero, compare its values y_0*y_1^(n-1) and y_0^2*y_1^(n-2) at states with one and two infections; equality forces y_0=y_1. If y_1=0 but y_0 is nonzero, the all-infected state has nonzero value while a one-infection state has zero value in the same class, impossible. If y_0=0, the product is zero on the nonempty class and constant on the singleton healthy class, so is harmonic.

Let 1=(1,1)^tr and chi=(1,-1)^tr. A Markov G_n annihilates 1^{tensor n}. A parity-preserving G_n also annihilates chi^{tensor n}. Therefore v=T1 and z=Tchi are two linearly independent nonzero vectors whose product powers are L_n-harmonic. By the classification above, one must be constant and the other a multiple of (0,1).

### Proof: exclude a constant v

Normalize v=(1,1). Then T is as in Case C of Theorem F. For G_n, the transition flipping all three sites in one consecutive triple receives a contribution from just that triple's center term. Indeed, each local term acts only on its center and the two neighbors, and for n>=5 no other centered triple contains all three sites of the given triple. Its rate is therefore -A_(i,1-i)*B_(s,1-s)*A_(k0,1-k0), exactly as in the local computation. Since B_01+B_10=1, global Markov positivity forces A_01=A_10=0. The Case C algebra then forces T to be the identity or spin flip. But Tchi is then (1,-1) or (-1,1), whose product power is not harmonic for L_n. This is a contradiction.

### Proof: exclude a healthy-indicator v

Normalize v=(0,1). Since z must be a nonzero constant vector, write z=(r,r), r nonzero. Solving the two column-sum/difference equations gives

    T=[[r/2,-r/2],[(1+r)/2,(1-r)/2]].

This is Case V with a=r/2, b=a+1/2 and d=-1/2. Formula (F3) gives

    B_01=-1/2+p/(4a),
    B_10=-1/2-p/(4a),
    B_01+B_10=-1.                                    (G1)

Here A has rows (b,1-b), and at least one of A_01=1-b and A_10=b is nonzero. A triple-spin flip changes parity, so parity preservation of the global Markov generator forces every such off-diagonal entry to be zero. Choose equal outer old spins so the two outer factors give the square of that nonzero entry of A. Uniqueness of the triple contribution then forces both B_01 and B_10 to be zero. This contradicts (G1). QED.

## Consequence and remaining gap

The hoped-for two-state tensor conjugation to a double-flip-like parity chain is impossible. This is a proved obstruction to a specific new method, not a counterexample to D0027. It does not exclude block transformations, a larger local state space, non-tensor duality kernels, signed dualities with separately controlled cancellations, or geometric invasion/coupling arguments. The uniform deterministic local-forgetting estimate remains unproved.

## Theorem H: even site-dependent tensor factors cannot give parity conservation

Theorem G remains true with an arbitrary invertible real matrix T_i at every site of the cycle. In fact no such conjugated matrix can simultaneously have zero row sums and zero off-diagonal entries between opposite-parity configurations; nonnegativity is not needed for this stronger assertion.

Proof. First extend the harmonic-product classification. For nonzero vectors y_i, the product function F(eta)=product_i y_i(eta_i) is not identically zero. If harmonic, it is constant, say c, on the nonempty-infection class. If c is nonzero, evaluate F at the all-infected state: every y_i(0) is nonzero. Evaluate at the state obtained by changing only site i to healthy (which remains in the nonempty class, since n>=2). It gives y_i(1)=y_i(0), for every i. If c=0, the only state where F can be nonzero is the fully healthy one. Consequently every y_i(1) is nonzero; evaluating F at a configuration with its sole infection at i forces y_i(0)=0 for every i. Thus a harmonic product has either all its factors constant, or all its factors healthy indicators.

For S=tensor_i T_i, zero row sums of G=S^{-1}L_n S imply that the product with factors v_i=T_i*1 is harmonic. Vanishing odd-parity transitions, together with zero row sums, implies G chi^{tensor n}=0, so the product with factors z_i=T_i*chi is also harmonic. Each pair (v_i,z_i) is linearly independent. Therefore all v_i are of one harmonic-product type and all z_i of the other type. Scale the T_i individually; scaling factors only multiply S by an overall scalar and do not affect G.

If v_i=(1,1), then z_i=(0,r_i), with r_i nonzero, and

    T_i=[[1/2,1/2],[(1+r_i)/2,(1-r_i)/2]].

Its conjugated constraint A_i has off-diagonal entries

    (A_i)_01=(1-r_i)/(2*r_i),
    (A_i)_10=-(1+r_i)/(2*r_i),

whose sum is -1. At least one is nonzero. Also B_i has row sums zero and trace -1, so (B_i)_01+(B_i)_10=1.

If v_i=(0,1), then z_i=(r_i,r_i), with r_i nonzero, and

    T_i=[[r_i/2,-r_i/2],[(1+r_i)/2,(1-r_i)/2]].

A_i has identical rows ((1+r_i)/2,(1-r_i)/2), so at least one off-diagonal entry is nonzero. Formula (G1) gives (B_i)_01+(B_i)_10=-1.

In either case, for a fixed center i, choose independently the two outer old spins so their off-diagonal A_(i-1) and A_(i+1) entries are nonzero. The transition flipping exactly those three sites has the unique coefficient

    -(A_(i-1))_(s,1-s) * (B_i)_(t,1-t)
                           * (A_(i+1))_(u,1-u).

It must vanish for each center old spin t, because it changes parity. The two nonzero outer factors force both off-diagonal B_i entries to vanish, contradicting their sum being 1 or -1. Uniqueness of the triple's local contribution uses n>=5, exactly as in Theorem G. QED.

For a Markov generator, the apparently weaker condition G chi=0 already forces all odd-parity transition rates to vanish: at any state, each odd-parity transition contributes the same signed factor -2 chi(state) times a nonnegative rate, and these rates must sum to zero. Hence Theorem H excludes a Markov representation with parity as a harmonic function as well as one explicitly defined by even-spin flips.

## Positive control: BABP does admit the targeted representation

This obstruction is specific to FA-1f's three-site product term. For BABP, the constraint is the number of infected neighbors. Write its generator as the sum over edges of

    L_edge = (I-N) tensor H + H tensor (I-N).

Each endpoint is refreshed at rate one when the other is infected; summing edges produces the BABP rate 0,1,2 according to the number of infected neighbors. Use the healthy-indicator transform

    T_r=[[r/2,-r/2],[(1+r)/2,(1-r)/2]],
    r=sqrt(p) in (0,1).

The transformed edge operator is

    E=(I-A) tensor B + B tensor (I-A).

With A's identical rows ((1+r)/2,(1-r)/2) and B's rows both constant within a row, B_0j=(-1+p/r)/2 and B_1j=(-1-p/r)/2. A direct entry computation shows the only possibly nonzero single-spin-flip entries are plus or minus (p-r^2)/(2r). They vanish when r^2=p. The remaining off-diagonal rates, in order 00,01,10,11, are exactly

    00 -> 11: (1-r)^2/2,
    11 -> 00: (1+r)^2/2,
    01 <-> 10: (1-r^2)/2=q/2.                         (H1)

All are strictly positive; diagonal entries are minus the row sums. Thus E is an honest parity-preserving double-flip Markov generator. This verifies the intended neighboring-model mechanism within the same conventions. Relabeling the two spins and rescaling time recovers the source's DFP parameterization. The FA-1f constraint contributes the unique triple-flip term absent from this edge decomposition, which is precisely what the no-go proof detects.

More precisely, with lambda=q/p and y=sqrt(1+lambda)=1/r, exchange the transformed labels 0 and 1 and multiply E by 1/p. The rates become (y+1)^2/2 for 00->11, (y-1)^2/2 for 11->00 and lambda/2 for exchange, exactly the source's displayed DFP rates. This is a check of conventions, not a transfer of the FA-1f conclusion.

## Corollary I: transpose duality does not evade the result with product stationarity

A standard duality writes L_n S=S Q^tr, rather than conjugating L_n directly to a row generator. One must not silently confuse these conventions. Nonetheless Theorem H excludes a parity-preserving row-Markov target Q with an everywhere positive product stationary law h, whenever S is a tensor product of invertible two-state factors.

Proof. Regard h as a positive column vector, so Q^tr h=0. Write h(eta)=product_i h_i(eta_i) with h_i(0),h_i(1)>0, and set D=diag(h)=tensor_i diag(h_i). Define R=D^{-1}Q^tr D. Its off-diagonal entries are R_(eta,zeta)=Q_(zeta,eta)*h(zeta)/h(eta)>=0, and R*1=D^{-1}Q^tr h=0. It preserves parity because Q does. From L_n S=S Q^tr,

    R=(S D)^{-1} L_n (S D).

But S D is again a product of invertible two-state factors, contradicting Theorem H. QED. The assumption of a product stationary law is essential to keep S D tensorial. This corollary therefore addresses precisely an invertible tensor duality to a DFP-like process with product equilibrium; it does not rule out general signed, non-invertible, or non-product duality kernels.

## Hostile-referee audit for the additional attempt

1. All four local transformations have been derived for arbitrary real entries of T, not only stochastic T. Normalization is by a nonzero scalar and does not alter conjugacy.
2. The local classification alone was not applied to global generators: Theorems G and H explicitly use a global harmonic-function argument and unique triple transitions, permitting cancellation of other local rates.
3. The finite cycle has n>=5. Smaller cycles are not asserted; wrapping can invalidate uniqueness of the centered triple.
4. The product-harmonic classification uses the two exact closed communicating classes of FA-1f and a finite maximum-principle proof, with q,p strictly positive. Endpoint q=0 or q=1 is excluded from these algebraic theorems.
5. Markov positivity and parity-harmonicity are distinguished from signed cancellation: a signed transformed matrix may annihilate parity while containing odd transitions. Exact full-cycle tests check this explicitly and locate negative entries.
6. Similarity and transpose-duality conventions are stated separately. Corollary I requires positive product stationarity and proves the needed diagonal change rather than assuming it.
7. The BABP positive control succeeds under precisely the same state and generator conventions, and matches the source's parameters after explicit relabeling/time rescaling.
8. The rational grid checks are finite consistency checks, not a proof that all real transformations were searched. The universal classifications are established by the written algebraic proofs.
9. These no-go results do not prove slow relaxation or give a counterexample to D0027. They rule out a specific neighboring-process mechanism. The original uniform deterministic local-forgetting estimate remains the exact unresolved step.

## A natural non-tensor escape: domain walls fail to be Markov by themselves

The bond variables d_i=eta_i XOR eta_(i+1) have even parity on a cycle, and a single spin flip changes exactly two adjacent bonds. This superficially resembles a double-flip process and is not excluded by Theorem H, since the transformation is non-tensor and non-invertible. However, the domain-wall projection alone is not a Markov lumping of FA-1f for 0<q<1.

Proof. The fully healthy and fully infected configurations have the same domain walls, d=0. The healthy configuration is absorbing. From the infected configuration every site flips to healthy at rate p>0, making two adjacent walls. For the domain-wall observable F(d)=1_{d is not identically zero},

    L_n(F composed with d)(all healthy)=0,
    L_n(F composed with d)(all infected)=n*p>0.

If a time-homogeneous Markov projection on d existed for every initial configuration, these infinitesimal expectations would be the same at two configurations in the same fiber. They are not. This directly proves failure of the generator criterion for Markov lumpability. QED.

Adding one reference spin makes the bond representation bijective on the even-wall subspace, but then a distant spin's value is reconstructed by the reference spin and the intervening wall string. The local facilitation constraint is consequently not a function of the nearby walls alone. Thus this representation does not supply the local, uniformly relaxing DFP needed by the chosen approach. It is an additional checked failure of an explicit construction, not a proof that all non-tensor representations fail.

## Theorem K: the homogeneous global Markov classification also closes

For every cycle n>=5, a homogeneous real invertible tensor conjugacy G_n=(T^{-1})^{tensor n} L_n T^{tensor n} is a Markov generator if and only if T, modulo scalar, is one of the four matrices in (F1). No separate local-Markov assumption is needed. Thus cancellation cannot produce an additional homogeneous two-state Markov process, whether parity-preserving or not.

Proof. Zero row sums imply that (T1)^{tensor n} is L_n-harmonic. The harmonic-product classification in Theorem G reduces T, modulo scalar, to Case C or Case V. In Case C, positivity of the unique triple-spin-flip rates and B_01+B_10=1 forces A_01=A_10=0, exactly as in Theorem G; hence T is identity or spin flip.

In Case V, A has identical rows w=(b,1-b). Two sites at distance two have a unique common neighbor on a cycle n>=5. A transition flipping exactly these two outer sites and leaving the common center unchanged therefore has the unique rate -w_j*w_l*B_ss. A transition additionally flipping the center has the unique rate -w_j*w_l*B_(s,1-s). By varying the old outer spins, the products include b^2, (1-b)^2, and b(1-b). If b lies outside [0,1], positive and negative products force all four entries of B to vanish, contradicting trace(B)=-1. Hence b is in [0,1]. The positive squared products also imply that every entry of B is nonpositive.

The endpoints are impossible. If b=1, then A_01=0. A single flip at a center in state 0 with a neighbor in state 1 receives no contribution from neighboring center terms (they would contain A_01), and its own term gives rate B_01. Positivity gives B_01>=0, so B_01=0. But (F3), with b=1, gives B_01=-a*q, which cannot vanish since a and q are nonzero. If b=0, the corresponding single flip of a center in state 1 with a neighbor in state 0 gives B_10>=0, whereas all entries are nonpositive. Thus B_10=0; (F3) gives B_10=a*q, again impossible. Therefore 0<b<1.

The second harmonic function for G_n is (T^{-1}1)^{tensor n}. Direct inversion gives

    T^{-1}1=((1+d)/a,d/a)^tr,  d=a-b.                (K1)

If d=0, this is a nonzero multiple of the indicator of the uniform 0 configuration. That uniform state is an extremum of a harmonic function, so all its exits must have zero rate. Its unique triple-flip rate is -(1-b)^2*B_01, hence B_01=0. Also B_10=0 automatically from d=0. The Case V algebra of Theorem F forces a=b=p. If d=-1, use the indicator of uniform 1 and its triple-flip rate -b^2*B_10; both off-diagonal B entries again vanish, giving a=-p,b=q.

Now assume d is neither 0 nor -1. Rescale the product function from (K1) to g(eta)=rho^{k(eta)}, where rho=d/(1+d) and k(eta) is the number of spins in state 1. Notice rho cannot be 0 or 1.

If rho>0, the uniform 0 and uniform 1 states are the unique extrema of g. All their exits must have zero rate; the two unique triple-flip rates force B_01=B_10=0.

If -1<rho<0, g's unique maximum is the uniform 0 state, and its minima are exactly the states with one spin in state 1. The uniform-0 triple flip forces B_01=0. From a singleton 1 at the triple's center, the triple flip makes two 1 spins and changes the value from rho (the minimum) to rho^2>0. This exit must have zero rate; its unique coefficient is -(1-b)^2*B_10, forcing B_10=0.

If rho<-1, the uniform 1 state is an extremum, and the opposite extremum is attained exactly at states with n-1 spins in state 1. Which is the maximum depends on the parity of n; this distinction does not affect the argument. The uniform-1 triple flip forces B_10=0. Put the unique 0 of an n-1 configuration at the center of a triple. Flipping that center and its two outer 1 spins changes k from n-1 to n-2, hence leaves that extremal level. Its unique rate -b^2*B_01 must vanish, giving B_01=0.

If rho=-1, g is parity; the Markov harmonicity argument in Theorem H forces every odd-flip rate to vanish, so the same triple rates force both off-diagonal B entries to vanish.

In all cases with d not in {0,-1}, we have B_01=B_10=0, contradicting the root classification in Theorem F. The maximum-principle use here does not require G_n to be irreducible: for any finite Markov generator and harmonic function, a state at a global extremum cannot have a positive-rate transition to a different value. This follows directly from the sum of same-sign differences in its generator equation. Thus no transient-state or local-cancellation assumption is hidden in this step. The only surviving Case V matrices are the dual and dual flip, already proved Markov. This completes the proof. QED.

Theorem K is homogeneous. Arbitrary site-dependent factors have only the parity no-go result of Theorem H here; no claim of a full inhomogeneous non-parity classification is made.

## Supplement: an exact reduction for the geometric alternative

The tensor approach has reached a proved obstruction. The unchosen geometric approach can also be reduced to a precise missing additive-functional bound, without assuming it follows from symmetry.

Start with finitely many infections, at least one. Let L_t and R_t be the leftmost and rightmost infected sites, D_t=R_t-L_t, and M_t=(R_t+L_t)/2. If D_t>0, define a_minus(t)=1_{eta_(L_t+1)=0} and a_plus(t)=1_{eta_(R_t-1)=0}. When D_t=0, set both indicators to zero. The last infection cannot heal, so these variables remain defined at every finite time.

### Lemma L: midpoint drift and concentration of its compensated part

The outward jump rates of R and L are q each. The inward rates are p*a_plus and p*a_minus, respectively. Every inward jump is exactly one site: an edge infection can heal only if the site immediately behind it is infected. This remains true at D=1, where either of the two adjacent infections can heal; at D=0 there are no inward jumps.

Thus the predictable midpoint drift is

    b_t=(p/2)*(a_minus(t)-a_plus(t)),
    B_t=integral_0^t b_s ds,
    W_t=M_t-M_0-B_t.                                  (L1)

W is a martingale with jumps of absolute size 1/2. Its jump intensity is at most 2q+2p=2, and its predictable quadratic variation is at most t/2. These statements follow directly by compensating the four boundary event counts; at D=1 the two healing events have different sites, and at D=0 the two birth events likewise have different sites, so there is no duplicate event counting.

For every epsilon>0 and t>=0,

    P(|W_t|>=epsilon*t)
       <= 2 exp[-(1/2)*min(epsilon^2,epsilon)*t].       (L2)

Proof of the tail bound. For theta in (0,1], the exponential compensator for the bounded-jump martingale has integrand sum_j lambda_j*(exp(theta*delta_j)-1-theta*delta_j), where |delta_j|=1/2 and sum_j lambda_j<=2. Taylor's integral remainder gives exp(u)-1-u<=u^2*exp(|u|)/2. Thus the integrand is at most theta^2*exp(theta/2)/4<=theta^2/2. The same bound holds with theta replaced by -theta. The compensated exponential is a nonnegative local martingale and hence a supermartingale. Since its compensator is bounded by the deterministic quantity theta^2*t/2, this yields E exp(plus or minus theta*W_t)<=exp(theta^2*t/2). All constructions may first be stopped when the boundary event count exceeds a level; this count is dominated by a rate-2 Poisson process, so no explosion or integrability issue occurs. Fatou's lemma removes stopping.

Exponential Markov inequality now gives each one-sided tail at most exp[-theta*epsilon*t+theta^2*t/2]. For epsilon<=1 choose theta=epsilon, and for epsilon>=1 choose theta=1. The exponents are at most -epsilon^2*t/2 and -epsilon*t/2, respectively. Add the two tails. This proves (L2). QED.

### Conditional bilateral-invasion reduction

For the single-infection start at the origin, M_0=0. Suppose there exists v>0 and positive constants C,c such that, for all large t,

    P(D_t<v*t)<=C exp(-c*t),
    P(|B_t|>v*t/8)<=C exp(-c*t).                      (L3)

Then P(R_t<v*t/4 or L_t>-v*t/4) is exponentially small. Indeed, outside the two exceptional events in (L3) and the event |W_t|>v*t/8, (L1) implies |M_t|<=v*t/4. Since D_t>=v*t, R_t=M_t+D_t/2>=v*t/4 and L_t=M_t-D_t/2<=-v*t/4. Apply (L2) with epsilon=v/8 and a union bound. This proves the conditional reduction in full.

Neither estimate in (L3) is newly claimed here. In particular, the source's almost-sure eventual linear diameter bound is not silently upgraded to a uniform exponential tail at each t. Even granting such a diameter-tail estimate, the drift imbalance B_t still needs its own concentration theorem. Reflection symmetry of the single-infection law gives E B_t=0, because reflection exchanges the two indicators, but a mean-zero variable may have fluctuations of order t. The elementary deterministic bound |B_t|<=p*t/2 is too large when the available expansion speed v is small. Finally, bilateral invasion alone would still need an interior-forgetting argument to prove D0027. Thus this alternative isolates additional exact gaps rather than closing the original one.

## Verification completed so far

- tensor_symbolic.py verifies the two-by-two conjugated constraint and heat-bath matrices, their traces/projection identities, zero row sums of the conjugated three-site operator, and the four classified cases in symbolic rational functions. The tensor product conjugacy follows from multiplication of tensor factors; exact concrete matrices are independently checked in tensor_checks.py. Output: tensor_symbolic.json.
- tensor_checks.py passed 792 exact rational local candidates (including negative and non-stochastic transformations). Exactly the four classified cases were Markov for each of q=1/5,1/2,4/5. These checks do not replace the all-real algebraic proof.
- The same script formed the full generator on a five-cycle for 24 parity-harmonic candidates. Every full generator had zero row sums and annihilated parity, yet had negative off-diagonal entries; explicit witnesses are in tensor_checks.json. This directly checks the cancellation issue that a local test alone would miss.
- The uniqueness of consecutive centered triples was checked for cycles of size 5 through 9.
- babp_control.py passed the exact BABP positive control at r=1/2,2/3,3/4; the entire four-by-four edge matrices and rates are in babp_positive_control.json.
- TensorObstruction.lean checks the generic square/sign obstruction, the two algebraic root alternatives, the parity off-diagonal sum, and a rational parity instance. Its completion is still pending at this save point. The full probabilistic or full matrix classification theorem is not claimed to be Lean formalized.

The site-dependent check in inhomogeneous_checks.py passed in 18 exact cases, including both harmonic branches. Two cases also verify the full 32-by-32 identity L*S=S*G by rational arithmetic, independently of the local tensor argument. Results are in inhomogeneous_checks.json. The new homogeneous global classification is being checked over the same rational grid on the full five-cycle.

The global homogeneous grid respected a 120-second job budget and stopped after 225 cases (127.460 seconds elapsed including scheduling delays). All completed cases passed. The entire 792-case global grid was **not** completed, and no exhaustive global-grid certificate is claimed. This is a consistency check of Theorem K; its proof is the all-parameter argument above.

The midpoint formulas were checked by exact generator enumeration on all 127 nonempty infection subsets of [-3,3], at q=1/5,1/2,4/5 (381 cases). The enumeration includes births at sites just outside the initial window, checks D=0 and D=1, and verifies the midpoint drift, width drift 2q-p*(a_minus+a_plus), jump-size bound, intensity bound, and predictable variance rate <=1/2. All passed; see midpoint_checks.py and midpoint_checks.json. This finite check does not prove the unassumed long-time drift-concentration estimate.

## Final verification and verdict

From ~/lean_verify ran `lake env lean ~/brain_workers/TRIO_1011/op/D0027/TensorObstruction.lean`, with a 3600-second timeout. It passed with exit code 0, elapsed 2317.851 seconds including shared-machine waiting. The file imports only Mathlib.Data.Real.Basic, Mathlib.Tactic.Linarith and Mathlib.Tactic.Ring. Its five auxiliary theorems are kernel checked; the rational instance uses decide +kernel. There is no sorry and no native_decide. Output: tensor_lean_check.txt. This is a check of the finite algebraic core, not a Lean formalization of the full classifications or stochastic martingale theorem.

Exact checks passed: 792 local tensor candidates; 24 parity-harmonic full five-cycle candidates; 18 site-dependent candidates with two full matrix similarities; three BABP positive controls; and 381 midpoint-generator cases. The global homogeneous grid passed 225 cases before its job budget and remains explicitly non-exhaustive. The all-parameter statements rely on the complete written proofs.

Verdict: PARTIAL. This additional attempt supplies a complete homogeneous tensor-Markov representation classification, a site-dependent parity no-go theorem and transpose-duality corollary, a checked failure of domain-wall lumping, and a compensated-midpoint concentration bound. No proof or counterexample to Conjecture 2 was found. The original uniform deterministic local-forgetting estimate remains unproved. For the geometric alternative, control of the edge-imbalance compensator and quantitative bilateral invasion/interior forgetting remain missing. Two new approaches were recorded and the more promising tensor route was pursued to its explicit obstruction; no claim of bibliographic novelty is made.
