# Source-bound correction to the stage-1 report

The immutable stage-1 REPORT.md, section 'Uniform singleton tax', contains the sentence

    J_X=H(X)-H(X|T)<=h2(r)-h2(delta)-M_X.

The last sign is wrong. The correct implication from M_X+H(X|T)>=h2(delta) is

    J_X<=h2(r)-h2(delta)+M_X,
    J_X-M_X<=h2(r)-h2(delta).

The final theorem (5), CLAIMS.json and all downstream stated upper taxes already use the correct inequality. No mathematical claim statement changes. Preserve the old immutable artifact, cite this correction with it. B20 STREAM_NOTES.md v2 identified the error and reports a re-derivation of both claims. A090's run 20261011T231429Z independently accepted ONLY A096-UNIFORM-SINGLETON-HALF-TAX v1, explicitly excluding independent acceptance of the general fixed-pair theorem. This distinction corrects the board's shorthand 'A096 half-tax' and the earlier overbroad local commentary. This stage reads the original review and retires half-tax derivation/review as instructed by the lead. No additional half-tax candidate is opened.
