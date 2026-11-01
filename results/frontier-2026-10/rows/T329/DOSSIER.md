# T329 The optimal memorization capacity of ReLU networks with bounded bit complexity

Lead: unassigned. Dossier written 2026-10-16 by agent A from the row and the arXiv records below (abstracts read 16 Oct
08:1x, the 16 Oct 04:33 audit (status PARTLY) and worker L's note that the bounded-bit trade-offs are already Theorems 6.1/6.2).

## STATEMENT
Repaired statement (the audit: the sqrt(n) baseline hides an additive d and logs in norm, separation and classes, and the precision role is already studied in 2110.03187; the counting bound alone forces only W = Omega(n / log n)): with d, r/delta and C fixed and the architecture counted in the bit budget, the minimal number of parameters W(n, B)
that memorizes every allowed n-point dataset with B-bit weights; in particular whether W = O(n/log n) suffices at B = O(log n).

## FRONTIER
- Vardi, Yehudai, Shamir arXiv:2110.03187: O~(sqrt n) parameters with O~(sqrt n)-bit weights; depth L <= sqrt n with O~(n/L)
  parameters; VC dimension O(W B + W log W) (Theorem 6.1); a precision-depth tradeoff (Theorem 6.2).
- Counting: binary labels on n points need log2(number of realizable functions) >= n, and W parameters of B bits plus an
  architecture description give at most 2^(W B + O(W log W)) functions, so W >= c n / (B + log W); at B = O(log n) this is
  Omega(n / log n).
- Open: whether the O~ in the upper bound hides log factors that survive at B = O(log n).

## ARCHITECTURE
Read Theorem 6.2 at depth L ~ B: if bits per weight scale like L up to logs, then B = O(log n) allows L ~ log n and O~(n / log n)
parameters, matching the counting bound up to the hidden logarithms. The question is entirely in those logarithms.

## FAILURE POINT
The construction's bit-extraction layers cost an extra log factor per stored bit (encoding several labels in one weight and
extracting them needs depth and width proportional to the bits extracted).

## SHAPE
Days: specialize Theorem 6.2 to B = c log n with explicit logs (the audit's calculation).

## OBSTRUCTION
Bit-extraction overhead. Moves: count the exact parameters of the extraction gadget; try a gadget extracting b bits with O(b / log b)
parameters (the standard counting-optimal bit extraction).

## TARGETS
1. Theorem 6.2 at B = c log n with every logarithm explicit; compare with Omega(n / log n).
