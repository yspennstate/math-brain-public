# Verification entry point

The earlier audit opened only the challenge statements. The release also provides a separate [comparison configuration](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/TraceReconstruction.json). It selects `ComparatorChallenges.TraceReconstruction` as challenge module and `OAI.Probability.TraceReconstruction` as solution module, and names the three quantitative and superpolynomial results. The permitted axioms are `propext`, `Quot.sound`, and `Classical.choice`; `enable_nanoda` is false. These are configuration settings, not observed checker results.

The [solution source](https://raw.githubusercontent.com/openai/math/main/lean/OAI/Probability/TraceReconstruction.lean) is accessible. It imports `OAI.Probability.TraceReconstruction.Induction` and `.Testing`. The quantitative theorem begins at source line 204, the one-trace theorem at line 318, and the sample-complexity theorem at line 362 (one-based numbering). They contain proof bodies. The quantitative proof calls the constructed final pair, error and restoration bounds, and a family-testing bound. Thus the challenge file's `sorry` bodies alone do not describe the separate solution.

The [release instructions](https://raw.githubusercontent.com/openai/math/main/lean/ComparatorChallenges/README.md) require comparator, landrun, and lean4export, followed by Lake setup. The task-specific invocation, inferred by substituting the actual configuration filename in the documented example, is:

```sh
lake env comparator ComparatorChallenges/TraceReconstruction.json
```

This command was not run. The dependency closure, accepted axioms of compiled theorems, and comparison outcome remain unchecked. Source availability and nonempty proof bodies establish neither kernel acceptance nor correctness. All URLs use the moving main branch; no immutable revision was established.
