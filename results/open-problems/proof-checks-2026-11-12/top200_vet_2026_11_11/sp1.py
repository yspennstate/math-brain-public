rows = [
("T230","KEEP","statement names the open remainder (multi-pass SGD at the generative-exponent rate, no label preprocessing) and cites the 2024 work"),
("T243","RESTATE","the n^-1/2 versus n^-1 question for smooth test functions of k-point marginals is answered at order 1/n (Favaro-Hanin-Marinucci-Nourdin-Peccati, Quantitative CLTs in deep neural networks); what is open is the sharp rate in a functional metric on C(K) with depth dependence - to confirm against the paper before editing"),
("T246","RESTATE","second half (limiting singular-value law as L/n -> t) overlaps T247; keep the log-normal law for smooth activations here and leave the spectrum to T247"),
("T247","KEEP","distinct once T246 is trimmed: proof of the free-probability formula and isometry in the joint limit"),
("T260","KEEP","asks the rigorous proof for all L >= 2 and general activations, which the cited paper only conjectures; check the 2024 follow-up on structured deep features before solving"),
("T286","KEEP","names the general-activation case left open by the quadratic-activation result"),
("T291","KEEP","asks the hardness side (AMP optimal among efficient algorithms); a special case of the theme of T296, not a duplicate"),
("T309","KEEP","explicit class, network and objective; asks poly time or an SQ lower bound"),
("T317","KEEP","explicit setting (unbounded supports, small epsilon, dependence on epsilon)")]
import os
new = not os.path.exists("STATEMENT_PASS.tsv")
with open("STATEMENT_PASS.tsv", "a", encoding="utf-8", newline="\n") as f:
    if new: f.write("id\tverdict_after_statement\treason\tchecked\n")
    for i, v, why in rows: f.write("\t".join([i, v, why, "2026-11-11 statement read, an agent"]) + "\n")
print(len(rows))
