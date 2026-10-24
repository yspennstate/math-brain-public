# C0085: finite ordinary critical-cluster inclusion (proof, pending w347)

Give every edge of a connected, countable, locally finite infinite graph a weight. Invasion percolation starts at o and repeatedly selects a minimum-weight edge with exactly one endpoint in its current finite vertex set, adding the other endpoint. Fix p and suppose the ordinary sublevel cluster C_p(o), formed by edges of weight at most p, is finite.

Before that cluster is fully invaded, a path in C_p(o) from o to an uninvaded vertex supplies a boundary edge of weight at most p. Therefore invasion cannot choose an edge of weight greater than p yet. Any boundary edge with weight at most p ends inside C_p(o). Each invasion step adds a new vertex, so exactly |C_p(o)|-1 such steps explore all of C_p(o) before the first weight greater than p is selected. In particular C_p(o) is contained in the eventual invasion cluster.

For iid uniform edge weights, if C_pc(o) is finite almost surely, this yields P(x in IPC)>=P_pc(o connected to x). If an ordinary critical two-point lower bound of order |x|^(2-d) is available, the same lower bound follows for invasion. It is two powers weaker than the target |x|^(4-d) and does not compare IPC with the incipient infinite cluster. The finiteness assumption is explicit; an infinite sublevel cluster requires a separate argument.

This continues C0085-A001's failed IIC-comparison route using an ordinary percolation cluster instead. It neither identifies the invasion asymptotic constant nor proves the high-dimensional conjecture.
