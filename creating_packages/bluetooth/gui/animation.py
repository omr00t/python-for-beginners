
def animate1():
    print("animate1 has been called.")

def animate2():
    print("animate2 has been called.")

def animate3():
    animate4()

def animate4():
    _internal_animate()

def _internal_animate():
    """
    This is an internal function that should not be called from 
    the module user.
    """
    print("_internal_animate has been called.")

if __name__ == "bluetooth.gui.animation":
    print("The animation module has been imported!")
