import customtkinter

"""A shared frame for all sunny-pi widget groups"""
class SunnyPiFrame(customtkinter.CTkFrame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.configure(corner_radius=8,
                       fg_color='white',
                       width=300,
                       height=200)