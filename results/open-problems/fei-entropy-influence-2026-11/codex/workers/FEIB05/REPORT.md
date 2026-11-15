# FEIB05 report

I rebuilt the K33 nine-coin function and reproduced H/(I−1) = 6.521845710923046575658143972949 using exact integer spectra and 60-digit logarithms. The brief’s host wording needs correcting: the host accepts edge sets that contain a perfect matching, rather than only the six inputs that are exactly a perfect matching. The host accepts 247 of its 512 inputs. A second construction using Hall’s condition agreed on all 262144 inputs of the final balanced function. Sources: k33_construction_certificate.json, high_precision.json, score.py and certify_k33.py.

For that record, H = 6.776605309006 bits, A = 4.361829264436 bits, B = 2.414776044570 bits, Gamma = 0.065424559676 bits, P = 2.283875991917 bits, and I = 261/128 = 2.0390625. Its A/(I−1) is 4.197850720660 and its B/(I−1) is 2.323994990263. Containment A supplies most of the entropy; sign cancellation is small. RESULTS.md and levels.csv give every level, including the requested comparison families.

The largest B ratio I found is 2.618025428957766259992985612521 on a balanced function with ten essential variables. It has B = 3.190718491542 bits and I = 71/32 = 2.21875. Its table is tables/search_n10_B.hex. Bit x is set exactly when f(x)=−1, with coordinate i the ith bit of x. This improves the B ratio of the K33 entropy record in this experiment; it is not a claim of a new best-known FEI entropy ratio or a literature-wide B record.

A much smaller explicit witness already clears the requested threshold: n=6, table 0x00eceeee00ae8eee, B/(I−1)=2.262756797677368237928213365666, B=1.697067598258 bits, I=7/4. Both it and the ten-variable winner exceed the precise Theorem 1 requirement 2.260922855462 inferred from the quoted entropy record. Sources: high_precision.json and tables/search_n6_B.hex.

The B winner is not unate. For example, coordinate 0 has 127 positive and one negative directed edge differences. It differs on 40 inputs from the nearest member of the coordinate-fixed K33 completion family: use the fresh coin on core edge 5, and substitute the core edge variable for every other coin. characterization.json lists all changed input indices and the directed-edge counts. This establishes a concrete description and rules out equivalence to the monotone comparison families under signs and coordinate permutations. I did not identify a standard exact name for it; this does not establish novelty.

The best ratios found are below. Each column uses a separately optimized function. Ratios have units of bits per unit of excess influence.

| n | A/(I−1) | B/(I−1) | Gamma/(I−1) | H/(I−1) |
|---:|---:|---:|---:|---:|
| 6 | 4.173533749351 | 2.262756797677 | 0.729836051872 | 6.347067498702 |
| 7 | 4.173533749351 | 2.345867735805 | 0.783215259430 | 6.347067498702 |
| 8 | 4.173533749351 | 2.430158924052 | 0.828442340816 | 6.363969446288 |
| 9 | 4.173533749351 | 2.573953469707 | 0.862066394750 | 6.429941892810 |
| 10 | 4.173533749351 | 2.618025428958 | 0.895788073140 | 6.457041884365 |
| 11 | 4.173533749351 | 2.618025428958 | 0.923140455968 | 6.457041884365 |
| 12 | 4.173533749351 | 2.618025428958 | 0.923140455968 | 6.457041884365 |

These are search lower bounds. A’s best function has six essential variables throughout this range. The B and H winners at n=11 and n=12 ignore the additional coordinates; their essential dimension is ten. The Gamma winner at n=12 has eleven essential variables. The B growth and subsequent plateau do not decide whether its supremum is bounded. A also appears flat in this run, but the eighteen-variable K33 function already exceeds that plateau. There is no certified maximum for n≥6 and no new upper bound here. Source: records_index.json.

The search made 24780000 balanced-swap proposals across deterministic annealing and refinement passes, plus scoring structured seeds, coin extensions and K33 layouts. search_manifest.json records the counts from engine logs. The exact integer certificates store Walsh numerators, containment masses, absolute restriction sums and nonzero restriction counts. score.py obtains restrictions by direct input-domain differences. verify_independent.py reconstructs them from Fourier supersets, checking exact integer equality with every saved certificate on nonzero Fourier support. It also checks influence by counting cube edges. All 28 search winners and all 27 structured realizations passed. audit.json records the 55-table audit; the largest floating H−A−B residual was 2.6645352591003757e-15 bits. high_precision.json independently evaluates the headline sums at 60-digit precision.

The complete outputs are RESULTS.md, levels.csv, best.json, structured.json, verified_structured.json, characterization.json, the tables directory and the certificates directory. REPRODUCE.md gives commands and explains the deterministic seeds and saved engine versions. All compute was single-threaded per process, at absolute nice 10, with no more than two compute processes running together. certify_structured.log measured a peak resident set of 156499968 bytes for the largest direct-scoring batch; verify_records.log measured 44482560 bytes for its verification batch. polish.log measured a peak child resident set of 24330240 bytes. These measured batches are well below the 3 GiB limit.

The brain helped materially: it supplied the exact K33 construction and an earlier eight-variable coin-site example, which I independently reproduced at 6.363969446288. The attempted math-store recall reported that no math store was installed. I wrote no files outside this worker folder, posted nothing to the mesh or fleet board, and started no subagents. These results are left here for the launching session to publish or remember.

Open work is mathematical: stronger global search could improve the lower bounds, the B winner’s structure is not fully classified, and boundedness of A/(I−1) and B/(I−1) remains unresolved. The requested computational brief and deliverables are complete.

Task: “Do the brief fully and carefully” — 10 Nov 2026, 01:29 +04, worker receipt; FEIB05 brief on extremal FEI functions in H=A+B with Gamma.
