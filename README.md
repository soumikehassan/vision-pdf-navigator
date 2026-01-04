# 📄👀 VisionReader: AI-Powered Hands-Free PDF Controller

> **Control PDFs with just your face.**
> VisionReader is a computer vision–based tool that lets you control PDF documents completely hands-free using face movements detected via your webcam.

---

## 🎥 Demo (Recommended)

Add a short **5–10 second GIF** at the top of this README showing:

* Your face in front of the webcam
* The PDF scrolling, zooming, and changing pages

```md
![VisionReader Demo](assets/demo.gif)
```

---

## 🚀 Overview

VisionReader is designed for situations where using your hands is inconvenient—such as **eating, taking notes, or multitasking**. By tracking head position and distance, it enables natural and intuitive PDF navigation.

---

## ✨ Key Features

* 🔽 **Vertical Scrolling** – Tilt your head up or down
* ↔️ **Horizontal Panning** – Move your head left or right
* 📄 **Page Flipping** – Move your head to the far left or right
* 🔍 **Smart Zoom** – Lean forward to zoom in, lean back to zoom out
* 🎯 **Neutral (Dead) Zone** – Prevents accidental movement while reading
* ⚡ **One-Key Calibration** – Press `C` to calibrate to your sitting position

---

## 🛠️ Built With

* **Python** – Core programming language
* **OpenCV** – Real-time computer vision
* **MediaPipe** – High-fidelity face mesh tracking
* **PyAutoGUI** – Keyboard and mouse automation

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
https://github.com/soumikehassan/vision-pdf-navigator.git
cd vision-pdf-navigator
```

### 2️⃣ Install Dependencies

> Recommended to use the same MediaPipe version used during development.

```bash
pip install opencv-python mediapipe==0.10.14 pyautogui
```

---

## 📁 requirements.txt

Create a file named `requirements.txt` with the following content:

```text
opencv-python
mediapipe==0.10.14
pyautogui
```

---

## 🎮 How to Use

1. Open your favorite PDF reader (Chrome, Edge, Adobe Acrobat, etc.)
2. Run the script:

   ```bash
   python main.py
   ```
3. **Calibrate**: Sit in your normal reading position and press `C`
4. Start reading:

   * 👃 Move your nose outside the gray box to scroll
   * 🔍 Lean forward/backward to zoom
   * 📄 Move head quickly to screen edges to change pages
5. **Quit**: Press `Q`

---

## ⚙️ Control Mapping

| Action              | Physical Movement      | Keyboard / Mouse Command |
| ------------------- | ---------------------- | ------------------------ |
| Scroll Up / Down    | Tilt head up / down    | Mouse Wheel              |
| Scroll Left / Right | Move head left / right | Shift + Mouse Wheel      |
| Next Page           | Head to far right      | Right Arrow              |
| Previous Page       | Head to far left       | Left Arrow               |
| Zoom In             | Lean forward           | Ctrl + `+`               |
| Zoom Out            | Lean backward          | Ctrl + `-`               |

---

## 🔧 Configuration

You can fine-tune sensitivity in `main.py`:

```python
V_SCROLL_SPEED = 5      # Vertical scroll speed
ZOOM_SENSITIVITY = 0.15 # Lean distance for zoom
DEAD_ZONE = 40          # Neutral zone size
```

* Increase **DEAD_ZONE** if the page moves too easily
* Increase **ZOOM_SENSITIVITY** if zoom triggers accidentally

---

## 🖼️ Screenshots

Add screenshots showing:

* Face mesh tracking
* Gray neutral zone box
* Live camera feed

```md
![Face Mesh View](assets/screenshot_face_mesh.png)
![Reading View](assets/screenshot_reader.png)
```

---

## 📝 License

Distributed under the **MIT License**.
See `LICENSE` for more information.

---

## 🤝 Contributing

Contributions are welcome!

* Open an issue for bugs or feature requests
* Submit a pull request for improvements

---

## 👤 Author

**Your Name**

🔗 Project Link:
[https://github.com/YOUR_USERNAME/vision-pdf-navigator](https://github.com/YOUR_USERNAME/vision-pdf-navigator)

---

## 🌟 Tips to Improve This Repo

* ✅ Add a demo GIF (very important!)
* ✅ Include screenshots
* ✅ Write docstrings in `main.py`
* ✅ Add comments explaining face landmark logic
* ✅ Tag the project with topics: `computer-vision`, `mediapipe`, `hands-free`, `accessibility`

---

⭐ If you like this project, consider giving it a star!
