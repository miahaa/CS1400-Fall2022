# CS1400 Assignment 3: Driving Cost Calculator by Thu Ha
# Add the functions for the assignment below here.

def calculate_gas_vehicle_trip_cost (distance, MPG_for_a_car, gascost):          #Define the function that calculate the cost of a trip for a gas vehicle using parameters for the trip distance (MILES) , the vehicle efficiency (MPG), and the cost of a gallon of gas (GASCOST)
    number_of_gallon_of_gas_needed = distance / MPG_for_a_car
    trip_cost_for_gas_vehicle = number_of_gallon_of_gas_needed * gascost
    return (trip_cost_for_gas_vehicle)

def calculate_electric_vehicle_trip_cost (distance, MPKWH_for_an_electric_car, electric_cost):        #Define the function that calculate the cost of a trip for an electric vehicle using parameters for the trip distance (MILES) , the vehicle efficiency in miles per kilowatt-hour (MPKWH)
    amount_of_electricity_used = distance / MPKWH_for_an_electric_car
    trip_cost_for_electric_vehicle = amount_of_electricity_used * electric_cost
    return (trip_cost_for_electric_vehicle)

def print_trip_cost_table (gascost, electric_cost, MPG_for_a_truck, MPG_for_a_car, MPKWH_for_an_electric_car):         #Define the function that display (print) a table of trip distances and the costs for a truck, a car, and electric car to drive that distance
    for distance in range(50, 550, 50):
        trip_cost_for_truck = calculate_gas_vehicle_trip_cost(distance, MPG_for_a_truck, gascost)
        trip_cost_for_gas_car = calculate_gas_vehicle_trip_cost(distance, MPG_for_a_car, gascost)
        trip_cost_for_electric_car = calculate_electric_vehicle_trip_cost(distance, MPKWH_for_an_electric_car, electric_cost)
        print("For a trip of", distance, "miles,", "the costs are truck:", "$" + str(round(trip_cost_for_truck)) + ",", "car:", "$" + str(round(trip_cost_for_gas_car)) + ",", "electric:", "$" + str(round(trip_cost_for_electric_car)))

# Keep this main function
def main():
    gascost = float(input("Please enter the price of gasoline in dollar per gallon: "))
    electric_cost = float(input("Please enter the price of electricity in dollar per kilowatt-hour: "))
    MPG_for_a_car = float(25.4)
    MPG_for_a_truck = float(14)
    MPKWH_for_an_electric_car = float(4.5)
    print_trip_cost_table(gascost, electric_cost, MPG_for_a_truck, MPG_for_a_car, MPKWH_for_an_electric_car)



# Keep these lines. It helps Python run the program correctly.
if __name__ == "__main__":
    main()