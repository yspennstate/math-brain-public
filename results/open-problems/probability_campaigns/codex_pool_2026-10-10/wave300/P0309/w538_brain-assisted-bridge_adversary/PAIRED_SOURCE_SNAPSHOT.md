Audit source snapshot from ~\brain_workers\w537\ATTEMPT.md
SHA256: 501c6afcde0865b287f030b45737e8f2e9545997f27f312512828550ff7b0c57

# P0309: pressure and removal of a periodic field

Author: w537. Mathematical review pending with w539. Current openness UNKNOWN. Nothing here proves the full P0309 conjecture. The primary distinct bridge is C5 (circular full-law Bragg intensity to pressure slope), supported by C2's exact probability-cost threshold. After saving C1-C5, a narrow read found that w531 independently developed a pressure-cusp route. C1/C3 share elementary infrastructure with that route; they are not claimed as unique new territory. Our calculations were saved before reading w531's PRESSURE_ROUTE.md.

## Source target and chosen precise subtarget

The 2026-09-07 ranking names positive-temperature crystalline Gibbs phases for three-dimensional Riesz gases. Lewin, arXiv:2202.09240v2, Section VI.2, discusses the expected BCC/FCC low-temperature phases, with dimensionless coupling Upsilon=beta*rho^(s/3). It treats s>3 and neutralized s<3 separately. The ranking has no quantified exponent range or crystallinity definition. The positive-temperature discussion is not the zero-temperature energy Conjecture 35. A single nonzero Fourier mode proves translation breaking, but does not identify BCC/FCC or a full rank crystalline phase.

Chosen subtarget: for a fixed finite beta>0 and specified translation-invariant canonical periodic Riesz Hamiltonian H_N at density rho>0, remove the external potential -h*cos(G.x), after the thermodynamic limit, and obtain an unpinned Gibbs limit with nonzero G-Fourier response. G is a nonzero reciprocal vector of a fixed full rank period lattice Gamma. The finite tori are compatible with Gamma and N/volume=rho. Long-range normalization and the limiting equilibrium equation must be explicitly fixed; their validity is not inferred from these pressure lemmas.

## C1. Exact double-limit response from a pressure cusp

Let beta>0. For each positive integer N, let M_N be a measurable real random variable on a probability space (Omega_N,mu_N), with |M_N|<=N. Assume its law is symmetric: M_N and -M_N have the same distribution. Define, on (-h0,h0),

    p_N(h) = log E_mu_N[exp(beta*h*M_N)]/(beta*N),
    m_N(h) = E_mu_N,h[M_N]/N = p_N'(h),
    dmu_N,h/dmu_N = exp(beta*h*M_N)/E exp(beta*h*M_N).

Assume p_N(h) converges pointwise to p(h) for every |h|<h0. Then p is even, convex, 1-Lipschitz, p(0)=0. Its right derivative m=p'_+(0) exists and is in [0,1]. For 0<2h<h0,

    p(h)/h <= liminf_N m_N(h)
              <= limsup_N m_N(h)
              <= [p(2h)-p(h)]/h.                         (C1.1)

Consequently both lim_{h down to 0}liminf_N m_N(h) and lim_{h down to 0}limsup_N m_N(h) equal m. In contrast m_N(0)=0 for every finite N. Spontaneous response m>0 therefore requires a cusp at zero; a positive response at a fixed h>0 is insufficient.

Proof. Boundedness allows differentiation under the expectation; p_N'=E_h M_N/N and p_N''=beta*Var_h(M_N)/N>=0. Also |p_N'|<=1. Symmetry makes p_N even. These properties pass to the pointwise limit. The tangent/secant inequalities for a differentiable convex function give p_N(h)/h<=p_N'(h)<=[p_N(2h)-p_N(h)]/h. Pass to limits in N. Convexity and p(0)=0 give p(h)/h -> p'_+(0)=m. The upper secant equals 2*p(2h)/(2h)-p(h)/h -> m. This proves the double limits without assuming p is differentiable at positive h. Symmetry yields E_mu_N M_N=0.

## C2. The exact missing free-energy threshold

Under C1's assumptions, put A_N=M_N/N and m=p'_+(0).

(a) If 0<=a<m, then

    liminf_N N^(-1) log mu_N(A_N>=a) = 0.             (C2.1)

(b) If m<a<=1, there are h>0 and eta>0 such that

    limsup_N N^(-1) log mu_N(A_N>=a) <= -eta.        (C2.2)

(c) If for some a>0 the left side of C2.1 is zero, then m>=a.

Proof (a). For fixed h>0 small enough that p(h)>h*a,

    E exp(beta*h*N*A_N)
      <= exp(beta*h*N*a) + exp(beta*h*N)*mu_N(A_N>=a).

Thus the probability is at least exp(beta*N*(p_N(h)-h))*[1-exp(beta*N*(h*a-p_N(h)))]. The bracket tends to one. Its log divided by N tends to zero. Hence liminf N^(-1)log probability>=beta*(p(h)-h). Let h down to zero; the right side tends to zero, whereas a log probability is never positive. This proves (a). For (b), pick h with p(h)/h<a, use exponential Markov, and take eta=beta*(h*a-p(h))>0. For (c), restrict the exponential moment to A_N>=a. Passing to the limit gives p(h)>=h*a; then let h down to zero.

