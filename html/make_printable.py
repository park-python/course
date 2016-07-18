#!/usr/bin/env python
import sys

replacement = """
        <script>
            var link = document.createElement( 'link' );
            link.rel = 'stylesheet';
            link.type = 'text/css';
            link.href = window.location.search.match( /print-pdf/gi ) ? 'css/print/pdf.css' : 'css/print/paper.css';
            document.getElementsByTagName( 'head' )[0].appendChild( link );
        </script>
    </body>
"""

if __name__ == "__main__":
    file_name = sys.argv[1]

    with open(file_name, "r") as f:
        content = f.read()

    new_content = content.replace("</body>", replacement)

    with open(file_name, "w") as f:
        f.write(new_content)
