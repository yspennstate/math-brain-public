# Frozen-spec seed-label correction

FROZEN_SPEC_V2.json's numerical Maj3 seed label 5951 was a transcription
error. The same frozen field explicitly defines the seed as Maj3 on the
first three signs with a fourth dummy. The implementation generates that
table from this definition and obtains mask 5911, recorded in the actual
output. The second seed 1343 is correct. No catalogue orbit was seeded by
5951; no domain, constant, dimension or generation algorithm was changed.
The original frozen specification is preserved. The two dyadic compositions
listed in V2 are executed by the completed reproduction helper.
