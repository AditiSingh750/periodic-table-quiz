{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ade41977-7547-4245-8a40-d92a28b610cf",
   "metadata": {},
   "source": [
    "🧪 Periodic Table Quiz Game (Python)\n",
    "This notebook lets you play a fun 10-question quiz about elements from the periodic table. Answer each question to test your chemistry knowledge!"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "d80fd38d-dfef-403f-b580-f38fd0e0560e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import random\n",
    "from IPython.display import clear_output\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4c576886-f4e2-4677-bce1-ab6f43974fa9",
   "metadata": {},
   "outputs": [],
   "source": [
    "questions = {\n",
    "    \"What is the chemical symbol for gold?\": \"Au\",\n",
    "    \"What is the atomic number of oxygen?\": \"8\",\n",
    "    \"Which element has the symbol Na?\": \"Sodium\",\n",
    "    \"What is the lightest element?\": \"Hydrogen\",\n",
    "    \"Which element has 6 protons?\": \"Carbon\",\n",
    "    \"Which element is a noble gas with atomic number 10?\": \"Neon\",\n",
    "    \"What is the chemical symbol for iron?\": \"Fe\",\n",
    "    \"Which element has the atomic number 1?\": \"Hydrogen\",\n",
    "    \"Which element is liquid at room temperature and has symbol Hg?\": \"Mercury\",\n",
    "    \"What is the most abundant gas in Earth's atmosphere?\": \"Nitrogen\"\n",
    "}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "cd1fdbf5-7cd9-447d-a88f-cbca0eb18fa4",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "\n",
      "Question 1: What is the chemical symbol for gold?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer:  au\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct!\n",
      "\n",
      "Question 2: Which element has the symbol Na?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer:  sodium\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct!\n",
      "\n",
      "Question 3: What is the chemical symbol for iron?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer:  fe\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct!\n",
      "\n",
      "Question 4: What is the lightest element?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer:  hydrogen\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Correct!\n",
      "\n",
      "Question 5: Which element is liquid at room temperature and has symbol Hg?\n"
     ]
    },
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Your answer:  aditi\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "❌ Wrong! The correct answer is: Mercury\n",
      "\n",
      "🎯 Final Score: 4 out of 10\n"
     ]
    }
   ],
   "source": [
    "def quiz_game():\n",
    "    score = 0\n",
    "    question_list = list(questions.items())\n",
    "    random.shuffle(question_list)\n",
    "\n",
    "    for i, (question, correct_answer) in enumerate(question_list[:5]):\n",
    "        print(f\"\\nQuestion {i+1}: {question}\")\n",
    "        user_answer = input(\"Your answer: \").strip()\n",
    "\n",
    "        if user_answer.lower() == correct_answer.lower():\n",
    "            print(\"✅ Correct!\")\n",
    "            score += 1\n",
    "        else:\n",
    "            print(f\"❌ Wrong! The correct answer is: {correct_answer}\")\n",
    "\n",
    "    print(f\"\\n🎯 Final Score: {score} out of 10\")\n",
    "\n",
    "# Run the game\n",
    "quiz_game()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "534fc47b-59c8-4579-a047-aee1a5472192",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
