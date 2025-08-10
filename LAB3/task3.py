class Meter:
    def __init__(self, prev_reading, curr_reading, meter_type):
        self.prev_reading = prev_reading
        self.curr_reading = curr_reading
        self.meter_type = meter_type.lower()
        self.units_consumed = self.curr_reading - self.prev_reading
        self.cost_per_unit = self.calculate_cost_per_unit()
        self.total_bill = self.units_consumed * self.cost_per_unit

    def calculate_cost_per_unit(self):
        units = self.units_consumed
        if self.meter_type == 'residential':
            if units <= 100:
                return 2
            elif units <= 250:
                return 4
            else:
                return 6
        elif self.meter_type == 'commercial':
            if units <= 100:
                return 4
            elif units <= 250:
                return 8
            else:
                return 12
        else:
            return 0

    def is_valid(self):
        if self.curr_reading < self.prev_reading:
            print("Current reading cannot be less than previous reading.")
            return False
        if self.meter_type not in ['residential', 'commercial']:
            print("Invalid meter type entered.")
            return False
        return True

    def print_bill(self):
        print("\n------ Electricity Bill ------")
        print(f"Meter Type        : {self.meter_type.capitalize()}")
        print(f"Previous Reading  : {self.prev_reading}")
        print(f"Current Reading   : {self.curr_reading}")
        print(f"Units Consumed    : {self.units_consumed}")
        print(f"Cost per Unit     : {self.cost_per_unit} rupees")
        print(f"Total Bill Amount : {self.total_bill} rupees")
        print("-----------------------------\n")

def main():
    try:
        prev_reading = float(input("Enter previous month reading: "))
        curr_reading = float(input("Enter current month reading: "))
        meter_type = input("Is the meter residential or commercial? (Enter 'residential' or 'commercial'): ").strip()
        meter = Meter(prev_reading, curr_reading, meter_type)
        if meter.is_valid():
            meter.print_bill()
    except ValueError:
        print("Invalid input. Please enter numeric values for readings.")

if __name__ == "__main__":
    main()


