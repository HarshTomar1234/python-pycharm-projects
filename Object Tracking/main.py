
"""
Object tracking is a computer vision process that involves locating and following the movement of objects across frames in a video sequence.
It is a crucial task in various applications such as surveillance, autonomous vehicles, medical imaging, and robotics.
 Here is a detailed guide to object tracking:

### Steps in Object Tracking

1. **Target Initialization**:
   - Define the number of targets and the objects of interest.
   - Identify the object of interest by drawing a bounding box around it in the first frame.
   - This can be done manually or automatically using object detectors.

2. **Appearance Modeling**:
   - Model the visual appearance of the object to handle changes in lighting, angles, and speeds.
   - This involves constructing robust object descriptions using visual features and building effective mathematical models for object identification using statistical learning techniques.

3. **Motion Estimation**:
   - Use predictors like linear regression, Kalman filters, or particle filters to predict the future position of the object.
   - This is a dynamic state estimation problem that helps the algorithm to track the object accurately.

4. **Target Positioning**:
   - Use the predicted position to pinpoint the exact location of the target.
   - This is typically done using a greedy search or maximum posterior estimation based on motion estimation.

### Deep Learning Algorithms for Object Tracking

1. **DeepSORT**:
   - An extension of the Simple Online Real-time Tracker (SORT) that uses deep learning to improve object tracking.
   - It combines object detection, prediction, and association to track objects accurately.

2. **Other Algorithms**:
   - There are various other deep learning algorithms used for object tracking, including YOLOv4, DeepSort, and Tensorflow implementations.

### Challenges in Object Tracking

1. **Occlusion**:
   - Occlusion occurs when the object is partially or fully hidden by other objects or the background.
   - This can be addressed by implementing occlusion sensitivity and using datasets with sparse backgrounds.

2. **Background Noise**:
   - Densely populated backgrounds can make it difficult to extract features and track objects.
   - Using well-curated datasets and background subtraction techniques can help mitigate this issue.

3. **Computational Efficiency**:
   - Object tracking algorithms can be computationally intensive, especially when dealing with high-resolution videos.
   - Optimizing the algorithms and using efficient hardware can help improve performance.

### Applications of Object Tracking

1. **Autonomous Vehicles**:
   - Object tracking is used in self-driving cars to detect obstacles, pedestrians, and other vehicles.

2. **Surveillance**:
   - Object tracking is used in surveillance systems to monitor subjects and activities captured by cameras.

3. **Retail**:
   - Object tracking is used in retail to track customers and items they pick up.

4. **Sports Analytics**:
   - Object tracking is used in sports to track the trajectory of balls, players, and other objects.

### Tools and Libraries for Object Tracking

1. **OpenCV**:
   - OpenCV is a popular computer vision library that provides tools for object tracking.

2. **SiamMask**:
   - SiamMask is a fast online object tracking algorithm that uses a siamese network to track objects.

3. **Roboflow**:
   - Roboflow is a platform that provides tools and datasets for object tracking and other computer vision tasks.

4. **DeepSort**:
   - DeepSort is a popular object tracking algorithm that uses deep learning to track objects accurately.

### Conclusion

Object tracking is a complex task that involves various steps and algorithms. Understanding the different methods and challenges involved in object tracking can help in developing more accurate and efficient tracking systems.
"""



