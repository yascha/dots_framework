from colorama import Fore

class Colours:
    RED = 0
    BLUE = 1
    GREEN = 2
    YELLOW = 3
    PURPLE = 4

    NUM_COLOURS = 5

    chars = {
                RED : 'r',
                BLUE : 'b',
                GREEN : 'g',
                YELLOW : 'y',
                PURPLE : 'p'
            } 

    escapes = {
                RED : Fore.RED,
                BLUE : Fore.BLUE,
                GREEN : Fore.GREEN,
                YELLOW : Fore.YELLOW,
                PURPLE : Fore.MAGENTA
               }

    def colour(self, colour):
        """Takes a numerical colour and returns a coloured char to represent it
        
        """
        return Colours.escapes[colour] + Colours.chars[colour] + Fore.RESET