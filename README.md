# Dr. Ahmad Atlas

Nine photographic sheets in three chapters, three worksheets, an offline HTML reading edition and a 15-page PDF. No checkout, account or backend.

Preview locally: python -m http.server 8765 --directory dist

Deployment output: dist/ (the directory containing index.html). No npm install command, build command, or environment variables. For plain static hosting, upload the contents of dist/ to the website document root.

Edit dist/data.js for topics, captions and source links. To regenerate downloads, run node export.mjs followed by python make_pdf.py with ReportLab installed. Source links identify clinical topics and further reading; they do not indicate clinician approval.
