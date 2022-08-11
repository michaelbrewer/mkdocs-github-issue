from pygments import highlight
from pygments.lexers.configs import TerraformLexer
from pygments.formatters import HtmlFormatter


code = """
x = <<EOF
    {}
 EOF
"""
print(highlight(code, TerraformLexer(), HtmlFormatter()))
