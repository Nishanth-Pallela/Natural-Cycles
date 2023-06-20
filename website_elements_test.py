import streamlit as st

answers = ['Condensation', "Evaporation", "Precipitation", "Transpiration"]
st.title("Read the following and answer the questions.")
st.subheader("Biological cycles are important for life. They also make elements balanced."
             " The three main ones are the Water Cycle, the Carbon Cycle, and the Nitrogen Cycle.")

st.write("The Water Cycle is perhaps the most common cycle. It also is the most simplest out of the three."
         " The Water Cycle explains how water moves around. The first two steps are Evaporation and Transpiration. "
         "Evaporation is a change of state with water. Liquid water gets heated up, usually by the sun,"
         " and turns into water vapor. Water vapor is the gas state of water."
         " Transpiration happens when plants release water vapor into the atmosphere."
         " What happens next is condensation. Up in the atmosphere where the water vapor that made it up there resides,"
         " the vapor starts to turn back into liquid."
         " This happens because the atmosphere is much colder than the vapor."
         " It causes a change in the state of the water. Then the water droplets form clouds."
         " Precipitation is when water, snow, hail, or sleet fall from the clouds. This is caused by the clouds"
         " getting to heavy. When it does become heavy, water droplets fall. Hail is ice falling from the clouds. "
         "Sleet is a mix of any of the three. \n  \n  The Carbon Cycle is a cycle that many don’t pay attention to."
         " More and more people should because of global warming."
         " There are many ways for carbon to be released into the atmosphere,"
         " and to balance the many ways for it to end up in the atmosphere there"
         " is only one way it can leave. If we start with photosynthesis,"
         " the only way carbon gets removed from the atmosphere, "
         "then we have to look at plants. Plants take CO2 from the"
         " environment and use it to make food (glucose)."
         " If the plant dies, then it can either become fossilized"
         " over a long period of time or it can be decomposed by microorganisms. "
         "The decomposition releases CO2 into the air."
         " Let’s say the plant gets eaten by an animal."
         " The animal now has all of that CO2 and if it di"
         "es then microorganisms will decompose it releasing "
         "CO2 into the air or it could fossilize. If the animal"
         " farts, it releases CO2 into the atmosphere. That animal"
         " may get eaten by another animal, and the whole process may"
         " repeat. Another thing about animals, when they breathe they m"
         "ay breathe CO2 and oxygen but in the end they release CO2. The ne"
         "xt part is combustion. We burn stuff, and burning stuff releases CO2 "
         "into the atmosphere. Let’s say a cow fossilized and turned into coal, "
         "we might burn it. This the second way dead things contribute CO2 into the atmosphere.")

st.radio(label="Which process happens before Precipitation? ", options=answers, key="radio")

if st.session_state["radio"] == "Condensation":
    st.text("Correct")
else:
    st.text('Incorrect')
