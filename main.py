import customtkinter
import current_power_widget
import pv_energy_widget
import weather_widget

app_window_size = '800x480'
app_title = 'Sunny Pi'
app_system_total_power = 7100
app_widget_padding = 10

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        
        self.geometry(app_window_size)
        self.title(app_title)
        
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure((0, 1), weight=1)

        self.init_current_power_widget()
        self.init_pv_energy_widget()
        self.init_weather_widget()

    def init_current_power_widget(self):
        self.current_power = current_power_widget.CurrentPowerWidget(self,
                                                        total_power=app_system_total_power)
        self.current_power.update_power(5136)
        self.current_power.grid(row=0,
                                column=0,
                                padx=app_widget_padding,
                                pady=app_widget_padding)

    def init_pv_energy_widget(self):
        self.pv_energy = pv_energy_widget.PvEnergyWidget(self)
        self.pv_energy.set_today_energy(21.09)
        self.pv_energy.set_total_energy(123)
        self.pv_energy.grid(row=0,
                            column=1,
                            padx=app_widget_padding,
                            pady=app_widget_padding)

    def init_weather_widget(self):
      self.weather_widget = weather_widget.WeatherWidget(self)
      self.weather_widget.set_temperature(-7)
      self.weather_widget.set_current_conditions('Cloudy')
      self.weather_widget.grid(row=0,
                               column=2,
                               padx=app_widget_padding,
                               pady=app_widget_padding)

if __name__ == "__main__":
    app = App()
    app.mainloop()
