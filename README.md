# 🐦 Fluppy Bird

**Fluppy Bird** is a simple 2D side-scrolling game made using **Pygame**, inspired by the classic *Flappy Bird*. The player controls a bird that must avoid pipes to keep scoring. The game includes a start menu, hover effects, background music, sound effects, and a score display.

---

## 🎮 Features

- Main menu with **Start** and **Exit** buttons
- Hover color effect on buttons
- Background music using `.mp3` files
- Button click sound effects
- Bird auto-fall and jump on spacebar press
- Pipe obstacles that scroll left
- Real-time score display
- Game ends on collision with pipes

---

## 🕹️ Controls

- **Spacebar** — Makes the bird jump upward
- **Mouse Click** — To select **Start** or **Exit** from the menu

---

## 📦 Required Assets

Place the following files in the same directory as the Python script:

| File Name          | Purpose                       |
|--------------------|-------------------------------|
| `mainbg.png`       | Main menu background image     |
| `background.png`   | Game background image          |
| `fuppy.png`        | Bird sprite                    |
| `pipe.png`         | Obstacle sprite (pipe)         |
| `bird.mp3`         | Background music               |
| `buttonclick.mp3`  | Button click sound effect      |

---

## 🛠️ Requirements

- Python 3.x
- Pygame

Install Pygame using pip:

```bash
pip install pygame
