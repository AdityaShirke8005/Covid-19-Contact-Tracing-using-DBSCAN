import streamlit as st
import pandas as pd
from sklearn.cluster import DBSCAN
from PIL import Image


# Load the data
df = pd.read_json("data.json")

# Function to get infected names
def get_infected_names(input_name):
    epsilon = 0.0018288  # a radial distance of 6 feet in kilometers
    model = DBSCAN(eps=epsilon, min_samples=2, metric='haversine').fit(df[['latitude', 'longitude']])
    df['cluster'] = model.labels_.tolist()

    input_name_clusters = []
    for i in range(len(df)):
        if df['id'][i] == input_name:
            if df['cluster'][i] in input_name_clusters:
                pass
            else:
                input_name_clusters.append(df['cluster'][i])

    infected_names = []
    for cluster in input_name_clusters:
        if cluster != -1:
            ids_in_cluster = df.loc[df['cluster'] == cluster, 'id']
            for i in range(len(ids_in_cluster)):
                member_id = ids_in_cluster.iloc[i]
                if (member_id not in infected_names) and (member_id != input_name):
                    infected_names.append(member_id)
                else:
                    pass
    return infected_names

# Streamlit app with styling
def main():
    st.title("Contact Tracing App")
    img = Image.open('img.png')
    st.image(img,width=650)
    st.markdown(
        """
        <style>
        .title {
            font-size: 36px;
            text-align: center;
            margin-bottom: 30px;
        }
        .btn {
            display: flex;
            justify-content: center;
        }
        .result {
            margin-top: 20px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown("<h3 style='text-align: center;'>Enter your name to check for potential exposure:</h3>", unsafe_allow_html=True)

    input_name = st.text_input("Name")

    if st.button("Check", key="check-btn"):
        if input_name:
            if input_name in df['id'].unique():
                infected_people = get_infected_names(input_name)
                if infected_people:
                    st.markdown(
                        "<h3 style='text-align: center; color: red;'>Potential exposure detected!</h3>",
                        unsafe_allow_html=True
                    )
                    st.markdown(
                        "<p style='text-align: center;'>You may have been in contact with the following infected people:</p>",
                        unsafe_allow_html=True
                    )
                    for person in infected_people:
                        st.write(f"- {person}")
                else:
                    st.markdown(
                        "<h3 style='text-align: center; color: green;'>No potential exposure detected. Stay safe!</h3>",
                        unsafe_allow_html=True
                    )
            else:
                st.markdown(
                    "<h3 style='text-align: center; color: orange;'>Name not found in the dataset.</h3>",
                    unsafe_allow_html=True
                )
                st.markdown(
                    "<p style='text-align: center;'>Please enter a valid name.</p>",
                    unsafe_allow_html=True
                )
        else:
            st.markdown("<p style='text-align: center;'>Please enter your name.</p>", unsafe_allow_html=True)
    
st.markdown(
            "<p class='footer'>Created with ❤️ by Aditya Shirke</p>",
            unsafe_allow_html=True
        )


               
if __name__ == "__main__":
    main()
