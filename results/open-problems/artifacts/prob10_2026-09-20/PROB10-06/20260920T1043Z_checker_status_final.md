# PROB10-06 final checker-status pointer

This note supersedes the checker pointer in `20260920T1034Z_checker_status_correction.md` without deleting any artifact.

The authoritative certificate for the theorem statements in this run is **v2**:

- `20260920T1042Z_quantitative_lower_branch_ratio_rigorous_check_v2.cpp`
- `20260920T1042Z_quantitative_lower_branch_ratio_rigorous_check_v2.out`

Reason for v2: it expands every stated rational/decimal rectangle endpoint outward by one adjacent IEEE-754 number and compares against proof thresholds rounded strictly downward. Hence the interval domains contain the exact intended rectangles. The earlier C++ checker is a correct preliminary calculation at nearest-double endpoints, but v2 is the one cited for exact theorem scope.

The Python `Fraction` draft/transcript at `20260920T1022Z_*` remains non-authoritative because its local re-execution exceeded the tool execution window. No theorem relies on that transcript.