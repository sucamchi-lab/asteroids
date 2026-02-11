Asteroids, Rebuilt in Pygame
============================

A small but complete Asteroids clone written in Python with Pygame. The goal was to learn game loops, sprite groups, and collision handling while keeping the code readable and easy to extend.

Built with guidance from the Boot.dev curriculum (https://boot.dev).

Features
--------
- Player ship with rotation, thrust, and shooting
- Asteroid spawning and splitting
- Shot cooldown and collision handling
- Lightweight event and state logging

Controls
--------
- W/S: thrust forward/back
- A/D: rotate
- Space: shoot

Run Locally
-----------
1. Create and activate a virtual environment.
2. Install dependencies:
	- pip install pygame
3. Run the game:
	- python main.py

Project Structure
-----------------
- main.py: game loop and group setup
- player.py: ship movement and shooting
- asteroid.py / asteroidfield.py: asteroid behavior and spawning
- shot.py: projectile behavior
- logger.py: state and event logging

Notes
-----
This project is intentionally small and hackable. If you want to add sound, score, or screen wrap, these files are a good starting point.
