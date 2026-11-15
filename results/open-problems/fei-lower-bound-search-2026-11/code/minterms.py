"""minterms.py - print the minimal points of the up-set (the terms of the monotone DNF) of a hex truth table.
usage: python minterms.py n HEX [HEX ...]   (hex as written by mono_search: high index first)"""
import sys
n = int(sys.argv[1])
N = 1 << n
for h in sys.argv[2:]:
    tab = int(h, 16)
    U = [x for x in range(N) if (tab >> x) & 1]
    S = set(U)
    mins = [x for x in U if all(not ((x >> i) & 1) or (x ^ (1 << i)) not in S for i in range(n))]
    terms = sorted(("".join(str(i) for i in range(n) if (x >> i) & 1) for x in mins), key=lambda s: (len(s), s))
    # maximal points of the complement = clauses of the CNF (complemented)
    C = [x for x in range(N) if x not in S]
    maxs = [x for x in C if all(((x >> i) & 1) or (x | (1 << i)) in S for i in range(n))]
    clauses = sorted(("".join(str(i) for i in range(n) if not (x >> i) & 1) for x in maxs), key=lambda s: (len(s), s))
    print("n=%d |U|=%d terms(%d): %s" % (n, len(U), len(terms), " ".join(terms)))
    print("   clauses(%d): %s" % (len(clauses), " ".join(clauses)))
