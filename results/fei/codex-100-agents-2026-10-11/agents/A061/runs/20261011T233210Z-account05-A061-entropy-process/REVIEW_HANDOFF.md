# Source-bound handoff to A087 / A094

The B13 lead requested this handoff in STREAM_NOTES.md v2, 2026-10-11 23:1xZ. This file is a local review artifact for supervisor collection, not a sent message or an independent acceptance by A061.

Exact source: claude/B13/runs/20261011T223500Z-claude-B13-logcharge-sandwich/CLAIMS.json, B13-LOGCHARGE-KL-FORM v1 and B13-LOGCHARGE-SANDWICH v1. The lead's claims file contains the proof where its REPORT.md could not be saved. Sources and hashes are recorded in out/SOURCE_RECEIPTS.json.

Requested reconstruction: use nu_i=b_T^2/d_i and q_i=a_T^2+b_T^2 with q_i a normalized spectral marginal, not the physical branch probability. Check the algebra lambda_i/d_i=log2(1/d_i)-KL_2(nu_i||q_i), zero queried mass conventions, and the sandwich with BOTH terminal terms:

    H(f)-E H(g_tau)-(3/ln2)[I(f)-E I(g_tau)]
        <= E sum lambda_t <= H(f)-E H(g_tau).

Dependency pins: A061-FAIR-TREE-PROCESS v1 and A061-LOG-COMPENSATION v1, run 20261011T214516Z-account05-A061-entropy-process. A087 already independently accepted these exact statements in run 20261011T221055Z-account05-A087-restriction-referee, CLAIMS.json and REPORT.md, sections “Physical blocks and the conserved budget” and “A061 logarithmic compensation and scalar boundaries”. The original A061 proof includes a self-contained scalar JS bound, so this handoff does not need the lead's separate B13-J-LE-B-UNCERTAINTY or its unpinned external citation. Please review the sandwich and KL form separately from that uncertainty claim and from float64 maxima.

A061 is a contributor to the compensation dependency and therefore does NOT count this assembly as independent acceptance of the full chain. The supplied new point-function certificate is a concrete all-dimensional application with direct KL verification; its analytic proof is POINT_CERTIFICATE.md. Inspect its decreasing-rate series bound (4)--(6), exact polynomial identity (10), and rational interval checker. No universal FEI conclusion is asserted.

The independent A087 v1 reconstruction is consumed this stage and retires A061's baseline: no further telescope/sandwich rederivation is needed without an objection or changed premise. The pending new mathematical claim is only A061-POINT-COORDINATE-CERTIFICATE v1.
