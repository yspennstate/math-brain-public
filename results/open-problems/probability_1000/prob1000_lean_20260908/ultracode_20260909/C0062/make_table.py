import json
recs = {}
for l in open("maxdim_results.jsonl", encoding="utf-8"):
    r = json.loads(l); recs[r["n"]] = r
with open("maxdim_table_1_90.txt", "w", encoding="utf-8") as f:
    f.write("n\tclasses_up_to_conjugation\tself_conjugate\tlog_gap_to_next_nonconjugate\tmaximiser(lambda_1>=rows)\tmax_dim\n")
    for n in range(1, 91):
        r = recs[n]
        f.write("%d\t%d\t%d\t%s\t%s\t%s\n" % (n, r["classes_up_to_conjugation"], int(r["self_conjugate"]), r["log_gap_to_next"], r["maximisers"][0], r["dmax"]))
