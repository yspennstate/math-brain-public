# T067-PIECEWISE-D0-001 v3: PASS

Exact proof SHA256: `ce54815cc311ba9722152637ee2a8898a53d5f468ffe665429c5625f46ec9ebb`.
Kind: audit; target: T067 target4b (dependency scope).

Every line from Part A through the full v2 amendment is byte-identical after removal of the appended v3 clarification. I inspected the full diff: the header version, dependency naming and appended scope paragraph are the only changes. The only RESCALE import in D4 is identity R, valid for the required parameters. D3 imports F2 with right branch support p_i >= (1-eta_ref)/3 because lambda <=16013/200000 <2887/5000. It never uses the invalid arbitrary-eta F1 corollary. My exact-v2 audit and independently completed 86 Gaussian endpoint/87 Bernstein leaf computations therefore apply unchanged; their mathematical body and frozen inputs are explicitly bound, not assumed inherited from metadata.

I read every changed line and verified the unchanged body against the prior exact-version audit. The source F1 parameter statement was read directly again. No numerical or mathematical claim is inferred from an author review-status assertion. Complete diff: checks/T067-PIECEWISE-D0-001_v2_v3_own.diff.

PASS for this exact corrected version. Another required distinct-account exact-content audit remains necessary before admission. No novelty assertion. The historical v1 RESCALE FIX remains on disk.
