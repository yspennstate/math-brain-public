# C0126: oriented bonds do not force a directed random walk

Status: route refutation and deterministic reduction, pending w347. Kumagai's cached Saint-Flour notes, Section 6.3, lines 3801-3869, need a zigzag estimate summing m^((4-d)/2) and leave d=5,6 open. Reference [18] is Barlow, Jarai, Kumagai and Slade, *Random walk on the incipient infinite cluster for oriented percolation in high dimensions*, Communications in Mathematical Physics 278 (2008), 385-431. No later answer was verified from the supplied caches.

The simple random walk in the spectral-dimension question traverses the underlying open cluster as an undirected graph. Oriented percolation defines which bonds and connections form the cluster; it does not prohibit backward steps of this walk. If it were forward-only, time would strictly increase and every positive-time return probability to the origin would be zero, incompatible with the heat-kernel question.

An explicit boundary check is the oriented diamond 0 -> a,b -> c. The underlying graph has two length-two paths in parallel. Ordinary simple random walk returns from 0 to 0 at two steps with probability 1/2: each of its two first-step choices contributes (1/2)(1/2). A forward-only walk has return probability zero. Therefore the previous argument that backward zigzags disappear by orientation changes the process and cannot justify a resistance or spectral-dimension estimate.

A legitimate deterministic reduction uses cutsets. In a unit-conductance network from an origin to a target boundary, suppose there are m distinct singleton edge cuts separating them. Every unit flow has net current of magnitude one through each of those edges. Its energy is at least m. Taking the infimum of energy gives effective resistance at least m (Thomson's principle). More generally disjoint cutsets C_j give the Nash-Williams bound sum_j 1/|C_j| by Cauchy-Schwarz on the currents in each cutset.

The missing random step is quantitative: on the d=5,6 IIC one would need the appropriate distribution/tail estimates for such bottlenecks or cutsets together with volume and heat-kernel assumptions. The deterministic inequality does not supply those estimates. As a finite independent check, exact grounded-Laplacian solves on m=1,2,3,4 diamonds each followed by a bridge gave resistances 2m with m separating singleton bridge cuts. The bare diamond has resistance one.

Audit the walk convention, return probability, current conservation across cuts, edge-disjointness and the gap between a deterministic inequality and random IIC tail bounds. No d=5,6 exponent is proved.
