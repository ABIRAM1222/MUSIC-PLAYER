import os
import pygame
import tkinter as tk
from tkinter import filedialog

class MusicPlayer:
    def __init__(self, root):  # Corrected constructor
        self.root = root
        self.root.title("Music Player")
        self.root.geometry("400x350")

        self.current_song = None
        self.playing = False

        pygame.mixer.init()

        self.play_button = tk.Button(self.root, text="Play", command=self.play_music)
        self.play_button.pack(pady=20)

        self.pause_button = tk.Button(self.root, text="Pause", command=self.pause_music)
        self.pause_button.pack(pady=20)

        self.stop_button = tk.Button(self.root, text="Stop", command=self.stop_music)
        self.stop_button.pack(pady=20)

        self.load_button = tk.Button(self.root, text="Load", command=self.load_music)
        self.load_button.pack(pady=20)

        self.music_list = tk.Listbox(self.root)
        self.music_list.pack(pady=20, fill=tk.BOTH, expand=True)

    def load_music(self):
        directory = filedialog.askdirectory()
        os.chdir(directory)
        songs = os.listdir()

        for song in songs:
            if song.endswith(".mp3"):
                self.music_list.insert(tk.END, song)

    def play_music(self):
        if not self.playing:
            self.current_song = self.music_list.get(tk.ACTIVE)
            pygame.mixer.music.load(self.current_song)
            pygame.mixer.music.play()
            self.playing = True

    def pause_music(self):
        if self.playing:
            pygame.mixer.music.pause()
            self.playing = False

    def stop_music(self):
        pygame.mixer.music.stop()
        self.playing = False

if __name__ == "__main__":  # Corrected entry point
    root = tk.Tk()
    app = MusicPlayer(root)
    root.mainloop()
