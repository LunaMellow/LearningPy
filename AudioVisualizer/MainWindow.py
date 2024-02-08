from pyglet import *
from pyglet.window import *
from pyglet.graphics import *
from random import *
from pydub import AudioSegment
import numpy as np

class MainWindow(Window):
    CIRCLE_RADIUS = 10
    NUM_CIRCLES = 100
    MAX_VELOCITY = 100

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Window size
        self.size = list(self.get_size())
        self.wx, self.wy = self.size[0], self.size[1]

        self.batch = Batch()

        self.circles = [pyglet.shapes.Circle(
            x=self.wx,
            y=self.wy,
            radius=self.CIRCLE_RADIUS,
            color=(randint(125, 175), randint(25, 75), randint(100, 255)),
            batch=self.batch,
        ) for _ in range(self.NUM_CIRCLES)]

        # Load the audio file
        audio_path = "/Users/lunasofiebergh/PycharmProjects/LearningPy/AudioVisualizer/Assets/Waves.mp3"
        audio = AudioSegment.from_mp3(audio_path)
        samples = np.array(audio.get_array_of_samples())
        fft_result = np.fft.fft(samples)
        self.amplitudes = np.abs(fft_result)

        self.amplitude_index = 0

        # Create a player object to play the audio
        self.player = pyglet.media.Player()
        self.player.queue(pyglet.media.load(audio_path))
        self.player.play()

    def on_draw(self):
        # Window clear
        window.clear()

        # Draw fps for performance insights
        fps_display.draw()

        self.batch.draw()

    # Function to update circle positions
    def update(self, dt):
        try:
            amplitude = self.amplitudes[self.amplitude_index]
            self.amplitude_index += 1

            for circle in self.circles:
                # Calculate velocity based on amplitude
                velocity_x = uniform(-amplitude, amplitude) * 0.00001
                velocity_y = uniform(-amplitude, amplitude) * 0.00001

                # Update circle position
                circle.x += velocity_x * dt
                circle.y += velocity_y * dt

                # Wrap around the window edges
                if circle.x < 0:
                    circle.x = self.wx
                elif circle.x > self.wx:
                    circle.x = 0
                if circle.y < 0:
                    circle.y = self.wy
                elif circle.y > self.wy:
                    circle.y = 0
        except Exception as e:
            print("Error:", e)


if __name__ == '__main__':
    # Window properties
    window = MainWindow(caption="Moving Circles", width=800, height=600, resizable=False)

    # Fps Display
    fps_display = FPSDisplay(window)

    # Run the application
    pyglet.clock.schedule_interval(window.update, 1 / 60)
    pyglet.app.run()
