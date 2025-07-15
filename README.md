# Gesture-Controlled-Assistants

# 🤖 AI_SSIST – A Touchless Hand Gesture AI Assistant for Seamless System Control

AI_SSIST is an AI-powered assistant that lets users perform tasks **using hand gestures only**, without touching the keyboard or mouse. Built with computer vision and text-to-speech, it’s especially helpful for accessibility and innovation-focused use cases.

---

## 📌 Features

- 🖐️ Detects real-time finger gestures via webcam
- 🗣️ Reads text aloud from `data.txt` (TTS)
- 🌐 Opens websites like YouTube, Gmail, and Google News
- 🎵 Plays music using a local file
- ❌ Exits the assistant when no fingers are shown

---

## 🧠 Hand Gesture Mappings

| 👋 Fingers | 🎯 Action                  | 💡 Purpose                                      |
|-----------|----------------------------|------------------------------------------------|
| 0         | Exit the assistant         | Safe shutdown by gesture                       |
| 1         | Read and speak `data.txt`  | Read aloud file for visually impaired users     |
| 2         | Open YouTube               | Gesture-based media control                    |
| 3         | Open Gmail                 | Productivity control via hand                  |
| 4         | Open Google News           | Stay updated using gestures                    |
| 5         | Play `music.mp3`           | Touchless music access                         |

---

## 🔧 Tech Stack

- 🐍 Python 3.10
- 🎯 OpenCV – camera & image processing
- ✋ MediaPipe – hand tracking
- 🗣️ pyttsx3 – offline text-to-speech
- 🌐 Webbrowser & OS – for tab opening and file execution

---

## 📁 File Overview

| File Name     | Description                               |
|---------------|-------------------------------------------|
| `ai_ssist.py` | Main Python code                          |
| `data.txt`    | File content to be read aloud             |
| `music.mp3`   | Music file to play using gestures         |

---

## 🚀 How to Run

### 1️⃣ Install Libraries

```bash
pip install opencv-python
pip install mediapipe
pip install pyttsx3
