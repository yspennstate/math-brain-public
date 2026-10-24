# Non-normal orbit quotients that are not normal quotients

Yitzchak Shmalo, Einstein Institute of Mathematics, The Hebrew University of Jerusalem.

Paper: [paper/main.pdf](paper/main.pdf) (source [paper/main.tex](paper/main.tex)).

Grimmett and Li (*Self-avoiding walks and connective constants*, arXiv:1704.05884, Question 4.5) asked whether a
non-normal subgroup A of a transitive group of automorphisms of an infinite transitive graph G can have a transitive
orbit quotient G_A that is not isomorphic to G_N for any normal subgroup N of any transitive group of automorphisms,
and whether a free action of A matters.

The paper shows that for every m >= 3 there is an infinite, connected, locally finite Cayley graph X whose automorphism
group acts regularly, with a non-normal subgroup B acting freely, such that X_B is the complete graph K_m while no
normal quotient of X is K_m. The graph is a graphical regular representation (Leemann and de la Salle) of F * F,
where F = S_3 for m = 3 and F = A_m for m >= 4, chosen to contain the edges of both factors; B is the preimage of a
point stabiliser under the projection onto the first factor.

The quotient X_B is finite. The version of the question with an infinite quotient, and Question 4.6 of the same paper,
are not addressed.

## Code

`code/check.py` (Python 3, standard library) checks the finite-group facts used in the proof for S_3 and A_4, ..., A_7:
the point stabiliser has index m, is nontrivial and is not normal, and no normal subgroup of F other than F has index
dividing m. It also checks the count of reduced words and the degree bound. Output: `code/check_output.txt`.

    python code/check.py

The proofs do not depend on the code.
