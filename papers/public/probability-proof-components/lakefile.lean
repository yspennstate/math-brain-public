import Lake
open Lake DSL

package probabilityProofComponents where

require mathlib from git
  "https://github.com/leanprover-community/mathlib4.git" @
  "0df444a360eaa60ab8c11dca51a86af692955474"

lean_lib CayleyAlgebra
lean_lib EndpointCore

@[default_target]
lean_lib ProbabilityProofComponents
