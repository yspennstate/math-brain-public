# Verification notes

The first local regression attempt intentionally included an assertion that the autonomous-chain lift count equals the full extension count. It failed on a generated structured case because the test harness passed the *pre-expansion* relation on `Q` into the corridor counter. Expanding a module forces additional `D<U` relations by transitivity, so the correct `Q=P\M` is the induced relation after taking the full transitive closure. I corrected only that harness defect, reran with site initialization disabled, and the final archived script/output passed. The mathematical lift theorem itself uses the induced `Q=P\M` throughout.

Final local execution hashes:

- `verify_autonomous_chain_binomial.py` SHA-256: `29c739af21f90a0e557e8d9798bf90474fb8068dfdc038d1c80969c121d61cb2`
- `verify_autonomous_chain_binomial.out` SHA-256: `54ee56dbe13aded7e771522b2648871cba5e715798bb4fd9d29970dc11104fda`

The exhaustive structured census is regression/adversarial evidence only. It is not used as arbitrary-size closure of POS3 or of the stated autonomous-chain dichotomy candidate.
