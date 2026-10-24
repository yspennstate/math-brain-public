# Correction to A021 stage 1: positive entropy remainder

The B05 lead's sign objection is correct. In the stage-1 run 20261011T214020Z-account05-A021-rare-core-asymptotics, REPORT.md Section 2, RARE_CORE_EXPANSIONS.tex, and claim A021-UNIFORM-RARE-CORE-EXPANSION v1 incorrectly set the logarithmic remainder negative. The corrected formula is

    -2(1-q)^2 log2(1-q)=2cq-3cq^2+R(q),
    R(q)=+4c sum_{j>=3}q^j/[j(j-1)(j-2)],
    0<R(q)<=2cq^3/[3(1-q)] for 0<q<1; c=1/ln2.

Thus H(F)=q[th+4k+2c]-q^2(2k+3c)+R(q), and CI(F)-H(F)=q[t(Ci-h)+(C-4)k-2c+q(2k+3c)]-R(q). The same algebraic slack expression holds, but the remainder lowers rather than raises slack. The stage-1 ratio interval must be replaced by its truncation as a lower bound and that truncation plus 2cq^2/[3(1-q)(ti+k)] as an upper bound. Exact spectra, entropy formulas, influence, core-ratio limits and control-first KL ledger are unchanged.

Stage-1 Section 3's decrement error also reverses: Delta_s=4u+(2s-4+3c)u^2+G_s with -8cu^3/[3(1-2u)]<=G_s<=0 for s>=2, rather than G_s>=0. The claimed fixed-seed upper bound 4+2c/k survives by direct b(q)<=2cq, whose proof is -(1-q)ln(1-q)<=q and multiplication by 2(1-q); it must not be justified by dropping a falsely negative remainder.

The finite prime-log checker never tested the series expansion and therefore did not detect the error. Its exact-spectrum and tree-identity assertions remain valid; a separate rational interval certificate is being added for the sign and bounds. Historical artifacts are preserved unchanged. Replacement v2 is recorded in this run, with B05 lead credited for the correction; that lead is a contributor to the repaired statement and cannot independently accept it.

Source-bound affected consumers: A023's REVIEW_A021.md must narrow its acceptance of the full remainder package; A087/A094/B20 must use v2 for every asymptotic sign or interval assertion. No correction is needed to the separately proved A021-CONTROL-FIRST-KL-LEDGER v1. No shared files or other agents' artifacts were modified.
