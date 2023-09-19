import json
from simon import simon
from mark import mark
from jamie import jamie

# --------------------------------------------------

def get_current_location(story, current, current_location):
  for passage in story["passages"]:
    if current == passage["pid"]:
      return passage
  return current_location



# --------------------------------------------------


def render(passage, moves, score, endings):
  print("\nMoves: \u001b[31m" + str(moves) + "\u001b[37m Score: \u001b[31m" + str(score) + "\u001b[37m Endings: \u001b[31m" + str(endings) + "\u001b[37m \n")
  print(passage["name"])
  print(passage["text"])
  print("\nChoose one of the following:")
  for link in passage["links"]:
    print("(" + link["selection"] + ") \u001b[36m" + link["label"] + "\u001b[31m ")
  print()


# --------------------------------------------------


def get_input():
  response = input("\u001b[32mWhat do you want to do?\u001b[37m(type quit to exit) ")
  return response
    


# --------------------------------------------------


def update(passage):
  current = ""
  for link in passage["links"]:
    if response == link["selection"]:
      current = link["pid"]
  if current == "":
    print("Please try again, I didn't understand what you tried to do")
  return current


# --------------------------------------------------


quit = False
while not quit:
  world = {}
  while world == {}:
    print("(1) " + simon["story"])
    print("(2) " + mark["story"])
    print("(3) " + jamie["story"])
    selection = input("A lakeside party amidst whispering trees. Laughter and music fill the air as a group of eager freshmen gather for a night of revelry by Griffy Lake. As the sun dips below the horizon, the atmosphere shifts. Shadows lengthen, and with each passing hour, the group dwindles. Stay vigilant as the joyous evening turns into a chilling ordeal, and the true nature of the darkness emerges.\nWho would you like to play as? Input number: "
)
    if selection == "1":
      world = simon
    elif selection == "2":
      world = mark
    elif selection == "3":
      world = jamie

  print("\nYou are playing " + world["story"])

  current = world["startnode"]
  current_location = {}
  moves = 0
  score = 0
  endings = 0
  
  while True:
    current_location = get_current_location(world,current, current_location)
    render(current_location, moves, score, endings)
    response = get_input()
    if response == "quit":
      break
    current = update(current_location)
    moves = moves + 1
    if "score" in current_location:
      score += current_location["score"]
    if "end" in current_location:
      endings += current_location["end"]
    
  if score == 100:
        print("Game won. You found all the favorable endings")
  print("Thanks for playing!\n\n")
  asking = True
  while asking:
    selection = input("Restart for alternative endings (y/n) ")
    if selection.lower() == "n":
      quit = True
      asking = False
    elif selection.lower() == "y":
      asking = False
