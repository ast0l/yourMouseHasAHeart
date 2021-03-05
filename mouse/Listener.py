import abc


class Listener(abc.ABC):

    def listener_mouse_scroll(self) -> None:
        """listen the mouse scroll action"""
        pass

    @abc.abstractmethod
    def listener_mouse_click(self, x, y, button, pressed) -> None:
        """listen the mouse click action"""
        pass

    @abc.abstractmethod
    def listener_mouse_movement(self, events: object, original_axes: tuple) -> None:
        """listen the mouse movement"""
        pass
