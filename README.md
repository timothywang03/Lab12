Lab 12: Binary Search Trees and Heaps
Due: Thursday, March 17, 2022, before class (2 Python modules and 1 Google doc)

Instructions:
You will be submitting two Python modules for this lab. Please name them as specified in the exercise description.
This lab also includes several written responses.  Please write them in a Google doc called Lab12Responses(yourname) and label all responses with the corresponding problem number.
All files for this lab should be in a folder called Lab12.

Exercises:
(7 pts) The game Twenty Questions is a two-player guessing game where one player thinks of something and the other player tries to figure out what it is by asking at most 20 yes/no questions.

Can this game be implemented using a binary search tree? If so, explain what the nodes represent, the relationship between a parent node and its children, and how it satisfies the binary search tree property. If not, explain why not and propose modifications to binary search trees to make it work.

In a module called TwentyQs.py implement a program that “learns” how to play Twenty Questions by starting every game with the question “Is it bigger than a bread box?” with initial guesses “mouse” and “elephant.” If the computer cannot guess the user’s word, then it should add the word to its “memory” by asking the user to supply a question that would lead to their word. The program should continue to play until the user wishes to quit. An example run is linked here.

(5 pts) Remember that all of the nice runtime analyses for binary search trees rely on the fact that the tree is balanced, but that cannot be guaranteed for a generic binary search tree. However, there are several schemes for maintaining a balanced tree so you’ll be exploring one here.

An AVL tree is a binary search tree that is height-balanced: for each node x, the heights of the left and right subtrees of x differ by at most 1 (the height of a subtree is the maximum distance from the root to any leaf). To implement an AVL tree, we need to consider how new nodes are inserted into the tree to maintain the height-balanced property.

To insert into an AVL tree, we first place a node into the appropriate place in binary search tree order. Afterward, the tree might no longer be height-balanced. Specifically, the heights of the left and right children of a node might differ by 2. Describe a procedure called balance(x) that takes a subtree rooted at x whose left and right children have heights that differ by at most 2, and uses rotations to alter the subtree rooted at x to be height-balanced.

Using your balance(x) procedure, describe how to add a new node z to an AVL tree while maintaining the properties of an AVL tree.

Recall that the point of maintaining a balanced tree is to guarantee that methods like inserting a new node run in O(lg n) time. Explain how the procedure you described in part (b) takes O(lg n) time and performs O(1) rotations.

(3 pts) Prove the correctness of HEAPSORT (as shown in CLRS on page 160) using the loop invariant:
At the start of each iteration of the for loop of lines 2–5, the subarray A = [1.. i] is a max-heap containing the i smallest elements of A = [1..n], and the subarray
A = [i+1..n] contains the n - i largest elements of A = [1..n] in sorted order.

(5 pts) We’ve now seen several algorithms that take advantage of a min-priority queue so now it’s time to implement one! In a module called MinPriorityQueue.py, write a MinPriorityQueue class that uses a min-heap to implement a min-priority queue with the following API:

size(): returns the number of elements in the min-priority queue

getMin(): returns the minimum value without removing it from the heap

extractMin(): removes the minimum value from the min-priority queue AND returns it. (Note: you may find it useful to also include a private helper method similar to MAX-HEAPIFY.)

insert(x): adds the value x to the min-priority queue while maintaining the min-heap property. (Note: you may find it useful to also include a private helper method similar to HEAP-INCREASE-KEY)

(5 pts) Min-priority queues have many useful applications as we’ve already seen. The following is another example. Suppose you have N values that you read in one at a time, and you want to maintain a collection of the k largest values you’ve seen so far, where k is much smaller than N. It would be inefficient to repeatedly sort the array of values every time you receive a new one just to pick out the top k, so you need to find another strategy.

Describe a better way to accomplish this task using a min-priority queue. Specifically, address the counterintuitive notion of using a min-priority queue when you’re trying to maintain a collection of maximum values. What is the runtime of your algorithm in big-O notation? Don’t forget to justify it!

In your MinPriorityQueue module, implement the solution you described in part (a) and test it. (My guess is that it would be best to create a class to aid in your implementation but this is not required.) Please leave your test function in your module for me to see.

Describe an application where the program you wrote in part (b) would be useful. Please be clear about how each piece of your application fits into the problem statement (e.g. what do the N values represent, what does k represent, why would you want to find the largest values, etc.).
(OPTIONAL but useful) A useful transformation that can be applied to binary search trees is a subtree rotation. As the name suggests, this rotates the position of two nodes in a binary search tree while maintaining the binary search tree property. Both a left- and right-rotation are illustrated below.



Explain how these rotations maintain the binary search tree property. It is enough for you to thoroughly justify this for one direction, then briefly describe the difference in your analysis for the opposite direction.

Add the following methods to your Tree class from Exercise #1:
leftRotate(x): rotates the nodes of the subtree rooted at x to look like the image on the left
rightRotate(y): rotates the nodes of the subtree rooted at y to look like the image on the right
subtreeHeight(x): returns the height of the subtree rooted at node x. (The height of a subtree is the maximum distance from the Tree root to any leaf of that subtree. Calling subtreeHeight(root) would return the height of the entire tree.)

Use your methods from part (b) to determine how a rotation changes the heights of subtrees 𝛼, 𝛽, and 𝛾. In your Google doc, record the observations of your experiment(s) and summarize the results. Please also include a commentary about whether your findings make sense and why.



A reminder of the expectations for all lab submissions:
You have the freedom to be as creative as you’d like with your implementation -- within the bounds of this class -- as long as your code adheres to the given API.  This means you must use all identifiers precisely as given (the ones in bold), but you can create others to help your program.  Remember that descriptive identifiers are incredibly useful!
Your code should not break even if a “reasonable” user enters invalid input.  So don’t forget to include input validation and thoroughly test your code.  You are welcome to keep your module’s test function but remove any print statements used to debug your code.
Each exercise needs to be in a separate module that includes appropriate headers (including your name and a description of your implementation) and comments throughout your code’s body.
Submit your programs by uploading your modules to your shared (H)ATCS Google Drive folder in a subfolder called Lab<number>.  You are responsible for checking that all of your modules are correctly uploaded.
You are welcome to write up your solutions to non-programming questions on paper then include an image of your written work in your doc.  If you choose this option, please make sure that you write clearly/your photo is clear enough for me to read easily.
The score earned on each exercise reflects its correctness/adherence to the specifications and readability, including clarity and helpfulness of comments.  Creativity is encouraged and much appreciated, but rarely affects your score. Remember that late submissions will be penalized 10% every 24 hours past the deadline, and you need to email me when this happens.
