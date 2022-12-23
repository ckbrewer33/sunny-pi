import customtkinter
import sunny_pi_frame

class PvEnergyWidget(sunny_pi_frame.SunnyPiFrame):
    def __init__(self,
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.header = customtkinter.CTkLabel(self, text='PV Energy')
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.power_today_label = customtkinter.CTkLabel(self, text='Loading...')
        self.power_today_label.grid(row=2, column=0)

        self.power_total_label = customtkinter.CTkLabel(self, text='Loading...')
        self.power_total_label.grid(row=3, column=0)

    def set_today_energy(self, energy_today):
      label_text = str(energy_today) + 'kWh'
      self.power_today_label.configure(text=label_text)
      
    def set_total_energy(self, energy_total):
      label_text = str(energy_total) + 'MWh'
      self.power_total_label.configure(text=label_text)

