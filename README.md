



run api.py


# Indian-Sign-Language-Recognition
#### Sign Languages are a set of languages that use predefined actions and movements to convey a message. These languages are primarily developed to aid deaf and other verbally challenged people. They use a simultaneous and precise combination of movement of hands, orientation of hands, hand shapes etc. Different regions have different sign languages like American Sign Language, Indian Sign Language etc. We focus on Indian Sign language in this project.Indian Sign Language (ISL) is a sign language that is predominantly used in South Asian countries. It is sometimes referred to as Indo-Pakistani Sign Language (IPSL). There are many special features present in ISL that distinguish it from other Sign Languages. Features like Number Signs, Family Relationship, use of space etc. are crucial features of ISL. Also, ISL does not have any temporal inflection.
#### ![alt text](https://github.com/yatharth77/Indian-Sign-Language-Gesture-Recognition/blob/master/isl.png?raw=true)

## Technologies
Project is created with:
* Numpy
* Pandas
* Sklearn
* Opencv
* TensorflowLorem version: 12.3
## Image Preprocessing
#### The main objective of the segmentation phase is to remove the background and noises, leaving only the Region of Interest (ROI), which is the only useful information in the image. This is achieved via Skin Masking defining the threshold on RGB schema and then converting RGB colour space to grey scale image. Finally Canny Edge technique is employed to identify and detect the presence of sharp discontinuities in an image, thereby detecting the edges of the figure in focus.

#### ![alt text](https://www.researchgate.net/publication/235755964/figure/fig3/AS:216357342846978@1428595018120/Preprocessing-for-hand-recognition-a-the-side-view-of-the-hand-a1-Gaussian-filter.png)

## Classification
#### CNNs have broken the mold and ascended the throne to become the state-of-the-art computer vision technique. Among the different types of neural networks (others include recurrent neural networks (RNN), long short term memory (LSTM), artificial neural networks (ANN), etc.), CNNs are easily the most popular.These convolutional neural network models are ubiquitous in the image data space. They work phenomenally well on computer vision tasks like image classification, object detection, image recognition, etc.Once a CNN is built, it can be used to classify the contents of different images. All we have to do is feed those images into the model. Just like ANNs, CNNs are inspired by the workings of the human brain. CNNs are able to classify images by detecting features, similar to how the human brain detects features to identify objects.

#### ![alt text](https://media.springernature.com/lw685/springer-static/image/art%3A10.1007%2Fs00500-020-04860-5/MediaObjects/500_2020_4860_Fig7_HTML.png)

## Interface
#### Input Feature
#### ![alt text](https://drive.google.com/file/d/1oKb0zKf0V-Se4m3ftbB3TG_zMdKcVahu/view)

