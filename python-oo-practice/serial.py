"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """

    def __init__(self, start=0):
        """Initialize generator with a given start number"""
        self.start = self.next = start

    def __repr__(self):
        """Class representation."""
        return f"Serial Generator starting with number {self.start}"

    def generate(self):
        """Generate next number."""
        self.next +=1
        return self.next - 1 

    def reset(self):
        """Reset number to original value."""
        self.next = self.start
         

