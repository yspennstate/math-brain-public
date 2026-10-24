# Serialization repair, frozen before the unchanged full-domain retry

The successful k=2 pilot took 0.024 seconds. The first full-domain invocation stopped during result serialization: exact Fraction endpoints exceeded Python's 4,300-digit integer-to-string guard. This was not a mathematical assertion failure, and the aborted invocation contributes no completed-case/check count.

Helper v1.1 reports interval endpoints rounded outward to the dyadic grid 2^-100. All computations and sign decisions continue to use the unchanged exact rational 24-term logarithm enclosures. No integer-string guard is disabled, dimension added, family changed, or precision search performed. The frozen full domain and resource caps remain unchanged. This also keeps output files well below 20 MB.
