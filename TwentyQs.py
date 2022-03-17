# File: TwentyQs.py - Timothy Wang

print('Welcome to Twenty Questions')
print("Think of something and I'll try to guess it asking at most 20 questions.")

questions = {1: 'Is it bigger than a bread box? ',
             2: 'Is it an elephant? ', 3: 'Is it a mouse? '}  # initializes dictionary that maps numbers to questions for use in binary tree
decisionTree = dict()   # initializes dictionary that acts as adjacency lists
decisionTree[1] = [2, 3]
decisionTree[2] = ['win', 0]
decisionTree[3] = ['win', 0]

while True:  # loop to keep the game running while the user hasn't quit
    two_prev = None  # keeps count of current win state,  previous question, and where the new question should be added if computer is wrong
    prev = None
    cur = 1
    iterations = 0
    while cur != 'win' and cur != 0:    # main game; traverses down the tree while there are still more branches to go
        question = input(questions[cur])
        if question == 'y':
            two_prev = prev
            prev = cur
            cur = decisionTree[cur][0]
        else:
            two_prev = prev
            prev = cur
            cur = decisionTree[cur][1]
        iterations += 1

    if cur == 'win':    # endgame condition in which the cpu guesses the thing correctly
        print('Yay! I guessed it')
    else:   # otherwise learn from user
        correct_thing = input('What were you thinking? ')
        new_question = input(
            'What is a yes/no question that distinguishes it from {} '.format(questions[prev].split()[-1]))
        new_question_answer = input(
            'Is yes or no the correct answer to get to {} '.format(correct_thing))

        # succeeding number is added to questions map
        questions[len(questions.keys()) + 1] = new_question

        # inserts the new question where the path branches off
        if prev == decisionTree[two_prev][0]:
            decisionTree[two_prev][0] = len(questions.keys())
        else:
            decisionTree[two_prev][1] = len(questions.keys())

        # sets the new question's anwer path to yes or no
        if new_question_answer == 'y':
            decisionTree[len(questions.keys())] = [
                len(questions.keys()) + 1, prev]
        else:
            decisionTree[len(questions.keys())] = [
                prev, len(questions.keys()) + 1]

        # includes proceeding question into decisionTree
        questions[len(questions.keys()) + 1] = 'Is it a(n) {}'.format(
            correct_thing)
        decisionTree[len(questions.keys())] = ['win', 0]

    restart_condition = input('\nPlay again? ')
    if restart_condition == 'n' or iterations == 20:
        if iterations == 20:    # break condition if more than 20 layers are traversed
            print("I couldn't get it in 20 questions!")
        break
