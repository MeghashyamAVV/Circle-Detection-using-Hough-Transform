# Circle-Detection-using-Hough-Transform


This code uses OpenCV library to detect circles in an image using the Hough Transform. The code first reads an image file and creates a copy of it. Then, using cv2.cvtColor function, it converts the image from color to grayscale. The cv2.HoughCircles function is then used to detect circles in the grayscale image. The function takes several parameters, including the minimum and maximum radius of the circles to be detected, as well as the minimum distance between circles.

If circles are detected, the code draws green circles around each detected circle using the cv2.circle function. The resulting image is displayed using cv2.imshow function. This technique can be useful in a variety of applications, such as object detection, tracking, and computer vision. By detecting circles in an image, this code can help identify and analyze circular objects in an automated and efficient manner.
