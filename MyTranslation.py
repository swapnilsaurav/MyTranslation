# Importing required packages
import streamlit as st
import openai
import prog1

# Set the model engine and your OpenAI API key
model_engine = "gpt-3.5-turbo-instruct"
#openai.api_key = "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"
openai.api_key = "MY_API_KEY"

#define a function to handle the translation process
def translation_process(content,target_lang):
    prompt=f"Translate '{content}' into {target_lang}"
    response = openai.completions.create(
        model=model_engine,
        prompt=prompt,
        temperature=0.7,
        max_tokens=1024,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )
    #extract the translated text from the response
    translated = response.choices[0].text.strip()
    return translated

def main():
    st.sidebar.header("Language Translation Service by Swapnil Saurav")
    st.sidebar.write("This is a language translation service. Enter the text to translate and the target language.")

    # setting up the input values
    inp_content = st.text_input("Enter the text for the translation")
    #selection box to get the language
    target_languages=['Arabic','English','Hindi','German','Spanish','French','Japanese']
    target_lang = st.selectbox("Select language",target_languages)
    #add button to start the translation services
    trans_button = st.button("Translate")
    #add placeholder for the output text
    output_text = st.empty()

    #hit the button
    if trans_button:
        output_text.text("Translating ...")
        output_text.text(translation_process(inp_content,target_lang))

#driving code
if __name__ == "__main__":
    main()
