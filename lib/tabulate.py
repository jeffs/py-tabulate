#!/usr/bin/env python3

import sys

def _find_indent(lines):
    """Returns all leading whitespace from the first non-empty line, if any."""
    line = next(line for line in lines if not line.isspace())
    return line[:len(line) - len(line.lstrip())]

def _tabulate(rows):
    num_fields = max(map(len, rows))

    length = lambda row, j: len(row[j]) if j < len(row) else 0
    widths = [max(length(row, j) for row in rows) for j in range(num_fields)]

    just = lambda x, w: x.rjust(w) if x.isdigit() else x.ljust(w)
    join = lambda row: ' '.join(just(x, w) for x, w in zip(row, widths))
    return [join(row).strip() for row in rows]

def tabulate(lines, max_fields=sys.maxsize):
    """Horizontally align space-separated fields in lines of text."""
    lines = tuple(lines)    # Force strict evaluation.
    split = lambda line: line.split(maxsplit=(max_fields - 1))
    rows = tuple(map(split, lines))
    indent = _find_indent(lines)
    return rows and tuple(indent + line for line in _tabulate(rows))
