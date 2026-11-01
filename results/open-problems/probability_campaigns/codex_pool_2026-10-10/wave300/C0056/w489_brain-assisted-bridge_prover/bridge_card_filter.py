"""Local proposal: disambiguate Poisson-transform cards in a small returned set.

This does not mutate the live retrieval engine or certify a theorem's hypotheses.
"""

def select_spectral_measure_cards(rows):
    kept = []
    for row in rows:
        title = row.get('title', '').casefold()
        body = row.get('body', '').casefold()
        if 'stieltjes' in title and 'measure' in body and 'transform' in body:
            kept.append(row)
        elif 'poisson' in title and 'kernel' in body and 'spectral measure' in body:
            kept.append(row)
    return kept
