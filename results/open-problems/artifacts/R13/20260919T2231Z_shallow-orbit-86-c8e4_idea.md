# R13 idea checkpoint — quotient the shallow-refinement forest before optimizing weights

Methods for this run: **#3 PROVE SOMETHING STRONGER, #14 FIND THE GROUP ACTING, #21 ASK WHO ELSE HAS THIS SHAPE.**

The previous 86-column obstruction varied shallow tie-breaking in an 11-cylinder refinement forest and improved the lower endpoint, but it did not identify the finite search space modulo the natural rooted-binary-tree symmetries. The new route is to quotient that search exactly before doing any further coefficient work.

For a shallowest-first refinement ending with k leaves, write d=floor(log2 k) and r=k-2^d. After the complete depth-d tree is built, the topology is determined by which r depth-d leaves are split once more, modulo the automorphism group of the complete rooted binary tree of depth d. For the retained leaf-count vector

(11,11,6,5,11,5,5,5,5,11,11),

there are five k=11 bases, one k=6 base and five k=5 bases. The exact finite targets are therefore:

- k=11: classify 3-subsets of the 8 depth-3 leaves under Aut(T_3);
- k=6: classify 2-subsets of the 4 depth-2 leaves under Aut(T_2);
- k=5: classify 1-subsets of the 4 depth-2 leaves under Aut(T_2);
- multiply the local orbit counts to obtain the exact number of global shallow topology classes.

Only after that quotient is certified will I test whether a canonical representative admits a stronger exact rational load certificate. The intended acceptance conditions are independent of floating-point scouting: projective cylinders pairwise incompatible, Kraft mass exactly one, every row normalized exactly, and every column squared norm strictly below one by Fraction arithmetic.

This is deliberately a topology/group-action route rather than another blind optimization of the 86 existing weights. The general Boolean-formula / unsatisfiable-matrix mechanism is prior art (Kunisky); no novelty claim is attached to that mechanism.