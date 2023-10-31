import re
import openai
import PyPDF2


# Read PDF
def get_pdf_paragraphs(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        text = ''
        for page in range(reader.numPages):
            text += reader.getPage(page).extractText()
        paragraphs = re.split('\n\n', text)
    return paragraphs

# Get question from paragraph using OpenAI API
def get_question_from_paragraph(paragraph):
    openai.api_key = "your_openai_api_key"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"What is the question being answered by this paragraph:\n{paragraph}\n",
        max_tokens=50,
        n=1,
        stop=None,
        temperature=0.8,
    )
    question = response.choices[0].text.strip()
    return question

# Main function
def main():
    pdf_file_path = "your_pdf_file_path.pdf"
    paragraphs = get_pdf_paragraphs(pdf_file_path)
    for paragraph in paragraphs:
        question = get_question_from_paragraph(paragraph)
        print(f"Paragraph: {paragraph}\nQuestion: {question}\n")

if __name__ == "__main__":
    main()
