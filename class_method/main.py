class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self,name,age,tracks,score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score


    def change_name(self,newname):
        self.name=newname
        print(self.name)

    def change_age(self,newage):
        self.age=int(newage)
        print(self.age)

    def add_track(self,newtracks):   
        self.tracks.append(newtracks)
        print(self.tracks)

    def get_score(self):
        print(self.score)
        return self.score
    



Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()
