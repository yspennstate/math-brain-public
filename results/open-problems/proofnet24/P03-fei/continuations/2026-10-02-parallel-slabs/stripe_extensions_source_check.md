# Primary sources and current-status checkpoint for the stripe/layer extensions

Inspected 2026-10-02 UTC (2026-10-03 in Jerusalem). This is a bounded prior-art check, not a proof of priority.

## Established inputs actually inspected

* Keller--Klein, *Biased Halfspaces, Noise Sensitivity, and Local Chernoff Inequalities*, Discrete Analysis 2019, Theorem 1.4: <https://arxiv.org/html/1710.07429v3>. The manuscript normalizes the input-weight L2 norm to one. Its maximal physical flip influence is comparable to p min(1,a_max sqrt(ln(1/p))). For weights w and remaining squared norm sigma², the normalized largest weight is w/sqrt(w²+sigma²). Complementation replaces output density by its minority value. These are the exact quantities used in the slab proof. The arXiv v3 date is September 25, 2019.
* Klivans--O'Donnell--Servedio, *Learning Intersections and Thresholds of Halfspaces*, Theorem 18: <https://www.cs.columbia.edu/~rocco/Public/focs02.pdf>. The full primary statement gives NS_epsilon(h)<=min(2p,20.5p sqrt(epsilon ln(1/p))) with p the minority density. Its bit-flip convention agrees with the tail conversion in the proof. A union bound over crossing halfspaces is used; no unsupported relative noise estimate for an entire interval is assumed.
* O'Donnell--Wright--Zhou, *The Fourier Entropy--Influence Conjecture for certain classes of Boolean functions* (ICALP 2011): <https://www.cs.cmu.edu/~odonnell/papers/fei.pdf>. Theorem 1 proves full symmetric Boolean FEI with constant 12.04 and includes arbitrary layer labels. Theorem 2 also proves d-part-symmetric FEI with constant 12.04+log2 d; that is prior work for block permutation symmetry, distinct from arbitrary nonsymmetric exceptional layers. The actual theorem statements and their Fourier conventions were inspected.
* Uniform-cube Bonami--Beckner hypercontractivity is a standard input, applying to signed real functions. The slab proof uses ||T_(1/sqrt2) B||_2<=||B||_(3/2), so stability at rho=1/2 is at most alpha^(4/3) when |B| is an indicator. It does not require B>=0.

The full all-LTF argument and its existing primary-source audits remain an inherited campaign result. The new slab proof explicitly adapts its concentration and dyadic-KL steps, rather than presenting the underlying halfspace inequalities as new.

## Recent full-conjecture status

Gonzalez--MacManus--Pereyra, *Further evidence towards the Fourier Entropy--Influence conjecture*, <https://arxiv.org/html/2606.00246v2>, still states the general FEI assertion as a conjecture and develops restricted classes using entropy-split induction. Its actual introduction and class statements were inspected.

Potapov, *On the Fourier Entropy--Influence Conjecture for Boolean Plateaued Functions*, <https://arxiv.org/html/2609.21563v1>, proves plateaued and partially bent subclasses. The abstract page <https://arxiv.org/abs/2609.21563> lists v1 submitted September 18, 2026 at09:52:28UTC. Its introduction and exact subclass theorem statements were inspected on October2UTC. Those classes do not establish a general FEI theorem and must be credited as prior subclass progress.

## Bounded search and attribution limits

Queries covered Fourier entropy with slabs, intervals of linear forms, parallel intervals, almost-symmetric/nonsymmetric Hamming layers, and degree-two polynomial thresholds. Search engines returned the established symmetric/function-composition/entropy-bound literature, including an old ECCC abstract that misleadingly retained an all-LTF claim. The actual revised ECCC manuscript was already inspected in the inherited LTF checkpoint and only supplies the weaker entropy bound. A search snippet is not proof of a valid theorem.

No earlier complete proof of these precise slab and maximum-run exceptional-layer statements was located in this bounded search. This does **not** establish originality, exhaustive current status, or historical priority. The general Boolean conjecture remains unproved in this campaign, as do arbitrary-weight finite crossings with unrestricted spacing. The new internal proofs require outside mathematical review before any public solution claim.
