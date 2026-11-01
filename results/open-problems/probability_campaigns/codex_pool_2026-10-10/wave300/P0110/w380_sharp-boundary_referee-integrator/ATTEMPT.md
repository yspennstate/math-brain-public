# P0110 attempt and boundary audit

The exact historical task is existential: find one iid nearest-neighbor FPP passage-time law for which the fluctuation and wandering exponents are established and obey $\chi=2\xi-1$. The source survey's Question 22 does not require $\chi=1/3$ or $\xi=2/3$. The conditional relation in Chatterjee (2013) is already proved, but its exponent-existence assumptions are the missing part for a concrete law.

I tested two proposed auxiliary shortcuts. The sharp forced-straight lemma of w378 proves a finite-scale equality $T_n=\sum_{i=1}^n\tau_i$ whenever $n(b-a)<2a$ for support $[a,b]$. This gives variance $n\sigma^2$ and zero transversal displacement. Taking the support width dependent on $n$ refutes any strict variance contraction with a law-independent onset. It does not determine an asymptotic exponent for a fixed law.

The w379 detour construction proves that monotone axial passage cost exceeds unrestricted cost by a positive linear amount almost surely for every nonconstant iid finite nonnegative law. The strongest step is the disjoint-block strong-law argument, which I rederived in REVIEW_PACKET.md. Thus a raw $o(n)$ transfer of passage times to a coordinatewise monotone axial model is false. A transfer after separate deterministic centering, or in interior directions, is not addressed.

No independence is inferred from per-row conditional estimates: the only iid events used here are on explicitly disjoint sets of edge weights. This boundary work leaves P0110 unsolved. NEXT: inspect a proposed fixed-law exponent route, or prove a law-dependent centered transfer with its error at the claimed scale.
