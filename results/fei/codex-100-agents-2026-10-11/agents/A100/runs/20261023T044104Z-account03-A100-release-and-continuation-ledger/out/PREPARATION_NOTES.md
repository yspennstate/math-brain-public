# Preparation corrections

The first inline finalizer writer failed before execution on nested string quoting; no mathematical result changed. The saved finalizer then correctly detected that the prior receipt set included the mutable STATUS snapshot, which this stage had advanced. Prior-stage original-byte comparison now checks only files INSIDE the prior immutable run, explicitly excluding current rolling snapshots. Rolling snapshots are separately hash-recorded in the new manifest. No source or previous run was modified.
