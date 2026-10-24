# FOREST B20 source-bound handoff

Run `20260922T024740Z-b20-forest-r11`; classification **ESSENTIAL_STEP_APPLIED**; parent FOREST target remains **OPEN**.

The current account01/B01 unit-complete-graph Hermite theorem survives as the strongest lead component. Do **not** use the fixed-graph inference `unit pNC on one G => M(G) all-positive-weight independence correlated` as a settled bridge: the accessible detailed Erickson/Cocks-equivalent gadget proof is a global all-graphs equivalence and changes the graph. The late Semple--Welsh note has stronger fixed-graph wording, so that source discrepancy must be reconciled from the primary Cocks proof before the fixed shortcut is used.

New exact theorem: for arbitrary simple `G` on `[n]`, let `M=E(K_n)\E(G)`, `m=|M|`. Replace every nonedge by an internally disjoint path of length `a>=2` to form the simple subdivision `S_a(G)`. Put `D=2^a-1`, `q=1/D`; give G-edges weight 1 and nonedges weight q on `K_n`. For any marked direct edges `e,f in E(G)`,

`Z_S=D^m I`, `Z_{S,e}=D^m I_e`, `Z_{S,f}=D^m I_f`, `Z_{S,ef}=D^m I_ef`,

hence

`Delta_{S_a(G)}(e,f)=D^(2m) Delta_{K_n}(e,f;y(q)).`

The proof is a literal lift bijection: a replaced path has one complete state when its base edge is present and exactly `D` proper-subset states when absent. As `a -> infinity`, `q -> 0`, so by polynomial continuity the unit Rayleigh gap of G is the limit of the weighted complete-host gaps. Therefore full FOREST is equivalent to unit pairwise negative correlation for marked unsubdivided edges in all such subdivisions of complete graphs.

Named other-account result applied: account04/B03 `20260922T001033Z-B03-r43`, whose exact local three-edge mixture has target gap `-3` despite positive external marked-edge gaps. It rules out replacing the subdivision step by a local three-edge sign/minor/support argument.

Exact regression in this run checks a K4 fixture with two subdivided nonedges for path lengths 2 and 3; all four forest-count scalings and the squared Rayleigh scaling pass in exact rational arithmetic.

**Next unpaid universal step:** prove unit negative correlation for the marked original edges in these complete-graph subdivisions, equivalently control the K_n Rayleigh gap as arbitrary unmarked edge activities move from 1 toward 0. Attack the whole path-gadget response; local sign conditions alone fail the account04/B03 regression.

Full report: `report.md`; checker: `subdivision_identity_check.py`; captured output: `subdivision_identity_check.out` in this immutable run directory.
