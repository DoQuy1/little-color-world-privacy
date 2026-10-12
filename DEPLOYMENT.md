# Deployment

Status: **BLOCKED on one manual step - GitHub Pages is not verified live.**
The policy text itself has no placeholders left.

## Publish with GitHub Pages (manual, in the browser)

1. Open https://github.com/DoQuy1/little-color-world-privacy
2. Settings > Pages
3. Source: **Deploy from a branch**
4. Branch: `main`, folder: `/ (root)`, then Save
5. Wait for the deployment (usually under a few minutes) and open
   https://doquy1.github.io/little-color-world-privacy/
6. Check both language links, then use that URL in Play Console (App content > Privacy policy) and in the app.

Repository must be public for Pages on a free plan (it can be cloned without login, so it is public).

## Checks done locally (2026-10-12)

- HTML parses with Python `html.parser`; tags balanced; one `<title>`; `lang` set per section.
- All `href="#..."` anchors exist; external links are plain https links, not fetched here.
- No scripts, forms, cookies, external fonts or images.
- No placeholder text left; no secrets (the only personal data is the publisher name and email the owner asked to publish).
- Facts compared with the app code: no account/backend, local storage only (artworks, unlock ids, settings), Google Mobile Ads SDK
  with child treatment and G rating, advertising-id permissions removed, no analytics or crash reporting.
- Rendering checked in a 375 px wide browser window.

## Not verified

- The live URL (Pages not enabled yet).
- What the Google Mobile Ads SDK sends on the network (not audited; the policy says so).
- Spelling by a native Vietnamese speaker.
