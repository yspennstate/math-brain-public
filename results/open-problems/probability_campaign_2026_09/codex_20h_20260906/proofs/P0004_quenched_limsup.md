# P0004: what can be proved about the limsup

Status: author-checked elementary partial result. No novelty claim. The source's question about existence of a limit remains unsolved here.

Target source: Geoffrey Grimmett, *Selected problems in probability theory*, arXiv:2205.07318, Question 2.3, PDF pages 3-4. The target is the exponential growth limit of self-avoiding walks on the infinite supercritical bond-percolation cluster of the square lattice.

## Deterministic root-independence lemma

Let G be an infinite connected graph of maximum degree Delta < infinity. Let c_n(v) count n-step self-avoiding walks starting at v, with c_0(v)=1. Then the quantity

    M(v) = limsup as n tends to infinity of c_n(v)^(1/n)

does not depend on v.

Proof. First let v and w be adjacent. Partition the walks from v according to whether they visit w. A walk which avoids w becomes an (n+1)-step self-avoiding walk from w after prepending the edge wv. If a walk visits w, let k in {1,...,n} be its unique visiting time. Reverse its prefix from v to w and retain its suffix from w. These are respectively k-step and (n-k)-step self-avoiding walks from w. Forgetting their disjointness only enlarges the number of pairs. Thus

    c_n(v) <= c_(n+1)(w) + sum_(k=1)^n c_k(w)c_(n-k)(w).

An infinite connected locally finite graph contains a ray from every vertex, by the elementary finite-branching tree argument applied to finite self-avoiding walks. Hence 1 <= M(w) <= Delta. For every epsilon>0 there is a finite C>=1 such that c_m(w)<=C(M(w)+epsilon)^m for every m>=0, by the definition of limsup and enlarging C for the finitely many exceptions. The displayed inequality gives

    c_n(v) <= [C(M(w)+epsilon) + n C^2](M(w)+epsilon)^n.

Take nth roots and limsup, then let epsilon decrease to zero. This gives M(v)<=M(w). Interchanging the roots gives equality. A finite path connects any two roots. QED.

Independent check: apply the argument to a tree. The visiting decomposition still holds although the exact counts can vary dramatically by root at finite n; the polynomial factor disappears at the exponential scale. The proof never uses transitivity or stationarity and therefore cannot, by itself, prove convergence of c_n(v)^(1/n).

## Consequences in percolation and an annealed upper bound

Using uniqueness of the infinite cluster and translation ergodicity of independent supercritical bond percolation, the common limsup is translation-invariant and therefore deterministic. These two standard percolation theorems are dependencies, not proved here. This conclusion is already in the literature: Hubert Lacoin, *Non-coincidence of quenched and annealed connective constants on the supercritical planar percolation cluster*, arXiv:1203.6051.

There is also an elementary upper bound. For a fixed lattice root, let c_n^omega count open n-step self-avoiding walks, including environments where the root has a finite cluster. Every lattice self-avoiding walk uses n distinct edges, so

    E c_n^omega = p^n c_n^lattice.

Write mu for the lattice connective constant. For any epsilon>0, eventually c_n^lattice<=(mu+epsilon)^n. Markov's inequality yields

    P(c_n^omega >= [p(mu+2epsilon)]^n)
        <= ((mu+epsilon)/(mu+2epsilon))^n.

The right side is summable. Borel-Cantelli, followed by a countable epsilon sequence tending to zero, proves limsup(c_n^omega)^(1/n)<=p mu almost surely. It remains valid after conditioning the root to belong to the infinite cluster. Lacoin proves a strictly smaller bound in the planar supercritical regime p<1; that strict improvement is not derived here.

## Why the obvious subadditivity route stops

Cutting a walk at time m only gives

    c_(m+n)^omega(v) <= c_m^omega(v) max_(u reachable in m steps) c_n^omega(u).

The endpoint maximum depends on the same environment and is not c_n^omega(v), nor a single predetermined stationary translate. Fekete's lemma therefore does not apply to log c_n^omega(v). Kingman's theorem needs a specified stationary subadditive process; no such process has been constructed by this inequality. Replacing the maximum with a typical-root value would require a uniform estimate over the growing set of endpoints and cannot be justified by an almost-sure statement at each fixed root alone.

Exact obstruction: prove that the liminf has the same exponential rate as the deterministic limsup. Root-independence, annealed expectations, and subexponential prefactors in the displayed comparison do not resolve it.
