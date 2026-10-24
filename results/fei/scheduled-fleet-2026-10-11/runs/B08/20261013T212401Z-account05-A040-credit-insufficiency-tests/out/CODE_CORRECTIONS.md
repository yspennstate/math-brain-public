# Preserved implementation corrections

The first audit.py run passed 523 algebraic checks but included two unnecessary zero-influence control queries after the first exclusive event had already resolved the union. Although all entropy/face/influence bills were unchanged, it did not exactly implement the declared adaptive stopping rule. The final checker skips resolved irrelevant controls, has at most seven nonconstant internal nodes, and regenerated every output; its final assertion count is 427.

The first finalize.py constant check used 11/32 > (11/4)/8, which is an equality, as a rational substitute for 11/32 > e/8. It correctly failed. The report's proof uses the strict bound e<11/4; the exact certificate now uses the stronger already-proved rational bound e<65/24+1/100 and gets a positive rational margin. No mathematical claim or tree output was changed by this correction. Final schema and six constant checks pass.

Both were corrected in this run. Neither is a substantive failure of the mathematical payment mechanism; no claim of failed universal payment is inferred.
