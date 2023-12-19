{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": []
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "BT4TRBrEhhn3"
      },
      "outputs": [],
      "source": [
        "import random\n",
        "HANGMAN = [\n",
        "    '________',\n",
        "    '|       |',\n",
        "    '|       O',\n",
        "    '|       |',\n",
        "    '|      /|\\ ',\n",
        "    '|       |',\n",
        "    '|      / \\ '\n",
        "]\n",
        "\n",
        "WORDS = [\n",
        "    'casa', 'car', 'mono', 'elevator', 'python', 'java',\n",
        "    'pleasure', 'young', 'festival', 'sing', 'class'\n",
        "]\n",
        "word_to_guess = random.choice(WORDS)\n",
        "hangman = Hangman(word_to_guess)\n",
        "hangman.play()"
      ]
    }
  ]
}