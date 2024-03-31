#!/bin/bash

# Define the music directory
music_dir="$HOME/Music"

# Check if the music directory exists
if [ ! -d "$music_dir" ]; then
    echo "Error: Music directory not found."
    exit 1
fi

# Get a list of music files in the directory
songs=("$music_dir"/*.mp3)

# Check if there are any music files
if [ ${#songs[@]} -eq 0 ]; then
    echo "Error: No music files found in the directory."
    exit 1
fi

# Initialize variables
current_song_index=0
is_playing=false

# Function to play the current song
play_song() {
    mpv "${songs[current_song_index]}" --no-video
    is_playing=true
}

# Function to toggle pause/play
toggle_pause() {
    if $is_playing; then
        pkill -STOP mpv
        is_playing=false
    else
        pkill -CONT mpv
        is_playing=true
    fi
}

# Function to play the next song
next_song() {
    ((current_song_index++))
    if ((current_song_index >= ${#songs[@]})); then
        current_song_index=0
    fi
    play_song
}

# Function to play the previous song
previous_song() {
    ((current_song_index--))
    if ((current_song_index < 0)); then
        current_song_index=$(( ${#songs[@]} - 1 ))
    fi
    play_song
}

# Main loop
while true; do
    clear
    echo "Echoez~"
    echo "---------------------"
    echo "Current Song: $(basename "${songs[current_song_index]}")"
    echo "Status: $(if $is_playing; then echo "Playing"; else echo "Paused"; fi)"
    echo "Controls:"
    echo "  [p] Play/Pause"
    echo "  [n] Next Song"
    echo "  [b] Previous Song"
    echo "  [q] Quit"

    read -rsn1 input
    case $input in
        "p") toggle_pause ;;
        "n") next_song ;;
        "b") previous_song ;;
        "q") break ;;
    esac
done
