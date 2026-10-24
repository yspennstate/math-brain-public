"""2026-09-09: Addario-Berry, Brandenberger, Hamdan, Kerriou, 'Universal height and width bounds for random
trees' (arXiv 2105.03195v2, EJP 27 (2022) 118; source abhk_height_width_2022) proves Janson's width statements
(Conjecture 20.6 = published 21.6, Problem 20.8 = published 21.8) and the height statements up to log^3 n.
F0066 and F0068 become literature exclusions; F0065 and F0067 get the lead appended. Every other line of
problems.jsonl is left byte-identical. Run once."""
import json
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
path = HERE / "problems.jsonl"

ABHK = ("Addario-Berry, Brandenberger, Hamdan, Kerriou, 'Universal height and width bounds for random trees' "
        "(arXiv 2105.03195v2, Electron. J. Probab. 27 (2022), paper 118), text read from the fetched PDF "
        "(source abhk_height_width_2022). Their Section 5 restates the source's statements as 'Conjecture 1 ([13]). "
        "Let w = (w_k, k >= 0) be a weight sequence with w_0 > 0 and with w_k > 0 for some k >= 2, and for n >= 0 with "
        "Z_n(w) > 0 let T_n be a simply generated tree of size n with weight sequence w. (1) If nu = 1 and sigma^2 = "
        "infinity then ht(T_n)/n^{1/2} -> 0 in probability. (2) If nu = 1 and sigma^2 = infinity then wid(T_n)/n^{1/2} "
        "-> infinity in probability. (3) If nu < 1 then ht(T_n)/n^{1/2} -> 0 in probability. (4) If nu < 1 then "
        "wid(T_n)/n^{1/2} -> infinity in probability.' (their [13] is the source; the numbering 21.5, 21.6, 21.7, 21.8 "
        "is the published version's, 20.5-20.8 in the arXiv version used here), and after Corollary 5.3: 'if nu < 1, "
        "or if nu = 1 and sigma^2 = infinity, then ht(T_n)/(n^{1/2} log^3 n) -> 0 and wid(T_n)/n^{1/2} -> infinity in "
        "probability. This proves the second and fourth points of the above conjecture and nearly proves the first "
        "and third points, up to the polylogarithmic factors.' Their abstract: 'Our results allow us to prove a "
        "conjecture and settle an open problem of Janson [13], and nearly prove another conjecture and settle "
        "another open problem from the same work (up to a polylogarithmic factor).' Lead supplied on the mesh by "
        "claude-prob1000-e0077-0908 (2026-09-09 03:08Z) and verified against the paper's text by the intake F agent.")

out = []
n = 0
for line in path.read_text(encoding="utf-8").splitlines():
    if not line.strip():
        continue
    r = json.loads(line)
    pid = r.get("problem_id")
    if pid in ("F0066", "F0068"):
        r["admitted"] = False
        r["current_status"] = "resolved_in_literature"
        r["resolved_by"] = ABHK + (" Point (2) is the source's Conjecture 20.6 verbatim." if pid == "F0066"
                                   else " Point (4) is the source's Problem 20.8 verbatim (answer: yes).")
        if not r["title"].startswith("[EXCLUDED] "):
            r["title"] = "[EXCLUDED] " + r["title"]
        r["status_search"] = r["status_search"] + " UPDATE 2026-09-09: resolved, see resolved_by."
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True)); n += 1
    elif pid in ("F0065", "F0067"):
        r["status_search"] = (r["status_search"] + " UPDATE 2026-09-09: " + ABHK +
                              " For this row (the height statement) they prove ht(T_n)/(n^{1/2} log^3 n) -> 0; the "
                              "o(n^{1/2}) statement itself is what remains open, so the row stays admitted.")
        out.append(json.dumps(r, ensure_ascii=False, sort_keys=True)); n += 1
    else:
        out.append(line)
path.write_text("\n".join(out) + "\n", encoding="utf-8", newline="\n")
print("patched rows:", n)
