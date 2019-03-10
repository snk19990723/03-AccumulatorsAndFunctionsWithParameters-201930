"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Deng Zou.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:
    # two_circles()
    # circle_and_rectangle()
    lines()

def two_circles():

    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # -------------------------------------------------------------------------
    window=rg.RoseWindow(400,400)
    circle = rg.Circle(rg.Point(200,200), 40)
    circle.fill_color='red'
    circle.attach_to(window)
    circle2=rg.Circle(rg.Point(100,100),50)
    circle2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # -------------------------------------------------------------------------
    # DONE: 3. Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # -------------------------------------------------------------------------
    window = rg.RoseWindow(400, 400)
    center_point1=rg.Point(100, 100)
    circle = rg.Circle(center_point1, 40)
    circle.fill_color = 'blue'
    circle.outline_thickness= '1'
    circle.attach_to(window)
    print('1')
    print('blue')
    print('Point (100,100)')
    print('100')
    print('100')

    point1 = rg.Point(300, 100)
    point2 = rg.Point(200, 400)
    rectangle = rg.Rectangle(point1,point2)
    rectangle.outline_thickness='10'
    print('10')
    print('none')
    print('Point (250,250)')
    print('250')
    print('250')
    rectangle.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # TODO: 4. Implement and test this function.
    window=rg.RoseWindow(500,500)
    p1=rg.Point(0,50)
    p2=rg.Point(450,50)
    line1=rg.Line(p1,p2)
    line1.thickness='5'
    midp=line1.get_midpoint()
    print(midp)
    print('225')
    print('50')

    p3 = rg.Point(10, 350)
    p4 = rg.Point(600, 350)
    line2=rg.Line(p3,p4)
    line2.defaults

    line1.attach_to(window)
    line2.attach_to(window)
    window.render()
    window.close_on_mouse_click()

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
