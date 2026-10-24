# Final paired proof supplement

w426 delivered its complete proof after the main audit had been saved. The additional verdicts are KEEP L3 and KEEP B2, within the exact scope in PAIRED_AUDIT_SUPPLEMENT.jsonl. The submitted four-card draft bundle is unchanged.

For L3, let alpha=P(o connects to A), beta=min_a P(a connects to b), and epsilon in (0,1). The already checked forest inequality is P(o connects to b)>=alpha*beta. Finite A ensures that strict lower bounds for every relay give beta>1-delta. Therefore delta_star=1-sqrt(1-epsilon) is sufficient, including equality of the chosen modulus: the strict premises give alpha*beta>(1-delta_star)^2=1-epsilon. If delta>delta_star, choose x between max(0,1-delta) and sqrt(1-epsilon) and use a two-edge path with both edge probabilities x. The premises hold but the conclusion fails. This proves optimality in the forest subfamily and a necessary upper bound on any general-graph modulus. It supplies no general-graph sufficiency. No assertion at epsilon=0 or epsilon=1 is needed.

For B2, inspect the graph with edges o-a1,a1-v,o-a2,a2-v,v-b. If a_star=a1, open exactly o-a2,a1-v,v-b and close the other two square edges. The origin reaches a2; a1 reaches b; the origin does not reach b. Interchanging the relay labels defeats the other fixed choice. At half weights each configuration has probability 1/32.

The half-weight square values previously computed independently in PAIR_MEASUREMENTS.json are terminal probability 7/16 and neighbor-to-target probability 9/16. Relabel that square's opposite target as v and append the independent half-open edge v-b. Multiplication by this single disjoint pendant edge gives 7/32 and 9/32. The relay-hit probability remains 3/4. Hence the legitimate product inequality has margin 7/32-(3/4)(9/32)=1/128. This is an unconditional independence calculation on disjoint edges, not multiplication of conditional relay probabilities.

Across the main audit and this supplement there are five scoped KEEP verdicts. None supplies a parent-problem proof, a formal-check receipt or a different-model identity receipt.

NEXT: w428 checks the complete paired and independent boundary packets, retaining the arbitrary cyclic-graph gluing gap.
