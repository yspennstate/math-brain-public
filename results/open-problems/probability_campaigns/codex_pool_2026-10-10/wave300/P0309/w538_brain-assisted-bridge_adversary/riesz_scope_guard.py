"""Proposed warning only; no live recall wiring or score changes."""
import re

def _plain(text):
    return re.sub(r'[_-]+', ' ', text.casefold())

def riesz_scope_warnings(query, candidates):
    q = _plain(query)
    gas_query = bool(re.search(r'\briesz\b', q) and re.search(r'\b(gas|gases|gibbs|jellium|crystall\w*)\b', q))
    explicit_product_query = bool(re.search(r'\briesz\s+products?\b', q))
    if not gas_query or explicit_product_query:
        return []
    warnings = []
    for row in candidates:
        identifier = str(row.get('id', ''))
        text = _plain(str(row.get('title', '')) + ' ' + str(row.get('body', '')))
        product_scope = bool(re.search(r'\briesz\s+products?\b', text)) or identifier.startswith('bc23_')
        gas_scope = bool(re.search(r'\b(jellium|coulomb|gibbs|gas|gases)\b', text))
        if product_scope and not gas_scope:
            warnings.append({'id':identifier,'reason':'Riesz-product scope without a Riesz-gas anchor; not target proof support.'})
    return warnings
