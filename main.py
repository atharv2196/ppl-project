import streamlit as st

def fuel_available():#UDF
        st.title(":rainbow[Welcome to Invictus Fuel Station!]")#title of project
        
        a,b,c = st.columns(3)#for aligning in centre
        with b   :
         st.image('icon.jpg')  #inserted image for logo
         st.write(":green[Types of Fuel Available]")
         st.write("CNG : 84 rs/kg")
         st.write("Petrol : 110 rs/lit")
         st.write("Diesel : 90 rs/lit")
         st.write("EV Charge : 4 rs/kWh")

def fuel_cost(fuel_type):#UDF for fuel cost using set
    cost = {
        "CNG": 84,
        "Petrol": 110,
        "Diesel": 90,
        "EV Charge": 4
    }
    return cost.get(fuel_type, 0)

def main():#UDF main for slecting fuel type and fill method
 
   
    fuel_available()
    
    fuel_choice = st.selectbox(
        ":green[Please select a fuel type:]",
        ["CNG", "Petrol", "Diesel", "EV Charge"]
    )#selecting fuel type to fill using select box

    st.write(f":green[You have selected: {fuel_choice}]")

    fill_type = st.radio(
        ":green[How would you like to fill the fuel?]",
        ("By money", "By quantity")
    )#choosing how to fill fuel

    if fill_type == "By money":
        money = st.number_input(f":green[Enter the amount of money to fill {fuel_choice}:]", min_value=0.0, step=10.0)
        if money > 0:
            cost = fuel_cost(fuel_choice)
            if st.button(":rainbow[ Please Click here to know amount of fuel you will recive]"):

             if fuel_choice == "CNG":
                st.write(f"#### You will receive :green[{money / cost}] kg of CNG.")
             
             elif fuel_choice == "Petrol":
                st.write(f"#### You will receive :green[{money / cost}] liters of Petrol.")

             elif fuel_choice == "Diesel":
                st.write(f"#### You will receive :green[{money / cost}] liters of Diesel.")

             elif fuel_choice == "EV Charge":
                st.write(f"#### You will receive :green[{money / cost}] kWh of EV Charge.")

            

    elif fill_type == "By quantity":
        quantity = st.number_input(f":green[Enter the quantity of {fuel_choice} to fill:]", min_value=0.0, step=0.5)
        if quantity > 0:
            cost = fuel_cost(fuel_choice)
            if st.button(":rainbow[Please click here to amount of money to pay fuel]"):
             st.write(f"#### The total cost for :green[{quantity}] units of :green[{fuel_choice}] is :green[{quantity * cost}] rs.")
                
    if st.button(":red[EXIT]"):    #the exit button with message
        st.write("\n Thank you for visiting the fuel station! Please drive safely.")
   

if __name__ == "__main__":
    main() #calling main function which includes fuel_available UDF too
