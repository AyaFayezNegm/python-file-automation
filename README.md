# 🖼️ Task Automation with Python

A simple Python automation script that automatically moves all `.jpg` image files from a source folder to a destination folder.

This project was developed as part of my Python learning journey to practice file automation using Python's built-in libraries.

---

## 📌 Features

- 📂 Reads all files from a source directory
- 🖼️ Detects `.jpg` image files only
- 🚚 Moves images automatically to another folder
- 💬 Displays a success message for each moved image
- ❌ Ignores non-image files

---

## 🛠️ Technologies Used

- Python 3
- `os` module
- `shutil` module

---
## 📁 Project Structure

```text
CodeAlpha_FileAutomation/
│
├── images/
│   ├── cat_large.jpg
│   ├── cat.jpg
│   ├── cats 2 (1).jpg
│   ├── cats.jpg
│   ├── group 1.jpg
│   ├── group 2.jpg
│   ├── lady.jpg
│   ├── dog.mp4
│   └── kitten.mp4
│
├── moved_images/
│
├── main.py
└── README.md
```
---

## 🚀 How It Works

1. Place your image files inside the **images** folder.
2. Run the script:

```bash
python main.py
```

3. The program:
   - Scans all files in the source folder.
   - Checks whether each file has the `.jpg` extension.
   - Moves image files to the **moved_images** folder.
   - Prints a success message for every moved image.

---

## 💻 Example Output

```text
cat.jpg moved successfully!
flower.jpg moved successfully!
group 1.jpg moved successfully!
lady.jpg moved successfully!
```

---

## 📚 Concepts Practiced

This project helped me practice:

- Variables
- Loops (`for`)
- Conditional Statements (`if`)
- File Handling
- Path Manipulation
- Python Modules
- Functions
- Automation Scripts

---

## 🔮 Future Improvements

- Support multiple image formats (`.png`, `.jpeg`)
- Automatically create destination folders if they don't exist
- Organize files by type (Images, Videos, Documents)
- Add a graphical user interface (GUI)

---

## 👩‍💻 Author

**Aya Fayez**

Bachelor's Degree in Languages & Translation

Currently learning Python for AI, NLP, and Automation.
