from imageai.Detection import VideoObjectDetection
import tensorflow as tf
import os

execution_path = os.getcwd()

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath( os.path.join(execution_path , "yolo.h5"))
detector.loadModel(detection_speed="flash") 
video_path = detector.detectObjectsFromVideo(input_file_path=os.path.join( execution_path, "traffic-mini.mp4"),
                                output_file_path=os.path.join(execution_path, "traffic_mini_detected_1")
                                , frames_per_second=29, log_progress=True)
print(video_path)