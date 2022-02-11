import itertools
s=str(input())
st=set()
for string in itertools.permutations(s):
    st.add("".join(string))
print(len(st))
