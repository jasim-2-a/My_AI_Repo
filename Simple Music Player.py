import pygame
import time


pygame.mixer.init()


def play_music(music_file):
    pygame.mixer.music.load(music_file)
    pygame.mixer.music.play(loops=0, start=0.0)
    print(f"🎶 Now playing: {music_file}")


def pause_music():
    pygame.mixer.music.pause()
    print("⏸️ Music paused")


def unpause_music():
    pygame.mixer.music.unpause()
    print("▶️ Music resumed")


def stop_music():
    pygame.mixer.music.stop()
    print("⛔ Music stopped")


def main():
    while True:
        print("\n🎵 Music Player")
        print("1. Play Music")
        print("2. Pause Music")
        print("3. Resume Music")
        print("4. Stop Music")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            music_file = input("Enter the path to the music file (e.g., song.mp3): ").strip()
            try:
                play_music(music_file)
            except Exception as e:
                print(f"❗ Error: Could not play the file. Please check the path and format. ({e})")

        elif choice == '2':
            pause_music()

        elif choice == '3':
            unpause_music()

        elif choice == '4':
            stop_music()

        elif choice == '5':
            stop_music()
            print("Goodbye! 🎶")
            break

        else:
            print("❗ Invalid choice. Please choose a number between 1 and 5.")

if __name__ == "__main__":
    main()
