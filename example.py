import re

text = """
Adfrt56 tratratyob dfsf werwe!
Rtrtu dfhjke uuu23.
"""

print(re.findall('[a-zA-Z]+', text))