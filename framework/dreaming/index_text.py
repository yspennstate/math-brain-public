"""Pure, budgeted index text helpers; importing this module performs no I/O."""
import re
import os

_TAGS = re.compile(r"^(?:\s*\[[A-Z][A-Z -]*\]\s*)+")
_QUESTION = re.compile(r"(?i)^(?:why|how|what|which|who|whom|whose|where|when|is|are|was|were|do|does|did|can|"
                       r"could|should|would|will|has|have|had|may|might|must)\b")


def index_row_text(desc, budget):
    """Existing answer-first policy, followed by boundary-safe shortening."""
    if os.environ.get("BRAIN_INDEX_ANSWER_FIRST", "1") == "0":
        return shorten_index_text(desc, budget)
    text = _TAGS.sub("", desc or "").strip()
    q = text.find("?")
    if _QUESTION.match(text) and 0 < q <= 200 and len(text) - q - 1 >= 20:
        text = text[q + 1:].strip()
    return shorten_index_text(text, budget)


def shorten_index_text(text, budget):
    """Keep a complete clause when useful, otherwise complete whitespace tokens.

    Budget counts characters, as the existing index writers do. A token longer
    than the entire budget is omitted rather than split. No ellipsis is added.
    """
    budget = max(0, int(budget))
    text = " ".join((text or "").split())
    if len(text) <= budget:
        return text
    # A previously shortened prefix already fits exactly. Keep it stable on
    # the next nightly pass instead of selecting an earlier clause again.
    if budget and text[budget].isspace():
        return text[:budget].rstrip()
    # Include punctuation only when followed by whitespace: don't split URLs,
    # decimal numbers, file names, hyphenated words or identifiers.
    clauses = [m.end() for m in re.finditer(r"[;,.!?](?=\s|$)", text)
               if m.end() <= budget]
    if clauses and clauses[-1] >= budget / 2:
        return text[:clauses[-1]].rstrip()
    boundaries = [m.start() for m in re.finditer(r"\s+", text)
                  if m.start() <= budget]
    return text[:boundaries[-1]].rstrip() if boundaries else ""


def frontmatter_description(path):
    """Read only a bounded frontmatter description; no body-derived summary."""
    try:
        with open(path, encoding="utf-8") as handle:
            head = handle.read(16384)
    except (OSError, UnicodeError):
        return ""
    fm = re.match(r"\ufeff?---[^\S\n]*\n(.*?)\n---(?:\s|$)", head, re.S)
    if not fm:
        return ""
    match = re.search(r"^description:[ \t]*(.*)$", fm.group(1), re.M)
    if not match:
        return ""
    value = match.group(1).strip()
    if value in ("|", ">", "|-", ">-", "|+", ">+"):
        continuation = fm.group(1)[match.end():].splitlines()
        parts = []
        for line in continuation:
            if line and not line[0].isspace():
                break
            parts.append(line.strip())
        value = " ".join(parts)
    elif len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        quote = value[0]
        value = value[1:-1]
        value = (value.replace('\\"', '"').replace('\\\\', '\\')
                 if quote == '"' else value.replace("''", "'"))
    return " ".join(value.split())


# Canonical readers must restore this optional output view before parsing it.
# Leave an adjacent opening parenthesis untouched: omitting the destination
# there would make the short pointer indistinguishable from a full link.
_PROMPT_MARKER = '<!-- brain-index-prompt-v1: self-link destinations omitted -->\n'
_SELF_LINK = re.compile(r'^- \[([A-Za-z0-9_-]+\.md)\]\(\1\)(?!\()', re.M)
_SHORT_POINTER = re.compile(r'^- \[([A-Za-z0-9_-]+\.md)\](?!\()', re.M)


def prompt_index_text(text):
    """Render self-links once, keeping all descriptions, tags and line endings.

    This is an output view, never a replacement for MEMORY.md. The marker and
    short-pointer syntax are reserved so restoration is unambiguous. Other
    link labels, destinations and Markdown are left byte-for-byte intact.
    """
    if text.startswith(_PROMPT_MARKER) or _SHORT_POINTER.search(text):
        raise ValueError('expected canonical index, not an existing prompt view')
    compact, count = _SELF_LINK.subn(lambda m: '- [%s]' % m.group(1), text)
    # Do not expand a small index merely to pay for the format marker.
    if count and len(text) - len(compact) > len(_PROMPT_MARKER):
        return _PROMPT_MARKER + compact
    return text


def restore_prompt_index(text):
    """Restore the exact canonical rows from a marked prompt view."""
    if not text.startswith(_PROMPT_MARKER):
        if _SHORT_POINTER.search(text):
            raise ValueError('unmarked short pointers are not a canonical index')
        return text
    body = text[len(_PROMPT_MARKER):]
    # Prompt views cannot contain another marker or already-expanded self-links.
    if body.startswith(_PROMPT_MARKER) or _SELF_LINK.search(body):
        raise ValueError('mixed or nested prompt view')
    restored, count = _SHORT_POINTER.subn(
        lambda m: '- [%s](%s)' % (m.group(1), m.group(1)), body)
    if not count:
        raise ValueError('prompt view has no short pointers')
    return restored


def _index_text_cli(argv=None):
    """Print either form; no index or memory is ever written by this command."""
    import argparse
    import sys
    parser = argparse.ArgumentParser(description='Print a canonical or compact memory-index prompt.')
    parser.add_argument('mode', choices=('canonical', 'prompt', 'restore'))
    parser.add_argument('path', help='UTF-8 index file to read')
    args = parser.parse_args(argv)
    # newline='' keeps CRLF in a reversible view as well as in library use.
    with open(args.path, encoding='utf-8', newline='') as handle:
        text = handle.read()
    if args.mode == 'prompt':
        text = prompt_index_text(text)
    elif args.mode == 'restore':
        text = restore_prompt_index(text)
    sys.stdout.buffer.write(text.encode('utf-8'))
    return 0


if __name__ == '__main__':
    raise SystemExit(_index_text_cli())
