# 📁 Smart File Organizer CLI

An automated command-line utility built in Python that cleans up messy folders (like `Downloads` or `Desktop`) by sorting files into categorized subfolders based on their extensions.

---

## ✨ Features

- **Automatic Category Detection:** Sorts files into `Images`, `Documents`, `Audio`, `Videos`, `Archives`, `Code_and_Scripts`, `Executables`, and `Others`.
- **Zero Third-Party Dependencies:** Uses native Python libraries (`os`, `shutil`, `sys`).
- **Flexible Path Execution:** Organize any folder by providing its path, or run it in the current directory.
- **Safe Execution:** Automatically ignores system/hidden files and existing subdirectories.

---

## 📂 File Categorization Rules

| Category | Supported Extensions |
| :--- | :--- |
| 🖼️ **Images** | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.svg`, `.webp` |
| 📄 **Documents** | `.pdf`, `.docx`, `.doc`, `.txt`, `.xlsx`, `.pptx`, `.csv` |
| 🎵 **Audio** | `.mp3`, `.wav`, `.aac`, `.flac`, `.m4a` |
| 🎬 **Videos** | `.mp4`, `.mkv`, `.mov`, `.avi`, `.flv` |
| 📦 **Archives** | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| 💻 **Code & Scripts** | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java`, `.json` |
| ⚙️ **Executables** | `.exe`, `.msi`, `.dmg`, `.sh`, `.bat` |
| 📁 **Others** | Any extension not listed above |

---

## 🚀 Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/downloads/) installed on your system.

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/file-organizer.git](https://github.com/your-username/file-organizer.git)
   cd file-organizer
