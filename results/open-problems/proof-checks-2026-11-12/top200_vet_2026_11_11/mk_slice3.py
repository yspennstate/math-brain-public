import json, csv
rows = [json.loads(l) for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()]
move = "T112 T121 T124 T134 T147 T148 T149 T157 T158 T166 T175 T182 T183 T184 T187 T189 T191 T192 T193 T195 T196 T197 T198 T199 T202 T203 T204 T205 T206 T207 T208 T209 T210 T211 T213 T216".split()
border = {"T127": "frog model on 3-ary/4-ary trees: one gap in a solved family, small literature",
 "T165": "SRBM positive recurrence d>=4: specialist queueing-theory problem",
 "T169": "Neuhauser-Pacala coexistence: Cox-Durrett-Perkins cover much; small open core",
 "T173": "slotted ALOHA stability, 4+ users: classical but narrow",
 "T177": "Derrida-Retaux: the conjectured exponent is largely proved (Chen-Dagard-Derrida-Hu-Lifshits-Shi); check what is left",
 "T185": "alpha-fair bandwidth sharing stability: specialist stochastic-network problem",
 "T186": "circumference of G(n,c/n) scaling limit: narrow",
 "T194": "Drossel-Schwabl fire lanes: narrow (van den Berg-Brouwer question)",
 "T200": "exact 3-D Brownian intersection exponents: no closed form is expected; the row may not be a well-posed target",
 "T215": "copolymer critical slope: specialist polymer problem",
 "T217": "once-excited walk speed monotonicity in low dimension: narrow",
 "T218": "VRRW finite-range localization: narrow",
 "T220": "marginal disordered pinning free-energy asymptotics: narrow, much settled by Berger-Lacoin",
 "T222": "Steele's TSP variance limit: narrow"}
check = {"T162": "upper tail: Harel-Mousset-Samotij settle cliques in most regimes; check the open core is stated",
 "T214": "factor of IID for free Ising: Nam-Sly-Zhang go beyond uniqueness; check the stated range",
 "T219": "Coulomb mean-field limit: Serfaty 2020 proves the first-order case; check the row means Vlasov-Poisson"}
five = "T111 T116 T117 T118 T119 T120 T122 T129 T136 T137 T138 T144 T146 T153 T154 T155 T162 T163".split()
theirs = {r["id"]: r["verdict"] for r in csv.DictReader(open("../top200_review_2026_11_10/VERDICTS.tsv", encoding="utf-8"), delimiter="\t")}
out = open("DESERVE.tsv", "a", encoding="utf-8", newline="\n"); diff = []
for r in rows[110:222]:
    i = r["problem_id"]
    if r["list"] == "TOP200_RETIRED": sc, v, why = 5, "RETIRED_CHECK_REASON", "retirement source checked in LITCHECK.tsv"
    elif i in move: sc, v, why = 4, "MOVE_TO_GENERAL", "a real famous problem but not a probability problem (combinatorics, dynamics, information theory, analysis, complexity or group theory)"
    elif i in border: sc, v, why = 3, "BORDERLINE_NICHE", border[i]
    elif i in check: sc, v, why = 4, "CHECK_STATEMENT", check[i]
    else: sc, v, why = (5 if i in five else 4), "DESERVES", "recognised problem of the field"
    t = theirs.get(i, "?")
    if (v == "MOVE_TO_GENERAL") != (t.upper().startswith("MOVE")): diff.append("%s mine=%s theirs=%s" % (i, v, t))
    out.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (i, r["list"], r["title"], sc, v, why, "2026-11-11 title read, an agent; agent verdict: " + t))
out.close()
print("rows now", sum(1 for _ in open("DESERVE.tsv", encoding="utf-8")) - 1); print("differences with agent on MOVE:"); print("\n".join(diff) or "none")
from collections import Counter
print(Counter(l.split("\t")[4] for l in open("DESERVE.tsv", encoding="utf-8").read().splitlines()[1:]))
