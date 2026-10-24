def require(cond: bool, msg: str, errors: list[str]) -> bool:
    if not cond:
        errors.append(msg)
        return False
    return True


def parse_draft(path: Path) -> tuple[dict, list[str]]:
    errors: list[str] = []
    try:
        payload = json.loads(path.read_text(encoding="utf-8-sig"))
    except Exception as exc:  # noqa: BLE001
        return {}, [f"unreadable JSON: {exc}"]
    if not isinstance(payload, dict):
        return {}, ["top level must be an object"]
    require(payload.get("spec") == "mathbrain-draft-v1", "spec must be mathbrain-draft-v1", errors)
    entries = payload.get("entries")
    if not require(isinstance(entries, list) and entries, "entries must be a nonempty list", errors):
        return payload, errors
    if len(entries) > 200:
        errors.append("more than 200 entries in one draft")
    seen_keys: set[str] = set()
    seen_logical: set[str] = set()
    for i, entry in enumerate(entries):
        where = f"entries[{i}]"
        if not isinstance(entry, dict):
            errors.append(f"{where}: not an object")
            continue
        key = entry.get("key", "")
        if not require(isinstance(key, str) and key.strip(), f"{where}: key required", errors):
            continue
        if key in seen_keys:
            errors.append(f"{where}: duplicate key {key}")
        seen_keys.add(key)
        kind = entry.get("kind", "")
        if not require(kind in DRAFT_KINDS, f"{where}: kind must be one of {sorted(DRAFT_KINDS)}", errors):
            continue
        claim_kind = DRAFT_KINDS[kind]
        ns, ln = entry.get("namespace", ""), entry.get("logical_name", "")
        require(isinstance(ns, str) and IDENTIFIER_RE.fullmatch(ns) is not None, f"{where}: bad namespace {ns!r}", errors)
        require(isinstance(ln, str) and IDENTIFIER_RE.fullmatch(ln) is not None, f"{where}: bad logical_name {ln!r}", errors)
        logical = f"{ns}:{ln}"
        if logical in seen_logical:
            errors.append(f"{where}: duplicate logical name {logical} within draft")
        seen_logical.add(logical)
        stmt = entry.get("statement", "")
        require(isinstance(stmt, str) and len(stmt.strip()) >= 20, f"{where}: statement missing or too short", errors)
        require(isinstance(entry.get("title", ""), str) and entry.get("title", "").strip() != "", f"{where}: title required", errors)
        proof = entry.get("proof_text")
        if claim_kind in PROOF_REQUIRED:
            require(isinstance(proof, str) and len(proof.strip()) >= 20, f"{where}: {kind} requires proof_text", errors)
        else:
            require(proof in (None, ""), f"{where}: {kind} must not carry proof_text", errors)
        assumptions = entry.get("assumptions", [])
        require(isinstance(assumptions, list) and all(isinstance(a, str) and a.strip() for a in assumptions), f"{where}: assumptions must be nonempty strings", errors)
        src = entry.get("source")
        if not require(isinstance(src, dict), f"{where}: source object required", errors):
            continue
        for field_name in ("source_id", "url", "revision", "license"):
            require(isinstance(src.get(field_name), str) and src.get(field_name, "").strip() != "", f"{where}: source.{field_name} required", errors)
        lic = str(src.get("license", "")).lower()
        require(any(lic.startswith(p) for p in ALLOWED_LICENSE_PREFIXES), f"{where}: license {lic!r} not in allowlist", errors)
    relations = payload.get("relations", [])
    if not isinstance(relations, list):
        errors.append("relations must be a list")
        relations = []
    adjacency: dict[str, set[str]] = {}
    for i, rel in enumerate(relations):
        where = f"relations[{i}]"
        if not isinstance(rel, dict):
            errors.append(f"{where}: not an object")
            continue
        fk, tk, kind = rel.get("from_key"), rel.get("to_key"), rel.get("kind")
        require(fk in seen_keys, f"{where}: from_key {fk!r} not an entry key", errors)
        if rel.get("to_existing_logical"):
            require(
                isinstance(rel["to_existing_logical"], str)
                and rel["to_existing_logical"].startswith("math:"),
                f"{where}: to_existing_logical must be a math:namespace:name id",
                errors,
            )
        else:
            require(tk in seen_keys, f"{where}: to_key {tk!r} not an entry key", errors)
        require(kind in DRAFT_RELATIONS, f"{where}: bad relation kind {kind!r}", errors)
        require(isinstance(rel.get("rationale"), str) and rel.get("rationale", "").strip() != "", f"{where}: rationale required", errors)
        if kind == "depends_on" and fk in seen_keys and tk in seen_keys:
            adjacency.setdefault(fk, set()).add(tk)
    state: dict[str, int] = {}

    def acyclic(node: str) -> bool:
        state[node] = 1
        for nxt in adjacency.get(node, ()):
            mark = state.get(nxt, 0)
            if mark == 1:
                return False
            if mark == 0 and not acyclic(nxt):
                return False
        state[node] = 2
        return True

    for node in list(adjacency):
        if state.get(node, 0) == 0 and not acyclic(node):
            errors.append("depends_on relations contain a cycle")
            break
    return payload, errors

