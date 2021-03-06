from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
import wikipedia
import requests

Builder.load_file('frontend.kv')


class FirstScreen(Screen):

    def get_image_link(self):
        # Get the user query from the text input box
        query = self.manager.current_screen.ids.user_query.text
        print(query)
        # Get the wikipedia page and extract list of image links
        page = wikipedia.page(query)
        # Get the first image returned
        image = page.images[0]
        return image

    def download_image(self):
        # Download the image
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(self.get_image_link(), headers=headers)
        # Write the returned image into a file locally
        image_path = 'files/image.jpg'
        with open(image_path, 'wb') as file:
            file.write(response.content)
        return image_path

    def set_image(self):
        # Set the downloaded image in the image widget
        self.manager.current_screen.ids.img.source = self.download_image()


class RootWidget(ScreenManager):
    pass


class MainApp(App):

    def build(self):
        return RootWidget()


MainApp().run()
