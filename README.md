# Real-Time Face De-Identification and Inside-Outside Classification

This repository contains two Python scripts and two pre-trained `.h5` models for real-time video processing:

1. **`real-time-de-identification.py`**
   - Identifies faces in real-time from a video feed or video file.
   - Blurs or de-identifies recognized faces using various methods.

2. **`outside_remover.py`**
   - Classifies frames from a video as `inside` or `outside` using a pre-trained model.
   - Saves frames classified as `inside` to a new video file.

## Requirements

### Python Dependencies
The scripts require the following libraries:

- `opencv-python`
- `numpy`
- `tensorflow`
- `scipy`

Install dependencies using pip:
```bash
pip install opencv-python numpy tensorflow scipy
```

### Model Files

- **`face_classifier.h5`**: Used in `real-time-de-identification.py` to classify faces as `me` or `not_me`.
- **`inside_outside.h5`**: Used in `outside_remover.py` to classify video frames as `inside` or `outside`.

Place the `.h5` files in the following directories:
- `face_classifier.h5` in `models/`
- `inside_outside.h5` in `Documents/5th_sem/Project/`

## Usage

### 1. Real-Time Face De-Identification

Run the `real-time-de-identification.py` script to process a live video feed or a saved video file.

#### Configuration
- Set `VIDEO_FILE` to the path of your video file if not using a live feed.
- Ensure `face_classifier.h5` is in the `models/` directory.

#### Run
```bash
python real-time-de-identification.py
```

#### Features
- Identifies faces using OpenCV's Haar Cascade.
- Uses a pre-trained classifier to determine if a face matches `me`.
- Blurs or de-identifies recognized faces using:
  - Gaussian blur
  - Pixelation (mosaic effect)

### 2. Inside-Outside Frame Classification

Run the `outside_remover.py` script to process a video file and save only `inside` frames to a new video file.

#### Configuration
- Set `video` to the path of your input video file.
- Set `output` to the desired path for the processed video.
- Ensure `inside_outside.h5` is in the `Documents/5th_sem/Project/` directory.

#### Run
```bash
python outside_remover.py
```

#### Features
- Classifies frames as `inside` or `outside` using a pre-trained model.
- Saves frames classified as `inside` to a new video file.

## File Structure

```
project/
├── models/
│   └── face_classifier.h5
├── Documents/
│   └── 5th_sem/
│       └── Project/
│           └── inside_outside.h5
├── real-time-de-identification.py
├── outside_remover.py
└── README.md
```

## Notes

- Ensure your Python environment has all the required dependencies.
- Modify file paths in the scripts to match your local directory structure if needed.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.

## Author
Praharsh Gurudatta
