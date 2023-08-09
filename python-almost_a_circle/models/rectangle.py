"""
Rectangle class

This class represents a rectangle.

**Attributes:**

* **width** (int): The width of the rectangle.
    * **Raises** `TypeError` if `width` is not an integer.
    * **Raises** `ValueError` if `width` is less than or equal to 0.
* **height** (int): The height of the rectangle.
    * **Raises** `TypeError` if `height` is not an integer.
    * **Raises** `ValueError` if `height` is less than or equal to 0.
* **x** (int): The x coordinate of the rectangle.
    * **Raises** `TypeError` if `x` is not an integer.
    * **Raises** `ValueError` if `x` is less than or equal to 0.
* **y** (int): The y coordinate of the rectangle.
    * **Raises** `TypeError` if `y` is not an integer.
    * **Raises** `ValueError` if `y` is less than or equal to 0.

**Methods:**

* **__init__(width, height, x=0, y=0, id=None)**:
    Initialize a new rectangle.
    * **Arguments:**
        * `width`: The width of the rectangle.
        * `height`: The height of the rectangle.
        * `x`: The x coordinate of the rectangle.
        * `y`: The y coordinate of the rectangle.
        * `id`: The ID of the rectangle.
    * **Raises** `TypeError` if `width` is not an integer.
    * **Raises** `ValueError` if `width` is less than or equal to 0.
    * **Raises** `TypeError` if `height` is not an integer.
    * **Raises** `ValueError` if `height` is less than or equal to 0.
    * **Raises** `TypeError` if `x` is not an integer.
    * **Raises** `ValueError` if `x` is less than or equal to 0.
    * **Raises** `TypeError` if `y` is not an integer.
    * **Raises** `ValueError` if `y` is less than or equal to 0.

* **width** (self):
    Get the width of the rectangle.
    * **Returns:** The width of the rectangle.

* **width** (self, value):
    Set the width of the rectangle.
    * **Arguments:**
        * `value`: The new width of the rectangle.
    * **Raises** `TypeError` if `value` is not an integer.
    * **Raises** `ValueError` if `value` is less than or equal to 0.

* **height** (self):
    Get the height of the rectangle.
    * **Returns:** The height of the rectangle.

* **height** (self, value):
    Set the height of the rectangle.
    * **Arguments:**
        * `value`: The new height of the rectangle.
    * **Raises** `TypeError` if `value` is not an integer.
    * **Raises** `ValueError` if `value` is less than or equal to 0.

* **x** (self):
    Get the x coordinate of the rectangle.
    * **Returns:** The x coordinate of the rectangle.

* **x** (self, value):
    Set the x coordinate of the rectangle.
    * **Arguments:**
        * `value`: The new x coordinate of the rectangle.
    * **Raises** `TypeError` if `value` is not an integer.
    * **Raises** `ValueError` if `value` is less than or equal to 0.

* **y** (self):
    Get the y coordinate of the rectangle.
    * **Returns:** The y coordinate of the rectangle.

* **y** (self, value):
    Set the y coordinate of the rectangle.
    * **Arguments:**
        * `value`: The new y coordinate of the rectangle.
    * **Raises** `TypeError` if `value` is not an integer.
    * **Raises** `ValueError` if `value` is less than or equal to 0.

* **__validate_width** (self, width):
    Validator for the width attribute.
    * **Arguments:**
        * `width`: The width of the rectangle.
    * **Raises** `TypeError` if `width
