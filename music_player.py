import pygame

pygame.mixer.init()

class Song:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class MusicPlayer:
    def __init__(self):
        self.head = None
        self.current = None

    def add_song(self, path):
        new_song = Song(path)

        if self.head is None:
            self.head = new_song
            new_song.next = new_song
            new_song.prev = new_song
            self.current = new_song
        else:
            tail = self.head.prev

            tail.next = new_song
            new_song.prev = tail

            new_song.next = self.head
            self.head.prev = new_song

    def display(self):
        if self.head is None:
            print("Playlist empty")
            return

        temp = self.head
        while True:
            print(temp.data, end=" -> ")
            temp = temp.next
            if temp == self.head:
                break
        print(" (circular)")

    def play(self):
        if self.current:
            pygame.mixer.music.load(self.current.data)
            pygame.mixer.music.play()
            print("Playing:", self.current.data)

    def pause(self):
        pygame.mixer.music.pause()
        print("Paused")

    def resume(self):
        pygame.mixer.music.unpause()
        print("Resumed")

    def stop(self):
        pygame.mixer.music.stop()
        print("Stopped")

    def next_song(self):
        if self.current:
            self.current = self.current.next
            self.play()

    def prev_song(self):
        if self.current:
            self.current = self.current.prev
            self.play()

    def insert_at_position(self, path, pos):
        new_song = Song(path)

        if pos == 1:
            if self.head is None:
                self.head = new_song
                new_song.next = new_song
                new_song.prev = new_song
                self.current = new_song
            else:
                tail = self.head.prev

                new_song.next = self.head
                new_song.prev = tail

                tail.next = new_song
                self.head.prev = new_song

                self.head = new_song
            return

        temp = self.head
        for _ in range(pos - 2):
            temp = temp.next

        new_song.next = temp.next
        new_song.prev = temp

        temp.next.prev = new_song
        temp.next = new_song

    def delete_at_position(self, pos):
        if self.head is None:
            print("Playlist empty")
            return

        if pos == 1:
            if self.head.next == self.head:
                self.head = None
                self.current = None
                return

            tail = self.head.prev
            self.head = self.head.next

            self.head.prev = tail
            tail.next = self.head
            return

        temp = self.head
        for _ in range(pos - 1):
            temp = temp.next

        temp.prev.next = temp.next
        temp.next.prev = temp.prev


player = MusicPlayer()

# Add songs
player.add_song(r"C:\Users\asara\Music\Maha Ganapatim Manasa.mp3")
player.add_song(r"C:\Users\asara\Music\Hrudayama.mp3")
player.add_song(r"C:\Users\asara\Music\Kadalalle - SenSongsMp3.Co.mp3")
player.add_song(r"C:\Users\asara\Music\O Madhu-SenSongsMp3.Com.mp3")
player.add_song(r"C:\Users\asara\Music\Sahana Sahana.mp3")

# options
while True:
    print("\n1.Play 2.Pause 3.Resume 4.Stop 5.Next 6.Previous")
    print("7.Display 8.Insert 9.Delete 0.Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        player.play()
    elif choice == 2:
        player.pause()
    elif choice == 3:
        player.resume()
    elif choice == 4:
        player.stop()
    elif choice == 5:
        player.next_song()
    elif choice == 6:
        player.prev_song()
    elif choice == 7:
        player.display()
    elif choice == 8:
        path = input("Enter song path: ")
        pos = int(input("Enter position: "))
        player.insert_at_position(path, pos)
    elif choice == 9:
        pos = int(input("Enter position to delete: "))
        player.delete_at_position(pos)
    elif choice == 0:
        break
    else:
        print("Invalid choice")