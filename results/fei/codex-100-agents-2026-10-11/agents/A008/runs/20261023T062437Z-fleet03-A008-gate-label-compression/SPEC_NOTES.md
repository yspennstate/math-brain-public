# Frozen-spec reconciliation

SPEC_REPLAY.json mistakenly predicted four w=1 directed transition cases. The fixed expression (r clause choices)^2 times (number of gates)^2 is 2^2*2^2=16, not four. The unchanged w=1,2 domain executes16+65,536=65,552 transition cases. No domain expansion or automatic dimension increase occurred; out/replay.json records the actual count. Main frozen counts and domains agree with the executed receipts.

Pilot630 assertions overlap the full202,119 assertions and are not added. Independent replay contributes66,540 additional assertions, making268,659 nonpilot assertions. Neither exact finite run is an independent-agent acceptance of the new all-w theorem.
