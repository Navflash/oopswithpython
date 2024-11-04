
class Repo():
    def __init__(self,name):
        self.name = name
        self.files = []

    def add(self,file):
        self.files.append(file)


class Commit():
    def __init__(self,name,author):
        self.name = name
        self.author = author

Git = Repo("college_project")

f1 = Commit("main.cpp","dev1")
f2 = Commit("header.h","dev2")

Git.add(f1)
Git.add(f2)

for f in Git.files:
    print(f"{f.name} by {f.author}")