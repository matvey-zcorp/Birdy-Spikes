from datetime import datetime
import pygame
import sys


class Logger:
    def __init__(self, logfile, msg=""):
        self.file = open(logfile, "w", encoding="UTF-8")
        if msg:
            self.file.write(f"{msg}\n")
            self.file.flush()
    def log(self, level, msg):
        self.file.write(f"{datetime.now():%H:%M:%S} [{level}] {msg}\n")
        self.file.flush()
    def close(self):
        self.file.close()


logger = Logger("game.log", "Birdy Spikes v1.0.0 Logs:")

logger.log("INFO", "Initializing engine...")
pygame.init()
logger.log("INFO", "Engine initialized!")

logger.log("INFO", "Creating window...")

WIDTH = 400
HEIGHT = 500

display = pygame.display.set_mode((WIDTH, HEIGHT))

logger.log("INFO", "Window created!")

while True:
    display.fill(pygame.Color("black"))

    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            logger.log("INFO", "Game closed!")
            logger.close()
            pygame.quit()
            sys.exit()

    pygame.display.flip()