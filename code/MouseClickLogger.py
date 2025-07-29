import time
from pynput import mouse
import pyautogui

def save_mouse_position_on_click(filename: str = "mouse_positions.txt") -> None:
    """
    Save the mouse position and screen size to a file when the left mouse button is clicked.

    Args:
        filename (str): The name of the file to save the mouse positions. Defaults to "mouse_positions.txt".
    """
    def on_click(x: int, y: int, button: mouse.Button, pressed: bool) -> None:
        """
        Callback function for mouse click events.

        Args:
            x (int): The x-coordinate of the mouse click.
            y (int): The y-coordinate of the mouse click.
            button (mouse.Button): The mouse button that was clicked.
            pressed (bool): Whether the button was pressed or released.
        """
        if button == mouse.Button.left and pressed:
            screenWidth, screenHeight = pyautogui.size()
            print('Screen size: (%s, %s), Mouse position: (%s, %s)' % (screenWidth, screenHeight, x, y))
            with open(filename, 'a') as file:
                file.write('Screen size: (%s, %s), Mouse position: (%s, %s)\n' % (screenWidth, screenHeight, x, y))
            time.sleep(2)  # Wait for 2 seconds to allow repositioning

    try:
        with mouse.Listener(on_click=on_click) as listener:
            listener.join()
    except KeyboardInterrupt:
        print('Ended')
    except Exception as e:
        print('An error occurred:', e)
        print('Ended')

if __name__ == "__main__":
    save_mouse_position_on_click()