# Echoez
TUI Music Player
- [x] Bash
- [x] Python
- [=] Rust

## Features
- **Simple and Lightweight**: Echoez provides a minimalist user interface, perfect for quick and easy music playback without any bloat.
- **Control Playback with Ease**: Use intuitive keyboard shortcuts to play/pause, skip to the next or previous track, and quit the player.
- **Customizable Playlist**: Echoez automatically scans your `~/Music` directory for MP3 files, allowing you to easily manage and update your playlist.
- **Efficient Resource Usage**: Built with Bash scripting and leveraging the power of `mpv`, Echoez consumes minimal system resources while delivering smooth audio playback.

## Requirements
- Linux operating system
- mpv command-line media player
- MP3 music files located in ~/Music directory

## Installation

1. Clone the repository to your local machine:
```bash
git clone https://github.com/Dawit-Sh/Echoez.git
```
2. Navigate to the directory:
```bash
cd Echoez
```
3. Make the script executable :
```bash
chmod +x echoez.sh
```
4. Run the script
```bash
./echoez.sh
```

## Usage
- Play/Pause: Press p to toggle between play and pause.
- Next Track: Press n to skip to the next track.
- Previous Track: Press b to go back to the previous track.
- Quit: Press q to exit the music player.

## Pyhon Version 
Due to the limitation of mpv on other audio files. I decided to create another one with python version

**supported**:
- [x] mp3
- [x] flac
- [x] wav
- [x] ogg

> Requires pygame module to be installed 
```bash
pip install pygame
```

## Contributing
Contributions to Echoez are welcome! 
Whether you want to fix bugs, improve existing features, or suggest new ideas, feel free to submit a pull request.

## License
This project is licensed under the GPL3 License. See the LICENSE file for details.

