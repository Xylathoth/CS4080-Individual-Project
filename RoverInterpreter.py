# Exception for syntax errors
class SyntaxError(Exception):
    pass

# Exception for runtime errors
class RuntimeError(Exception):
    pass

class RoverInterpreter:
    def __init__(self):
        # Rover's inital state: position (x, y) and direction
        self.x = 0
        self.y = 0
        self.direction = 'NORTH'
        self.directions = ['NORTH', 'EAST', 'SOUTH', 'WEST']  # Clockwise rotation order of possible directions

    # Parse command strings into action and argument values
    def parse(self, command):
        parts = command.strip().split()
        if not parts:
            raise SyntaxError("Empty command.")

        action = parts[0]
        args = parts[1:]
        return action, args

    # Execute a list of commands for rover's movement
    def execute(self, commands):
        for command in commands:
            action, args = self.parse(command)
            if action == 'MOVE':
                self.move(args)
            elif action == 'TURN':
                self.turn(args)
            elif action == 'REPORT':
                self.report()
            else:
                raise SyntaxError(f"Unknown command: {action}")

    # Moves rover in current direction
    def move(self, args):
        if len(args) != 1 or not args[0].isdigit():
            raise SyntaxError("MOVE requires a single numeric argument.")

        distance = int(args[0])
        if self.direction == 'NORTH':
            self.y += distance
        elif self.direction == 'EAST':
            self.x += distance
        elif self.direction == 'SOUTH':
            self.y -= distance
        elif self.direction == 'WEST':
            self.x -= distance

    # Turns the rover left or right
    def turn(self, args):
        if len(args) != 1 or args[0] not in ['LEFT', 'RIGHT']:
            raise SyntaxError("TURN requires a single argument: LEFT or RIGHT.")

        if args[0] == 'LEFT':
            self.direction = self.directions[(self.directions.index(self.direction) - 1)]
        elif args[0] == 'RIGHT':
            self.direction = self.directions[(self.directions.index(self.direction) + 1)]

    # Prints rover's current position and direction
    def report(self):
        print(f"Position: ({self.x}, {self.y}), Direction: {self.direction}")

# Main method containing rover instructions
def main():
    interpreter = RoverInterpreter()
    instructions = [
        "MOVE 10",
        "TURN LEFT",
        "MOVE 5",
        "REPORT",
    ]

    # Try-except block for running program and printing errors 
    try:
        interpreter.execute(instructions)
    except (SyntaxError, RuntimeError) as e:
        print(f"Error: {e}")

# Run program
if __name__ == "__main__":
    main()