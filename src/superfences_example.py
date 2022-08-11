import markdown

MD = """
```terraform
x = <<EOF
    {}
 EOF
```
"""
print(markdown.markdown(MD, extensions=["pymdownx.superfences"]))
