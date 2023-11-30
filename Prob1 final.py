                            #### Problem Statement - 1 ####
            # Step 1: Creating an Assistant

#import required libraries
from openai import OpenAI
import json
import time

api_key = 'ENTER API-KEY'             # OpenAi API Key
client = OpenAI(api_key=api_key)                                            # Initialise OpenAI

            # Step 2: Uploading a research paper to Assistant
file_path = r"C:\Users\heman\Downloads\sample research.pdf"                 # Path to the file
file = client.files.create(file=open(file_path, "rb"), purpose='assistants')# Uploading file to Assistants

# Creating an assistant
assistant = client.beta.assistants.create(
    instructions="You are an assistant that reads research papers and gives abstract as per user defined length.",
    name='Research Assistant',                                              # Naming the Assistant
    model="gpt-3.5-turbo-1106",                                             
    tools=[{"type": "retrieval"}],                                          # We use gpt-3.5-turbo-1106 as it supports Retrieval type
    file_ids=[file.id]
)

# We Define a function to wait for the run to complete
def wait_for_run_completion(thread_id, run_id):
    run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id).status   # Checks the status of run (In_progress / Completed / failed)
    while run_status != "completed":                                                            # Breaks the loop only if status changes to completed
        time.sleep(1)
        run_status = client.beta.threads.runs.retrieve(thread_id=thread_id, run_id=run_id).status

            #Step 3: Asking the assistant to get the abstract
thread = client.beta.threads.create(messages=[{"role": "user", "content": "Get the abstract of the research paper, and store the word count of the abstract provided by you and do not print anything about word count"}])  # Creating a thread with the message
run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)            # Creating a run for the thread
wait_for_run_completion(thread.id, run.id)                                  # Call run completion function to check run.status

            # Step 4: Printing the assistant's response
messages = client.beta.threads.messages.list(thread_id=thread.id)           # Retrieves the list of messages 
print(messages.data[0].content[-1].text.value + '\n')                       # Prints the latest message i.e of assistant

            # Step 5: Asking the assistant to change the tone and length of the abstract as per user input
thread_message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",                                                            # Creates a new user message taking the input of required tone & length 
    content=f"Now Change the length of abstract to {input('Choose Length(one/two/three: )')} times the number of sentences of original abstract length by adding more insights from the paper and also change the tone of the abstract to {input('Choose Tone (Aggressive/Creative/Academic): ')}."
)      

thread_message = client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",                                                            # Creates a new user message taking the input of required tone & length 
    content="The output should not be a text paragraph. It needs to be a list of sentences in JSON format that should be easily processed by using code: json.loads(gpt_output)  ",
)        


run = client.beta.threads.runs.create(thread_id=thread.id, assistant_id=assistant.id)           # Creating a new run and waiting for the run to complete.
wait_for_run_completion(thread.id, run.id)

# Get the final output
messages = client.beta.threads.messages.list(thread_id=thread.id)           # Retrieving the list of messages
final_output = messages.data[0].content[-1].text.value

print(final_output)                                                          # Print final output
