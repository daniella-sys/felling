class Kyiv:
      def __init__(self, title, years, famous, peoples):
          self.title = title
          self.years = years
          self.famous = famous
          self.peoples = peoples
#Enter information
      def display_info(self):
          print(f"title: {self.title}, years: {self.years}, famous: {self.famous}, peoples: {self.peoples}")

kiew1 = Kyiv("Kyiv", 482, True, "1 milion")
kiew1.display_info()







