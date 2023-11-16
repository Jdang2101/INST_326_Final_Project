import sys
import argparse
from gui.frontend import app


def main(gui_enabled: bool):
    """ The main function which will be executed when the script is run.

    Args:
        gui_enabled (bool): Whether or not the GUI is enabled.
    """

    # Check to see if the GUI is enabled.
    if gui_enabled:
        # If the GUI is enabled, then run the GUI code.
        app.run(debug=True)


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    
    # For the sake of readability it is important to insert comments all throughout.
    # Complicated operations get a few lines of comments before the operations commence. 
    # Non-obvious ones get comments at the end of the line.
    # For example:
    # This function uses the argparse module in order to parse command line arguments.
    
    parser = argparse.ArgumentParser() #Create an ArgumentParser object.
    
    # Then we will add arguments to this parser object.
    # In this case, we have a required positional argument.
    # Followed by an optional keyword argument which contains a default value.
    
    parser.add_argument('--gui', '-g', type=bool, default=False, help='Enable the GUI')  
    
    args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.

    return args


if __name__ == "__main__":
    # If name == main statements are statements that basically ask:
    # Is the current script being run natively or as a module?
    # It the script is being run as a module, the block of code under this will not be executed.
    # If the script is being run natively, the block of code below this will be executed.
    
    arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
    
    # The returned object is an object with those command line arguments as attributes of an object.
    # We will pass both of these arguments into the main function.
    # Note that you do not need a main function, but you might find it helpfull.
    # You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
    
    main(arguments.gui)
