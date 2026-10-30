# PDF audit status

Exact pinned PDF bytes were fetched through the authorized GitHub connector and independently base64-decoded in this invocation. The decoded file is 484,310 bytes, begins with `%PDF-1.5`, contains 14 PDF page objects, has Git blob `8be3aae36ecad7a9dc9b7c95978aad09499f32d0`, and independently recomputed SHA-256 `4c1a8eb808b32739625aa475c1aad24dc857a3f35fc960504b371487f2850423`.

Direct rendered-page inspection is **UNCHECKED/BLOCKED** in this invocation. The required web PDF open path was attempted on the exact raw GitHub URL and returned `DisabledError`, so no screenshot tool could be invoked. I do not claim a fresh visual comparison that did not occur.

For exact PDF-page references in the line ledger I reused only the page/source boundary map produced by B19's previous independent decoded-stream pass on the *same exact pinned PDF blob*, after revalidating the blob/hash/page count here: p1 L1-70; p2 L71-118; p3 L119-162; p4 L163-204; p5 L205-248; p6 L249-305; p7 L306-345; p8 L346-392; p9 L393-436; p10 L437-484; p11 L485-537; p12 L538-576; p13 L577-627; p14 L628-676.

Consequently this run completes two full TeX proof passes with exact PDF page scaffolding and exact PDF byte integrity, but it does **not** upgrade the rendered-PDF visual layer to PASS. That remains the first representation-level unchecked item.
