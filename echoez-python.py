import os
import pygame

music_dir = os.path.expanduser("~/Music")

pygame.init()

songs = [os.path.join(music_dir, f) for f in os.listdir(music_dir) if f.endswith(('.mp3', '.flac', '.wav', '.ogg'))]

if not songs:
    print("Error: No music files found in the directory.")
    exit(1)

current_song_index = 0
is_playing = False
repeat = False
volume = 0.5

# play the current song
def play_song():
    global is_playing
    pygame.mixer.music.load(songs[current_song_index])
    pygame.mixer.music.play()
    is_playing = True

# pause/play
def toggle_pause():
    global is_playing
    if is_playing:
        pygame.mixer.music.pause()
        is_playing = False
    else:
        pygame.mixer.music.unpause()
        is_playing = True

# next song
def next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(songs)
    play_song()

# previous song
def previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(songs)
    play_song()

# volume
def increase_volume():
    global volume
    volume = min(volume + 0.1, 1.0)
    pygame.mixer.music.set_volume(volume)

# decrease volume
def decrease_volume():
    global volume
    volume = max(volume - 0.1, 0.0)
    pygame.mixer.music.set_volume(volume)

# toggle repeat
def toggle_repeat():
    global repeat
    repeat = not repeat
    pygame.mixer.music.set_endevent(pygame.USEREVENT if repeat else pygame.constants.USEREVENT + 1)

# Play the first song
play_song()

# Main loop
while True:
    print("\nEchoez~")
    print("---------------------")
    print("Current Song:", os.path.basename(songs[current_song_index]))
    print("Status:", "Playing" if is_playing else "Paused")
    print("Volume:", int(volume * 100), "%")
    print("Controls:")
    print("  [p] Play/Pause")
    print("  [n] Next Song")
    print("  [b] Previous Song")
    print("  [+] Increase Volume")
    print("  [-] Decrease Volume")
    print("  [r] Repeat:", "ON" if repeat else "OFF")
    print("  [q] Quit")

    user_input = input("Enter your choice: ").lower()

    if user_input == "p":
        toggle_pause()
    elif user_input == "n":
        next_song()
    elif user_input == "b":
        previous_song()
    elif user_input == "+":
        increase_volume()
    elif user_input == "-":
        decrease_volume()
    elif user_input == "r":
        toggle_repeat()
    elif user_input == "q":
        pygame.mixer.music.stop()
        break

pygame.quit()
