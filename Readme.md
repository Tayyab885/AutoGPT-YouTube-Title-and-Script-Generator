# AutoGPT YouTube Title and Script Generator

This is a simple app built on Python that generates YouTube video titles and scripts using the OpenAI's GPT language model. The app is designed to help YouTubers quickly come up with ideas for their videos, and generate corresponding scripts based on those titles.

## Dependencies
This app uses the following Python libraries:
- `os`
- `streamlit`
- `langchain` 

## How to Use

1. Clone this repository to your local machine
2. Install the required dependencies
3. Create an OpenAI API key and store it in a file called `apikey.py`
4. Run `app.py`
5. Enter a prompt for the video title and click on the 'Generate' button
6. The app will generate a title and a script based on your prompt

## Explanation of Code

The code uses the `langchain` library to interact with the GPT model. The user enters a prompt for the video title, which is used to generate a title template. This template is then used to generate a video title using the GPT model.

Once the video title has been generated, it is used as a prompt for the script template. The script template also takes a Wikipedia research input to help generate the script content.

Finally, the generated title and script are displayed on the Streamlit app. The app also includes an option to view the title history, script history, and Wikipedia research history.
