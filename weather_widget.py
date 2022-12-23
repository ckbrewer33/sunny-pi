import customtkinter
import sunny_pi_frame

class WeatherWidget(sunny_pi_frame.SunnyPiFrame):
    def __init__(self,
                 *args,
                 **kwargs):

        super().__init__(*args, **kwargs)

        self.header = customtkinter.CTkLabel(self, text='Current Weather')
        self.header.grid(row=0, column=0, padx=10, pady=10)

        self.temp_label = customtkinter.CTkLabel(self, text='Loading...')
        self.temp_label.grid(row=2, column=0)

        self.current_conditions_label = customtkinter.CTkLabel(self, text='Cloudy')
        self.current_conditions_label.grid(row=3, column=0)
        
    def _get_temp_label(self, temperature):
      degree_symbol = u'\N{DEGREE SIGN}'
      return f'{temperature}{degree_symbol} C'
    
    def set_temperature(self, temperature):
      label_value = self._get_temp_label(temperature)
      self.temp_label.configure(text=label_value)
    
    def set_current_conditions(self, current_conditions):
      self.current_conditions_label.configure(text=current_conditions)
