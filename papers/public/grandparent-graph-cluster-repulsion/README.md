# Finite touching sets between percolation clusters on grandparent graphs

Yitzchak Shmalo

A transitive graph exhibits cluster repulsion at p if, almost surely, any two distinct clusters of Bernoulli bond
percolation with parameter p are joined by only finitely many edges. Timar proved this for every unimodular
quasi-transitive graph, and the nonunimodular case is open (Bell, Chu, Rodgers, Terlov and Tserunyan, Question 1.1).
The paper proves cluster repulsion at every p in [0, 1] for the grandparent graphs GP_b, b >= 2, the standard
transitive nonunimodular examples, whose infinite clusters are light for 1/b < p < 1. The proof shows that every
two-point function p -> P_p(u <-> v) is continuous on (0, 1): each descendant cone is integrated out through the exact
equation t = 1 - (1 - p)(1 - pt)^b for its reliability, and the effect of the missing ancestors is bounded uniformly
in p. The sprinkling argument of Haggstrom, Peres and Schonmann then gives the theorem.

## Contents

- `paper/main.tex`, `paper/main.pdf`: the paper.
- `code/check_proof.py`: exact enumeration in rational arithmetic of the cone recursion, the replacement of attached
  cones by single edges, and the edge-boundary lemma, for b = 2, 3, 4; writes `data/proof_checks.json`.
- `code/simulate.py`: percolation on finite binary descendant cones of depths 10, 12 and 14, counting edges between
  distinct large components; writes `data/simulation_summary.csv`, `data/cluster_pairs.csv`,
  `data/contacts_by_level.csv`, `data/anchored_levels.csv`, `data/anchored_pairs.csv` and
  `data/simulation_metadata.json`.
- `code/audit_data.py`: recomputes the depth-10 simulations by breadth-first search and checks them against the saved
  files; writes `data/data_audit.json`.
- `SHA256SUMS`: checksums of the files above.

Python 3, standard library only. The scripts lower their own priority with `os.nice`, and `simulate.py` uses the Unix
`resource` module, so run them on Linux or macOS from the repository root, for example `python code/check_proof.py`.
Each takes a few seconds. The computations are not part of the proof: a finite window can split one cluster of GP_b
into several components.

## License

MIT, see `LICENSE`.
