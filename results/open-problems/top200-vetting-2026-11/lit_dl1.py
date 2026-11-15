rows = [("T253","2205.10217, 2007.12826","Bombari-Amani-Mondelli; Montanari-Zhong"),("T261","2403.08160","Hu-Lu-Misiakiewicz"),
("T283","2505.17360","Buhai-Hsieh-Jain-Kothari"),("T284","2411.01836","Li-Schramm"),("T292","2304.10524","Chen-Dou-Goel-Klivans-Meka"),
("T305","2304.04724","Chen-Gatmiry-Jiang"),("T310","2409.08469","Banerjee-Balasubramanian-Ghosal"),("T314","2609.30590","Lee-Sandhu-Shi, Potential Hessian Ascent IV"),
("T350","2504.19983","Ren-Nichani-Wu-Lee"),("T361","2504.19983","Ren-Nichani-Wu-Lee"),("T352","2401.10371v7","Chien-Wang-Chen-Li, Langevin Unlearning: title is about unlearning, read Thm 3.3 before accepting the removal"),
("T377","2503.02877, 2610.09044","Medvedev-Lyu-Yu-Arora-Li; Oliveira-Paquette")]
import json
t = {json.loads(l)["problem_id"]: json.loads(l)["title"] for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()}
with open("LITCHECK.tsv", "a", encoding="utf-8", newline="\n") as f:
    for i, a, who in rows:
        f.write("\t".join([i, t[i], a, "exists, title and authors read: " + who, "EXISTS (claim in agent VERDICTS not yet read against the paper)"]) + "\n")
print("ok")
