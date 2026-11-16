"""Add the 15 Nov reading of the round-6 T127 brief to column 7 of DESERVE.tsv."""
P = "DESERVE.tsv"
ADD = ("2026-11-15 an agent (Opus 5.5) read round6/T127 REPORT.md and SOLVED_ELSEWHERE.md: the outside source is "
       "mt0-svg v2.0.0 (4 Oct 2026, Zenodo 10.5281/zenodo.23121586, no arXiv id), recurrent for d=3 and transient for d=4; "
       "the round-6 worker audited its 14 blob identities, model definitions and the d=3 planted-count bridge "
       "(conditional bound improved to 9/400) but did not rerun the Lean build or check the d=3 linear estimate; "
       "status stays CLAIMED_SOLVED_UNVERIFIED; ")
rows = open(P, encoding="utf-8").read().split("\n")
n = 0
for k, line in enumerate(rows):
    f = line.split("\t")
    if len(f) == 7 and f[0] == "T127" and "2026-11-15" not in f[6]:
        f[6] = ADD + "earlier: " + f[6]
        rows[k] = "\t".join(f)
        n += 1
open(P, "w", encoding="utf-8", newline="").write("\n".join(rows))
print("updated", n)
