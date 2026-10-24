# Frozen-spec errata

The executed function families, dimensions, arithmetic, helper code, resource limits, and predicates did not change during execution.

1. FROZEN_SPEC.json originally and still lists case_count=33034. This was an addition error: 2+8+128+32768=32906. Both outputs give actual counts. REPRODUCTION_SPEC.json supplies the correct count.
2. REPRODUCTION_SPEC.json originally described its acceptance predicate as `4 sum|products| <= (7/2) sum squares`, then `8 sum|products| <=7 sum squares`. That text had an extra factor two. The frozen checker code always executed the correct predicate `4*prod <=7*den`, equivalent to `A_i/I_i=2 prod/den <=7/2`. The specification text was corrected after launch to agree with its unchanged helper. This was a documentation correction, not a changed search predicate. The original text is preserved here for review.
3. The first persistence schema assertion compared the annotated protocol entry `packet_ids (one primary ID, for compatibility)` literally to the JSON key. It failed after saving the stage files. The checker now strips that explanatory annotation, because the user expressly requires `packet_ids: ["A026"]`. All other required field names are checked literally. The final save and schema check passed.
