# import libraries
# Getting a frame every second for scanning with AI.
# This allows the program to keep up with the live feed's pace
import time  # for sleep
import multiprocessing


# TODO: object detection function
def scan_image(frame, call_time):
    # run AI on frame
    # if object found, save frame and log result.
    print("we are in scan_image()! count: " + str(frame))
    return


if __name__ == '__main__':
    import cv2  # include opencv library functions in python
    from vidgear.gears import CamGear

    def birdIDer():
        fpsLimit = 1  # throttle limit
        startTime = time.time()
        imagesFolder = "saved_images"
        x = 1
        c = 0

        # Create an object to hold reference to livestream
        #cap = cv2.VideoCapture(0)
        options = {"CAP_PROP_FPS": 1}
        cap = CamGear(source='https://www.youtube.com/watch?v=JhajwzEv1Fo',
                      stream_mode=True, logging=True, **options).start()
        # currently only doing one frame per 5 seconds.

        while True:
            nowTime = time.time()
            frame = cap.read()  # capture the frame from live video
            # if (nowTime - startTime) >= fpsLimit: #without this, every single frame is saved even though options state 1fps
            if(c % 30 == 0):
                filename = imagesFolder + "/image_" + str(x) + ".jpg"
                x += 1
                cv2.imwrite(filename, frame)  # save image
                # new object detection process per frame
                p = multiprocessing.Process(target=scan_image(x))
                p.start()
                startTime = time.time()  # reset time
            c += 1

    def main():
        birdIDer()

    main()
