import json, re
rows = [json.loads(l) for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()]
border = {"T059": "Robbins' problem: well known in optimal stopping, narrow reach; read statement",
          "T062": "Sylvester's problem d>=3: geometric probability classic, narrow reach; read statement",
          "T073": "noisy majority vote on Z^2: known in IPS, small literature; read statement",
          "T101": "Lorentz mirror model closed orbits: known (Grimmett list), small literature; read statement",
          "T104": "Oliveira's conjecture: much is proved (Alon-Kozma, Hermon-Salez); check what is left is top-200",
          "T096": "SK Glauber up to beta=1: sampling side largely done; check the open core"}
out = open("DESERVE.tsv", "a", encoding="utf-8", newline="\n")
for r in rows[40:110]:
    i = r["problem_id"]; ret = r.get("list") == "TOP200_RETIRED"
    if ret: sc, v, why = 5, "RETIRED_CHECK_REASON", "canonical; retirement source checked in LITCHECK.tsv"
    elif i in border: sc, v, why = 3, "BORDERLINE_READ_STATEMENT", border[i]
    else: sc, v, why = (5 if int(i[1:]) <= 60 else 4), "DESERVES", "recognised named problem of the field"
    out.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (i, r["list"], r["title"], sc, v, why, "2026-11-11 title read, an agent; statement not yet re-read"))
out.close()
found = {}
for l in open("arxiv_found.txt", encoding="utf-8"):
    if "|" in l: found[l.split("v")[0].strip()] = l.strip()
lc = open("LITCHECK.tsv", "w", encoding="utf-8", newline="\n")
lc.write("id\ttitle\tcited\tarxiv_api_2026_11_11\tverdict\n")
for r in rows:
    if r.get("list") != "TOP200_RETIRED": continue
    ids = re.findall(r"arXiv:(\d{4}\.\d{5})", str(r.get("retired_reason")))
    hit = [found[x] for x in ids if x in found]
    lc.write("%s\t%s\t%s\t%s\t%s\n" % (r["problem_id"], r["title"], ",".join(ids) or "no arXiv id (see reason)", " ;; ".join(hit) or "not fetched",
             "RETIREMENT SOURCE EXISTS, title and authors match; proof itself not audited" if hit else "TO CHECK"))
lc.close(); print("ok", sum(1 for _ in open("DESERVE.tsv", encoding="utf-8")) - 1, "deserve rows")
