# Generated API links

On each applicable authored page, link the first visible explanatory mention of
every project-owned public API entity to its generated GNATdoc entry. Entities
include packages, generic packages, subprograms, types, objects, exceptions,
enumeration literals, and other documented declarations.

Determine the consumer's contract before authoring a link:

1. Read the site build and API-link resolver, when present.
2. Inspect representative authored pages that pass the current verifier.
3. Identify every project-owned API root built by the repository. A monorepo
   may publish more than one crate under different paths.
4. Determine whether authored source uses resolver attributes such as
   `data-api` and `data-api-signature` or checked literal `href` targets. Do not
   mix mechanisms or copy one from another repository.

Then apply these rules:

- Follow reading order. The first mention can occur in a hero, callout,
  paragraph, list, table, or figure caption.
- Use an HTML link containing a `code` element for an identifier in prose.
- Link a package to its generated unit page. Link a declaration to its exact
  entity anchor when one exists.
- For an overloaded subprogram, use the repository's reviewed signature
  selector when its resolver supports one. Otherwise select the declaration
  that matches the described operation. Link the package page when prose
  describes the overload family.
- If the first identifier occurs in a code block, comment, or SVG label, link
  it in the nearest explanatory prose or caption.
- Resolve generated filenames and anchors from actual GNATdoc output, its
  search index, or the maintained resolver. Do not guess them.
- Verify both the target file and fragment through the repository's site build
  and link checks.
- Link only the first explanatory mention unless the same spelling denotes a
  different entity or a deliberate navigation aid is useful.
- Do not link Ada language constructs, compiler or runtime internals, protocol
  standards, OS interfaces, environment variables, shell commands, scripts,
  or external APIs to project GNATdoc. Link external documentation only when it
  is authoritative and useful.
- Report a missing generated entry as a finding. Do not link to an unrelated
  declaration.
