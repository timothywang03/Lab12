# File: TwentyQs.py - Timothy Wang

print('Welcome to Twenty Questions')
print("Think of something and I'll try to guess it asking at most 20 questions.")

questions = {1: 'Is it bigger than a bread box? ',
             2: 'Is it an elephant? ', 3: 'Is it a mouse? '}
decisionTree = dict()
decisionTree[1] = [2, 3]
decisionTree[2] = ['win', 0]
decisionTree[3] = ['win', 0]

while True:
    two_prev = None
    prev = None
    cur = 1
    while cur != 'win' and cur != 0:
        question = input(questions[cur])
        if question == 'y':
            two_prev = prev
            prev = cur
            cur = decisionTree[cur][0]
        else:
            two_prev = prev
            prev = cur
            cur = decisionTree[cur][1]

    if cur == 'win':
        print('Yay! I guessed it')
    else:
        correct_thing = input('What were you thinking? ')
        new_question = input(
            'What is a yes/no question that distinguishes it from {} '.format(questions[prev].split()[-1]))
        new_question_answer = input(
            'Is yes or no the correct answer to get to {} '.format(correct_thing))

        questions[len(questions.keys()) + 1] = new_question
        if prev == decisionTree[two_prev][0]:
            decisionTree[two_prev][0] = len(questions.keys())
        else:
            decisionTree[two_prev][1] = len(questions.keys())

        if new_question_answer == 'y':
            decisionTree[len(questions.keys())] = [
                len(questions.keys()) + 1, prev]
        else:
            decisionTree[len(questions.keys())] = [
                prev, len(questions.keys()) + 1]

        questions[len(questions.keys()) + 1] = 'Is it a(n) {}'.format(
            correct_thing)
        decisionTree[len(questions.keys())] = ['win', 0]

    restart_condition = input('Play again? ')
    if restart_condition == 'n':
        break
