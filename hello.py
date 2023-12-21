import streamlit as st
import time

# Basic Function

# Title used to add title
st.title('Hello, Streamlit!')

# Header used to add header
st.header('Machine Learning')

# Subheader used to add subheader
st.subheader('Machine Learning with Streamlit')

# Text used to add text
st.text("Hello this is text")

# Markdown
st.markdown("# This is a markdown")
st.markdown("## This is a markdown")
st.markdown("### This is a markdown")
st.markdown(":apple:")

# success show success
st.success("Success")

# warning show warning
st.warning("Warning")

# To give information
st.info("This is an information")

# error show error
st.error("Error")

# Write text
st.write("Text with write")

# Writing python inbuilt function range()
st.write(range(10))

# To display mathematical expression
st.latex(r''' a+bx^2+c ''')

# To display image
st.image("streamlit.png", width=500)



# Widgets

# Checkbox
st.checkbox("Login")
st.checkbox("Logout", True)
if st.checkbox("Show/Hide"):
    # display the text if the checkbox returns True value
    st.text("Showing the widget")

# Button
st.button("Click")
if(st.button("About")):
    st.text("Welcome To World of Generative AI!!!")

# Radio
st.radio("Pick your gender", ['Male', 'Female', 'Others'])  
status = st.radio("Select Gender: ", ('Male', 'Female')) 
if (status == 'Male'):
    st.success("Male")
else:
    st.success("Female")  

# Selection box
st.selectbox("pick your course",["DS","ML","CV","NLP"])
hobby = st.selectbox("Hobbies: ",
                     ['Dancing', 'Reading', 'Sports'])
st.write("Your hobby is: ", hobby)

# Multiselect
st.multiselect("select your favourite sports",["Soccer","Cricket","Football","Hockey","Tennis"])
hobbies = st.multiselect("Hobbies: ",
                         ['Dancing', 'Reading', 'Sports'])
st.write("You selected", len(hobbies), 'hobbies')

# SelectSlider
st.select_slider("Select your age", options=[18, 20, 22, 24, 26, 28, 30])

# Slider
level = st.slider("Select the level", 1, 5)
st.text('Selected: {}'.format(level))

# NumberInput
st.number_input("Select the level", 1, 10)

# TextInput
st.text_input("Your name")
st.text_input("Your name","Type something here")
st.text_input("Enter your email", placeholder="Enter email")
name = st.text_input("Enter Your name", "Type Here ...")
if(st.button('Submit')):
    result = name.title()
    st.success(result)

# DateInput
st.date_input("Your joining date")

# TimeInput
st.time_input("Current time")

# TextArea
st.text_area("Tell us about yourself", placeholder="Type here ...")

# Upload file or folder
st.file_uploader("Upload a file")
st.file_uploader("Upload a file", type=["pdf", "png", "jpg"])

# ColorPicker
st.color_picker("Pick your favorite color")

# Progress
st.progress(50)

# Spinner
with st.spinner("just wait"):
    time.sleep(2)

# Balloon
st.balloons()

# Sidebar
st.sidebar.title("Hello World")
st.sidebar.text_input("Enter your name",placeholder="Enter name")
st.sidebar.text_input("Enter your password",placeholder="Enter password")
st.sidebar.button("Submit",key="Submit")
st.sidebar.radio("Submit",["Login","Logout"])
    
