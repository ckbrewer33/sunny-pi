import customtkinter
import current_power

app_window_size = '800x480'
app_title = 'Sunny Pi'
app_system_total_power = 7100
app_widget_padding = 10

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry(app_window_size)
        self.title(app_title)
        
        self.current_power = current_power.CurrentPower(self,
                                                        total_power=app_system_total_power)
        self.current_power.update_power(5136)
        self.current_power.grid(row=0,
                                padx=app_widget_padding,
                                pady=app_widget_padding)


if __name__ == "__main__":
    app = App()
    app.mainloop()
