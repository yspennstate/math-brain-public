# Formal verification

The repository pins Lean in `formal/lean-toolchain` and keeps the trusted source
surface independent of external theorem libraries. `lakefile.toml` is accepted
only as declarative project metadata: the authority runner never launches Lake,
an Elan proxy, a shell, a script, or a network-capable package resolver.

## Local authority runner

`check_lean_file` stable-reads every local `.lean` file, the exact toolchain pin,
and the strict dependency-free Lake TOML schema. It rejects links, hard links,
oversized trees, nonlocal imports, import cycles, proof placeholders, new axioms,
unsafe/native escapes, custom elaborators, compile-time I/O, and output-spoofing
commands. It then copies the accepted bytes into a fresh private snapshot.

The runner resolves `lean` directly inside the exact installed pinned Elan
toolchain. The executable is hash-pinned and held against replacement for the
entire run. Local modules are compiled in topological order with a fixed plan:

```text
lean --trust=0 -j1 -M1024 -R <snapshot> -o <module>.olean <module>.lean
```

Execution uses bounded output pipes, one global timeout and output budget,
hidden and BelowNormal Windows process creation, whole-tree containment, and
fresh compute-governor checks before and throughout the run. The environment is
reduced to a fixed allowlist, `LEAN_PATH` names only the immutable snapshot, and
no cloud or API path exists. Any timeout, owner return, governor closure, output
overflow, executable drift, process-tree failure, or unverified cleanup fails
closed.

## Named declarations and authority

Authority is Windows-only. Holding the executable against replacement uses a
Windows file handle; on Linux and macOS the runner opens the binary read-only,
cannot stop it from being replaced, and records `executable_lock_enforced =
false`. A build there still runs and reports its diagnostics, its reason says
that the authority is unsupported on the platform, `authority_blockers` names
the gate, and no `lean_kernel` evidence can be issued.

A successful compile is diagnostic until the caller names at least one formal
declaration. Every named declaration must have exactly one canonical
`#print axioms Fully.Qualified.name` command in the captured source and exactly
one kernel output saying that it depends on no axioms. Duplicate, missing, or
positive axiom reports make the result ineligible for authority.

An authority-eligible result binds the source tree, request policy, named
declarations, executable, pinned and observed toolchain, bounded output,
environment, compute observations, cleanup status, zero marginal API cost, and
no-network status. An ephemeral in-process HMAC seal prevents callers from
substituting fields between execution and issuance.

`LocalLeanEvidenceAuthority.verify_and_issue` performs the run and emits a
`lean_kernel` evidence row, typed local-automated attestation, and authenticated
receipt only when every gate passes. The attestation additionally binds the
immutable claim digest. A failed or merely diagnostic run returns no authority
records and cannot be promoted.

## Human formalization-fidelity authority

Kernel authority and semantic fidelity use different keys, roles, and issuance
paths. `bind_formal_statement` stable-reads the exact local `.lean` file and
records one named declaration, repository-relative file locator, file hash,
one-based line span, and exact byte-span hash. The line span must contain exactly
one supported declaration header. This is a locator for human review, not an
automated claim that the prose and formal statement mean the same thing.

`StatementFidelityReview` binds the immutable claim digest, exact UTF-8 prose
hash, sealed Lean-result digest, source-tree hash, ordered declaration bindings,
reviewer key ID, all seven checklist answers, and bounded notes. Each checklist
answer must be an exact boolean, and notes cannot override a false answer.

`LocalFormalizationFidelityAuthority.review_and_issue` reopens the project through
the stable-reader boundary and independently recomputes the source tree, project
manifest, file hashes, line-span hashes, and declaration headers. It issues
`formalization_fidelity` evidence only if every binding still matches, the
ephemeral Lean-result seal is valid, every checklist dimension passes, and the
reviewer key ID is the key owned by this human-review authority. A passing
issuance also requires a nonempty signed review note. The resulting
attestation and HMAC receipt bind the exact review and remain local, offline, and
zero marginal API cost.

The evidence verifier fixes `formalization_fidelity` to the human-review role.
It rejects a human key configured for automated evidence and rejects any attempt
to reuse the same key material under both Lean and human authority IDs. Thus an
automated Lean signer cannot satisfy both halves of the theorem-verification
route.

## What a kernel check proves

A successful authority run proves that the named formal declarations were
accepted by the pinned local Lean kernel from the exact recorded source snapshot
without reported axioms. It does not prove that a formal statement faithfully
represents a prose theorem, nor does it validate citations or experiments.

Promotion therefore requires separate evidence:

1. `lean_kernel` — the exact named declarations pass the local authority runner;
2. `formalization_fidelity` — an independent reviewer compares definitions,
   domains, assumptions, quantifiers, conclusions, and boundary cases against
   the hashed prose claim.

Notes cannot override a failed fidelity dimension. The formal statement must be
repaired or the prose claim narrowed.

The two records must describe one formal generation. Status promotion joins the
kernel and fidelity records on the source-tree hash and toolchain digest in their
authenticated receipts and on the declarations their evidence names; a kernel
record and a fidelity record that differ in any of these do not form a route,
whichever records exist beside them, and a persisted event built on such a pair
fails replay. Among several records the first kernel record with a matching
fidelity record is used. The lakefile and the exact Lean-result digest are not
carried in the receipts, so they are not part of the join.

These authorities are a library interface. No command in this repository calls
them, so no deployed theorem-verification path exists yet.

## Reproducibility

The evidence envelope contains path-scrubbed diagnostics and content hashes, not
machine hostnames or public absolute paths. Independent reproduction reruns the
same source and toolchain policy under a distinct authority key; it is not
inferred from the first machine's receipt.
