import streamlit as st
from PIL import Image
import random
import pickle
import numpy
import pandas
import sklearn
from random import choice


#image = Image.open('iip_logo.jpg')

#st.image(image, width = 150)
if __name__ == '__main__':

    # Display IIP logo

    col27, col28, col29 = st.columns([2, 2, 2])
    with col27:
        st.write("")

    with col28:

        image = Image.open('iip_logo.jpg')
        st.image(image, width=150, caption="India In Pixels")

    with col29:
        st.write("")


    st.title("Shark-Tank Simulator")

    image = Image.open('tank.jpeg')

    st.image(image)


    st.subheader("Ever wondered what it takes to impress the sharks and raise funds for your business idea?")

    st.subheader("This is the perfect application that simulates your experience and predicts the likelihood of investment by each shark.")

    st.header("What is Shark Tank?")
    st.write("An adaptation of the popular Japanese show – 'Tigers of money', which became 'Dragon’s Den' in UK and "
             "finally  took the name ‘Shark Tank’ in US. A panel of investors judge the pitches from entrepreneurs and "
             "invest in brilliant (and also sometimes weird) ideas.")

    st.header("How to use this application?")
    st.write("Simple! Answer the questions below and hit the 'Pitch your idea!' button. Our sharks will give"
             "their decision based on a number of factors. This application is trained using "
             "sophisticated machine learning algorithm on the (limited to 1 season) data available "
             "on Shark Tank India.")

    st.text("Are you ready?")

    st.write("[Disclaimer: Any loss of funds or insult by judges will not be the responsibility of this application]")

    st.header("Let's begin")

    #n = st.text_input('Enter your Name')
    #a = st.selectbox('Enter your age',
    #('18-20', '21-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60+'))
    #idea = st.text_input('Name of your Business')
    #prod = st.text_input("Brief description of your product")

    with st.form(key='my_form'):
        col2, col1 = st.columns([3,3])

        with col1:
            n = st.text_input('Enter your Name')
            a = st.selectbox('Enter your age',
                             ('18-20', '21-25', '25-30', '30-35', '35-40', '40-45', '45-50', '50-55', '55-60', '60+'))

        with col2:
            st.image("peyush_asks1.jpg")



        col3, col4 = st.columns([3,3])

        with col4:
            idea = st.text_input('Name of your Business')
            prod = st.text_input("Brief description of your product")

        with col3:
            st.image("aman_asks1.jpg")


        col6, col5 = st.columns([3,3])

        with col5:
            city = st.selectbox('Enter your City',
                             ('Adoni',
     'Agartala',
     'Agra',
     'Ahmedabad',
     'Ahmednagar',
     'Aizawl',
     'Ajmer',
     'Akola',
     'Alappuzha',
     'Aligarh',
     'Allahabad',
     'Alwar',
     'Amaravati',
     'Ambala',
     'Ambarnath',
     'Ambattur',
     'Amravati',
     'Amritsar',
     'Amroha',
     'Anand',
     'Anantapur',
     'Anantapuram',
     'Anantnag',
     'Arrah',
     'Asansol',
     'Aurangabad',
     'Aurangabad',
     'Avadi',
     'Bahraich',
     'Ballia',
     'Bally',
     'Bengaluru',
     'Baranagar',
     'Barasat',
     'Bardhaman',
     'Bareilly',
     'Bathinda',
     'Begusarai',
     'Belgaum',
     'Bellary',
     'Berhampore',
     'Berhampur',
     'Bettiah',
     'Bhagalpur',
     'Bhalswa Jahangir Pur',
     'Bharatpur',
     'Bhatpara',
     'Bhavnagar',
     'Bhilai',
     'Bhilwara',
     'Bhimavaram',
     'Bhind',
     'Bhiwandi',
     'Bhiwani',
     'Bhopal',
     'Bhubaneswar',
     'Bhusawal',
     'Bidar',
     'Bidhannagar',
     'Bihar Sharif',
     'Bijapur',
     'Bikaner',
     'Bilaspur',
     'Bokaro',
     'Bongaigaon',
     'Budaun',
     'Bulandshahr',
     'Burhanpur',
     'Buxar',
     'Chandigarh',
     'Chandrapur',
     'Chapra',
     'Chennai',
     'Chinsurah',
     'Chittoor',
     'Coimbatore',
     'Cuttack',
     'Danapur',
     'Darbhanga',
     'Davanagere',
     'Dehradun',
     'Dehri',
     'Deoghar',
     'Dewas',
     'Dhanbad',
     'Dharmavaram',
     'Dhule',
     'Dibrugarh',
     'Dindigul',
     'Durg',
     'Durgapur',
     'Eluru',
     'Erode',
     'Etawah',
     'Faridabad',
     'Farrukhabad',
     'Fatehpur',
     'Firozabad',
     'Gandhidham',
     'Gandhinagar',
     'Gangtok',
     'Gaya',
     'Ghaziabad',
     'Giridih',
     'Gopalpur',
     'Gorakhpur',
     'Gudivada',
     'Gulbarga',
     'Guna',
     'Guntakal',
     'Guntur',
     'Gurgaon',
     'Guwahati',
     'Gwalior',
     'Hajipur',
     'Haldia',
     'Hapur',
     'Haridwar',
     'Hazaribagh',
     'Hindupur',
     'Hospet',
     'Hosur',
     'Howrah',
     'Hubli–Dharwad',
     'Hyderabad',
     'Ichalkaranji',
     'Imphal',
     'Indore',
     'Jabalpur',
     'Jaipur',
     'Jalandhar',
     'Jalgaon',
     'Jalna',
     'Jamalpur',
     'Jammu',
     'Jamnagar',
     'Jamshedpur',
     'Jaunpur',
     'Jehanabad',
     'Jhansi',
     'Jodhpur',
     'Jorhat',
     'Junagadh',
     'Kadapa',
     'Kakinada',
     'Kalyan-Dombivli',
     'Kamarhati',
     'Kanpur',
     'Karaikudi',
     'Karawal Nagar',
     'Karimnagar',
     'Karnal',
     'Karur',
     'Katihar',
     'Katni',
     'Kavali',
     'Khammam',
     'Khandwa',
     'Kharagpur',
     'Khora, Ghaziabad',
     'Kirari Suleman Nagar',
     'Kishanganj',
     'Kochi',
     'Kolhapur',
     'Kolkata',
     'Kollam',
     'Korba',
     'Kota',
     'Kottayam',
     'Kozhikode',
     'Kulti',
     'Kumbakonam',
     'Kurnool',
     'Latur',
     'Loni',
     'Lucknow',
     'Ludhiana',
     'Machilipatnam',
     'Madanapalle',
     'Madhyamgram',
     'Madurai',
     'Mahbubnagar',
     'Maheshtala',
     'Malda',
     'Malegaon',
     'Mangalore',
     'Mango',
     'Mathura',
     'Mau',
     'Medininagar',
     'Meerut',
     'Mehsana',
     'Mira-Bhayandar',
     'Miryalaguda',
     'Mirzapur',
     'Moradabad',
     'Morbi',
     'Morena',
     'Motihari',
     'Mumbai',
     'Munger',
     'Muzaffarnagar',
     'Muzaffarpur',
     'Mysore',
     'Nadiad',
     'Nagaon',
     'Nagercoil',
     'Nagpur',
     'Naihati',
     'Nanded',
     'Nandyal',
     'Nangloi Jat',
     'Narasaraopet',
     'Nashik',
     'Navi Mumbai',
     'Nellore',
     'NCT of Delhi',
     'Nizamabad',
     'Noida',
     'North Dumdum',
     'Ongole',
     'Orai',
     'Pali',
     'Pallavaram',
     'Panchkula',
     'Panihati',
     'Panipat',
     'Panvel',
     'Parbhani',
     'Patiala',
     'Patna',
     'Phagwara',
     'Phusro',
     'Pimpri-Chinchwad',
     'Pondicherry',
     'Port Blair',
     'Proddatur',
     'Pudukkottai',
     'Pune',
     'Puri',
     'Purnia',
     'Raebareli',
     'Raichur',
     'Raiganj',
     'Raipur',
     'Rajahmundry',
     'Rajkot',
     'Rajpur Sonarpur',
     'Ramagundam',
     'Ramgarh',
     'Rampur',
     'Ranchi',
     'Ratlam',
     'Rewa',
     'Rohtak',
     'Rourkela',
     'Sagar',
     'Saharanpur',
     'Saharsa',
     'Salem',
     'Sambalpur',
     'Sambhal',
     'Sangli-Miraj & Kupwad',
     'Sasaram',
     'Satara',
     'Satna',
     'Secunderabad',
     'Serampore',
     'Shahjahanpur',
     'Shimla',
     'Shimoga',
     'Shivpuri',
     'Sikar',
     'Silchar',
     'Siliguri',
     'Singrauli',
     'Sirsa',
     'Siwan',
     'Solapur',
     'Sonipat',
     'South Dumdum',
     'Sri Ganganagar',
     'Srikakulam',
     'Srinagar',
     'Sultan Pur Majra',
     'Surat',
     'Surendranagar Dudhrej',
     'Suryapet',
     'Tadepalligudem',
     'Tadipatri',
     'Tenali',
     'Tezpur',
     'Thane',
     'Thanjavur',
     'Thiruvananthapuram',
     'Thoothukudi',
     'Thrissur',
     'Tinsukia',
     'Tiruchirappalli',
     'Tirunelveli',
     'Tirupati',
     'Tiruppur',
     'Tiruvottiyur',
     'Tumkur',
     'Udaipur',
     'Udupi',
     'Ujjain',
     'Ulhasnagar',
     'Uluberia',
     'Unnao',
     'Uzhavarkarai',
     'Vadodara',
     'Varanasi',
     'Vasai-Virar',
     'Vasco Da Gama',
     'Vellore',
     'Vijayanagaram',
     'Vijayawada',
     'Visakhapatnam',
     'Warangal',
     'Yamunanagar'))

            dict_city = {'Faridabad': 0, 'Sanand': 1, 'NCT of Delhi': 2, 'Bengaluru': 3, 'Pune': 4, 'Jalna': 5, 'Darbhanga': 6,
                        'Ahmedabad': 7, 'Nashik': 8, 'Mumbai': 9, 'Nagpur': 10, 'Hyderabad': 11, 'Alappuzha': 12,
                        'Vadodara': 13, 'Phari': 14, 'Chennai': 15, 'Jaipur': 16, 'Ghogali': 17, 'Kolkata': 18,
                        'Indore': 19, 'Valsad': 20, 'Panipat': 21, 'Dombivali': 22, 'Pimpri-Chinchwad': 23,
                        'Ludhiana': 24, 'Gurgaon': 25, 'Ernakulam': 26, 'Pithampura': 27, 'Mira Bhayandar': 28,
                        'Jammu': 29, 'Pirangut': 30, 'Secunderabad': 31, 'Malegaon': 32, 'Dehradun': 33,
                        'Surat': 34, 'Lucknow': 35, 'Rajkot': 36, 'Noida': 37, 'Panaji': 38}

            random_city = random.randint(1, 38)

            if city in dict_city:
                city = int(dict_city[city])
            else:
                city = int(random_city)



            state = st.selectbox('Enter your State',
                                 ("Andhra Pradesh","Arunachal Pradesh ","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal Pradesh","Jammu and Kashmir","Jharkhand","Karnataka","Kerala","Madhya Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil Nadu","Telangana","Tripura","Uttar Pradesh","Uttarakhand","West Bengal",
                                  "Andaman and Nicobar Islands","Chandigarh","Dadra and Nagar Haveli","Daman and Diu",
                                  "Lakshadweep","NCT of Delhi","Puducherry"))

            dict_state = {'Haryana' : 0, 'Gujarat' : 1, 'NCT of Delhi' : 2, 'Karnataka' : 3, 'Maharashtra' : 4,
                            'Bihar' : 5, 'Telangana' : 6, 'Kerala' : 7, 'West Bengal' : 8, 'Tamil Nadu' : 9,
                            'Rajasthan' : 10, 'Madhya Pradesh' : 11, 'Punjab' : 12, 'Jammu & Kashmir' : 13,
                            'Uttarakhand' : 14, 'Uttar Pradesh' : 15, 'Goa' : 16}

            random_state = random.randint(1, 16)

            if state in dict_state:
                state = int(dict_state[state])
            else:
                state = int(random_state)



        with col6:
            st.image("vineeta asks1.jpg")


        col7, col8 = st.columns([3,3])

        with col8:
            sec = st.selectbox('Select Sector',
                               ("Food and drinks", "Service", "Clothing", "Healthcare", "Tourism",
                                "Automobiles", "Beauty/Cosmetics", "Sociology", "Construction",
                                "Tech", "Other", "Nature friendly", "Entertainment", "Clothing & Accessories",
                                "Agro", "Cosmetics", "Finance", "Sports", "Education"))

            dict_sector = {"Food and drinks": 0, "Service": 1, "Clothing": 2, "Healthcare": 3, "Tourism": 4,
                           "Automobiles": 5, "Beauty/Cosmetics": 6, "Sociology": 7, "Construction": 8,
                           "Tech": 9, "Other": 10, "Nature friendly": 11, "Entertainment": 12, "Clothing & Accessories": 13,
                           "Agro": 14, "Cosmetics": 15, "Finance": 16, "Sports": 17, "Education": 18}

            if sec in dict_sector:
                sec = int(dict_sector[sec])


            exp = st.select_slider(
             'Select your experience in years',
             options=['0-2', '2-4', '4-8', '8+'])

        with col7:
            st.image("namita_asks1.jpg")



        col10, col9 = st.columns([3,3])

        with col9:
            equ = st.number_input('Enter the equity you wish to offer (%)', min_value=0.0, max_value=100.0)
            cap = st.number_input('Enter the capital you want to raise in Lakhs (INR)', min_value=1)

        with col10:
            st.image("ashneer_asks1.jpg")

        cap = cap*100000
        equ_temp = equ
        cap_temp = cap



        col11, col12 = st.columns([3,3])

        with col12:
            mod = st.radio(
             "What is your business model?",
             ('B2B (Businesses serving other businesses)', 'B2C (Businesses serving customers direclty)'))

            holders = st.select_slider('How many owners does your company currently have',
             options=['1', '2', '3', '4', '5', '5+'])

        with col11:
            st.image("anupam_asks1.jpg")
            
        
        
        
        col49, col50 = st.columns([3, 3])

        with col50:
            rev = st.number_input('Annual Revenue generated by your company in INR (in Lakhs)', min_value=0.0)

            debt = st.radio('Have you taken a debt before?',
                            ('Yes', 'No'))

        with col49:
            st.image("ghazal_asks1.jpg")



        #Loading the Model and doing Predictions




        with open('./KNN_Model_Aman2.pkl', 'rb') as file:
            model_aman = pickle.load(file)

        with open('./KNN_Model_Anupam1.pkl', 'rb') as file:
            model_anupam = pickle.load(file)

        with open('./KNN_Model_Ashneer1.pkl', 'rb') as file:
            model_ashneer = pickle.load(file)

        with open('./KNN_Model_Ghazal1.pkl', 'rb') as file:
            model_ghazal = pickle.load(file)

        with open('./KNN_Model_Peyush2.pkl', 'rb') as file:
            model_peyush = pickle.load(file)

        with open('./KNN_Model_Vineeta1.pkl', 'rb') as file:
            model_vineeta = pickle.load(file)

        with open('./KNN_Model_Namita1.pkl', 'rb') as file:
            model_namita = pickle.load(file)

        input_lis = [city, state, sec, cap, equ]
        arr = numpy.array(input_lis)
        dff = pandas.DataFrame(arr)
        dff = dff.transpose()

        out_aman = model_aman.predict(dff)
        out_anupam = model_anupam.predict(dff)
        out_ashneer = model_ashneer.predict(dff)
        out_ghazal = model_ghazal.predict(dff)
        out_peyush = model_peyush.predict(dff)
        out_vineeta = model_vineeta.predict(dff)
        out_namita = model_namita.predict(dff)

        opt = ["No Deal"]



        #Output and counter-offer

        if st.form_submit_button("Pitch your idea!"):
            st.write("")
            st.subheader("Result")
            st.write("Welcome to Shark Tank ", n, ". Your idea of", prod, " seems good. Based on your inputs, the Sharks have come to a decision. Let's"
                                                  " start with Aman.")
            col13, col14 = st.columns([3, 3])
            with col13:
                st.write("")
                st.write("")
                st.write("")
                st.image("aman_asks.jpg")

            with col14:
                if out_aman == 1:
                    opt.append("Aman")
                    l = [1,-1]
                    choose = [1,2,3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_aman = equ_temp + random.randint(10,15)
                        cap_aman = cap_temp - choice(cap_down)
                        if cap_aman < 0.3*cap_temp:
                            cap_aman = cap_temp
                        else:
                            cap_aman = cap_aman

                    if selection < 0:
                        equ_aman = equ_temp + random.randint(20,30)
                        cap_aman = cap_temp + choice(cap_down)
                        if cap_aman < 0.3*cap_temp:
                            cap_aman = cap_temp
                        else:
                            cap_aman = cap_aman

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Aman: I would like to give you a counter-offer. I will give you INR ", cap_aman, " for ", equ_aman," % equity")

                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Aman: Sorry I am out of this")



            col15, col16 = st.columns([3, 3])
            with col15:
                st.write("")
                st.write("")
                st.write("")
                st.image("anupam_asks.jpg")

            with col16:

                if out_anupam == 1:
                    opt.append("Anupam")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_anupam = equ_temp + random.randint(10, 15)
                        cap_anupam = cap_temp - choice(cap_down)
                        if cap_anupam < 0.3 * cap_temp:
                            cap_anupam = cap_temp
                        else:
                            cap_anupam = cap_anupam

                    if selection < 0:
                        equ_anupam = equ_temp + random.randint(20,30)
                        cap_anupam = cap_temp + choice(cap_down)
                        if cap_anupam < 0.3*cap_temp:
                            cap_anupam = cap_temp
                        else:
                            cap_anupam = cap_anupam

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Anupam: I would like to give you a counter-offer. I will give you INR ", cap_anupam, " for ", equ_anupam,
                             " % equity")

                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Anupam: I wish you all the very best but I'm out")


            col17, col18 = st.columns([3, 3])
            with col17:
                st.write("")
                st.write("")
                st.write("")
                st.image("ashneer_asks.jpg")

            with col18:
                if out_ashneer == 1:
                    opt.append("Ashneer")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_ashneer = equ_temp + random.randint(10, 15)
                        cap_ashneer = cap_temp - choice(cap_down)
                        if cap_ashneer < 0.3 * cap_temp:
                            cap_ashneer = cap_temp
                        else:
                            cap_ashneer = cap_ashneer

                    if selection < 0:
                        equ_ashneer = equ_temp + random.randint(20, 30)
                        cap_ashneer = cap_temp + choice(cap_down)
                        if cap_ashneer < 0.3 * cap_temp:
                            cap_ashneer = cap_temp
                        else:
                            cap_ashneer = cap_ashneer

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Ashneer: I would like to give you a counter-offer. I will give you INR ", cap_ashneer, " for ", equ_ashneer,
                             " % equity")

                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Ashneer: Ye sab bakwaas hai, aapne aapki degree waste kar di hai. Doglapan hai sab."
                             " Aap yeh sab band kar do aur naukri dhund lo.")

            col19, col20 = st.columns([3, 3])
            with col19:
                st.write("")
                st.write("")
                st.write("")
                st.image("ghazal_asks.jpg")

            with col20:
                if out_ghazal == 1:
                    opt.append("Ghazal")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_ghazal = equ_temp + random.randint(10, 15)
                        cap_ghazal = cap_temp - choice(cap_down)
                        if cap_ghazal < 0.3 * cap_temp:
                            cap_ghazal = cap_temp
                        else:
                            cap_ghazal = cap_ghazal
                    if selection > 0:
                        equ_ghazal = equ_temp + random.randint(20, 30)
                        cap_ghazal = cap_temp + choice(cap_down)
                        if cap_ghazal < 0.3 * cap_temp:
                            cap_ghazal = cap_temp
                        else:
                            cap_ghazal = cap_ghazal

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Ghazal: I would like to give you a counter-offer. I will give you INR ", cap_ghazal, " for ", equ_ghazal,
                             " % equity")

                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Ghazal: I am very sorry, par mein out hu.")

            col21, col22 = st.columns([3, 3])
            with col21:
                st.write("")
                st.write("")
                st.write("")
                st.image("namita_asks.jpg")

            with col22:
                if out_namita == 1:
                    opt.append("Namita")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_namita = equ_temp + random.randint(10, 15)
                        cap_namita = cap_temp - choice(cap_down)
                        if cap_namita < 0.3 * cap_temp:
                            cap_namita = cap_temp
                        else:
                            cap_namita = cap_namita
                    if selection < 0:
                        equ_namita = equ_temp + random.randint(20, 30)
                        cap_namita = cap_temp + choice(cap_down)
                        if cap_namita < 0.3 * cap_temp:
                            cap_namita = cap_temp
                        else:
                            cap_namita = cap_namita

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Namita: I would like to give you a counter-offer. I will give you INR ", cap_namita, " for ", equ_namita,
                             " % equity")
                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Namita: Ye mere expertise ke bahar hai, so I am out.")




            col23, col24 = st.columns([3, 3])
            with col23:
                st.write("")
                st.write("")
                st.write("")
                st.image("peyush_asks.jpg")

            with col24:
                if out_peyush == 1:
                    opt.append("Peyush")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_peyush = equ_temp + random.randint(10, 20)
                        cap_peyush = cap_temp - choice(cap_down)
                        if cap_peyush < 0.3 * cap:
                            cap_peyush = cap_temp
                        else:
                            cap_peyush = cap_peyush
                    if selection < 0:
                        equ_peyush = equ_temp + random.randint(20, 35)
                        cap_peyush = cap_temp + choice(cap_down)
                        if cap_peyush < 0.3 * cap:
                            cap_peyush = cap_temp
                        else:
                            cap_peyush = cap_peyush

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Peyush: I would like to give you a counter-offer. I will give you INR ", cap_peyush, " for ", equ_peyush,
                             " % equity")
                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Peyush: I like your idea, ismein vision hai, and a great potential "
                             "to bring a change, but I am out of this.")




            col25, col26 = st.columns([3, 3])
            with col25:
                st.write("")
                st.write("")
                st.write("")
                st.image("vineeta asks.jpg")

            with col26:
                if out_vineeta == 1:
                    opt.append("Vineeta")
                    l = [1, -1]
                    choose = [1, 2, 3]
                    cap_down = [100000, 200000, 300000, 400000, 500000, 800000, 1000000, 2000000]
                    selection = choice(l)
                    if selection > 0:
                        equ_vineeta = equ_temp + random.randint(10, 15)
                        cap_vineeta = cap_temp - choice(cap_down)
                        if cap_vineeta < 0.3 * cap_temp:
                            cap_vineeta = cap_temp
                        else:
                            cap_vineeta = cap_vineeta
                    if selection < 0:
                        equ_vineeta = equ_temp + random.randint(20, 30)
                        cap_vineeta = cap_temp + choice(cap_down)
                        if cap_vineeta < 0.3 * cap_temp:
                            cap_vineeta = cap_temp
                        else:
                            cap_vineeta = cap_vineeta

                    st.write("")
                    st.write("")
                    st.write("")
                    st.write(" Vineeta: I would like to give you a counter-offer. I will give you INR ", cap_vineeta, " for ", equ_vineeta,
                             " % equity")
                else:
                    st.write("")
                    st.write("")
                    st.write("")
                    st.write("Vineeta: Mein isse bahar hu, all the very best.")


        #Display option to user to select the best counter-offer
    sub_button_dict = {"No Deal": "submit_button", "Aman": "submit_button1",
                       "Anupam":"submit_button2", "Ashneer": "submit_button3",
                       "Peyush": "submit_button4", "Namita": "submit_button5",
                       "Ghazal": "submit_button6", "Vineeta": "submit_button7"}

    submit_button = None
    submit_button1 = None
    submit_button2 = None
    submit_button3 = None
    submit_button4 = None
    submit_button5 = False
    submit_button6 = False
    submit_button7 = False

    with st.form(key='my_form2'):

        if len(opt) > 1:
            st.write("Woah, your idea is liked by following investor(s). Click on their"
                     " names to finalize the counter-offer made")

        submit_button = st.form_submit_button(label='No deal')
        if out_aman == 1:
            submit_button4 = st.form_submit_button(label='Aman')

        if out_anupam == 1:
            submit_button1 = st.form_submit_button(label='Anupam')

        if out_ashneer == 1:
            submit_button2 = st.form_submit_button(label='Ashneer')

        if out_peyush == 1:
            submit_button3 = st.form_submit_button(label='Peyush')

        if out_namita == 1:
            submit_button5 = st.form_submit_button(label = 'Namita')

        if out_vineeta == 1:
            submit_button6 = st.form_submit_button(label = 'Vineeta')

        if out_ghazal == 1:
            submit_button7 = st.form_submit_button(label = 'Ghazal')


    if submit_button:
        st.subheader("No Deal made. All the best.")

    if submit_button4:
        st.subheader("Congratulations, you have decided to go with Aman's counter-offer")
        st.balloons()

    if submit_button1:
        st.subheader("Congratulations, you have decided to go with Anupam's counter-offer")
        st.balloons()

    if submit_button2:
        st.subheader("Congratulations, you have decided to go with Ashneer's counter-offer")
        st.balloons()

    if submit_button3:
        st.subheader("Congratulations, you have decided to go with Peyush's counter-offer")
        st.balloons()

    if submit_button5:
        st.subheader("Congratulations, you have decided to go with Namita's counter-offer")
        st.balloons()

    if submit_button6:
        st.subheader("Congratulations, you have decided to go with Vineeta's counter-offer")
        st.balloons()

    if submit_button7:
        st.subheader("Congratulations, you have decided to go with Ghazal's counter-offer")
        st.balloons()












    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.write("")
    st.subheader("Thanks for Playing")
    st.write("How did you fare? Kitni investment mili? If you like this simulator, "
             "please [subscribe](https://www.youtube.com/c/IndiainPixels) to our channel, India in Pixels on YouTube. " 
             "You can also follow us on Instagram [Sarthak](https://www.instagram.com/ns_sarthakh/), [Dev](https://www.instagram.com/dev_patel_511/)"
             " and [Gauri](https://www.instagram.com/_gauripandey_/).")
