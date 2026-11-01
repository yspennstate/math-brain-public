# P0150: uniform-vertex graph obstruction (proof of a generic route failure, pending w347)

Let K_m be a star with m vertices. Attach a pendant path with k_m=floor(sqrt(m)) new vertices to its center. Give all m+k_m vertices uniform mass and rescale graph distance by a_m=m^(-1/4).

For any fixed r independent samples, the probability that at least one sample is in the path is at most r k_m/(m+k_m), which tends to zero. If all samples belong to the star, every distance is at most 2a_m, which tends to zero. Thus all finite sampled distance matrices converge in probability to the zero matrix: the spaces converge Gromov-weakly to a point.

Their rescaled diameters equal a_m(k_m+1) for m>=2 and tend to infinity. The Gromov-Hausdorff distance to a point is half the diameter, so they fail even GH tightness. The uniform measure has full support in every finite graph. This is a graph version of P0150-A001's thin-mass obstruction, without an atom-plus-continuous measure. It is not a configuration-model counterexample and does not meet the heavy-tailed critical degree hypotheses.

Useful sufficient input. For compact metric probability spaces, suppose every radius-epsilon/2 ball has mass at least b_half>0 and every radius-epsilon ball has mass at least b_full>0. A maximal epsilon-separated set has at most 1/b_half points, using the disjoint radius-epsilon/2 balls. Each covering radius-epsilon ball is missed by N iid samples with probability at most (1-b_full)^N. A union bound gives failure probability at most (1/b_half)(1-b_full)^N for a 2epsilon-dense sample. Random lower-mass bounds require tightness of their reciprocals. The open task is to prove this input under the requested degree assumptions, not to infer it from weak convergence alone.
