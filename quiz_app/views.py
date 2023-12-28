# quiz_app/views.py
from django.shortcuts import render, redirect
from .models import Question
from .forms import QuizForm
from django.contrib import messages

def quiz(request, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            user_answer = form.cleaned_data['user_answer']
            correct = (user_answer.lower() == question.correct_answer.lower())
            print(correct)
            if not correct:
                # If the user answers incorrectly, redirect to the same question
                messages.add_message(request, messages.ERROR, f"Sorry, the correct answer was {question.correct_answer}. \n{question.additional_info}")
                next_question_id = Question.objects.order_by('?')[0].id
                return redirect('quiz', question_id=next_question_id)
            # Implement logic for correct answer, e.g., move to the next question
            print(Question.objects.order_by('?')[0].id)
            messages.add_message(request, messages.SUCCESS, f"Correct!")
            next_question_id = Question.objects.order_by('?')[0].id
            return redirect('quiz', question_id=next_question_id)
    else:
        form = QuizForm()

    return render(request, 'quiz_app/question.html', {'question': question, 'form': form})
