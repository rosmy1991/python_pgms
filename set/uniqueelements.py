all=["mohan","fahad","dq","vijay","nivin","asif"]
dq_f=["mohan","fahad","asif"]
suggestions=set(all).difference(set(dq_f))
suggestions.remove("dq")
print(suggestions)