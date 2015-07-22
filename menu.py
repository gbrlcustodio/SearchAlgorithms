from time import sleep
import curses, os # Curses is the interface for capturing key presses on the menu, os launches the files

class Menu:
    def __init__(self, graph, dijkstra, a_star):
        self.MENU = "menu"
        self.COMMAND = "command"
        self.EXITMENU = "exitmenu"

        self.screen = curses.initscr() # Initializes a new window for capturing key presses
        self._graph = graph
        self._dijkstra = dijkstra
        self._a_star = a_star

        self.menu_data = {
            'title': "Artificial Intelligence - Search Algorithms", 'type': self.MENU, 'subtitle': "Please select an option...",
                'options':[
                    { 'title': "Print graph data", 'type': self.COMMAND, 'command': 'print_graph' },
                    { 'title': "Run Dijkstra algorithm", 'type': self.COMMAND, 'command': 'dijkstra' },
                    { 'title': "Run A-Star algorithm", 'type': self.COMMAND, 'command': 'a_star' },
                ]
        }

    def runmenu(self, menu, parent):
        # Work out what text to display as the last menu option
        if parent is None:
            lastoption = "Exit"
        else:
            lastoption = "Return to %s menu" % parent['title']

        optioncount = len(menu['options']) # how many options in this menu

        # pos is the zero-based index of the hightlighted menu option.
        # Every time runmenu is called, position returns to 0,
        # when runmenu ends the position is returned and tells the program what opt$
        pos = 0
        # Used to prevent the screen being redrawn every time
        oldpos = None
        # Control for while loop, let's you scroll through options until return key is pressed then returns pos to program
        x = None

        # Loop until return key is pressed
        while x != ord('\n'):
            if pos != oldpos:
                oldpos = pos
                self.screen.border(0)
                self.screen.addstr(2, 2, menu['title'], curses.A_STANDOUT) # Title for this menu
                self.screen.addstr(4, 2, menu['subtitle'], curses.A_BOLD) # Subtitle for this menu

            # Display all the menu items, showing the 'pos' item highlighted
            for index in range(optioncount):
                textstyle = self.n
                if pos == index:
                    textstyle = self.h
                self.screen.addstr(5 + index, 4, "%d - %s" % (index + 1, menu['options'][index]['title']), textstyle)
                # Now display Exit/Return at bottom of menu
                textstyle = self.n
                if pos == optioncount:
                    textstyle = self.h
                self.screen.addstr(5 + optioncount, 4, "%d - %s" % (optioncount + 1, lastoption), textstyle)
                self.screen.refresh()
                # finished updating screen

            x = self.screen.getch() # Gets user input

            # What is user input?
            if x >= ord('1') and x <= ord(str(optioncount + 1)):
                pos = x - ord('0') - 1 # Convert keypress back to a number, then subtract 1 to get index
            elif x == 258: # Down arrow
                if pos < optioncount:
                    pos += 1
                else:
                    pos = 0
            elif x == 259: # Up arrow
                if pos > 0:
                    pos += -1
                else:
                    pos = optioncount

        # Return index of the selected item
        return pos

    def processmenu(self, menu, parent = None):
        optioncount = len(menu['options'])
        exitmenu = False

        while not exitmenu: #Loop until the user exits the menu
            getin = self.runmenu(menu, parent)

            if getin == optioncount:
                exitmenu = True
            elif menu['options'][getin]['type'] == self.COMMAND:
                curses.def_prog_mode()    # Save curent curses environment
                os.system('reset')
                if menu['options'][getin]['command'] == 'print_graph':
                    self._graph.print_data()
                elif menu['options'][getin]['command'] == 'dijkstra':
                    self._dijkstra.run()
                    print('Iterations: %d' % self._dijkstra.iterations)
                    print('Comparison: %d' % self._dijkstra.comparison)
                    print('Moviments: %d' % self._dijkstra.moviments)
                elif menu['options'][getin]['command'] == 'a_star':
                    self._a_star.run()
                    print('Iterations: %d' % self._a_star.iterations)
                    print('Comparison: %d' % self._a_star.comparison)
                    print('Moviments: %d' % self._a_star.moviments)

                print('Press ENTER key to return.')
                input()
                self.screen.clear() # Clears previous screen on key press and updates display based on pos
                curses.reset_prog_mode()   # Reset to 'current' curses environment
                curses.curs_set(1)         # Reset doesn't do this right
                curses.curs_set(0)
            elif menu['options'][getin]['type'] == self.MENU:
                self.screen.clear() # Clears previous screen on key press and updates display based on pos
                processmenu(menu['options'][getin], menu) # display the submenu
                self.screen.clear() # Clears previous screen on key press and updates display based on pos
            elif menu['options'][getin]['type'] == self.EXITMENU:
                exitmenu = True

    def run(self):
        curses.noecho() # Disables automatic echoing of key presses (prevents program from input each key twice)
        curses.cbreak() # Disables line buffering (runs each key as it is pressed rather than waiting for the return key to pressed)
        curses.start_color() # Lets you use colors when highlighting selected menu option
        self.screen.keypad(1) # Capture input from keypad

        # Change this to use different colors when highlighting
        curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE) # Sets up color pair #1, it does black text with white background
        self.h = curses.color_pair(1) # h is the coloring for a highlighted menu option
        self.n = curses.A_NORMAL # n is the coloring for a non highlighted menu option

        self.processmenu(self.menu_data)

    def __del__(self):
        curses.endwin() #VITAL! This closes out the menu system and returns you to the bash prompt.
        os.system('clear')
