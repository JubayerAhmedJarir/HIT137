import tkinter as tk
from tkinter import ttk

# Decorator to log actions
def log_action(func):
    def wrapper(*args, **kwargs):
        print(f"Action performed: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Another decorator for logging button clicks
def log_click(func):
    def wrapper(*args, **kwargs):
        print(f"Button clicked: {func.__name__}")
        return func(*args, **kwargs)
    return wrapper

# Base class for a button
class Button:
    def __init__(self, master, text, command=None):
        self.button = tk.Button(master, text=text, command=command)
    
    def pack(self, **kwargs):
        self.button.pack(**kwargs)

# A subclass to customize button appearance (method overriding)
class StyledButton(Button):
    def __init__(self, master, text, command=None, bg="red", fg="white"):
        super().__init__(master, text, command)
        self.button.configure(bg=bg, fg=fg)
    
    # Override the pack method to log button packing
    def pack(self, **kwargs):
        print("Packing a styled button")
        super().pack(**kwargs)

# Encapsulating video details
class VideoDetails:
    def __init__(self, title, description):
        self.__title = title
        self.__description = description
    
    # Getter for video title
    def get_title(self):
        return self.__title
    
    # Setter for video title
    def set_title(self, title):
        self.__title = title
    
    # Getter for video description
    def get_description(self):
        return self.__description

    # Setter for video description
    def set_description(self, description):
        self.__description = description

# Video Player class
class VideoPlayer:
    @log_action
    def play(self):
        print("Playing video...")

# Class with multiple inheritance
class Video(VideoPlayer, VideoDetails):
    def __init__(self, title, description):
        VideoPlayer.__init__(self)
        VideoDetails.__init__(self, title, description)

# A class to manage the entire interface
class YouTubeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube-like Interface")
        self.root.geometry("800x600")

        # Current video being played
        self.current_video = Video("Default Video Title", "Default video description.")

        # Create main UI components
        self.create_video_frame()
        self.create_recommendation_frame()

    @log_click
    def create_video_frame(self):
        # Frame for video and details (left side)
        self.video_frame = tk.Frame(self.root, width=600, height=400, bg="black")
        self.video_frame.pack(side="left", fill="both", expand=True, padx=10, pady=10)

        # Video title label
        self.video_title = tk.Label(self.video_frame, text=self.current_video.get_title(), font=("Helvetica", 18), bg="black", fg="white")
        self.video_title.pack(pady=10)

        # Placeholder for video play area
        self.video_placeholder = tk.Label(self.video_frame, text="Video Player Placeholder", bg="black", fg="white", font=("Helvetica", 12))
        self.video_placeholder.pack(expand=True)

        # Play button (using the StyledButton class with method overriding)
        self.play_button = StyledButton(self.video_frame, "Play", command=self.play_video, bg="red", fg="white")
        self.play_button.pack(pady=10)

        # Video description label
        self.video_description = tk.Label(self.video_frame, text=self.current_video.get_description(), wraplength=500, justify="left", font=("Helvetica", 12), bg="black", fg="white")
        self.video_description.pack(pady=10)

    @log_click
    def create_recommendation_frame(self):
        # Frame for recommended videos (right side)
        self.recommend_frame = tk.Frame(self.root, width=200, height=400)
        self.recommend_frame.pack(side="right", fill="both", padx=10, pady=10)

        # Recommended video label
        recommend_label = tk.Label(self.recommend_frame, text="Recommended Videos", font=("Helvetica", 14))
        recommend_label.pack(pady=10)

        # List of recommended videos
        self.recommendations = [
            Video("Video 1", "Description for Video 1"),
            Video("Video 2", "Description for Video 2"),
            Video("Video 3", "Description for Video 3"),
        ]

        # Scrollable listbox for recommended videos
        self.recommend_list = tk.Listbox(self.recommend_frame, height=10, font=("Helvetica", 12))
        for video in self.recommendations:
            self.recommend_list.insert(tk.END, video.get_title())
        
        self.recommend_list.pack(padx=10, pady=10)

        # Bind the selection event to the listbox
        self.recommend_list.bind('<<ListboxSelect>>', self.on_select)

    @log_click
    def play_video(self):
        self.current_video.play()

    # Handle selection from the recommended video list
    @log_click
    def on_select(self, event):
        widget = event.widget
        selection = widget.curselection()
        if selection:
            selected_video = self.recommendations[selection[0]]
            self.update_video(selected_video)

    # Update video details when a new video is selected
    @log_action
    def update_video(self, video):
        self.current_video = video
        self.video_title.config(text=self.current_video.get_title())
        self.video_description.config(text=self.current_video.get_description())

# Run the main event loop
root = tk.Tk()
app = YouTubeApp(root)
root.mainloop()
