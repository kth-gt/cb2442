#!/usr/bin/env bash
#
# md2html.sh -- render a course Markdown page as a standalone HTML page.
#
# Usage (from this directory):
#   ./md2html.sh schedule.md              # writes schedule.html
#   ./md2html.sh schedule.md out.html     # writes out.html
#   ./md2html.sh -f page.md               # body fragment only, for Canvas
#
# The generated HTML is deliberately plain so that it can be hand-edited
# afterwards: raw inline tags in the Markdown (<oth>, <ali>, <sf>, <phyl>,
# <cncl>) and the <style> block that colours them are passed through
# untouched.
#
# With -f/--fragment the <html>/<head>/<body> wrapper is left out. Use this
# for Canvas: open a page in the Rich Content Editor, switch to the HTML view
# with the "</>" button and paste the fragment. Canvas strips <style> blocks,
# so a fragment that relies on one will lose its colours there.
#
# Requires pandoc (apt install pandoc).

set -euo pipefail

fragment=0
case ${1:-} in
    -f|--fragment) fragment=1; shift ;;
esac

if [ $# -lt 1 ] || [ $# -gt 2 ]; then
    echo "Usage: $0 [-f|--fragment] <input.md> [output.html]" >&2
    exit 1
fi

src=$1
dst=${2:-${src%.md}.html}

if [ ! -f "$src" ]; then
    echo "$0: no such file: $src" >&2
    exit 1
fi

if ! command -v pandoc >/dev/null 2>&1; then
    echo "$0: pandoc not found, install it with 'sudo apt install pandoc'" >&2
    exit 1
fi

# Title: first level-1 heading of the document, falling back to the file name.
title=$(sed -n 's/^# \+//p' "$src" | head -1)
title=${title:-$(basename "${src%.md}")}

# -smart          keeps "--" and quotes verbatim instead of prettifying them
# --columns=999   stops pandoc from emitting a <colgroup> with fixed relative
#                 widths, so the browser sizes the schedule columns itself
body=$(pandoc \
    --from=markdown+pipe_tables+raw_html+auto_identifiers-smart \
    --to=html5 \
    --wrap=preserve \
    --columns=999 \
    "$src")

if [ "$fragment" -eq 1 ]; then
    printf '%s\n' "$body" > "$dst"
    echo "$src -> $dst (fragment)"
    exit 0
fi

cat > "$dst" <<EOF
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>$title</title>
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/4.0.0/github-markdown.min.css">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/gh/highlightjs/cdn-release/build/styles/default.min.css">
<style>
body.markdown-body { box-sizing: border-box; max-width: 1012px; margin: 0 auto; padding: 32px; }
</style>
</head>
<body class="markdown-body">
$body
</body>
</html>
EOF

echo "$src -> $dst"
