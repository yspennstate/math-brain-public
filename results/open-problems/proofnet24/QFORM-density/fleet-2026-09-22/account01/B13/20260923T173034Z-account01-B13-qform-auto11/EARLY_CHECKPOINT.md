# account01/B13 early checkpoint

Programme: `QFORM-DENSITY-3EIG-20260922`.

Run: `20260923T173034Z-account01-B13-qform-auto11`.

Status: supporting derivation in progress; full QFORM remains OPEN; continuity remains separate.

Current mechanism: apply the latest completed account02/B13 four-anchor/rank-two-core report in its exact `Delta=0` branch, where `A=D+R` with `D` diagonal and `rank R<=2`. For the genuine rank-two case write `R=U Lambda U^T`, `U^T U=I_2`. After a genuine original-coordinate scalar pivot `z`, derive an exact volume-sampling identity for the Schur residual: if `a=A_zz`, `d=D_zz`, `c=||u_z||^2`, then after whitening `U_{-z}` the residual rank-two coefficient has determinant `(1-c)d det(Lambda)/a`. A random original-coordinate bipartition captures a fraction `delta_z/16` of its complete pair exterior energy, where `delta_z` is the probability that two independent rank-two volume-sampled physical pairs are disjoint. Combining with the completed unconditional pair-volume half-Riesz theorem should give a new leverage-free density certificate and classify the exact `delta_z=0` endpoint as a star or triangle support graph.

No rotation of random variables, perturbative deletion, interval extremality, bounded-diameter assumption, or pointwise scalar Fresnel decay is used.
