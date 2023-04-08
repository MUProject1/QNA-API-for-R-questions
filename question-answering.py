import os, sys
from dotenv import load_dotenv
from azure.core.credentials import AzureKeyCredential
from azure.ai.textanalytics import TextAnalyticsClient
from azure.ai.language.questionanswering import QuestionAnsweringClient

load_dotenv()
endpoint = os.environ.get('AA_QA_ENDPOINT')
credential = AzureKeyCredential(os.environ.get('AA_QA_KEY'))
knowledge_base_project = os.environ.get('AA_QA_KB')
deployment = "test"

def main():
    question = input("Question: ")
    if len(question.strip()) == 0:
        sys.exit('Please enter a question.')
    ld_client = TextAnalyticsClient(endpoint, credential)
    if ld_client.detect_language(documents = [question])[0].primary_language.name != 'English':
        print('Sorry, I can only speak English.')
    else:
        qa_client = QuestionAnsweringClient(endpoint, credential)
        with qa_client:
            response = qa_client.get_answers(
                question = question,
                confidence_threshold = 0.5,
                top = 3,
                project_name = knowledge_base_project,
                deployment_name = deployment
            )

        if response.answers[0].qna_id == -1:
            print('No answers found.')
        else:
            for i, answer in enumerate(response.answers, start=1):
                if 'chitchat' in answer.source:
                    print(answer.answer)
                    break
                else:
                    print(f'{i}: {answer.questions[0]}')
                    print(f'   Confidence score: {answer.confidence}')
                    print(f'   URL: https://stackoverflow.com/q/{answer.answer}\n')


if __name__ == '__main__':
    main()
