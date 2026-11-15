rows = [
("T327","KEEP","asks standard parameterization from small random init with the plateaus; Nichani-Damian-Lee prove a simplified model only"),
("T329","KEEP","explicit: the logarithmic gaps posed by Vardi-Yehudai-Shamir; narrow but well posed"),
("T331","REPLACE_OR_RESTATE","the two extensions the row asks for (sparse Erdos-Renyi, attention aggregation) are in Adam-Day-Benedikt-Ceylan-Finkelshtein, arXiv 2403.03880 (abstract read: sparse and dense ER, SBM, Barabasi-Albert; mean and attention); what may be left is max aggregation - read the paper for the exact sparse regime before editing"),
("T335","RESTATE","'identify natural operator classes' is a programme, not a statement; restate to one class with matching sample-complexity bounds, and check whether Lanthaler-Stuart's own Hamilton-Jacobi result already covers the example named"),
("T342","REPLACE_OR_RESTATE","the threshold at which random features fit degree-k content (N of order d^k) is Ghorbani-Mei-Misiakiewicz-Montanari, arXiv 1904.12191, with the joint N-n trade-off in Mei-Misiakiewicz-Montanari and Hu-Lu-Misiakiewicz 2403.08160; little of the row is open as written"),
("T344","KEEP","statement already records where the claim fails and asks the remaining width profiles"),
("T365","KEEP","L >= 3 levels with a standard architecture and all layers trained together; distinct from T277"),
("T277","REPLACE_OR_RESTATE","three-layer versus two-layer on f = g(h(x)), h low-degree: Nichani-Damian-Lee, arXiv 2305.06986, prove the three-layer upper bound and an optimisation-based separation (layer-wise training); read the lower-bound theorem to see whether 'any two-layer width, standard init' is still open"),
("T367","MERGE_WITH_T241","same question (global convergence of the three-layer feature-learning limit) in the mean-field parametrisation; T241 states it precisely in muP. Keep one row, mention both parametrisations"),
("T241","KEEP","precise statement; absorbs T367"),
("T373","DUPLICATE_OF_T268","both ask whether spectral-norm control alone gives size-independent sample complexity"),
("T268","RESTATE","Vardi-Shamir-Srebro, arXiv 2202.06233 (abstract read): spectral-norm control alone is insufficient in general already for one hidden layer, sufficient for smooth activations (extending to deeper networks); restate to what that leaves open, and absorb T373")]
with open("STATEMENT_PASS.tsv", "a", encoding="utf-8", newline="\n") as f:
    for i, v, why in rows: f.write("\t".join([i, v, why, "2026-11-11 statement read, an agent"]) + "\n")
print(len(rows))
