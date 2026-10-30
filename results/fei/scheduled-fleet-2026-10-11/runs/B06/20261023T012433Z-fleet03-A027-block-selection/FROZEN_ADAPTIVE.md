The four adaptive continuations are fixed before executing the pilot. All stop on a constant function or a failed control; all retain the full terminal spectrum. Data0,data1,selector2 are in that order.

0: query all three data coordinates, then all remaining controls only on selector outcome0.
1: data0, first control, data1, selector; then one further control only on selector outcome1.
2: data0,data1; query first control iff the current known restricted core has negative probability>1/8; then selector and stop.
3: data0,first control,data1; query second control if available; then selector; then remaining controls only on selector outcome0.

The restricted-core bias in mode2 is a statistic of the supplied Boolean function and revealed physical history; it does not observe an unknown input bit. All point-control permutations are equivalent, so controls are queried in their fixed original order. Fixed orders retain ALL shuffles for queried prefixes k=0..r. No policy/dimension expansion is authorized by passing the pilot.
