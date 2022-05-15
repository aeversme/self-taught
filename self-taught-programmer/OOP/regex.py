import re

zen = """
The Zen of Python
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one--and preferably only one--obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea--let's do more of those!
"""

# find character/word matches
dutch = re.findall("dutch", zen, re.IGNORECASE)

# find matches at the beginning of a line
begin = re.findall("^If", zen, re.MULTILINE)

# match multiple characters
text = "Two turtles turned too."
mult = re.findall("t[ow]o", text, re.IGNORECASE)

# match digits; format is [[:digit:]] in bash
line = "123?34 hello?"
digits = re.findall("\d", line, re.IGNORECASE)

# greedy and non-greedy matching
under = "__one__ __two__ __three__"
g = re.findall("__.*__", under)
ng = re.findall("__.*?__", under)

# escaping characters
cash = "I love $"
money = re.findall("\\$", cash)

# practice
ghost = "The ghost that says boo haunts the loo."
oos = re.findall(".oo", ghost)

print(oos)
