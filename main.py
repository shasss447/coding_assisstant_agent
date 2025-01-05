import autogen
from autogen import ConversableAgent
from helper import MarkdownCodeExtractor


def main(): # main function to initiate agents and chat between them
    
    # creating configuration for using llm for writing code
    config_list = autogen.config_list_from_json(env_or_file="config.json")

    # prompt for the code writer agent
    code_writer_system_message = """You are a helpful AI assistant.Solve tasks using your coding and language skills.
    In the following cases, suggest python code (in a python coding block) or shell script (in a sh coding block) for the user to execute.
    1. When you need to collect info, use the code to output the info you need, for example, browse or search the web, download/read a file, print the content of a webpage or a file, get the current date/time, check the operating system. After sufficient info is printed and the task is ready to be solved based on your language skill, you can solve the task by yourself.
    2. When you need to perform some task with code, use the code to perform the task and output the result. Finish the task smartly.
    Solve the task step by step if you need to. If a plan is not provided, explain your plan first. Be clear which step uses code, and which step uses your language skill.
    When using code, you must indicate the script type in the code block. The user cannot provide any other feedback or perform any other action beyond executing the code you suggest. The user can't modify your code. So do not suggest incomplete code which requires users to modify. Don't use a code block if it's not intended to be executed by the user.
    If you want the user to save the code in a file before executing it, put # filename: <filename> inside the code block as the first line. Don't include multiple code blocks in one response. Do not ask users to copy and paste the result. Instead, use 'print' function for the output when relevant. Check the execution result returned by the user.
    When user sends this "exitcode: 0 (execution succeeded)", reply only with "TERMINATE".
    If the result indicates there is an error, fix the error and output the code again. Suggest the full code instead of partial code or code changes. If the error can't be fixed or if the task is not solved even after the code is executed successfully, analyze the problem, revisit your assumption, collect additional info you need, and think of a different approach to try.
    When you find an answer, verify the answer carefully. Include verifiable evidence in your response if possible.
    """

    # Create an agent with LLM configuration for writing code
    code_writer_agent = ConversableAgent(
     "code_writer_agent",
     system_message=code_writer_system_message, # prompt for the code writer agent
     llm_config={"config_list":config_list},
     code_execution_config=False,  # Turn off code execution for this agent.
     )

    # Create an agent with code executor configuration
    code_executor_agent = ConversableAgent(
    "code_executor_agent",
    llm_config=False,  # Turn off LLM for this agent.
    code_execution_config={"use_docker":False},
    human_input_mode="ALWAYS",  # Always take human input for this agent for safety
    )

    message= input("Hello! How can I assist you with your code today?") # input from user

    # Initiate chat between the two agents.
    chat_result = code_executor_agent.initiate_chat(
    code_writer_agent,
    message=message,
    )

    # Extract code blocks from the chat history
    code_extracter=MarkdownCodeExtractor()
    code=code_extracter.extract_code_blocks(chat_result.chat_history)

    # Write the code to a file.
    file = open(f"{message}.txt", "w")
    file.write(message+"\n")
    for i in code:
     file.write(i.code+"\n")   
    file.close() 
    
# Run the main function
if __name__=="__main__":
    main()