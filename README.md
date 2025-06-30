# Playing Cards Generator

This project generates a full deck of playing cards as images using Python and Pillow.

---

## 🪟 Windows Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/playing-cards.git
   cd playing-cards
   ```
2. **Install [uv](https://github.com/astral-sh/uv):**
   - Download and install uv from the [official releases](https://github.com/astral-sh/uv#installation).
   - Or, with pipx:
     ```sh
     pipx install uv
     ```
3. **Set up the Python environment and install dependencies:**
   ```sh
   uv venv
   uv install
   ```
4. **Activate the virtual environment:**
   ```sh
   .venv\Scripts\activate
   ```
5. **Place your resources:**
   - Put your font files (e.g., `CalSans-Regular.ttf`, `DejaVuSans.ttf`) in a folder named `fonts` in the project root.
   - Put your watermark image (e.g., `kraken.png`) in a folder named `watermarks` in the project root.
6. **Run the script:**
   ```sh
   python generate-card.py
   ```
   Output images will be in the `output` folder.

---

## 🍏 Mac Setup

1. **Clone the repository:**
   ```sh
   git clone https://github.com/YOUR_GITHUB_USERNAME/playing-cards.git
   cd playing-cards
   ```
2. **Install [uv](https://github.com/astral-sh/uv):**
   - With Homebrew:
     ```sh
     brew install astral-sh/uv/uv
     ```
   - Or, with pipx:
     ```sh
     pipx install uv
     ```
3. **Set up the Python environment and install dependencies:**
   ```sh
   uv venv
   uv install
   ```
4. **Activate the virtual environment:**
   ```sh
   source .venv/bin/activate
   ```
5. **Place your resources:**
   - Put your font files (e.g., `CalSans-Regular.ttf`, `DejaVuSans.ttf`) in a folder named `fonts` in the project root.
   - Put your watermark image (e.g., `kraken.png`) in a folder named `watermarks` in the project root.
6. **Run the script:**
   ```sh
   python generate-card.py
   ```
   Output images will be in the `output` folder.

---

## Notes

- Make sure the font and watermark file names match those referenced in `generate-card.py`.
- The script will generate 52 PNG images, one for each card, in the `output` directory.
