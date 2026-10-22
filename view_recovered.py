from pathlib import Path
import html

source = Path("recovered_deleted_chat.txt")
output = Path("recovered_chat_view.html")

text = source.read_text(encoding="utf-8", errors="replace")

page = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Recovered ChatGPT Data</title>
<style>
body {{
    font-family: Arial, sans-serif;
    max-width: 1000px;
    margin: 40px auto;
    background: #212121;
    color: #ececec;
}}

h1 {{
    border-bottom: 1px solid #555;
    padding-bottom: 15px;
}}

.data {{
    background: #2f2f2f;
    border-radius: 12px;
    padding: 25px;
    white-space: pre-wrap;
    word-wrap: break-word;
    line-height: 1.6;
}}
</style>
</head>

<body>

<h1>Recovered ChatGPT Heap Data</h1>

<div class="data">
{html.escape(text)}
</div>

</body>
</html>
"""

output.write_text(page, encoding="utf-8")

print("Created:", output.resolve())