from django.apps import AppConfig


class ImageboardConfig(AppConfig):
    name = 'imageboard'

    def ready(self):
        import imageboard.signals
