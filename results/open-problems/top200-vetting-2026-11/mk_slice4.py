import json, csv
rows = [json.loads(l) for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()]
five = "T223 T226 T231 T237 T241 T244 T256 T263 T272 T274 T283 T284 T287 T289 T290 T292 T296 T301 T304 T308".split()
replace = {"T255": "solved by us on the repaired statement (17 Oct, triple audit): the row leaves the list and a replacement enters",
 "T303": "the KLS conjecture: duplicate of retired probability row T018 and not a deep-learning problem",
 "T314": "reported solved (Lee-Sandhu-Shi arXiv 2609.30590, unrefereed): confirm the preprint, then replace"}
check = {"T230": "sample reuse / generative exponent: Lee-Oko-Suzuki-Wu and Dandi et al. (2024) answer much; check what the row still asks",
 "T243": "optimal Gaussian-process rates: Favaro-Hanin-Marinucci-Nourdin-Peccati and Trevisan give sharp rates in several metrics; check the open core",
 "T247": "possible overlap with T246 (Jacobian law): read both statements",
 "T260": "deep random-features error universality: Schroder-Cui-Dmitriev-Loureiro (2023) prove a large part; check the open core",
 "T286": "quadratic-activation case solved (Maillard-Troiani-Martin-Krzakala-Zdeborova 2024); check the row names the general case",
 "T291": "weak learnability of multi-index models: Troiani-Dandi-Defilippis-Zdeborova-Loureiro-Krzakala (2024) give the AMP thresholds; check the open core",
 "T309": "Gaussian mixtures by score matching: Chen-Kontonis-Shah and Gatmiry-Kelner-Lee (2024) answer much; check the open core",
 "T317": "Sinkhorn / IPF rates: exponential convergence known in several settings (Conforti, Chiarini et al.); check the stated setting"}
border = {"T258": "symmetric spurious minima of ReLU teacher-student (Arjevani-Field): narrow",
 "T313": "Do GANs learn the distribution: a discussion question more than a stated conjecture; check for a precise target",
 "T318": "cold posterior effect: an empirical puzzle with no agreed mathematical statement",
 "T320": "depth of normalizing flows: narrow approximation question",
 "T321": "polynomial mixing of Langevin for nonconvex learning objectives: too broad as titled; check for a precise target"}
theirs = {r["id"]: (r["verdict"], r["reason"]) for r in csv.DictReader(open("../top200_review_2026_11_10/VERDICTS.tsv", encoding="utf-8"), delimiter="\t")}
out = open("DESERVE.tsv", "a", encoding="utf-8", newline="\n"); n = {}
for r in rows[222:322]:
    i = r["problem_id"]; tv, tr = theirs.get(i, ("?", ""))
    if i in replace: sc, v, why = 0, "REPLACE", replace[i]
    elif tv == "RESTATE": sc, v, why = (5 if i in five else 4), "DESERVES_RESTATE", "agent: " + tr
    elif i in check: sc, v, why = 4, "CHECK_STATEMENT", check[i]
    elif i in border: sc, v, why = 3, "BORDERLINE_NICHE", border[i]
    else: sc, v, why = (5 if i in five else 4), "DESERVES", "recognised problem of deep-learning theory"
    n[v] = n.get(v, 0) + 1
    out.write("\t".join([i, r["list"], r["title"], str(sc), v, why, "2026-11-11 title read, an agent; agent verdict: " + tv]) + "\n")
out.close(); print(n)
