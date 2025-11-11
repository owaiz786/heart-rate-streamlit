# 💓 Real-Time Heart Rate Estimation using Face Video (rPPG)

This project demonstrates a **non-contact heart rate estimation system** using a regular webcam.  
It uses **remote photoplethysmography (rPPG)** to detect subtle color variations in the **forehead region** caused by blood flow.  
The project extracts the green-channel intensity signal, visualizes its temporal fluctuations, and performs **FFT-based heart rate analysis**.

---

## 🧠 Concept Overview

When the human heart pumps blood, **minute color changes** occur on the skin surface—especially in the **forehead region**.  
These changes, although invisible to the naked eye, can be captured by a camera and analyzed to estimate **pulse rate**.

This project:
1. Detects a face using OpenCV’s Haar Cascade.
2. Extracts the **forehead region** as the ROI (Region of Interest).
3. Measures the **average green-channel intensity** over time.
4. Performs **Fast Fourier Transform (FFT)** on the intensity signal.
5. Identifies the **dominant frequency** corresponding to heart rate (in BPM).

---

## 🧩 Features

- 🧍‍♂️ Real-time face and forehead detection.
- 🌈 Dynamic face color overlay based on signal fluctuations (red, green, blue).
- 📊 Visualization of pixel intensity over time.
- ⚡ FFT-based estimation of heart rate.
- 🩺 Outputs an estimated **BPM (Beats Per Minute)**.

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **Libraries:**  
  - `opencv-python` – Face detection & live video capture  
  - `numpy` – Numerical operations  
  - `matplotlib` – Data visualization  
  - `scipy` – FFT computation  
  - `collections` – Deque for buffer handling  

---

## ⚙️ Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/face-heart-rate-estimation.git
   cd face-heart-rate-estimation
Install required packages:

pip install opencv-python numpy matplotlib scipy


Ensure your webcam is working and accessible by OpenCV.

▶️ How to Run

Run the main script:

python main.py


A live window will open showing your face:

A colored overlay (red, green, blue) will appear on your face depending on intensity changes.

Press q to stop the recording.

After quitting:

The program plots your pixel intensity variation.

Performs an FFT and estimates your heart rate in BPM.

📈 Output
1. Live Webcam Feed

Real-time face detection with forehead ROI highlighted.

Color overlay representing changes in pixel intensity:

🔴 Red: Intensity increasing

🟩 Green: Stable

🔵 Blue: Intensity decreasing

2. Pixel Intensity Plot

Shows how the average green-channel intensity varies across frames.

3. FFT Spectrum

Displays frequency-domain power with a peak indicating estimated heart rate.

4. Console Output

Example:

❤️ Estimated Heart Rate: 76.35 BPM

📊 Sample Results
Stage	Description	Visualization
Face Detection	Detects face & forehead region	🧍‍♂️
Intensity Extraction	Tracks green-channel changes	📈
FFT Analysis	Identifies peak frequency	🔍
Heart Rate Estimation	Converts peak frequency → BPM	❤️ 76 BPM
🚀 Future Improvements

🔬 Replace Haar Cascade with MediaPipe or Dlib for more robust face tracking.

📉 Implement real-time BVP graph and heart rate display while recording.

🌐 Build a Flask or Streamlit dashboard for live monitoring.

🤖 Integrate deep learning-based rPPG signal denoising and quality assessment.

📚 References

Poh et al., “Non-contact, automated cardiac pulse measurements using video imaging and blind source separation,” Optics Express, 2010.

OpenCV Documentation: https://docs.opencv.org

rPPG Theory and Applications: https://en.wikipedia.org/wiki/Remote_photoplethysmography
