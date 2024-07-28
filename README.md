
#  Python-Video-Generator

Creates a maximum of 10 videos at a time containing dad jokes in the format of YouTube shorts or Instagram reels.

 The code provides insights into integrating external APIs, image manipulation, and video creation using Python libraries like requests and OpenCV.


## Working

1. The code starts by importing necessary libraries such as cv2 for OpenCV image and video processing, os for operating system functions, random for random    selection, textwrap for text formatting, and requests for making HTTP requests.

2. The fourcc is set to specify the codec for video writing (MP4 in this case), and height and width are defined for the video dimensions.

3. The length variable specifies the length of the generated video in seconds, and number_of_videos indicates how many videos should be created.

4. Using a regular expression, The simplify_text function replaces Unicode escape sequences in text.

5. The API_Call function makes a request to an API that provides dad jokes. The jokes are retrieved and processed for further use.

6. The Jokes variable stores the list of dad jokes obtained from the API.

7. The textFormater function uses the simplify_text function and wraps the text into smaller chunks using textwrap.TextWrapper.

8. The imagePathGenerator function generates paths of background images by walking through the specified directory.

9. The image_to_video function is the core of the video creation process. It iterates over the number of videos specified and performs the following steps:

   - Select a random background image path.
   - Initializes a VideoWriter object to write the video.
   - Write the same image with text into the video multiple  times for each frame, creating the illusion of a longer video.
   - The code employs OpenCV's cv2 functions for tasks like reading images, overlaying text, and writing video frames. This showcases the capabilities of OpenCV in image and video manipulation.

10. Finally, the image_to_video function generates the videos based on the provided parameters.
#

It is important to ensure that the background images have the same dimensions as specified in the code (1080x1920), otherwise, the output videos will be corrupted. 

Remember to replace placeholders like 'YOUR API KEY' and adjust file paths to match your own environment. 

