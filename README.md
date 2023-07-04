# COVID-19 Contact Tracing App

A Contact Tracing App implemented in Python using Streamlit to help track potential exposure to COVID-19. The app takes user input and checks for potential contacts with infected individuals based on location data.

![App Demo](Contact_tracing.gif)

## Features

- User-friendly interface for entering the name and checking for potential exposure.
- Utilizes DBSCAN clustering algorithm to identify potential contacts.
- Displays a list of infected people if potential exposure is detected.
- Provides appropriate messages based on the outcome of the check.

## Technologies Used

- Python
- Streamlit
- Pandas
- scikit-learn

## How to Use

1. Clone the repository:

   ```shell
   git clone https://github.com/AdityaShirke8005/Covid-19-Contact-Tracing-using-DBSCAN

2. Install the required dependencies:

   ```shell
   pip install -r requirements.txt

3. Prepare the contact tracing data:

   ```shell
   Create a JSON file named contacttracing_data.json with the required data structure.
   Make sure to include columns for id, latitude, and longitude.

4. Run the app:

   ```shell
   streamlit run app.py
   
6. Enter your name in the app to check for potential exposure.

## Future Scope

- **Real-time Data Integration**: Enhance the app by integrating with real-time data sources, such as public health databases or APIs, to provide up-to-date information on infected individuals and potential exposure.
- **User Authentication**: Implement user authentication functionality to ensure privacy and data security, allowing users to securely access their own exposure history and receive personalized recommendations.
- **Geolocation Tracking**: Integrate with mobile device geolocation services to track user movement and provide more accurate exposure alerts based on proximity to infected individuals.
- **Visualization and Analytics**: Develop visualizations and analytics features to display trends, hotspots, and patterns of potential exposure, empowering users and public health authorities with actionable insights.
- **Automated Contact Tracing**: Implement automated contact tracing using Bluetooth Low Energy (BLE) or other proximity-based technologies, enabling more precise identification of potential contacts and reducing reliance on self-reporting.
- **Notifications and Alerts**: Implement push notifications and alerts to notify users about potential exposure, provide guidance on necessary precautions, and facilitate communication with public health authorities.
- **Multi-language Support**: Add support for multiple languages to make the app accessible to a wider user base, considering the diversity of languages spoken in different regions.
- **Machine Learning Enhancements**: Explore the use of advanced machine learning techniques, such as anomaly detection or predictive modeling, to improve the accuracy and effectiveness of contact tracing and exposure predictions.

These are just a few potential areas of improvement and expansion for the COVID-19 Contact Tracing App. Feel free to explore and implement additional features based on user feedback and evolving requirements.


## Demo

Here's a GIF demonstrating the working of the Contact Tracing App:

![App Demo](Contact_tracing.gif)

## Contributors

- Aditya Shirke - [GitHub](https://github.com/AdityaShirke8005) - [LinkedIn](https://www.linkedin.com/in/aditya-shirke-031695269/)


