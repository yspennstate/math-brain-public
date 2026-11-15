"""Add the peer report on T127 to DESERVE.tsv (an agent, 11 Nov)."""
import io
p = "DESERVE.tsv"
with io.open(p, encoding="utf-8", newline="") as f:
    s = f.read()
nl = "\r\n" if "\r\n" in s else "\n"
rows = s.split(nl)
n = 0
for k, r in enumerate(rows):
    c = r.split("\t")
    if c[0] == "T127" and len(c) >= 7:
        assert "mt0-svg" not in c[5]
        c[4] = "CLAIMED_SOLVED_UNVERIFIED"
        c[5] += ("; a public repository of Oct 2026 (github mt0-svg/frog-model-tree, Lean 4, Zenodo 10.5281/zenodo.23121586) claims "
                 "both halves; an agent replayed the d = 4 certificate with no failure, Lean build not rerun, d = 3 unread "
                 "(memory t127_frog_t3_t4_public_lean_proof_claim_mt0_svg_2026_11_11). No worker time until it is checked")
        c[6] += "; 2026-11-11 peer report recorded"
        rows[k] = "\t".join(c)
        n += 1
assert n == 1
with io.open(p, "w", encoding="utf-8", newline="") as f:
    f.write(nl.join(rows))
print("T127 noted")
