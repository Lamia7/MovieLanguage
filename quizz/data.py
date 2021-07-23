from django.db.utils import IntegrityError

from quizz.models import Language, Movie, Question, Answer


class DataManager:
    """Manages data (save)
    """

    def save_movie(self, movie):
        try:
            movie.save()
        except IntegrityError:
            movie = Movie.objects.get(title=movie)
        return movie

    def save_language(self, language):
        try:
            language.save()
        except IntegrityError:
            language = Language.objects.get(name=language)
        return language

    def save_question(self, question, quizz):
        try:
            question = Question.objects.create(
                question_content=question,
                quizz=quizz
            )
        except IntegrityError:
            question = Question.objects.get(question_content=question)
        print(f"TYPE QUESTIONS: {type(question)} - QUESTION {question}, {type(question)}")
        print(f"QUESTION ID: {question.id}")
        return question

    # def save_answers(self, question_item, question_obj):
    def save_answers(self, answer_text, question_obj, is_solution):

        # solution = question_item['solution']
        # # pr chq dict réponse dans la liste de réponses
        # for answer in question_item['answers']:
        #     # pr chq clé de chq dict de réponse
        #     for key in answer.keys():
        #         #print(f"ANSWERS {answer[key]}")
        #         # si la clé dans le dict de réponse et = à solution
        #         if key == solution:
        #             is_solution = True
        #             #print(f"c'est la bonne réponse: {key}")
        #         else:
        #             is_solution = False
        # enregistrer réponse------------------------------------------------
        try:
            answer_obj = Answer.objects.create(
                answer_content=answer_text,
                is_correct=is_solution,
                question=question_obj
            )
        except IntegrityError:
            answer_obj = Answer.objects.get(answer_content=answer_text)
            # print(f"ANSWER_OBJ: {answer_obj} - ASNWER: {answer}")
        return answer_obj
    # continue


"""        solution = question_item['solution']
        for answer in question_item['answers']:
            if answer = solution
        print(f"TYPE ANSWERS: {type(answers)} - ANSWERS {answers}")
        print(f"--------------------")"""
