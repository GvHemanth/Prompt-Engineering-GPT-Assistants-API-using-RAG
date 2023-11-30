
                        #### Problem Statement - 2 ( Few Shot Learning ) ####


# Importing OpenAI module
from openai import OpenAI

# Replace 'API_KEY' with your actual OpenAI API key
api_key = 'API_KEY'

# Initialize the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Defining the context containing information 
Context = 'Context 1 author: Trinita Roy Context 1 text: BERT is an encoder transformer model which is trained on two tasks - masked LM and next sentence prediction. Context 2 author: Asheesh Kumar Context 2 text: GPT is a decoder model that works best on sequence generation tasks. Context 3 author: Siddhant Jain Context 3 text: LSTMs have been very popular for sequence-to-sequence tasks but have limitations in processing long texts.'

# Using the OpenAI Chat Completions API to generate an answer with citations
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Answer only to the question in a concise form using information provided only from the provided context. For each detail used from a context, cite it only in the format of (Author_last_name, et al.). Structure the answer appropriately, while strictly adhering to the format of citing the relevant authors for each detail."},
        {"role": "user", "content": 'Question: What is the difference between LSTM and BERT models?'},
        {"role": "user", "content": Context},
        {"role": "user", "content": 'Follow the Below Example output format for the Sample Question: what is the difference between GPT and BERT?'},
        {"role": "user", "content": 'Sample Answer: While GPT is a decoder model (Kumar et al.), BERT is an encoder transformer model (Roy et al.). Based on their training tasks, GPT is more suitable for sequence generation (Roy et al). BERT is more suited for next-sentence prediction (Kumar et al.).'}
    ]
)

# Extracting the assistant's reply from the API response
answer = response.choices[0].message.content

# Printing the generated answer with citations
print(answer)