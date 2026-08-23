# Generated API links

On each authored Guide, Architecture, or Journal page, link the first visible
explanatory mention of every project-owned public API entity to its generated
GNATdoc entry.

- Follow reading order. The first mention can occur in a hero, callout,
  paragraph, list, table, or figure caption.
- Use an HTML link containing a `code` element for an identifier in prose.
- Link a package to its generated unit page. Link a declaration to its exact
  entity anchor when one exists.
- For an overloaded subprogram, select the declaration that matches the
  described operation. Link the package page when prose describes the overload
  family.
- If the first identifier occurs in a code block, comment, or SVG label, link
  it in the nearest explanatory prose or caption.
- Resolve generated filenames and anchors from actual GNATdoc output or its
  search index. Do not guess them.
- Verify both the target file and fragment.
- Link only the first explanatory mention unless the same spelling denotes a
  different entity or a deliberate navigation aid is useful.
- Report a missing generated entry as a finding. Do not link to an unrelated
  declaration.