Interpretation. The usable bridge is subexponential accessibility of a nonzero Fourier response under the **unrestricted** zero-field law. An exponentially tiny defect-free basin is insufficient. This criterion already includes entropy and normalization rather than just a low energy bound. It neither assumes independence nor multiplies conditional probabilities.

## C3. Volume response becomes local only with explicit control

Let finite tori be tiled by K_N fundamental cells C+gamma of Gamma, with N=rho*K_N*|C|. Let mu_N,h be invariant under Gamma translations, with G reciprocal to Gamma, and M_N(X)=sum_{x in X}cos(G.x). Let h_k down to zero and N_k tend to infinity, with m_Nk(h_k)->m>0. Suppose their periodically lifted point-process laws converge locally weakly to P. Assume P puts no points on boundary C, and the local counts n_C are uniformly integrable along the sequence. Then

    E_P sum_{x in X cap C} cos(G.x) = rho*|C|*m >0. (C3.1)

In particular P is not invariant under all translations. If, in addition, the chosen zero-field Gibbs specification is closed under this sequence of local limits as h_k->0, P is an unpinned Gibbs law. Closure of a long-range Gibbs specification is a separate assumption here.

Proof. Gamma invariance and periodicity give E M_N=K_N E sum_{x in C}cos(G.x); divide by N. The local Fourier sum converges in distribution by local weak convergence and the zero boundary count assumption. Its absolute value is bounded by n_C, so uniform integrability passes its expectation to the limit. A fully translation-invariant locally finite-intensity point process has constant intensity measure. The integral of a nonzero reciprocal Fourier character over C is zero, contradicting C3.1. The final Gibbs conclusion uses precisely the separately stated closure assumption; this proof does not manufacture it.

Limit warning: C1 provides diagonal choices N_k,h_k with response approaching m, but provides neither local tightness nor uniform integrability nor long-range specification closure.

## C4. A crystalline conditional branch need not survive removal of the field

Fix beta,c>0 and 0<a<=1. Under mu_N let M_N/N be +a,-a,0 with respective probabilities 1/(2+exp(c*N)), 1/(2+exp(c*N)), exp(c*N)/(2+exp(c*N)). Conditional on the positive branch the Fourier response is exactly a. Nevertheless,

    p(h) = max(a*abs(h)-c/beta,0),
    p'_+(0)=0.

Proof. The normalized moment-generating function is [2*cosh(beta*h*a*N)+exp(c*N)]/[2+exp(c*N)]. Divide its logarithm by beta*N and compare the three exponential rates. The limit is max(a*abs(h),c/beta)-c/beta. It vanishes in an interval around zero. The ordered branches have probability exponentially small at rate c. Thus positive order within a selected branch and at sufficiently large pinning field does not imply spontaneous order. This is a finite probability counterexample to the inference, not a counterexample to Riesz crystallization.

## C5. Full-law Bragg intensity implies spontaneous field response

In addition to C1, suppose S_N is complex with |S_N|<=N, its law is invariant under S_N -> exp(i*theta)*S_N for every theta, and M_N=Re S_N. Assume liminf_N E|S_N/N|^2>=b^2 for some 0<b<=1. Then the pressure right slope satisfies p'_+(0)>=b.

Proof. Write B_N=S_N/N, R_N=|B_N|. Fix 0<a<r<b. For all sufficiently large N, E R_N^2>=(b^2+r^2)/2. Since R_N<=1,

    P(R_N>=r) >= (b^2-r^2)/[2*(1-r^2)].           (C5.1)

Average the circularly invariant law against a uniform auxiliary angle. Conditional on any B_N of modulus at least r, the fraction of angles giving Re(exp(i*theta)*B_N)>=a is at least acos(a/r)/pi. Hence

    P(Re B_N>=a) >= (b^2-r^2)*acos(a/r)
                    /[2*pi*(1-r^2)] >0.          (C5.2)

This bound is independent of N, so C2(c) gives p'_+(0)>=a. Let a increase to b (choosing an intervening r) to obtain the claim. Independence is used only for the optional auxiliary random angle representing a symmetry average, never for particles or conditional per-particle bounds.

For the unpinned canonical periodic Riesz law, global translations multiply S_N=sum_x exp(i*G.x) by any complex phase, because G is nonzero. Thus a full-law positive Bragg-intensity bound, pressure-limit existence, and C3's local-limit/Gibbs hypotheses are sufficient for a translation-breaking phase. The other triads' conditional or harmonic Bragg bounds cannot be inserted until their probability-law mismatch is closed. The theorem proves a phase response under its explicit hypotheses, not those missing Riesz hypotheses.

## Single hardest remaining gap

Prove for an actual unrestricted three-dimensional Riesz law at some fixed finite beta that a nonzero crystalline Fourier-response event has zero exponential probability cost, equivalently establish p'_+(0)>0 for the correctly normalized full pressure. C5 reduces this to a positive full-law Bragg-intensity bound if such a bound can be obtained. No bound here proves these Riesz inputs. Riesz local tightness/UI and renormalized Gibbs closure must also be supplied before turning the response into an equilibrium phase. BCC/FCC identification and full rank periodicity remain beyond this necessary subtarget.

NEXT: Compare the full convexity card with C1, then test whether a proposed Riesz crystalline branch has subexponential mass in the unrestricted zero-field partition function.
