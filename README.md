# Playing with Computer Vision

[![SQBBF.gif](https://s11.gifyu.com/images/SQBBF.gif)](https://www.linkedin.com/in/alokahirrao/)

## GUI

![Game photo](https://iili.io/HiNUD3N.jpg)

### Games Overview:

1. **Tower Building**  
   - [Play Tower Building on Microsoft Store](https://apps.microsoft.com/detail/9MXKDQKFJGBJ?hl=en-us&gl=IN&ocid=pdpshare)

2. **Hill Climb Racing**  
   - [Play Hill Climb Racing on Microsoft Store](https://apps.microsoft.com/detail/9WZDNCRDCWK8?hl=en&gl=IN&ocid=pdpshare)

3. **Dino Game**  
   - [Play Dino Game Online](https://www.google.com/search?q=dino+game) (Simply search "Dino Game" in Google for offline play or play directly in your browser when disconnected from the internet!)

4. **Pong Classic**  
   - This game is built in the project code using **OpenCV**. It’s a classic Pong game where you control paddles with hand gestures.

### Features:
- **Hand Gesture Recognition** using OpenCV and MediaPipe.
- **Key Simulation** through custom key press libraries.
- **Interactive GUI** to select and play different games.

![Game photo](https://iili.io/HiNUmvt.jpg)
![Game photo](https://iili.io/HiNUbaI.jpg)
![Game photo](https://iili.io/HiNUZ4p.jpg)
![Game photo](https://iili.io/HiNUpyX.jpg)

---

### Files and Formats:

```
/my-project
│
├── .idea/                  # IDE configuration files (used by JetBrains IDEs like PyCharm)
├── Resources/              # Folder containing all background images and game-related assets
│   ├── Background.png      # Background image used in the GUI
│   └── gameOver.png        # Game over screen image
├── __pycache__/            # Automatically generated folder by Python containing compiled bytecode files
├── img_re/                 # Folder for storing image-related resources
│   ├── dino.png            # Example image for the Dino game
│   └── pong_ball.png       # Example image for the Pong game
├── .gitattributes          # Git configuration file for line endings and attributes
├── GUI.py                  # Python script for the Graphical User Interface (GUI)
├── README.md               # Project documentation
├── directkeys1.py          # Python script for simulating key presses for Game 1
├── directkeys2.py          # Python script for simulating key presses for Game 2
├── directkeys3.py          # Python script for simulating key presses for Game 3
├── game1.png               # Image file (PNG format) used for displaying the button for Game 1
├── game2.png               # Image file (PNG format) used for displaying the button for Game 2
├── game3.png               # Image file (PNG format) used for displaying the button for Game 3
├── game4.png               # Image file (PNG format) used for displaying the button for Game 4
├── hand_landmarks.png      # Image file (PNG format) used for visualizing hand landmarks
├── main.py                 # Python script that runs the game control system
└── requirements.txt        # File listing all the dependencies for the project
```

---

### How to Run:

1. **Run the Game GUI**:
   - To start the game, **run `main.py` first**. This will launch the GUI where you can select the game.
   
   ```bash
   python main.py
   ```

2. **Select a Game**:
   - You will see the four game options in the GUI:
     - **Tower Building**
     - **Hill Climb Racing**
     - **Dino Game**
     - **Pong Classic**

3. **Control the Game**:
   - **Hand gestures** will control the game.
   - Use gestures to simulate pressing keys like **"Space"** for jumping, **"Enter"** for selecting, or **"Left/Right arrows** for movement, depending on the game selected.

4. **Libraries**:
   - Install the required libraries by running:
     ```bash
     pip install -r requirements.txt
     ```

5. **Game Control**:
   - The games are controlled using **hand gestures** detected through **OpenCV** and **MediaPipe**.

---

### Conclusion

This project demonstrates how to build a **hand-gesture-controlled gaming system** using **OpenCV** and **MediaPipe**. By using this directory structure and the accompanying Python scripts, you can easily manage the assets, game logic, and interface for an interactive game.
