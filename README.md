# Plant-Diseases-Classification 

## Streamlit App with Pyngrok

This is a Streamlit App with Pyngrok, which allows users to upload a crop leaf and have AI predict whether it's infected with a plant disease.

The App allows users to choose one of two CNN models 
- Self-Created CNN Model
- MobileNetV2 - Pretrained Model

The code can be found within crops_detection_using_cnn.ipynb file

Notice: The App is written with Google Colab; therefore, no packages are installed locally

## Installation 

1. Create your own [Ngrok Authtoken](https://dashboard.ngrok.com/get-started/setup)
2. Open streamlit_app.ipynb with google colabs
3. From the secrets tab, set pyngrok_auth_token with your created Ngrok Authtoken
4. From streamlit_app.ipynb "Runtime" menu --> Run all
