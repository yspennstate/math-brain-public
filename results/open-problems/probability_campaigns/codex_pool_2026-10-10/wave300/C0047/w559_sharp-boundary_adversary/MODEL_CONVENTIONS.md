C_2 multiplicity boundary — source and model receipt

The independent ATTEMPT.md fixes a simple undirected Cayley graph: the order-two generator contributes one a-edge per vertex. Its critical equation is 2p^2+2p^3-2p^4=1 and p_c=0.6372776105... .

Kozakova, Critical Percolation of Free Product of Groups, arXiv:math/0611668v3, section 1.1, defines Cayley edges with the quote "with the appropriate multiplicity". Section 5 reports the modular-group polynomial 2p^5-6p^4+2p^3+4p^2-1 and threshold 0.5199... . These numbers must not be imported into the simple-graph packet.

Model interpretation (an inference from the stated cyclic-factor model and polynomial): replace every a-edge by two independent parallel bonds, each open with probability p. The probability that the pair connects its endpoints is r=1-(1-p)^2=2p-p^2. The same triangle exploration has mean r*2(p+p^2-p^3)=4p^2+2p^3-6p^4+2p^5, exactly the polynomial in that source. This is a different Bernoulli bond model on a multigraph. Merging the parallel pair while preserving its original parameter p changes the threshold. Merging it with effective parameter r preserves connectivity but makes the simple graph anisotropic.

Fresh gated check: all 128 local configurations agree with that polynomial; threshold display 0.519949076628999857100079608579018017285621637660275717346325; exact rational bracket 0.51<p_c<0.53. Runtime 0.010378s. This supplements the simple-graph derivation and does not revise it.

Primary source: https://arxiv.org/html/math/0611668v3 . Source interpretation and both infinite-graph statements require w560 review; no numerical discrepancy is called a refutation of the paper.
