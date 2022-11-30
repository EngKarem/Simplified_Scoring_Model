class Project:
    def __init__(self):
        self.scores = []

    def setScore(self, value):
        self.scores.append(value)

    def getScore(self):
        return self.scores


class Model:
    def __init__(self, Type):
        self.Type = Type

    def CreateModel(self):
        if self.Type == 'ssm':
            criteria_number = int(input("Enter number of criteria"))
            projects_number = int(input("Enter number of Projects"))
            importanceWeights = []
            Projects = []
            Weighed_scores = []
            Sum = 0
            for i in range(criteria_number):
                Imp_Weight = int(input(f"Enter importance Weight No.{i + 1} "))
                importanceWeights.append(Imp_Weight)

            for i in range(projects_number):
                project = Project()
                print(f"Project No.{i + 1}")
                for j in range(criteria_number):
                    score = int(input())
                    project.setScore(score)
                Projects.append(project.getScore())

            for i in range(projects_number):
                for j in range(criteria_number):
                    Sum += Projects[i][j] * importanceWeights[j]
                Weighed_scores.append(Sum)
                Sum = 0

            print(Weighed_scores)
            max = Weighed_scores[0]
            i = 1
            for i in range(1, len(Weighed_scores)):
                if Weighed_scores[i] < max:
                    max = Weighed_scores[i]
            print(f"Project {i+1} represents the best choice, using the weighted scoring model")


model = Model("ssm")
model.CreateModel()
