# Probability proof components in Lean

**Yitzchak Shmalo**  
Einstein Institute of Mathematics, The Hebrew University of Jerusalem

Two collections of checked Lean components arising from research on probability open questions. These files formalize specific algebraic and measure-theoretic steps. **They do not formalize the complete stochastic theorems, certify novelty, or constitute complete solutions to the source open problems.**

| File | Checked declarations | Scope |
|---|---:|---|
| [CayleyAlgebra.lean](CayleyAlgebra.lean) | 8 | Exact reset-generator, spectral-sector and time-scale algebra for an unweighted Abelian Cayley construction |
| [EndpointCore.lean](EndpointCore.lean) | 9 | Dominated-convergence obstruction and coefficient/scaling algebra for a critical Allen-Cahn example |

## Build

Install [Lean through elan](https://github.com/leanprover/elan), then run:

```sh
git clone https://github.com/yspennstate/probability-proof-components.git
cd probability-proof-components
lake update
lake exe cache get
lake build
python scripts/check_sources.py
python scripts/check_axioms.py
```

The toolchain is Lean **4.33.1**, with mathlib pinned to commit `0df444a360eaa60ab8c11dca51a86af692955474`. A clean checkout may need a substantial dependency download. The GitHub Actions workflow builds both libraries from the pinned configuration.

To inspect the declarations and their transitive axiom reports directly:

```sh
lake env lean CayleyAlgebra.lean
lake env lean EndpointCore.lean
```

Each target declaration has a `#print axioms` command. The recorded successful component runs use only `propext`, `Classical.choice`, and `Quot.sound`; there are no `sorry` proofs or newly declared axioms in these files. These are standard Lean foundations, not hypotheses supplying the missing probability theory.

## What remains outside Lean

For the Cayley construction: the finite graph, the Markov semigroup, the conditional auxiliary-coordinate bound, character completeness, cube mixing limits and the final asymptotic cutoff conclusion. The file treats the comparison logarithm as an arbitrary real scalar.

For the critical stochastic example: Brownian motion, Ito's formula, the Bessel representation, hitting-time asymptotics, stochastic existence and the connection to the source SPDE assumptions. In particular, the dominated-convergence lemma assumes the convergence and strict expectation defect it uses.

Detailed correspondence guides: [Cayley](docs/CAYLEY_FORMALIZATION.md) and [critical endpoint](docs/ENDPOINT_FORMALIZATION.md).

## Verification evidence

[verification/component_runs.json](verification/component_runs.json) records exact source and compiler hashes, the mathlib revision, return codes and declaration counts from the successful original component runs. The compiler output is included alongside it. This is historical evidence for those exact source bytes. The Actions result is a separate fresh build of the repository; neither substitutes for semantic review of a manuscript.

## AI assistance

These files and their documentation were prepared and checked with assistance from OpenAI's Codex. AI assistance included mathematical argument development, Lean implementation and review. The author is responsible for the research. Compilation establishes the encoded statements only; mathematical scope and originality require separate review.
