import unittest
import os
from polybot.img_proc import Img

# Define your test cases by subclassing unittest.TestCase
class TestImgConcat(unittest.TestCase):

    # Set up any necessary resources or state before each test method
    def setUp(self):
        # Construct the path to the test image
        current_dir = os.path.dirname(os.path.abspath(__file__))
        img_path = os.path.join(current_dir, 'beatles.jpeg')
        # Initialize an Img instance with the test image
        self.img = Img(img_path)
        self.original_dimension = (len(self.img.data), len(self.img.data[0]))

    # Define test methods starting with "test_"
    def test_rotation_dimension(self):
        # Perform the rotation operation
        self.img.rotate()
        # Assert the expected dimension after rotation
        actual_dimension = (len(self.img.data), len(self.img.data[0]))
        self.assertEqual(self.original_dimension, actual_dimension[::-1])

    def test_360_rotation(self):
        # Perform two rotations (360 degrees)
        self.img.rotate()
        self.img.rotate()
        # Prepare the expected rotated image
        rotated_image = [row[::-1] for row in self.img.data]
        expected_img = [row[::-1] for row in rotated_image]
        # Assert that the rotated image matches the expected image
        self.assertEqual(expected_img, self.img.data)

# Define a main function to run the tests
def main():
    unittest.main()

# Check if the script is executed directly and run the tests
if __name__ == '__main__':
    main()






    def show(self):
        from matplotlib import pyplot as plt
        plt.imshow(self.data, cmap='gray')
        plt.axis('off')
        plt.show()

# Define the path to the image
pic_path = r'..\polybot\test\beatles.jpeg'
pic_path_2 = r'C:\Users\Alex\Desktop\images\Cat.jpg'

checky = Img(pic_path)
checky2 = Img(pic_path_2)
# Call the rotate method to rotate and display the image
checky.rotate()

# Segment the image
segmented_image = checky.segment()
segmented_image.show()

# salt_n_pepper the image
checky.salt_n_pepper()
checky.show()

# concat the image
checky.concat(checky2)
checky.show()
