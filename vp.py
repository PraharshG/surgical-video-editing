import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import cv2
import numpy as np

#def process_frame(frame):
#    _, buffer = cv2.imencode('.jpg', frame)
#
#    # Convert the buffer to a numpy array
#    jpg_image = np.array(buffer).tobytes()
#    
#    jpg_image.save("cache/img.jpg")
#    jpg_image = Image.open('cache/img.jpg',0)   
#
#    res = predictor(jpg_image)
#    return res

def predictor():
    img = tf.keras.preprocessing.image.load_img('cache/img.jpg', target_size=(128, 128))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = tf.expand_dims(img_array, 0)
    loaded_model = tf.keras.models.load_model('in_out.h5')
    predictions = loaded_model.predict(img_array)
    return predictions[0][0]

video_path = "My Videos/202109080914_45_1.mp4"
output_video_path = "output.avi"

cap = cv2.VideoCapture(video_path)

# Get the frames per second (fps)
fps = cap.get(cv2.CAP_PROP_FPS)
print(f"Video FPS: {fps}")

# Loop through the frames
frame_number = 0
out_frame = 0

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

fourcc = cv2.VideoWriter_fourcc(*'MPEG')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (width, height))

while True:

    ret, frame = cap.read()
    # Check if the frame was read successfully
    if not ret:
        break

    cv2.imwrite('cache/img.jpg',frame)
    check = predictor()
    if check == 0.0:
        out.write(frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break    

cap.release()
out.release()
cv2.destroyAllWindows()
