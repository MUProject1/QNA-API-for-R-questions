from azure.core.credentials import AzureKeyCredential
from azure.ai.language.questionanswering import QuestionAnsweringClient
from dotenv import load_dotenv
import os
import pandas as pd

load_dotenv()
table = {}

def main1(userAskedQuestion):
    client = QuestionAnsweringClient(os.getenv("endpoint_1"), AzureKeyCredential(os.getenv("credential_1")))
    with client:
        question=userAskedQuestion
        output = client.get_answers(
            question = question,
            project_name="qna3",
            deployment_name="test"
        )
    table[output.answers[0].confidence] = output.answers[0].answer

    client = QuestionAnsweringClient(os.getenv("endpoint_2"), AzureKeyCredential(os.getenv("credential_2")))
    with client:
        question=userAskedQuestion
        output = client.get_answers(
            question = question,
            project_name="newQnaProject",
            deployment_name="test"
        )
    table[output.answers[0].confidence] = output.answers[0].answer

    client = QuestionAnsweringClient(os.getenv("endpoint_3"), AzureKeyCredential(os.getenv("credential_3")))
    with client:
        question=userAskedQuestion
        output = client.get_answers(
            question = question,
            project_name="qnaProject",
            deployment_name="test"
        )
    table[output.answers[0].confidence] = output.answers[0].answer
    sorted_dictionary = dict(sorted(table.items(), key=lambda x:x[0], reverse=True))
        
    for i in sorted_dictionary.items():
        print(f"Confidence Score: {round(i[0],4)}, AnswerID : {i[1]}")

if __name__ == '__main__':
    userAskedQuestion = "define quantile"
    print(f"Qusetion asked : {userAskedQuestion}")
    main1(userAskedQuestion)






############### APPROACH ONE - TO GET ANSWERS USING THE ANSWER ID ###############

# rAnswers = pd.read_csv("data\Ranswers.csv",encoding = "ISO-8859-1")
# # Assume `answers` is your pandas dataframe

# parent_id = 39921971  # Replace with the actual value for ParentId

# # Filter the rows by ParentId and sort by Score in descending order
# best_answers = answers[answers['ParentId'] == parent_id].sort_values('Score', ascending=False)

# if best_answers.empty:
#     print("No results found for ParentId = ", parent_id)
# else:
#     # If there are fewer than 3 rows, take all of them
#     if len(best_answers) < 3:
#         best_answers = best_answers[:]
    
#     # Print the Body column of the top 3 rows if there are at least 3 rows in the subset
#     if len(best_answers) >= 3:
#         i = 1
#         for index, row in best_answers.head(3).iterrows():
#             print(f"Answer {i}: {row['Body']}\n")
#             i += 1
#     else:
#         i = 1
#         for index, row in best_answers.iterrows():
#             print(f"Answer {i}: {row['Body']}\n")
#             i += 1


#########################################################################################################


############### APPROACH TWO - TO GET ANSWERS AND ANSWERS LINK USING THE ANSWER ID ###############

# answers = pd.read_csv("data\Ranswers.csv",encoding = "ISO-8859-1")
# answers['answerLink'] = answers['ParentId'].apply(lambda x: f"https://stackoverflow.com/q/{x}")
# # Assume `answers` is your pandas dataframe

# parent_id = 79709  # Replace with the actual value for ParentId

# # Filter the rows by ParentId and sort by Score in descending order
# best_answers = answers[answers['ParentId'] == parent_id].sort_values('Score', ascending=False)

# if best_answers.empty:
#     print("No results found for ParentId = ", parent_id)
# else:
#     # If there are fewer than 3 rows, take all of them
#     if len(best_answers) < 3:
#         best_answers = best_answers[:]

#     # Print the Body and answerLink columns of the top 3 rows if there are at least 3 rows in the subset
#     if len(best_answers) >= 3:
#         for i, (index, row) in enumerate(best_answers.head(3).iterrows()):
#             print(f"Answer {i+1}: {row['Body']}\nAnswer {i+1} link: {row['answerLink']}\n")
#     else:
#         for i, (index, row) in enumerate(best_answers.iterrows()):
#             print(f"Answer {i+1}: {row['Body']}\nAnswer {i+1} link: {row['answerLink']}\n")
#########################################################################################################