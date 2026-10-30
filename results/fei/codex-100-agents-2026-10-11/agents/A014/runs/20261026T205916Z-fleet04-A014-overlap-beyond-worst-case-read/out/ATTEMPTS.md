# Preserved validation failure

The first local pilot exited 1 at assertion 49 (local_check.py line 35),
the enclosing upper comparison CE<=259I/32. This was an inconclusive interval,
not a counterexample: the reused evaluator rounded every logarithm to a
fixed 2^-40 grid. On the rare r=12,m=144 function, the upper rounding error
on log(1/(1-v)) exceeded the entire influence. The repair retains at least
40 relative bits near argument one by a proved finer dyadic grid. The
atanh enclosure and all exact reference/Boolean formulas are unchanged.
No failed comparison is reported as a successful mathematical certificate.
