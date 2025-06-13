import json, pdfkit
from jinja2 import Environment, FileSystemLoader

# Load resume data
with open('resume.json') as f:
    data = json.load(f)

# Load template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('modern.html')
output_html = template.render(data)

# Output PDF
pdfkit.from_string(output_html, 'output/resume.pdf')
print("✅ Resume generated successfully!")
