# Correction to `BT4-SIX-DUAL-WALL-LIFT-v1`

This addendum preserves the immutable original report and corrects one directional typo in its setup.

The sentence in **Inherited exact-six dual-wall state** describing the residual support edge of the exact-six witness `z in B` should read:

> Because `B` is chordless, `d^+(z)=7`, `|N^+(z) intersect (A union C)|=6`, and `N^+(z) intersect R=empty`, the unique outgoing edge of `z` in `D-(A union C)` is its support-successor edge `z -> z^+`. Put `p=z^-`, so `p->z` is the incoming support edge used by the predecessor-exit argument.

The original sentence conflated these two directed support edges. No proof step uses the mistaken direction: every later use of `p` treats it as the predecessor `z^-` with arc `p->z`, and the dual-wall theorem itself uses only the incoming companion ladders, the predecessor rays from `p`, acyclicity of `R`, and 3-vertex-strongness of `D-{p,z}`. The theorem statement and proof are otherwise unchanged.
