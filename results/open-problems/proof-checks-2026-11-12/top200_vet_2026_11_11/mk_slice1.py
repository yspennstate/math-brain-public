import json
rows = [json.loads(l) for l in open("../top200_probability_2026_10_14/list.jsonl", encoding="utf-8") if l.strip()]
out = open("DESERVE.tsv", "w", encoding="utf-8", newline="\n")
out.write("id\tlist\ttitle\tscore_1to5\tverdict\treason\tchecked\n")
for r in rows[:40]:
    ret = r.get("list") == "TOP200_RETIRED"
    out.write("%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (r["problem_id"], r["list"], r["title"], 5,
              "RETIRED_CHECK_REASON" if ret else "DESERVES",
              "canonical named problem of the field; retirement reason to be checked against the literature" if ret
              else "canonical named problem of the field (standard problem lists, ICM and survey literature)",
              "2026-11-11 title read, an agent (Fable 5.2); statement not yet re-read"))
out.close(); print("wrote", 40)
