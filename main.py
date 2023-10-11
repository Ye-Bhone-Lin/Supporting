import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title='Service For My One & Only', page_icon='❤️')
left_column, right_column = st.columns(2)

with right_column:
    st.image("human.png")

with left_column:
    st.title('The Service For My One & Only')
    name_text = st.text_input("Enter Your Name")

if name_text == "Ye's Holly":
    st.header('**Welcome to The Personal Service**')
    selected = option_menu(menu_title=None,
                       options=['If you feel tired or stressed, click this', 'If you feel lonely or miss, click this',"If you can't sleep or dream nightmares, click this"],
                       icons=['balloon-heart', 'balloon-heart','balloon-heart'],
                       default_index=0,
                       orientation='horizontal')
    
    if selected == "If you feel tired or stressed, click this":
        st.image('hug.jpg')
        st.write("I know you have been through these hard times. At this time, please remember you have me, and don't hesitate to consult with me. You have the power to overcome these feelings. No matter what, I will listen with all my ears. I know you can do it, and don't give up. We can fight together. I always believe in you, and I am proud of what you are doing.")
        st.audio('tired.aac')
    
    elif selected == "If you feel lonely or miss, click this":
        st.image("miss.jpg")
        st.write("I want you to know that I will always be by your side, no matter what happens. You are incredibly valuable and worthy of love, just as you are. Your presence in my life brings immense joy, and I cherish the connection we share. Whenever you feel lonely, remember that I am here for you, and our bond is unbreakable. Stay strong, keep believing in yourself; I always believe in you, and never forget how special you are.")
        st.audio('Rec again.aac')
    
    elif selected == "If you can't sleep or dream nightmares, click this":
        st.image('virtual.jpeg')
        st.write("Don't worry, baby; I will always be by your side. Don't think too much, and relax your mind. When you dream a nightmare, drink water, relax, and try going back to sleep. Don't think about those nightmares again. Those nightmares cannot show up in real life. Don't think too much, baby. Remember that you have me.")
        st.audio("Gn.aac")
        st.write(":red[Here is the story in case you can't sleep again.]")
        st.audio("Story.aac")

    st.header('Love meter 🤪')
    love_meter = st.slider('How much do you love me xD', 0, 100, 0)

    if love_meter <= 99:
        st.write('Your love is too low to get a hug xD')
    
    else:
        st.write('Yayyyyyyy I will give you a hugggggggg <3')
        st.video('virtual_hug.mp4')
    
    if st.button("Let's call it a day"):
        st.write("Yayyyyyy!!! Well done for today, and you did a great job. I know you can do it and keep that momentum. I will always be proud of you, my lovely.")
else:  
    st.write('Please Write Your name Correctly otherwise you wont see anything')

