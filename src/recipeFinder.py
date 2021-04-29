from random import randrange


class Recipe:
    def __init__(self, name, link, ings):
        self.name = name
        self.link = link
        self.ings = ings


def createRandom(file, file2):
    f = open(file, "r")
    ings = [ing.replace(";\n", "") for ing in f]
    f.close()
    ingsleng = len(ings)
    randIngs = ""
    numOfIngs = randrange(20, 50)
    for i in range(numOfIngs-1):
        randIngs += ings[randrange(ingsleng)]+', '
    randIngs += ings[randrange(ingsleng)]

    ings = randIngs.split(", ")
    recipes = pre_process(file2)
    possibleRec = []
    for recipe in recipes:
        pos = recipeCheck(recipe, ings)
        if pos != None:
            possibleRec.append(pos)

    return randIngs, possibleRec


def recipeData(file, ings):
    recipes = pre_process(file)
    ings = ings.split(",")
    currentRec = []
    for recipe in recipes:
        pos = recipeCheck(recipe, ings)
        if pos != None:
            currentRec.append(pos)
    newIngs = ['potato', 'enoki mushoom', 'onion', 'potatos', 'onions']
    userIngs = ings + newIngs
    possibleRec = []
    for recipe in recipes:
        pos = recipeCheck(recipe, userIngs)
        if pos != None:
            possibleRec.append(pos)
    uing = "potato, enoki mushoom, onion"
    return possibleRec, uing, currentRec


def recipeCheck(recipe, userIngs):
    for recIng in recipe.ings:
        for userIng in userIngs:
            if userIng in recIng:
                recipe.ings[recIng] = True
                break
    for recIng in recipe.ings:
        if not recipe.ings[recIng]:
            return
    return [recipe.name, recipe.link]


def pre_process(file):
    recipeDataBase = open(file, "r")
    recipes = []
    for line in recipeDataBase:
        line = line.split(';')
        name = line[1]
        link = line[2]
        temp = [ing for ing in line[3:] if ing != "" and ing != "\n"]
        ings = {}
        for ele in temp:
            ings[ele] = False
        recipes.append(Recipe(name, link, ings))
    recipeDataBase.close()
    return recipes
