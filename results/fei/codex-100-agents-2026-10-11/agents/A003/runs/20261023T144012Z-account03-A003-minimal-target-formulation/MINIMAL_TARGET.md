# Final minimal target comparison

All information is in bits; c=2/ln2. Every assertion below quantifies over all finite uniform Boolean cubes unless a source/terminal class is explicitly specified. No local reset theorem supplies initial O(I) admission.

| Route | Paid implication | First unpaid all-dimensional line |
|---|---|---|
| C018 total erasure | B<=K I => a good coordinate => FEI(K+c); FEI(C)=>B<=C I | Prove an actual Boolean structural bound B<=lambda H+K I with lambda<1, giving FEI((K+c)/(1-lambda)) |
| Good coordinate, weak regime | If max Inf<tau admits B_i<=(lambda H/I+K)Inf_i, FEI constant is max(log2(e/tau)+c,(K+c)/(1-lambda)) | At tau=1/4, require Inf_i>=I/(2d) AND B_i<=4Inf_i on every weak-coordinate function; this fixed structural lemma implies FEI(4+c) |
| Signed Booleanity | L_i=sum_T p(T+i)log2(1+p(T)/p(T+i)); L_i<=B_i<=L_i+Inf_i/ln2; some L_i<=KInf_i =>FEI(K+3/ln2) | Obtain L_i<=4Inf_i from the full signed convolution constraints, not just an arbitrary probability law; implies FEI(4+3/ln2) |
| Whole-set witness | The full posterior-residual bound R*<=K I implies FEI(2+K_ref+K), K_ref=3+2log2(3)+log2(6e) | Pay the FIXED baseline witness residual with its original gate/selector/normalizer and complete reference costs; changing the admissible family changes the target |
| C019/C024 deferral | Exact matched zero-erasure queries cost zero entropy, preserving ORIGINAL K L I-H | Re-expressing capacity at CURRENT core influence is not free: endpoint residual is K I-H, exactly FEI(K) |

These constants and route interfaces are the established baseline, not new theorems this stage. There is no canonical least stronger lemma among inequivalent structural hypotheses. The fixed numerical coordinate/signed/witness targets are reviewable sufficient statements. A mere unspecified influence-priced full-reference supplier is FEI-equivalent, since CE>=H and Q=P realizes equality.

The complete checked previous theorem is DERIVATION.md, now independently accepted by A004 at unchanged scope. Its key distinction is: sum erasure + full terminal CE remains H(core), whereas an additional K-times-queried-influence earmark leaves K I(current)-H(core). Both accounts are valid when declared; they cannot be silently exchanged. Maj3 with L2,K1 retains original entropy surplus1 but has endpoint influence residual-1/2. This is a fixed-rate heredity obstruction, never a FEI disproof.

Next substantive target: supply a noncircular Boolean mechanism for one displayed coordinate/signed/witness inequality or a well-founded decreasing original-source construction. Stop treating optional exact-match resets, paid padding, or relabeling current influence as universal progress. Full FEI remains OPEN.
