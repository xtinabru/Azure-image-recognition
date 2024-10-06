# 🌟 Azure Image Recognition

A Python-based application that uses **Azure Cognitive Services'** Computer Vision API to analyze and describe images. The application sends images to the API and returns categories, descriptions, and confidence levels. Suitable for basic image recognition and analysis tasks.

---

## 📖 Overview

This project is a **Python application** that leverages the **Azure Cognitive Services Computer Vision API** to analyze images.  
It provides image descriptions, categories, and confidence scores by sending the images to the Azure API.

---

## ✨ Features

- 📷 Analyzes images and returns descriptions with confidence levels.
- 💻 Uses the Azure Computer Vision API to categorize and describe images.
- 🛠️ Designed for easy use with Python.

---

## ⚙️ Requirements

- **Python 3.x**
- **Azure Cognitive Services account** with a Computer Vision resource
- Libraries: `requests`, `python-dotenv`

---

## 🛠️ Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd your-repository-name
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables:**

   - Create a `.env` file in the root directory:

      ```plaintext
      SUBSCRIPTION_KEY=your_subscription_key_here
      ENDPOINT=https://your_endpoint_here
      ```

---

## 🚀 Usage

1. **Place an image** in the appropriate directory (e.g., `/Pictures`).
2. **Edit the `image_path`** variable in the code to point to your image.
3. **Run the script:**

    ```bash
    python image_recognition.py
    ```

The program will send the image to the Azure API and output the description and categories.

---

## 📋 Example Output

After running the program, you should see something like:

```bash
Available keys:
- categories
- description
- requestId
- metadata
- modelVersion

What we can see in the picture:
- A building with a large archway (confidence: 0.24)
