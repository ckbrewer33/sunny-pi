import customtkinter
import sunny_pi_frame

class CurrentPowerWidget(sunny_pi_frame.SunnyPiFrame):
    def __init__(self,
                 *args,
                 total_power=1,
                 **kwargs):

        super().__init__(*args, **kwargs)
        self.total_power = total_power

        self.header = customtkinter.CTkLabel(self, text='Current PV Power')
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.progress_bar = customtkinter.CTkProgressBar(self)
        self.progress_bar.set(0.25)
        self.progress_bar.grid(row=1, column=0, padx=15)

        self.power_value_label = customtkinter.CTkLabel(self, text='Loading...')
        self.power_value_label.grid(row=2, column=0)

    def update_power(self, power_value):
      self.progress_bar.set(power_value / self.total_power)
      self.power_value_label.configure(text=self.get_power_label_string(power_value))
      
    def get_power_label_string(self, power_value):
      return str(power_value) + ' W'