"""

# Deep Sort 

Deep SORT (Simple Online and Realtime Tracking with a Deep Association Metric) is a state-of-the-art algorithm 
for multi-object tracking (MOT) in video sequences. It extends the original SORT (Simple Online Realtime Tracking) algorithm 
by incorporating deep learning techniques to improve tracking accuracy and robustness. Here is a detailed explanation of Deep SORT:

### Key Components

1. **Object Detection**:
   - Deep SORT starts with object detection using a convolutional neural network (CNN) like YOLO (You Only Look Once) to identify objects within a frame.
   - Each detection is associated with a high-dimensional appearance descriptor extracted by another CNN.

2. **Appearance Descriptors**:
   - These descriptors encode the appearance of the detected objects and are used for matching.
   - The appearance descriptors are learned offline using a large-scale person re-identification dataset.

3. **Kalman Filter**:
   - Deep SORT uses a Kalman filter for state prediction, similar to the original SORT algorithm.
   - The Kalman filter predicts the future position of the objects and corrects the association based on the actual measurements.

4. **Data Association**:
   - Deep SORT introduces a deep association metric that combines both motion and appearance descriptors.
   - This metric is used to associate detections with existing tracks, minimizing identity switches and improving tracking accuracy.

### How Deep SORT Works

1. **Detection and Feature Extraction**:
   - The algorithm detects objects in each frame using a CNN-based detector like YOLO.
   - For each detection, a high-dimensional appearance descriptor is extracted using another CNN.

2. **State Prediction**:
   - The Kalman filter predicts the future position of the objects based on their past motion.

3. **Data Association**:
   - The algorithm computes a cost matrix based on the intersection-over-union (IOU) distance between each detection and all predicted bounding boxes from the existing targets.
   - The assignment is solved optimally using the Hungarian algorithm.
   - If the IOU of detection and target is less than a certain threshold value called IOUmin, then that assignment is rejected.

4. **Track Creation and Deletion**:
   - Unique identities are created and destroyed according to the IOUmin.
   - Tracks are terminated if they are not detected for a certain number of frames (TLost).

### Advantages of Deep SORT

1. **Improved Tracking Accuracy**:
   - Deep SORT achieves state-of-the-art performance in multiple object tracking tasks due to its ability to handle occlusions and different viewpoints.

2. **Robustness to Occlusions**:
   - The deep association metric helps to recover identities after long-term occlusions when motion is less discriminative.

3. **Real-Time Performance**:
   - Deep SORT is designed for real-time tracking and can handle high-speed video streams.

### Applications of Deep SORT

1. **Surveillance**:
   - Deep SORT is used in surveillance systems to track people, vehicles, and other objects.

2. **Autonomous Vehicles**:
   - It is used in self-driving cars to track other vehicles, pedestrians, and obstacles.

3. **Sports Analytics**:
   - Deep SORT is used in sports to track players, balls, and other objects.

### Tools and Libraries for Deep SORT

1. **GitHub Repository**:
   - The official GitHub repository for Deep SORT provides the code and pre-trained models for implementation.

2. **Python Libraries**:
   - Deep SORT requires Python libraries like NumPy, scikit-learn, OpenCV, and TensorFlow for feature generation.

### Conclusion

Deep SORT is a powerful algorithm for multi-object tracking that combines the strengths of the SORT algorithm with deep learning techniques. Its ability to handle occlusions, maintain object identities, and perform in real-time makes it a valuable tool for various applications in computer vision and artificial intelligence.

"""

"""
Kalman Filter

The Kalman filter is a mathematical algorithm that uses a series of measurements observed over time, including statistical noise and other inaccuracies, to produce estimates of unknown variables that tend to be more accurate than those based on a single measurement alone. Here is a detailed explanation of the Kalman filter with mathematical derivations:

### Predict Phase

1. **State Prediction**:
   - The algorithm predicts the future state of the system based on the current state and the system dynamics.
   - The state prediction equation is given by:
     $$
     x_{k+1} = Ax_k + Bu_k + w_k
     $$
     where:
     - $$x_k$$ is the current state
     - $$A$$ is the state transition matrix
     - $$B$$ is the control input matrix
     - $$u_k$$ is the control input
     - $$w_k$$ is the process noise

2. **Error Covariance Prediction**:
   - The algorithm predicts the error covariance matrix based on the current error covariance and the system dynamics.
   - The error covariance prediction equation is given by:
     $$
     P_{k+1} = AP_kA^T + Q
     $$
     where:
     - $$P_k$$ is the current error covariance matrix
     - $$Q$$ is the process noise covariance matrix

### Update Phase

1. **Measurement Prediction**:
   - The algorithm predicts the measurement based on the predicted state and the measurement model.
   - The measurement prediction equation is given by:
     $$
     z_{k+1} = Hx_{k+1} + v_k
     $$
     where:
     - $$z_{k+1}$$ is the predicted measurement
     - $$H$$ is the measurement matrix
     - $$v_k$$ is the measurement noise

2. **Innovation**:
   - The algorithm computes the innovation, which is the difference between the actual measurement and the predicted measurement.
   - The innovation equation is given by:
     $$
     y_k = z_k - Hx_{k+1}
     $$
     where:
     - $$z_k$$ is the actual measurement

3. **Kalman Gain**:
   - The algorithm computes the Kalman gain, which is used to update the state estimate.
   - The Kalman gain equation is given by:
     $$
     K_k = P_{k+1}H^T(HP_{k+1}H^T + R)^{-1}
     $$
     where:
     - $$R$$ is the measurement noise covariance matrix

4. **State Update**:
   - The algorithm updates the state estimate using the Kalman gain and the innovation.
   - The state update equation is given by:
     $$
     x_{k+1} = x_{k+1} + K_ky_k
     $$
     where:
     - $$x_{k+1}$$ is the updated state estimate

5. **Error Covariance Update**:
   - The algorithm updates the error covariance matrix using the Kalman gain and the innovation.
   - The error covariance update equation is given by:
     $$
     P_{k+1} = (I - K_kH)P_{k+1}
     $$
     where:
     - $$I$$ is the identity matrix

### Mathematical Derivation

The Kalman filter can be derived using the Bayesian approach or the orthogonal projection method. Here is a brief overview of both methods:

#### Bayesian Approach

1. **Bayes' Theorem**:
   - The algorithm uses Bayes' theorem to update the state estimate based on the measurement.
   - The Bayes' theorem equation is given by:
     $$
     p(x_k|z_{1:k}) = \frac{p(z_k|x_k)p(x_k|z_{1:k-1})}{p(z_k|z_{1:k-1})}
     $$
     where:
     - $$p(x_k|z_{1:k})$$ is the posterior probability distribution of the state
     - $$p(z_k|x_k)$$ is the likelihood function
     - $$p(x_k|z_{1:k-1})$$ is the prior probability distribution of the state
     - $$p(z_k|z_{1:k-1})$$ is the normalizing constant

2. **Gaussian Assumption**:
   - The algorithm assumes that the state and measurement are Gaussian distributed.
   - The Gaussian assumption allows for the use of the Kalman filter equations.

#### Orthogonal Projection Method

1. **Orthogonal Projection**:
   - The algorithm uses orthogonal projection to find the best estimate of the state.
   - The orthogonal projection equation is given by:
     $$
     x_{k+1} = x_{k+1} + P_{k+1}H^T(HP_{k+1}H^T + R)^{-1}(z_k - Hx_{k+1})
     $$
     where:
     - $$P_{k+1}$$ is the error covariance matrix
     - $$H$$ is the measurement matrix
     - $$R$$ is the measurement noise covariance matrix

2. **Optimization**:
   - The algorithm optimizes the state estimate by minimizing the mean squared error.
   - The optimization equation is given by:
     $$
     \min_{x_{k+1}} \mathbb{E}[(x_{k+1} - x_k)^T(x_{k+1} - x_k)]
     $$
     where:
     - $$x_k$$ is the current state
     - $$x_{k+1}$$ is the updated state estimate

### Conclusion

The Kalman filter is a powerful algorithm for estimating the state of a system from noisy measurements. It uses a combination of prediction and update steps to produce an optimal estimate of the state. The algorithm can be derived using either the Bayesian approach or the orthogonal projection method.

"""



