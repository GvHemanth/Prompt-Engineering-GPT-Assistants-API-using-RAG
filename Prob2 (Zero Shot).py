                        #### Problem Statement - 2 (Zero Shot Prompt)####

# Importing the OpenAI module
from openai import OpenAI

# Replace 'API_KEY' with actual OpenAI API key
api_key = 'API_KEY'

# Initializing the OpenAI client with the API key
client = OpenAI(api_key=api_key)

# Defining the user prompt with the question and provided contexts
prompt = f"Question: what is the difference between GPT and BERT?\n\nContext 1 author: Trinita Roy\nContext 1 text: BERT is an encoder transformer model which is trained on two tasks - masked LM and next sentence prediction.\n\nContext 2 author: Asheesh Kumar\nContext 2 text: GPT is a decoder model that works best on sequence generation tasks.\n\nContext 3 author: Siddhant Jain\nContext 3 text: LSTMs have been very popular for sequence-to-sequence tasks but have limitations in processing long texts.\n\nAnswer:"

# Using the OpenAI Chat Completions API to generate an answer with citations
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Answer only to the question in a concise form using information only from the provided contexts. For each detail used from a context strictly cite it only in the format of (Author_last_name, et al.). Structure the answer appropriately, while strictly adhering to the format of citing the relevant authors for each detail."},
        {"role": "user", "content": prompt}
    ]
)

# Extracting the assistant's reply from the API response
answer = response.choices[0].message.content

# Printing the generated answer with citations
print(answer)