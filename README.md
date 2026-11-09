# Dr. Ahmad Atlas

Nine photographic sheets in three chapters, a concern-led directory of eight published Harley Street Aesthetics skin treatments, three worksheets, an HTML reading copy and a 15-page PDF. No checkout, account or backend.

Preview locally: python -m http.server 8765 --directory dist

Deployment output: dist/ (the directory containing index.html). No npm install command, build command, or environment variables. For plain static hosting, upload the contents of dist/ to the website document root.

Edit dist/data.js for reference sheets, captions and source links. Edit dist/skin-services.js for the website's concern and treatment directory. To regenerate the downloadable reading files, run node export.mjs followed by python make_pdf.py with ReportLab installed. Verify treatment availability and claims against the clinic's live pages before changing the directory. Source links identify clinic topics and further reading; they do not indicate clinician approval.