import random

import cv2
from ultralytics import YOLO

from tracker import Tracker

video_path = 'C:/Users/Harsh/OneDrive/Documents/Desktop/Object Tracking/data/people.mp4'
video_out_path = 'C:/Users/Harsh/OneDrive/Documents/Desktop/Object Tracking/data/out.mp4'

cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()

cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS),
                          (frame.shape[1], frame.shape[0]))

model = YOLO("yolov8n.pt")

tracker = Tracker()

colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]

detection_threshold = 0.5

while ret:
    results = model(frame)

    for result in results:
        detections = []
        for r in result.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = r
            x1, x2, y1, y2 = map(int, [x1, x2, y1, y2])
            class_id = int(class_id)
            if score > detection_threshold:
                detections.append([x1, y1, x2, y2, score])

        tracker.update(frame, detections)

        for track in tracker.tracks:
            bbox = track.bbox
            x1, y1, x2, y2 = map(int, bbox)
            track_id = track.track_id

            cv2.rectangle(frame, (x1, y1), (x2, y2), (colors[track_id % len(colors)]), 3)

    # Display the frame
    cv2.imshow('Video', frame)

    # Write the frame to the output video
    cap_out.write(frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    # Read the next frame
    ret, frame = cap.read()

cap.release()
cap_out.release()
cv2.destroyAllWindows()






# import os
# import random
#
# import cv2
# from ultralytics import YOLO
#
# from tracker import Tracker
#
#
# video_path = 'C:/Users/Harsh/OneDrive/Documents/Desktop/Object Tracking/data/people.mp4'
#
# video_out_path = 'C:/Users/Harsh/OneDrive/Documents/Desktop/Object Tracking/data/out.mp4'
#
# cap = cv2.VideoCapture(video_path)
# ret, frame = cap.read()
#
# cap_out = cv2.VideoWriter(video_out_path, cv2.VideoWriter_fourcc(*'mp4v'), cap.get(cv2.CAP_PROP_FPS),
#                           (frame.shape[1], frame.shape[0]))
#
# model = YOLO("yolov8n.pt")
#
# tracker = Tracker()
#
# colors = [(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)) for j in range(10)]
#
# detection_threshold = 0.5
# while ret:
#
#     results = model(frame)
#
#     for result in results:
#         detections = []
#         for r in result.boxes.data.tolist():
#             x1, y1, x2, y2, score, class_id = r
#             x1 = int(x1)
#             x2 = int(x2)
#             y1 = int(y1)
#             y2 = int(y2)
#             class_id = int(class_id)
#             if score > detection_threshold:
#                 detections.append([x1, y1, x2, y2, score])
#
#         tracker.update(frame, detections)
#
#         for track in tracker.tracks:
#             bbox = track.bbox
#             x1, y1, x2, y2 = bbox
#             track_id = track.track_id
#
#             cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (colors[track_id % len(colors)]), 3)
#
#     cap_out.write(frame)
#     ret, frame = cap.read()
#
# cap.release()
# cap_out.release()
# cv2.destroyAllWindows()