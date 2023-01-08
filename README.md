_The final project for IT-140 at Southern New Hampshire University._

__________________________

### PROJECT REQUIREMENTS:

+ Create a new file in PyCharm and title it “TextBasedGame.py"
+ You must develop all of your code in one Python file
+ Develop a navigation function that can: 
  + Show the player the different commands they can enter
  + Show the player’s status by:
    + identifying the room they are currently in
    + showing a list of their inventory of items
    + displaying the item in their current room
+ Create a dictionary linking rooms to one another and linking items to their corresponding rooms.
+ Develop a main function that will contain the overall gameplay functionality.
  + The bulk of it should include a loop for the gameplay
    + Within the gameplay loop, there should be decision branching for player input. Be sure to include:
      + Input validation
      + What happens if the player enters a command to move between rooms
      + What happens if the player enters a valid command to get an item from the room
    + The gameplay should continue looping until the player has either won or lost the game
+ The player wins the game by retrieving all of the items before encountering the room with the villain
+ The player loses the game by moving to the room with the villain before collecting all of the items
